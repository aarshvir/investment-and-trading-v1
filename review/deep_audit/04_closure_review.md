# Independent closure review — deeper data audit

26 September 2026 Dubai. Original decision cutoff: 24 September 2026 US close.

**Conclusion:** The new work materially improves historical cash-flow reconciliation and dated-price corroboration. It supports correcting our earlier Airbnb caution. It does not establish independent forecast collection, point-in-time estimate vintages, complete historical-price integrity or investment approval.

## Exact checked scope

Read the three deep-audit reports, their ledger schemas and selected numerical records, the provider-access ledger, finalist repair code and outputs, and original-integrity results. Independently counted **33 filing observations**, **154 market observations across 14 finalists**, **497 company-coverage rows**, **593 cached-document rows**, and **497 outage rows**. Rehashed all **67 original source files** against the original manifest: **zero changed files**.

Recomputed the principal displayed cash-flow/debt bridges below. Independently reopened Airbnb's full SEC 10-Q and checked the quarterly reconciliation and customer-funds qualification; inspected Microsoft's downloaded 10-K text for operating cash, PPE additions, lease payments and uncommenced commitments. Inspected the saved FMP NVIDIA JSON, Microsoft selected-field capture and two price objects. This reviewer did not observe the authenticated FMP browser session, independently reopen all 14 external price/forecast pages, repeat every XBRL extraction, or rebuild all 497 histories. Provider-access conclusions depend on the lead's explicitly described capture record.

## Mathematical and source checks accepted

| Reconciliation | Independently checked result |
|---|---:|
| NVIDIA TTM CFO = FY + current H1 − prior H1 | $134,360m |
| NVIDIA TTM capital cash purchases / related principal | $7,354m / $120m |
| NVIDIA CFO less purchases / company FCF including principal deduction | $127,006m / $126,886m |
| NVIDIA conventional TTM less saved headline FCF | $85,196.125056m difference |
| Airbnb Q2 CFO less capex / FCF margin | $1,253m / 34.7284% |
| Airbnb separate adjusted EBITDA bridge | $1,261m |
| NetApp component bridge to CFO year-on-year change | −$170m |
| Corpay H1 CFO less capex / company adjusted-income alias | $1,307.950m / $861.554m |
| Difference between those Corpay definitions | $446.396m |
| AMETEK June carrying debt / illustrative post-purchase net debt | $2,036.174m / $6,540.728m |
| Microsoft FY2026 CFO less cash PPE / less finance principal | $66,987m / $63,886m |
| Microsoft conventional FCF less saved headline | $50,441.499840m difference |

Airbnb's filing supports both $1.3bn/35% rounded FCF and adjusted EBITDA, with different exact amounts. Its customer-held balances do not enter FCF except through interest; its own advance service-fee receipts do affect timing. Any earlier implication that the rounded FCF necessarily confused EBITDA must be superseded. This does not validate vendor TTM FCF. [Airbnb Q2 2026 10-Q, reconciliations and qualification](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000027/abnb-20260630.htm).

The downloaded Microsoft 10-K supports CFO $182,935m, PPE additions $115,948m, operating-lease cash $6,443m, finance-lease operating cash $2,547m and finance principal $3,101m. Deducting the first two lease cash categories again from CFO would double-count them. The $329.1bn uncommenced commitment is not all present recognized debt. [Microsoft FY2026 10-K](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm).

The AMETEK number remains an explicitly assumed financing bridge, not an observed closing balance sheet. Corpay's two FCF definitions and the vendor headline must remain separately labeled rather than forcing equality.

## Corrections and qualifications communicated

