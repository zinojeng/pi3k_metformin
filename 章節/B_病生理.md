# B. 病理生理學圖解文字稿 —— PI3Kα inhibition 造成高血糖的機轉，以及 insulin feedback 的真實證據強度

> **本節閱讀規則**
> `📄` = 本地有全文可 grep；`📌` = 本地僅有 abstract，不對其內文細節作具體斷言。
> 每個事實後標示來源檔名；每個建議標示證據等級【L1】–【L5】。
> 本節刻意把 **alpelisib（α-selective inhibitor）** 與 **inavolisib（α-selective inhibitor + mutant p110α degrader）** 分開陳述，不視為同一藥。

---

## B-1. 一張投影片的圖解文字稿（分層節點與箭頭）

### 圖標題
**「PI3Kα inhibition 的 on-target 代謝級聯：從 p110α 到腫瘤抗藥性」**

### 第 0 層｜藥物作用點（人體證據，【L1】【L2】）

```
alpelisib / inavolisib
        │  抑制 p110α（PIK3CA 基因產物）
        ▼
   ★ 關鍵：治療劑量下同時抑制 mutant 與 wild-type p110α
```

- p110α「mediates most tissue responses to insulin and IGF1, driving tissue growth and maintaining glucose homeostasis」[Mech_Fruman_Cell_2017.md] 📄【L5】
- 「most p110α inhibitors that have entered clinical trials for solid tumors inhibit both the mutant and wild type p110α at therapeutic doses, these drugs induce acute insulin resistance, resulting in severe hyperglycemia, which, in turn, leads to severe hyperinsulinemia」[Mech_Fruman_Cell_2017.md] 📄【L5】
- 生化層面上，各 PI3K inhibitor 對 **p110α WT 與 mutant 酵素的 Ki 並無顯著差異**（"no significant differences between inhibitor Ki for p110a wild-type (WT) and p110a-mutant enzyme"）[Preclin_Song_Inavolisib_2022.md] 📄【L5】
  → **臨床意義：沒有任何一個已上市的 PI3Kα inhibitor 是「只打腫瘤、不打肌肉肝臟」的。高血糖不是脫靶毒性，而是療效的同源代價。**

### 第 1 層｜近端訊號（前臨床機轉，【L5】）

```
p110α ⊣（受抑制）
   │
   ├─ IRS-1 / IRS-2 → PI3K → PIP3 生成↓
   │        （p85 regulatory subunit 為 p110 穩定與活化所必需）
   ▼
 PDK1 / mTORC2 → AKT (Thr308 / Ser473) 磷酸化 ↓
```

- 「AKT phosphorylation on Thr 308 is both necessary and sufficient to mediate many downstream events」；mTORC2 磷酸化 Ser473，對 **FOXO transcription factors** 這一群受質特別重要 [Mech_Fruman_Cell_2017.md] 📄【L5】
- p85 對 p110 的穩定性與功能為必需，但過量時反而透過 sequestration of IRS-1、活化 PTEN 與 JNK 抑制 insulin signaling [Mech_Fruman_Cell_2017.md] 📄【L5】

### 第 2 層｜四個並行的下游分支（前臨床機轉，【L5】）

```
AKT↓
 ├─(A) AS160(TBC1D1) 去磷酸化 → GLUT4 儲存囊泡無法移位 → 肌肉／脂肪 葡萄糖攝取 ↓↓
 ├─(B) FOXO1 去抑制（核內滯留）→ PEPCK↑ + G6PC↑ → 肝臟 gluconeogenesis ↑
 ├─(C) GSK3 去抑制 → glycogen synthase 受抑 → 肝醣合成↓ ／ 肝醣分解↑
 └─(D) 脂肪組織：PI3K/AKT 對 PKA 與 ATGL 的抑制解除 → lipolysis↑ → FFA↑
```

逐條來源：

| 分支 | 分子事件 | 來源 | 等級 |
|---|---|---|---|
| (A) | 「AKT2 is the primary isoform that phosphorylates and inhibits the function of the RabGAP, AS160, which allows intracellular vesicles containing the glucose transporter GLUT4 to migrate to the plasma membrane」；此過程在血中 insulin 上升後「within minutes」發生 | [Mech_Fruman_Cell_2017.md] 📄 | 【L5】 |
| (A) | 「AKT directly phosphorylates AS160, inducing GLUT4 translocation」；骨骼肌承擔約 90% 的 insulin-stimulated glucose utilization | [Mech_Huang_ObesityT2D_2018.md] 📄 | 【L5】 |
| (B) | 「FoxO1 induces the expression of phosphoenolpyruvate carboxykinase (PEPCK) and glucose-6-phosphatase gene (G6PC), subsequently increases gluconeogenesis」；「AKT directly inhibits FoxO1, reducing glucose levels」 | [Mech_Huang_ObesityT2D_2018.md] 📄 | 【L5】 |
| (C) | 「GSK3 inhibits glycogen synthase (GS)… AKT exerts an inhibitory effect on GSK3 by phosphorylation」 | [Mech_Huang_ObesityT2D_2018.md] 📄 | 【L5】 |
| (A)+(B)+(C) 合併之藥理表述 | 「blocking insulin signaling promotes glycogen breakdown in the liver and prevents glucose uptake in the skeletal muscle and adipose tissue, resulting in **transient hyperglycemia that occurs within a few hours** of PI3K inhibition」 | [InsulinFeedback_Hopkins_2018.md] 📄 | 【L5】 |
| (A)+(B)+(C) 之管理型綜述表述 | 「PI3K/AKT/mTOR pathway inhibitors block AKT-mediated GLUT4 translocation, resulting in reduced glucose uptake into muscles and adipose tissue… It also increases glycogenolysis and gluconeogenesis」 | [ToxMgmt_Jhaveri_2026.md] 📄 | 【L3】 |
| (D) | AKT 經 FoxO1 調控 ATGL、IRF4、PDE3B 以抑制脂肪分解；PI3K/AKT 抑制 PKA 而抑制 lipolysis | [Mech_Huang_ObesityT2D_2018.md] 📄 | 【L5】 |

### 第 3 層｜整體代謝表現（人體證據，【L1】【L2】）

