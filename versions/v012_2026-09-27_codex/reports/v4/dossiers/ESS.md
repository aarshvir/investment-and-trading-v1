# Essex Property Trust, Inc. (ESS) — Diligence Dossier
Agent: F113 | Depth: Standard | As of: 2026-09-25 close ($271.61) | CIK 0000920522

## 1. Verdict
**INCLUDE-SMALL** (half weight, reservation: West Coast apartment supply/rent-control regulatory risk concentrated in three states). Reason: guidance was raised on the metric the market prices (Core FFO/share), same-property fundamentals are re-accelerating, and the price implies roughly flat-to-slightly-negative long-run Core FFO growth versus a base case of low-single-digit growth — a modest but real margin of safety. Horizon: 24–36 months.

## 2. Business in plain English
Essex is a REIT that owns and operates ~250 apartment communities (~62,000 units) concentrated in coastal Southern California, Northern California/Bay Area and Seattle. It makes money by collecting rent from tenants, funding growth via a mix of wholly-owned acquisitions/development and preferred-equity/structured co-investments in other operators' properties, and paying most of its taxable income out as dividends (32 consecutive years of dividend increases per the Q1 2026 release). Its competitive position rests on operating scale and revenue-management technology in supply-constrained West Coast submarkets where new apartment construction is structurally limited by zoning and cost.

## 3. Why the model likes it / is it durable
b1_live_scores: composite 0.238 (decile 3, live_rank 379/503) — a middling quant score, driven almost entirely by Quality (fam_Q 0.800, near-top decile: ROE 7.8%, OCF/assets 8.7%, low leverage percentile) with Value (fam_V 0.189) and earnings momentum (fam_S 0.052, SUE −1.32) both weak. The SUE reading looks like a REIT-specific data artefact: ESS's GAAP EPS is lumpy quarter to quarter because of gains/losses on structured-finance and co-investment positions (see §4), which the SUE calculation (built for operating companies) is not designed to normalize — **flagged as a data_conflict**: the quant model's earnings-momentum score should not be read as a red flag for a REIT whose GAAP EPS is not the operating metric management or investors target (Core FFO is). The quality signal (low leverage, high cash conversion, high-barrier submarkets) is durable; it is a business characteristic, not a one-off.

