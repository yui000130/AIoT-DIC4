# Change 004: Experiment (Q–V)

## Goal
Maintain Section IV (Experiments) of `ICEIB paper/main.tex` following items Q–V of the A-to-Z SOP. Rewritten 2026-11-26 with the completed E1–E4 results from `results/` of the MultibaggerScout-AIagent repository.

## Affected Sections
- `ICEIB paper/main.tex`: `\section{Experiments}`, Tables II–IV

## A–Z Checklist Mapping
- **Q (Metrics):** Precision@20/50, Recall@50 and PR-AUC against each round's positive rate; 5-year gross return and maximum drawdown; quintile positive rates and SHAP stability; numerical accuracy, required-field coverage, evidence citation rate, template fallback.
- **R (Compared methods):** LightGBM, logistic regression (rank-transformed), low P/B, high ROE, Yartseva-inspired rule, 1,000 random rankings, 0050, a direct LLM with the same raw data.
- **S (Setup):** Rounds train 2013 / 2013–2014 / 2013–2015 → test 2018 / 2019 / 2020 (training labels must resolve before the test date); overlapping test windows are reported per round.
- **T (Parameters):** Fixed settings table; no tuning (17 positives in round 1 leave no room for time-ordered validation).
- **U (Results):** E1 table, E2 returns, E3 associations, E4 table.
- **V (Verify):** Pre-specified criteria (beyond the random 95th percentile; bootstrap CI excluding 0) and threats to validity.