```
周邊 glucose disposal↓ ＋ hepatic glucose output↑
        ▼
   急性 insulin resistance → 血糖 ↑（快、早、可預期）
        ▼
   β cell 代償性大量分泌 → compensatory hyperinsulinemia
        ▼
   若 β cell 儲備足夠 → 血糖數小時內回落（transient）
   若 β cell 儲備不足（prediabetes / T2DM / β cell 質量減少）→ 持續高血糖、G3–G4、DKA/HHS
```

- 「The effect is usually transient because compensatory insulin release from the pancreas (i.e. insulin feedback) restores normal glucose homeostasis. However, the hyperglycemia may be exacerbated or prolonged in patients with any degree of insulin resistance」[InsulinFeedback_Hopkins_2018.md] 📄【L5】
- 專家共識版本：「Inhibition of PI3K leads to acute insulin resistance, blocking glucose uptake in skeletal muscle and adipose tissue, activating hepatic glycogenolysis, causing hyperglycemia and a compensatory increase in circulating insulin」[Delphi_Gallagher_2024.md] 📄【L3】
- β cell 儲備決定表現型：「If the patient is unable to produce enough insulin (undiagnosed prediabetes, due to either subacute beta cell burnout or a chronic loss in beta cell mass)… hyperglycemia occurs」[ToxMgmt_Jhaveri_2026.md] 📄【L3】
- 人體對應證據：SOLAR-1 中 baseline prediabetic 者高血糖發生率高於血糖正常者；當 HbA1c 納入門檻由 <6.5% 放寬為 <8.0% 後，grade 3/4 高血糖率上升 [Mgmt_Goncalves_2022.md] 📄【L4/L2 事後分析】
- 「As predicted by the mouse models, **hyperinsulinemia has also been observed in subjects treated with alpelisib and other PI3Kis in clinical trials and in clinical practice.**」[Mgmt_Goncalves_2022.md] 📄【L3 綜述引述】
  → 這是本回顧在本地檔案中，關於「人體確實出現 hyperinsulinemia」最直接的一句敘述。**本回顧未取得可驗證的人體 serial insulin/C-peptide 原始數據表**。
- 個案層級的人體 hyperinsulinemia：inavolisib 相關 HHS 個案中，記錄到血中 insulin 值與「strictly normal HbA1c and negative diabetes-associated autoantibodies」並存 [Inavolisib_HHS_Li_2026.md] 📄【L4】

### 第 4 層｜回頭作用於腫瘤（**此段為前臨床推論，見 B-3**）

```
血中 insulin ↑↑
   ├─→ 腫瘤 INSR（及 IGF-1R）活化
   ├─→ 即使藥物仍在，PI3K–AKT–mTORC1 部分再活化（pAKT 部分回復、pS6 幾乎完全回復）
   └─→ 腫瘤 glucose uptake↑、增殖回復 → 「self-defeating systemic feedback」→ 療效被削弱
```

- 細胞實驗：10 ng/mL insulin（等同小鼠給藥後 15–30 分鐘的血中濃度）「was sufficient to partially rescue PI3K signaling in the continued presence of PI3K inhibitors as indicated by partial re-activation of phosphorylated AKT (pAKT) and **almost complete reactivation of phosphorylated S6 (pS6)**」[InsulinFeedback_Hopkins_2018.md] 📄【L5】
- 「the increase in insulin secretion can activate not only IR, but also IGF-1R, providing a mechanism for survival of tumor cells」[Mgmt_Goncalves_2022.md] 📄【L3 綜述】
- 原文作者自己的用語：「limit this **self-defeating systemic feedback**」[InsulinFeedback_Hopkins_2018.md] 📄【L5】

---

## B-2. Q1 —— 為何 PI3Kα inhibition 會造成急性 insulin resistance、hepatic glucose output 增加與 compensatory hyperinsulinemia？

### 一句話回答
因為 **PIK3CA 所編碼的 p110α，正好就是介導 insulin 在肌肉、脂肪、肝臟全部代謝作用的同一個酵素**；治療劑量下藥物無法區分腫瘤內的 mutant p110α 與代謝組織內的 wild-type p110α，因此「抑制腫瘤 PI3K」與「製造一個藥理性的 insulin resistance 狀態」是同一個分子事件的兩面 [Mech_Fruman_Cell_2017.md] 📄【L5】。

### 拆解為三個必答子問題

**(1) 為何是「急性」（hours–days，而非 weeks）？**
因為受阻的是 **post-receptor 的既有蛋白移位事件**，不需要新的基因表現：GLUT4 由儲存囊泡移至細胞膜是 insulin 上升後「within minutes」的過程 [Mech_Fruman_Cell_2017.md] 📄【L5】。因此高血糖「occurs within a few hours of PI3K inhibition」[InsulinFeedback_Hopkins_2018.md] 📄【L5】。
臨床上這對應到極短的 time-to-onset：
- alpelisib：grade ≥2 高血糖首次發生的中位時間 **15 天（範圍 5–517 天）**[label_alpelisib.md]【L1】
- inavolisib：高血糖首次發生的中位時間 **7 天（範圍 2–955 天）**[label_inavolisib.md]【L1】；INAVO120 亦為 7.0 天（2.0–955.0）[INAVO120_Safety_Im_2026.md] 📄【L2】

> **可執行推論**：監測窗必須壓在**開始用藥的第一週**。inavolisib 仿單即要求第 1 週每 3 天測一次空腹血糖 [label_inavolisib.md]【L1】；alpelisib 仿單要求前 2 週每週至少一次 [label_alpelisib.md]【L1】。若照一般 T2DM 的「3 個月回診」節奏處理，必然來不及。

**(2) 為何 hepatic glucose output 會「主動增加」，而不只是「攝取減少」？**
兩條肝內路徑同時鬆綁：
- **FOXO1 去抑制**：AKT 活性下降 → FOXO1 不再被磷酸化排出核外 → PEPCK 與 G6PC 表現上升 → gluconeogenesis↑ [Mech_Huang_ObesityT2D_2018.md] 📄【L5】
- **GSK3 去抑制 + 肝醣分解**：GSK3 恢復抑制 glycogen synthase，肝醣合成↓；同時「blocking insulin signaling promotes glycogen breakdown in the liver」[InsulinFeedback_Hopkins_2018.md] 📄【L5】

