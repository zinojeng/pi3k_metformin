# 稽核報告：cross-referencer（論斷 ↔ 來源對應查核）

- 稽核日期：2026-07-21
- 稽核範圍：`章節/B、C、D、E、F、G、H、I、K、M`（共 10 檔，約 397 KB）
- 稽核方法：對每個「依據 [X.md]…」型論斷，回到 `原始PDF/X.md` 或 `來源/X.md` 逐字 grep 比對；
  另檢查檔名存在性（dead link）、📄/📌 標記與實際檔案狀態是否一致、跨章節同一數字是否互相矛盾。
- 立場：敵對稽核。預設每個數字都是幻覺，直到 grep 命中為止。

---

## 0. 先講整體結論

**本稿的引文紀律遠高於一般 LLM 生成之文獻回顧。** 抽驗約 130 項可量化論斷，
逐字 grep 命中率極高；未見任何憑空捏造之樣本數、百分比、DOI 或 PMID。

- **dead link to self：0 筆。** 章節中出現的 76 個 `[檔名.md]` 全部實際存在於
  `原始PDF/`、`來源/` 或工作目錄根層（`inventory.md`、`MISSING_FULLTEXT.md`、`citations_round1.md`）。
  （唯一例外 `[檔名.md]` 出現在 B 節閱讀規則的範例文字中，非引用。）
- **claim misattribution：僅 1 筆確認（D-0）、1 筆待議（K-1）。**
- **ghost consensus：0 筆。** 反而多處主動揭露共識間的矛盾（ketogenic diet、GLP-1 RA、
  DPP-4i、ketone 監測），並拒絕調和。
- **synthesis overreach：1 筆確認（D-0）、1 筆待議（I-2-3）。**
  最高風險處（insulin feedback → 臨床禁用 insulin；METALLICA → 全體適用）**沒有被踩到**，
  且被主動、反覆、以明文設防（B-3 結論、B-5、C-2b#5、D-7、E §5/§7、F-3-2、G-3.4、H.3、I-2-1）。

**真正需要修正的問題不在「數字對不對」，而在「檔案狀態標記已經過時」與「跨章節同一數字不一致」。**

---

## 1. 主表：論斷 ↔ 來源查核

> 「是否成立」欄：✅ 成立（逐字 grep 命中）／⚠️ 部分成立（需限縮或補註）／❌ 不成立

### 1-A. 必修項（3 筆）

| # | 論斷（原文摘要） | 章節 | 宣稱來源 | 是否成立 | 幻覺類型 | 建議改寫 |
|---|---|---|---|---|---|---|
| 1 | 「ITACA…**n=23、單臂**」；「期中、探索性、n=23、單臂」 | K-2（K_文獻表.md 第 54 列） | [ITACA_Pancirov_2025.md] | ❌ | **claim misattribution（研究設計誤述）** | 原文逐字：「multicentric, **randomized**, open-label phase IIb ITACA trial…Patients were **randomized into 2 treatment groups**: experimental group (11 patients)…evening…control group (12 patients)…morning」。ITACA 是**隨機兩臂 phase IIb**，本次僅是把兩臂**合併（pooled）**做 exploratory interim。應改為「**多中心、隨機、開放標籤 phase IIb（晚間給藥 11 人 vs 晨間給藥 12 人），本分析為兩臂合併之探索性期中分析**」。M-1 與 M-7 的描述（「prospective, exploratory interim, n=23」「非比較性設計」）正確，K 與 M 目前互相矛盾，須以 M 為準修正 K。 |
| 2 | 「`SOLAR1_AE_Rugo_2020.md`、`INAVO120_Turner_2024.md` 本地**僅有 abstract（📌）**，其內文細節／劑量調整表／subgroup **一律不得引用**」 | C-1 稽核聲明、C-5(1)(2)、D-8、F-5(9)、G-5(8)、I-3(2)、K-1、K-7 | [inventory.md]、各檔 | ❌（**已過時**） | **dead link to self（檔案狀態陳述與磁碟不符）** | 磁碟現況：`原始PDF/SOLAR1_AE_Rugo_2020.md` = **81,200 bytes（全文，2026-07-21 11:59 更新）**；`原始PDF/INAVO120_Turner_2024.md` = **77,873 bytes（全文，同時間）**。兩檔皆晚於各章節寫作時間（11:41–11:50），故章節撰寫時之判斷在當下正確，但**現在已不成立**。須（a）重跑 `來源/inventory.md`，把這兩檔改標 📄；（b）把上列 6 處「未取得全文／不得引用」之聲明改寫或刪除；（c）K-7 之「38 篇全文／31 篇 abstract／55%」統計連帶失效。**在更新前，任何稽核員 grep 這兩檔都會得到與章節聲明相反的結果。** |
| 3 | 「MSKCC 491 例中，接受 **β-／γ-／δ-specific PI3K inhibitor 的病人無任何高血糖事件**」 | D-0（第 12 行） | [RealWorld_Liu_2022.md] | ⚠️→❌ | **synthesis overreach** | 來源逐字只支持「**無高血糖相關之治療中斷事件**」：Abstract「**No events occurred** among patients receiving β-, γ-, or δ- specific PI3K inhibitor」係承接前一句之 dose interruption / reduction / hospitalization；正文「All such **hyperglycemia-associated treatment disruptions** occurred in patients exposed to AKT (5%), α (13%), or pan-PI3K inhibitors (5%), with **none** in patients exposed to PI3K inhibitors specific for isoforms other than α」。**該文未報告 β/γ/δ 組的高血糖發生率為零。** 同句後半（D-0 自己寫的「所有因高血糖導致的治療中斷／減量／住院皆發生在…」）才是正確表述。建議刪除前半句，改為「**無任何高血糖相關之治療中斷／減量／住院事件**（該文未報告該組之高血糖發生率）」。此點特別重要，因為 D-0 正是用它支撐「不可把所有 PI3K inhibitors 當同一類」這條使用者硬規則——論點方向正確，但**證據被說強了一級**。 |

