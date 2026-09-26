# MU — Micron Technology, Inc. (diligence agent F29, standard depth)

## 1. Verdict
**WATCH** (12–36 month thesis horizon). Micron is the highest-quality merchant memory franchise in the world and is living through a genuine, filing-verified AI/HBM pricing supercycle — but the 25-Sep-2026 close of $1,082.28 already prices a continuation and further escalation of peak-cycle earnings that memory economics have never sustained for a decade. This is a case of "great business, priced for more than it can deliver" (V4 rule), not a business or balance-sheet problem.

## 2. Business in plain English
Micron designs and manufactures DRAM, NAND flash and, increasingly, HBM (high-bandwidth memory) chips used in servers, PCs, phones, and AI accelerators. It sells commodity-like memory bits into an oligopoly (with Samsung and SK Hynix) where price is set by the industry's bit-supply/bit-demand balance, not by product differentiation. Its 2026 growth is being driven almost entirely by HBM allocated to AI accelerators and by a broader DRAM shortage that has pushed pricing and margins to records.

## 3. Why the model likes it — durable or artefact?
b1 quant scores (`v4/data/b1_live_scores.csv`, as of 2026-09-25): composite 0.981 (decile 10, live_rank 10/~500), driven by momentum (fam_M 0.981, mom_12_1 +474%) and earnings-surprise (fam_S 0.940, SUE 7.31 — one of the highest in the entire universe) — i.e., the model likes MU because of an enormous, recent, positive earnings shock, not because of a stable quality or value signal (fam_V is a modest 0.595; value here is an artefact of the market not yet re-rating for what may be peak earnings, exactly the trap the sector playbook warns about: "a mid-single-digit P/E on record earnings is a warning, not a valuation"). **This reason is largely an artefact of where memory sits in its own bit-price cycle**, not a structural re-rating of the business, even though the AI/HBM demand driver is real and likely multi-year.

## 4. Last two years of results (GAAP, fiscal year ends ~last Thu of August)
| FQ (end) | Revenue | QoQ | Gross margin | Op. margin | Diluted EPS (GAAP) |
|---|---|---|---|---|---|
| FY24 Q1 (2023-11-30) | $4.73B | — | −0.7% | −23.8% | −$1.12 |
| FY24 Q2 (2024-02-29) | $5.82B | +23% | 18.5% | 3.3% | $0.71 |
| FY24 Q3 (2024-05-30) | $6.81B | +17% | 26.9% | 10.6% | $0.30 |
| FY25 Q1 (2024-11-28) | $8.71B | +28% | 38.4% | 25.0% | $1.67 |
| FY25 Q2 (2025-02-27) | $8.05B | −8% | 36.8% | 22.0% | $1.41 |
| FY25 Q3 (2025-05-29) | $9.30B | +15% | 37.7% | 23.3% | $1.68 |
| FY26 Q1 (2025-11-27) | $13.64B | +47% | 56.1% | 45.0% | $4.60 |
| FY26 Q2 (2026-02-26) | $23.86B | +75% | 74.4% | 67.6% | $12.07 |
| FY26 Q3 (2026-05-28) | $41.46B | +74% | 84.6% | 80.4% | $24.67 |

Source: SEC XBRL `data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json` (tags `RevenueFromContractWithCustomerExcludingAssessedTax`, `GrossProfit`, `OperatingIncomeLoss`, `EarningsPerShareDiluted`), cross-checked against Micron's own FQ3'26 press release (investors.micron.com, 2026-06-25: "record fiscal Q3 revenue of $41.46B, +346% YoY, DRAM $31.3B / 76% of revenue, non-GAAP gross margin 84.9%, non-GAAP EPS $25.11"). Every figure above is GAAP; Micron's own non-GAAP EPS ($25.11 FQ3'26) differs from GAAP ($24.67) mainly by stock-compensation and inventory step-up adjustments. **Three consecutive quarters of >45% sequential revenue growth in a supposedly mature commodity business is the single fact this dossier weighs most heavily** — it is real (filing-verified) but structurally unusual, and DRAM industry economics have mean-reverted after every prior episode like it (see §9).

