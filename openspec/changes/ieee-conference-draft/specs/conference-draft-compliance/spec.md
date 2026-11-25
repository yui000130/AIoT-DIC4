# Delta Specification: IEEE Conference Draft & MCP Compliance (`conference-draft-compliance`)

## ADDED Requirements

### Requirement: IEEEtran Conference LaTeX Draft with Native Vector Diagrams
The workspace SHALL provide a complete Overleaf-ready `overleaf/` directory containing `main.tex` (`\documentclass[conference]{IEEEtran}`), `references.bib` (15 verified BibTeX entries), and native TikZ vector diagrams (`figures/architecture_tikz.tex`, `figures/walkforward_tikz.tex`) plus a packaged `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip` archive with `main.tex` at the archive root.

#### Scenario: Author Placeholder Editability
- **WHEN** the user opens `overleaf/main.tex` in Overleaf or a local editor
- **THEN** author name, affiliation, and email placeholders are clearly delimited with `% TODO` comments inside `\author{\IEEEauthorblockN{...}}` so the user can update them without modifying paper layout or content.

---

### Requirement: Overleaf MCP & GitHub MCP Configuration Blueprint
The repository SHALL include `mcp/mcp_config.example.json` (using placeholder environment variables—never hardcoded secrets or session cookies) and `mcp/OVERLEAF_MCP_GUIDE.md` documenting both free-tier real-time MCP synchronization and Git-bridge MCP workflows.

#### Scenario: Zero-Secret Repository Hygiene
- **WHEN** the repository is committed and pushed to GitHub
- **THEN** no Overleaf session cookies, Git tokens, or personal credentials exist in tracked files, and `.gitignore` excludes `_ref_dic3/`, LaTeX build artifacts, and `.env` files.

---

### Requirement: Automated IEEE LaTeX & DIC-3 Guardrail Verification
The repository SHALL provide `scripts/verify_ieee_draft.py` validating LaTeX syntax balance, BibTeX key integrity, all 7 DIC-3 Guardrails (G1–G7), and A–Z IEEE conference checkpoints in a single deterministic run.

#### Scenario: Full Verification Pass
- **WHEN** `python scripts/verify_ieee_draft.py` is executed
- **THEN** it exits with status code `0` reporting 100% PASS across LaTeX syntax, BibTeX bijection, 7/7 Guardrails, and all A–Z checkpoints.
