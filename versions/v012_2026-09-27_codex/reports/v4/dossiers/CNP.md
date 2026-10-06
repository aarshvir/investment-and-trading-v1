# CenterPoint Energy, Inc. (CNP) — Diligence Dossier

**Agent:** F109 (wave 7) | **As of:** 2026-09-25 close ($36.84, mkt cap $24.10bn per d4/b1 snapshot) | **CIK 0001130310**

## 1. Verdict
**INCLUDE-SMALL** (half weight), thesis horizon 24–36 months. Reason: a rate-regulated T&D utility with unusually strong, regulator-blessed load growth (Houston Electric) is priced for less growth than management's own long-range guidance implies, but elevated consolidated leverage and a lumpy near-term debt/refinancing calendar are a specific, named reservation that keeps this from full weight.

## 2. Business in plain English
CenterPoint Energy is a regulated electric transmission & distribution (T&D) and natural-gas distribution utility holding company. Its main earner is **CenterPoint Energy Houston Electric, LLC** (a wholly owned subsidiary, "Houston Electric"), which delivers (does not generate) electricity to ~2.9m metered customers in the Houston metro area under ERCOT; it also owns natural-gas LDCs in Indiana, Minnesota, and other states. It earns a regulator-approved return on a growing "rate base" (capital invested in wires, poles, pipes) — revenue and profit grow mainly by investing capital and getting it into rates, not by selling more volume at a margin.

## 3. Why the model likes it — durable or artefact?
b1_live_scores.csv: composite decile 5 / quintile 3, live_rank 268 (mid-pack, not a top-30 name), Quality family percentile ~0.45 (roe pct 0.34, ocf/assets pct 0.15 — modest), Value family higher (fcfp pct 0.79, ep pct 0.66) — the model likes it mostly on *cheapness* (low forward multiple, high nominal FCF-yield metric) more than on quality; the fcfp (FCF/price) percentile is high because reported operating cash flow is being compared against a market cap depressed by scale, but note the underlying FCF is deeply negative once capex is netted (see §6) — the model's "value" signal here is partly an artefact of how FCF-yield is computed pre-capex-netting for a heavy-capex utility, not a signal of cash-generative cheapness. The durable part of the bull case is the **rate case pipeline**: Houston Electric's capital plan is filed and largely pre-approved through settlements, which is a real, verifiable growth driver independent of the model's factor scores.

## 4. Last several quarters (consolidated, GAAP, USD millions; SEC XBRL via companyfacts, cross-checked against 8-K press releases)
| Period | Revenue | Op. income | Net income | Non-GAAP EPS (co. reported) |
|---|---|---|---|---|
| Q3 2024 | 1,856 | 424 | 193 | n/a (not re-derived) |
| Q4 2024 (10-K minus 9-mo) | 2,262 | 483 | 248 | — |
| FY2024 | 8,643 | 1,990 | 1,019 | — |
| Q1 2025 | (in 9-mo 4,864 less Q2 below) | — | 297* | — |
| Q2 2025 | 1,944 | 417 | 198 | — |
| Q3 2025 | 1,988 | 502 | 293 | — |
| FY2025 | 9,357 | 2,110 | 1,052 | delivered within the FY2025 non-GAAP EPS range the company had communicated (see §5 for verbatim FY2026 guidance) |
| Q1 2026 | 2,975 | 658 | 316 | — |
| Q2 2026 | ~2,110 (co. release) | — | ~$0.37 GAAP EPS | **$0.40 non-GAAP EPS** |

