# FIX — Comfort Systems USA, Inc. — Diligence Dossier (Agent F60, Wave 3)

## 1. Verdict
**WATCH** (12–24 month horizon). A genuinely strong, structurally-growing mechanical/electrical contractor riding the data-center capex cycle, but at a 29x NTM P/E (73rd percentile of its own 10-year history) with heavy insider selling and a single-end-market concentration risk, there is no margin of safety — my own corrected reverse DCF shows the market pricing in growth roughly at (not below) my base case. A great business, but not cheap enough right now to hold at full or half weight.

## 2. Business in plain English
Comfort Systems USA installs and services mechanical (HVAC, plumbing, process piping) and electrical systems for large commercial, industrial and — increasingly — data-center construction projects across the US. It earns money on design-build and installation contracts (increasingly modular, prefabricated in its own plants) plus a growing recurring service book. Its competitive position has shifted from a diversified regional mechanical contractor to the leading specialist for hyperscale data-center electrical/mechanical build-outs, which now generate the majority of growth.

## 3. Why the model likes it — durable or artefact?
b1 factor scores rank FIX in the top decile on quality (gross-profit/assets 84th pct, ROE 97th pct) and momentum (96th pct 12-1m), with earnings-momentum (SUE) also very strong (90th pct). This is **not** an accounting artefact: revenue, operating income and backlog have all inflected together (see §4), and management describes the technology/data-center mix explicitly (58% of H1 2026 revenue vs 40% a year ago — Q2 2026 earnings call, 2026-07-23). It is, however, a **concentration** story — the growth driver is one end market (data centers/hyperscalers), so durability depends on continued hyperscaler capex, not diversification.

## 4. Last two years of results (quarterly, GAAP; source: SEC XBRL companyfacts, cross-checked against each 10-Q/10-K)
All figures consolidated (Comfort Systems USA, Inc., CIK 0001035983). $ in millions except EPS.

| Quarter end | Revenue | YoY growth | Operating income | Op. margin | Diluted EPS |
|---|---|---|---|---|---|
| 2024-03-31 | 1,537.0 | — | 135.5 | 8.8% | 2.69 |
| 2024-06-30 | 1,810.3 | +39.6%¹ | 184.7 | 10.2% | 3.74 |
| 2024-09-30 | 1,812.4 | +31.5% | 202.9 | 11.2% | 4.09 |
| 2024-12-31 (derived²) | 1,867.8 | — | 227.4 | 12.2% | 5.35³ |
| 2025-03-31 | 1,831.3 | +19.1% | 209.1 | 11.4% | 4.75 |
| 2025-06-30 | 2,173.3 | +20.1% | 299.9 | 13.8% | 6.53 |
| 2025-09-30 | 2,451.0 | +35.2% | 378.9 | 15.5% | 8.25 |
| 2025-12-31 (derived²) | 2,646.1 | +41.7% | 426.7 | 16.1% | 9.35³ |
| 2026-03-31 | 2,865.3 | +56.5% | 485.7 | 17.0% | 10.51 |
| 2026-06-30 | 3,265.7 | +50.3% | 558.0 | 17.1% | 12.53 |

¹ vs Q2-2023 ($1,296.4M). ² Q4 = audited FY total (10-K) minus the sum of the three reported quarters; not separately filed. ³ Derived the same way from full-year diluted EPS.
Revenue/OI acceleration through 2025–26 is real and broad-based (every quarter both YoY growth and op. margin expanded); FY2023 $5,206.8M → FY2024 $7,027.5M → FY2025 $9,101.6M (10-K, filed 2026-02-19). TTM (Q3-25–Q2-26) revenue = **$11,228.0M**, TTM operating income = **$1,849.3M** (16.5% margin), TTM diluted EPS **$40.64**.

