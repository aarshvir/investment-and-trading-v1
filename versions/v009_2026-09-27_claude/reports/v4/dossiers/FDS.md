# FDS — FactSet Research Systems Inc. (Diligence dossier, agent F66, standard depth)

## 1. Verdict
**INCLUDE-SMALL** (12–36 month horizon), with a named reservation: an internal-control material weakness first identified in FY2024 is still unremediated two fiscal years later, and the company has churned through its CFO and reshuffled its top technology leadership within the last six months. FactSet is a high-quality, high-switching-cost financial-data subscription business priced, on my own reverse-DCF read, for near-zero long-run FCF growth — but the near-term numbers (Q3 FY2026 GAAP operating margin fell 650bp YoY) show the controls/leadership turmoil is not merely paperwork; it is showing up in the P&L. No V1 systematic valuation row exists for FDS (`v1_valuation_table.csv` has no FDS entry); `v1_verdict` = null.

## 2. Business in plain English
FactSet sells subscription access to a financial data, analytics and portfolio/research workstation platform used by asset managers, banks, wealth managers and corporates. Clients pay recurring "Annual Subscription Value" (ASV) fees for data feeds, the desktop workstation, ESG/analytics tools and (increasingly) AI-assisted research products; FactSet earns money on very high incremental margins as it adds users onto already-built infrastructure. Its moat is switching cost: portfolio and research workflows are built around FactSet's data model and interfaces, and clients (~9,130 of them, 247,766 users as of 31 May 2026) sign multi-year subscriptions with retention above 95%.

## 3. Why the model likes it — durable or artefact?
Disqualifying-flag gate: checked — the Q05 triage found no disqualifying red flag for FDS (only a competitive-pressure watch-item), and this diligence pass independently confirms no disqualifying red flag, though it does surface the material weakness and leadership-turnover items in §9/§12 that are not disqualifying but are material.
Per `v4/data/b1_live_scores.csv` (as of 2026-09-25): FDS composite decile 8/10, quintile 4, live_rank 146 of ~500. Factor percentiles: quality (fam_Q) strong — pct_roe 0.69, pct_ocf_a 0.75, pct_leverage 0.79 (i.e., FDS uses more balance-sheet leverage than most peers, not less — flagged, not necessarily bad given its FCF stability); value (fam_V) percentiles are moderate-to-strong — pct_ep 0.62, pct_bp 0.75 (book/price, unusually high for an asset-light business — reflects a low book value per share versus buybacks, not unusual cheapness); momentum weak (pct_mom_12_1 0.31 — the stock has lagged over the last year, consistent with the margin/EPS deceleration found below); earnings-momentum (SUE) very weak, pct_sue 0.14. **This is a genuine mixed signal, not a clean "quality growth" story**: the model likes FDS mainly on quality-persistence and a modest value tilt, while price momentum and earnings surprise are actively negative — both durable facts, confirmed in the primary filings (§4), not artefacts of stale data.

## 4. Last two years of results (fiscal quarters end Feb/May/Aug/Nov; consolidated; source: 10-Q/10-K XBRL, CIK 0001013237, and quarterly earnings releases, Ex-99.1)
| Quarter (FQ end) | GAAP revenue ($M) | GAAP op. margin | Adj. op. margin | GAAP diluted EPS | Adj. diluted EPS |
|---|---|---|---|---|---|
| Q3 FY24 (31-May-24) | 529.8 | n/a | n/a | n/a | n/a |
| Q4 FY24 (31-Aug-24) | ~552 | n/a | n/a | n/a | n/a |
| Q1 FY25 (30-Nov-24) | 542.2 | n/a | n/a | $3.84 | n/a |
| Q2 FY25 (28-Feb-25) | 545.9 | n/a | n/a | $3.70 | n/a |
| Q3 FY25 (31-May-25) | 585.5 | 33.2% | 36.8% | $3.87 (as later restated basis) | $4.05 |
| Q4/FY25 (31-Aug-25) | 596.9 (Q4); 2,321.7 (FY) | 29.7% (Q4); 32.2% (FY) | 33.8% (Q4); 36.3% (FY) | $4.03 (Q4); $15.55 (FY) | $4.05 (Q4); $16.98 (FY) |
| Q1 FY26 (30-Nov-25) | 607.6 | n/a | n/a | $3.95 | $3.89 |
| Q2 FY26 (28-Feb-26) | 611.0 | n/a | n/a | $3.60 | $3.76 |
| Q3 FY26 (31-May-26) | 622.9 | **26.7%** | **34.0%** | $3.50 | n/a (Q3 reconciliation in 10-Q) |

