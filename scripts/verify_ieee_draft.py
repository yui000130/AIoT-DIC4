#!/usr/bin/env python3
r"""
Multibagger Scout (DIC4) -- IEEE Conference LaTeX & OpenSpec Automated Verifier
Checks:
  1. Overleaf pdfLaTeX hygiene (ASCII safety, brace/env balance, \input paths, \ref/\label match, stray markdown)
  2. BibTeX citation bijection (every \cite{} defined, zero uncited orphan entries)
  3. 7 DIC-3 Non-Negotiable Guardrails (G1-G7)
  4. IEEE Conference A-Z SOP Structural Checkpoints
Usage:
  python scripts/verify_ieee_draft.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OVERLEAF_DIR = ROOT / "overleaf"
MAIN_TEX = OVERLEAF_DIR / "main.tex"
BIB_FILE = OVERLEAF_DIR / "references.bib"


def strip_latex_comments(text: str) -> str:
    """Remove unescaped % comments line by line."""
    cleaned_lines = []
    for line in text.splitlines():
        out = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                break
            out.append(line[i])
            i += 1
        cleaned_lines.append("".join(out))
    return "\n".join(cleaned_lines)


def check_braces_and_envs(filepath: Path) -> list[str]:
    issues: list[str] = []
    raw = filepath.read_text(encoding="utf-8")

    # 1. Pure ASCII check (Overleaf pdfLaTeX safety)
    non_ascii = [(idx + 1, ch) for idx, line in enumerate(raw.splitlines()) for ch in line if ord(ch) > 127]
    if non_ascii:
        sample = ", ".join(f"L{ln}:{repr(ch)}" for ln, ch in non_ascii[:5])
        issues.append(f"{filepath.name}: non-ASCII chars found ({len(non_ascii)} total: {sample})")

    # 2. Detect likely unescaped percentage in prose (digit followed by unescaped %)
    for idx, line in enumerate(raw.splitlines(), start=1):
        # Ignore full comment lines
        if line.lstrip().startswith("%"):
            continue
        m = re.search(r"(?<!\\)\d%", line)
        if m:
            issues.append(f"{filepath.name}:L{idx} possible unescaped '%' after digit -> {line.strip()[:80]}")

    # 3. Detect stray single markdown backticks (ignore LaTeX `` opening quotes)
    no_comments = strip_latex_comments(raw)
    stray_bt = re.findall(r"(?<!`)`(?!`)", no_comments)
    if stray_bt:
        issues.append(f"{filepath.name}: found {len(stray_bt)} stray single backtick(s)")

    # 4. Brace balance (ignoring \{ and \})
    depth = 0
    for idx, line in enumerate(no_comments.splitlines(), start=1):
        i = 0
        while i < len(line):
            if line[i] == "\\" and i + 1 < len(line):
                i += 2
                continue
            if line[i] == "{":
                depth += 1
            elif line[i] == "}":
                depth -= 1
                if depth < 0:
                    issues.append(f"{filepath.name}:L{idx} unmatched closing brace '}}'")
                    depth = 0
            i += 1
    if depth != 0:
        issues.append(f"{filepath.name}: unbalanced braces (final depth={depth})")

    # 5. Environment balance (\begin{...} vs \end{...})
    stack: list[tuple[str, int]] = []
    for idx, line in enumerate(no_comments.splitlines(), start=1):
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", line):
            kind, env = m.group(1), m.group(2)
            if kind == "begin":
                stack.append((env, idx))
            else:
                if not stack:
                    issues.append(f"{filepath.name}:L{idx} unexpected \\end{{{env}}}")
                else:
                    top_env, top_ln = stack.pop()
                    if top_env != env:
                        issues.append(
                            f"{filepath.name}:L{idx} mismatched \\end{{{env}}} for \\begin{{{top_env}}} (L{top_ln})"
                        )
    for env, ln in stack:
        issues.append(f"{filepath.name}:L{ln} unclosed \\begin{{{env}}}")

    return issues


def main() -> int:
    if not MAIN_TEX.exists() or not BIB_FILE.exists():
        print("[ERROR] Missing overleaf/main.tex or overleaf/references.bib")
        return 2

    tex_files = [MAIN_TEX] + sorted((OVERLEAF_DIR / "figures").glob("*.tex"))
    main_raw = MAIN_TEX.read_text(encoding="utf-8")
    main_clean = strip_latex_comments(main_raw)
    bib_raw = BIB_FILE.read_text(encoding="utf-8")

    print("=== Multibagger Scout (DIC4) IEEE Conference Draft Verifier ===\n")

    # ------------------------------------------------------------------
    # Part 1: Overleaf LaTeX Syntax & File Integrity
    # ------------------------------------------------------------------
    print("[Part 1] Overleaf pdfLaTeX Syntax & Hygiene")
    syntax_issues: list[str] = []
    for tf in tex_files:
        syntax_issues.extend(check_braces_and_envs(tf))

    # Check \input{...} targets
    for inp in re.findall(r"\\input\{([^}]+)\}", main_clean):
        target = OVERLEAF_DIR / inp
        if not target.exists():
            syntax_issues.append(f"Missing \\input target: {inp}")

    # Check \ref{...} targets against \label{...}
    labels = set(re.findall(r"\\label\{([^}]+)\}", main_clean))
    refs = set(re.findall(r"\\ref\{([^}]+)\}", main_clean))
    missing_refs = sorted(refs - labels)
    if missing_refs:
        syntax_issues.append(f"Undefined \\ref target(s): {missing_refs}")

    # Check for unescaped underscore inside \texttt{...} outside $...$ math spans
    for m in re.finditer(r"\\texttt\{([^}]+)\}", main_clean):
        no_math = re.sub(r"\$[^$]*\$", "", m.group(1))
        if re.search(r"(?<!\\)_", no_math):
            syntax_issues.append(f"Unescaped '_' inside \\texttt{{{m.group(1)}}}")

    if not syntax_issues:
        print(f"  PASS | Checked {len(tex_files)} LaTeX files: pure ASCII, balanced braces/envs, valid \\input paths.")
    else:
        for iss in syntax_issues:
            print(f"  FAIL | {iss}")

    # ------------------------------------------------------------------
    # Part 2: BibTeX Citation Bijection
    # ------------------------------------------------------------------
    print("\n[Part 2] BibTeX Citation Integrity")
    cited_keys: set[str] = set()
    for grp in re.findall(r"\\cite\{([^}]+)\}", main_clean):
        for k in grp.split(","):
            k = k.strip()
            if k:
                cited_keys.add(k)
    bib_keys = set(re.findall(r"@\w+\{([^,\s]+)\s*,", bib_raw))

    missing_in_bib = sorted(cited_keys - bib_keys)
    uncited_in_bib = sorted(bib_keys - cited_keys)
    bib_ok = (len(missing_in_bib) == 0) and (len(uncited_in_bib) == 0) and (len(bib_keys) == 15)
    if bib_ok:
        print(f"  PASS | 15/15 BibTeX entries defined and cited with 100% bijection.")
    else:
        print(f"  FAIL | Bib entries={len(bib_keys)}, Missing={missing_in_bib}, Uncited={uncited_in_bib}")

    # ------------------------------------------------------------------
    # Part 3: 7 DIC-3 Non-Negotiable Guardrails (G1-G7)
    # ------------------------------------------------------------------
    print("\n[Part 3] DIC-3 Seven Non-Negotiable Guardrails (G1-G7)")
    guardrails = [
        (
            "G1 Universe (TWSE common stocks, Emerging Board excluded, bottom 10% turnover)",
            all(k in main_clean for k in ["TWSE", "Emerging Stock Board", "10\\%", "delisted"]),
        ),
        (
            "G2 Feature Scope (April-end, prior-year annual/revenue, 10 features + Industry)",
            all(
                k in main_clean
                for k in [
                    "Market Capitalization",
                    "FCF Yield",
                    "Book-to-Market",
                    "Price-to-Earnings",
                    "ROE",
                    "Gross Margin",
                    "Annual Revenue Growth",
                    "OCF / Net Income",
                    "Debt Ratio",
                    "Trailing 12M Return",
                    "Industry Category",
                ]
            ),
        ),
        (
            "G3 Domain Rules (Exactly 2 red flags: Earnings Quality & Extreme Valuation)",
            all(k in main_clean for k in ["Earnings Quality Red Flag", "Extreme Valuation Red Flag"]),
        ),
        (
            "G4 Labels & Terminal Window (20 trading days, y_main, y_raw, UNKNOWN never 0)",
            all(k in main_clean for k in ["20", "y\\_main", "y\\_raw", "UNKNOWN"]),
        ),
        (
            "G5 Agent 7 Whitelisted Tools (exact names, max_calls=12, 3-round verify_report)",
            all(
                k in main_clean
                for k in [
                    "analyze\\_stock",
                    "get\\_features",
                    "score\\_model",
                    "find\\_cases",
                    "check\\_rules",
                    "follow\\_up",
                    "verify\\_report",
                    "max\\_calls",
                    "template\\_report",
                ]
            ),
        ),
        (
            "G6 Model Score Terminology (model score, never upside probability prior to calibration)",
            "model score" in main_clean.lower() and "never" in main_clean.lower() and "probabilit" in main_clean.lower(),
        ),
        (
            "G7 Honest Data-Stage Metrics (1,322 / 9,256 / 7,754 / 1.7% / 8/8 / 8201 / 214/214 / pending E1-E4)",
            all(
                k in main_clean
                for k in ["1,322", "9,256", "7,754", "1.7\\%", "8201", "214", "Pending"]
            )
            and ("8/8" in main_clean or "8 / 8" in main_clean),
        ),
    ]
    g_pass = 0
    for label, ok in guardrails:
        print(f"  {'PASS' if ok else 'FAIL'} | {label}")
        if ok:
            g_pass += 1

    # ------------------------------------------------------------------
    # Part 4: IEEE Conference A-Z SOP Structural Checkpoints
    # ------------------------------------------------------------------
    print("\n[Part 4] IEEE Conference A-Z SOP Structural Checkpoints (8 Checks)")
    a2z = [
        (
            "[IEEEtran + A-F] Conference class, abstract, keywords & 2025-2026 empirical evidence",
            "\\documentclass[conference]{IEEEtran}" in main_clean
            and all(k in main_clean for k in ["\\begin{abstract}", "\\begin{IEEEkeywords}", "14.83", "46 firms", "SPIVA", "FAITH", "Alpha Arena", "88\\%"]),
        ),
        (
            "[L] Introduction ends with Paper Organization paragraph",
            "The remainder of this paper is organized as follows" in main_clean,
        ),
        (
            "[O] Related Work 4x5 Literature Comparison Matrix (Table I)",
            "\\label{tab:related_work}" in main_clean and "4$\\times$5" in main_clean,
        ),
        (
            "[PM] Formal Math Equations (1)-(6): Wealth, 20-day return, ratio k, dual labels, walk-forward",
            all(
                f"\\label{{{lbl}}}" in main_clean
                for lbl in ["eq:wealth", "eq:return", "eq:ratio_k", "eq:yraw", "eq:ymain", "eq:walkforward"]
            ),
        ),
        (
            "[T] Hyperparameter Tuning Table (max_depth, num_leaves, learning_rate, kNN)",
            "\\label{tab:tuning}" in main_clean
            and all(k in main_clean for k in ["max\\_depth", "num\\_leaves", "learning\\_rate"]),
        ),
        (
            "[PI & PJ] Algorithms 1 & 2 + TSMC 2330 Step-by-Step Run-Through",
            all(k in main_clean for k in ["\\label{alg:agent}", "\\label{alg:dataset}", "2330 TSMC", "2019-04-30"]),
        ),
        (
            "[6.2 + Figs] Completed Data Validation Table, E1-E4 Criteria Table, & 2 Native TikZ Figures",
            all(
                k in main_clean
                for k in [
                    "\\label{tab:data_validation}",
                    "\\label{tab:experiments}",
                    "\\label{fig:architecture}",
                    "\\label{fig:walkforward}",
                ]
            ),
        ),
        (
            "[W-Z] Independent Conclusion and Future Work Section",
            "\\section{Conclusion and Future Work}" in main_clean,
        ),
    ]
    a_pass = 0
    for label, ok in a2z:
        print(f"  {'PASS' if ok else 'FAIL'} | {label}")
        if ok:
            a_pass += 1

    print("\n=== Summary ===")
    print(f"  Syntax & Hygiene : {'PASS' if not syntax_issues else f'FAIL ({len(syntax_issues)} issues)'}")
    print(f"  BibTeX Bijection : {'PASS' if bib_ok else 'FAIL'} ({len(cited_keys)} cited / {len(bib_keys)} defined)")
    print(f"  Guardrails G1-G7 : {g_pass}/{len(guardrails)}")
    print(f"  A-Z Checkpoints  : {a_pass}/{len(a2z)}")

    all_ok = (not syntax_issues) and bib_ok and (g_pass == len(guardrails)) and (a_pass == len(a2z))
    if all_ok:
        print("\nALL CHECKS PASSED: Overleaf IEEE Conference draft is verified and ready.")
        return 0
    print("\nVERIFICATION FAILED: Please inspect FAIL items above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