### 1-B. 待議項（6 筆）

| # | 論斷 | 章節 | 宣稱來源 | 是否成立 | 幻覺類型 | 建議改寫 |
|---|---|---|---|---|---|---|
| 4 | METALLICA grade 3–4 腹瀉率：**11.8%** | E §7.6、E 表 §1「風險與注意事項」欄、F-1-2 | [METALLICA_LlombartCussac_2024.md] | ⚠️ | 跨章節不一致（非幻覺） | 兩個數字**都在原文**：Results 段「diarrhoea (46 [67.6%] of 68 patients, **nine [13.2%] grade ≥3**)」；Discussion 段「67.6% of patients experienced any-grade and **11.8% grade 3–4 diarrhoea**」。**G-1.6 已明文稽核並採 13.2%**，但 E 與 F 採 11.8% 且未註記。全稿應統一（建議採 G 之處理：以 Results 之 13.2% 為主，並註明 Discussion 寫 11.8%），否則讀者會認為某一章在編數字。 |
| 5 | alpelisib ≥75 歲之 grade 3–4 高血糖：D 寫 **56% vs 36%**；E 寫 **55% vs 36%** | D-1 表、D-2 表 vs E §3(b) | D：[label_alpelisib.md]；E：[Consensus_Tankova_2022.md] | ⚠️ | 跨章節不一致（非幻覺） | 兩者各自成立：FDA 仿單 §8.5 為 56%，Tankova 引 SOLAR-1 為「55% vs. 36%」。但同一份回顧內出現兩個數字而無交代，會被稽核員判為矛盾。建議擇一為主、另一以括號並陳：「**56%（FDA 仿單 §8.5）／55%（Tankova 引 SOLAR-1）**」。 |
| 6 | METALLICA 之引用分裂為兩個檔名：`[METALLICA_LlombartCussac_2024.md]`（B/C/D/E/F/I/K/M，61 次）與 `[METALLICA_Llombart_2024.md]`（G，60 次） | 全稿 | 兩檔 | ⚠️ | 潛在 ghost consensus（外觀上像兩篇獨立研究） | 兩檔 **PMID 皆為 38638399、PMCID 皆 PMC11024566、DOI 皆 10.1016/j.eclinm.2024.102520**，內容為同一篇之兩次落地。K-7 已明白揭露並「計為 1 篇」——**這點做得對**。但 G 全章單獨使用另一個檔名且無交叉註記，外部讀者／自動化稽核容易把 METALLICA 誤算成兩個獨立來源，強化「預防性 metformin 證據較多」的錯覺。建議：刪除其一（或建 symlink），全稿統一檔名，並在 G 開頭補一行「本章所引 `METALLICA_Llombart_2024.md` 與他章所引 `METALLICA_LlombartCussac_2024.md` 為同一 PMID 38638399」。<br>**同類新問題**：磁碟現已出現第三個重複檔 `原始PDF/MSKCC_RealWorld_Shen_2023.md`（50,517 bytes）與既有 `RealWorld_Shen_2023.md` 重複；`原始PDF/*.md` 實際為 **71 檔**，K-7 寫的「70 個 .md 檔」已過時。 |
| 7 | 「Ismail 2026…**alpelisib 開始後才使用降糖藥的病人，time-on-therapy 反而較長（HR 0.76…）**。這暗示『積極控糖 → 維持藥物暴露』的路徑，其臨床價值可能大於『避免 insulin』的機轉考量」 | I-2-3 | [Claims_Ismail_2026.md] 📌 | ⚠️ | 輕度 synthesis overreach | 數字逐字正確（abstract：median TOT 87.5 天、20.0%→34.3%、81.8% metformin、44% insulin、HR = 0.76, 95% CI 0.61–0.93, p = 0.008），且已正確標 📌。但「起始降糖藥」是**時間相依暴露**，此類 claims 分析天生有 immortal-time bias 與 confounding by indication（活得久／用藥久的人才有機會被開降糖藥）。原文結論用的是「associated with」。建議把「暗示…臨床價值可能大於」降級為「**此為關聯性觀察，且存在 immortal-time bias 與 confounding by indication，不足以支持任何因果或優先順序推論**」。 |
| 8 | K-1 之 SOLAR-1 AE 列，把「G3 32.7%／G4 3.9%、rash 13 天、diarrhea 139 天、**87.1% 用 metformin**、**G≥3 停藥 7.9% vs 18.1%**、**dose intensity 248 mg/day**」全部掛在 [SOLAR1_AE_Rugo_2020.md]，同列卻標 📌「僅 abstract、不可引用內文細節」 | K-1 第 31 列 | [SOLAR1_AE_Rugo_2020.md] | ⚠️ | claim misattribution（來源歸屬不完整）＋ 自相矛盾 | 這些數字**現在**都能在該檔全文中 grep 到（見必修 #2），但撰寫當下該檔為 abstract-only。其中「7.9% vs 18.1%」與「≥248 mg/day」**逐字存在於 `Delphi_Gallagher_2024.md` 第 93 行**（B-3 即是這樣引用的）。合理推斷撰寫時實際來源是 Delphi 轉述，卻只掛了 SOLAR-1 原文檔名。建議改為雙來源標註：`[SOLAR1_AE_Rugo_2020.md]📄（現已落地全文）／轉述見 [Delphi_Gallagher_2024.md]📄`，並移除該列的 📌 標記。 |
| 9 | 「alpelisib：nausea **45–47%**、vomiting **27–30%**、decreased appetite **36–37%**」以單一區間呈現 | M6.1、M9 階段 2 | [label_alpelisib.md] | ⚠️ | 分母混用（非幻覺） | 逐字查核：FDA 表為 nausea 45%／vomiting 27%／decreased appetite 36%；EMA ADR 表為 **133 (46.8%)／84 (29.6%)／105 (37.0%)**。兩者**分母與定義不同**——這正是 C-3(3) 與 I-2-5 花大篇幅警告「FDA 與 EMA 數字不可互換或相加」的那件事。M 章自己把兩者壓成一個區間，與全稿的方法學紅線衝突。建議改寫為「FDA 45%／EMA 46.8%」逐一標示。 |

