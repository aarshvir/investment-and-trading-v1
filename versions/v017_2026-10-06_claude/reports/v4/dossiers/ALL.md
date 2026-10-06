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

¹ Derived as FY minus 9-month YTD (both officially reported XBRL figures, source #5). **[Corrected 2026-10-06: Q4 2025 net income applicable to common is $3.803B (FY $10.165B less 9M $6.362B, XBRL NetIncomeLossAvailableToCommonStockholdersBasic), not $3.832B; the row labelled 'to common' for other quarters is total net income (before preferred dividends of about $30m a quarter). Immaterial.]** Per the Q2-26 earnings release (source #1), adjusted (non-GAAP operating) net income was Q2-26 $2.330B/$8.99 diluted vs Q2-25 $1.591B/$5.94 (+46%); note GAAP EPS *exceeds* adjusted EPS this quarter because of large net realized/unrealized investment gains excluded from the adjusted figure — the opposite of the usual "adjusted flatters GAAP" pattern, worth flagging as its own data point.

**Combined ratio (Property-Liability; recorded vs. underlying — the sector-correct measure):**
| Period | Recorded CR | Underlying CR (ex-cat, ex-PYD) |
|---|---|---|
| Q2 2025 | 91.1% | 79.5% |
| Q2 2026 | 86.6% (−4.5 pt) | 79.4% (−0.1 pt, flat) |
| 1H 2025 | 94.2% | 81.3% |
| 1H 2026 | 84.3% (−9.9 pt) | 79.8% (−1.5 pt) |

Per the same Q2-26 release (source #1): Auto recorded combined ratio 83.3% (Q2-26) vs 86.0% (Q2-25), underlying flat at 87.6%/87.8%. **Homeowners: recorded 94.6% vs 102.0% (big headline improvement from lower cat losses), but *underlying* combined ratio actually worsened to 61.5% from ~58.6%, "reflecting higher loss costs"** — a genuine deterioration masked by a benign-cat headline. Catastrophe losses: Q2-26 $1.408B vs Q2-25 $1.614B; 1H26 $2.454B vs 1H25 $3.438B (−28.6%) — again largely the January 2025 California wildfires rolling off (10-Q, Note on catastrophes and reinsurance recoverables explicitly references "the California wildfires" reinsurance program). **[Corrected 2026-10-06: wrong figures. $1.408B / $1.614B / $2.454B / $3.438B are Allstate Protection HOMEOWNERS catastrophe losses (Q2 2026 release, homeowners table). Property-Liability total catastrophe losses were $1,722m in Q2 2026 vs $1,990m in Q2 2025 (-13.5%) and $2,962m vs $4,192m in 1H (-29.3%). The conclusion (most of the combined-ratio gain is cat base effect and reserve releases) is unchanged: 1H recorded CR 84.3 vs 94.2 = 9.9 points = cat 4.8 + favourable reserve development 3.6 + underlying 1.5. See Re-assessment (RA10).]** **Conclusion: as with TRV, the great majority of the YoY "recorded" combined-ratio improvement is a catastrophe base effect and reserve releases, not underlying repricing — underlying auto is flat and underlying homeowners is getting worse.**

## 5. Guidance track record
Allstate, like TRV, **gives no formal quantitative EPS/margin guidance** in earnings releases (no "outlook"/"guidance"/numeric target found across the releases reviewed). Not applicable; see §3/§8 for forward-looking read.

## 6. Earnings quality & balance sheet
- **FCF/OCF:** FY2025 OCF $10.110B, capex $228M, FCF≈$9.882B vs GAAP NI $10.282B (≈0.96x) — reasonable, though (per sector playbook) OCF is partly a float-growth artefact, not a pure quality signal. **[Corrected 2026-10-06: FY2025 net income applicable to common is $10.165B (XBRL), so FCF/NI is 0.97x, not 0.96x on $10.282B. Immaterial.]**
- **SBC:** $123M FY2025 = 0.18% of revenue — immaterial.
- **Debt:** $7.492B (Q2-26) vs $7.490B (FY25) — stable, and consistent with both Yahoo ($7.497B) and the b1 prelim figure ($7.742B); **no material data conflict here** (unlike TRV/GL — see their dossiers).
- **Buybacks:** paused during the 2022-23 capital rebuild ($335M FY23, just **$2M** FY24) then resumed hard: $1.233B FY25, **$1.0B in Q2-26 alone** ("share repurchases were increased to $1.0 billion for the quarter"). This buyback reactivation timeline is itself corroborating evidence of the cycle: capital was scarce in 2022-23 (the personal-auto crisis years) and abundant now.
- **Book value:** $123.38/share, **+49.7% YoY** — an extraordinary one-year jump, driven by the earnings surge plus buybacks; not a steady-state compounding rate.
- **Policies in force:** total 215.9M (+3.8%); auto 25.95M (+2.8%, new business +8.8%); homeowners 7.82M (+2.9%, new business +16.4%) — growing, not just repricing a shrinking book.

## 7. Valuation snapshot
*(`scripts/ratios.py`/`scripts/valuation.py` were deliberately not run: their outputs — EV/EBITDA, FCF-based DCF, generic ROCE/current-ratio — are the specific metrics the insurance sector playbook states are undefined or misleading for underwriters. The P/B-anchored-to-ROE and peer-comparison approach below is the playbook's mandated substitute.)*

NTM P/E (d4) **7.65x** — the cheapest of the three names on this metric, and the reason is the FY2027 consensus air-pocket, not a re-rating opportunity per se. P/B **1.82x**. Peer set (same live snapshot): PGR 3.48x P/B / 34.9% ROE (PGR's own `pe_ntm` reads as a data anomaly — 0.27x — excluded as unusable, likely a denominator/split artefact); CB 1.71x/14.8%/11.6x; HIG 1.75x/22.1%/9.2x; CINF 1.50x/21.5%/18.3x. **Read:** ALL trades at a *lower* P/B than PGR despite a *higher* reported ROE — the market has already substantially discounted ALL's ROE as unsustainable. Reverse-DCF sense: at 1.8x book, the price requires normalized ROE of roughly only 12-15% to be justified (using the sector playbook's P/B≈(ROE-g)/(COE-g) framework) — i.e. even a large mean-reversion from 44% is largely priced in already. **[Corrected 2026-10-06: the 12-15% range had no stated cost of equity. With the 10-year Treasury at 5.17% (25 Sep 2026), COE 9.0% (beta 0.8, ERP 4.8%) and g 3%, the price of 1.84x book value ($227.60 / $123.38) requires a sustained ROE of 14.1% (12.6% at COE 8.2%, 15.9% at COE 10.0%). Allstate's own ROE (net income to common / average equity) averaged 13.2% and had a median of 12.6% over 2016-2025 (11.3% median over 2012-2025, including -6.6% in 2022 and -1.8% in 2023). Implied is in line with, not well below, a 13.5% base. See Re-assessment (RA10).]** The open question is whether normalized ROE lands at "high teens" (still attractive, supports upside) or reverts closer to the mid-single-digits/negative territory seen in the 2022 personal-auto crisis (FY2022 net income was **−$1.289B**, per XBRL) if the pricing cycle turns harder than expected.

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
Next earnings: **2026-11-04** (Q3 2026 — peak-of-hurricane-season print). No investor day/index event identified in this pass. **[Corrected 2026-10-06: two post-Q2 events were missed. (1) 8-K of 17 Sep 2026 (accession 0000899051-26-000135): August catastrophe losses $748m ($591m after tax); July+August $1.43bn ($1.13bn after tax) against $397m a year earlier (and $558m for all of Q3 2025). (2) 8-K of 14 Jul 2026 (0000899051-26-000109, Item 5.02): Christian M. Lown joined as EVP and Chief Financial Officer on 3 Aug 2026. See Re-assessment (RA10).]**

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


---
## Re-assessment (RA10, 2026-10-06)
Data cutoff for filings: 2026-10-06 (EDGAR submissions checked for every ticker). Prices and share counts are the 25 Sep 2026 values in the dossier / d4 snapshot unless stated. Discount-rate convention for RA10: 10-year Treasury 5.17% (FRED DGS10, 25 Sep 2026; 5.28% on 2 Oct) plus an equity risk premium of 4.8% (assumption) times beta, where beta is the Blume-adjusted 5-year beta floored at 0.8 (raw betas of 0.15-0.6 understate risk when the 10-year yield is 5.17%). V1 used an ERP of 4.14% and unfloored betas. Research only; not personal advice.

**Result: verdict INCLUDE-SMALL kept; implied_vs_base was not stated in the summary -> in_line; 3-year scenario returns added (bear -11.5% / base +8.1% / bull +18.4%); one kill criterion added.** Original text above is unchanged except for inline **[Corrected 2026-10-06: ...]** markers.

**Recency (EDGAR, 5 Aug to 6 Oct 2026).** 8-K 17 Sep 2026, Items 7.01/9.01, accession 0000899051-26-000135 (August catastrophe losses, quoted above); 8-K 20 Aug 2026, accession 0000899051-26-000127 (July catastrophe losses $682m, $539m after tax, 23 events, about 75% from two wind and hail events); 8-K 14 Jul 2026, Item 5.02, accession 0000899051-26-000109 (new CFO Christian M. Lown from 3 Aug 2026; previously CFO of CoStar and Freddie Mac); three Forms 4 filed 5 Oct 2026 (Traquina, Perold, Keane; transaction detail not tabulated). No 10-Q, 10-K, 13D, S-4 or merger agreement after the 10-Q of 5 Aug 2026 (0000899051-26-000118). Prior-year comparison from the 2025 monthly 8-Ks (accessions 0000899051-25-000072, -000078, -000092): July 2025 $184m, August 2025 $213m, September 2025 $161m, Q3 2025 total $558m. Q3 2026 catastrophe losses are therefore already at least $1.43bn against $558m a year earlier, about $0.8bn after tax (about $3.2 a share on 253.5m shares) more than Jul+Aug 2025 before September. The Q3 print (dossier says 4 Nov 2026; not re-verified in a filing) will show a much higher recorded combined ratio even if the underlying ratio holds.

### Claims verified
| Claim | Status | Source |
|---|---|---|
| Q2 2026 adjusted net income $2.330bn / $8.99 per diluted share vs $1.591bn / $5.94 (+46%) | CONFIRMED | Q2 release Ex-99.1 (0000899051-26-000117) |
| Adjusted net income ROE (ttm) 44.2% vs 28.6%; GAAP ROE 49.1% | CONFIRMED | same release, consolidated highlights table |
| Book value per common share $123.38 (+49.7%); 253.5m common shares | CONFIRMED | same release |
| Property-Liability recorded combined ratio 86.6 vs 91.1 (Q2) and 84.3 vs 94.2 (1H); underlying 79.4 vs 79.5 and 79.8 vs 81.3 | CONFIRMED | same release |
| Homeowners underlying combined ratio 61.5 vs 58.6 "reflecting higher loss costs" | CONFIRMED | same release |
| Policies in force 215.9m (+3.8%); auto 25.95m (+2.8%, new business +8.8%); homeowners 7.82m (+2.9%, new business +16.4%) | CONFIRMED | same release |
| Cat losses Q2 $1.408bn vs $1.614bn; 1H $2.454bn vs $3.438bn labelled Property-Liability | WRONG (homeowners only) | release: total Q2 $1,722m vs $1,990m; 1H $2,962m vs $4,192m |
| FY2025 net income $10.282bn; Q4 2025 $3.832bn | WRONG (immaterial) | XBRL companyfacts: FY NetIncomeLossAvailableToCommonStockholdersBasic $10,165m; ProfitLoss $10,266m; derived Q4 $3,803m |
| Debt $7.492bn (Q2) vs $7.490bn (FY25) | CONFIRMED | XBRL LongTermDebt 7,492 / 7,490 |
| Buybacks FY2025 $1.233bn, FY2024 $2m, FY2023 $335m; $1.0bn in Q2 2026 | CONFIRMED | XBRL PaymentsForRepurchaseOfCommonStock 1,233 / 2 / 335; Q2 release "increased to $1.0 billion" |
| FY2025 OCF $10.110bn, capex $228m, SBC $123m | CONFIRMED | XBRL annual NetCashProvidedByUsedInOperatingActivities 10,110; AllocatedShareBasedCompensationExpense 123; capex quarters 92 - 1 + 48 + 89 = 228 |
| FY2027 consensus EPS $27.74 is 21.3% below FY2026 $35.26 | CONFIRMED as dossier / d4 value | d4_live_snapshot (epsCurrentYear 35.26017, epsForward 27.74057); not independently re-sourced |
| Dividend $4.32 a share (annual) | CONFIRMED as d4 value; Q2 dividends paid $280m | d4 dividendRate 4.32; Q2 release "$280 million in dividends" |
| Fed raised to 3.75-4.00% on 16 Sep 2026; 10-year 5.17% on 25 Sep | CONFIRMED | FOMC statement (as verified by RA1); FRED DGS10 fetched 6 Oct: 5.17 on 2026-09-25, 5.28 on 2026-10-02 |

### Valuation recomputed (own arithmetic)
Method: insurer, so P/B against sustainable ROE, (ROE - g) / (COE - g) = P/B, not a DCF on FCF. Book value per common share $123.38 (30 Jun 2026), price $227.60 (25 Sep 2026) = 1.84x. g = 3%. COE = 5.17% + 0.8 x 4.8% = 9.0% (V1's Blume beta is 0.63 and its ERP 4.14%, giving COE 7.78% and an implied ROE of 11.4%).

| COE | implied sustained ROE |
|---|---|
| 8.2% (V1 beta 0.63, ERP 4.8%) | 12.6% |
| 9.0% (central) | 14.1% |
| 10.0% | 15.9% |

Own history (net income applicable to common / average shareholders' equity, XBRL; equity includes about $2bn of preferred so common ROE is slightly higher): 2012 11.9%, 2013 10.8%, 2014 12.5%, 2015 9.7%, 2016 8.3%, 2017 15.9%, 2018 9.2%, 2019 19.8%, 2020 19.4%, 2021 5.4%, 2022 -6.6%, 2023 -1.8%, 2024 23.2%, 2025 39.1%. 2016-2025 mean 13.2%, median 12.6%; 2012-2025 mean 12.6%, median 11.3%. Base case sustained ROE 13.5% (range 11-16%): investment income is higher (Q2 net investment income $1,009m, +$255m; portfolio $87.8bn; trailing total return 5.6%) and Transformative Growth is adding policies (+3.8%), offset by the pricing cycle (the dossier's own bear case) and the Jul-Aug catastrophe run. Implied 14.1% is inside the base range -> **in_line**.

Cross-check on earnings: price / FY2027 consensus EPS = 8.2x; FY2027 consensus EPS $27.74 on book value of about $135-140 at end-2026 (own estimate) is a 20% ROE, so the market already discounts a fall from 44% to 20% in 2027 and to about 14% afterwards.

### Scenario arithmetic (3 years from 25 Sep 2026; annualised total return, aggregate model)
Start: equity $31.28bn ($123.38 x 253.5m), dividends $4.32 a share growing 4% a year, buybacks funded at the model price. Base: ROE 23% / 17% / 14% in years 1-3 (year 1 is NTM consensus EPS $29.74 on average book), buybacks $4.0bn a year (current pace $1.0bn a quarter), exit P/B 1.65x (justified 1.83x at 14%) -> exit price about $274, dividends $13.5, **+8.1%**. Bear: ROE 17% / 8% / 5%, buybacks $2.5bn, exit 1.0x -> about $144, **-11.5%**. Bull: ROE 25% / 22% / 19%, buybacks $5.0bn, exit 2.1x -> about $364, **+18.4%**. V1's +10.5% base used COE 7.78% and ROE 12.1% with 4.9% a year of share shrinkage.

**Verdict: INCLUDE-SMALL (unchanged).** At a 5.17% risk-free rate the price still requires only a mid-teens ROE through the cycle and sits at 8.2x FY2027 consensus, but there is no margin beyond that: the implied ROE is in line with the 13.5% base, the Q3 catastrophe run is the worst in the series, and the CFO has just changed. No kill criterion has fired (recorded combined ratio 86.6, policies in force growing, adjusted ROE 44% above 35%). Added kill criterion 6: Property-Liability underlying combined ratio above 85 in any quarter (79.4 now).
