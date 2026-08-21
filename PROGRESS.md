# 專案進度紀錄（PROGRESS）

> 目的：記錄本專案各階段的產出與待辦，供任何後續 session（人或 AI）快速接手。
> 最後更新：2026-08-21

---

## 時間軸

### 2026-07-21 — 文獻回顧完成（第一次 commit）
- 主文《PI3Kα抑制劑相關高血糖與metformin.md》（約 82,600 字，A–L 章）
- 三層外部知識管線 ＋ 敵對稽核（citation-verifier / claim-auditor / cross-referencer）
- 70+ 篇全文落地為可 grep Markdown（`原始PDF/`）；仿單逐字擷取稿（`來源/`）

### 2026-08-11 — 臨床處置指引與決策工具（本輪）

**1. Workflow 文獻更新（7 個並行 agents，約 64 萬 tokens）**
- 4 個本地抽取：風險分層＋監測（D/M 章）、metformin 劑量（G/E 章）、其他降糖藥（H 章＋ADA 擷取稿）、兩藥仿單全表
- 3 個外部搜尋，關鍵新發現：
  - **ADA Standards of Care 2026**（2025-12-08 發布）：首設「Diabetes Induced by Systemic Anti-Cancer Therapy」專節；Rec 3.8（高風險者考慮預防性 metformin）、9.35a（metformin 第一線）、9.35b（insulin 保留給重症）
  - **FDA inavolisib 仿單 2025-09 → 04/2026**：新增 fatal hyperglycemia / ketoacidosis 警語＋上市後致死個案；04/2026 新增腎功能劑量
  - ESMO Open 2026 跨藥物毒性管理綜述（Jhaveri，PMID 41604817）；GO39374 安全性總覽（PMID 40513140）；2025 中國專家共識（PMID 40206206）；INAVO120 final OS（NEJM 2025）；ITACA（第 1 週高血糖 91.3%、中位 6 天）
  - Capivasertib 2025–2026 重症個案系列（DKA 需 insulin 130 U/h；正常 HbA1c 一週後 >1200 mg/dL 併 DKA+HHS 需 CRRT）
  - **明確未找到**：SGLT2i 預防之 RCT（EPIK-B4 因收案 n=2 終止）；capivasertib 預防性用藥 RCT
- Workflow journal：`~/.claude/projects/-Users-ander-Documents-medical-diabetes-pi3k/.../subagents/workflows/wf_c845fe12-d15/journal.jsonl`

**2. `PROTOCOL.md` — 臨床處置指引 v1.0**
- 回答四個核心問題：①血糖高怎麼加藥（metformin 階梯→SGLT2i/TZD→DPP4i，避免 SU）②更高時抗癌藥與降糖藥同步調整（§4.1 兩藥並列 FPG 分層總表）③insulin 時機（七項立即啟用指徵；insulin-sparing ≠ 不用）④PI3Ki 減量/暫停/永久停藥＋rechallenge 七步 checklist
- §9 納入 2025–2026 證據更新；§11 誠實聲明證據缺口

**3. `docs/index.html` — 護理端互動決策網頁**
- 五步表單（紅旗→藥物劑量→FPG→降糖藥→情境）→ 分級結果面板（抗癌藥動作/降糖藥升階/監測/照會/常見錯誤）
- 已含「21 天倒數」實例卡（alpelisib Grade 2 時依今天日期算出判定日、個人化減量階梯）
- GitHub Pages 已啟用：https://zinojeng.github.io/pi3k_metformin/
- Artifact 即用版：https://claude.ai/code/artifact/a74cfb3a-bde2-44ed-8a0b-3a5f236874ec

**4. `PROTOCOL.md` §4.2 新增「各時間條款的白話說明與實例演算」**
- 七個帶日期演算範例：alpelisib 21 天倒數／3–5 天窗＋21 天終局／24 小時複驗；inavolisib Grade 2 對照／7 天保劑量／30 天觀察窗；恢復用藥低血糖陷阱
- 原 §4.2/§4.3 依序改編號為 §4.3/§4.4
- ⚠️ 因本機權限事件（見下），此節**經 GitHub API 直接提交**，本機工作樹落後遠端，權限恢復後需 `git pull`

**5. Metformin 上限條款更新（同日稍晚）**
- 查證 Glucophage 仿單：美國 FDA IR 上限 2550 mg/day（>2000 建議 TID）、歐盟 SmPC 3000 mg/day 分 3 次、XR 一律 2000
- PROTOCOL.md §3.2 與網頁工具新增「2000 mg 之後的空間」條款：標準上限維持 2000，選擇性病人（腸胃耐受、eGFR ≥60）可依仿單 IR 上調至 850–1000 mg TID；引 Garber 1997 劑量反應平頂為據，明示加 SGLT2i 通常更有效率

