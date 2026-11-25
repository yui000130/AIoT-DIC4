# Change 006: References (IEEE Format)

## Goal
Maintain and verify all IEEE-formatted bibliography entries (`\bibitem{b1}`–`\bibitem{b15}`) in `ICEIB paper/main.tex` against `Multibagger Scout A–F 最新研究證據補強.md`.

## Affected Sections
- `ICEIB paper/main.tex`: `\begin{thebibliography}{99}...\end{thebibliography}`

## Verification Criteria
- All citations `[1]`–`[15]` match verified sources (Bessembinder 2026, SPIVA 2025, Lopez-Lira & Tang JFE 2026, FAITH, ABFER 2026, Economics Letters 2025, Alpha Arena, TradingAgents v5, Agentic RAG PoT 2026, Yartseva 2025/HKEJ, CNA, Focus Taiwan, CommonWealth, pitbacktest).
- All `\cite{...}` keys in `main.tex` resolve with zero undefined citations in Overleaf.
