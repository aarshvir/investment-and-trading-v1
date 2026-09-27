# The Allstate Corporation (NYSE: ALL) — Fundamental Diligence Dossier

**Prepared by:** f1 (fundamental diligence analyst) | **Data cutoff:** 2026-09-25 close | **Most recent period incorporated:** Q2 2026 (10-Q filed 2026-08-05, period ended 2026-06-30); checked for events to 2026-09-25. Next scheduled report: Q3 2026 on 2026-11-04. **Basis:** consolidated GAAP financial statements throughout (Allstate reports on a single consolidated basis; adjusted net income is the company's own non-GAAP measure, labeled as such wherever used).

**Data quality note:** all financial figures below are sourced to SEC EDGAR primary filings (10-Q/10-K, 8-K earnings-release exhibits) or SEC XBRL company facts (a machine-readable copy of the same filings), each cited by number in §12; quant/peer context is sourced to the v4 internal `lead_prelim_rank.csv` and `d4_live_snapshot.parquet`, labeled as such. Figures marked ¹ are derived (FY minus 9-month YTD, both officially reported) rather than directly reported. The Q4/FY2025 earnings-release exhibit could not be fetched this session (persistent SEC EDGAR 503 errors); FY2024/2025 annuals instead use SEC XBRL company facts, a fully primary but less narrative source — see note at the end of §12. No figure is estimated, interpolated, or recalled from training-data memory. **This dossier is research output for internal investment-process use, not personalised investment advice; it is not a recommendation to buy or sell any security, and the reader is responsible for their own decisions.**

## 1. Verdict: INCLUDE-SMALL (half weight) — thesis horizon 6–18 months
Real, structural personal-lines repair (auto/home) layered on top of an even larger cyclical/base-effect earnings surge; current profitability (44% trailing adjusted ROE) is not a run-rate. Half-weight sizing reflects a genuine business but a high near-term probability that reported earnings decelerate sharply, which the market (7.65x NTM P/E) and the Street (FY2027 consensus EPS −21% vs FY2026) already anticipate.

## 2. Business in plain English
Allstate is a personal-lines-focused P&C insurer (the "You're in Good Hands" brand) selling primarily auto and homeowners insurance to individuals through captive/exclusive agents, independent agents, and direct channels, plus non-standard auto via its National General subsidiary (acquired 2021). It also runs smaller Protection Plans (extended warranties/appliance protection) and Health & Benefits segments. It earns money through underwriting profit and investment income on reserves, and — unusually for a "carrier" — a meaningful fee-based Protection Services business layered on top.

## 3. Why the model likes it — and whether that's durable
b1-family prelim scores (source: internal `lead_prelim_rank.csv`): Q 0.752, V 0.586, M 0.940 (12-1m return +22.4%), composite 0.874. **This is the starkest case in the batch of a quant score built substantially on a cyclical peak.** Per `d4_live_snapshot.parquet`, trailing GAAP ROE (Yahoo-sourced field) is **46.1%**; per the Q2-26 earnings release (§12 #1), the company's own "adjusted net income ROE (ttm)" is **44.2%**, up from 28.6% a year ago (+15.6 pts). No P&C insurer sustains a 44% ROE through a cycle — the sector playbook's own "excellent and rare" bar is 15%+. The **d4 quant snapshot explicitly flags this**: `ntm_flags = "fy1_below_fy0_by_15pct+"`, `ntm_quality = "caution"` — FY2027 consensus EPS ($27.74) is **21.3% below** FY2026 consensus ($35.26), the largest forward-EPS air-pocket of the three names reviewed (`d4_live_snapshot.parquet`). Momentum (M=0.940) and the Value score (cheap on trailing/NTM earnings, 7.65x P/E per d4) are two sides of the same coin: the market is pricing today's earnings as unrepresentative. **Durable part:** per the Q2-26 release (§12 #1), auto insurance policies-in-force are growing (+2.8% YoY) with **new business up 8.8%**, i.e. Allstate is not just harvesting price increases while losing share — the repricing appears to be holding demand, a real structural signal. **Not durable:** the *magnitude* of current combined ratios and ROE.

## 4. Results — last 8 quarters + FY trend (GAAP; SEC XBRL, source #6, cross-checked to press releases #1–#3)
| Quarter | Revenue ($B) | Net income to common ($B) | Diluted EPS (GAAP) |
|---|---|---|---|
| Q3 2024 | 16.63 | 1.190 | 4.33 |
| Q4 2024 | 16.51 | 1.928¹ | 7.07 |
| Q1 2025 | 16.45 | 0.595 | 2.11 |
| Q2 2025 | 16.63 | 2.109 | 7.76 |
| Q3 2025 | 17.26 | 3.746 | 13.95 |
| Q4 2025 | 17.35 | 3.832¹ | 14.37 |
| Q1 2026 | 16.94 | 2.457 | 9.25 |
| Q2 2026 | 18.60 | 3.271 (3.241 to common) | 12.51 |

¹ Derived as FY minus 9-month YTD (both officially reported XBRL figures, source #5). Per the Q2-26 earnings release (source #1), adjusted (non-GAAP operating) net income was Q2-26 $2.330B/$8.99 diluted vs Q2-25 $1.591B/$5.94 (+46%); note GAAP EPS *exceeds* adjusted EPS this quarter because of large net realized/unrealized investment gains excluded from the adjusted figure — the opposite of the usual "adjusted flatters GAAP" pattern, worth flagging as its own data point.

**Combined ratio (Property-Liability; recorded vs. underlying — the sector-correct measure):**
| Period | Recorded CR | Underlying CR (ex-cat, ex-PYD) |
|---|---|---|
| Q2 2025 | 91.1% | 79.5% |
| Q2 2026 | 86.6% (−4.5 pt) | 79.4% (−0.1 pt, flat) |
| 1H 2025 | 94.2% | 81.3% |
| 1H 2026 | 84.3% (−9.9 pt) | 79.8% (−1.5 pt) |

Per the same Q2-26 release (source #1): Auto recorded combined ratio 83.3% (Q2-26) vs 86.0% (Q2-25), underlying flat at 87.6%/87.8%. **Homeowners: recorded 94.6% vs 102.0% (big headline improvement from lower cat losses), but *underlying* combined ratio actually worsened to 61.5% from ~58.6%, "reflecting higher loss costs"** — a genuine deterioration masked by a benign-cat headline. Catastrophe losses: Q2-26 $1.408B vs Q2-25 $1.614B; 1H26 $2.454B vs 1H25 $3.438B (−28.6%) — again largely the January 2025 California wildfires rolling off (10-Q, Note on catastrophes and reinsurance recoverables explicitly references "the California wildfires" reinsurance program). **Conclusion: as with TRV, the great majority of the YoY "recorded" combined-ratio improvement is a catastrophe base effect and reserve releases, not underlying repricing — underlying auto is flat and underlying homeowners is getting worse.**

## 5. Guidance track record
Allstate, like TRV, **gives no formal quantitative EPS/margin guidance** in earnings releases (no "outlook"/"guidance"/numeric target found across the releases reviewed). Not applicable; see §3/§8 for forward-looking read.

## 6. Earnings quality & balance sheet
- **FCF/OCF:** FY2025 OCF $10.110B, capex $228M, FCF≈$9.882B vs GAAP NI $10.282B (≈0.96x) — reasonable, though (per sector playbook) OCF is partly a float-growth artefact, not a pure quality signal.
- **SBC:** $123M FY2025 = 0.18% of revenue — immaterial.
- **Debt:** $7.492B (Q2-26) vs $7.490B (FY25) — stable, and consistent with both Yahoo ($7.497B) and the b1 prelim figure ($7.742B); **no material data conflict here** (unlike TRV/GL — see their dossiers).
- **Buybacks:** paused during the 2022-23 capital rebuild ($335M FY23, just **$2M** FY24) then resumed hard: $1.233B FY25, **$1.0B in Q2-26 alone** ("share repurchases were increased to $1.0 billion for the quarter"). This buyback reactivation timeline is itself corroborating evidence of the cycle: capital was scarce in 2022-23 (the personal-auto crisis years) and abundant now.
- **Book value:** $123.38/share, **+49.7% YoY** — an extraordinary one-year jump, driven by the earnings surge plus buybacks; not a steady-state compounding rate.
- **Policies in force:** total 215.9M (+3.8%); auto 25.95M (+2.8%, new business +8.8%); homeowners 7.82M (+2.9%, new business +16.4%) — growing, not just repricing a shrinking book.

## 7. Valuation snapshot
*(`scripts/ratios.py`/`scripts/valuation.py` were deliberately not run: their outputs — EV/EBITDA, FCF-based DCF, generic ROCE/current-ratio — are the specific metrics the insurance sector playbook states are undefined or misleading for underwriters. The P/B-anchored-to-ROE and peer-comparison approach below is the playbook's mandated substitute.)*

NTM P/E (d4) **7.65x** — the cheapest of the three names on this metric, and the reason is the FY2027 consensus air-pocket, not a re-rating opportunity per se. P/B **1.82x**. Peer set (same live snapshot): PGR 3.48x P/B / 34.9% ROE (PGR's own `pe_ntm` reads as a data anomaly — 0.27x — excluded as unusable, likely a denominator/split artefact); CB 1.71x/14.8%/11.6x; HIG 1.75x/22.1%/9.2x; CINF 1.50x/21.5%/18.3x. **Read:** ALL trades at a *lower* P/B than PGR despite a *higher* reported ROE — the market has already substantially discounted ALL's ROE as unsustainable. Reverse-DCF sense: at 1.8x book, the price requires normalized ROE of roughly only 12-15% to be justified (using the sector playbook's P/B≈(ROE-g)/(COE-g) framework) — i.e. even a large mean-reversion from 44% is largely priced in already. The open question is whether normalized ROE lands at "high teens" (still attractive, supports upside) or reverts closer to the mid-single-digits/negative territory seen in the 2022 personal-auto crisis (FY2022 net income was **−$1.289B**, per XBRL) if the pricing cycle turns harder than expected.

## 8. Bull case / Bear case
**Bull:** (1) Policies-in-force and new business are both growing at mid-to-high single/double digits — the repricing is holding volume, unlike a pure harvest-and-shrink strategy. (2) Even after heavy mean-reversion, current valuation (7.65x NTM P/E, 1.82x P/B) leaves room for a "normal-good" outcome (mid-teens ROE) to still look cheap. (3) Capital position fully rebuilt from the 2022 crisis with buybacks now running at $1B/quarter.
**Bear:** (1) 44% ROE and the FY2027 consensus EPS cut of 21% are not compatible with "durable" — a two-year-old bull case (auto repair) has now been almost entirely realized and priced. (2) Underlying homeowners combined ratio is *already* deteriorating (61.5%, +2.9 pts YoY) even before any broader loss-cost reacceleration — an early crack in the "structural improvement" story. (3) The auto insurance pricing cycle is adversarial: Allstate's own price increases invite competitor re-entry (Progressive, GEICO, State Farm) exactly when Allstate's margins look best, which is the mechanism by which 2022-style compression historically returns.

## 9. Key risks & kill criteria — thesis is invalidated if any of the following are observed (source: company 10-Q/8-K disclosures each quarter)
1. Property-Liability recorded combined ratio > 100% for two consecutive quarters.
2. Auto or homeowners policies-in-force growth turns negative for two consecutive quarters (share loss as competitors reprice back down).
3. Adjusted net income ROE (ttm) stays above ~35% for another two quarters *without* a corresponding upward revision to FY2027 consensus (would mean the deceleration is being denied, not resolved) — OR falls below ~15% (confirms hard mean reversion, re-underwrite thesis).
4. Net favorable reserve development flips negative in auto/casualty for two consecutive quarters.
5. Homeowners underlying combined ratio deteriorates a further ~5 pts from 61.5%.

## 10. Catalysts & calendar
Next earnings: **2026-11-04** (Q3 2026 — peak-of-hurricane-season print). No investor day/index event identified in this pass.

## 11. Red-flag scan
No auditor change (no Item 4.01 8-K found), no restatement, no going-concern/material-weakness language, no SEC/DOJ investigation disclosed. "No material changes" to FY2025 10-K risk factors per the Q2-26 10-Q. One named routine suit (Holland Hewitt v. Allstate Life, E.D. Cal.) noted in passing in the 10-Q's litigation note — appears to be ordinary-course, not separately escalated. 40 Form 4 filings between 2026-02-23 and 2026-09-08 (SEC EDGAR) — direction not individually tabulated in this pass; no 13D/G activist stake surfaced.

## 12. Sources
1. ALL Q2 2026 earnings release (8-K Ex-99.1, filed 2026-08-05): https://www.sec.gov/Archives/edgar/data/899051/000089905126000117/allcorp63026earningsreleas.htm
2. ALL Q2 2026 10-Q (filed 2026-08-05): https://www.sec.gov/Archives/edgar/data/0000899051/000089905126000118/all-20260630.htm
3. ALL FY2025 10-K (filed 2026-02-20): https://www.sec.gov/Archives/edgar/data/0000899051/000089905126000031/all-20251231.htm
4. ALL SEC submissions index: https://data.sec.gov/submissions/CIK0000899051.json
5. ALL SEC XBRL company facts (revenue/NI/EPS/equity/OCF/SBC/buybacks time series): https://data.sec.gov/api/xbrl/companyfacts/CIK0000899051.json
6. ALL Form 4 filing history (SEC EDGAR atom feed): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000899051&type=4&output=atom
7. v4 internal: `data/lead_prelim_rank.csv`, `data/d4_live_snapshot.parquet` (quant context incl. `ntm_flags`/`ntm_quality`, peer snapshot: PGR/CB/HIG/ACGL/WRB/CINF)

Note: the Q4/FY2025 earnings-release exhibit (accession 0000899051-26-000013) returned persistent SEC EDGAR 503 errors across multiple retries during this session and could not be directly fetched; FY2024/FY2025 annual figures used instead come from SEC XBRL company facts (source #5) and the Q2-26 release's own YoY comparisons, both primary-sourced.
