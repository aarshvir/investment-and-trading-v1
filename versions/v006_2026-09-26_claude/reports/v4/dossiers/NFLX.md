# NFLX — Netflix, Inc.

## 1. Verdict
**INCLUDE-SMALL.** Horizon 24–48 months. Named reservation: the 25-Sep-2026 close ($71.14, post the Nov-2025 10-for-1 split) already prices in roughly the same ~11–12%/year 10-year FCF growth this analyst's own base case assumes — the stock is close to fully priced, not cheap, so the position should be small enough to survive a repeat of the Q3 2026 guidance disappointment rather than sized for a valuation margin of safety that does not currently exist.

## 2. Business in plain English
Netflix is the largest global subscription streaming video service (~300mn+ paid memberships across ad-supported and ad-free tiers), monetizing through subscription fees and a fast-growing advertising tier, and increasingly through live sports and events (NFL games, boxing, MLB). It makes money by amortizing a large content library and new productions across a subscriber base that scales globally with minimal incremental distribution cost, which is the source of its industry-leading operating margin (33%+).

## 3. Why the model likes it — durability check
b1 composite 0.405 (decile 5, quintile 3, live_rank 296 — a mid-pack quant rank, not a top-30 pick). The composite is carried by **Quality (fam_Q 0.72)** — ROE 45.3% (pct 77), OCF/assets 20.5% (pct 86), high gross-profit/assets (pct 51) — while **Value is weak (fam_V 0.32)** and **Momentum is barely above the median (fam_M 0.29)**, reflecting the post-Q3-guidance selloff. This is an honest signal, not an artefact: the model likes the business quality but is neutral-to-cautious on price and recent trend, which matches this analyst's own valuation finding below (fairly priced, not cheap).

## 4. Last two years of results (quarterly, GAAP, $mn, 10-Q, SEC EDGAR CIK 1065280; EPS restated for the Nov-2025 10-for-1 split)
| Quarter | Revenue | YoY | Op. income | Op. margin | Net income | Diluted EPS |
|---|---:|---:|---:|---:|---:|---:|
| Q3 2024 | 9,825 | — | 2,909 | 29.6% | 2,364 | 0.54 |
| Q1 2025 | 10,543 | — | 3,347 | 31.7% | 2,890 | 0.66 |
| Q2 2025 | 11,079 | — | 3,775 | 34.1% | 3,125 | 0.72 |
| Q3 2025 | 11,510 | +17.2% | 3,248 | 28.2% | 2,547 | 0.59 |
| Q1 2026 | 12,250 | +16.2% | 3,957 | 32.3% | **5,283** | **1.23** |
| Q2 2026 | 12,560 | +13.4% | 4,193 | 33.4% | 3,401 | 0.80 |

Q1 2026 net income ($5.28bn) is far above what the $3.96bn operating income and a normal tax rate would imply — Netflix does not report a non-GAAP EPS, but its shareholder letters have historically flagged FX remeasurement (on euro-denominated debt) and unrealized gains on equity investments as swing factors in "other income"; this quarter's GAAP EPS should be read with that caveat rather than as a clean run-rate. **Free cash flow fell to $1.53bn in Q2 2026 from $2.27bn in Q2 2025 (−32.6% yoy)** even as net income rose — FCF/NI conversion dropped from ~73% to ~45% quarter-over-quarter-yoy, the single most important adverse fact in this dossier (see §6).

## 5. Guidance track record (last 4 quarterly releases, company shareholder letters)
- **Q4 2025 letter → Q1 2026 guide:** delivered in line.
- **Q1 2026 letter → Q2 2026 guide:** revenue growth 13% (12% FX-neutral), op margin 32.6%. **Delivered: +13.4% growth, 33.4% margin — beat on both.**
- **Q1 2026 letter → FY2026 guide:** revenue $50.7–51.7bn (12–14% growth), op margin 31.5%.
- **Q2 2026 letter → FY2026 guide:** revenue narrowed to $51.0–51.4bn, op margin maintained at 31.5% — **same midpoint, narrowed range: maintained, not raised or cut.**
- **Q2 2026 letter → Q3 2026 guide:** revenue growth **11.7%** to $12.86bn and op margin 33.2% — a *deceleration* from the 13.4% just delivered, and **below sell-side estimates of ~$13bn**, which triggered a ~9% after-hours stock drop on the print (Variety, CNBC, 16-Jul-2026). This is the first quarter-over-quarter guided deceleration in the trailing four releases and is the leading indicator behind this dossier's "fully priced, not cheap" verdict.