## 5. Guidance track record (last 3 releases; FQ4 not yet reported)
- **FQ2 FY26** (guided 2025-12-18, delivered 2026-03-18): guided revenue $18.7B ±$0.4B, GM 68%±1pt → delivered $23.86B (+27.6% above midpoint) and GM 74% (+6pt above the high end). **Beat, not a raise-then-beat** — the beat itself was the surprise.
- **FQ3 FY26** (guided 2026-03-18, delivered 2026-06-25): guided revenue $33.5B ±$0.75B, GM ~81% → delivered $41.46B (+23.8% above midpoint), GM 84.9% (+3.9pt above guide).
- **FQ4 FY26** (guided 2026-06-25, reports 2026-09-30 — 5 days after this dossier's cutoff): guidance is revenue $50.0B ±$1B, GM ~86%, EPS $31±$1, capex ~$10B (investors.micron.com press release, 2026-06-25 / Vantage Markets, 2026-09-23 earnings-date confirmation).
Every recent guide has been beaten by 20–30%, which is bullish for near-term execution but means the market is now extrapolating a fourth consecutive outsized beat into the price — the reverse-DCF in §7 shows what growth rate is actually required.

## 6. Earnings quality & balance sheet
- **FCF conversion:** TTM (to 2026-05-28) OCF $51.4B, capex $25.3B, FCF $26.2B, TTM NI $50.5B → FCF/NI ≈ 52% (V1 `outputs/v1_valuation.json`, D3 pipeline). Capex/D&A is running well above 1x (capex $25.3B vs D&A $9.0B TTM) — consistent with a genuine, not harvested, capacity build (sector playbook: capex sustained below D&A would be the red flag; here it is the opposite, i.e. investing into the upcycle, which is normal and expected at this point in a memory cycle).
- **SBC:** ~$1.18B TTM vs $90.3B TTM revenue ≈ 1.3% of revenue — low, not a distortion driver.
- **GAAP vs non-GAAP gap:** small and stable (inventory step-up/stock-comp adjustments only); this is not the source of the "cheap" screen — genuine GAAP earnings drove it.
- **Balance sheet:** net cash of roughly −$20.9B (i.e., net cash position) per V1/D3; cash alone rose from $9.6B (2025-08-28) to $25.0B (2026-05-28) in three quarters (SEC 10-Q, CIK0000723125). No leverage concern. Diluted share count ~1.13B, essentially flat (modest net issuance/buyback offset); a $300M buyback resumed in FQ1 FY26 after a pause (XBRL `PaymentsForRepurchaseOfCommonStock`).
- **Sector-appropriate valuation lens (memory: value on P/B through the cycle, not trailing P/E):** book value/share ≈ $89.2 (equity $100.7B ÷ ~1.129B shares, 2026-05-28) → **P/B ≈ 12.1x**, which is rich even against past supercycle peaks for a merchant memory maker (playbook: "troughs cluster near or below 1x, peaks well above" — 12x is toward the high end of that "well above").

## 7. Valuation — reconciling with V1
V1 (`outputs/v1_valuation.json`, `v1_valuation_table.csv`, priced 2026-09-25): **verdict "fair"** (score 0.162), method reverse-DCF FCFF, WACC 11.6%. V1 itself flags a **data conflict**: "D3 TTM revenue implies an implausible EBIT margin (65.6%)" — this is not a data error, it is the real, filing-verified blended TTM margin as memory pricing spiked mid-year (I confirm 65.6% is correct: TTM EBIT $59.2B / TTM revenue $90.3B = 65.6%, and the FQ3 standalone operating margin was 80.4%). V1's NTM P/E is **6.79x** (22nd percentile of its own 135-month history — screens statistically cheap) on **consensus FY1 EPS growth of +91%**, but V1's own reverse DCF says the price requires **33.0%/yr FCFF growth for 10 years** fading to 3% terminal — above Micron's own trailing 5-year delivered CAGR of 28.8% and far above its 10-year CAGR of 21.6% (both of which are themselves inflated by the current quarter). V1's own base case (16.8% growth assumption, exit multiple 13.8x) produces a **3-year annualised return of −36.8%**, and its street-flag notes the base case is *below the Street's own 12-month low target* ($361 vs $1,082 spot) — i.e., even Street bears are less bearish than V1's base case. Bull case (+35.0%/yr) requires 61%/yr growth.
**My reconciliation:** I agree with V1's caution and go further on the *reason*: the sector playbook is explicit that memory P/E is "inverted" — a single-digit multiple on record earnings is a warning, and P/B (12.1x) is a cleaner cross-check that confirms the market is capitalising close to peak conditions, not offering a value discount. **Implied 10-year growth (33.0%) is ABOVE my own evidence-based base case (~18–22%/yr, allowing 2–3 more years of AI/HBM-driven strength before bit-supply catches up and pricing normalises, as it has after every prior memory upcycle)** → dossier view: **expensive on a mid-cycle basis**, consistent with V1. `valuation_view_vs_v1.implied_vs_base = "above"`.

## 8. Bull case / Bear case
**Bull:** (1) HBM4 is in high-volume shipment to a lead AI-accelerator customer with HBM4E qualification underway for 2027 volume production (Micron FQ3'26 earnings-call prepared remarks, investors.micron.com) — a genuine multi-year, capacity-constrained, contracted-ahead product line that behaves more like specialty logic than commodity DRAM. (2) Bit-supply discipline: Micron, Samsung and SK Hynix have all reallocated capacity toward HBM, structurally tightening commodity DRAM/NAND supply. (3) $10B Boise "mega-fab"/lab investment signals multi-year confidence and secures US onshore capacity (investors.micron.com FQ3'26 release).
**Bear:** (1) Memory is the industry's most inverted-multiple, most commodity-like sub-sector; every prior DRAM upcycle since the 1990s has ended in oversupply and a margin collapse once new capacity (Micron's own $10B Boise investment among others) comes online. (2) A federal class action filed 2026-06-25 (N.D. Cal., per web reporting) alleges Micron, Samsung and SK Hynix conspired to restrict DRAM supply and inflate prices, citing a 700% price increase over four years — even if defended successfully, it is a live signal that the "shortage" narrative itself is contested, and any negotiated remedy or output response would hit the pricing this valuation depends on. (3) V1's own base-case DCF, using Micron's own trailing figures, is priced for the current run-rate to continue growing at 33%/yr for a decade — a bar memory has never cleared historically.

