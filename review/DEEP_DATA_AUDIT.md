# Deep data audit — investment evidence, 26 September 2026

**The three additional parallel audits materially improve the evidence, but do not clear the original portfolio for investment.** The review now comprises nine specialist agents in total, with an additional closing challenge by the original adversarial reviewer. The three new auditors investigated the data itself: filings and footnotes; prices, corporate actions and forecasts; and historical availability and transformations. They are separate reviewers using overlapping sources, not nine independent financial institutions.

Information cutoff remains **24 September 2026 US close**. Retrieval occurred afterward. A current webpage that agrees with a number does not prove that number was available at the historical cutoff. The newer findings below supersede inconsistent statements in the first six reports, which remain preserved as an audit trail.

## Decision-changing results

| Finding | Reconciled evidence | Investment implication |
|---|---|---|
| NVIDIA headline cash-flow field is unsuitable without a definition | Filing-derived TTM CFO less capital purchases **$127.006bn**; company-defined FCF **$126.886bn**; saved headline **$41.810bn** | Quarantine the ambiguous headline field. Saved quarterly totals already matched the conventional measure; this is a disagreement between fields, not proof all original cash-flow data were wrong. |
| Microsoft has the same headline-field problem | FY2026 conventional FCF **$66.987bn** versus saved headline **$16.546bn**; after finance-lease principal **$63.886bn** | Use an explicitly defined cash measure; reconcile leases before forecasting capital intensity. |
| Airbnb's disputed quarterly FCF claim is supportable | FCF **$1.253bn** and adjusted EBITDA **$1.261bn** both round to **$1.3bn / 35%** | Correct our earlier ambiguity. The two measures remain distinct; quarterly verification does not approve TTM vendor FCF or valuation. |
| Corpay uses a different FCF definition | H1 CFO less capex **$1.308bn** versus adjusted-income “FCF” **$0.862bn** | Reconcile customer funds, corporate liquidity and covenant leverage; these figures are not interchangeable. |
| A broad missing trading day was silently filled | **438/497 stocks plus benchmark** missing 22 September; repaired **12 affected finalists plus benchmark** in a separate copy | **426 other stock gaps remain.** Recalculate affected features; never equate missing data with a zero return. |
| The oldest validation slice lacks its central inputs | Of **485** companies in the 2023 test, only **1** has revenue growth and **5** have EPS growth | That slice cannot validate the intended growth strategy. Historical vintages and sufficient prior periods are required. |
| All 14 snapshot closes now have external corroboration | Dated public historical displays agree; authenticated FMP also agrees for **NVDA and MSFT** | This advances price validation, not forecast-vintage certification or whole-history verification. |
| Research coverage was overstated | **593 releases for 66 companies**; 56 collector truncations; 394 unresearched companies passed management checks | Replace favorable missing-data defaults with UNKNOWN. Complete filings and numerical guidance bridges are required. |

The filing work retained **12 successfully archived raw sources**, **67 selected inline-XBRL facts across six filings**, and a **33-row field ledger**, including two provider corroborations. One AMETEK release archive attempt timed out; its 8-K is retained. The market audit adds **154 field observations across 14 names**. The historical audit covers all 497 scored companies and all 593 cached releases. These counts describe the completed scope; they do not imply full forensic accounting for 497 companies.

