# Multibagger Scout｜論文與報告文件

台股潛力股探勘 AI Agent（Multibagger Scout）的 ICEIB 2027 研討會論文與期末報告工作區。

**2026-11-26 更新**：論文依系統設計文件 DESIGN.md **v0.8** 與實際實驗結果（E1–E4）重寫。程式、資料管線與實驗結果在 [MultibaggerScout-AIagent](https://github.com/yui000130/AIoT-FinalProject-MultibaggerScout-AIagent)；論文中的數字都來自該 repo 的 `results/`。

## 文件總覽

| 文件 | 內容 | 狀態 |
| --- | --- | --- |
| [ICEIB 2027 論文草稿 (LaTeX檔)](ICEIB%20paper/main.tex) | IEEE `IEEEtran` 雙欄研討會論文，章節對應 A–Z 規範 | 2026-11-26 依 v0.8 與 E1–E4 結果重寫 |
| [ICEIB 2027 論文草稿 (PDF檔)](ICEIB%20paper/IEEEtran.pdf) | Overleaf 編譯產出的 PDF | **舊版**，需以新版 `main.tex` 在 Overleaf 重新編譯 |
| [OpenSpec 論文規格設定](openspec/config.yaml) | ICEIB + A–Z 寫作規範與 `000`–`006` 章節 Changes | 2026-11-26 更新 |
| [專業摘要](專業摘要.md) | 約 500 字中文專業摘要 | 2026-11-26 加入實驗結果 |
| [專題設計規範檢核](專題設計規範檢核.md) | 依 A2Z outline（2020 A-Z SOP）逐章檢核 | 原檢核保留，開頭加上目前補齊狀態 |
| [A–F 最新研究證據補強](Multibagger%20Scout%20A–F%20最新研究證據補強.md) | Abstract A–F 的研究數據、案例新聞與引用清單 | 未更動（素材來源，論文只引用其中可查證的部分） |
| [A–Z 檢核資訊圖表](MultibaggerScout_A2Z_A4.png) | A4 橫式資訊圖表 | 舊版（依提案階段繪製） |

## 論文的 A–Z 對應

| 章節 | A–Z 項目 | 內容 |
| --- | --- | --- |
| Abstract | A–F | 動機、挑戰、方法、資料與設計、實驗、**實際結果** |
| I. Introduction | G–L | 背景、四個挑戰、文獻與缺口、RQ1–RQ3 與貢獻、章節結構 |
| II. Related Work | M–O | 四個文獻流派、本研究定位、**4 流派 × 5 面向**比較矩陣（Table I） |
| III. Proposed Design | PA–PM | 目標與 PoT 原則、數學定義（含息財富、20 日平均、前 5% 標記、營收 CAGR、UNKNOWN、時間一致性限制）、8 模組架構、Algorithm 1–2、**真實案例走訪**（1310 台苯，2018-04-30） |
| IV. Experiments | Q–V | 資料與三輪 walk-forward、固定參數表（不調參）、指標與基準、事先固定的判準、E1–E4 結果、效度威脅 |
| V. Conclusion | W–Z | 方法總結、優勢、成果、限制與未來工作 |

## 主要結果（摘自論文）

- **E1 排序品質**：LightGBM 的 PR-AUC 在第 1、3 輪高於隨機 1,000 次的第 95 百分位（0.082、0.081）；邏輯迴歸、低 P/B、高 ROE、Yartseva 啟發規則三輪都在隨機範圍內
- **E2 組合表現**：LightGBM 前 50 的 5 年毛報酬 +62.9% / +195.8% / +157.8%，0050 為 +75.3% / +125.8% / +135.4%；只有第 3 輪高於隨機第 95 百分位
- **E3 特徵關聯**：過去 12 個月報酬與年營收成長率的關聯最明顯；Yartseva 的美股十倍股方向在台股大多不成立
- **E4 報告品質**：數字正確率 Agent 1.000、直接 LLM 0.623（差 +0.377，95% 信賴區間 0.359～0.397）；Agent 模板退回率 10.4%

## 投稿前待辦

- 在 Overleaf 重新編譯 `main.tex`，確認頁數（4–8 頁）與表格版面，更新 PDF
- 逐一點開引用 [1]、[3]、[6]、[8]、[11] 的原始頁面確認內容（來自 A–F 證據補強，尚未逐篇核對全文）
- 確認作者與單位
