# NVIDIA Corporation (NVDA) — Fundamental Diligence Dossier

**Verdict: INCLUDE-SMALL** (half weight) — 12–36 month thesis horizon. **[Corrected 2026-10-08: VERDICT CHANGED to WATCH after verification DV31 (restated reverse DCF at a beta-consistent cost of capital implies about 22% a year, near the bull case; see the Correction section at the end)]**
One-sentence reason: near-monopoly AI-accelerator franchise with genuine execution (four straight quarters of YoY acceleration, gross margin back to 75%), but at the 25-Sep-2026 close ($225.07, mkt cap $5.42T) the price bakes in more 10-year growth (15.4% on trailing free cash flow) than a fair, evidence-based base case (≈13%) — this is a "would hold, but not at full weight" name, not a screaming buy.

## 1. Business in plain English
NVIDIA designs GPUs and the software/networking stack around them; it does not manufacture (TSMC fabs the chips). Data Center — Blackwell/GB200-era systems, Vera Rubin systems entering production, InfiniBand/NVLink/Ethernet networking, CUDA software — is now ~93% of revenue ($89.0B of $96.2B in fiscal Q2 2027), sold to hyperscalers (Microsoft, Google, Amazon, Meta, Oracle), sovereign-AI buyers, and enterprises building AI infrastructure. Gaming, Pro Visualization and Automotive are the remainder. The moat is CUDA software lock-in plus a multi-generation systems lead (chip + networking + rack-scale + software), not just raw chip performance.

## 2. Why the model likes it / is it durable
b1 factor data (v4/data/b1_live_scores.csv, as_of 2026-09-25): composite percentile 0.79 driven mainly by Value (fam_V 0.84, EBIT/EV percentile 0.79) and Momentum (fam_M 0.42) — the model likes NVDA's cash-flow yield and 12-month momentum, not "growth" as a factor per se (SUE/earnings-momentum percentile is only 0.79 fam_S but n_S sample thin at n=4 families). live_rank 103 (outside the top-70 gate that excluded it from earlier waves). This is a real, filed-numbers-driven signal (record Data Center revenue, 4 consecutive quarters of YoY acceleration per management's own Q2 FY27 call), not an accounting artefact — but it is a **cyclical capex signal**: it depends on hyperscaler capex continuing at the current run-rate, which is itself a debated, not proven, multi-year commitment.

## 3. Last 8 quarters (fiscal quarters; $M except EPS; FQ4 FY25 (Oct24–Jan25) is not separately XBRL-tagged in quarterly form — 10-K reports only the full year — so it is omitted rather than estimated)
| Quarter | Revenue | QoQ | Gross margin | Op margin | Net income | Diluted EPS |
|---|---|---|---|---|---|---|
| FQ1 FY25 (end 2024-04-28) | 26,044 | — | 78.4% | 64.9% | 14,881 | 0.60 |
| FQ2 FY25 (end 2024-07-28) | 30,040 | +15% | 75.1% | 62.1% | 16,599 | 0.67 |
| FQ3 FY25 (end 2024-10-27) | 35,082 | +17% | 74.6% | 62.3% | 19,309 | 0.78 |
| FQ1 FY26 (end 2025-04-27) | 44,062 | +26%* | **60.5%** | 49.1% | 18,775 | 0.76 |
| FQ2 FY26 (end 2025-07-27) | 46,743 | +6% | 72.4% | 60.8% | 26,422 | 1.08 |
| FQ3 FY26 (end 2025-10-26) | 57,006 | +22% | 73.4% | 63.2% | 31,910 | 1.30 |
| FQ4 FY26 (end 2026-01-25, derived: FY total − 9-mo) | 68,127 | +20% | 75.0% | 65.0% | 42,960 | ~1.76 |
| FQ1 FY27 (end 2026-04-26) | 81,615 | +20% | 74.9% | 65.6% | 58,321 | 2.39 |
| FQ2 FY27 (end 2026-07-26) | 96,221 | +18% | 75.0% | 66.2% | 59,688 | 2.46 |