## 6. Earnings quality & balance sheet
- **TTM (Q3'25–Q2'26): revenue $48.37bn, operating income $16.24bn (33.6% margin), FCF $11.15bn, gross debt $14.4bn, cash $9.1bn** (shareholder letter, cross-checked against XBRL LongTermDebtNoncurrent $11.83bn + other debt).
- **FCF conversion is the key watch item.** Q2 2026 FCF/NI (~45%) is well below the ~73% delivered a year earlier; management attributes part of this to elevated content amortization timing (flagged in the Q1 2026 letter as "the highest year-over-year content amortization growth rate in 2026" for Q2), but a single quarter of GAAP-NI-outpacing-cash is exactly the pattern this program's diligence template is built to catch — not yet a red flag, but a named, measurable item to track (kill criterion below).
- **Capital allocation is aggressive:** Q2 2026 buybacks were **$4.7bn, the largest single quarter in company history**, with $27.1bn of authorization remaining. This is funded by FCF and modest debt, not dilution — share count has fallen from ~4.22bn (year-end 2025, post-split) to ~4.16bn (30-Jun-2026).
- **Content/sports commitments are a growing, if not yet quantified-here, obligation:** new NFL games (Thanksgiving Eve, Christmas Day, a Week 1 game, the final week of the season through Q1 2027), the Tyson Fury–Anthony Joshua fight, and MLB events (Home Run Derby, Field of Dreams) — these are cash and/or amortization commitments layered on top of the existing content slate, a genuine but not yet fully disclosed cost tailwind.
- No debt maturity wall of concern identified in this window beyond a stated ~$1bn maturity being refinanced.

## 7. Valuation — no V1 row exists for NFLX; performed directly here (`scripts/valuation.py`, same FCFF reverse-DCF method V1 uses elsewhere in this program)
EV bridge: market cap $296.24bn + gross debt $14.4bn − cash $9.1bn = **EV $301.5bn**. Reverse DCF on TTM FCF $11.15bn, WACC 10.0% (CAPM-style: high-growth-media beta ~1.25, rf 5.17%, ERP 4.14%, minimal debt weight), 10-year fade to 3% terminal growth: **implied stage-1 FCF growth ≈ 11.2%/year for 10 years.**

**My base case:** ~12%/year revenue growth (matching the FY2026 guided range and the ad-tier/live-sports ramp), with operating margin drifting from ~33% toward ~34–35% as the ad business scales — a base-case FCF growth path close to, and not clearly above, the 11.2%/year priced in. **implied_vs_base = in_line.** This is genuinely different from a "cheap" call: NFLX is a high-quality compounder priced for high-quality compounding to continue almost exactly as guided, with very little room for the kind of guidance miss just seen in the Q3 2026 print.

**3-year scenario returns (from $71.14; no dividend):**
| Scenario | Revenue growth | Op. margin (yr3) | Exit P/E | EPS (yr3) | Price (yr3) | 3-yr ann. return |
|---|---:|---:|---:|---:|---:|---:|
| Bear | 7%/yr | 29% | 15x | $3.38 | $50.7 | **−10.7%** |
| Base | 12%/yr | 34% | 20x | $4.83 | $96.6 | **+10.7%** |
| Bull | 16%/yr | 37% | 25x | $5.93 | $148.2 | **+27.7%** |

## 8. Bull case
1. Ad-tier monetization and live sports/events (NFL, boxing, MLB) are new, incremental revenue levers layered on top of an already-profitable subscription base — Netflix is diversifying its growth drivers rather than relying solely on subscriber adds.
2. Capital discipline: management walked away from the WBD/Paramount-Skydance bidding war in Feb-2026 rather than overpay, and is instead returning capital at a record pace ($4.7bn buyback in a single quarter) — a demonstrated willingness to say no to expensive growth.
3. Quality metrics (45%+ ROE, 20%+ OCF/assets, industry-leading margins) are genuinely best-in-class among global media/streaming peers, evidenced in both the b1 factor scores and the primary filings.

## Bear case
1. The Q3 2026 guide (11.7% growth, below Street) is the first sign that the post-password-sharing-crackdown and ad-tier-launch growth burst is normalizing toward a lower structural rate — exactly the risk the triage flagged ("next leg of growth needs live sports/content execution").
2. FCF/NI conversion fell from ~73% to ~45% year-over-year in the most recent quarter, driven by content amortization timing; if this proves structural rather than timing-related as new sports rights layer on, the cash-generative character of the model — the main reason it commands a premium multiple — would be directly challenged.
3. At an implied 10-year FCF growth rate of ~11.2%/year against a base case of ~12%/year, there is essentially no valuation margin of safety; a single soft quarter (as just happened) can move the stock sharply because the price already assumes sustained execution.

