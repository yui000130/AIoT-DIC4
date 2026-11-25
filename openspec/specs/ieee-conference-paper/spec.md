# IEEE Conference Paper Specification (`ieee-conference-paper`)

本規格定義 *Multibagger Scout* IEEE 研討會論文初稿（`overleaf/`）在格式、章節結構、數學表達、圖表設計、引用管理與防走歪紅線上必須滿足之正式要求。

---

## 1. Document Class & Overleaf Build Compatibility

### Requirement: Standard `IEEEtran` Conference Format & Zero-Dependency pdfLaTeX Build
The manuscript `overleaf/main.tex` SHALL use `\documentclass[conference]{IEEEtran}` and compile cleanly on Overleaf using standard `pdfLaTeX` + `BibTeX` (`\bibliographystyle{IEEEtran}`) without requiring CJK engines (`XeLaTeX`/`LuaLaTeX`) or external proprietary style files.

#### Scenario: One-Click Overleaf Upload & Compilation
- **WHEN** a user uploads `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip` (or syncs `overleaf/` via Overleaf MCP) to Overleaf and clicks **Recompile**
- **THEN** `main.tex` compiles with standard TeX Live packages (`amsmath`, `amssymb`, `algorithm`, `algpseudocode`, `booktabs`, `tabularx`, `tikz`, `cite`, `hyperref`), renders both native TikZ vector diagrams, and resolves all 15 BibTeX references cleanly.

---

## 2. A–Z SOP Paper Structure & Content Requirements

### Requirement: Complete A–Z Academic Conference Architecture
The IEEE conference manuscript SHALL cover all 26 A–Z SOP checkpoints in academic English:
1. **Title, Author Block (editable placeholders), Abstract (`A–F`) & IEEE Keywords**: Exact IEEE conference formatting using `\begin{abstract}` and `\begin{IEEEkeywords}`.
2. **Section I — Introduction (`G–L`)**: Market participation & extreme wealth concentration (`G`), four structural challenges (`H`), dual-axis literature context (`I`), research gaps (`J`), research questions RQ1–RQ3 & three core contributions (`K`), and explicit paper organization paragraph (`L`).
3. **Section II — Related Work (`M–O`)**: Structured dual-axis review covering domain multibagger studies, ML asset pricing, financial LLMs/multi-agent systems, and PoT numerical verification (`M`), explicit novelty positioning (`N`), and a full-width **4×5 Literature Comparison Matrix** (`O`).
4. **Section III — Proposed System: Multibagger Scout (`PA–PM`)**:
   - System overview & 8-module architecture diagram (Fig. 1, TikZ).
   - Point-in-Time universe, fixed 10 features + industry table, and formal LaTeX mathematical formulations (`[PM-1]` wealth-preserving return $W_{i,t\to d}$, 20-day terminal average $r_{i,t}$, capital-reduction ratio $k$, dual labels $y_{\text{raw}}, y_{\text{main}}$; `[PM-2]` walk-forward isolation $\mathcal{D}_{\text{train}}^{(k)} = \mathcal{C}^{(k)}$ with $a_{i,y} \le t_{\text{test}}^{(k)}$).
   - Analytics engine, 2 domain red-flag rules, and hyperparameter tuning table (`[T]`).
   - PoT 7-tool whitelist, **Algorithm 1** (Agent Main Execution & 3-Round Verification Loop) and **Algorithm 2** (Point-in-Time Dataset & Dual-Label Construction).
   - End-to-end step-by-step run-through (`[PJ]`: TSMC 2330 on `2019-04-30`).
5. **Section IV — Data Validation & Experimental Protocol (`Q–V`, `[6.2]`)**:
   - Completed data-stage validation results table (1,322 stocks, 9,256 tasks / 0% failure, 7,754 firm-years, anomaly rate 14.7% → 1.7%, 8/8 TSMC cross-check, 8201 NT\$8,690 cash capital reduction check, 214/214 TWSE share-ratio check).
   - Walk-forward timeline diagram (Fig. 2, TikZ) and E1–E5 evaluation protocol with quantitative validation criteria table (`[6.2]`), explicitly marked as pending hypotheses with zero fabricated results.
   - Concise summary of key limitations & research ethics/disclaimer.
6. **Section V — Conclusion & Future Work (`W–Z`)**: Summarizes problem/method (`W`), key advantages (`X`), completed data-stage yields (`Y`), and future work (`Z`).
7. **References**: Complete `references.bib` with all 15 verified citations (`[1]–[15]`), every reference cited in text and zero undefined citations.

---

## 3. Guardrail & Verification Requirement

### Requirement: Automated Pre-Sync Compliance Audit
Before syncing `overleaf/` via MCP or pushing to GitHub, `python scripts/verify_ieee_draft.py` SHALL verify:
- Balanced LaTeX environments (`\begin{...}` / `\end{...}`) and braces
- 100% BibTeX key bijection between `\cite{...}` in `main.tex` and entries in `references.bib`
- 7/7 DIC-3 Guardrails (G1–G7) pass
- All A–Z structural checkpoints pass