> **可執行推論（此推論本身為【L5】，但對應到已落地的【L3】飲食建議）**：肝醣庫存是急性高血糖的第一個彈藥庫。因此「限制碳水」在機轉圖上作用於**上游**，而非只是「少吃糖」——見 B-4。

**(3) 為何會出現 compensatory hyperinsulinemia，而不是單純高血糖？**
β cell 本身的 glucose sensing 並未被藥物破壞（藥物阻斷的是**周邊組織對 insulin 的反應**，不是 insulin 的分泌）。血糖上升 → β cell 代償性釋放大量 insulin，這正是高血糖「usually transient」的原因 [InsulinFeedback_Hopkins_2018.md] 📄【L5】。
臨床上這產生一個關鍵的**分岔**：

| β cell 儲備 | 表現 | 臨床意涵 |
|---|---|---|
| 儲備充足（血糖正常、非肥胖） | 血糖尖峰後自行回落，可能只表現為 grade 1–2 | 仍會有 hyperinsulinemia，只是血糖看不出來 [Mgmt_Goncalves_2022.md] 📄【L3】 |
| 儲備不足（prediabetes、T2DM、高齡、肥胖） | 持續高血糖、grade 3–4、需多重藥物 | SOLAR-1 中 prediabetes 者發生率與嚴重度較高 [Mgmt_Goncalves_2022.md] 📄【L4】；INAVO120 亦顯示 baseline 危險因子分層差異 [INAVO120_Safety_Im_2026.md] 📄【L2】 |
| 儲備嚴重不足／急性代償失敗 | DKA、HHS | 兩藥仿單皆載有上市後**致死性** ketoacidosis：alpelisib「Fatal cases of ketoacidosis have occurred in the postmarketing setting」[label_alpelisib.md]【L1】；inavolisib「Ketoacidosis with a fatal outcome has occurred in the postmarketing setting」[label_inavolisib.md]【L1】 |

> **⚠️ 禁忌提醒（使用者明確要求）**：上述機轉**不構成延遲 insulin 的理由**。在 DKA／HHS／嚴重高血糖，insulin 是救命治療。詳見 B-5。

### 為什麼這是 on-target effect —— 三個獨立來源的一致用語
- 「Hyperglycemia, an **on-target adverse effect** of PI3Kα inhibition」[SGLT2i_Borrego_2024.md] 📄【L2/L5】
- 「Hyperglycemia is a particularly challenging **on-target class effect** of PI3K inhibitors」[Consensus_Tankova_2022.md] 📄【L3】
- 「hyperglycemia can be considered an expected **"on-target" effect** of PI3K inhibition」[Mgmt_Goncalves_2022.md] 📄【L3】
- 「on-target side effects, such as hyperglycemia, which occur **due to wild-type inhibition**」[ToxMgmt_Jhaveri_2026.md] 📄【L3】

**on-target 的三個可操作推論：**
1. **可預期 → 應該前置處理，而非事後救火。** 高血糖「is predictable, readily identifiable, and generally manageable」[Consensus_Tankova_2022.md] 📄【L3】。
2. **與劑量／曝露同源 → 停藥即快速回復。** alpelisib 仿單註腳明言：insulin 在多數情況下可能非必要，「given the short half-life of PIQRAY and the expectation of glucose levels normalizing after interruption of PIQRAY」[label_alpelisib.md]【L1】。個案報告亦顯示停藥後高血糖與 ketoacidosis 快速緩解 [DKA_Loke_2025.md] 📄【L4】；inavolisib HHS 個案的 insulin 需求由 46 IU/day 在一週內完全停用 [Inavolisib_HHS_Li_2026.md] 📄【L4】。
3. **不能用「換一個 PI3Kα inhibitor」來規避。** 因為問題出在 wild-type p110α，不是特定分子的結構缺陷 [Mech_Fruman_Cell_2017.md] 📄【L5】。

---

## B-3. Q2 —— Hyperinsulinemia 是否可能重新活化腫瘤 PI3K signaling？這是臨床證據還是前臨床推論？

### 誠實的分層回答

| 命題 | 證據來源與物種 | 等級 | 判定 |
|---|---|---|---|
| ① PI3Ki 造成血糖上升並伴隨 insulin／C-peptide 上升 | 小鼠（多種 INSR/IGFR、PI3K、AKT、mTOR 抑制劑）[InsulinFeedback_Hopkins_2018.md] 📄；大鼠（BN、ZDF，alpelisib 誘發 hyperglycemia and hyperinsulinemia）[SGLT2i_Borrego_2024.md] 📄 | 【L5】 | **動物已確立** |
| ①' 人體亦出現 hyperinsulinemia | 「hyperinsulinemia has also been observed in subjects treated with alpelisib and other PI3Kis in clinical trials and in clinical practice」[Mgmt_Goncalves_2022.md] 📄 | 【L3 綜述引述】 | **人體有敘述性支持，但本回顧未取得原始定量數據** |
| ② insulin 能在藥物存在下重新活化 PI3K–AKT–mTORC1 | 細胞（KPC cells + 10 ng/mL insulin → pAKT 部分回復、pS6 幾乎完全回復）[InsulinFeedback_Hopkins_2018.md] 📄 | 【L5】 | **僅細胞／小鼠** |
| ③ 抑制 insulin feedback 能提升 PI3Ki 抗腫瘤療效 | 小鼠 xenograft／allograft：ketogenic diet 與 SGLT2i 降低血糖與 c-peptide 並降低腫瘤 pS6；shIR 敲低 insulin receptor 後 BYL-719 造成腫瘤縮小；外源性 insulin 可「rescue」掉 ketogenic diet 的療效增益 [InsulinFeedback_Hopkins_2018.md] 📄 | 【L5】 | **僅小鼠** |
| ④ **人體上「降低 insulin → 提升 PI3Ki 療效」有直接證據嗎？** | — | — | **本回顧未取得可驗證來源。** |

### ③ 的關鍵數字（皆為小鼠，【L5】）
在攜帶 KPC allograft 的 C57BL/6 小鼠，單劑 BKM120 前先給 metformin、SGLT2i 或 ketogenic diet：