*FQ1 FY26 QoQ vs the derived FQ4 FY25 figure is not shown because FQ4 FY25 is omitted; growth rate approximate.
FQ1 FY26's gross-margin dip to 60.5% is a real, filed event: NVIDIA recorded a **$4.5B charge for H20 excess inventory and purchase obligations** after the U.S. tightened China export rules — not a one-off accounting artefact, a direct hit from the export-control regime described in §6. [1][2]
Q2 FY27 (reported 26-Aug-2026): revenue $96.2B (+106% YoY, +18% QoQ); Data Center $89.0B (+117% YoY); Hyperscale $49B (+13% QoQ); "ACIE" (enterprise/other compute) $40B (+25% QoQ, +138% YoY); Sovereign AI revenue tripled YoY — evidence of some customer diversification beyond the largest hyperscalers. [3]

## 4. Guidance track record (last 4 quarters, vs prior guidance)
- Q3 FY26 report (Nov-2025) → guided Q4 FY26 revenue; actual Q4 FY26 $68.1B, "record," +20% QoQ — **beat**.
- Q4 FY26 report (Feb-2026) → guided Q1 FY27; actual Q1 FY27 $81.6B, +85% YoY, "third consecutive quarter of YoY acceleration" — **beat**.
- Q1 FY27 report (May-2026) → guided Q2 FY27 revenue $91B ±2%; actual $96.2B — **beat by ~5.7%**.
- Q2 FY27 report (Aug-2026) → guided Q3 FY27 revenue $108B ±2%, non-GAAP gross margin ~74% (Q4 FY27 trough estimate 71–72%). Not yet reported as of this cutoff.
Pattern: four straight beats, and management itself now frames the constraint as **supply, not demand** — a FY2028 growth guide of "approximately 70%" was described on the call as immediately qualified as supply-constrained, with unconstrained demand "a lot higher." [3][4][5] That is bullish for near-term execution but means further upside requires NVIDIA and its foundry/packaging partners to add capacity — a real operational risk, not a demand one.

## 5. Moat and competition
- **Market share:** NVIDIA ≈80% of the AI-accelerator market in 2026, down from ≈92% in 2023. [6]
- **AMD:** Instinct line ≈$7–8B revenue in 2025 (≈5–7% share); MI400 lands H2 2026 on TSMC 2nm, anchored by AMD's own multi-gigawatt OpenAI compute deal — a credible, growing #2, not yet a threat to NVIDIA's economics. [6]
- **Hyperscaler custom silicon — the more structural threat:** Google TPU v7/TPU v8i, AWS Trainium3, Microsoft Maia200, Meta MTIA collectively ≈15–20% of accelerator spend and "growing fast." Google runs >75% of Gemini inference on its own TPUs; AWS Trainium handles >50% of Bedrock token throughput. [6][7] This is customers building around NVIDIA for a rising share of *their own* inference workloads while still buying NVIDIA for training and general-purpose capacity — a genuine, evidenced dilution of the moat, not a bear-case hypothetical.
- **Customer concentration:** FY2026 10-K discloses one direct customer at 22% of revenue and a second at 14% (36% combined); Q2 FY26 "Customer A"/"Customer B" were 23%/16%. [8][9] Two counterparties are >1/3 of revenue — a real, filed risk, and these are believed to be system integrators/hyperscalers reselling further, so end-customer concentration is likely even higher.
- **Export controls:** NVIDIA is "effectively foreclosed" from China's data-center compute market as of FY2026 year-end per its own 10-K language; H20 was NVIDIA's compliant fallback and still triggered a $4.5B charge. Any further U.S.–China escalation is asymmetric downside (China was historically 20%+ of Data Center revenue pre-restriction). [1][2]
- Announced (Aug-2026) $12.9B acquisition of Hugging Face — a software-ecosystem bet, not yet closed as of this cutoff; adds integration risk. [4] **[Corrected 2026-10-08: Announced 2 Sep 2026, not August: about $11.9B purchase price plus an equity retention programme of up to about $1.0B; expected to close in 1H 2027 (8-K 0001045810-26-000078). Also omitted: $105B of SB Energy/OpenAI residual-value guarantees (8-K 0001045810-26-000069) and $366B of future commitments (10-Q Note 10)]**

