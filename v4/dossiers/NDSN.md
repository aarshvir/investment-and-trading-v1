# NDSN — Nordson Corporation — Diligence Dossier (Agent F89, STANDARD depth)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Thesis horizon: 12–36 months. Reason: durable, high-margin precision-dispensing compounder with organic growth clearly reaccelerating, but the stock trades at the rich end of its own multiple history with no valuation margin of safety, and leverage stepped up materially after the FY2024 Atrion deal.

## 2. Business in plain English
Nordson makes precision dispensing, adhesive, coating and fluid-management equipment (and the nozzles/consumables that go with it) used to build electronics, medical devices, packaging and industrial products. Roughly half of revenue is recurring parts/consumables and systems tied to existing installed base, which supports high (~55%+ gross) margins and pricing power. It sells through three segments — Industrial Precision Solutions, Medical & Fluid Solutions, Advanced Technology Solutions (electronics) — competing on engineering precision and switching costs rather than price.

## 3. Why the model likes it / is it durable?
Triage flagged reaccelerating growth (10.3% reported) at ~25x NTM P/E with 18.6% margins. Confirmed and stronger in the most recent quarter: Q3 FY26 (Jun–Jul 2026) organic growth ~12%, driven by an electronics-capex recovery in Advanced Technology Solutions. This looks durable (broad-based across all three segments per management commentary, not one customer), not an artefact — but part of the "growth" comp is easy: FY25 growth was soft, so FY26 is partly a recovery off a weak base.

## 4. Last several quarters — results
GAAP, $ thousands unless noted; source: SEC EDGAR 10-Q/10-K XBRL (facts as of each filing date).

| Quarter (FYQ) | Revenue | YoY | Operating income | Op margin | GAAP diluted EPS | Adj. EPS (co. release) |
|---|---|---|---|---|---|---|
| Q4 FY25 (Aug–Oct25, 10-K) | $751.8M* | — | — | — | — | — |
| FY2025 (full yr) | $2,791.7M | ~flat | $711.7M | 25.5% | — | — |
| Q1 FY26 (Nov25–Jan26) | $669.5M | — | $166.4M | 24.9% | — | — |
| Q2 FY26 (Feb–Apr26) | $740.8M | — | $197.2M | 26.6% | — | — |
| Q3 FY26 (May–Jul26) | $817.7M | **+10.3%** vs $741.5M Q3FY25 | $223.1M | 27.3% | $2.73 (+23% YoY) | $3.25 (+19% YoY) |

*Q4 FY25 = FY25 total ($2,791.7M) minus 9-month FY25 ($2,039.9M) = $751.8M.
Nine-month FY26 (Nov25–Jul26): revenue $2,228.0M, net income $403.5M, operating cash flow $570.5M, capex $40.3M → FCF ≈ $530M vs 9-month NI $403.5M, i.e. FCF/NI ≈ 1.3x — strong cash conversion.
Sources: Nordson 10-Q filings (2026-02-19, 2026-05-21, 2026-08-20), 10-K (2025-12-17); Nordson press release "Reports Third Quarter Fiscal 2026 Results and Increases Full Year Guidance" (nordson.com, 2026-08-19); SEC 8-K exhibit ndsn-q320268kxex991.htm.

## 5. Guidance track record
- **Aug 19, 2026 (Q3 FY26 release):** raised full-year FY26 guidance to sales $3,035–3,075M and adjusted EPS $11.80–12.00, citing backlog +35% YoY and continued Q4 momentum. This is a genuine raise (prior FY26 guidance, per the same release series, was lower — company language: "Increases Full Year Guidance"). Verified from the primary release, not a news summary.
- Company gives full-year (not quarterly point) guidance, updated each quarter; three consecutive quarters in FY26 have beaten and guidance has moved up each time (per 10-Q MD&A commentary and the Q3 release headline "Record Third Quarter … Increases Full Year Guidance").

## 6. Earnings quality & balance sheet
- **FCF conversion:** 9-month FY26 FCF/NI ≈ 1.3x (strong; low capex intensity, ~1.8% of revenue).
- **GAAP vs adjusted gap:** Q3 FY26 GAAP EPS $2.73 vs adjusted $3.25 (+19% YoY) — the ~$0.52 gap is mostly acquisition-related intangible amortization from Atrion (2024) and CyberOptics (2022), a real recurring non-cash cost, not a one-off; investors should weight GAAP more than management's framing implies.
- **Balance sheet (consolidated, per 10-Q Q3 FY26, filed 2026-08-20):** long-term debt $1,731.0M, cash $113.4M → net debt ≈ $1,618M. Stockholders' equity $3,269.1M (steadily rising each quarter). TTM operating income ≈ $774M (Q4FY25 est. $178M + 9mo FY26 $586.7M − Q4FY25 est. overlap; approx.) → net debt/EBIT ≈ 2.0–2.1x, moderate and declining (debt fell from $1,996M in Oct25 to $1,731M in Jul26 as the company pays down Atrion-deal debt).
- **Share count:** stable, no material dilution; modest buybacks alongside a $3.76/share annual dividend (~1.0% yield), part of a long dividend-growth streak (Dividend King status referenced in prior coverage — not independently re-verified here).
- **M&A:** no new pending deals found in FY26 filings; the debt step-up in FY2024 (Atrion, ~$800M, closed July 2024) is now the dominant capital-structure event and is being amortized down.

