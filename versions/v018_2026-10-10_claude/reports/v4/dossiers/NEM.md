# NEM — Newmont Corporation — Diligence Dossier (Agent F89, STANDARD depth)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Thesis horizon: 12–24 months. Reason: record free cash flow and a net-cash balance sheet at today's gold price, and the market is pricing in outright *shrinkage*, not growth — but the entire thesis is a single-commodity bet on gold staying near record highs, so it is sized down, not full weight.

## 2. Business in plain English
Newmont is the world's largest gold miner (with meaningful copper/silver by-product), operating a global portfolio of mines across the Americas, Australia and Africa. It makes money by selling gold at the prevailing spot/realized price against a relatively fixed-in-the-short-run cash cost per ounce (AISC); as gold has risen, nearly all of the price increase has fallen straight to cash flow because costs have not kept pace.

## 3. Why the model likes it / is it durable?
Triage cited record FCF ($3.1B Q1, $2.2B Q2 2026) against AISC guided ~$1,680/oz vs realized prices near $4,900/oz. **Confirmed, with a correction:** Q2 2026 realized gold price was $4,414/oz (not $4,900 — that figure is closer to spot in September, not the Q2 average) **[Corrected 2026-10-08: wrong: $4,900/oz was the Q1 2026 average realized price (Q2 $4,414), per the Q2 release Ex-99.1 acc 0001164727-26-000034; the triage was right]**, and Q2 AISC was $1,621/oz (below the $1,680 full-year guide). Revenue growth is being driven almost entirely by price, not volume: Q2 2026 realized price +33% YoY while cost-applicable-to-sales rose only ~4% — genuine operating leverage, but not a repeatable *growth* driver if gold prices plateau or fall. This is a price-cycle tailwind, not a durable structural moat — flagged as **not durable** in the sense the model's quality/value scores would suggest; it is a cyclical windfall.

## 4. Last several quarters — results
GAAP, source: SEC EDGAR 10-Q/10-K XBRL + company releases.

| Quarter | Revenue | YoY | Net income (GAAP) | Adj. net income | Realized Au price | AISC (Au) |
|---|---|---|---|---|---|---|
| Q1 2025 | $5,010M | — | $1,891M | — | — | — |
| Q2 2025 | $5,317M | — | $2,061M | — | — | — |
| Q3 2025 | $5,524M | — | $1,832M | — | — | — |
| FY2025 | $22,669M | — | $7,085M | — | — | — |
| Q1 2026 | $7,307M | +45.9% | $3,262M | $2.4B ($2.24/sh, per release) **[Corrected 2026-10-08: Q1 2026 adjusted net income was $3,156m, $2.90 per share (Q2 release summary table); $2.4B/$2.24 does not appear]** | ~$4,200/oz (est.) **[Corrected 2026-10-08: actual Q1 2026 average realized gold price $4,900/oz; Q1 by-product AISC $1,029/oz]** | below guide |
| Q2 2026 | $6,118M | +15.1% | $2,202M ($2.06/sh) | $2.2B ($2.10/sh) | $4,414/oz | $1,621/oz |