**Data-integrity finding (important — see §7 and the mandatory entity-scope note):** the quant pipeline's TTM revenue input for FIX ($3,957,669,000, used in `outputs/v1_valuation.json`) and TTM EBIT input ($743,811,000) are wrong by roughly 2.8x. I traced this to a filer XBRL tagging bug: FIX's Q1-2026 10-Q duplicate-tagged the **Q1 2025 quarter's** revenue/EPS/operating-income facts with a **full-calendar-year 2025** context (`start=2025-01-01, end=2025-12-31`, value $1,831,286,000 — which is exactly the real Q1-2025 quarterly revenue, filed 2026-04-23, accession 0001104659-26-047689). The correct FY2025 figure, taken from the audited 10-K (filed 2026-02-19, accession 0001104659-26-017530) with the same start/end dates, is $9,101,641,000. D3/V1 evidently picked up the erroneous duplicate context. OCF, capex and SBC inputs in the same V1 record are **not** affected (they reconcile exactly to the cash-flow statement — verified independently below) — only revenue and EBIT.

## 5. Guidance track record
FIX does not issue formal quarterly point guidance (no revenue/EPS ranges). It gives a full-year same-store growth framework on the earnings call. Most recent (Q2 2026 call, 2026-07-23, transcript): management guided **full-year 2026 same-store revenue growth in the mid-to-high 30% range**, explicitly citing tougher H2 comparisons — i.e. a deceleration from H1's 50%+ reported growth is management's own expectation, not a surprise. Backlog reached $14.1B at Q2-26 (+73% YoY, +$1.6B sequentially); management said the current backlog is "already planned and permitted" and that a slowdown would more likely show up as projects moving location than disappearing (Q2-26 call). No guidance cuts identified in the last four releases (Q3-25, Q4-25/FY25, Q1-26, Q2-26); each showed sequential acceleration in backlog and margin.

## 6. Earnings quality & balance sheet
- **Entity scope: all figures below are consolidated (Comfort Systems USA, Inc., 10-Q/10-K).** FIX does not break out a separate finance subsidiary; there is no bank/insurance-style regulatory capital measure.
- **FCF conversion:** TTM (Q3-25–Q2-26) operating cash flow $2,550.1M vs TTM net income $1,434.4M → **OCF/NI = 1.78x** (very strong, backlog-advance-billing driven; confirmed by summing the cash-flow statement's discrete quarters from each 10-Q, not a single filing's YTD figure). TTM capex $390.3M → **FCF (OCF–capex) = $2,159.8M**, FCF/NI = 1.51x.
- **SBC:** TTM $38.2M, or 0.34% of TTM revenue — immaterial GAAP/adjusted gap; FIX does not report a non-GAAP adjusted EPS.
- **Net cash position (not net debt):** cash $1,854.8M vs total debt (long-term $54.1M + current portion $0.2M) $54.3M at 2026-06-30 (10-Q balance sheet) → **net cash ≈ $1.80B**, consistent with the (correctly-computed) V1 net-debt input of –$1,800.7M. Leverage is a non-issue.
- **Working capital:** ΔNWC has been a large **source** of cash (contract-asset/liability mix favors FIX as billings run ahead of costs on the growing project book) — a genuine structural feature of the model shift toward larger, milestone-billed data-center jobs, not a one-off.
- **Buybacks/dividend:** FY2025 buybacks $216.0M; quarterly dividend raised four times in five quarters ($0.40→$0.45→$0.50→$0.70→$0.80, per share, 10-Q dividend-declared disclosures) — trivial yield (~0.2%) but a real, fast-growing capital return.
- **Share count:** ~35.25M diluted, slowly declining (buybacks modestly exceed dilution).