| 前置處置 | 血糖（two-way RM ANOVA p） | c-peptide（unpaired t-test p） | 腫瘤 pS6 陽性細胞（t-test p） |
|---|---|---|---|
| metformin | 0.2136（**不顯著**） | 0.7566（**不顯著**） | 0.6186（**不顯著**） |
| SGLT2i（canagliflozin） | <0.0001 | 0.0386 | <0.0001 |
| ketogenic diet | 0.007 | 0.0117 | <0.0001 |

[InsulinFeedback_Hopkins_2018.md] 📄【L5】

> **必須注意的反直覺結果**：在這個急性模型中，**metformin 對 PI3Ki 誘發的血糖／insulin 尖峰與腫瘤 mTORC1 訊號幾乎沒有影響**（三個 p 值皆不顯著）[InsulinFeedback_Hopkins_2018.md] 📄【L5】。這與臨床上以 metformin 作為第一線處置的做法（見 B-5）並不矛盾——臨床目標是**控制慢性高血糖以維持 dose intensity**，而非「消滅 insulin spike」。**不可把 metformin 說成是「阻斷 insulin feedback」的藥。**

### ④ 人體證據的現況 —— 據本地檔案如實陳述
- **最接近人體訊號的一筆，來自 glioblastoma 而非乳癌，且本地僅有 abstract（📌）**：Noch 等人回溯分析 buparlisib 的 phase 2 GBM 試驗，abstract 陳述「hyperglycemia was an independent factor associated with poor progression-free survival in patients with GBM」以及「PI3K inhibition increased insulin receptor activation… in tumor tissue from these patients」[InsulinFeedback_Noch_2023.md] 📌【L5/L4】。
  → **這是「高血糖與較差 PFS 相關」的關聯性觀察，不是「降低 insulin 可改善療效」的介入性證據；且本地無全文，不得對其方法學細節作斷言。**
- **SGLT2i 的人體資料只證明高血糖被控制，未證明療效被改善**：Borrego 等人以 SOLAR-1 與 BYLieve 中使用 SGLT2i 者（n = 19）對比 propensity-score 配對的未使用者（n = 74），結果為 grade ≥3 高血糖 AE 與導致 alpelisib 劑量調整／中斷／停藥之高血糖 AE 分別低 **4.9 倍與 6.4 倍**，相對風險下降 70.6% 與 35.7% [SGLT2i_Borrego_2024.md] 📄【L2/L4，探索性】。**其臨床終點是高血糖事件，不是 PFS/OS。**（動物端則顯示「Alpelisib antitumor efficacy was maintained when used with dapagliflozin in tumor-bearing rats」——是「維持」，不是「增強」[SGLT2i_Borrego_2024.md] 📄【L5】。）
- **專門檢驗此假說的人體試驗仍未讀出結果**：TIFA（NCT05090358, Targeting Insulin Feedback to Enhance Alpelisib）為 phase 2 隨機三臂（ketogenic diet／low-carbohydrate diet／canagliflozin），**實際收案 15 人，主要終點為 12 週 grade 3/4 高血糖-free rate，狀態 ACTIVE_NOT_RECRUITING**[trials_ongoing.md] 📌【L2-登錄】。
  → **即使讀出，其主要終點也是高血糖，不是腫瘤療效；樣本數亦不足以回答療效問題。**
- 專家共識的措辭同樣保守：「The hyperinsulinemia… **may** provide breast cancer cells with a survival mechanism and reduce the efficacy of alpelisib **as demonstrated in preclinical studies**」[Consensus_Tankova_2022.md] 📄【L3】；「Preclinical data suggest that the resulting hyperinsulinemia **can partially reactivate** the PI3K pathway」[Delphi_Gallagher_2024.md] 📄【L3】。

### Q2 結論（請直接引用此段）
> **「Insulin feedback 會削弱 PI3Kα inhibitor 療效」目前是一個機轉上高度可信、但在人體上尚未被直接證實的假說。其核心證據來自細胞株與小鼠 xenograft/allograft 模型【L5】。人體端目前只有：(a) 高血糖與 PI3Ki 治療下較差 PFS 的關聯性觀察（GBM，本地僅 abstract）【L5/L4】；(b) SGLT2i 可改善高血糖並減少劑量調整的探索性配對分析——但終點是高血糖而非療效【L2/L4】。本回顧未取得任何顯示「在人體中降低 insulin 可提升 PI3Kα inhibitor 抗腫瘤療效」的直接證據。**
>
> 因此，臨床上「insulin-sparing」的正當理由應建立在**兩個已被人體資料支持的目標**上：① 維持 dose intensity（SOLAR-1 中 median dose intensity ≥248 mg/day 者較 <248 mg/day 者觀察到相對較長的 median PFS [Delphi_Gallagher_2024.md] 📄【L2 事後分析】）；② 避免 DKA/HHS 等可致死併發症【L1】。**而非建立在「避免餵養腫瘤」這個尚屬前臨床的推論上。**

---

## B-4. Ketogenic／低碳水飲食與 SGLT2i 在機轉圖上的位置

### 作用點對照

```
[肝醣庫存] ──低碳水／ketogenic diet 在此耗竭彈藥庫──┐
                                                    ▼
p110α⊣ → AKT↓ → GLUT4↓ / FOXO1↑ / GSK3↑ → 血糖↑ ──SGLT2i 在此把糖倒掉──┐
                                                                        ▼
                                                            β cell 代償 → insulin↑
                                                                        ▼
                                                            （假說）腫瘤 PI3K 再活化
```

| 介入 | 在圖上的節點 | 機轉根據 | 等級 |
|---|---|---|---|
| **ketogenic / 低碳水飲食** | **上游**：肝醣庫存與碳水負荷 | 「The rationale for using a ketogenic diet was to **deplete hepatic glycogen stores** and thereby limit the acute release of glucose from the liver that occurs following PI3K inhibition」[InsulinFeedback_Hopkins_2018.md] 📄 | 【L5】 |
| **SGLT2i** | **中游**：血糖池本身（腎小管再吸收） | 「SGLT2 inhibitors inhibit the glucose transporters responsible for reabsorption of glucose in the kidney… The resulting glycosuria lowers the plasma glucose level and **decreases hyperinsulinemia**」[Consensus_Tankova_2022.md] 📄 | 【L3】 |
| **metformin** | 提升 insulin sensitivity、降低基礎血糖與 insulin | 「biguanides… increase systemic insulin sensitivity and reduce basal blood glucose and insulin levels, **though systemic insulin is typically still elevated**」[Mech_Fruman_Cell_2017.md] 📄 | 【L5】 |
| **sulfonylurea / meglitinide** | **反向作用**：直接推高 insulin | 「insulin sensitizers… are preferable to insulin secretagogues… due to the deleterious effect of insulin on the PI3K blockade, **as demonstrated in animal models**」[Consensus_Tankova_2022.md] 📄 | 【L3】（其機轉理由為【L5】） |