*Q1 2025 net income of $297m is the 10-Q line item filed 2026-04-23 (accession 0001130310-26-000028) — labelled here as prior-year comparative, not current-year Q1 2026.
Source: SEC XBRL companyfacts CIK0001130310 (`NetIncomeLoss`, `OperatingIncomeLoss`, `Revenues` tags, consolidated, all forms 10-Q/10-K, accessions as filed); Q2 2026 figures from the 8-K exhibit (SEC EDGAR, https://www.sec.gov/Archives/edgar/data/1130310/000110465926087279/tm2621002d1_ex99-1.htm, filed ~2026-07-28).
**Trend:** revenue and operating income both stepped up in 2025 vs 2024 and continued into Q1 2026 ($658m operating income vs $649m Q1 2025 restated basis), consistent with rate-base growth; no deceleration visible in the two years of consolidated data reviewed.

## 5. Guidance track record (verbatim quotes, most recent four releases)
- **Q2 2026 (8-K, filed ~2026-07-28):** "reiterates its 2026 non-GAAP EPS guidance range of at least the midpoint of $1.89-$1.91" — **maintained**, not raised (verbatim per company release, accession referenced above).
- **Same release:** 10-year capital plan raised "to $66.7 billion from $65.5 billion," i.e., **capital plan raised** even while EPS guidance for the current year was held.
- **Q4 2025 release (Investing.com/company summary of the 8-K, "CenterPoint Energy Q4 2025 slides"):** long-term non-GAAP EPS growth guidance increased to "the mid-to-high end of 7%-9%" for 2026-2028 and "7%-9% thereafter through 2035," up from the prior "6% to 8%" long-range target — **long-range guidance raised**.
- The two verbatim quotes above ("reiterates its 2026 non-GAAP EPS guidance range of at least the midpoint of $1.89-$1.91"; "the mid-to-high end of 7%-9%... through 2035") are the company's only two numeric guidance ranges identified; it does not give explicit multi-year FCF guidance (capex-heavy utilities structurally run negative FCF while building rate base — see §6).

## 6. Earnings quality & balance sheet
**Entity scope:** all figures below are **consolidated CenterPoint Energy, Inc.** unless labelled otherwise. Houston Electric (the regulated T&D subsidiary) issues its own debt and has separate credit ratings from the parent holding company; this dossier does not have Houston Electric's stand-alone balance sheet and states so as a limitation.
- **FCF (consolidated):** H1 2025 OCF $970m − capex $2,167m = **−$1,197m** FCF (10-Q, filed 2025-07-24, accession 0001130310-25-000113); 9-mo 2025 OCF $1,712m − capex $3,389m = **−$1,677m** FCF (10-Q filed 2025-10-23). This is structural, not a red flag by itself for a utility mid-buildout — capex is largely recovered later through the rate base — but it means CNP funds growth with debt/equity issuance, and the model's fcfp signal (§3) is misleading if read as "cash-rich."
- **SBC:** not separately quantified in the sources reviewed within the time box; flagged as a data gap, not zero.
- **Leverage (consolidated, from 10-Q/10-K XBRL, as filed):** Assets grew from $43,768m (2024-12-31, 10-K, accession 0001130310-26-000008) to $47,837m (2026-03-31, 10-Q, accession 0001130310-26-000028); consolidated `LongTermDebtNoncurrent` rose from $20,397m (2024-12-31, same 10-K) to $22,476m (2026-03-31, same 10-Q); `StockholdersEquity` $10,666m → $11,449m over the same span. Debt/equity on this XBRL slice ≈ 1.96x at 2026-03-31, consistent with a market-reported "debt/equity ratio of 1.95" for the three months ended 2026-06-30 (source: web search summary of company/Macrotrends-style data, not independently re-derived from XBRL for Q2 — **labelled as a secondary-source figure**, cross-check only).
- **Credit metrics (consolidated, company-reported, secondary-source aggregation, not independently re-derived):** FFO/debt ~13.0–13.4% (S&P/Moody's-style methodology) for the trailing twelve months to Q2 2026, and net debt/EBITDA reported around 5.5x as of Q1 2026 — both above what rating agencies typically want for a "strong" investment-grade T&D utility (commonly cited threshold ~15% FFO/debt); this matches the triage's leverage red flag and is **not resolved favourably** by the two-year filing history reviewed — leverage has risen, not fallen, alongside the accelerating capital plan.
- **Debt maturity wall:** a **$1.0bn 4.25% Convertible Senior Notes due 2026** (per the 2023 8-K, accession 0001193125-23-203904: matured/convertible from 15 May 2026, final maturity 15 Aug 2026, initial conversion price ≈$36.86/share) was outstanding entering 2026; the sources reviewed in this diligence window did not surface a confirmed settlement method (cash, shares, or refinancing) for this specific tranche as of the Sept-2026 cutoff — **this is an open data gap, disclosed rather than assumed**, and should be checked against the Q3 2026 10-Q debt footnote before any position is sized. Separately, the company issued $2.64bn of new debt (including $650m of 2.875% convertible notes due 2029) in February 2026, consistent with continuing to term out near-term maturities.
- **Share count / buybacks:** not separately verified in this window; no evidence found of a buyback program (capex-heavy growth utilities typically do not repurchase stock).
- **M&A:** none identified as pending for CNP itself in the sources reviewed.

## 7. Valuation snapshot
NTM P/E ≈ $36.84 / $1.90 (2026 non-GAAP EPS midpoint, from the §5 quote "reiterates its 2026 non-GAAP EPS guidance range of at least the midpoint of $1.89-$1.91") ≈ **19.4x**. No V1 systematic valuation row exists for CNP (`outputs/v1_valuation_table.csv` has no CNP line) — `v1_verdict` is therefore **null**, per the wave-7 prompt's instruction.
**Reverse dividend/earnings-growth model (utility-appropriate; a levered FCF DCF is not meaningful here per §6):** using a simplified Gordon-growth framing, P = D₁/(r−g) with an assumed payout ratio of ~45% of the $1.90 EPS midpoint (D₁≈$0.855) and an assumed cost of equity r≈8.5% (typical regulated-utility CAPM range), the price of $36.84 implies r−g ≈ D₁/P ≈ 2.32%, i.e. an **implied long-run EPS/dividend growth rate of roughly 6.2%/yr**. Management's own long-range target (§5 verbatim quote: "the mid-to-high end of 7%-9%... through 2035") is higher. The price therefore appears to discount **less** growth than the company is targeting — i.e., **implied growth is below the evidence-based base case**, which is the necessary condition for INCLUDE/INCLUDE-SMALL under the wave-7 rule. This reverse model is a simplification (single-stage Gordon growth, assumed payout and cost of equity not independently verified against CNP's actual dividend policy in this diligence window) and should be treated as indicative, not precise.

## 8. Bull case / Bear case
**Bull:**
1. Houston Electric's Batch Zero ERCOT interconnection queue shows ~17 GW of large-load requests, ~14 GW expected to qualify, against a current system peak of ~21 GW — a potential ~65%+ demand increase with energization targeted by 2031 (company Q2 2026 release), a scale of contracted/queued demand growth rare among regulated T&D utilities.
2. The 10-year capital plan was raised again in Q2 2026 (to $66.7bn from $65.5bn, per §5), and the long-range EPS-growth target was raised to "the mid-to-high end of 7%-9%" (§5 verbatim quote) — management is executing, not just promising.
3. The 2025 Houston storm-resiliency settlement (referenced in the Q15 triage sources) removed a major regulatory/reputational overhang from the 2024 Hurricane Beryl outages.

**Bear:**
1. Consolidated leverage (FFO/debt ~13%, net debt/EBITDA ~5.5x) is elevated for the utility sector and has been rising alongside the capital plan, not falling; a credit-rating action would raise financing costs for the entire growth story.
2. Structurally negative FCF means the equity story depends on continued capital-markets access on reasonable terms; a $1bn convertible tranche's settlement (§6) is an unresolved open item this diligence window could not close out.
3. The bull case (17 GW of queued load) is a pipeline of *requests*, not signed, rate-approved contracts; large-load interconnection queues across ERCOT have historically seen significant attrition between "submitted" and "energized."

## 9. Key risks & kill criteria (measurable)
1. Consolidated net debt/EBITDA rises above **6.5x** for two consecutive quarters (vs. ~5.5x now).
2. FFO/debt falls below **11%** (vs. ~13% now) on a trailing-twelve-month basis, per company or rating-agency-reported figures.
3. Full-year non-GAAP EPS guidance is **cut** from the current "$1.89-$1.91" range quoted in §5 (any downward revision, not just a miss).
4. The 4.25% convertible notes due 2026 are confirmed to have required a distressed or unfavourable refinancing (materially above the ~2.9% coupon on the 2029 tranche priced in Feb 2026).
5. ERCOT Batch Zero "qualified" large-load capacity (currently ~14 GW) falls by more than 30% in a subsequent quarterly update, signalling the demand pipeline is not converting.

## 10. Catalysts & calendar
- Next earnings: Q3 2026 results expected late October 2026 (2025's Q3 report was filed 2025-10-23; **this is an estimate, not a confirmed date**).
- Ongoing: ERCOT large-load interconnection process updates; any rate-case filings/settlements in Texas, Indiana or Minnesota; convertible-note maturity resolution.

## 11. Red-flag scan
- No auditor changes, material weaknesses, restatements, going-concern language, SEC/DOJ investigations, or short-seller reports identified in the sources reviewed.
- No Form 4 insider-selling pattern independently reviewed in this window (data gap, disclosed).
- Litigation: none material identified beyond the (now largely settled per triage sources) 2024 Hurricane Beryl storm-response scrutiny.

## 12. Sources
1. SEC EDGAR XBRL companyfacts, CIK0001130310 (`https://data.sec.gov/api/xbrl/companyfacts/CIK0001130310.json`), retrieved 2026-09-27.
2. SEC EDGAR submissions, CIK0001130310 (`https://data.sec.gov/submissions/CIK0001130310.json`), retrieved 2026-09-27.
3. CenterPoint Energy Q2 2026 8-K earnings exhibit, https://www.sec.gov/Archives/edgar/data/1130310/000110465926087279/tm2621002d1_ex99-1.htm.
4. Investing.com, "CenterPoint Q2 2026 slides: demand surge drives capital plan boost," accessed 2026-09-27 (secondary source, cross-check only).
5. CenterPoint Energy Announces Record 10-Year Plan / Q4 2025 guidance release (via investors.centerpointenergy.com news-releases index and Investing.com summary), accessed 2026-09-27.
6. CenterPoint Energy 4.25% Convertible Senior Notes Due 2026 pricing release, investors.centerpointenergy.com, and 2023 8-K, https://www.sec.gov/Archives/edgar/data/1130310/000119312523203904/d536903d8k.htm.
7. Houston Public Media / Investing.com triage sources (Q15_triage.json): Houston resiliency settlement, Houston load growth (dated 2025-06-17 and undated 2026 article).
8. Secondary-source credit-metric aggregation (FFO/debt, debt/EBITDA), cross-check only, not independently re-derived from XBRL for the latest quarter — accessed 2026-09-27.

## 13. Data basis, recency and disclaimer
Most recent period incorporated: Q1 2026 10-Q (accession 0001130310-26-000028, filed 2026-04-23, period ended 2026-03-31) from XBRL companyfacts, supplemented by the Q2 2026 8-K earnings release (accession referenced in §12, period ended 2026-06-30, released ~2026-07-28) for headline EPS figures not yet reflected in the cached companyfacts extract at the time of this diligence (2026-09-27). Events checked to 2026-09-25. GAAP figures are labelled GAAP; company-reported "non-GAAP EPS" figures are labelled as such and are the company's own reconciliation, not independently rebuilt from GAAP line items in this window. Research, not personal investment advice.
