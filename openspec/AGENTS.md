# OpenSpec + MCP Instructions & Workflow Guide (DIC4)

本專案採用 **OpenSpec（Spec-Driven Development）** 搭配 **MCP（Model Context Protocol：Overleaf MCP + GitHub MCP）** 管理 *Multibagger Scout* 之 **IEEE Conference Paper Overleaf Draft** 撰寫、檢核與同步流程。

---

## 1. Repository & OpenSpec Directory Map

```text
DIC4/
├── README.md                                        # 專案總覽、作業對照表、Overleaf 與 GitHub 快速指引
├── overleaf/                                        # Overleaf 論文原始碼（IEEEtran 雙欄會議論文）
│   ├── main.tex                                     # 論文主檔（完整 A–Z SOP 英文 IEEE 論文）
│   ├── references.bib                               # 15 篇驗證過之 IEEE BibTeX 文獻
│   └── figures/
│       ├── architecture_tikz.tex                    # 圖 1：八大模組＋7 白名單工具＋3 輪 verify_report 向量架構圖
│       └── walkforward_tikz.tex                     # 圖 2：2013–2020 三輪不重疊 Walk-Forward 時間軸向量圖
├── dist/
│   └── MultibaggerScout_IEEE_Conference_Overleaf.zip # 一鍵上傳 Overleaf 之壓縮包
├── mcp/
│   ├── mcp_config.example.json                      # Overleaf MCP & GitHub MCP 客戶端設定範本
│   └── OVERLEAF_MCP_GUIDE.md                        # Overleaf MCP 連線同步與免費／付費方案操作手冊
├── openspec/
│   ├── project.md                                   # 專案全局脈絡、A–F、5 Cores、3 Trade-offs、10 Details、7 大紅線
│   ├── AGENTS.md                                    # AI Agent 執行 OpenSpec + MCP 工作流程指南（本文件）
│   ├── specs/
│   │   ├── multibagger-scout/spec.md                # 系統本體規格（源自 DESIGN.md v0.6）
│   │   └── ieee-conference-paper/spec.md            # IEEE 會議論文排版、章節、公式、引用與紅線規格
│   └── changes/
│       └── ieee-conference-draft/                   # DIC4 活躍變更集（Active Change Workflow）
│           ├── proposal.md                          # Why & What Changes
│           ├── design.md                            # 論文架構設計、6 頁篇幅配置、TikZ 與 MCP 同步管線
│           ├── tasks.md                             # 分階段可執行任務清單
│           └── specs/
│               └── conference-draft-compliance/
│                   └── spec.md                      # Delta Spec（ADDED / MODIFIED Requirements）
└── scripts/
    ├── verify_ieee_draft.py                         # LaTeX 語法、BibTeX 引用、7 大紅線與 A–Z 結構自動檢核腳本
    └── build_overleaf_zip.py                        # 一鍵打包 Overleaf 上傳 ZIP 腳本
```

---

## 2. Spec-Driven Paper Authoring & MCP Workflow

### Stage 1: Context & Spec Alignment（對齊規格）
修改任何論文段落或圖表前，Agent 必須依序讀取：
1. [openspec/project.md](./project.md)：確認 7 大防走歪紅線（G1–G7）與所有已驗證之實證數據。
2. [openspec/specs/multibagger-scout/spec.md](./specs/multibagger-scout/spec.md)：確認系統 8 大模組、10 項特徵、雙標記與 7 個白名單工具。
3. [openspec/specs/ieee-conference-paper/spec.md](./specs/ieee-conference-paper/spec.md)：確認 IEEEtran 雙欄格式、純英文 pdfLaTeX 相容性、A–Z 結構與 BibTeX 規範。

### Stage 2: Execute Change & Author LaTeX（執行變更與編修）
1. 依循 [changes/ieee-conference-draft/design.md](./changes/ieee-conference-draft/design.md) 與 [tasks.md](./changes/ieee-conference-draft/tasks.md) 編修 `overleaf/main.tex`、`overleaf/references.bib` 與 `overleaf/figures/*.tex`。
2. 禁止在未取得實際回測數據前填寫 E1–E4 假數值；僅能於 Section V 呈現已完成驗證之資料層指標與待驗證判準。

### Stage 3: Automated Verification & Packaging（自動檢核與打包）
每次編修完成後，執行：
```bash
python scripts/verify_ieee_draft.py
python scripts/build_overleaf_zip.py
```
確認所有檢核項（LaTeX 結構平衡、BibTeX 引用完整性、7/7 紅線 G1–G7、A–Z 會議論文必備元素）全數 **PASS**。

### Stage 4: Sync via MCP / Git（同步至 Overleaf 與 GitHub）
- **Overleaf 同步**：透過已掛載之 Overleaf MCP（詳見 [mcp/OVERLEAF_MCP_GUIDE.md](../mcp/OVERLEAF_MCP_GUIDE.md)）推送 `overleaf/` 內容並觸發遠端編譯，或直接將 `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip` 上傳至 Overleaf。
- **GitHub 同步**：將完整 `openspec/`、`overleaf/`、`mcp/`、`scripts/` 提交並推送至 GitHub 儲存庫（可透過 `git push` 或 GitHub MCP）。