## 9. Key risks & kill criteria
1. Sequential DRAM/HBM ASP (blended) declines for **two consecutive quarters** (first visible via gross margin compression from the 84–86% FQ3/FQ4 FY26 level).
2. GAAP gross margin falls below **65%** for a full quarter (roughly the FQ1 FY26 level), signalling the cycle has turned.
3. Capex guidance is cut versus the ~$10B/quarter FQ4 FY26 run-rate while HBM demand commentary stays positive (a harvesting signal, not a demand signal).
4. Net cash position turns to net debt, or buybacks are suspended while capex stays elevated (financing-stress signal).
5. The DRAM price-fixing class action (N.D. Cal., filed 2026-06-25) results in an adverse ruling, DOJ referral, or negotiated output/pricing remedy.

## 10. Catalysts & calendar
Next earnings: **2026-09-30** (FQ4 FY26; 5 days after this dossier's price cutoff — high-impact, imminent event). HBM4E volume production targeted calendar 2027. No known lock-ups or index events flagged in the data reviewed.

## 11. Red-flag scan
- **Antitrust:** DRAM price-fixing federal class action against Micron, Samsung, SK Hynix, filed 2026-06-25, alleging Sherman Act violations and a 700% price surge over four years; Scott+Scott is separately investigating Micron officers/directors for related fiduciary-duty claims (web search, multiple outlets, 2026-09). **Live and material given this dossier's entire bull case rests on the pricing the suit says is manipulated.**
- **Securities litigation (resolved favourably):** a Sept–Dec 2024 class-period securities suit (S.D. Fla.) alleging misleading NAND/consumer-demand statements was dismissed 2026-02-03 with leave to amend; plaintiffs voluntarily dismissed 2026-04-03 — concluded, not a live risk.
- **ITC:** a U.S. International Trade Commission investigation was instituted involving Micron in 2026 (PR Newswire headline found; complainant/respondent status and product scope not independently confirmed in the time available for this pass — flagged as an open item, not incorporated into the verdict).
- No auditor change, going-concern language, or material weakness found in the filings reviewed.

## 12. Data basis, recency and disclaimer
All figures are in US dollars; B = billions, M = millions, unless stated otherwise. Most recent period incorporated: fiscal Q3 2026 (period ended 2026-05-28; 10-Q filed 2026-06-25, plus the FQ3'26 earnings press release dated 2026-06-25). Events checked to 2026-09-25. GAAP figures are used throughout §4 and are explicitly labelled where non-GAAP company figures are cited for comparison (§4, §5). **This is research, not personalized investment advice.**

## 13. Sources
1. SEC EDGAR XBRL companyfacts, CIK 0000723125 — `data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json` (retrieved 2026-09-26).
2. SEC EDGAR submissions, CIK 0000723125 — `data.sec.gov/submissions/CIK0000723125.json` (retrieved 2026-09-26).
3. Micron Technology, Inc. Reports Record Results for the Third Quarter of Fiscal 2026 — investors.micron.com, 2026-06-25.
4. Micron Technology, Inc. Fiscal Q3 2026 Earnings Call Prepared Remarks — investors.micron.com, 2026-06-25.
5. Micron Technology, Inc. Reports Results for the Second Quarter of Fiscal 2026 — investors.micron.com / SEC 8-K EX-99.1, 2026-03-18.
6. "Micron to Report Fiscal Fourth Quarter Results on September 30, 2026" — investors.micron.com, 2026-09.
7. v4/outputs/v1_valuation.json and v1_valuation_table.csv (MU row) — v4 program, priced 2026-09-25.
8. v4/data/b1_live_scores.csv (MU row) — v4 program, as of 2026-09-25.
9. v4/outputs/Q12_triage.json (MU entry) — v4 program triage.
10. DRAM price-fixing class action reporting (Micron/Samsung/SK Hynix), filed 2026-06-25 — web search aggregation, 2026-09.
11. Micron securities litigation status (S.D. Fla. dismissal 2026-02-03, voluntary dismissal 2026-04-03) — web search aggregation, 2026-09.