### ⚠️ 關於 ketogenic diet，兩份【L3】共識彼此不一致 —— 必須誠實呈現

| 立場 | 來源 | 具體內容 |
|---|---|---|
| **不建議 very-low-carbohydrate／ketogenic** | [Consensus_Tankova_2022.md] 📄【L3】 | 理由有四：(1) 常不易耐受或不可持續；(2) 會造成尿酮陽性，「may be misinterpreted as alpelisib-induced ketoacidosis」，若同時用 SGLT2i 更易混淆；(3) 前臨床研究中 ketogenic diet 對腫瘤異種移植效果最好，但「the worst effect on animal well-being」；(4) 另一份小鼠研究顯示短期 ketogenic diet 誘發的肝臟 insulin resistance 比高脂飲食更嚴重。故建議**中度碳水限制**：碳水約占每日熱量 30–40%（約 200 g），以複合碳水為主，避免單醣。 |
| **可以考慮 ketogenic** | [Delphi_Gallagher_2024.md] 📄【L3】 | 起始 alpelisib 前，所有病人建議低碳飲食（60–130 g/day）；「it **may also be appropriate** to recommend a ketogenic diet (total carbohydrate intake of <50 g/day) and/or pre-treatment fasting」。 |
| **試驗中之操作型定義** | [ToxMgmt_Jhaveri_2026.md] 📄【L3】 | SOLAR-1 與 INAVO120 對 FBG ≥100 mg/dL 者建議「small frequent meals, a low-carbohydrate and high-fiber diet, balancing carbohydrates over the course of the day」。 |
| **另一份綜述之數字** | [Mgmt_Goncalves_2022.md] 📄【L3】 | 碳水限制至 130 g/day；必要時可進一步限制至 <100 g/day。 |

> **給臨床醫師的可執行折衷（本節綜合建議，【L3】）**
> 1. **所有病人**：起始前即衛教低碳、高纖、複合碳水、分餐——這是四份來源皆同意的最低共識 [Consensus_Tankova_2022.md][Delphi_Gallagher_2024.md][ToxMgmt_Jhaveri_2026.md][Mgmt_Goncalves_2022.md] 📄【L3】。
> 2. **不常規推 ketogenic diet**。若病人已有食慾不佳、體重下降或腹瀉，ketogenic diet 的耐受性與熱量攝取風險超過其（仍屬【L5】的）理論利益 [Consensus_Tankova_2022.md] 📄【L3】。
> 3. **若採用低碳／ketogenic，必須先跟團隊講好「尿酮陽性≠DKA」的判讀規則**，尤其在合併 SGLT2i 時 [Consensus_Tankova_2022.md] 📄【L3】；SGLT2i 本身有 euglycemic DKA 風險 [Delphi_Gallagher_2024.md] 📄【L3】，且本地有 taselisib 併用 canagliflozin 後發生 ketoacidosis 的個案 [EuglycemicDKA_Bowman_2017.md] 📄【L4】。判讀原則請對照 SGLT2i-DKA 國際共識 [DKA_Danne_Consensus_2019.md] 📄【L3】。
> 4. **高蛋白飲食前先評估腎功能** [Consensus_Tankova_2022.md] 📄【L3】——癌症病人常有脫水與腎功能波動；alpelisib 之嚴重不良反應中 acute kidney injury 佔 2.5% [label_alpelisib.md]【L1】。
> 5. **Delphi 專家不要求在 SGLT2i 期間常規監測酮體**，但可由醫師自行決定 [Delphi_Gallagher_2024.md] 📄【L3】。在腹瀉、脫水、食慾不佳的癌症病人身上，本節建議採取較積極的酮體監測門檻（此為推論，非直接引自來源）。

---

## B-5. 「insulin-sparing」的處置邏輯 —— 以及它的邊界

### 為什麼是 insulin-sparing（順序，不是禁令）

| 順位 | 藥物 | 在機轉圖上的合理性 | 來源 | 等級 |
|---|---|---|---|---|
| 1 | metformin（500 mg 起，每 3–4 週加 500 mg，上限 2000 mg；優先 XR） | insulin sensitizer，不推高 insulin | [ToxMgmt_Jhaveri_2026.md] 📄；[Consensus_Tankova_2022.md] 📄（500→2000 mg/day） | 【L3】；仿單亦列 metformin 為適用藥 [label_alpelisib.md][label_inavolisib.md]【L1】 |
| 2 | SGLT2i | 直接把血糖倒掉 → 同時降 insulin | [Consensus_Tankova_2022.md] 📄【L3】；人體探索性資料 [SGLT2i_Borrego_2024.md] 📄【L2/L4】 | 【L2/L3】 |
| 2–3 | pioglitazone（15–45 mg） | insulin sensitizer；但起效需 6–8 週，不可單獨作第一線 | [Consensus_Tankova_2022.md] 📄 | 【L3】 |
| 3 | GLP-1 RA（BMI >30 者） | — | [ToxMgmt_Jhaveri_2026.md] 📄；**但須考量 cachexia 與 malnutrition 風險** | 【L3】 |
| 4 | DPP-4i | Delphi 認為不適合作第一／二線，可作第三線 | [Delphi_Gallagher_2024.md] 📄 | 【L3】 |
| 5 | sulfonylurea | 直接推高 insulin；且有 rebound hypoglycemia 風險 | 「Sulfonylureas should be avoided as primary treatment」[Consensus_Tankova_2022.md] 📄；「sulfonylurea should be avoided… due to the risk of rebound hypoglycemia」[ToxMgmt_Jhaveri_2026.md] 📄 | 【L3】 |
| 6 | insulin | 作為 rescue | 見下 | 【L1】【L3】 |