Q3 FY26 vs Q3 FY25: GAAP revenue +6.4% (organic +7.0%); **GAAP operating margin fell from 33.2% to 26.7%** and adjusted operating margin fell from 36.8% to 34.0% — both down, so the margin story is not purely a one-off add-back. The 10-Q attributes this to "higher operating expenses, mainly due to an increase in employee compensation costs, including one-time restructuring charges and Chief Executive Officer ("CEO") compensation costs pursuant to the terms of his employment agreement" (10-Q, MD&A, p.34). Net income fell 14.7% YoY and diluted EPS fell 9.6% to $3.50. As of 31-May-2026, Organic ASV was $2,485.6m, +7.1% YoY — all three regions grew (Americas +7.2%, EMEA +5.6%, Asia Pacific +10.0%), driven mainly by data solutions and workstations.

## 5. Guidance track record (last 4 releases, FY2026, all primary-source press releases furnished as 8-K Ex-99.1)
| Release (date) | Organic ASV growth | GAAP revenue | GAAP diluted EPS | Adjusted diluted EPS | Action |
|---|---|---|---|---|---|
| Q4/FY25 (18-Sep-2025) — initial FY26 guide | $100M–$150M (4–6%) | $2,423M–$2,448M | $14.55–$15.25 | $16.90–$17.60 | Initial |
| Q1 FY26 (18-Dec-2025) | $100M–$150M | $2,423M–$2,448M | $14.55–$15.25 | $16.90–$17.60 | **Reaffirmed** |
| Q2 FY26 (31-Mar-2026) | $130M–$160M | $2,450M–$2,470M | $14.85–$15.35 | $17.25–$17.75 | **Raised** (explicitly "up from" the prior range on every line) |
| Q3 FY26 (1-Jul-2026) | $130M–$160M | $2,450M–$2,470M | $14.85–$15.35 | $17.25–$17.75 | **Reaffirmed** |

FactSet has a genuine, primary-source-verified pattern of raising and then holding FY2026 guidance — this is a real positive, but note the raise (Mar-2026) came before the margin deterioration disclosed in the Q3 (Jul-2026) 10-Q became fully visible in the operating-margin line; the reaffirmation in July did not walk back the EPS range despite the margin miss, implying management expects the Q4 quarter (not yet reported as of this cutoff) to absorb the gap.

## 6. Earnings quality & balance sheet
**Entity scope: all figures are FactSet Research Systems Inc. consolidated, from the 10-Q for the quarter ended 31-May-2026 (filed 1-Jul-2026, accession 0001628280-26-046549), unless noted.**
- **FCF conversion:** FY2025 free cash flow $617.5M vs FY2025 net income (GAAP) ~$561M (FY25 diluted EPS $15.55 × ~36.1M avg diluted shares) → FCF/NI ≈ 110%, a strong conversion consistent with a subscription, low-capex model.
- **SBC / adjustments:** Q3 FY26 operating-income bridge to adjusted: intangible amortization $19.0M, restructuring/severance $19.6M, CEO compensation costs $4.3M, business disposition/acquisition costs $1.8M, client bankruptcy charge $0.75M — adjusted operating income $211.8M vs GAAP $166.3M, i.e., **>20% of Q3 operating income is add-backs**, a meaningfully wider GAAP-vs-adjusted gap than FactSet has historically run (source: 10-Q Non-GAAP reconciliation table, p.42).
- **Balance sheet (instant, 31-May-2026):** total assets $4,192.0M; total liabilities $2,159.7M; cash & equivalents $288.1M + short-term investments $16.1M; long-term debt $890.5M + current portion $499.2M = **total debt $1,389.7M**; net debt ≈ **$1,085M**. Stockholders' equity $2,032.3M (down from $2,186.4M a year earlier, mainly via buybacks). Shares outstanding fell from 37.65M (Aug-2025) to 35.78M (May-2026), −4.9% in nine months.
- **Capital return:** $243.4M returned to stockholders (buybacks + dividends) in Q3 FY26 alone; 926,370 shares repurchased at avg $219.21; $494.0M remained under the buyback authorization as of 31-May-2026.
- **Sales Tax Dispute (resolved):** a multi-year Massachusetts Department of Revenue sales-tax matter (tax periods 2006–2023) was fully settled 26-Nov-2024; cumulative charges/payments ≈$66.2M, with a $2.4M charge and $56.4M cash payment in Q1 FY2025. No open balance remains (10-Q Note 11).
- **M&A:** two small tuck-ins on the balance sheet — LiquidityBook (goodwill $164.8M) and Irwin (closed 5-Nov-2024, goodwill $91.4M) — both immaterial to leverage.