## 7. Valuation snapshot — and reconciliation with V1
V1 (`outputs/v1_valuation.json`/`v1_valuation_table.csv`) verdict: **excessive** (score –0.84), NTM P/E 29.0x (73rd pct of 10-yr own history; peers EME/J/PWR median 25.2x, n=4 — this multiple and percentile are correct, they don't depend on the broken revenue input), bear/base/bull annualised 3y returns **–68.8%/–51.8%/–34.7%**, flagged "base 3y value below Street 12m low target."

**I disagree with V1's scenario returns and the "Street flag," and partially with the "excessive" label**, for a primary-source reason: V1's FCFF reverse-DCF used the corrupted $3.96B TTM-revenue input (§4) as `revenue_base`, and a correspondingly wrong $0.744B TTM EBIT, producing a nonsensical implied 10-year growth rate of 74.7% and a year-3 base-case value of $185/share against an $1,658.91 price (the model needed extreme growth to reconcile a real EV against an artificially tiny revenue base). Its Street-target sanity check ($1,910–$2,500) is in fact **above** the current price — i.e., Street targets do not support "excessive" at all; V1's own flag logic compared them to the broken $185 base-case price, not to the raw target range.

Redoing the reverse DCF with the corrected TTM figures (revenue $11,228.0M, EBIT $1,849.3M; capex, D&A, SBC, ΔNWC, net debt, shares, WACC 10.37% all unchanged from V1, since I verified those independently reconcile to the cash-flow statement) and the same 10-year-fade-to-3%-terminal method, EV0 = $56,682M implies a **10-year FCF growth rate of ~11.6%/yr** (vs. V1's 74.7%) — below trailing 5-yr delivered CAGR is not the right comparison here (5-yr delivered 7.2% predates the data-center inflection), but roughly **in line with** consensus next-year growth (19.0%) once you average in the deceleration management itself is guiding for H2 2026 onward.

My own explicit 3-year scenario (EPS × exit-multiple + dividends, independent of V1's broken FCFF machinery):
- **Base:** EPS grows from TTM $40.64 to ~$49 (FY26, consistent with the mid-to-high-30s guide) → ~$60 (FY27, using the pre-existing D4 forward estimate of $60.18) → ~$70 (FY28, growth decelerating to ~16%), exit at 24.4x (V1's own calibrated base-case multiple, unaffected by the revenue bug) ≈ $1,708/share + ~$11 cumulative dividends ≈ $1,719 → **annualised 3y return ≈ +1.2%**.
- **Bear:** data-center capex pause; EPS growth stalls to ~5%/yr after FY26 (~$49→$51→$54), multiple de-rates to 16x (below the 25.2x peer median, penalising the growth disappointment) ≈ $790/share + div ≈ $799 → **≈ –21.5%/yr**.
- **Bull:** growth keeps compounding at ~30%+ (backlog conversion, further margin gains toward 19–20%) → EPS ~$50→$65→$85, multiple holds at the current 29x ≈ $2,465 + div ≈ $2,476 (consistent with the Street's own $2,500 high target) → **≈ +14.4%/yr**.

**valuation_view_vs_v1:** v1_verdict "excessive" is **not confirmed** — it rests on a data bug, not a real overvaluation finding. My own view is **fair/in_line**: the stock prices in growth close to my base case, with real downside if the single-end-market thesis breaks (bear case –21.5%/yr) and only modest upside if it does not (base case ≈ flat). That thin margin of safety, not "excessiveness," is why this is a WATCH.

## 8. Bull case / Bear case
**Bull (3):** (1) Data-center/hyperscaler capex supercycle continues for several more years; FIX's modular manufacturing capacity is still expanding 30%+ and is a genuine capacity moat competitors can't quickly replicate. (2) Backlog ($14.1B, +73% YoY) already exceeds TTM revenue, giving >1 year of revenue visibility; management says projects are "planned and permitted," reducing air-pocket risk. (3) Margin expansion (8.8%→17.1% operating margin in two years) reflects a genuine mix shift to higher-value technology/data-center work, not merely operating leverage on a cyclical peak.

**Bear (3):** (1) Revenue and backlog are now concentrated in one capital-spending cycle (hyperscaler data-center capex); a pause or share loss to competitors (EME, PWR, in-house hyperscaler build teams) would hit disproportionately given the technology segment is now 58% of revenue. (2) Heavy insider selling: CEO Brian Lane and CFO William George sold a combined ~$82M in Feb 2026 alone, part of ~$152M of insider sales over the trailing year with zero purchases (Form 4 filings via SEC/press aggregation) — consistent with insiders viewing the valuation as full, even if legally routine (10b5-1 plans not confirmed from the filings reviewed). (3) At 29x NTM P/E (73rd percentile of FIX's own 10-year history) there is little room for even a modest growth disappointment before a sharp de-rating (bear case above).

## 9. Key risks & kill criteria (measurable)
1. Same-store backlog growth turns negative for two consecutive quarters (vs the +69% same-store backlog growth reported at Q2-2026).
2. Technology/data-center segment revenue share falls below 45% of total revenue for two consecutive quarters (vs 58% at H1-2026), signalling the growth driver is fading without being replaced.
3. Operating margin compresses by more than 200 bps YoY in any quarter (vs the current 17.1%, Q2-2026).
4. Net insider selling exceeds $100M in any rolling 6-month window with zero offsetting purchases (trailing-year run-rate already ~$152M; a further acceleration would be a stronger signal).
5. Diluted EPS growth (YoY) falls below 15% for two consecutive quarters — well below the current 56–91% pace and below even management's own guided deceleration.

## 10. Catalysts & calendar
- Next earnings: **Q3 2026, expected ~2026-10-22** (based on the historical Oct-22/23/24 reporting pattern; not yet confirmed by an 8-K as of this dossier's writing).
- Ongoing: quarterly backlog and same-store growth disclosure is the key data point to watch each release; no investor day or index event identified in the review window.

## 11. Red-flag scan
- **Auditor / restatements / going concern:** none identified in the 10-K (FY2025, filed 2026-02-19) or subsequent 10-Qs reviewed.
- **Litigation:** the 10-K/10-Q note ordinary-course claims and lawsuits with insurance coverage and accruals for probable losses; no SEC/DOJ investigation or material litigation disclosed in the filings reviewed (no primary-source litigation item found beyond standard boilerplate).
- **Insider selling:** see §8 bear case — a real, well-documented pattern (secondary-source aggregation of Form 4 filings; I did not individually re-derive each Form 4 but the cluster of Feb-2026 C-suite sales is corroborated across multiple aggregators).
- **Data integrity:** the revenue/EBIT XBRL tagging bug described in §4/§7 is the most significant finding of this dossier — it invalidates V1's FIX-specific reverse DCF and should be corrected in the shared valuation pipeline (flagged to the lead separately).

## 12. Data basis, recency and disclaimer
Most recent period incorporated: 10-Q for the quarter ended 2026-06-30 (filed 2026-07-23, accession 0001104659-26-086258); FY2025 10-K filed 2026-02-19 (accession 0001104659-26-017530). Checked for events to 2026-09-25 (price, guidance, insider-trading commentary, litigation searches all dated through September 2026). GAAP vs adjusted: FIX reports GAAP only; no company non-GAAP EPS exists, so all figures above are GAAP unless marked "guided"/"estimate." Research, not personal investment advice.

## 13. Sources
1. SEC EDGAR submissions/companyfacts, CIK 0001035983: `https://data.sec.gov/submissions/CIK0001035983.json`, `https://data.sec.gov/api/xbrl/companyfacts/CIK0001035983.json` (retrieved 2026-09-26).
2. FIX 10-K, FY2025, filed 2026-02-19: `https://www.sec.gov/Archives/edgar/data/1035983/000110465926017530/fix-20251231x10k.htm`.
3. FIX 10-Q, Q2 2026, filed 2026-07-23: `https://www.sec.gov/Archives/edgar/data/1035983/000110465926086258/fix-20260630x10q.htm`.
4. FIX 10-Q, Q1 2026, filed 2026-04-23 (source of the duplicate-context XBRL tagging bug), accession 0001104659-26-047689.
5. Investing.com, "Comfort Systems Q2 2026 slides: revenue tops $3B, backlog hits $14B," 2026 (backlog, same-store guidance): https://www.investing.com/news/company-news/comfort-systems-q2-2026-slides-revenue-tops-3b-backlog-hits-14b-93CH-4812234
6. Yahoo Finance, "Comfort Systems USA Inc (FIX) Q2 2026 Earnings Call Highlights," 2026: https://finance.yahoo.com/markets/stocks/articles/comfort-systems-usa-inc-fix-230035794.html
7. Finexus/Insider Monkey/MarketBeat insider-trading aggregation (CEO/CFO Feb-2026 sales, trailing-year $152M total), 2026.
8. `v4/outputs/v1_valuation.json`, `v4/outputs/v1_valuation_table.csv` (FIX row) — systematic valuation reconciled and partially disputed above.
9. `v4/outputs/Q09_triage.json` (FIX triage entry, quality/growth/price_vs_growth scores and red flag).
