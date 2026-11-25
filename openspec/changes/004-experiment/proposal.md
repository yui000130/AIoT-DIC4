# Change 004: Experiment (Q–V)

## Goal
Maintain and refine Section 4 (Experimental Design and Evaluation Protocol) of `ICEIB paper/main.tex` following items Q–V of the A-to-Z SOP.

## Affected Sections
- `ICEIB paper/main.tex`: `\section{Experimental Design and Evaluation Protocol}` (4.1–4.4)

## A–Z Checklist Mapping
- **Q (Quality & Quantity):** Precision@K (K=10, 20, 50), Recall@50, PR-AUC, MDD, Report Numerical Accuracy & Evidence Coverage.
- **R (Related methods to compare):** LightGBM, L2 Logistic Regression, Single-Factor Rules (Low P/B, High ROE), 0050 ETF, Random (<=5%), Direct-LLM.
- **S (Simulation Setup):** 2013–2020 feature window, 3-round expanding walk-forward (2018-04-30, 2019-04-30, 2020-04-30), regime boundary discussion (2023–2026 AI cycle).
- **T (Tuning parameters):** Time-ordered CV search space within training windows only; zero tuning on test folds.
- **U–V (Useful results & Verify effectiveness):** Currently documents `verify_data.py` feasibility and FinMind delisted-stock audit plan; replace with backtest tables and statistical significance tests once experiments complete.
