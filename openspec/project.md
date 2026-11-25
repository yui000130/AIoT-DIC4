# Project Context: DIC4 — Multibagger Scout IEEE Conference Draft via MCP & OpenSpec

## 1. Purpose & DIC4 Deliverables
本專案為 **DIC4 作業：Overleaf Draft for Conference using MCP and OpenSpec**，延續 [DIC-3-project-refactor](https://github.com/yui000130/DIC-3-project-refactor.git) 之 *Multibagger Scout*（台股潛力股探勘 AI Agent，`DESIGN.md` v0.6）A–Z SOP 重構規格，透過 **OpenSpec（Spec-Driven Development）** 與 **Overleaf MCP / Git 工作流程** 完成兩項核心交付：

1. **Overleaf Draft for IEEE Conference（`overleaf/` & `dist/`）**：
   - 標準雙欄 IEEE 研討會論文初稿（`\documentclass[conference]{IEEEtran}`），包含 `main.tex`、`references.bib`、兩張原生 TikZ 向量架構／時間軸圖（`figures/architecture_tikz.tex`、`figures/walkforward_tikz.tex`），以及可直接上傳 Overleaf 編譯的 `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip`。
   - 完整涵蓋 A–Z SOP 26 字母結構：Abstract (`A–F`)、Introduction (`G–L`)、Related Work (`M–O`, 4×5 Matrix)、Proposed Scheme (`PA–PM`, Math Equations, Algorithm 1 & 2, 2330 TSMC Run-Through)、Data Validation & Experimental Protocol (`Q–V`, `[T]` Tuning Table, `[6.2]` E1–E4 Quantitative Targets, Limitations)、Conclusion (`W–Z`) 與 15 篇驗證過之 IEEE BibTeX 參考文獻。
2. **OpenSpec on GitHub（`openspec/`、`mcp/`、`scripts/`）**：
   - 標準 OpenSpec 規格庫（`project.md`、`AGENTS.md`、`specs/`、`changes/ieee-conference-draft/`），搭配 Overleaf MCP / GitHub MCP 接軌設定檔（`mcp/mcp_config.example.json`、`mcp/OVERLEAF_MCP_GUIDE.md`）與自動化 LaTeX／紅線檢核腳本（`scripts/verify_ieee_draft.py`）。

> **學術倫理與免責聲明**：本系統為學術研究與財金教學用途，所有模型分數與分析報告均不構成投資建議；論文僅呈現已完成驗證之資料層實測數據，絕不編造尚未執行完畢之模型實驗結果。

---

## 2. Core Research Decomposition (Synchronized with DIC-3 `DESIGN.md` v0.6)

### 2.1 Abstract (A to F)
- **A (Attention Getter)**：台股 2026 年 10 月底開戶數達 1,482.7 萬人（30 歲以下占單月新增 56.3%），但長期股東財富極端集中（Bessembinder 2026 百年美股 29,754 檔中僅 46 家貢獻 91 兆美元淨財富之一半，中位數報酬 −6.9%；台積電單檔占台股市值逾 40%）。
- **B (But)**：S&P SPIVA 2025 顯示 79% 主動美股大型股基金落後大盤、2021–2025 五年 0% 維持前四分之一；倖存者偏差虛增長期回測 30%–100%（免費資料源下市股覆蓋 `pitbacktest` 僅 0/41）；LLM 具預訓練時間洩漏與算術幻覺（FAITH 多變數計算失誤率 10%–20%+；Alpha Arena 38 個 AI 帳戶中 31 個虧損）。
- **C (Cure)**：提出 **Multibagger Scout**——時間一致（Point-in-Time, PiT）且可程序化核對數字的台股潛力股探勘 Domain AI Agent。
- **D (Development)**：八大模組架構＋Program of Thoughts（PoT）計算與語言分離；FinMind 全市場上市普通股（含 93 檔已下市，共 1,322 檔）之 10 項特徵＋產業類別；雙標記 `y_main`（前 5% 最後 20 交易日平均含息報酬且 5 年營收 CAGR ≥ 10%）與 `y_raw`；LightGBM + SHAP + kNN 已揭曉案例（$\tau \le t - 5\text{Y}$）+ 2 條領域紅旗規則；7 個白名單工具（`max_calls = 12`）與最多 3 輪 `verify_report` 數字核對迴圈。
- **E (Experiments)**：2013–2020 年 8 個每年 4 月底視窗，2018–2020 三輪觀察期不重疊 walk-forward 驗證，評估 E1（`Precision@20/50`、`Recall@50`、`PR-AUC` vs 1,000 次隨機抽樣）、E2（前 50 檔等權 vs 0050）、E3（三組與下市分層 SHAP）、E4（30 家報告數字正確率 vs 直接 LLM）及 E5（敏感度分析）。
- **F (Findings)**：已完成資料層全市場驗證（1,322 檔、9,256 任務 0 失敗、7,754 筆樣本、價格異常率由 14.7% 降至 1.7%、台積電外部核對 8/8 一致、8201 現金減資財富守恆 NT\$8,690 驗算、證交所減資股數比 214/214 通過）；模型排序能否優於 ~5% 基準率列為待驗證假設。

### 2.2 5 Cores, 3 Trade-offs & 10 Details
- **5 Cores**：① 全市場 PiT 資料收集（含已下市 93 檔，共 1,322 檔）；② 財富守恆含息報酬與雙標記資料集（10 特徵＋產業）；③ 三輪不重疊 Walk-Forward 訓練與 E1–E3 評估；④ 7 白名單工具＋SHAP＋kNN＋2 紅旗＋3 輪 `verify_report` 核對 Agent 與 E4 評估；⑤ Streamlit 互動分析介面。
- **3 Trade-offs**：① 時間粒度（固定每年 4 月底、只用前一年度年報與月營收）換取 100% 零前視偏誤；② 白名單工具與 3 輪核對（捨棄自由寫碼與外部新聞）換取零算術幻覺與零未授權數字；③ 上市普通股母體與 `UNKNOWN` 誠實保留（不當負例）換取標記純淨度。
- **10 Details**：除權息／減資／分割財富守恆因子、最後 20 個交易日平均終點價、90 天內 ≥ 5 天非升降單位排除興櫃（394 筆）、漲跌幅限制 7%/10% 價格異常檢查（134 筆 / 1.7%）、跨 2012–2013 IFRS 跳升 > 3 倍標 `UNKNOWN`、減資換股率 $k$ 市值修正、$\lceil 0.05 N_t \rceil$ 含同分代號排序與排除最低 10% 流動性、kNN 鎖定 $\tau \le t - 5\text{Y}$、2 條紅旗門檻限訓練期擬合、未校準前一律稱「模型分數」並區分雙基準率。

---

## 3. Tech Stack & Authoring Toolchain
- **Paper Format**: IEEE Conference (`IEEEtran` v1.8b, `\documentclass[conference]{IEEEtran}`, double-column, US letter, target 6 pages)
- **LaTeX Compiler Target**: Overleaf (`pdfLaTeX` + `BibTeX` with `IEEEtran.bst`, pure ASCII/English `.tex` with zero CJK dependency)
- **Diagrams**: Native LaTeX `TikZ` vector diagrams (`figures/architecture_tikz.tex`, `figures/walkforward_tikz.tex`)
- **MCP Integration**: Overleaf MCP (`@netique/overleaf-mcp` for free-tier real-time sync or `OverleafMCP` for Git-bridge sync) & GitHub MCP for OpenSpec version control
- **Verification**: `Python 3.10+` (`scripts/verify_ieee_draft.py`, `scripts/build_overleaf_zip.py`)

---

## 4. Non-Negotiable Guardrails（DIC-3 繼承之 7 大防走歪紅線）
本專案所有 LaTeX 論文內容與規格修改，皆須通過 `python scripts/verify_ieee_draft.py` 檢核，嚴格遵守：
1. **G1 母體範圍**：僅限 TWSE 上市普通股（含已下市），排除上櫃、興櫃、存託憑證、ETF、特別股與最低 10% 成交值。
2. **G2 特徵口徑**：每年 4 月底特徵日、只用前一年度年報與 1–12 月營收、固定 10 項特徵＋產業類別（嚴禁塞回 v0.4 已刪之 ROA、EBITDA 利潤率、資產成長率、波動度、殖利率）。
3. **G3 領域規則**：僅 2 條紅旗（Earnings Quality、Extreme Valuation），門檻限訓練期決定，無動態新聞 RAG。
4. **G4 標記與終點價**：最後 20 交易日平均含息財富、雙標記 `y_main` / `y_raw`、`UNKNOWN` 絕不視為負例。
5. **G5 Agent 工具與核對**：7 個白名單工具名稱逐字一致、`max_calls = 12`、最多 3 輪 `verify_report` 核對與 `template_report(T)` 降級。
6. **G6 模型分數用語**：一律稱 **model score**（嚴禁稱 probability / upside probability），明確區分訓練期基準率與同輪 E1 實際正例率。
7. **G7 實證誠實原則**：僅呈現已驗證之資料層實證數據（1,322 / 9,256 / 7,754 / 1.7% / 8/8 / 8201 / 214/214），嚴禁編造 E1–E4 模型實驗結果。