## 7. Valuation snapshot and reconciliation with V1
- **No V1 row exists for FDS** (confirmed absent from `v4/outputs/v1_valuation_table.csv`). Per program rule, `v1_verdict` = **null**.
- Quant snapshot (b1, 25-Sep-2026 close, price $273.08): trailing earnings yield (ep) 7.29% (~13.7x), FCF yield (fcfp) 6.67% (~15.0x P/FCF) — both consistent with the triage note's "13.8x forward." My own trailing-guidance-based check: FY2026 guidance midpoints (GAAP diluted EPS ~$15.10, adjusted ~$17.50) imply a trailing **GAAP P/E ≈ 18.1x** and **adjusted P/E ≈ 15.6x** — the gap versus the b1 "13.7x" figure is explained by the b1/d4 metric using a forward (next-FY) consensus EPS base, which is higher than the FY2026-just-completed base, given expected continued ASV-driven EPS growth.
- **My own reverse DCF** (2-stage FCF model; FCF0 ≈ $640M [FY2025 $617.5M, grown modestly for FY26 ASV growth]; EV ≈ market cap $273.08 × ~35.8M shares + net debt $1.09bn ≈ $10.87bn; WACC 8.5%; 10-year explicit growth then 3% terminal): implied 10-year FCF growth ≈ **1.8%/yr** — the market is pricing FactSet as barely growing at all.
- **My bear/base/bull (10-yr FCF/EPS growth), evidence-based:**
  - **Bear** (organic ASV growth continues decelerating toward 4–5%, AI-native research tools and Bloomberg/LSEG pricing pressure erode net retention, margin stays depressed by CEO-comp/restructuring drag): ≈ 1–3%/yr — close to the implied rate; downside mainly from multiple compression, not FCF decline.
  - **Base** (Organic ASV growth stabilizes at 6–8% per recent quarters, restructuring/CEO-comp add-backs roll off by FY2027, adjusted margin recovers toward 35–36%): ≈ 7–9%/yr.
  - **Bull** (AI/analytics products re-accelerate ASV growth into double digits, cost discipline restores margin above 37%): ≈ 12–15%/yr.
  - All three scenarios sit **above** the ~1.8%/yr implied rate → `implied_vs_base` = **below** (cheap on a pure numbers basis).
- valuation_view_vs_v1: no v1 row to reconcile against (null); dossier_view = **cheap**, but I weight this less heavily than usual because the cheapness coincides with a real, disclosed deterioration in controls and margin, not merely sentiment — see kill criteria.

## 8. Bull case
1. Organic ASV growth is accelerating, not decelerating — $2,485.6M as of May-2026, +7.1% YoY, with growth in all three regions and enterprise renewals extending 30% in average length, annual ASV retention >95% (Q3 FY26 earnings release, Operational Highlights).
2. Guidance has been raised once and reaffirmed twice through FY2026 despite the margin miss — management is not walking back full-year expectations.
3. Strong, growing capital return: $243M returned in Q3 alone; share count down ~5% in nine months; $494M of buyback capacity still authorized.

## 9. Bear case
1. GAAP operating margin fell 650bp YoY in Q3 FY26 (33.2%→26.7%) and adjusted margin fell 280bp (36.8%→34.0%) — both down, driven by restructuring and new-CEO compensation costs that are real cash/dilution costs, not merely accounting noise.
2. A material weakness in IT general controls, first identified FY2024, remains unremediated as of the Q3 FY26 10-Q (filed 1-Jul-2026) — management "is targeting completion of these remediation measures during fiscal 2026," meaning it has already run past one full fiscal year without resolution.
3. Leadership churn: new CFO (Joshua Warren, effective 13-Apr-2026, ex-Envestnet) within the same year the CTO was reassigned to "Chief AI Officer" and a new CTO installed (2-Mar-2026) — three of the top finance/technology roles turned over inside twelve months, alongside CEO Sanoke Viswanathan (in the role since 2024) receiving one-time equity awards that are themselves adding to the margin drag.

