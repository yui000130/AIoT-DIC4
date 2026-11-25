# Change Proposal: IEEE Conference Overleaf Draft via MCP & OpenSpec (`ieee-conference-draft`)

## 1. Why（變更動機與背景）
在 **DIC3 (`yui000130/DIC-3-project-refactor`)** 中，我們已依據 2020 A–Z SOP 與 `DESIGN.md` v0.6 完成 *Multibagger Scout* 的 OpenSpec 規格重構、中英文摘要、Introduction（G–L）、Related Work（M–O, 4×5 矩陣）、數學定義式（`[PM]`）、超參數表（`[T]`）、2330 台積電端到端案例（`[PJ]`）、E1–E4 量化驗證判準（`[6.2]`）與結論（`[W–Z]`）。

然而，DIC3 的產出以中文 Markdown 規格與修補範本為主，尚未整合為可直接於 **Overleaf** 編譯投稿之 **IEEE Conference 雙欄英文 LaTeX 論文初稿**，亦缺少 **MCP（Overleaf MCP / GitHub MCP）** 協作同步與自動化 LaTeX／紅線檢核管線。

為完成 **DIC4：Overleaf Draft for Conference using MCP and OpenSpec** 兩大作業標的：
1. **Overleaf Draft for IEEE Conference**：將完整 A–Z 規格轉譯、精煉並排版為標準 `\documentclass[conference]{IEEEtran}` 英文論文專案（含 TikZ 向量圖、BibTeX 文獻庫與 Overleaf 一鍵匯入 `.zip`）。
2. **OpenSpec on GitHub**：建立可追蹤、可重現、可自動檢核的 OpenSpec 規格庫與 MCP 設定範本，推送至 GitHub 進行版本控制。

---

## 2. What Changes（變更內容）
1. **建立 IEEE Conference 論文正式規格（`openspec/specs/ieee-conference-paper/spec.md`）**：
   - 定義 `IEEEtran` 雙欄格式、純英文 `pdfLaTeX + BibTeX` 零相依編譯規範、A–Z 章節對照與 7 大紅線（G1–G7）防走歪規則。
2. **撰寫完整 Overleaf IEEE 會議論文專案（`overleaf/`）**：
   - `overleaf/main.tex`：涵蓋 Title/Author Placeholders、Abstract (`A–F`)、Keywords、Sections I–V（Introduction `G–L`、Related Work `M–O` + 4×5 Matrix、Proposed System `PA–PM` + Math + Algorithms 1 & 2 + TSMC 2330 Run-Through、Data Validation & Experimental Protocol `Q–V` + `[T]` + `[6.2]` + Limitations、Conclusion `W–Z`）。
   - `overleaf/references.bib`：15 篇驗證過之 IEEE BibTeX 引用條目（對應 DIC3 `[1]–[15]`）。
   - `overleaf/figures/architecture_tikz.tex` & `walkforward_tikz.tex`：兩張原生 TikZ 向量圖（八大模組 PoT 與 3 輪核對流程圖；2013–2020 三輪不重疊 Walk-Forward 時間軸圖）。
   - `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip`：一鍵上傳 Overleaf 壓縮包。
3. **建置 Overleaf MCP & GitHub MCP 接軌配置（`mcp/`）**：
   - `mcp/mcp_config.example.json`：涵蓋免費版 Overleaf（`@netique/overleaf-mcp`）、付費版 Git-Bridge（`OverleafMCP`）與 GitHub MCP 之標準客戶端設定範本。
   - `mcp/OVERLEAF_MCP_GUIDE.md`：完整安裝、連線、同步與編譯排錯指南。
4. **建立自動化檢核與打包工具（`scripts/`）**：
   - `scripts/verify_ieee_draft.py`：驗證 LaTeX 環境與括號平衡、BibTeX 鍵值雙向一致、7 大防走歪紅線（G1–G7）及 A–Z 會議論文必備項目。
   - `scripts/build_overleaf_zip.py`：自動打包 `overleaf/` 為根目錄含 `main.tex` 之 Overleaf ZIP。

---

## 3. Impact（影響範圍）
- **Affected Specs**: `multibagger-scout`, `ieee-conference-paper`, `conference-draft-compliance`
- **Artifacts Created**: `overleaf/**`, `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip`, `mcp/**`, `openspec/**`, `scripts/**`, `README.md`
- **Guardrail Guarantee**: 100% 繼承並嚴格遵守 DIC3 `DESIGN.md` v0.6 之 7 大紅線，不編造任何 E1–E4 實驗數值。