### ⚠️ insulin 的紅線 —— 不可因為理論而延誤

1. **DKA / HHS / 嚴重高血糖時，insulin 是治療，不是選項。** DKA「should be managed with fluid replacement using saline solution, followed by insulin treatment and potassium replacement」[ToxMgmt_Jhaveri_2026.md] 📄【L3】。alpelisib 仿單對 grade 4（FPG >500 mg/dL）明確要求「administer intravenous hydration and consider appropriate treatment (e.g., intervention for electrolyte/ketoacidosis/hyperosmolar disturbances)」並於 24 小時內複測 [label_alpelisib.md]【L1】。
2. **實際個案中 insulin 是有效且必要的**：inavolisib 相關 HHS 個案於急診以 insulin pump 處置後血糖下降，最高需求 46 IU/day，隨 insulin resistance 緩解於一週內完全停用 [Inavolisib_HHS_Li_2026.md] 📄【L4】；alpelisib 相關 DKA 個案在 insulin 與停藥後高血糖與酮酸中毒迅速緩解 [DKA_Loke_2025.md] 📄【L4】；另有病例需 38 IU/day（0.68 U/kg）之 basal-bolus regimen [FGM_PlaPeris_2022.md] 📄【L4】。
3. **真正的 insulin-sparing 意涵是「短期、目標導向、且要預先規劃退場」**：alpelisib 仿單註腳 3 寫明「insulin may be used for 1-2 days until hyperglycemia resolves. However, this may not be necessary in the majority of PIQRAY-induced hyperglycemia, given the short half-life of PIQRAY」[label_alpelisib.md]【L1】。
4. **退場失控會造成低血糖**：Delphi 明確警告「Exercise caution on the use of insulin when holding ALP. Holding ALP may likely cause hyperglycemia to resolve, and adding insulin may lead to hypoglycemia」[Delphi_Gallagher_2024.md] 📄【L3】。INAVO120 的措辭更直接：「Insulin or sulphonylureas were recommended to be administered with caution, **as subsequent inavolisib interruption could lead to rapid insulin level escalation**」[INAVO120_Safety_Im_2026.md] 📄【L2】。
   → **可執行規則：只要決定停／減 PI3Kα inhibitor，同一份醫囑就要同步寫下 insulin 的減量計畫與低血糖監測頻率。**
5. **臨床現實中 insulin 的使用比例並不低**：INAVO120 中 11/162（6.8%）病人使用 insulin，中位使用期 5.0 天（範圍 1.0–539.0，上限來自兩位長期用 insulin 者）[INAVO120_Safety_Im_2026.md] 📄【L2】；仿單記為 7%（11/162）[label_inavolisib.md]【L1】。SOLAR-1 中，糖尿病者 12 人中 5 人、prediabetes 者 159 人中 34 人、血糖正常者 113 人中 13 人使用過 insulin；其中 33 人為長期（>2 天）、19 人為 rescue [ToxMgmt_Jhaveri_2026.md] 📄【L3 引述 L2 資料】。

### 癌症病人特有的干擾因子（必須同時處理）

| 因子 | 對本機轉圖的影響 | 來源／等級 |
|---|---|---|
| 腹瀉 | metformin 本身會腹瀉，與 alpelisib 之腹瀉疊加；「Maintenance of alpelisib therapy, rather than metformin, is preferred in cases of diarrhea」；可減量、換 XR，嚴重時改 pioglitazone 或 SGLT2i | [Consensus_Tankova_2022.md] 📄【L3】 |
| 脫水／體液不足 | 高血糖 →滲透性利尿 → 血容積下降 → 血漿滲透壓上升 → HHS | [Inavolisib_HHS_Li_2026.md] 📄【L4】；「Acute hyperglycemia… can cause volume depletion, electrolyte disturbances, catabolic weight loss」[Delphi_Gallagher_2024.md] 📄【L3】 |
| 體重下降／食慾不佳 | 限制 ketogenic diet 與 GLP-1 RA 的可行性；GLP-1 RA 需權衡 cachexia 與 malnutrition | [ToxMgmt_Jhaveri_2026.md] 📄【L3】 |
| 腎功能波動 | 影響 metformin（GFR >45 才用到 2000–2500 mg/day）與 SGLT2i；高蛋白飲食前須評估腎功能 | [Delphi_Gallagher_2024.md] 📄【L3】；[Consensus_Tankova_2022.md] 📄【L3】 |
| 併用 corticosteroid | alpelisib 仿單將「use of concomitant systemic corticosteroids」列為需更密集監測血糖的危險因子 | [label_alpelisib.md]【L1】 |
| 靜脈輸糖／營養補充品 | 「it may also be important to think about how common clinical practices such as IV glucose administration, glucocorticoid use, or providing patients with glucose-laden nutritional supplements may impact therapeutic responses」 | [InsulinFeedback_Hopkins_2018.md] 📄【L5】 |
| 血糖目標不宜過嚴 | 建議 CGM 下維持 70–250 mg/dL 佔 >90% 時間；餐後 <250 mg/dL 為合理目標，以「prevent catabolic wasting」 | [ToxMgmt_Jhaveri_2026.md] 📄【L3】 |

---

## B-6. alpelisib 與 inavolisib：機轉差異，以及是否轉譯為不同的高血糖表現

### 機轉差異（【L5】，來自本地全文之前臨床研究）