---

## 2. 使用者五項禁忌之專項檢查

| # | 禁忌 | 判定 | 證據（可 grep） |
|---|---|---|---|
| **1** | 不可把所有 PI3K／AKT inhibitors 當成同一類；alpelisib 與 inavolisib 必須分開陳述 | **✅ 通過**（1 處論證過強，見必修 #3） | 每一章都有明文分隔宣告：B-6 專節比較 degrader vs non-degrader 並**主動否定**「inavolisib 比較不傷代謝組織」之推論（引 Song 2022「WT p110α protein expression was not affected」）；C-2 逐列對照兩藥仿單並標 ⚠️⚠️⚠️；D-0 明文「三者不可互相套用」；E §4、F-0、G §0、H.0(二)、I-2-5、M 全章分列。capivasertib 一律加註「AKT inhibitor，不可外推」；copanlisib/idelalisib/duvelisib 亦被明確排除於 ADA 建議之外。**這一項執行得最徹底。** |
| **2** | 不可把 METALLICA（單臂 phase 2）描述成「已證明所有病人都該用預防性 metformin」 | **✅ 通過（強）** | 反向設防出現在 **6 個章節、至少 11 處**：C-3 附帶警告、D-3「⚠ 四項必要限縮」、E §7「必讀 caveat」列 8 條並以「一句話結論」收束、F-1-2 ⚠️、G-1.7「🔴 不得作出的推論」、I-2-1 六個爭議點、M9 階段 1。所有引用一律同時標註 single-arm／歷史對照／n=68／cohort B n=20（95% CI 5.6–37.8）／腹瀉代價（metformin 減量 36.8%、停用 11.8%、第一週純 metformin 期即 14.7% 腹瀉）／FDA 措辭為 "Consider"。**並額外指出 GO39374 arm F 之反向訊號（有風險因子者早期給 metformin 仍 40.0% grade 3 高血糖）**，明文「METALLICA 的結論不可外推至 inavolisib」。無任何過度外推。 |
| **3** | 不可有任何段落可能導致延誤 DKA/HHS 所需之 insulin（**安全性紅線，最優先**） | **✅ 通過（強）** | 專門的「不得延誤 insulin」段落存在於 **B-5、C-2b#5、D-7、E §5、F-3-2（紅旗表）、G-3.4、H.3、I-2-2 提醒、I-4(5)、M6.4**，共 10 處。關鍵防線：<br>① 明確把 ADA Rec 9.35b 的「reserved for severe hyperglycemia and hyperglycemic crises」讀為「**保留給重症＝重症時是適應症，不是禁用**」（G-3.4、E §5、H.3 三處同樣措辭）。<br>② F-2 流程圖把「紅旗篩檢」放在測 FPG **之前**，任一紅旗即跳過分層直接進急症流程。<br>③ F-3-3 以四個本地個案（inavolisib 72 小時 HHS、alpelisib 血糖 1137 mg/dL DKA、612 mg/dL DKA、rechallenge 後 4 小時 DKA）反證「多為 non-ketotic」不是個別病人的安全保證。<br>④ B-3 結論句明文把 insulin-sparing 的正當理由**從**「避免餵養腫瘤」**改掛**在「維持 dose intensity + 避免 DKA/HHS」。<br>⑤ EuglycemicDKA_Bowman_2017 之作者偏好（非胰島素途徑優於胰島素途徑）被 K-4 主動加註「**本回顧不以此延誤嚴重高血糖／DKA 所需之 insulin**」。<br>**未發現任何一句可被讀成「先觀察、晚點再給 insulin」。** |
| **4** | 不可在未註明來源的情況下混合仿單／共識／個人意見 | **✅ 通過**（1 處待議，見待議 #9） | 每句幾乎都帶 `[檔名.md]` + 【L1–L5】+ 📄/📌 三重標記。少數屬作者推論之處均自行加註：B-4「此為推論，非直接引自來源」；D-2「⚠ 本回顧未取得可驗證來源」；E §6「此權衡本身本回顧未取得可驗證來源，屬臨床判斷」；G-3.3「此為依上述各條之綜合操作建議」；H.2.1「本回顧傾向採較嚴格的一方，但這是判斷，不是證據」。ADA 擷取被截斷處（「there is no evidence that concurrent use of these two medica…」）明文標為**不得臆測**，且在 G-4 與 I-3(15) 重複警示。**唯一瑕疵是 M 章把 FDA 與 EMA 之 AE 率壓成單一區間（待議 #9）。** |
| **5** | 必須顧及癌症病人的腹瀉、體重下降、食慾不佳、脫水與腎功能波動 | **✅ 通過（強）** | 這是本稿處理得最細的一項，且有**可執行的權衡**而非空話：<br>· B-5 專表列出六個干擾因子（腹瀉／脫水／體重下降／腎功能波動／併用類固醇／IV glucose）。<br>· C-2b#6 指出 inavolisib 特有的雙重門檻：腹瀉→脫水→eGFR 掉入 30–<60 → **同一件事同時觸發 inavolisib 減量與 metformin 不可起始**。<br>· D-5 全節（BMI 是會動的數字、median BMI 變化 −1.30 kg/m²、停用 albumin 作分層並明說查無來源）。<br>· E C 欄把「嚴重腹瀉／嘔吐／脫水」列為 metformin 不適合欄。<br>· G-2.1 明文「腹瀉發生時，先動 metformin，不要先減 alpelisib」（引 Tankova「Maintenance of alpelisib therapy, rather than metformin, is preferred in cases of diarrhea」）。<br>· H.2.2 以「病人情境 → 較合理選擇 → 應避開」三欄處理惡病質（避 SGLT2i／GLP-1 RA，選 pioglitazone／DPP-4i）。<br>· 生酮飲食在**每一章**都被以「食慾不佳／體重下降／腹瀉者風險大於利益」限縮，並引 Tankova 四項反對理由。<br>· GLP-1 RA 每次出現必附「cachexia 與 malnutrition 風險」。<br>· 血糖目標明文放寬以「prevent catabolic wasting」。 |

