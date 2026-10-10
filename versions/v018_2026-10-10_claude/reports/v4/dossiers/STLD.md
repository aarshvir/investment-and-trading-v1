# Steel Dynamics, Inc. (NASDAQ: STLD) — Fundamental Diligence Dossier

**Prepared by:** F48 (fundamental diligence analyst, wave 2) | **Data cutoff:** 2026-09-25 close | **Most recent period incorporated:** Q2 2026 10-Q (filed 2026-07-28, period ended 2026-06-30); Q3 2026 earnings-guidance 8-K (filed 2026-09-18, dated 2026-09-17) also incorporated. Checked for events to 2026-09-25. Next scheduled report: ~2026-10-19/20 (Q3 2026 results, based on the FY2025 Oct-20 cadence). **Basis:** consolidated GAAP unless labeled otherwise; STLD reports essentially no non-GAAP adjustments to EPS in its releases (Adjusted EBITDA is the main non-GAAP measure used, and is labeled at every use). **Scorecard gates:** not applicable — this dossier does not use a disqualifying-gate checklist; the quant composite cited in §3 is context, not a pass/fail gate.

**Data-quality note:** every figure is sourced to SEC EDGAR primary filings (10-Q/10-K, 8-K Ex-99.1 earnings/guidance releases) or SEC XBRL company facts (`data.sec.gov/api/xbrl/companyfacts`, a machine-readable copy of the same filings), each cited in §12. Quant context (composite score, factor percentiles) is from `v4/data/b1_live_scores.csv`; own-history/peer valuation context is from `v4/outputs/v1_valuation.json` and `v1_valuation_table.csv`. No number is estimated, interpolated, or recalled from training-data memory without being labeled. Research output for internal process use, not personalized investment advice.

## 1. Verdict: WATCH — thesis horizon: re-assess after a multiple reset or a full-cycle guidance test (12–24 months)
Steel Dynamics is a genuinely well-run, low-cost electric-arc-furnace steelmaker with a credible new growth leg (aluminum flat-rolled) and an excellent record of beating its own quarterly guidance, but the current 12.3x NTM P/E is being earned on an EPS run-rate ($2.78 → $3.69 → guided $5.34–5.38 over the last three quarters) that is inflated by tariff-protected steel pricing and record shipments — and the company's own analyst consensus expects revenue growth of only **0.4%** next fiscal year (V1 `consensus_fy1_growth`), i.e., the Street itself does not expect this run-rate to keep accelerating. V1's reverse-DCF shows the price implies **14.4%** 10-year revenue growth against a **9.7%** delivered 5-year and **10.9%** delivered 10-year CAGR — the market is paying for continuation of a cyclical peak, not for what STLD has historically compounded at. This is a "great business, priced for more than its own base rate" case, not a broken one: **not now**, re-open on a multiple reset to a mid-cycle earnings basis or evidence the tariff-supported pricing survives a full cycle.

## 2. Business in plain English
Steel Dynamics operates low-cost electric-arc-furnace (EAF) steel mills (flat-rolled and long-product/structural steel), a metals-recycling (scrap) business that supplies its own mills, a steel-fabrication business (joist/deck for non-residential construction), and — as of 2025–26 — a new aluminum flat-rolled products platform (a new mill in Columbus, Mississippi, still ramping). It sells mainly to non-residential construction, automotive, energy, industrial and (for aluminum) beverage-can/industrial/automotive customers. It makes money on the spread between steel selling prices and input costs (scrap, energy), and its competitive position rests on being one of the lowest-cost EAF operators in North America, vertically integrated into its own scrap supply, with domestic-trade-policy (Section 232-style tariff) protection currently supporting US steel pricing versus imports.