Nine-month FY26 not yet filed at cutoff (Q3 2026 10-Q due ~late October). H1 2026 operating cash flow $6,709M vs H1 2025 $4,415M (+52%). Cash rose from $3.6B (Dec-24) to $9.0B (Jun-26); long-term debt fell from $8.48B (Dec-24) to $5.08B (Jun-26) — net debt swung from ~+$4.9B to **net cash ≈ −$3.9B** (per V1's D3 pull, consistent with my own cash-minus-debt calc of $5.08B − $9.01B = −$3.93B).
Sources: Newmont 10-Q (2026-04-23, 2026-07-23), 10-K FY2025 (2026-02-19); Newmont press release "Newmont Reports Robust Second Quarter 2026 Results," newmont.com, 2026-08-13 (per 8-K exhibit filed 2026-08-13) **[Corrected 2026-10-08: the Q2 release and 8-K were filed 2026-07-23 (acc 0001164727-26-000034)]**; SEC XBRL companyfacts CIK 0001164727.

## 5. Guidance track record
Q2 2026 release: "remains on track to achieve full-year 2026 guidance" — maintained, not raised, despite the FCF beat; management is explicitly not extrapolating the gold price. AISC guidance ($1,680/oz full-year) has been beaten each of the last two quarters reported ($1,621 in Q2). This is a conservative-guidance pattern, consistent with a management team that does not want to be caught promising growth tied to a commodity price it cannot control.

## 6. Earnings quality & balance sheet
- **FCF conversion:** Q2 2026 FCF $2.2B vs GAAP NI $2.2B ≈ 1.0x — clean, no accrual red flags apparent in the quarters reviewed.
- **Balance sheet (consolidated):** net cash ≈ $3.9B (Jun-26); stockholders' equity $35.2B and rising every quarter. This is a genuinely strong, low-leverage balance sheet — net debt/EBITDA is negative.
- **Capital returns:** $1.9B returned to shareholders in Q2 2026 alone **[Corrected 2026-10-08: the release's $1.9B is 'since the last earnings call' (23 Apr to 23 Jul, incl. over $600m of July buybacks); cash-flow statement Q2 buybacks $1,567m plus dividends $277m = $1.84bn]** (dividend + buybacks) — aggressive capital return supports the cash thesis but also means less is being reinvested in reserve replacement; this is a red flag to monitor for reserve-life disclosures (not fully assessed at this depth).
- **Single-commodity exposure:** ~90%+ of revenue is gold; this is the dominant earnings-quality caveat — "quality" here is a function of price, not diversified business execution.

## 7. Valuation — reverse DCF, reconciliation with V1
**V1 has a row for NEM** (`v1_valuation_table.csv` / `v1_valuation.json`): verdict "fair" (score 0.246), core DCF implied 10-year FCF growth **−1.79%/yr** at WACC 8.30%, vs historical delivered CAGR 15.6% (5y) / 12.8% (10y) and consensus FY1 growth 9.1%. **I adopt V1's core DCF output** (implied growth −1.8%) — it is internally consistent with NTM P/E 12.2x and TTM FCF yield 6.9%/7.4% (SBC-adjusted).
**Data conflict — flagged, not adopted:** V1's own scenario table (`scenarios.bear/base/bull`) is internally broken: the "bear" case shows a *negative absolute stock price* (`price_yr3 = -18.91`), which is mathematically impossible for equity, and the "base" case's `annualised_return_3y = -28.7%` is inconsistent with its own assumed +7.9% revenue growth and +6.4pt margin expansion (which should produce EPS growth, not a collapse to $1.92 EPS from a >$8 TTM base). I do **not** use V1's scenario returns and instead compute my own below.
**My own scenario_returns_3y** (starting point: TTM EPS ≈ $8.06 **[Corrected 2026-10-08: sum of the four quarterly diluted EPS = $7.92 (1.67+1.19+3.00+2.06); NI $8,597m]** [NI $8.60B / ~1.067B diluted shares], NTM EPS consensus $9.97):
- **Bear:** gold reverts toward $3,200–3,400/oz (a ~30% correction from current spot), AISC leverage reverses; EPS falls to ~$4.50–5.00 by yr3; multiple compresses to 9x (trough historical); dividend ~$1.04/yr. → **≈ −11%/yr**. **[Corrected 2026-10-08: on the stated inputs (derived price $121.6, EPS 4.75, 9x, $1.04 dividends) the annualised return is about -28%]**
- **Base:** gold holds in a $4,000–4,500/oz range, EPS roughly flat to modestly down from today's peak (~$8.50 by yr3) as AISC inflation catches up slightly; multiple holds ~12x NTM (current). → **≈ +4%/yr**. **[Corrected 2026-10-08: on the stated inputs (EPS 8.50 x 12x = $102) the annualised return is about -5%]**
- **Bull:** gold continues toward $5,500+/oz, EPS grows to ~$11–12; multiple re-rates to 15x on de-risked net-cash balance sheet. → **≈ +22%/yr**. **[Corrected 2026-10-08: on the stated inputs (EPS 11.5 x 15x = $172.5) the annualised return is about +13%]**
**implied_vs_base = "below"** **[Corrected 2026-10-08: restated to IN_LINE (about 0% implied on the Q2 run-rate vs a flat-to-down base with falling volume); verdict INCLUDE-SMALL changed to WATCH, see Correction section]** — the market's implied growth (−1.8%/yr) is well below even my conservative base case (flat-to-modest EPS growth), which is why this is INCLUDE-rather-than-WATCH territory — but the single-commodity dependency and the magnitude of the recent price windfall (not yet "stress-tested" through a full cycle) are why it is sized small, not full weight.

## 8. Bull / Bear
**Bull:** (1) net-cash balance sheet and record FCF give real downside optionality (buybacks accelerate if gold falls, debt already low); (2) implied growth is deeply negative, i.e. priced for a gold-price reversal that has not yet happened; (3) AISC guidance has been beaten for two straight quarters, showing genuine cost discipline, not just a price tailwind.
**Bear:** (1) ~90%+ single-commodity revenue — a gold correction hits earnings dollar-for-dollar with almost no operating offset; (2) the entire "quality" score (ROE 25.9% per triage) is a function of an elevated gold price the company does not control and cannot be relied on to persist; (3) capital returns ($1.9B/quarter) are being funded by the price windfall, not by underlying volume growth — production growth is essentially flat **[Corrected 2026-10-08: wrong: attributable gold production fell 16% YoY in Q1-26 and 13% in Q2-26 (Ex-99.1 summary table); 2026 guidance is 5.3 Moz vs 5.89 Moz in 2025]**.

## 9. Key risks & measurable kill criteria
1. Gold spot price falls and stays below $3,200/oz for two consecutive quarters.
2. AISC (company-guided, per quarterly release) rises above $2,000/oz for two consecutive quarters (cost discipline breaking down).
3. Net cash position (LongTermDebt − Cash, consolidated, per 10-Q balance sheet) turns to net debt >$2B.
4. Quarterly production (attributable gold ounces) falls >10% YoY without an offsetting price effect already priced in. **[Corrected 2026-10-08: on volume alone this is already met (Q1-26 -16%, Q2-26 -13% YoY); the price offset (+33% YoY realized price) is the only reason it is not a clean trigger; re-base before relying on it]**
5. Full-year guidance is missed (not just "on track") in two consecutive quarterly releases.

## 10. Catalysts & calendar
Next scheduled earnings: Q3 2026 results, per D4 snapshot **2026-10-22**.

## 11. Red-flag scan
No auditor change, restatement, or going-concern language found in the FY2025 10-K or the two FY26 10-Qs reviewed. No SEC/DOJ investigation identified in this pass. Insider holding is negligible (~0.3% per Yahoo cross-check) — typical for a mega-cap. No short-seller report identified. The main "softer" flag is the commodity concentration itself, which is a business-model fact, not a governance issue.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q (period ended 2026-06-30, filed 2026-07-23) and the Aug-13-2026 8-K/press release. Checked for events to 2026-09-25 (no Q3 2026 filing yet — not due until ~late October per the calendar above). GAAP figures labelled GAAP; "adjusted net income" figures are the company's own release figures, cited and labelled, not independently recomputed. This report is research, not personal investment advice.

## 13. Sources
1. Newmont 10-K, FY2025 (filed 2026-02-19) and 10-Q Q1/Q2 2026 (filed 2026-04-23, 2026-07-23) — SEC EDGAR CIK 0001164727.
2. SEC XBRL companyfacts, CIK 0001164727, retrieved 2026-09-27.
3. Newmont press release, "Newmont Reports Robust Second Quarter 2026 Results; Remains on Track to Achieve Full Year Guidance," newmont.com, 2026-08-13.
4. v4/outputs/v1_valuation.json and v1_valuation_table.csv, NEM row (systematic reverse-DCF; scenario-table inconsistency flagged above).
5. v4/data/d4_live_snapshot.parquet (price/consensus cross-check, as of 2026-09-25).
6. v4/outputs/Q13_triage.json (prior triage note for NEM).

## Correction (verification DV30, 2026-10-08)

**1. Realized price and Q1 figures (wrong 'correction' of the triage).** The dossier said the triage's $4,900/oz was 'closer to spot in September, not the Q2 average' and put Q1-26 realized at '~$4,200/oz (est.)'. The Q2 release summary table (Ex-99.1 acc 0001164727-26-000034, filed 2026-07-23, not 2026-08-13) gives average realized gold price Q1-26 $4,900, Q2-26 $4,414 (YTD $4,661). The triage was right; the Q2 figure of $4,414/oz and Q2 AISC $1,621/oz in the dossier are correct. Q1-26 adjusted net income was $3,156m ($2.90 per share), not $2.4B ($2.24); Q1 GAAP net income $3,262m and Q2 GAAP $2,202m ($2.06) are correct; Q2 adjusted $2,246m ($2.10) is correct.

**2. Volume and costs (supports a verdict change).** The dossier states production is 'roughly flat'. Attributable gold production was 1.30 Moz in Q1-26 (Q1-25 1.54, -16%) and 1.29 Moz in Q2-26 (Q2-25 1.48, -13%); FY2025 was 5.89 Moz and 2026 guidance is 5.3 Moz. Q2 by-product AISC of $1,621/oz was up 58% on Q1 ($1,029) and 18% on Q2-25 ($1,375) after the Cadia seismic events (copper -43% QoQ); the full-year guide is $1,680. Kill criterion 4 (production down more than 10% YoY) is met on volume.

**3. Scenario returns (arithmetic).** With the dossier's own inputs (price implied by 12.2x NTM P/E on EPS $9.97 = $121.6; dividends $1.04/yr; bear EPS about $4.75 at 9x; base EPS about $8.50 at 12x; bull EPS about $11.5 at 15x) the annualised 3-year returns are about -28%, -5% and +13%, not -11%, +4% and +22%. The base case is a loss, not a gain.

**4. Valuation method and verdict (changes verdict).** The dossier adopts V1's implied -1.8%/yr as 'cheap'. The V1 DCF is a valid FCF model (reproduced: TTM FCF $9.73bn = 1,571+2,813+3,144+2,205; market cap about $130bn; WACC 8.3% vs 5.17% + beta x 4.14%) but TTM FCF includes the Q1-26 peak; on the Q2 run-rate ($8.8bn) the price implies about 0% growth, and the proper comparison is a base with falling volume and rising unit costs. implied_vs_base is **in_line**, and with the corrected scenario table (base -5%/yr) and the volume fall, INCLUDE-SMALL is not supported. **Verdict INCLUDE-SMALL -> WATCH.** F89_summary.json updated (verdict, implied_vs_base, reconciliation, scenarios, adverse facts, confidence).

**5. Smaller items.** TTM diluted EPS is $7.92 (sum of quarters), not $8.06. The '$1.9B returned in Q2 alone' is the release's 'since the last earnings call' figure; Q2 cash-flow statement buybacks $1,567m plus dividends $277m = $1.84bn. Balance-sheet figures are correct (cash $9,009m, debt $5,083m, equity $35,243m at 30 Jun 2026; Dec-24 debt $8,476m, cash $3,619m).