## 9. Key risks & kill criteria (thesis-invalidation triggers)
1. Quarterly revenue growth decelerates below 10% YoY for two consecutive quarters (from 13.4% in Q2 2026 and an 11.7% Q3 2026 guide).
2. Full-year operating margin comes in below 30% (guided 31.5% for FY2026).
3. FCF/NI conversion stays below 60% for two consecutive quarters (Q2 2026 was ~45%, down from ~73% a year earlier).
4. Content/sports-rights cash commitments grow faster than revenue for two consecutive years (not yet quantified in company disclosure — a disclosure gap to monitor, not yet a confirmed trend).
5. Quarterly share buybacks fall below $2bn for two consecutive quarters without a stated reason (from a $4.7bn record in Q2 2026), suggesting management sees reduced value or emerging cash constraints.

## 10. Catalysts & calendar
Next earnings: **20-Oct-2026** (Q3 2026 results and shareholder letter, per company IR announcement).

## 11. Red-flag scan
No auditor changes, restatements, going-concern language or short-seller report identified in this review window. No major pending litigation or regulatory action identified (not exhaustively checked against the full 10-K legal-proceedings note — scope limitation, disclosed). **Data conflict / limitation:** the b1 quant snapshot's momentum score is weak (fam_M 0.29, well below the composite's other families) purely because of the recent post-guidance selloff — this is a real, current market reaction, not a data error, but it means the "Quality" story and the "Momentum" story currently point in different directions for this name.

## Data quality note, recency and disclaimer
All figures are on a **consolidated** basis (Netflix, Inc. and subsidiaries; no standalone/parent-only statements used). Most recent period incorporated: Q2 2026 10-Q (quarter ended 30-Jun-2026, filed 17-Jul-2026) and the Q2 2026 shareholder letter (8-K exhibit, same date). Events checked to 2026-09-25 close. GAAP figures are labeled GAAP throughout; Netflix does not publish a non-GAAP EPS, so no adjusted-vs-GAAP reconciliation exists to report, but the Q1 2026 GAAP EPS spike from non-operating items is flagged explicitly in §4/§6. No V1 systematic valuation row exists for this ticker; the valuation in §7 was built directly by this analyst using the same reverse-DCF/scenario method (`scripts/valuation.py`) V1 uses elsewhere in the program, so it is methodologically consistent but not independently cross-checked by a second agent. This is research, not personalised investment advice, and not a recommendation to buy or sell; the reader is responsible for their own decisions.

## 12. Sources
1. NFLX companyfacts (XBRL) — https://data.sec.gov/api/xbrl/companyfacts/CIK0001065280.json
2. NFLX Q2 2026 shareholder letter (8-K exhibit) — https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm
3. NFLX Q1 2026 shareholder letter (8-K exhibit) — https://www.sec.gov/Archives/edgar/data/1065280/000106528026000137/ex991_q126.htm
4. NFLX FY2025 10-K (filed 23-Jan-2026, accession 0001065280-26-000034) — https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/
5. Variety — "Netflix Q2 Earnings Results In-Line... Stock Drops on Lower Q3 Revenue Outlook" (16-Jul-2026) — https://variety.com/2026/tv/news/netflix-q2-2026-earnings-1236812558/
6. CNBC — Netflix Q2 2026 earnings coverage — https://www.cnbc.com/2026/07/16/netflix-nflx-earnings-q2-2026.html
7. CNBC — Netflix walks away from WBD bidding war (26-Feb-2026) — https://www.cnbc.com/2026/02/26/warner-bros-discovery-paramount-skydance-deal-superior-netflix.html
8. Netflix IR — Q3 2026 earnings-date announcement — https://ir.netflix.net/investor-news-and-events/financial-releases/press-release-details/2026/Netflix-to-Announce-Third-Quarter-2026-Financial-Results/default.aspx
9. Valuation calculator run (this analyst) — `stock-analysis` skill `scripts/valuation.py`, input archived at `C:\Users\user\eqv4\cache\F19\nflx_valuation.json`
10. v4 quant context — `v4/data/b1_live_scores.csv` (NFLX row)