## 3. Why the model likes it — durable or artefact?
Quant snapshot (`b1_live_scores.csv`, as of 2026-09-25): composite 0.904 (decile 10, live_rank 48/503, not in live_top30). Family scores: Q 0.436, V 0.551, M 0.854, S 0.896 (sector-relative percentiles). ROE 17.1%, gross-profit/assets 17.6%, earnings yield 4.8%, FCF/price 2.9%, 12-1 month momentum +68.2%, SUE (earnings-surprise) 1.26 (very high — consistent with the guide-beat pattern in §5).
- **Momentum and earnings-surprise (M, S) are real and primary-source-confirmed**, not an artefact: STLD beat its own quarterly EPS guidance in every one of the last three verifiable quarters (§5), and the sequential EPS trajectory (Q1'26 $2.78 → Q2'26 $3.69 → Q3'26 guided $5.34–5.38) is a genuine, filed-and-guided acceleration, not a one-off.
- **Value (V, 55th percentile) is where the "cheap" read breaks down on closer inspection.** The 12.3x NTM P/E triage/b1 cite as "cheap for the trajectory" is priced off an NTM EPS run-rate (V1 input: $18.96) that annualizes the current cyclically-elevated quarter, not a mid-cycle level. V1's own reverse-DCF flags this precisely: the price implies **14.4%** 10-year revenue growth vs **9.7%/10.9%** delivered 5y/10y CAGRs and just **0.4%** consensus FY1 growth — a large gap between what the price assumes and what the business has actually compounded at, or is expected to grow at, next year. FCF yield is low (TTM 0.7% per V1; 2.6% on an SBC-adjusted basis) because the aluminum build-out is consuming heavy capex even as earnings rise — earnings quality (cash conversion) is currently weaker than the EPS headline suggests.
- **Quality (Q, 44th percentile)** is unremarkable on the model's own metrics (leverage, accruals, asset growth) — consistent with a business mid-way through a large capex cycle (Columbus, MS aluminum mill), not with the "record shipments, record profitability" framing alone.

## 4. Last 8 quarters (GAAP; primary-sourced to Ex-99.1 earnings releases, §12 #2–#7)
| Quarter | Net sales ($B) | Net income ($M) | Diluted EPS | Adj. EBITDA ($M) | OCF ($M) |
|---|---|---|---|---|---|
| Q3 2025 | 4.8 | 404 | $2.74 | 664 | 723 |
| Q4 2025 | 4.4 | 266 | $1.82 | n/a (not sourced this pass) | n/a |
| FY2025 | 18.2 | 1,200 | — | 2,200 | 1,400 |
| Q1 2026 | 5.2 | 403 | $2.78 | 700 | 148¹ |
| Q2 2026 | 6.1 | 534 | $3.69 | 921 | 428 |
| Q3 2026 (guided, not yet reported) | — | — | **$5.34–5.38** | — | — |

¹ Q1 2026 OCF was reduced by the annual companywide $120m retirement profit-sharing distribution (company's own MD&A) — a recurring seasonal item, not a one-off deterioration.

**Sequential trend and the peak-earnings question:** Q2 2026 net income (+33% sequentially over Q1) and the guided Q3 2026 EPS (+45–46% sequentially over Q2's $3.69) reflect, per the company's own guidance commentary, "metal margin expansion across the platform and record shipments," "average realized steel selling values… increase in combination with lower scrap costs," and continued ramp of the new aluminum mill. Every driver cited is a **pricing/margin and ramp-up** story, not a volume-only one — meaning the earnings level is more exposed to a pricing reversal (tariff policy or scrap-cost normalization) than a pure volume growth story would be. Only two quarters back (Q4 2025), sequential EPS fell from $2.74 to $1.82 (−34%) on "lower average realized selling values and lower volumes" — direct primary-source evidence that this business can and does swing materially quarter to quarter.

## 5. Guidance track record (last four dated guidance-to-actual pairs; both numbers quoted every time)
| Guidance date | Guided EPS | Actual EPS (release date) | Result |
|---|---|---|---|
| 2025-09-15 (Q3'25 guide) | $2.60–$2.64 | **$2.74** (2025-10-20) | **Beat** (above high end by $0.10) |
| 2025-12-17 (Q4'25 guide) | $1.65–$1.69 | **$1.82** (2026-01-26) | **Beat** (above high end by $0.13) |
| 2026-06-17 (Q2'26 guide) | $3.51–$3.55 | **$3.69** (2026-07-20, incl. a $16m one-off Arizona-to-Columbus relocation impairment; ex-impairment ~$3.80) | **Beat** (above high end by $0.14–0.25) |
| 2026-09-17 (Q3'26 guide, pending) | **$5.34–$5.38** | not yet reported (due ~2026-10-19/20) | pending |

STLD does not appear to issue a mid-quarter guidance update ahead of its Q1 release (only Q2–Q4 have a preceding guide in the window reviewed) — flagged as a gap in this pass rather than a missing data point. **Every guided quarter in this sample beat its own range**, consistently by $0.10–0.25/share — a genuinely strong execution record, distinct from (and a real mitigant to) the valuation concern in §3/§7.

## 6. Earnings quality & balance sheet
- **Cash conversion is the weak link relative to the EPS headline.** TTM FCF (OCF − capex) is $955.6m against TTM net income of $1,607m (V1 inputs) — FCF/NI ≈ 59%, and TTM FCF yield on EV is just 0.7% (V1), because TTM capex ($616m) and the aluminum ramp are consuming most of operating cash flow. This is a genuine, primary-source-verified gap between "record profitability" (income-statement framing used in every release) and free cash actually available to shareholders today.
- **SBC is immaterial to dilution:** ~$14m/quarter (Q2 2026) on $6.1bn quarterly revenue ≈ 0.23% of revenue.
- **Share count and capital return:** weighted-average diluted shares fell from 148.96m (Q2 2025) to 144.59m (Q2 2026), a ~3.0% reduction in four quarters, funded by $200m of Q2 2026 buybacks alone (plus $901m FY2025, "over 4% of shares outstanding"). Dividend raised 6% in Q1 2026. This is real, consistent capital return, not a one-off.
- **Balance sheet:** long-term debt ~$4.20bn flat since FY2025; cash fell from $769.9m (FY2025) to $567.7m (Q2 2026) as capex ramped; net debt ≈ $3.63bn, matching V1's independently-sourced input exactly (cross-check passed). Stockholders' equity grew from $8.96bn (FY2025) to $9.42bn (Q2 2026) despite the buybacks, i.e., retained earnings are outrunning capital return — a healthy sign.
- **Net debt/EBITDA:** using FY2025 Adjusted EBITDA ($2.2bn) and Q2'26 net debt ($3.63bn) ≈ **1.65x** — comfortably low leverage, a real strength.
- **M&A / capex:** the Columbus, Mississippi aluminum flat-rolled mill is the single largest capital program under way; as of the Sep-2026 guidance release, "all three cold mills are now operational" and the first of two Continuous Annealing and Solution Heat (CASH) lines is running, with the second expected in 2027 — a multi-year commissioning risk that is not yet fully resolved. **[Corrected 2026-10-08: the 17 Sep 2026 release says the second CASH line is expected to begin producing material for customer qualification before the end of 2026 (first line ships commercial material in Q4 2026); 2027 is the ramp year, not the start]**
- **Governance — a material, primary-source item not in the triage note:** on 2026-08-04, the board announced that co-founder and long-tenured CEO **Mark D. Millett will retire as CEO and become Executive Chairman effective 1 January 2027**, with CFO **Theresa E. Wagler** (28-year company veteran, CFO since 2007) becoming President & CEO, and Treasurer Richard Poinsatte succeeding her as CFO. This is an orderly, long-planned internal succession (not a forced departure), but it is a leadership-continuity item worth tracking given Millett co-founded the company over 30 years ago and personally narrates every earnings release reviewed in this pass.

## 7. Valuation snapshot and reconciliation with V1
**V1 verdict: "excessive"** (score −0.41, the worst tier), using metric NTM P/E 12.32x (41st percentile of ~14 years' own history — i.e., mid-range, not statistically cheap on a percentile basis despite looking low in absolute terms), peer median 12.47x (peer set: STLD vs NUE only, n=2 — a thin peer sample, flagged), and a reverse-DCF (FCFF, 9.19% WACC) showing the **EV0 of $37.4bn implies 14.4% 10-year revenue growth**, against **9.7%/10.9%** delivered 5y/10y CAGR and just **0.4%** consensus FY1 growth. V1's three scenario paths: **bear −54.3%/yr, base −9.7%/yr, bull +52.7%/yr** (3-year annualized) — a base case that is *negative*, and a street-flag noting "base 3y value below Street 12m low target" ($221 low vs V1's base-case $172 exit value on a 3-year view before dividends of $166, plus $6.14 cumulative dividends = $172.08). **This dossier agrees with V1's "excessive" call.** The mechanism (peak-cycle EPS being extrapolated into a 10-year DCF, and the multiple looking cheap only relative to itself, not to a normalized earnings level) is exactly what §3–§5 above independently document from the primary-source guidance and results: real near-term execution strength, but a price that requires the current tariff-supported pricing/margin level to persist far longer than STLD's own 5–10 year track record or the Street's own next-FY estimate would suggest. **Consistent: true.** Dossier view: **expensive**.

**3-year annualised scenario returns (adopted from V1's reverse-DCF, price+dividends):** bear **−54.3%/yr**, base **−9.7%/yr**, bull **+52.7%/yr**.

## 8. Bull case and bear case
**Bull (3 points):**
1. Guidance-beat discipline: three consecutive quarters beaten by $0.10–0.25/share, and Q3 2026 guidance ($5.34–5.38) implies a further ~45% sequential EPS jump if delivered — the earnings momentum is real and filed, not promotional.
2. Aluminum diversification (Columbus, MS) is a genuine new profit pool with automotive/beverage-can qualifications already secured, reducing pure-play steel-cycle exposure over time, funded from internal cash flow without balance-sheet strain (net debt/EBITDA ~1.65x).
3. Low leverage and consistent capital return (buybacks + 6% dividend increase) give the balance sheet real flexibility to weather a steel-price downturn without cutting the dividend.

**Bear (3 points):**
1. Consensus itself models only 0.4% revenue growth next FY (V1) — the Street does not expect the current pricing tailwind to compound further, directly contradicting the "cheap relative to growth" framing in the triage note.
2. Tariff-dependent pricing (flagged by triage) is a trade-policy variable, not a structural moat; V1's bear scenario (−10.8% revenue growth, margin compressing to 2.3%, implying a −54%/yr 3-year return) shows how violently this business can reprice if scrap costs rise or import protection is rolled back.
3. TTM free-cash-flow yield of just 0.7–2.6% (SBC-adjusted) means the "record profitability" is not yet translating into distributable cash at a rate that supports the current EV, while the aluminum ramp still carries multi-year commissioning risk (second CASH line not expected until 2027).

## 9. Key risks & kill criteria (measurable)
1. Quarterly diluted EPS falls below the Q1 2026 level ($2.78) for two consecutive quarters without a one-off explanation — signals the cyclical peak has passed without a corresponding valuation reset.
2. Section 232/import-tariff protection on steel is materially reduced or removed (the specific trade-policy risk both triage and V1's bear case flag).
3. Net debt/EBITDA rises above 2.5x (from ~1.65x now) as aluminum capex continues.
4. The Columbus, MS aluminum platform fails to reach management's own stated qualification/ramp milestones (e.g., second CASH line not operating by end-2027) after $3bn+ invested. **[Corrected 2026-10-08: milestone anchor corrected: second CASH line producing qualification material by end-2026 per the company; a miss would be visible a year earlier than this criterion implies]**
5. FY2027 guidance (first given under new CEO Theresa Wagler, effective 1 Jan 2027) shows a step-down in capital-return pace (buybacks or dividend growth) versus the FY2025–26 run-rate.

## 10. Catalysts & calendar
- Next earnings: **~2026-10-19/20** (Q3 2026 results against the $5.34–$5.38 guide; estimated from the FY2025 Oct-20 reporting date, not yet confirmed by the company).
- CEO/CFO transition effective **2027-01-01** (Wagler CEO, Poinsatte CFO, Millett to Executive Chairman).
- Second Columbus, MS aluminum CASH line commissioning target: **2027**. **[Corrected 2026-10-08: company target is to begin producing customer-qualification material before the end of 2026]**
- Typical mid-quarter guidance pre-announcement pattern (mid-Dec for Q4, mid-Mar/Apr for Q1 results, mid-Jun for Q2, mid-Sep for Q3) — next expected mid-December 2026 for Q4 2026 guidance.

## 11. Red-flag scan
No auditor changes, material weaknesses, restatements, SEC/DOJ investigation, or going-concern language identified in the sections reviewed (Q2 2026 10-Q, FY2025 10-K highlights, and the six Ex-99.1 releases sourced in §12). No short-seller report identified in this pass (not exhaustively searched — disclosed limitation). Insider Form 4 pattern **not independently checked this pass** — disclosed gap; the CEO/CFO succession (§6) is a governance item to monitor but is disclosed as planned, not adverse. Litigation: none identified as individually material in the sections reviewed; a fuller Item 3/Note-level legal-proceedings read was not completed in the time box (disclosed limitation).

## 12. Sources
1. SEC EDGAR — Steel Dynamics Inc, CIK 0001022671: submissions JSON (`data.sec.gov/submissions/CIK0001022671.json`) and companyfacts JSON (`data.sec.gov/api/xbrl/companyfacts/CIK0001022671.json`), retrieved 2026-09-26.
2. 8-K Ex-99.1, "Steel Dynamics Reports Third Quarter 2025 Results," filed 2025-10-21 (dated 2025-10-20). `sec.gov/Archives/edgar/data/1022671/000110465925101080/tm2529138d1_ex99-1.htm`
3. 8-K Ex-99.1, "Steel Dynamics Reports Fourth Quarter and Annual 2025 Results," filed 2026-01-27 (dated 2026-01-26). `sec.gov/Archives/edgar/data/1022671/000110465926006889/tm264071d1_ex99-1.htm`
4. 8-K Ex-99.1, "Steel Dynamics Reports First Quarter 2026 Results," filed 2026-04-27 (dated 2026-04-20). `sec.gov/Archives/edgar/data/1022671/000110465926045938/tm2612296d1_ex99-1.htm`
5. 8-K Ex-99.1, "Steel Dynamics Reports Second Quarter 2026 Results," filed 2026-07-21 (dated 2026-07-20). `sec.gov/Archives/edgar/data/1022671/000110465926085277/tm2620920d1_ex99-1.htm`
6. 8-K Ex-99.1 guidance releases: Q3'25 (2025-09-15), Q4'25 (2025-12-17), Q2'26 (2026-06-17), Q3'26 (2026-09-17, filed 2026-09-18). `sec.gov/Archives/edgar/data/1022671/000110465925090047/`, `.../000110465925121880/`, `.../000110465926075470/`, `.../000110465926108777/tm2625690d1_ex99-1.htm`
7. 8-K Ex-99.1, "Theresa E. Wagler to become… President and CEO," filed 2026-08-04. `sec.gov/Archives/edgar/data/1022671/000110465926090129/tm2622182d1_ex99-1.htm`
8. `v4/outputs/v1_valuation.json` and `v1_valuation_table.csv` (STLD row, as_of 2026-09-25); `v4/data/b1_live_scores.csv`; `v4/outputs/Q13_triage.json`.

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q, period ended 2026-06-30, filed 2026-07-28; Q3 2026 guidance 8-K dated 2026-09-17. Checked for events to 2026-09-25 (no new material 8-K identified between 2026-09-18 and 2026-09-25). GAAP vs adjusted: all results above are GAAP as reported; Adjusted EBITDA is STLD's own defined non-GAAP measure and is labeled as such at every use. Research, not personal investment advice.

## Correction (verification DV38, 2026-10-08)

**Verifier:** DV38. **Source:** 8-K Ex-99.1 acc 0001104659-26-108777 (Q3-26 guidance release, 17 Sep 2026): "All three cold mills are now operational, and the first of two ... CASH lines is operating and is expected to ship commercial material in the fourth quarter. The second CASH line is expected to begin producing material for customer qualification before the end of the year."

**1. Second CASH line timing (FAIL).** Wrong text: second CASH line "expected in 2027" (s6), "second CASH line not operating by end-2027" (kill criterion 4) and catalyst "2027" (s10). Correct: second line expected to begin producing qualification material before the end of 2026. Effect: the kill criterion is looser than the company's own commitment; the F48 summary kill criterion 4 was reworded to the end-2026 anchor (no other summary field changed). **Verdict unchanged (WATCH); implied_vs_base unchanged (above).**

**2. Minor.** Net debt on balance-sheet lines is $3,614m (LTD 4,180.8 + current 1.3 - cash 567.7); $3.63bn is V1's definition. Net debt/EBITDA of 1.65x uses FY2025 Adjusted EBITDA ($2.2bn); on TTM Adjusted EBITDA it is nearer 1.3x. Neither changes any conclusion.

**Verified without change:** Q2-26 sales $6.1bn / NI $534m / EPS $3.69 / Adj EBITDA $921m / OCF $428m; Q1-26 and Q3/Q4-25 rows; guidance ranges for Q3-25, Q4-25, Q2-26, Q3-26; TTM FCF $955.6m (OCF 1,571.6 - capex 616.0); the crosstie flag (TTM NI 1,607 vs XBRL 534) is a four-quarter sum; V1 inputs (rf 5.17%, WACC 9.19%, FCFF with SBC as a cost).