### 2026-08-19 — Research gaps 系統性盤點（本輪）

**`RESEARCH_GAPS.md` — 24 條 research gaps 全景**
- Workflow 多 agent 盤點（27 agents、約 183 萬 tokens）：7 個並行抽取員（章節稿／PROTOCOL＋PROGRESS／試驗登錄與仿單／75 篇全文 limitations 分三組／稽核與個案）抽出 123 條線索 → 合併去重 18 條 → 每條由獨立敵對驗證員回 grep 本地全文庫嘗試反駁 → 18 條全數成立（數條收窄措辭）→ 完整性批判補 6 個角度（5 條本地有線索＋1 條延伸建議）
- 六大類：預防與飲食（無 RCT、共識矛盾）、藥物比較（SGLT2i 無 RCT 且仿單「推薦卻不警示」、三藥無頭對頭）、特殊族群（既有 T2DM、CKD、亞洲/台灣、老年）、監測與急症（CGM vs SMBG 空白、HHS 無分母、rechallenge 僅個案）、機轉與長期結局（insulin feedback 人體證據方向不一致、停藥後完全回復時程未報告）、批判補充（PK DDI、顯影劑週期性停 metformin、類固醇併用、實施科學、衛教成效、健康經濟）
- 附錄收錄驗證過程抓到的 6 處現有文件措辭失準（如 MSKCC「逾半數」應為 31.7%、中斷率 28% 應為 27.2%、「INAVO120 無時序資料」已被 Im 2026 反駁）——**待回修主文與章節稿**
- Workflow journal：`.../subagents/workflows/wf_c009b4f7-f29/journal.jsonl`

### 2026-08-21 — 案例 §2e 更新（本輪）

- **08/14 以 150 mg（仿單外）恢復 → 08/15 二度 Grade 3（FPG 305）→ 再停 → 08/18 起 1/4 錠（約 37.5 mg）續用**
- 現行降糖：Toujeo 14 U QD＋NovoRapid 8 U TID AC＋Glucophage 1500 mg/day；FPG 134→133→158 連 3 天 ≤160（Grade 1），殘餘晚餐段峰 304–354
- 核心爭點移到腫瘤端：仿單減量止於 200 mg、<200 應永久停藥、膜衣錠不可剝——已寫成 A（停藥換線）/B（200 mg 再挑戰）/C（知情續用 37.5）三選項與 08/21 SOAP，見 `cases/2026-08_alpelisib_T2DM_hyperglycemia.md` §2e、§4

---

## ⚠️ 2026-08-11 本機權限事件（已解決）

編輯過程中，macOS 將執行 Claude Code 的程序對 `~/Documents` 的存取權整個收回（TCC 層級）：所有既有檔案讀寫、`ls ~/Documents`、git 操作全部 EPERM，連停用沙箱亦同；僅新建檔案短暫可行後也失效。**修復方式**：系統設定 → 隱私權與安全性 → 檔案與檔案夾（或完整磁碟取用權限）→ 對執行 Claude Code 之 App 勾選「文件檔案夾」→ 完全重啟該 App。

**權限恢復後的第一件事**：
```bash
cd ~/Documents/medical/diabetes/pi3k && git pull
```
（遠端已含 §4.2 實例演算、PROGRESS.md、CLAUDE.md；本機工作樹需同步）

---

## 待辦 / 可能的下一步

- [ ] 依 `RESEARCH_GAPS.md` 附錄修正主文/章節稿的 6 處措辭失準（MSKCC 31.7%、中斷率 27.2% 附分母、INAVO120 時序已有 Im 2026 來源、血糖機 ±15% 無來源、copanlisib+keto n=2、Goncalves 門檻待驗）
- [ ] 網頁工具可選強化：capivasertib 模式（4-on/3-off 監測邏輯不同）、中英切換、列印版病人衛教單
- [ ] 追蹤中的試驗：NCT07748208（inavolisib 於 T2DM 病人，2026-09 起）、NCT05090358 TIFA、NCT06083038（CGM，已完成未發表）
- [ ] TFDA inavolisib 中文仿單：尚未取得，取得後補入 PROTOCOL.md
- [ ] 主文（82,600 字回顧）尚未納入 2025–2026 更新——若要更新，重點是 ADA SoC 2026 專節與 inavolisib 仿單 09/2025 警語