## 6. Earnings quality & balance sheet
- FCF conversion: TTM (Q3 FY26–Q2 FY27) operating cash flow $134.4B, capex (PaymentsToAcquireProductiveAssets) $7.4B, **FCF ≈$127.0B**, i.e. FCF/NI conversion is strong (TTM net income ≈$192.9B off the same quarters, so FCF/NI ≈66% — capex-light because NVIDIA is fabless; the ratio is depressed mainly by working-capital swings, not accounting quality). Note the **OCF sequential decline** from Q1 FY27 ($50.3B) to Q2 FY27 ($24.1B) despite revenue growing — a real, filed working-capital swing (accounts receivable alone grew ~$24.6B in the period) worth watching, not a red flag on its own given the scale of growth, but not explained by the press release headline. [10]
- SBC: ~$2.0B/quarter (~2.1% of revenue) — low and stable versus peers.
- Balance sheet: cash & equivalents $22.4B (Jul-2026); **long-term debt jumped from ~$7.5B to $32.4B in a single quarter (Q2 FY27)** — a new, large debt issuance not present in prior quarters, coinciding with the Hugging Face deal announcement. Stockholders' equity $229.0B, assets $320.3B. This debt jump is unexplained by the press-release excerpts available and is flagged as a data conflict to verify against the full 10-Q. [10] **[Corrected 2026-10-08: Explained: NVIDIA issued $25.0B of senior unsecured notes across seven tranches in June 2026 for general corporate purposes (10-Q 0001045810-26-000075 debt note; CFO commentary in 8-K 0001045810-26-000073); this was before, and unrelated to, the Hugging Face deal]**
- Dividends token-sized (~$0.01–0.26/share quarterly, small % of FCF); buybacks are the primary capital return (~$19.3B in Q1 FY27 alone, ~$26B total shareholder return in Q2 FY27).

## 7. Valuation — reverse DCF (this analyst's own model; there is no V1 systematic valuation row for NVDA)
Inputs: EV ≈ market cap $5,424,187M (net cash/debt roughly offsetting at this scale); TTM FCF $127,006M; WACC 9.5%; terminal growth 3.5%; 10-year horizon.
**Solving for the constant FCF growth rate that justifies the price: 15.4%/year for 10 years** (FCF yield on trailing FCF = 2.34%).
Sensitivity: if the *sell-side FY2027 consensus* FCF (~$194.1B, itself +53% YoY over TTM) is used as the starting base instead of trailing actuals, the required ongoing growth falls to **9.8%/year** — i.e., NVDA's price is fully defensible *if* the current fiscal year's guided ramp actually lands, but is a materially more demanding ask on today's already-strong trailing numbers. [11]
- **Bear case (10y FCF CAGR ≈0–5%):** custom-silicon substitution accelerates past 30% share, a China/export shock recurs, AI capex cyclically pauses.
- **Base case (10y FCF CAGR ≈13%):** front-loaded growth (25–30%/yr next 2 years on Rubin ramp) decelerating to high-single-digits by year 8–10 as the market matures and share erodes toward 55–65%.
- **Bull case (10y FCF CAGR ≈22%):** Rubin/Rubin-Ultra sustain dominant share, new demand pools (sovereign AI, robotics/"physical AI") materialize as management claims.
**Implied vs. base: ABOVE.** On the conservative (trailing-FCF) method the market is paying for more than this analyst's base case; on the sell-side's own near-term numbers it is paying for roughly base case. This is a genuine, close call, not a clear-cut overvaluation — hence INCLUDE-SMALL rather than REJECT/WATCH. **[Corrected 2026-10-08: Restated: WACC 9.5% is not consistent with 5.17% plus a beta-based premium (5-year weekly Blume beta about 1.71 gives cost of equity about 12.2%) and FCF adds back about $7.2B of TTM stock compensation; implied growth is about 22% a year (not 15.4%) and about 16% on consensus FY27 FCF (not 9.8%); implied_vs_base stays ABOVE and verdict becomes WATCH]**

### 3-year scenario returns (annualised total return from $225.07, illustrative — not a probability statement)
| Scenario | 3y FCF CAGR (yrs 1–3) | Exit EV/FCF | Annualised return |
|---|---|---|---|
| Bear | ~0% | 18x (de-rate from 42.7x entry) | **≈ −25%/yr** |
| Base | ~25% | 30x | **≈ +11%/yr** |
| Bull | ~35% | 38x | **≈ +30%/yr** |

## 8. Bull case
1. Vera Rubin now in full production; hyperscale growth explicitly expected to reaccelerate in Q4 FY27 into FY28 as Rubin supply increases — a company-stated, near-term, checkable catalyst.
2. Management says demand is running well above the guided ~70% FY28 growth rate; supply, not orders, is the binding constraint — a "good problem," and capacity additions are visible/trackable.
3. Diversification evidence: sovereign-AI revenue tripled YoY and "ACIE" (non-hyperscale enterprise/other) grew 138% YoY in Q2 FY27 — reduces reliance on the two largest customers over time.