## 10. Key risks & kill criteria (measurable)
1. Organic ASV growth falls below 5% for two consecutive quarters (vs. 7.1% at 31-May-2026).
2. The IT general controls material weakness, first identified in FY2024, is not remediated (per management's own effective-control conclusion) by the end of FY2026 (31-Aug-2026) — its own stated target.
3. Adjusted operating margin stays below 33% (vs. 34.0% in Q3 FY26, 36.8% a year earlier) for two consecutive quarters.
4. A further unplanned CEO or CFO departure within 12 months of this dossier (on top of the CFO change already seen in Apr-2026).
5. Net debt/EBITDA (consolidated) rises above 2.0x (roughly ~1.1–1.2x currently, using ~$1.09bn net debt against an adjusted-EBITDA run-rate in the ~$900M–$1.0bn range) from debt-funded buybacks or M&A.

## 11. Catalysts & calendar
- Next earnings: Q4/FY2026 and full-year results, not yet formally scheduled in any SEC filing reviewed as of the 25-Sep-2026 cutoff. FY2025's equivalent release was 18-Sep-2025; FY2026's had not occurred as of the cutoff date, so a release in the first half of October 2026 is a reasonable but **unconfirmed estimate**.
- Newly appointed director Marcel Prins joined the Board 23-Sep-2026 (8-K, 25-Sep-2026) — too recent to assess impact; noted for completeness.
- Continued monitoring of the IT general controls remediation program, which management has targeted for completion within FY2026.

## 12. Red-flag scan
- **Material weakness (open):** IT general controls material weakness first identified FY2024, still not remediated as of the Q3 FY26 10-Q; disclosure controls and procedures were concluded **not effective** as of 31-May-2026 (10-Q, Item 4, Controls and Procedures).
- **Leadership turnover:** CFO change (Apr-2026), CTO/Chief AI Officer reorganization (Mar-2026) — both disclosed via 8-K Item 5.02, not the subject of any stated "for cause" language, but concentrated in a short window.
- **Litigation/tax:** Massachusetts sales-tax dispute (2006–2023 periods) fully resolved Nov-2024, ~$66.2M aggregate cost — closed, not open.
- No auditor change, restatement or going-concern language found in the reviewed filings. No pending M&A found.

## 13. Sources
1. FDS 10-Q for the quarter ended 31-May-2026, filed 1-Jul-2026, accession 0001628280-26-046549: https://www.sec.gov/Archives/edgar/data/1013237/000162828026046549/fds-20260531.htm
2. FDS 10-K for FY2025 (ended 31-Aug-2025), filed 22-Oct-2025, accession 0001628280-25-045769: https://www.sec.gov/Archives/edgar/data/1013237/000162828025045769/fds-20250831.htm
3. Earnings releases (Ex-99.1, furnished under 8-K Item 2.02): Q4/FY25 (18-Sep-2025, accession 0001013237-25-000084, fdsq42025earningsrelease.htm); Q1 FY26 (18-Dec-2025, accession 0001628280-25-057794, fdsq12026earningsrelease.htm); Q2 FY26 (31-Mar-2026, accession 0001628280-26-022203, fdsq22026earningsrelease.htm); Q3 FY26 (1-Jul-2026, accession 0001628280-26-046338, fdsq32026earningsrelease.htm).
4. 8-K, Item 5.02 (CFO appointment), 13-Apr-2026 context per Q3 FY26 earnings release; CTO/Chief AI Officer change, 8-K filed 4-Mar-2026, accession 0001628280-26-014385; director appointment 8-K, 25-Sep-2026, accession 0001628280-26-063495.
5. SEC XBRL companyfacts, CIK0001013237: https://data.sec.gov/api/xbrl/companyfacts/CIK0001013237.json; submissions: https://data.sec.gov/submissions/CIK0001013237.json.
6. v4/data/b1_live_scores.csv (row FDS, as_of 2026-09-25); v4/outputs/Q05_triage.json (FDS entry); v4/outputs/v1_valuation_table.csv (no FDS row — confirmed absent).

## 14. Data basis, recency and disclaimer
Most recent period incorporated: 10-Q for the quarter ended **31-May-2026**, filed 1-Jul-2026. Events checked to 2026-09-25 close (plus the 25-Sep-2026 director-appointment 8-K). GAAP figures are labelled as such throughout; "adjusted" figures (operating margin, EPS, EBITDA) are the company's own non-GAAP measures, reconciled in each 10-Q/earnings release and labelled here wherever used. This is research, not personalized investment advice, and not a recommendation to buy or sell any security.
