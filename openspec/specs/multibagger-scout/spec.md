# Multibagger Scout System Specification (Synchronized from `DESIGN.md` v0.6)

本規格檔為 *Multibagger Scout* 系統本體之單一真實來源（Single Source of Truth），供 DIC4 IEEE Conference 論文與後續程式實作共同遵循。

---

## 1. System Architecture (Eight Modules)

1. **Module 1 — User / Application Scenario**: Retail investors and finance students interacting via Streamlit (`app.py`).
2. **Module 2 — Query / Input**: Stock ticker (`stock_id`) and decision date `t` (aligned to the last trading day of April).
3. **Module 3 — Planner & Reasoning Agent**: LLM planner selecting strictly from 7 whitelisted deterministic tools (`max_calls = 12`).
4. **Module 4 — Data Acquisition (FinMind)**: Point-in-time retrieval of prior-year annual financial statements (Dec 31), prior-year Jan–Dec monthly revenues, and daily prices/corporate actions on or before `t`.
5. **Module 5 — Analytics Engine**: Computes 10 fixed features + industry category, runs LightGBM (and Logistic Regression baseline) to produce an uncalibrated **model score**, computes SHAP feature attributions, and retrieves $k$NN historical cases strictly restricted to outcomes resolved by `t` ($\tau \le t - 5\text{Y}$).
6. **Module 6 — Domain Knowledge Integration**: Evaluates exactly 2 deterministic red-flag rules (`Earnings Quality Red Flag` and `Extreme Valuation Red Flag`) using training-window quantile thresholds and static literature notes in `knowledge/`.
7. **Module 7 — Decision / Recommendation**: Synthesizes potential tier, model score vs. training-period base rate, supporting/opposing evidence, and historical cases into a structured evidence bundle `T`.
8. **Module 8 — Verification & Output**: Runs `verify_report(R, T)` for up to 3 revision rounds checking entities, dates, units, values, and `evidence_id` provenance; falls back to deterministic `template_report(T)` on exhaustion.

---

## 2. Formal Requirements & Scenarios

### Requirement: Point-in-Time Universe & Feature Scope (G1, G2)
The system SHALL evaluate only TWSE-listed common stocks (4-digit non-zero prefix, including subsequently delisted firms; excluding 9-prefix TDRs, ETFs, preferred shares, TPEx/OTC stocks, and Emerging Stock Board periods), listed for at least one year as of feature date `t` (last trading day of April), and excluding the bottom 10% by prior-year average daily trading value. Features SHALL consist solely of 10 numerical metrics plus Industry Category computed strictly from prior-year (year $y-1$) annual reports, prior-year Jan–Dec monthly revenues, and prices $\le t$.

#### Scenario: Emerging Stock Board Exclusion
- **WHEN** a stock has $\ge 5$ trading days within the 90 calendar days preceding feature date `t` whose OHLC prices violate official TWSE tick-size increments
- **THEN** that firm-year is classified as trading on the Emerging Stock Board and excluded from $\mathcal{U}_t$ (394 firm-years excluded across 2013–2020).

#### Scenario: Fixed 10-Feature Set
- **WHEN** `get_features(stock_id, as_of=t)` is called
- **THEN** it computes exactly: (1) Market Capitalization (with capital-reduction share-ratio $k$ adjustment), (2) FCF Yield, (3) Book-to-Market (B/M), (4) Price-to-Earnings (P/E), (5) ROE, (6) Gross Margin, (7) Annual Revenue Growth, (8) Operating Cash Flow / Net Income (OCF/NI), (9) Debt Ratio, (10) Trailing 12-Month Adjusted Return, plus Industry Category. Deleted v0.4 features (`ROA`, `EBITDA margin`, `asset growth`, `volatility`, `dividend yield`) SHALL NOT appear.

---

### Requirement: Wealth-Preserving Return & Dual-Label Construction (G4)
The system SHALL compute a daily wealth-preserving adjusted wealth sequence $W_{i, t \to d}$ chaining dividend/rights ex-dates, capital reductions (both cash and loss-offsetting), and stock splits, define the 5-year return $r_{i,t}$ using the arithmetic mean of the final 20 trading days of $W_{i, t \to d}$, and assign dual labels `y_raw` (top $\lceil 0.05 N_t \rceil$) and `y_main` (`y_raw = 1` AND 5-year revenue CAGR $\ge 10\%$).

#### Scenario: Honest `UNKNOWN` Label Handling
- **WHEN** a firm-year exhibits a single-day adjusted wealth move exceeding TWSE daily price limits (7% pre-June 2015, 10% thereafter), an IFRS 2012→2013 revenue jump $> 3\times$, or delists before completing 5 years so revenue CAGR is indeterminate
- **THEN** the label is assigned `UNKNOWN` and excluded from training and primary evaluation—NEVER coerced to negative (`0`).

---

### Requirement: Non-Overlapping Walk-Forward Split & PoT Verification (G3, G5, G6)
Training windows and $k$NN case libraries SHALL satisfy $a_{i,y} = t_y + 5\text{Y} \le t_{\text{test}}^{(k)}$ across three rounds (2013→2018, 2013–2014→2019, 2013–2015→2020). The Agent SHALL invoke only the 7 whitelisted tools (`analyze_stock`, `get_features`, `score_model`, `find_cases`, `check_rules`, `follow_up`, `verify_report`) with `max_calls = 12`, report uncalibrated scores strictly as **model score** (never probability), and enforce up to 3 rounds of `verify_report(R, T)` before `template_report(T)` fallback.