1. **Timestamp check — initial finding withdrawn:** direct inspection confirms raw `quote_utc` strings correctly use UTC, e.g. `2026-09-24T20:00:01+00:00`. This reviewer's PowerShell JSON round trip converted timestamps into Dubai local time and produced the apparent date discrepancy. That was an inspection-tool transformation, not a source-file defect. The market reviewer also added explicit `market_session_date=2026-09-24` to JSON/CSV as a useful downstream control.
2. **FMP capture method:** NVIDIA's annual JSON was downloaded; Microsoft's saved file contains selected fields transcribed from the full response displayed in the authenticated UI. The two price objects are also UI transcriptions. The latter files must not be described as byte-for-byte raw responses. Their hashes preserve these observation records, not transport provenance. Requested explicit capture wording in filing row F033 and report 01; the provider-access ledger already makes the distinction.
3. **Corpay leverage definitions:** the old vendor net-debt/EBITDA around 2.701x and management-reported 2.55x can use different definitions. A missing primary-table reconciliation does not prove the vendor ratio was fabricated or that 2.55x can simply replace it. The company/covenant numerator and denominator still need a bridge.
4. **Price-patch adjustment basis:** matching the raw September 24 endpoint is useful but does not alone prove that September 22 raw close matches the original adjusted-price basis. Confirm no intervening corporate action through the cutoff, or keep the inserted values labeled a provisional diagnostic pending that check. RL correctly excludes the later September 25 dividend adjustment. Requested this qualification from the lineage reviewer.
5. **Benchmark completion:** the latest repair-impact JSON now sets `benchmark_repaired=true` using the externally observed **7,764.64** S&P 500 price-index close. Supersede earlier statements that the benchmark is still missing. This repair concerns one price-index observation; it does not convert that benchmark into a total-return series.

## Source independence and date boundaries

The FMP-access ledger supports **two successful price responses and 12 HTTP 402 access failures**, with fallback samples explicitly rejected. It does not support FMP validation of the other 12 prices. Those have separate public-display corroboration. FMP annual statement extraction corroborates issuer numbers, but both derive from the same issuer filing. It does not independently corroborate NVIDIA's TTM bridge, estimate quality or economic durability.

Public StockAnalysis forecasts identify S&P Global, while the original Yahoo upstream is undocumented. Two distributors therefore do not establish independent estimate collection. Later page updates for AME, PAYX and MSFT also prevent calling the newly displayed forecasts a frozen September 24 vintage. The market report states these limits correctly. Next-FY EPS, NTM EPS, current-FY ranges and next-FY dispersion must remain separate. ABNB, SNA and PAYX cache discrepancies require reconciliation rather than selecting the most favorable denominator.

No authenticated Financial Datasets values were acquired. Provider documentation, API examples, an unavailable endpoint or an install page supplies no portfolio-number validation.

## Historical-coverage findings accepted

Independently recounted **431 companies without release research**, **394 of those passing the management lens**, and **438 scored stocks with the September 22 gap**. Of 593 cached releases, **56** reach the collector's 60,000-character cutoff, **544** exceed the guidance parser's 15,000-character limit, and **233** exceed the flag parser's 40,000-character limit. These counts support the coverage criticism, not a claim that omitted text necessarily contains adverse facts.

The separate patch fills 12 finalist gaps and the benchmark gap; **426 other scored stocks remain missing September 22**. The original-cache defect ledgers intentionally preserve pre-repair statuses and link to the later impact file. Daily versus weekly constant-weight risk comparisons are labeled correctly; they must not be substituted for the original monthly-rebalanced simulation's volatility. The price-index/total-return benchmark mismatch remains open.

The 2023 growth-coverage and missing historical-vintage conclusions are supported by the new ledgers and code review; this closure reviewer did not rerun the full pickle computation. Current cached releases cannot prove what was public in 2023. Likewise, recent regime-indicator files do not authenticate their constituent histories or create a validated daily trading strategy.

## Release gate

Publish the reconciled historical fields, explicit Airbnb correction, limited price-repair evidence and preserved uncertainty. Do not approve new trades from this audit alone. Outstanding gates include complete corporate-action alignment; the other universe gaps; original filing/estimate vintages; historical membership and delistings; coherent forecasts and valuations; reserve/product suitability; actual portfolio exposures; and forward validation. Multiple review agents and multiple distributors are useful controls, but neither automatically establishes independent underlying data or investment skill.

### Correction status at closure

Verified that report 01 now distinguishes Corpay's vendor and management leverage definitions and describes the Microsoft UI transcription accurately; F033 links the capture limitation to the provider-access ledger. The market builder/outputs now include explicit session dates; the original UTC field was correct and the initial defect finding was withdrawn. The benchmark patch is present. The remaining corporate-action alignment limitation must stay visible on the finalist diagnostic layer; its point-price corroboration is stronger than its certification as a complete adjusted return series.

The lead analyst subsequently added the provisional corporate-action alignment qualification to report03, the patch CSV, the repair-impact JSON, its reproduction script, the integrated synthesis and the current committee memo. The economic limitation remains open; the disclosure correction is complete.
