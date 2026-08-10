# CLAUDE.md — 專案工作規範

本 repo 為「PI3Kα 抑制劑相關高血糖與 metformin」之醫學文獻回顧與臨床處置指引專案。任何 AI 協作 session 開始前先讀本檔與 `PROGRESS.md`。

## 語言與對象

- 一律使用**繁體中文**撰寫，藥名、劑量單位、試驗名稱保留英文（alpelisib、FPG、mg/dL）。
- 讀者為臨床醫師、研究護理師與個案管理師；文件須可直接照做（含精確數字），不寫模糊建議。

## 內容硬規則（違反即為錯誤）

1. **alpelisib 與 inavolisib 的規則分開陳述，不可互相外推**。兩藥在 FPG 161–250 的處置方向相反（alpelisib 續用、inavolisib 暫停）。
2. **劑量決策只用空腹血糖（FPG）**，不可用隨機血糖。
3. **引用紀律**：每個事實標註證據等級【L1】仿單／【L2】試驗全文／【L3】共識指引／【L4】個案回溯／【L5】前臨床，並附本地來源檔名。📄 = 本地有全文可 grep；📌 = 僅 abstract，**不得引用其內文細節**。
4. **分母紀律**：SOLAR-1 有 preferred term 與 AESI grouped term 兩套（分母皆 284 但範圍不同）；INAVO120 有 safety（162/162）與 full analysis（161/164）兩套。百分比必附分母，不可互換相加。
5. **沉默不等於未發生**：論文未報告 DKA 只能寫「未報告」，不可寫「未發生」（alpelisib 仿單載 SOLAR-1 ketoacidosis 0.7%）。
6. 查無來源時明寫「**本回顧未取得可驗證來源**」，不可補推論。
7. 跨試驗比較（SOLAR-1 vs INAVO120）不可直接相減——族群、納入條件、CTCAE 版本皆不同。

## 檔案地圖

| 路徑 | 內容 | 注意 |
|---|---|---|
| `PROTOCOL.md` | 臨床處置指引（主要交付物） | 章節編號被引用於網頁 footer，改動時檢查交叉引用 |
| `docs/index.html` | 護理端互動決策網頁（GitHub Pages：`/docs`） | 自足式單檔；改 JS 後跑 `node --check` 驗語法；深淺色主題皆須測 |
| `PI3Kα抑制劑相關高血糖與metformin.md` | 82,600 字回顧主文（A–L 章） | 2026-07 定稿，尚未含 2025–2026 更新 |
| `章節/` `來源/` `稽核/` `原始PDF/` | 章節稿、仿單擷取、稽核報告、全文轉檔 | `原始PDF/*.pdf` 不入版控（版權）；`.md` 轉檔僅供 grep 驗證 |
| `PROGRESS.md` | 進度紀錄與待辦 | 每輪工作結束時更新 |

## 工作流程慣例

- 事實查證：先 grep 本地 `原始PDF/`、`來源/`，不確定就標註查無；新文獻用 paper-search MCP（PubMed/Europe PMC）搜尋並記 PMID/DOI。
- 大型多源整理用 Workflow 並行 agents（本地抽取與外部搜尋分開）。
- 網頁部署：push 到 main 後 GitHub Pages 自動重建；Artifact 版另行 republish。
- Commit 訊息英文、內文可中文；不 force push。

## 已知環境問題

- macOS 對 `~/Documents` 的 TCC 權限曾於 2026-08-11 中途收回，導致本機讀寫全面 EPERM。若再發生：改用 GitHub Contents API 直接提交（`gh api repos/zinojeng/pi3k_metformin/contents/<path>` 取 sha 後 PUT），並提醒使用者到「系統設定 → 隱私權與安全性」重新授權後 `git pull`。
- 專案資料夾內的 macOS `Icon\r` 檔會汙染 `.git/refs` 導致 fetch 失敗；清除方式：`find .git -name $'Icon\r' -delete`。
