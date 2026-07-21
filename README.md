# PI3Kα inhibitor 相關高血糖與 metformin 的角色

臨床醫師層級的文獻回顧與演講架構（繁體中文）。

**主題**：PI3Kα inhibitor–associated hyperglycemia — 機轉、風險分層，以及 metformin 的預防性與治療性角色
**族群**：成人癌症患者，以 PIK3CA-mutated HR+/HER2− advanced breast cancer 為主
**產出日期**：2026-07-21

---

## 主要成品

| 檔案 | 內容 |
|---|---|
| [`PI3Kα抑制劑相關高血糖與metformin.md`](PI3Kα抑制劑相關高血糖與metformin.md) | **主文**。含 A–L 全部輸出、錨點目錄、證據標記說明 |
| [`撰寫方法論.md`](撰寫方法論.md) | 本次檢索與稽核流程的執行紀錄 |
| [`MISSING_FULLTEXT.md`](MISSING_FULLTEXT.md) | 未取得全文的文獻與原因 |
| [`章節/`](章節/) | 各章節原始稿 |
| [`來源/`](來源/) | 仿單、指引、試驗登錄的逐字擷取稿；文獻清單與清冊 |
| [`稽核/`](稽核/) | 三份敵對稽核報告（引用／數字／交叉比對） |
| [`原始PDF/`](原始PDF/) | 論文全文轉檔 Markdown（PDF 本身不入版控） |

主文結構對應需求的 A–L：摘要、病理生理圖解文字稿、alpelisib vs inavolisib 比較表、
基線風險分層表、metformin 三欄比較表、以 mg/dL 與 mmol/L 並列的處置流程、
metformin 劑量遞增表、後續降糖藥比較表、爭議與 knowledge gaps、
14 張投影片的演講大綱、重要文獻表、以及五句 take-home messages。

---

## 證據標記

主文中每個建議都標註來源層級，讀者可一眼區分「規定／試驗／共識／推論」：

| 標記 | 意義 |
|---|---|
| 【L1】 | FDA／EMA／TFDA 正式仿單 |
| 【L2】 | 前瞻性臨床試驗（SOLAR-1、BYLieve、METALLICA、INAVO120 等） |
| 【L3】 | 專家共識／Delphi／學會指引 |
| 【L4】 | 回溯性研究／real-world／case series |
| 【L5】 | 前臨床或機轉推論 |

全文取得標記：**📄** = 本地有全文可 grep；**📌** = 僅有 abstract／metadata，
禁止對其內文細節作具體斷言。

---

## 方法

採「三層外部知識管線」：所有事實性內容必須能 grep 驗回本地落地的來源檔，
LLM 只負責組織與改寫，不作為知識來源。

1. **第一層｜搜尋**：`paper-search-mcp`（PubMed／Europe PMC 等多源）+ web 檢索仿單與指引
2. **第二層｜全文落地**：Europe PMC JATS XML 轉 Markdown（保留 reference list）；
   非 OA 者走 PMC／Unpaywall PDF → LlamaParse
3. **第三層｜敵對稽核**：三個獨立稽核員並行攻擊草稿
   - `citation-verifier` — DOI resolve + Crossref／PubMed metadata 比對
   - `claim-auditor` — 每個百分比／樣本數／HR／引號字串逐一 grep 回原文
   - `cross-referencer` — 論斷與來源的對應關係、13 類幻覺、五項內容禁忌

由 arbitrator 收斂稽核結論並回頭修正草稿。

### 資料規模

- 落地為可 grep Markdown 的文獻：**70+ 篇**
- 仿單／指引逐字擷取稿：alpelisib、inavolisib、ADA SOC 與比較用藥、ClinicalTrials.gov
- 主文約 **82,600 字**

### 稽核結果

| 稽核員 | 抽驗項目 | 必修 | 待議 | 通過 |
|---|---|---|---|---|
| citation-verifier | 146 | 2 | 7 | 137 |
| claim-auditor | 228 | 3 | 5 | 220 |
| cross-referencer | 130 | 3 | 6 | 121 |

70/70 DOI 經 Crossref 驗證有效；69/69 PMID 與文中 DOI 相符；無 fabricated citation。
所有「必修」項目已於定稿前修正（例如 ITACA 原被誤述為單臂，實為 randomized phase IIb）。

---

## 本回顧刻意避免的五件事

1. 把所有 PI3K／AKT inhibitors 視為同一類 — alpelisib 與 inavolisib 全程分開陳述，
   兩者的 FPG 門檻與劑量調整規則並列比較而非合併。
2. 把 METALLICA（單臂 phase 2）描述為「已證明所有患者都應接受預防性 metformin」。
3. 因理論上想避免 hyperinsulinemia，而延誤嚴重高血糖／DKA／HHS 所需的 insulin —
   主文將此列為安全紅線。
4. 未註明來源即混合 FDA 仿單、專家共識與個人意見。
5. 忽略癌症患者的腹瀉、體重下降、食慾不佳、脫水與腎功能波動。

---

## 已知限制

- **預防性 metformin 缺乏隨機對照試驗**。METALLICA 為單臂設計，無法回答
  「不給 metformin 會如何」。主文對此的措辭刻意保守。
- **已知糖尿病患者被多數關鍵試驗排除** — 臨床上最需要指引的族群，證據反而最少。
- **hyperinsulinemia 削弱抗腫瘤療效**：前臨床證據明確，人體臨床證據薄弱。
- 部分付費牆文獻僅取得 abstract（標 📌），其內文細節不得引用；
  清單見 `MISSING_FULLTEXT.md`。
- 亞洲／台灣族群資料有限，西方試驗的風險分層是否可直接套用仍待驗證。
- 本回顧為文獻整理，**不構成個別病人的醫療建議**。

---

## 授權與聲明

本儲存庫為文獻整理與教學用途。`原始PDF/` 內的轉檔 Markdown 僅供研究者個人檢索驗證之用，
著作權仍屬各原始出版者。仿單內容以各國主管機關公告之最新版本為準。
