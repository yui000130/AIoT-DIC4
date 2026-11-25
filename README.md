# DIC4: Multibagger Scout — IEEE Conference Overleaf Draft using MCP & OpenSpec

延續 [DIC-3-project-refactor](https://github.com/yui000130/DIC-3-project-refactor.git) 之 *Multibagger Scout*（台股潛力股探勘 Domain AI Agent，`DESIGN.md` v0.6）A–Z SOP 規格重構，本儲存庫透過 **OpenSpec（Spec-Driven Development）** 與 **MCP（Overleaf MCP + GitHub MCP）** 完成 **DIC4 兩項核心交付標的**：

1. **Overleaf Draft for IEEE Conference**：標準雙欄 `\documentclass[conference]{IEEEtran}` 英文會議論文專案（`overleaf/`），內建兩張原生 TikZ 向量圖、15 篇驗證過之 BibTeX 文獻，並打包為可直接上傳 Overleaf 編譯的 `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip`。
2. **OpenSpec on GitHub**：完整的規格驅動開發目錄（`openspec/`）、Overleaf/GitHub MCP 設定範本與指南（`mcp/`），以及自動化 LaTeX／BibTeX／7 大紅線檢核腳本（`scripts/verify_ieee_draft.py`）。

---

## 📋 DIC4 作業需求對照表

| 作業要求項目 | 對應檔案與連結 | 內容摘要 |
| :--- | :--- | :--- |
| **1. Overleaf Draft for IEEE Conference** | [overleaf/main.tex](overleaf/main.tex)<br/>[overleaf/references.bib](overleaf/references.bib)<br/>[overleaf/figures/architecture_tikz.tex](overleaf/figures/architecture_tikz.tex)<br/>[overleaf/figures/walkforward_tikz.tex](overleaf/figures/walkforward_tikz.tex)<br/>[dist/MultibaggerScout_IEEE_Conference_Overleaf.zip](dist/MultibaggerScout_IEEE_Conference_Overleaf.zip) | 完整雙欄 IEEE Conference LaTeX 論文（涵蓋 `A–F` 摘要、`G–L` 緒論、`M–O` 4×5 文獻矩陣、數學式 Eqs. (1)–(6)、`[T]` 超參數表、Algorithm 1 & 2、`[PJ]` 2330 台積電端到端案例、已完成資料層驗證結果、`[6.2]` E1–E4 評估協定、`W–Z` 結論與 15 篇 IEEE BibTeX 引用）。作者欄已標註 `% TODO:` 方便自行填入。 |
| **2. OpenSpec on GitHub** | [openspec/project.md](openspec/project.md)<br/>[openspec/AGENTS.md](openspec/AGENTS.md)<br/>[openspec/specs/multibagger-scout/spec.md](openspec/specs/multibagger-scout/spec.md)<br/>[openspec/specs/ieee-conference-paper/spec.md](openspec/specs/ieee-conference-paper/spec.md)<br/>[openspec/changes/ieee-conference-draft/](openspec/changes/ieee-conference-draft/) | 完整 OpenSpec 規格庫（全局脈絡、AI Agent 指南、系統本體規格、IEEE 論文格式規格，以及活躍變更集 `proposal.md`、`design.md`、`tasks.md` 與 Delta Spec）。 |
| **MCP 整合設定與操作指南** | [mcp/mcp_config.example.json](mcp/mcp_config.example.json)<br/>[mcp/OVERLEAF_MCP_GUIDE.md](mcp/OVERLEAF_MCP_GUIDE.md) | 支援免費版 Overleaf MCP（`@netique/overleaf-mcp`）、付費版 Git-Bridge MCP（`OverleafMCP`）與 GitHub MCP 之設定範本與同步手冊（零機密安全規範）。 |
| **自動化檢核與一鍵打包** | [scripts/verify_ieee_draft.py](scripts/verify_ieee_draft.py)<br/>[scripts/build_overleaf_zip.py](scripts/build_overleaf_zip.py) | 自動驗證 Overleaf `pdfLaTeX` 純英文語法安全、括號／環境平衡、BibTeX 15/15 引用一致、DIC-3 7/7 防走歪紅線（G1–G7）與 8/8 A–Z 會議論文必備項目。 |

---

## 🚀 快速使用步驟

### Step 1：填入作者資訊並上傳 Overleaf 編譯 PDF
1. 開啟 [overleaf/main.tex](overleaf/main.tex) 第 28–36 行（已標記 `% TODO:`），填入您的姓名、系所／學校、城市與 Email（或上傳 Overleaf 後直接於網頁編輯）。
2. 如在本地修改過 `overleaf/`，重新檢核並打包：
   ```bash
   python scripts/verify_ieee_draft.py
   python scripts/build_overleaf_zip.py
   ```
3. 前往 [Overleaf](https://www.overleaf.com/) → **New Project → Upload Project**，上傳 `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip`，編譯器維持預設 **`pdfLaTeX`**，點選 **Recompile** 即可產出 IEEE Conference PDF（若想改用 Overleaf MCP 即時同步，請見 [mcp/OVERLEAF_MCP_GUIDE.md](mcp/OVERLEAF_MCP_GUIDE.md)）。

### Step 2：推送 OpenSpec 專案至 GitHub
在 GitHub 建立一個空白儲存庫（例如 `DIC-4-overleaf-conference-draft`）後，於本資料夾執行：
```bash
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

---

## ✅ 防走歪紅線與實證誠實保證（繼承 DIC-3 `DESIGN.md` v0.6）
本論文與 OpenSpec 嚴格遵守 7 大紅線（可透過 `python scripts/verify_ieee_draft.py` 一鍵驗證）：
- **母體**：僅限證交所上市普通股（含 93 檔已下市，共 1,322 檔），排除上櫃、興櫃與前一年成交值最低 10%。
- **特徵與時間**：固定每年 4 月底、只用前一年度年報與 1–12 月營收、固定 10 項特徵＋產業類別。
- **標記**：最後 20 個交易日含息財富平均、雙標記 `y_main` / `y_raw`，`UNKNOWN` 絕不當成負例。
- **Agent 與用語**：7 個白名單工具（`max_calls = 12`）、2 條領域紅旗、最多 3 輪 `verify_report` 核對與 `template_report(T)` 降級；未校準前一律稱 **model score**。
- **誠實揭露**：僅呈現已完成驗證之資料層成果（1,322 檔、9,256 任務 0 失敗、7,754 筆樣本、價格異常率 14.7% → 1.7%、台積電 8/8 一致、8201 現金減資 NT\$8,690 財富守恆、214/214 減資股數比核對），E1–E4 模型實驗誠實標註為待驗證協定，絕不編造數據。
