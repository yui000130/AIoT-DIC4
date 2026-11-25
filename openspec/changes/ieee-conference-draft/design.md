# Design Blueprint: IEEE Conference Overleaf Draft & MCP Pipeline

## 1. IEEE Conference Paper Architecture & Page Budget (Target: 6–8 Pages Double-Column)

| Paper Section | A–Z Checkpoints | Key Elements (Tables / Figures / Algorithms / Equations) | Source Alignment (DIC-3) |
| :--- | :--- | :--- | :--- |
| **Title, Authors, Abstract, Keywords** | `A–F` | Editable IEEE `\IEEEauthorblockN` placeholders; IEEE conference abstract; 8 Index Terms | `ieee_abstract_and_cores.md` §1 |
| **I. Introduction** | `G–L` | `G` (14.83M accounts, 46/29,754 firms, TSMC >40%); `H` (SPIVA 79%/0%, 30–100% bias, FAITH 10–20%+, Alpha Arena 31/38); `I–J`; `K` (RQ1–RQ3 + 3 contributions); `L` (organization) | `introduction_refactor.md` |
| **II. Related Work** | `M–O` | Dual-axis review (Domain Factors, ML Asset Pricing, Financial LLMs, PoT Verification); Novelty (`N`); **Table I: 4×5 Literature Comparison Matrix (`O`)** | `related_work_refactor.md` |
| **III. Proposed System** | `PA–PM`, `[T]`, `[PJ]` | **Fig. 1** (`architecture_tikz.tex`, 8 modules + 7 tools + 3-round loop); **Table II** (Fixed 10 Features + Industry); **Eqs. (1)–(6)** (`[PM-1]` wealth return, 20-day mean, ratio $k$, dual labels; `[PM-2]` walk-forward isolation); **Table III** (Hyperparameter Tuning `[T]`); **Algorithms 1 & 2**; TSMC 2330 Step-by-Step Run-Through (`[PJ]`) | `spec.md`, `templates.md` §2–4 |
| **IV. Data Validation & Experimental Protocol** | `Q–V`, `[6.2]` | **Table IV** (Completed Data-Stage Empirical Validation: 1,322 stocks, 9,256 tasks, 7,754 firm-years, 14.7%→1.7%, 8/8 TSMC, 8201 NT\$8,690, 214/214 ratio); **Fig. 2** (`walkforward_tikz.tex`, 2013–2020 3-round split); **Table V** (E1–E4 Quantitative Validation Criteria `[6.2]`, explicitly pending); Key Limitations & Disclaimer | `templates.md` §5, `project.md` |
| **V. Conclusion & Future Work** | `W–Z` | `W` (problem/PoT recap), `X` (advantages), `Y` (data-stage yields), `Z` (future work & disclaimer) | `templates.md` §6 |
| **References** | `[1]–[15]` | Complete `references.bib` formatted with `\bibliographystyle{IEEEtran}` | `templates.md` §7 + verified bibliographic records |

---

## 2. Overleaf Compilation & Visual Polish Decisions
1. **Pure English pdfLaTeX Compilation**: Zero CJK characters inside `overleaf/main.tex` and `overleaf/references.bib`, guaranteeing 100% zero-error compilation on Overleaf's default `pdfLaTeX` engine.
2. **Native Vector TikZ Figures**: Both Fig. 1 (8-module PoT architecture) and Fig. 2 (3-round non-overlapping walk-forward timeline) are authored in pure TikZ wrapped inside `\resizebox{\textwidth}{!}{...}` inside `figure*` environments—crisp vector PDF rendering at any zoom level with zero broken image paths or margin overflows.
3. **Full-Width `table*` with `booktabs` & `tabularx`**: Wide tables (Table I 4×5 Matrix, Table III Hyperparameters, Table V E1–E4 Criteria) use `table*` spanning both columns with `p{...}`/`X` ragged-right wrapping to eliminate `Overfull \hbox` warnings.
4. **Honest Proposal/Data-Validation Framing (G7)**: Section IV clearly separates **Section IV-A (Completed Data-Stage Validation)** from **Section IV-B (Pending Walk-Forward & Agent Evaluation Protocol)** so reviewers see verified numbers with zero fabricated claims.

---

## 3. MCP & OpenSpec Synchronization Pipeline

```text
[OpenSpec Specs & Changes]
   openspec/specs/ieee-conference-paper/spec.md
   openspec/changes/ieee-conference-draft/{proposal,design,tasks}.md
          │
          ▼ (Spec-Driven Authoring)
[Overleaf LaTeX Source]
   overleaf/main.tex + references.bib + figures/*.tex
          │
          ▼ (Automated Audit & Packaging)
   python scripts/verify_ieee_draft.py   --> Syntax + BibTeX + 7 Guardrails + A–Z PASS
   python scripts/build_overleaf_zip.py  --> dist/MultibaggerScout_IEEE_Conference_Overleaf.zip
          │
          ├──────────────────────────► Overleaf (via Overleaf MCP or ZIP Upload)
          └──────────────────────────► GitHub   (via Git CLI or GitHub MCP)
```