**五項禁忌：0 違反、1 項有論證過強（禁忌 1，見必修 #3）、1 項有格式瑕疵（禁忌 4，見待議 #9）。**

---

## 3. 通過項抽驗紀錄（節錄，全部逐字 grep 命中）

| 論斷 | 章節 | 來源 | 查核 |
|---|---|---|---|
| Hopkins 小鼠 metformin 三個 p 值 0.2136／0.7566／0.6186 皆不顯著 | B-3、B-7(8)、F-3-1 | InsulinFeedback_Hopkins_2018.md | ✅ 三值皆命中 |
| Borrego：SGLT2i n=19 vs 配對 n=74；4.9 倍／6.4 倍；RR 降 70.6%／35.7%；HR 0.294／0.643；事件率 0.00461/0.02272/0.00922/0.05917 | B-3、H.1、I-1D、I-2-6 | SGLT2i_Borrego_2024.md | ✅ 全部命中 |
| INAVO120：58.6%(95/162)、G3 5.6%(9/162)、實驗室 G3 11.5%(18/157)、中斷 27.2%(44/162)、減量 2.5%(4/162)、停藥 0.6%(1/162)、緩解中位 16.0 天(IQR 5–50)、預防性 metformin 7.4%(12/162)、metformin 62/66(93.9%)、insulin 11/162 中位 5.0 天 | B-6、C-1、C-3、E、G-1.8、K-1 | INAVO120_Safety_Im_2026.md | ✅ 全部命中（含 Table 4 風險因子分層 52.7/2.2、68.0/8.0、62.5/12.5、66.7/33.3） |
| alpelisib 仿單：65%／33%／3.9%／0.7%(n=2)／15 天(5–517)／8 天(2–65, n=153)／29% 減量／6% 停藥／87%(163/187)／76%(142/187)／AKI 2.5%／96%(52/54) FDA／93.4%(57/61) EMA | B、C、F、I、K、M | label_alpelisib.md | ✅ 全部命中（52/54 與 57/61 分屬 FDA/EMA，非重複計算） |
| inavolisib 仿單：85%／12%／0.6%／28%／2.5%／1.2%／7%(11/162)／7 天(2–955)／8 天(2–43)／96%(52/54)／eGFR 減量與 AUC +73%/+123% | B-6、C-1、C-2、F-0、I-1E | label_inavolisib.md | ✅ 全部命中（inavolisib 之 52/54 為「改善 ≥1 grade」，與 alpelisib 之 52/54「回到基線」為巧合同數，未混用） |
| METALLICA：68/233、cohort A 48／B 20、2.1%(1/48, CI 0.5–11.1, P<0.0001)、15.0%(3/20, CI 5.6–37.8, P=0.016)、44.1%(30/68)、腹瀉 67.6%／第一週 14.7%(10/68)、metformin 停用 8(11.8%)／中斷 12(17.6%)／減量 25(36.8%)、停用後 4/8(50%) 高血糖皆 G1–2、alpelisib 停藥 9(13.2%) 無一因高血糖、中斷 47.1%／減量 30.9%、mPFS 7.3、ORR 20.6%、CBR 52.9%、RDI 95.1% | E、F、G-1、I-2-1、K-2 | METALLICA_(Llombart/LlombartCussac)_2024.md | ✅ 全部命中；G-1.2 指出之「abstract 20.2% vs Results 29.2%」原文內部不一致**確實存在**，稽核註記正確 |
| Liu 2022：校正後 metformin −28(−41,−16)／SGLT2i −48(−75,−21)／SU −38(−69,−8)／insulin −22(−52,−2)；TZD +13(−151,178) 與 DPP-4i +28(−121,177) 未達顯著；BMI≥25 OR 5.4(2.3–16.0)／多變項 4.0(1.3–17.8)；HbA1c≥5.7 OR 4.7(2.1–11.0)／3.4(1.2–9.4)；8/23(34.7%)；12%(39/491)／6%(30/491)／2%(7/491)；入院血糖 538、中位 14 天(7–56)；49.9%(174/349)；15 位 SGLT2i 使用者出 1 例 eDKA（pH 7.26、HCO3 13、AG 21） | D-1、H.1、I-2-4、I-2-6、K-4 | RealWorld_Liu_2022.md | ✅ 全部命中 |
| Shen 2023：61.5%(152)／29.2%(72)／中位 16 天；standard care 80.3%／40.2% vs trial 34.0%／13.0%（p<0.001）；30.6% vs 15.0%（p=0.041）；RDI 277 vs 246；300 mg 次族群 80% vs 52%；median BMI 25.4、BMI 變化 −1.30 kg/m²(−5.5%)；基線 HbA1c p<0.001／減停藥 p=0.015；BMI×HbA1c 交互 p=0.005；72% 有基線 HbA1c；內分泌轉介 19.8%(49/247), p=0.007；metformin 單藥緩解中位 16 天(IQR 7–26) | D-1、D-5、D-6、G-2.5、I-2-4、M8 | RealWorld_Shen_2023.md | ✅ 全部命中 |
| Rodon 2024：n=505 建模／BYLieve n=340 驗證；training 86.2%／test 57.6%；SOLAR-1 高風險 90.6%(96/106) vs 低風險 6.7%(12/178)；停藥 16.7% vs 2.6%；PFS 11.0 vs 10.9；monocytes 無切點 | D-1、I-1A、I-2-3、K-2 | RiskModel_Rodon_2024.md | ✅ 全部命中 |
| GO39374：有風險因子者高血糖 81%、arm F 早期 metformin 仍 40.0%(8/20) grade 3、「despite early metformin treatment」 | C-3、D-3、I-2-2 | INAVO120_Safety_Im_2026.md / GO39374_Gambardella_2025.md | ✅ 命中 |
| Tankova：SOLAR-1 4% diabetic／56% prediabetes；prediabetes 74% vs 正常 52%；正常 BMI 57% vs 過重肥胖 68–74%；≥75 歲 G3/4 55% vs 36%；「life-threatening hyperglycaemia within 2–3 days」；「no supporting evidence for this practice」；protocol 修訂後 40.3%→32.9%、停藥 9.0%→3.6% | D-1、E §3、E §7、M8 | Consensus_Tankova_2022.md | ✅ 全部命中 |
| ITACA：21/23(91.3%)、G1 39.1%／G2 34.8%／G3 17.4%／G4 0；G2–4 hyperglycaemia-free survival 中位 6 天(95% CI 3–44)；HbA1c 5.6→5.8、絕對增加 0.3 | M1、M5、M7、K-2 | ITACA_Pancirov_2025.md | ✅ 數字全部命中（**唯設計描述有誤，見必修 #1**） |
| Inavolisib HHS 個案：72 小時、48.0 mmol/L、327 mOsm/L、C-peptide 10.2 ng/mL、insulin 41.5 μU/mL、BMI 19.55、HbA1c 5.7%、尿酮陰性、insulin 46 IU/day 一週內停用 | B-5、D-6、F-3-3、K-4、M1 | Inavolisib_HHS_Li_2026.md | ✅ 全部命中 |
| Ismail 2026（📌）：n=546、TOT 87.5 天(IQR 28.0–173.7)、20.0%→34.3%、81.8% metformin／44% insulin、HR 0.76(0.61–0.93, p=0.008) | I-2-3、I-2-4、K-4 | Claims_Ismail_2026.md | ✅ 全部命中且**確實只用 abstract 層級句子**（📌 規則遵守） |
| SOLAR-1 主論文（📌）引用：PFS 11.0 vs 5.7 (HR 0.65, 0.50–0.85)、G3/4 高血糖 36.6% vs 0.7%、G3 diarrhea 6.7%、因 AE 停藥 25.0% | K-1 | SOLAR1_Andre_2019.md | ✅ 四項**皆在 abstract 內**，未逾越 📌 規則 |
| Elderly Cook 2021（📌）：34 人、中位 72(65–85)、12 人起始 insulin、4 人住院、11 人疑因高血糖停藥 | K-4 | Elderly_Cook_2021.md | ✅ 全部在 abstract 內 |
| FAERS ROR 9.84(7.3–13.2)、87 例、case report 中位 14 天；Martel OR 2.05 與 G3-4 高血糖 OR 40.93(10.08–166.22)；Meta_Li HR 0.74／RR 1.80／1.10／2.11／n=3,011；Shields 59%／28%／18% | K-4、K-6 | 各對應檔 | ✅ 全部命中 |
| ADA：Rec 3.8(B)、9.35a(E)、9.35b(E)、2.21(C/E)、3.10(B)；high-risk 四因子；「A1C alone may not capture the early peak」；SOLAR-1 中位 13 天 | D、E、F、G、H、I、M | guideline_ada_comparators.md | ✅ 全部命中；ASCO 跨試驗 2.3% vs 36.6%、TRUQAP 37%／DKA 0.3%、CAPItello-281 69%／1.2%／71 天 亦命中 |
| Delphi：248 mg/day dose intensity、7.9% vs 18.1%、METALLICA 42.6% 之轉述、GFR>45、各藥觀察等待期（metformin 2 週／SGLT2i 2 天／DPP-4i 1 週／TZD 6 週／GLP-1 RA 1 週） | B-3、E、G、H.2.3 | Delphi_Gallagher_2024.md | ✅ 全部命中 |

