# Overleaf MCP & GitHub MCP Integration Guide (DIC4)

本指南說明如何透過 **MCP（Model Context Protocol）** 或 **一鍵 ZIP 上傳**，將 `overleaf/` 內之 *Multibagger Scout* IEEE 會議論文同步至 Overleaf 並遠端編譯 PDF，以及透過 Git / GitHub MCP 管理 `openspec/` 規格庫。

---

## 方式一：一鍵上傳 Overleaf（最快速，不需設定 Token，免費版可用）

1. 開啟 [Overleaf](https://www.overleaf.com/) 並登入帳號。
2. 點選左上角 **New Project → Upload Project**。
3. 直接拖曳本專案打包好的壓縮檔：
   - `dist/MultibaggerScout_IEEE_Conference_Overleaf.zip`
4. 開啟 `main.tex`，將第 28–36 行 `% TODO:` 註解處改為您的**作者姓名、系所／學校、城市與 Email**。
5. 確認左上角 **Menu → Compiler** 為預設的 **`pdfLaTeX`**（本論文純英文無 CJK 相依，原生零錯誤編譯），按下 **Recompile** 即可產出標準雙欄 IEEE Conference PDF！

> 若後續有修改 `overleaf/` 檔案，執行 `python scripts/build_overleaf_zip.py` 即可重新產生最新 ZIP。

---

## 方式二：透過 Overleaf MCP 即時同步（適合免費版或付費版進階協作）

### 方案 2A：Overleaf 免費版（`@netique/overleaf-mcp`，Web / Socket.IO）
1. 需本機具備 **Node.js 18+**（提供 `npx`）。
2. 在 Overleaf 建立一個空白專案，從網址 `https://www.overleaf.com/project/<PROJECT_ID>` 取得 `OVERLEAF_PROJECT_ID`。
3. 參考 [mcp_config.example.json](./mcp_config.example.json)，將 `overleaf-free-tier` 區塊複製至您使用的 AI Agent / IDE 的 MCP 設定檔（例如 Antigravity / Cursor / Claude Desktop 的 `mcp_config.json`），並以環境變數填入您的 Session Cookie 與 Project ID（**切勿將 Cookie 或 Token 提交至 Git**）。
4. 重啟 MCP Client 後，即可直接請 AI Agent 依 `openspec/specs/ieee-conference-paper/spec.md` 同步 `overleaf/main.tex`、`overleaf/references.bib` 與 `overleaf/figures/*.tex` 至 Overleaf 並讀取遠端編譯紀錄。

### 方案 2B：Overleaf 付費版 / 校園授權（Git Bridge + `OverleafMCP`）
若您的 Overleaf 帳號具備 Git Integration 權限：
1. 在 Overleaf 專案左上角 **Menu → Sync → Git** 取得 Git URL（`https://git.overleaf.com/<PROJECT_ID>`）並產生 Git Token。
2. 啟用 [mcp_config.example.json](./mcp_config.example.json) 中的 `overleaf-git-bridge` 區塊，或直接以 Git subtree / remote 同步 `overleaf/` 目錄。

---

## 方式三：GitHub OpenSpec 同步（Git CLI 或 GitHub MCP）

本專案已於本地完成 Git 初始化與 OpenSpec 規格建立。您可以任選：
- **Git CLI（推薦）**：在 GitHub 建立空儲存庫（例如 `DIC-4-overleaf-conference-draft`）後執行：
  ```bash
  git remote add origin https://github.com/<your-username>/<your-repo-name>.git
  git push -u origin main
  ```
- **GitHub MCP**：於 MCP 設定檔啟用 `github` 伺服器並填入 `GITHUB_PERSONAL_ACCESS_TOKEN`，即可讓 AI Agent 直接透過 MCP 建立 Repo、提交 OpenSpec PR 與管理 Issue。

---

## 安全提醒（Zero-Secret Hygiene）
- `mcp_config.example.json` 僅作為設定範本，請勿直接將真實 Token 或 Cookie 寫入專案資料夾並 `git push`。
- `.gitignore` 已自動排除 `.env`、`mcp_config.json`、`_ref_dic3/` 與 LaTeX 編譯暫存檔。