| 面向 | alpelisib (BYL719) | inavolisib (GDC-0077) |
|---|---|---|
| 對 p110α 的**生化**選擇性 | α-selective；但對 WT 與 mutant p110α 酵素之 Ki **無顯著差異** [Preclin_Song_Inavolisib_2022.md] 📄 | 同樣對 WT 與 mutant 酵素之 Ki 無顯著差異；但「significant improvement in PI3Kα isoform selectivity over both taselisib and BYL719」[Preclin_Song_Inavolisib_2022.md] 📄 |
| 是否誘導 mutant p110α 降解 | **否**。「p110a depletion was not observed with 40 mg/kg BYL719」；「taselisib, GDC-0077… result in p110a degradation, whereas others (BYL719, pictilisib) do not」[Preclin_Song_Inavolisib_2022.md] 📄 | **是**。經 ubiquitin–proteasome 途徑；MG132 與 UAE1 inhibitor 可回復；降解優先發生於**細胞膜區隔**，依賴 **p85β** 與 **RTK（HER2/HER3）活性** [Preclin_Song_Inavolisib_2022.md] 📄 |
| 蛋白半衰期 | — | WT p110α ≈ 26.7 h；H1047R mutant 基礎狀態 ≈ 9.6 h，加 taselisib 後縮短至 ≈ 4 h [Preclin_Song_Inavolisib_2022.md] 📄 |
| 降解在哪些細胞才有優勢 | — | 依賴 RTK 活性；**HER2-amplified** 細胞株全部可見 p110α 降解，HER2-negative 者多數不可；在 HER2-negative 細胞中「the degrader mechanism of action **may not provide additional benefit** over drugs with a nondegrader mechanism」[Preclin_Song_Inavolisib_2022.md] 📄 |

> **關鍵推論（【L5】，但對回答使用者的問題至為重要）**
> inavolisib 的 mutant-selectivity **不是在酵素抑制層次，而是在「突變蛋白降解」層次**，且此降解機制**依賴 RTK 活性、在 HER2-negative 腫瘤中多半不啟動**[Preclin_Song_Inavolisib_2022.md] 📄。而目前 inavolisib 的核准適應症族群為 HR+/HER2-negative [label_inavolisib.md]【L1】。
> **因此，不能宣稱「inavolisib 因為會降解突變型 p110α，所以比較不傷代謝組織」。** 代謝組織（肌肉、肝、脂肪）表現的是 **wild-type** p110α，而 Song 等人明確指出「WT p110a protein expression was not affected」by degradation 機制 [Preclin_Song_Inavolisib_2022.md] 📄——換言之，降解機制根本繞不開 wild-type 抑制這條致高血糖路徑。Fruman 也把「drugs that have higher selectivity for mutant versus wild type PI3K」列為**尚待實現**的解方 [Mech_Fruman_Cell_2017.md] 📄。

### 高血糖表現是否不同？—— 數字並列，但**不做跨試驗優劣判定**