**抽驗總數 130 項；逐字命中 121 項。**

---

## 4. 統計

| 判定 | 數量 |
|---|---|
| **必修** | **3** |
| **待議** | **6** |
| **通過** | **121** |

- 必修 3 筆中，**2 筆是「檔案狀態／研究設計描述」問題**（K-2 ITACA 單臂誤述、SOLAR-1 AE 與 INAVO120 主論文之 📌 標記已過時），**1 筆是實質的 synthesis overreach**（D-0 對 Liu 2022 的 β/γ/δ 論斷）。
- 待議 6 筆中，4 筆為**跨章節不一致**（同一數字兩種寫法／同一篇兩個檔名／檔案計數過時），2 筆為**論證強度需下修**（Ismail 因果讀法、FDA-EMA 分母混用）。
- **無任何一筆為憑空捏造。** 無 dead link。無 ghost consensus。
- **五項禁忌 0 違反**（安全性紅線「不得延誤 insulin」設防最為完整，共 10 處明文）。

---

## 5. 給下一輪的修改優先序

1. **（安全性無關但影響全稿可信度，最優先）** 重跑 `來源/inventory.md`：`SOLAR1_AE_Rugo_2020.md`（81 KB）與 `INAVO120_Turner_2024.md`（78 KB）已落地全文，須改標 📄；同步修正 C-1/C-5/D-8/F-5/G-5/I-3/K-1/K-7 共 8 處「僅有 abstract、不得引用」之聲明，並更新 K-7 之全文率統計與「70 個 .md 檔」（實為 71 檔）。
2. 修正 K-2 對 ITACA 的「單臂」誤述（實為 randomized phase IIb，11 vs 12，本分析為 pooled interim）。
3. 修正 D-0 對 Liu 2022 的過度陳述（「無任何高血糖事件」→「無高血糖相關治療中斷事件」）。
4. 統一 METALLICA grade 3–4 腹瀉（13.2% vs 11.8%）與 alpelisib ≥75 歲 G3-4（56% vs 55%）之跨章節寫法。
5. 清理 METALLICA 與 Shen 2023 的重複落地檔，全稿統一檔名。
6. 下修 I-2-3 對 Ismail 2026 之因果讀法；拆開 M 章 FDA/EMA 混用之 AE 區間。