Primary documents include [NVIDIA FY2026 cash flows](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), [NVIDIA H1 FY2027 cash flows](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf), [Microsoft FY2026 cash flows and lease note](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), [Airbnb's exact reconciliations](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000027/abnb-20260630.htm), and [Corpay's cash-flow statement](https://www.sec.gov/Archives/edgar/data/1175454/000117545426000050/cpay-20260630.htm). The detailed audit supplies page/table locators, accounting contexts and arithmetic.

## Measure the effect, rather than merely flag the problem

The externally corroborated missing-day repair changes ABNB's annualized 252-day volatility **36.1675% → 35.5973%**; PAYX **29.7190% → 29.6064%**; AMP **26.3150% → 26.0218%**. The original basket's constant-weight daily-return diagnostic changes **15.9939% → 15.9239%**. Weekly volatility remains **17.8266%**; each finalist's six- and twelve-month endpoint momentum and three-year maximum drawdown are unchanged. These are specifically defined diagnostics, not a replacement strategy backtest or a risk guarantee.

For Ralph Lauren, the missing-day raw close is **$346.06**, while the later dividend-adjusted display is **$345.08**. Inserting the latter into the frozen earlier series would create a new error. The separate patch uses the observed raw close. Matching the cutoff endpoint alone does not prove every intervening adjustment; the resulting return and risk diagnostics are provisional until corporate actions through the cutoff are fully reconciled. All 67 original source files remain unchanged. Complete historical corporate-action reconstruction remains open.

## Sources: establish what each can prove

| Source layer | Actual use and result | Boundary |
|---|---|---|
| SEC / issuer filings | Full statements, reconciliation tables, debt and lease footnotes; source bytes and hashes; selected XBRL contexts | Filing extraction is not an audit opinion on issuer accounting. Normalized cash flows still require judgment. |
| FMP authenticated API Viewer | Actual dated NVDA/MSFT prices and three annual cash-flow rows for each | Free plan returned 402 for the other 12 price queries. The UI displayed bundled AAPL sample data after failures; identity/date checks rejected it. No upgrade was purchased. |
| FMP evidence retention | Full NVIDIA JSON download; Microsoft selected fields transcribed from the complete displayed Raw response; two observed price objects retained | Microsoft capture is explicitly an observation extract, not a byte-for-byte downloaded response. No credentials are included. |
| Barchart / StockAnalysis / Cboe displays | Dated price corroboration and missing-day recovery; declared forecast accounting basis and fiscal horizon | A second website may share upstream data. Original forecast publication vintages and entire adjustment histories are not certified. |
| Financial Datasets | Reviewed deeper provenance and earnings schemas: Databento equity prices, SEC statement parsing, filing identifiers | At the initial audit the plugin showed Install. It is now connected, but a direct Microsoft FY2026 cash-flow query returned a $0.00 provider-balance error. No values were acquired; documentation remains distinct from validation. |

[Financial Datasets provenance](https://docs.financialdatasets.ai/data-provenance), [earnings lineage fields](https://docs.financialdatasets.ai/api/earnings), [FMP reference](https://site.financialmodelingprep.com/developer/docs), and [StockAnalysis source policy](https://stockanalysis.com/data-sources/) explain the source contracts. An endpoint named “historical” or “as reported” does not establish complete historical vintages. FMP's documentation and FAQ also conflict on historical constituent coverage; actual coverage must be tested before purchasing or relying on it.

Public forecast tables use adjusted EPS, and **next fiscal year is not next twelve months**. SNA, ABNB and PAYX have differing cached/displayed estimates. AME, PAYX and MSFT public pages were updated after the cutoff. Seven finalists lack original next-FY low/high/count fields. These are separate unresolved issues; a matched share price cannot cure them.

## The requested Druckenmiller framework

The finance-skills financial-analyst workflow and the explicitly requested Druckenmiller skill were read and applied. Actual upstream runs produced breadth **28.6/100** and uptrend **39.6/100**, using 24 September data. Both trace to TraderMonty; they are not independent providers. Their underlying security-level aggregates were not rebuilt.

The requested skill explicitly says: “Run the required skills first.” Its input requirements list five fresh reports. Source: C:/Users/user/.agents/skills/stanley-druckenmiller-investment/stanley-druckenmiller-investment/SKILL.md, lines 33–59. Market-top, macro-regime and follow-through-day runs stopped because the process lacked required FMP access. The synthesizer correctly refused the incomplete set. **No combined conviction score or allocation is published.** Separate code probes also found that malformed reports could pass weak schema defaults, file modification time could conceal old observations, and bearish agreement could inflate convergence. These must be repaired before the skill influences sizing.

Its generic concentration and exposure suggestions do not override your 15–20% drawdown tolerance. The useful principles are liquidity awareness, asymmetric reward versus loss, explicit thesis invalidation and flexibility when facts change. None establishes an empirically calibrated probability of profit.

## A stronger weekly method: three independent data passes

1. **Source and accounting pass.** Retrieve material filing facts with accession, acceptance time, raw file/hash, page/table, tag/context, period, unit and GAAP/adjusted definition. Rebuild TTM from fiscal intervals. Reconcile cash, capex, leases, share dilution, restricted/customer money, debt and acquisitions. Distinguish actual, management outlook and analyst assumption.
2. **Market and forecast pass.** Independently challenge instrument, session, price basis, corporate action and estimate horizon. Require timestamped forecast vintages and consistent contributor/period definitions. Reject wrong-symbol samples, HTTP/access errors and stale last-good responses. Compare independent collectors where available; disclose shared lineage.
3. **Historical and transformation pass.** Test session completeness and before/after effects of every repair. Use historical membership, original publication times, restatements, delistings and genuine prior-year data. Missing critical evidence blocks the relevant signal. Recompute dependent valuations and portfolio risk after material changes; do not merely edit the prose.

Each field carries a status: VERIFIED SPECIFIC FACT, RECONCILED DERIVATION, CORROBORATED DISPLAY, MANAGEMENT CLAIM, ASSUMPTION, or QUARANTINED. Reviewers retain disagreements. Accounting bridges reconcile within source rounding; price differences are investigated after timestamp/basis alignment. Exact provenance and materiality matter more than a blanket “two sources” checkbox. New or changed material fields receive all three passes; unchanged evidence can be reused with freshness and event checks.

The release decision remains a gate, not an average score: **data → economic underwriting → coherent valuation → historical validation → portfolio risk → implementation**. A material failure prevents a fresh purchase recommendation. Existing holdings require a separate thesis/risk decision; missing data alone is not an automatic sell rule.

## Unfinished work that affects capital deployment

The remaining gates are specific: 426 stock gaps and complete corporate-action coverage; original forecast vintages and uncertainty fields; accession-specific historical fundamentals and constituents; two-year full-filing underwriting beyond the targeted six-name work; AMETEK actual closing debt; Corpay covenant/customer-funds bridge; sustainable cash-flow forecasts; and validated portfolio construction. The repaired cash-flow numbers do not mechanically create new price targets. Revised target prices require a consistent FCFF or FCFE model and sensitivity to economic assumptions.

The current output remains **WATCH / re-underwrite** for the 14 candidates. No combined skill score, invented price target or personal sell instruction fills those gaps. Weekly refresh is active and now carries these source controls; it is research, not daily surveillance or trade execution.

**One next step:** provide the current holdings and cash export across accounts. That lets subsequent research prioritize actual exposure while continuing to close the valuation and data gates.


## Subsequent connection check

Financial Datasets is now callable. The actual MSFT annual cash-flow request for 30 June 2026 returned: “Your current balance is $0.00. Please add more credits to continue using the API.” No statement values were returned and no credits were purchased. The tool wrapper set isError=false despite the error text; data gates must inspect the actual response content. The exact request and response are retained in deep_audit/05_financial_datasets_connection.json. This supersedes the initial unavailable-connector status, while all financial conclusions remain unchanged.
