# OpenSpec Tasks: DIC4 IEEE Conference Overleaf Draft & GitHub OpenSpec

## Phase 1: OpenSpec Foundation & Specification Setup (Deliverable 2)
- [x] **1.1** Sync DIC-3 core context (`A–F`, `5 Cores`, `3 Trade-offs`, `10 Details`, 7 Guardrails) into `openspec/project.md` and `openspec/specs/multibagger-scout/spec.md`.
- [x] **1.2** Author `openspec/AGENTS.md` defining the OpenSpec + Overleaf MCP + GitHub MCP workflow.
- [x] **1.3** Author `openspec/specs/ieee-conference-paper/spec.md` and active change artifacts (`proposal.md`, `design.md`, `tasks.md`, `specs/conference-draft-compliance/spec.md`).

## Phase 2: IEEE Conference LaTeX Draft for Overleaf (Deliverable 1)
- [x] **2.1** Create complete verified BibTeX bibliography `overleaf/references.bib` (15 citations `[1]–[15]`).
- [x] **2.2** Create native TikZ vector diagrams: `overleaf/figures/architecture_tikz.tex` (8-module PoT + 7-tool whitelist + 3-round verification) and `overleaf/figures/walkforward_tikz.tex` (2013–2020 3-round non-overlapping walk-forward timeline).
- [x] **2.3** Author full `\documentclass[conference]{IEEEtran}` paper in `overleaf/main.tex` with editable author placeholders, covering all A–Z checkpoints, Equations (1)–(6), Tables I–V, Algorithms 1 & 2, and TSMC 2330 run-through.

## Phase 3: MCP Integration & Automation Scripts
- [x] **3.1** Provide `mcp/mcp_config.example.json` and `mcp/OVERLEAF_MCP_GUIDE.md` covering free-tier Overleaf MCP (`@netique/overleaf-mcp`), Git-bridge MCP (`OverleafMCP`), and GitHub MCP.
- [x] **3.2** Implement `scripts/verify_ieee_draft.py` (LaTeX balance, BibTeX bijection, 7 Guardrails G1–G7, A–Z checkpoints) and verify 100% PASS.
- [x] **3.3** Implement `scripts/build_overleaf_zip.py` and generate `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip`.

## Phase 4: Local Git Commit & User Final Handoff
- [x] **4.1** Initialize clean Git repository in `DIC4/` (excluding `_ref_dic3/` via `.gitignore`), write comprehensive `README.md`, and create clean initial commit.
- [ ] **4.2** *(User action)* Fill in author name, affiliation, and email in `overleaf/main.tex` (marked with `TODO: Fill in author info`).
- [ ] **4.3** *(User action)* Upload `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip` to Overleaf (or sync via Overleaf MCP) and click **Recompile** to generate the final PDF.
- [ ] **4.4** *(User action)* Add your new GitHub remote (`git remote add origin <URL>`) and run `git push -u origin main`.