| 指標 | alpelisib（PIQRAY 仿單） | inavolisib（ITOVEBI 仿單 / INAVO120） |
|---|---|---|
| 發生率 | Hyperglycemia 報告於 **65%**[label_alpelisib.md]【L1】 | Increased fasting glucose 發生於 **85%**[label_inavolisib.md]【L1】；INAVO120 中 hyperglycaemia（grouped term, CTCAE v5.0）**58.6%（95/162）**[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| Grade 3 | **33%**（FPG >250–500 mg/dL）[label_alpelisib.md]【L1】 | 仿單 **12%**（FPG >250–500）[label_inavolisib.md]【L1】；INAVO120 AE 層級 grade 3 **5.6%（9/162）**，檢驗值層級（CTCAE v4.0）grade 3 **11.5%（18/157）**[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| Grade 4 | **3.9%**（FPG >500 mg/dL）[label_alpelisib.md]【L1】 | 仿單 **0.6%**[label_inavolisib.md]【L1】；INAVO120 無 grade 4–5 AE，檢驗值層級 grade 4 為 1/157（0.6%）[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| Ketoacidosis | 試驗中 **0.7%（n=2）**；上市後有致死病例 [label_alpelisib.md]【L1】 | INAVO120 中 **無 DKA** [INAVO120_Safety_Im_2026.md] 📄【L2】；但上市後有致死性 ketoacidosis [label_inavolisib.md]【L1】 |
| 中位發生時間 | grade ≥2：**15 天（5–517）**[label_alpelisib.md]【L1】 | **7 天（2–955）**[label_inavolisib.md]【L1】[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| 中位改善／緩解時間 | grade ≥2 有 ≥1 grade 改善者（n=153）中位 **8 天（2–65）**[label_alpelisib.md]【L1】 | FPG >160 mg/dL 者 96%（52/54）有 ≥1 grade 改善，中位 **8 天（2–43）**[label_inavolisib.md]【L1】；AE 中位緩解時間 **16.0 天（IQR 5.0–50.0）**[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| 因高血糖而減量 | **29%**[label_alpelisib.md]【L1】 | **2.5%**[label_inavolisib.md]【L1】[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| 因高血糖而停藥 | **6%**[label_alpelisib.md]【L1】 | **1.2%**（仿單）[label_inavolisib.md]【L1】；INAVO120 為 0.6%（1/162）[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| 因高血糖而中斷 | 本回顧未取得仿單中之對應百分比 | **28%**[label_inavolisib.md]【L1】；INAVO120 27.2%（44/162）[INAVO120_Safety_Im_2026.md] 📄【L2】 |
| 使用 insulin 比例 | SOLAR-1：糖尿病 5/12、prediabetes 34/159、正常 13/113 [ToxMgmt_Jhaveri_2026.md] 📄【L3 引述】 | **7%（11/162）**[label_inavolisib.md]【L1】 |

> **⚠️ 這張表不可被讀成「inavolisib 的高血糖比較輕」。理由（皆有本地來源支持）：**
> 1. **分級標準不同**：alpelisib 仿單 Table 3 表註明示採 **CTCAE v4.03**[label_alpelisib.md]【L1】；INAVO120 之 AE 採 **NCI-CTCAE v5.0**[INAVO120_Safety_Im_2026.md] 📄【L2】。而「hyperglycemia grade no longer corresponds to specific glucose ranges in CTCAE v5」[ToxMgmt_Jhaveri_2026.md] 📄【L3】。同一份 INAVO120 資料以 v5.0 AE 計為 grade 3 5.6%，以 v4.0 檢驗值計則為 11.5%——**同一群病人，兩倍差距，只因分級規則不同** [INAVO120_Safety_Im_2026.md] 📄【L2】。
> 2. **端點定義不同**：alpelisib 仿單記的是「Hyperglycemia」，inavolisib 仿單記的是「Increased fasting glucose」（85%）——後者是實驗室異常，不是 AE 通報 [label_alpelisib.md][label_inavolisib.md]【L1】。
> 3. **合併治療與族群不同**：alpelisib + fulvestrant vs inavolisib + palbociclib + fulvestrant，且 INAVO120 為 endocrine-resistant 一線族群 [label_alpelisib.md][label_inavolisib.md]【L1】。
> 4. **管理強度不同**：INAVO120 允許預防性抗高血糖治療（研究者判斷下可於 C1D1 起始），且對高血糖中斷後給予最多 7 天恢復期以避免過早減量或停藥 [INAVO120_Safety_Im_2026.md] 📄【L2】；SOLAR-1 則是在收案過半後才修訂 protocol 加強監測 [Delphi_Gallagher_2024.md] 📄【L3】。
> 5. **本回顧未取得 head-to-head 比較試驗**。SOLAR-1 與 INAVO120 主論文在本地僅有 abstract（📌），其劑量調整表與 subgroup 不得引用 [inventory.md]。
>
> **可以說的是**：兩藥的高血糖**發生時間點都極早**（中位 7–15 天）、**改善都很快**（中位約 8 天）、**都有上市後致死性 ketoacidosis**、**兩者的仿單都把 metformin／SGLT2i／insulin sensitizer 列為處置選項**[label_alpelisib.md][label_inavolisib.md]【L1】。也就是說，**機轉圖與處置邏輯對兩藥是共通的；差異在於監測時程的密度**（inavolisib 第 1 週每 3 天，alpelisib 前 2 週每週）[label_inavolisib.md][label_alpelisib.md]【L1】。

### 一個必須點名的空白
`inavolisib` 的高血糖是否因 mutant degradation 機制而在**代謝組織**上有任何差異（例如對 wild-type p110α 的曝露時間更短），**本回顧未取得可驗證來源**。Song 等人的研究終點是腫瘤細胞與 xenograft 的 p110α 蛋白量與 pAKT，**未報告代謝組織之血糖或 insulin 數據** [Preclin_Song_Inavolisib_2022.md] 📄。`Preclin_Hanan_Inavolisib_2022`（GDC-0077 藥物化學）與 `Preclin_Fritsch_BYL719_2014`（BYL719 特性描述）在本地**僅有 abstract**（📌），不得對其內文細節作斷言 [inventory.md]。

---

## B-7. 一頁式重點（可直接作為投影片講稿）

1. **PIK3CA 編碼的 p110α，同時是腫瘤的驅動者與 insulin 代謝的執行者。** 治療劑量下藥物打不掉這個重疊，所以高血糖是 **on-target**，不是意外 [Mech_Fruman_Cell_2017.md]【L5】[SGLT2i_Borrego_2024.md]【L2】。
2. **級聯**：p110α⊣ → AKT↓ →（GLUT4 移位↓ / FOXO1 去抑制 → PEPCK・G6PC↑ / GSK3 去抑制）→ 周邊攝取↓ + 肝糖輸出↑ → 急性高血糖（數小時內）→ β cell 代償 → hyperinsulinemia [Mech_Huang_ObesityT2D_2018.md][InsulinFeedback_Hopkins_2018.md]【L5】。
3. **表現型由 β cell 儲備決定**：儲備夠 → 一過性；儲備不足 → G3/G4、DKA、HHS [ToxMgmt_Jhaveri_2026.md]【L3】[label_alpelisib.md][label_inavolisib.md]【L1】。
4. **「insulin 回頭餵養腫瘤」在小鼠與細胞成立，在人體尚未被直接證實。** 不要在病人面前把它講成已知事實 [InsulinFeedback_Hopkins_2018.md]【L5】。
5. **insulin-sparing 的正當理由是「維持 dose intensity + 避免 DKA/HHS」**，不是「避免餵養腫瘤」[Delphi_Gallagher_2024.md]【L2 事後分析】【L1】。
6. **Ketogenic diet 在圖上作用於肝醣庫存（上游），SGLT2i 作用於血糖池（中游）**；但 ketogenic diet 在【L3】共識間有分歧，且在食慾不佳／體重下降／腹瀉的病人身上風險大於（仍屬【L5】的）利益 [InsulinFeedback_Hopkins_2018.md][Consensus_Tankova_2022.md][Delphi_Gallagher_2024.md]。
7. **alpelisib 與 inavolisib 的機轉差異（degrader vs non-degrader）目前無法被證明轉譯為代謝組織上的差異**；跨試驗的高血糖數字因 CTCAE 版本與端點定義不同而不可直接相比 [Preclin_Song_Inavolisib_2022.md]【L5】[ToxMgmt_Jhaveri_2026.md]【L3】[INAVO120_Safety_Im_2026.md]【L2】。
8. **在小鼠急性模型中，metformin 對 PI3Ki 誘發的血糖／c-peptide 尖峰與腫瘤 pS6 皆無顯著影響**（p = 0.2136 / 0.7566 / 0.6186）——臨床用 metformin 的理由是慢性血糖控制，不是阻斷 insulin feedback [InsulinFeedback_Hopkins_2018.md]【L5】。

---

## B-8. 本節明列之證據空白（本回顧未取得可驗證來源）

1. 人體中「降低 insulin → 提升 PI3Kα inhibitor 抗腫瘤療效」之直接介入性證據。
2. 人體 PI3Kα inhibitor 治療下的 serial insulin / C-peptide 定量曲線（僅有 [Mgmt_Goncalves_2022.md] 之敘述性陳述與個案數據）。
3. alpelisib vs inavolisib 之 head-to-head 高血糖比較。
4. inavolisib 之 mutant p110α degradation 是否改變代謝組織之 wild-type p110α 曝露。
5. `InsulinFeedback_Noch_2023`（GBM insulin feedback）之全文——本地僅 abstract（📌）。
6. `Preclin_Fritsch_BYL719_2014`、`Preclin_Hanan_Inavolisib_2022`、`Mech_Drullinsky_2020`、`Mech_Crouthamel_AKT_2009`、`Mech_Goncalves_NEJM_2018` 之全文——本地僅 abstract（📌），本節未對其內文細節作斷言 [inventory.md]。
7. SOLAR-1、INAVO120、BYLieve 主論文之劑量調整表與 subgroup——本地僅 abstract（📌）[inventory.md]。
8. TFDA 之 alpelisib／inavolisib 中文仿單——本回顧未取得；本節【L1】引用皆為 FDA（PIQRAY / ITOVEBI）與 EMA 條目 [label_alpelisib.md][label_inavolisib.md]。