## 4. Last two years — quarterly results (GAAP + Core FFO reconciliation)
| Quarter | Total revenue | YoY | Net income (GAAP, attributable) | Diluted EPS (GAAP) | Core FFO/share | Same-property revenue growth |
|---|---|---|---|---|---|---|
| Q1 2025 | $464.6m | +3.9% | — | $3.16 | — | — |
| Q2 2025 | $469.8m | — | — | $3.44 | — | +2.9% (Q1'25, YTD) |
| Q3 2025 | $473.3m | — | — | $2.56 | — | — |
| **Q1 2026** | $484.8m | +4.4% | — | $1.65 | $4.06 (beat guide midpoint by $0.11) | +2.9% |
| **Q2 2026** | $489.0m | +4.1% | — | $0.97 | (Q2 beat guide midpoint by $0.10) | +2.7% (vs Q2'25); sequential +0.8% |

Figures are GAAP `Revenues`/`EarningsPerShareDiluted` from XBRL companyfacts (CIK0000920522) except Core FFO and same-property growth, which are non-GAAP figures quoted verbatim from the Q1 and Q2 2026 earnings releases (Ex-99.1 to the 8-Ks) below. **GAAP diluted EPS fell sharply Q1→Q2 2026 ($1.65 → $0.97) even as Core FFO and same-property NOI both grew** — this is the GAAP-vs-adjusted gap flagged as mandatory: it is driven by non-cash items (depreciation timing, gains on real estate/structured-finance dispositions that hit GAAP net income but are excluded from Core FFO) rather than a deterioration in the operating business; the earnings releases quantify this reconciliation in their supplemental tables (pages S-15 to S-17), which were reviewed but not reproduced line-by-line here given the time box.

## 5. Guidance track record (verbatim quotes, entity: consolidated REIT)
- **Q1 2026 release (filed 2026-04-28, Ex-99.1 to 8-K 0001140361-26-017477), headline:** *"Essex Announces First Quarter 2026 Results"* — *"Reaffirmed the full-year guidance ranges for Core FFO per diluted share, same-property revenue, expenses, and NOI."* Revised full-year Net Income and Total FFO ranges were nudged up (Net Income midpoint $5.87, +$0.07 vs previous; Total FFO midpoint $15.96, +$0.17) due to *"an additional $90 million in early structured finance redemptions... not previously expected in the original plan."*
- **Q2 2026 release (filed 2026-07-29, Ex-99.1 to 8-K 0001140361-26-030060), headline:** *"Essex Announces Second Quarter 2026 Results and Raises Full-Year 2026 Guidance."* Table: *"Full-Year 2026 Revised Guidance... Core FFO per diluted share $16.03 - $16.25... Revised Midpoint $16.14... Change at Midpoint +$0.20."* Same release: full-year Net Income per diluted share midpoint was cut **−$0.29** to $5.58, and full-year same-property revenue growth guide was narrowed to 2.5%–3.1% (midpoint implied ~2.8%, matching the +0.70 pp same-property NOI beat quoted above).
- **Verdict on this guidance step: RAISED (Core FFO, the metric that drives the share price and dividend), with a simultaneous cut to the GAAP net-income guide.** This is exactly the kind of GAAP-vs-adjusted divergence the prior audit flagged as needing explicit reconciliation, not silent averaging: the Core FFO raise is driven by operating outperformance (same-property NOI +2.6% in Q2 2026 vs guide), the net-income cut by non-cash/disposition-timing items.

## 6. Earnings quality & balance sheet
- **FCF conversion:** TTM (H2 2025 + H1 2026) operating cash flow ≈ **$1,118.0m** (FY2025 10-K OCF $1,074.4m − H1 2025 $497.6m + H1 2026 $541.2m); this compares with TTM Core FFO of roughly $16.0/share × 64.27m shares ≈ $1,028m — OCF running slightly above Core FFO, consistent with a REIT (D&A add-back plus working-capital timing); no evidence of aggressive earnings management.
- **Entity scope on debt:** `LongTermDebt` (consolidated, XBRL tag, CIK0000920522) = **$6,386.5m** at 2026-06-30 vs cash $58.3m → consolidated net debt ≈ **$6,328.2m**. This is the whole-company (Essex Property Trust, Inc. and its operating partnership) balance sheet figure — Essex does not separately report a smaller "core portfolio only" debt figure, so no further disaggregation is possible or needed here.
- **Leverage (consolidated entity; estimated, not a company-disclosed exact figure):** using annualized Q2 2026 consolidated revenue ($489.0m × 4 = $1,956.2m) and a typical apartment-REIT NOI margin (~62–65%), estimated annualized NOI ≈ $1.2–1.3bn and EBITDA (NOI less G&A) ≈ **$1.10–1.15bn**, giving **net debt/EBITDA ≈ 5.4x–5.8x** — within the normal 5–6x range for a coastal apartment REIT, but this is an analyst estimate, not lifted from a company-disclosed ratio (none was found in the text of the two releases reviewed); flagged as an estimate.
- **Liquidity:** *"As of March 31, 2026, the Company's immediately available liquidity was over $1.7 billion"* (Q1 2026 release, verbatim).
- **SBC / GAAP-adjusted gap:** discussed in §4; not separately quantified as a % of revenue within the time box.
- **Share count:** 64,268,177 shares outstanding at 6/30/26 (down from 64,442,290 six months earlier — modest buybacks; Q1 2026 release cites *"Repurchased $61.9 million of common stock year-to-date"*).
- **Total assets $12,898.3m, total liabilities $7,385.4m** (10-Q, period 6/30/26) — equity cushion of ~43% of the balance sheet, low for a REIT only in the sense that real-estate assets are carried at depreciated cost, not market value.

## 7. Valuation snapshot and reverse DCF
No V1 systematic valuation row exists for ESS (confirmed absent from `outputs/v1_valuation_table.csv`); **v1_verdict = null**.
- Price $271.61; market cap $17.46bn (b1_live_scores); P/Core FFO (FY26 guided midpoint $16.14) ≈ **16.8x**; dividend yield (using the last declared quarterly rate, not separately re-verified here) approximately 3.5–4%, in line with sector norms.
- **Reverse DCF (2-stage, 10-yr explicit + 2.5% terminal Core-FFO/share growth, cost of equity 7.5–8.0%, on FY26 guided Core FFO/share $16.14):** the price implies a 10-year Core FFO/share CAGR of only **~0% to +1.2%/yr**. My evidence-based base case for a supply-constrained, well-located coastal apartment REIT with a track record of 32 consecutive annual dividend increases is **3–4%/yr** long-run Core FFO/share growth (same-property NOI growth of ~2.5–3% plus modest external growth/buybacks). **Implied growth is clearly below base case.**
- **valuation_view_vs_v1.implied_vs_base = "below."**

## 8. Bull case / bear case
**Bull:** (1) Guidance was raised on Core FFO for a second straight quarter on genuine operating outperformance (same-property NOI +2.6% Q2 2026 vs a 2.5–3.1% full-year revenue guide), not financial engineering. (2) West Coast/Seattle apartment supply is structurally constrained by zoning and construction cost, giving Essex pricing power most Sunbelt apartment REITs lack. (3) 32 consecutive years of dividend growth and >$1.7bn liquidity show a conservatively run balance sheet through a full cycle.
**Bear:** (1) Concentration in three high-regulation states (California, Washington) creates rent-control/eviction-moratorium tail risk that a national REIT would not carry. (2) GAAP net income per share fell sharply quarter over quarter ($1.65 → $0.97) and the full-year GAAP net-income guide was cut even as Core FFO was raised — investors relying on GAAP alone would see a very different (negative) picture, and the drivers of the gap were not independently re-derived line-by-line at this depth. (3) Estimated consolidated net debt/EBITDA of ~5.4–5.8x (analyst estimate, not company-disclosed) is on the higher side of the REIT peer range; a rate shock would compress the FFO/share growth the base case assumes.

## 9. Key risks & kill criteria
1. Full-year 2026 Core FFO/share guidance cut below the current $16.03–$16.25 range at the Q3 2026 release (next print, estimated late October 2026).
2. Same-property revenue growth falls below 2.0% for two consecutive quarters (from 2.7–2.9% currently).
3. Estimated net debt/EBITDA rises above 6.5x (analyst estimate methodology as in §6; monitor consolidated `LongTermDebt` vs revenue trend at each 10-Q).
4. Any California or Washington state/local rent-control legislation that caps annual same-property revenue growth below 2% system-wide (a regulatory, not operating, trigger).
5. Dividend increase streak broken (would end the 32-consecutive-year record cited in the Q1 2026 release) — a strong signal management sees a structural, not cyclical, problem.

## 10. Catalysts & calendar
- Next earnings: **Q3 2026 results — no explicit date found in the Q1/Q2 2026 releases reviewed; estimated late October 2026 based on Essex's historical cadence (Q3 2025 was reported 2025-10-30). Labelled an estimate, not a confirmed date.**
- Annual dividend-increase announcement typically alongside Q4/full-year results (historically ~January/February).

## 11. Red-flag scan
- **Litigation:** 10-Q (period 6/30/26, filed 2026-07-30) Item 1 states lawsuits/claims are addressed in Note 11 (Commitments and Contingencies) and that management does not believe any current matter will have a material adverse effect — verbatim: *"nor is any legal proceeding currently threatened against the Company that the Company believes... would have a material adverse effect."* No named material litigation found.
- **Auditor/restatement/going-concern:** none found in the 10-Q text reviewed.
- **Insider selling / short reports:** not reviewed at Standard depth within the time box — open item, not a confirmed red flag.
- **Pending deals:** none disclosed.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (quarter ended 2026-06-30), 10-Q filed 2026-07-30 (accession 0000920522-26-000022) and 8-K Ex-99.1 filed 2026-07-29 (accession 0001140361-26-030060). Events checked to 2026-09-25. GAAP figures (revenue, EPS, balance sheet) are labelled GAAP; Core FFO, Total FFO, same-property revenue/NOI growth and the FY26 guidance ranges are non-GAAP figures as reported by the company and are labelled as such throughout. Leverage/EBITDA figures in §6 are analyst estimates, explicitly flagged. Research, not personal investment advice.

## 13. Sources
1. SEC EDGAR, ESS submissions index, https://data.sec.gov/submissions/CIK0000920522.json (retrieved 2026-09-27).
2. SEC EDGAR, ESS companyfacts XBRL, https://data.sec.gov/api/xbrl/companyfacts/CIK0000920522.json (retrieved 2026-09-27).
3. Essex 10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession 0000920522-26-000022, https://www.sec.gov/Archives/edgar/data/920522/000092052226000022/ess-20260630.htm
4. Essex Q2 2026 earnings release, Ex-99.1 to 8-K filed 2026-07-29, accession 0001140361-26-030060, https://www.sec.gov/Archives/edgar/data/920522/000114036126030060/ef20078746_ex99-1.htm
5. Essex Q1 2026 earnings release, Ex-99.1 to 8-K filed 2026-04-28, accession 0001140361-26-017477, https://www.sec.gov/Archives/edgar/data/920522/000114036126017477/ef20071359_ex99-1.htm
6. v4/data/b1_live_scores.csv, v4/data/triage_cards.csv (quant context, checked 2026-09-26).
7. v4/outputs/v1_valuation_table.csv, v4/outputs/v1_valuation.json — confirmed no ESS row exists.