## 7. Valuation — reverse DCF and reconciliation with V1
No NDSN row exists in `v1_valuation_table.csv` / `v1_valuation.json` → **v1_verdict = null**. I therefore built a simplified reverse-DCF myself (Gordon-growth approximation on FCF yield, disclosed as a simplification, not the full 10-year-fade V1 model):
- Price (2026-09-25 close) $325.77; market cap $18.15B; TTM FCF (Yahoo-sourced, cross-check only) ≈ $614M → FCF yield ≈ 3.4%.
- WACC ≈ 8.7% (beta 0.97, rf 5.17%, ERP 4.14% → cost of equity 9.2%; ~9% debt weight at ~5% pretax cost).
- Implied perpetual FCF growth ≈ WACC − FCF yield ≈ **5.3%/yr**.
- Base case (my own, evidence-based): mid-to-high-single-digit organic growth (12% this quarter, but boosted by an electronics-capex upcycle that will normalize) plus modest M&A — **base ≈ 6–7%/yr** over a full cycle.
- **implied_vs_base = "below"** — the market is pricing in less growth (5.3%) than the current trend and consensus (fy1 EPS growth 8.7%, revenue growth 5.2% per D4 consensus) would suggest is achievable, which is why this clears the INCLUDE-SMALL bar rather than being priced for perfection. The reservation is that today's 25–27x NTM/FY0 P/E is well above where a cyclical industrial typically trades, so a growth disappointment (electronics capex rolling over) would compress the multiple even if the DCF math still "works."

## 8. Bull / Bear
**Bull:** (1) electronics-capex upcycle continues, ATS segment keeps compounding double digits; (2) Atrion/medical cross-sell drives Medical & Fluid Solutions margin expansion; (3) further bolt-on M&A funded by fast debt paydown (net debt/EBIT already improving).
**Bear:** (1) ATS growth is cyclical — electronics capex has historically been lumpy, and today's 12% organic growth could revert; (2) 25x+ NTM P/E leaves no room for a miss; (3) further debt-funded M&A could re-lever the balance sheet before the Atrion deal is fully paid down.

## 9. Key risks & measurable kill criteria
1. Organic revenue growth <3% for two consecutive quarters (signals the electronics upcycle has rolled over).
2. Consolidated net debt/EBIT (per the 10-Q cash-flow/balance-sheet tables) rises back above 3.0x.
3. Full-year guidance is cut (vs. the raised Aug-2026 range of $3,035–3,075M sales / $11.80–12.00 adjusted EPS).
4. FCF/NI conversion falls below 0.8x for two consecutive quarters (earnings-quality deterioration).
5. A debt-funded acquisition >$500M is announced before net debt/EBIT falls below 1.5x.

## 10. Catalysts & calendar
Next scheduled earnings: Q4/FY26 results, expected early December 2026 (fiscal year ends Oct 31; FY25 release was 2025-12-10). No investor day identified in filings reviewed.

## 11. Red-flag scan
No auditor change, no restatement, no material weakness, no SEC/DOJ investigation, no going-concern language found in the 10-K (FY2025, filed 2025-12-17) or the three FY26 10-Qs reviewed. No short-seller report identified in this pass. Insider holding ~5.6% (Yahoo-sourced, cross-check only); no unusual Form 4 cluster identified within the time box — this is a limitation, not a clean bill, given the standard (not deep) depth of this pass.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q3 FY2026 10-Q (period ended 2026-07-31, filed 2026-08-20) and the Aug 19, 2026 earnings/guidance release. Checked for events to 2026-09-25 (no subsequent 8-K items found beyond routine items). GAAP figures are labelled GAAP; adjusted EPS is labelled and sourced to the company's own release, not restated by me. This report is research, not personal investment advice.

## 13. Sources
1. Nordson 10-K, FY2025 (filed 2025-12-17): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000072331
2. Nordson 10-Q, Q1 FY26 (filed 2026-02-19), Q2 FY26 (filed 2026-05-21), Q3 FY26 (filed 2026-08-20) — SEC EDGAR CIK 0000072331.
3. SEC XBRL companyfacts, CIK 0000072331, retrieved 2026-09-27 (data.sec.gov/api/xbrl/companyfacts).
4. Nordson press release, "Nordson Corporation Reports Third Quarter Fiscal 2026 Results and Increases Full Year Guidance," 2026-08-19, nordson.com/en/About-Us/Newsroom.
5. v4/data/d4_live_snapshot.parquet (consensus/price cross-check, retrieved for as-of 2026-09-25).
6. v4/outputs/Q10_triage.json (prior triage note for NDSN).