## 9. Bear case
1. Two direct customers were 36% of FY26 revenue; any pullback, in-sourcing acceleration, or renegotiation by either is a single-name concentration risk at a scale that moves the whole stock.
2. Hyperscaler custom silicon (TPU/Trainium/Maia/MTIA) is ≈15–20% of accelerator spend and "growing fast," concentrated exactly among NVIDIA's largest customers — the buyers most able to substitute are doing so fastest.
3. China is a foreclosed, not just discounted, market as of FY26 per NVIDIA's own 10-K; the $4.5B H20 charge shows the earnings impact of policy risk is real and has already landed once.

## 10. Key risks & kill criteria — thesis-invalidation triggers (what would change the verdict / break the thesis)
1. Gross margin below 70% for two consecutive quarters (ex a disclosed one-off).
2. Data Center YoY growth decelerates below 40% for two consecutive quarters.
3. Independent trackers show combined hyperscaler custom-silicon share above 30% of AI accelerator spend.
4. Two-largest-customer revenue concentration exceeds 45% of total revenue (vs. 36% in FY26).
5. Net new long-term debt issuance beyond the Q2 FY27 $32.4B level without clear, disclosed use-of-proceeds.

## 11. Catalysts & calendar
- Next earnings: Q3 FY27, estimated **~18-Nov-2026** (pattern-based estimate from FY26 Q3's 19-Nov-2025 report date; not yet confirmed/scheduled as of this cutoff).
- Vera Rubin production ramp commentary expected on that call (management said shipments "commence in the second half of fiscal 2027, starting in Q3").
- Hugging Face acquisition close (announced Aug-2026, pending as of cutoff).

## 12. Red-flag scan
- $4.5B H20 inventory/purchase-obligation charge (FQ1 FY26) — disclosed, not hidden, but a real earnings hit from geopolitical risk. [1][2]
- Sudden Q2 FY27 long-term debt jump ($7.5B→$32.4B) and OCF sequential decline — flagged as data conflicts requiring full 10-Q verification; not explained in the press-release-level sources used here. **[Corrected 2026-10-08: Resolved: $25.0B notes issued June 2026; OCF fell on higher working capital and cash taxes (CFO commentary). New unflagged items: $105B guarantee for OpenAI's Portsmouth (Ohio) leases and $366B total commitments]**
- No auditor changes, restatements, or going-concern language found in the sources reviewed.
- Vendor-financing/circularity concern (industry-wide, not NVDA-specific): NVIDIA, its hyperscaler customers, and AI labs (e.g., OpenAI) are increasingly counterparties to each other's revenue and investment — a systemic risk to the whole AI-capex thesis, not a company-specific defect, but relevant context for sizing.

## 13. Data basis, recency and disclaimer
All figures are consolidated (NVIDIA has no separately reported standalone/parent-only financial statements). Most recent period incorporated: fiscal Q2 2027 10-Q, period ended 2026-07-26, filed 2026-08-26 (SEC accession per data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json). Events and news checked to 2026-09-25. GAAP figures are used throughout except where "non-GAAP gross margin" is explicitly labelled (guidance commentary in §4). This is research, not investment advice: not a recommendation, and not personalised to any individual's circumstances.

## Sources
1. NVIDIA 10-K FY2026, SEC EDGAR (data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json; https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
2. Motley Fool, "Nvidia May be Back in Business in China," 2026-03-28 (fool.com)
3. NVIDIA Newsroom, "Financial Results for Second Quarter Fiscal 2027," 2026-08-26 (nvidianews.nvidia.com)
4. Simply Wall St, NVDA Future Growth / narrative "What They Said vs. What They Did," accessed 2026-09 (simplywall.st)
5. betafinch.com, "NVIDIA Q1 FY2027 Revenue Forecast," 2026-05
6. Multiple 2026 AI-chip market-share aggregations (siliconanalysts.com, commandlinux.com, teahose.com), cross-checked
7. tomshardware.com, "custom AI ASICs examined," 2026-05
8. DataCenterDynamics, "Two unnamed customers accounted for almost 40% of Nvidia's Q2 2026 revenue," 2025 (datacenterdynamics.com)
9. CNBC, "Nvidia's top two mystery customers made up 39% of...Q2 revenue," 2025-08-28
10. NVIDIA Newsroom Q1 FY2027 and Q2 FY2027 press releases (nvidianews.nvidia.com); SEC XBRL companyfacts
11. simplywall.st analyst consensus table (FY2027/FY2028 revenue, earnings, FCF forecasts), accessed 2026-09
12. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (as_of 2026-09-25)

## Correction (verification DV31, 2026-10-08)

- **Wrong text 1:** "Announced (Aug-2026) $12.9B acquisition of Hugging Face" and "long-term debt jumped ... coinciding with the Hugging Face deal announcement ... unexplained".
- **Correct value 1:** the Hugging Face agreement was signed and announced on 2 Sep 2026: about $11.9B to stockholders plus an equity retention programme of up to about $1.0B; closing expected 1H 2027 (8-K 0001045810-26-000078). The debt rise is $25.0B of senior unsecured notes issued in seven tranches in June 2026 for general corporate purposes (10-Q 0001045810-26-000075 debt note; CFO commentary, 8-K 0001045810-26-000073); long-term debt 32,366 + short-term 1,000 = 33,366 carrying value. The OCF fall ($50.3B to $24.1B) is attributed to higher working capital and cash taxes (receivables +$24.6B since January).
- **Omission 2 (material):** on 17 Aug 2026 NVIDIA gave residual-value guarantees capped at $105B for leases of about 4.25 GW at the Portsmouth (Ohio) campus, tenant an OpenAI affiliate (8-K 0001045810-26-000069; 10-Q Note 10), and the 10-Q lists $366B of future commitments (supply and capacity $279B, up from $119B a quarter earlier; cloud service $29B; equity investments $25B; leases not commenced $25B; capex $8B) plus $36B of AI cloud agreements. None appears in the red-flag scan, balance-sheet section or kill criteria. Balance sheet also holds $34.1B marketable debt securities, $42.8B marketable equity securities and $51.2B non-marketable securities, so "net cash/debt roughly offsetting" is wrong (net cash about $66B before non-marketable holdings; effect on EV about 1%).
- **Valuation method (e):** WACC 9.5% equals 5.17% + about 4.3 points, i.e. a beta near 1; NVDA's 5-year weekly beta is 2.06 (Blume 1.71), cost of equity about 12.2% on the program convention (rf 5.17%, ERP 4.14%). The TTM FCF of $127.0B is OCF minus capex and so adds back about $7.2B of stock-based compensation; the program rule treats it as a cost. Recomputed (same 10-year constant growth then 3.5% terminal, EV $5,424B): at 9.5% and $127.0B growth 15.4% (reproduces dossier); at 12.2% and $119.8B (after SBC) 22.6%; at 12.2% and $127.0B 21.7%; on FY27 consensus FCF of $194.1B (less about $9B SBC) at 12.2%: 16.4% (dossier 9.8% at 9.5%).
- **Verdict effect: INCLUDE-SMALL -> WATCH.** Implied growth of about 22% a year is at the dossier's own bull case (22%) rather than "a close call"; the dossier's base 3-year return (+11% a year) is below the 12.2% cost of equity; and the omitted $105B/$366B commitments raise the risk that TTM FCF is not the right base. implied_vs_base stays "above" (gap widened). Kill criterion 5 (debt beyond $32.4B "without disclosed use-of-proceeds") rests on a false premise; replaced in F17_summary.json. Customer data: in Q2 FY27 one direct customer was 16% of revenue and in H1 FY27 three were 16%, 15% and 13% (10-Q); the FY26 22%/14% figures are verified.
- **Verified without change:** all eight table quarters (revenue, net income, EPS, margins) against XBRL; Q2 FY27 revenue $96.2B, Data Center $89.0B, Hyperscale $48.7B, ACIE $40.3B (note: one company was reclassified from ACIE to Hyperscale and prior periods recast); Q3 FY27 guide $108.0B +/-2%, GM 74.0% +/-50bp; Q2 guide $91.0B +/-2%; TTM OCF $134.4B, capex $7.35B; $4.5B H20 charge. Not verifiable from primary sources: Q4 FY27 trough margin 71-72%, FY28 "about 70%" growth comment (call remarks).
