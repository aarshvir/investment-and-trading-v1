# Audit 3 — historical availability, data lineage, missing values and regime-skill readiness

Audit date: September 26, 2026 (Dubai). Original investment snapshot: September 24, 2026 US close. Scope: all 497 scored companies, all 14 finalists, both price matrices, 593 cached release documents, annual fundamentals and saved historical backtest rows. This audit reads the preserved source bundle; it does not overwrite it or replace missing observations with invented values.

**Decision: the historical validation and weekly trading signals are not decision-ready.** The source files contain a recent cross-market price-data gap, an almost absent growth history in the 2023 validation slice, and unsupported management passes when earnings-release research is missing. Those are demonstrable data defects, not disagreements about market outlook.

## 1. The September 22 outage affects 12 of 14 proposed holdings

The long-history matrix contains 2,765 rows and 498 columns (497 scored stocks plus S&P 500), spanning September 25, 2015–September 24, 2026. It has 38,795 missing cells, most of which are not themselves proof of bad data because some companies did not trade for the full interval. The important distinction is **440 cells made artificially present by forward-filling**: 439 on September 22, 2026 and one on November 12, 2025. September 22 affects **438/497 scored stocks plus the S&P 500 benchmark**.

The three-year matrix independently contains the same September 22 gap for those 438 stocks. It cannot repair even one affected stock. The two files come from the same provider and are not independent corroboration.

**12/14 finalists are missing September 22 in both files:** CPAY, AMP, RL, AME, SNA, ABNB, NTAP, PAYX, IBKR, HIG, ALLE and AIZ. NVDA and MSFT have observations. The original scripts' unconditional `.ffill()` converts the missing day into a 0% return and puts the accumulated change into the next available day. Thus the copied benchmark and stocks can appear synchronized while their daily path is unobserved.

Examples from the original adjusted-price cache:

| Stock | Artificial Sep 22 return | Sep 23 return after forward-fill | Original annualized 252-day volatility | Exclude gap-touching intervals: sensitivity only |
|---|---:|---:|---:|---:|
| ABNB | 0.00% | -10.3452% | 36.1675% | 34.7503% |
| PAYX | 0.00% | -9.1470% | 29.7190% | 28.3977% |
| AMP | 0.00% | -6.1469% | 26.3150% | 25.6808% |

The final column is **not corrected risk**, and neither its direction nor magnitude bounds the true effect. Removing missing intervals drops potentially important returns. Without external observations the actual Sep 21–23 movement remains but its two daily components are unavailable. A weekly endpoint return can remain mathematically unchanged while intraperiod drawdown and risk are wrong. A subsequent independent observation repair for the 12 finalists is documented immediately below; the original-cache diagnostic CSVs deliberately remain unmodified.

### Raw observations recovered for the 12 finalist gaps; adjusted-return patch provisional

The parallel price auditor recovered the actual September 22 observations from explicit StockAnalysis historical price tables, rather than interpolation. Their September 24 raw closes also reconcile to the original cache. These are corroborating distributor observations, not a complete raw exchange-feed certification. A separate 12-row patch preserves each source URL and price. All original files remain unchanged. **426 other scored stocks still have the September 22 gap.**

For RL, the current external adjusted price (345.08) already incorporates a subsequent dividend. We use the 346.06 raw close matching the September 24 snapshot basis; mixing the current adjusted vintage into the old series would introduce a new error. Other names likewise use the raw closes reconciled at the snapshot endpoint. Full corporate-action reconstruction remains a separate open control. Matching September 24 raw endpoints does not by itself establish that every September 22 inserted raw observation matches the original adjusted series through the cutoff. All patch-dependent return, beta and volatility calculations below are provisional diagnostics until intervening actions are reconciled.

| Recomputed measure | Original forward-filled path | Externally corroborated finalist repair |
|---|---:|---:|
| ABNB Sep 22 daily return | 0.0000% | **-3.0149%** |
| ABNB Sep 23 daily return | -10.3452% | **-7.5582%** |
| ABNB annualized 252-day volatility | 36.1675% | **35.5973%** |
| PAYX Sep 23 daily return | -9.1470% | **-8.7663%** |
| PAYX annualized 252-day volatility | 29.7190% | **29.6064%** |
| AMP annualized 252-day volatility | 26.3150% | **26.0218%** |
| Portfolio annualized daily-return volatility, latest 252 days | 15.9939% | **15.9239%** |
| Portfolio weekly-return volatility, latest 156 weeks | 17.8266% | **17.8266%** |

The portfolio diagnostic uses the prior audit's exact original basket weights and daily or weekly constant-weight returns as labeled. It is not the original monthly bootstrap's volatility or a new allocation. Six- and twelve-month endpoint momentum and three-year maximum drawdown are unchanged for each finalist; moving averages change because the previously missing interior observation is now present. The 14-name before/after metrics are in `03_finalist_repair_impact.json`; the corrected price-copy diagnostic is `03_finalist_repaired_history_diagnostic.csv`.

The parallel auditor additionally corroborated the September 22 S&P 500 **price-index** level of **7,764.64** in two distributor histories. The adjoining Sep 21/23/24 levels reconcile to the preserved cache; that observation was patched into the separate benchmark copy and daily beta recomputed for all 14 names. It is not a total-return index. Exact observations and source limitations are in `raw/02_sep22_sp500_observation.json`. [Investing.com dated S&P history](https://www.investing.com/indices/us-spx-500-historical-data), [ChartExchange SPX history](https://chartexchange.com/symbol/index-spx/historical/). A limited repair does not validate historical membership, filings, forecasts or the rest of the universe.

Evidence: `03_price_gaps.csv` enumerates leading/internal/trailing gaps for every column; `03_sep22_outage_497.csv` includes all 497 stocks, both caches, exact return and volatility sensitivity values. Both matrices have zero duplicate dates and zero nonpositive prices; those structural passes do not cure the gap.

## 2. The 2023 “out-of-sample” growth test largely had no growth data

The source backtest selects annual statement columns using fiscal period end before a fixed 90-day cutoff. For the September 29, 2023 test it uses periods ending by July 1, 2023. That is **not a check of when information became public**, nor a check of which version was public then.

| Saved historical slice | Tested companies | Nonmissing revenue growth | Nonmissing EPS growth | Distinct growth-pillar scores |
|---|---:|---:|---:|---:|
| 2023 | 485 | **1** | **5** | 5 |
| 2024 | 491 | 488 | 440 | 400 |
| 2025 | 495 | 495 | 462 | 417 |

These are recomputed from `bt_frames.pkl`, not estimates. At the earlier cutoff 494/497 companies have one available annual revenue value, but **only PSKY has two**. The cross-sectional median fill therefore gives nearly every 2023 company the same revenue-growth input, rather than testing a real historical growth signal. The result cannot validate the intended growth factor. The exact company/year coverage is in `03_backtest_period_availability.csv`.

PSKY is itself a necessary identity-control example. Paramount says PSKY began trading on August 7, 2025 after the merger, and distinguishes predecessor through August 6 from successor thereafter. Historical vendor series labeled PSKY therefore require documented predecessor security and accounting mappings; their presence is not proof the 2023 economic entity and basis were identical. This audit does not assert every historical PSKY value is wrong. It establishes that the required mapping and vintage evidence are absent. [Paramount merger announcement](https://www.paramount.com/press/skydance-media-and-paramount-global-complete-merger-creating-next-generation-media-company), [predecessor/successor accounting FAQ](https://ir.paramount.com/investor-faqs).

## 3. Filing coverage is narrower than the “read everything” impression

The preserved EDGAR cache has **593 documents for 66 companies**. That leaves **431/497 companies without cached earnings-release research**. All 14 finalists do have nine release entries apiece; that is useful coverage of earnings releases, but is not a full 10-K/10-Q/footnote audit.

Most seriously, **394 of those 431 unresearched companies pass the management/red-flags lens**. The cause is explicit: `conv.py:42` tests `cuts4.fillna(0)==0`. Missing evidence is treated as no guidance cuts. `conv.py:35` also treats missing nonfinancial net-debt/EBITDA as zero in its balance-sheet comparison. These are unearned favorable assumptions. A re-audit must change required evidence to UNKNOWN and gate entry, rather than assign zero cuts or zero leverage.

The collection script requests 8-Ks containing Item 2.02 after July 1, 2024, picks the first filename matching a release-style expression, and stops after nine documents. It does not collect every material filing, amendments, debt-note tables, auditor opinions, segment footnotes, or the filing's complete exhibit tree.

| Document integrity test | Count |
|---|---:|
| Cached release documents | 593 |
| Exactly 60,000 characters: source collector truncation | **56** |
| Longer than 15,000 characters: guidance scoring ignores remainder | **544** |
| Longer than 40,000 characters: flag parsing ignores remainder | **233** |
| Preserved SEC acceptance timestamp | **0** |
| Preserved original HTML alongside parsed release | **0** |

The cache preserves filing date, URL and stripped text. Accession and CIK can be recovered from its URL, which the new `03_document_ledger.csv` does for all 593 documents. It also adds a SHA-256 of the cached text. These hashes prove which cached text we audited; they do **not** prove the original collector captured the whole filing or that the extracted figures were correct.

The cached release dates run July 11, 2024–September 23, 2026. They cannot independently document what was known at the September 2023 backtest date. Guidance regex matching is weaker than checking the actual numerical prior and revised guidance ranges and the statement to which they refer. The explicit MSFT override at `conv.py:30` fixes one recognized regex false positive but does not validate all other companies.

## 4. What point-in-time evidence is missing

The annual financial tables provide fiscal periods and normalized labels, but no retained accession per fact, acceptance time, filing vintage, tag/context/unit or restatement history. **0/497 companies are verified here as having original, point-in-time annual financial vintages.** This is a coverage statement, not a claim that all current numbers are wrong.

The source universe has 503 security rows; the scored data have 497. The omitted tickers are FDXF, FOX, GOOG, HONA, NWS and Q. The source contains no dated membership intervals or delisting-return ledger. Replaying today's surviving securities over an earlier decade is not historical S&P membership. For a concrete benchmark example, Airbnb joined the S&P 500 on September 18, 2023; its earlier returns may be legitimate listed-stock returns but cannot establish it was an index member in the years before inclusion. [S&P's dated inclusion notice](https://press.spglobal.com/2023-09-01-Blackstone-and-Airbnb-Set-to-Join-S-P-500-Others-to-Join-S-P-100%2C-S-P-MidCap-400-and-S-P-SmallCap-600).

The SEC provides submissions and company-fact APIs, but merely switching to SEC data is insufficient: frames select a last-filed fact aligned to a calendar period, and can contain differing start/end dates. Build an accession-specific, acceptance-time-bounded fact store; keep as-filed and restated values separately, and never apply a later restatement to an earlier decision date. [SEC API specification](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [SEC filing and acceptance-time definitions](https://www.sec.gov/about/webmaster-frequently-asked-questions).

The target lineage must be:

`security ID + ticker effective dates → original document/response + hash → accession + acceptance/publication time → XBRL tag + context + unit + fiscal interval → normalized metric + reconciliation → feature computed before decision timestamp → rule/version → risk-constrained proposed action`.

Today the strongest reproducible chain is `vendor snapshot → calculation → score`, with release URLs for a subset. That is materially weaker than the target.

## 5. Corporate-action spot checks: continuity passes, complete reconciliation remains open

| Event | Primary-source fact | Cached adjusted return over event |
|---|---|---:|
| NVDA, June 10, 2024 | 10-for-1 split-adjusted trading | +0.7461% |
| IBKR, June 18, 2025 | 4-for-1 split-adjusted trading | +1.0712% |
| CPAY, March 25, 2024 | FLT renamed/re-tickered to CPAY | +1.4509% |

These tests find no obvious 90% or 75% artificial collapse on the checked split dates. They do not independently verify every price, dividend reinvestment, share count, spin-off, or cash merger consideration. There is no explicit corporate-action ledger in the supplied data. [NVIDIA split FAQ](https://investor.nvidia.com/files/doc_downloads/2024/06/nvidia-2024-stock-split_faq_investors.pdf), [IBKR filing and retroactive per-share adjustment](https://www.sec.gov/Archives/edgar/data/1381197/000138119725000103/ibkr-20250630x10q.htm), [Corpay dated rename notice](https://investor.corpay.com/news-releases/news-release-details/fleetcor-announces-rebranding-corpay).

The backtest also multiplies an adjusted historical price by statement diluted average shares (`backtest3.py:33`) to approximate market cap. Diluted average shares are not contemporaneous shares outstanding; dividend-adjusted price is not the traded price used to measure historical market capitalization. Split bases must also match. This approximation needs replacement before historical valuation yields are interpreted as exact.

## 6. The explicitly requested Druckenmiller skill was exercised, with honest limits

The skill and its investment philosophy, market-analysis and conviction-matrix references were read. No recent required reports existed initially. Its actual no-key upstream scripts were run, producing:

| Required input | Actual result | Underlying data date | Eligibility |
|---|---|---|---|
| Market breadth | 28.6/100, Weakening | Sep 24, 2026 | Generated, not independently corroborated |
| Uptrend | 39.6/100, Cautious | Sep 24, 2026 | Generated, not independently corroborated |
| Market top | Execution stopped: FMP key unavailable to process | None | Missing |
| Macro regime | Execution stopped: FMP key unavailable to process | None | Missing |
| Follow-through day | Execution stopped: FMP key unavailable to process | None | Missing |

The required synthesizer was then run with `--max-age 72`; it **correctly refused** to synthesize because three required files are missing. No market conviction score or synthesized allocation is published. The first no-key execution hit Windows text encoding only after generating JSON; rerunning in UTF-8 completed genuine JSON and Markdown reports. No package installation or account setup was used.

The two available signals share TraderMonty provenance. They are **two measurements, not two independent data providers**. Raw source CSVs, source URLs, retrieval timestamps, sizes and SHA-256 values are saved under `reports/raw` and `reports/03_druckenmiller_readiness.json`. Breadth covers 2,512 observations; uptrend has 29,262 sector/time-series rows. Their numerical scores are heuristic, not calibrated success probabilities.

The fetched September 24 breadth reading has 8-day breadth around 52.6%, about 10.4 percentage points below its 200-day breadth average; uptrend ratio is about 13.7%. These reproduce the third-party series' outputs. Security-level constituents, corporate actions and point-in-time membership underneath those external aggregates have not been independently rebuilt. The peak/trough method uses historical turning-point detection; it must be replayed on truncated history before historical results can be treated as free of hindsight.

### Skill-code audit findings

1. **Fresh file is not fresh data.** `report_loader.py` tests filesystem modification time; copying an old report can make stale underlying observations pass. Require both creation time and latest observation date against the appropriate market calendar.
2. **A present JSON file can be malformed.** Extractors do not enforce required fields. An isolated malformed-input test (empty report bodies, never used as market data) yields a **38.5 conviction score and 5 “available” components**. Missing market-top score defaults to zero, which becomes 100/100 distribution health.
3. **The `data_availability` argument is ignored when constructing availability.** The regression probe supplied `distribution_risk=False`; the returned component still marked itself available. Required unknown data must block allocation.
4. **Agreement and bullishness are different.** Five mutually bearish test scores still produce **85/100 convergence**, which contributes positively to conviction. Macro transition intensity is also used in convergence as though higher always meant bullish; its own methodology describes transition intensity irrespective of direction. Recode signed directional agreement separately from confidence/transition intensity.
5. **The documented exposure/position rules are uncalibrated heuristics for this mandate.** Generic 90–100% equity, a 25% single position, or selective leverage must not override the user's 15–20% drawdown tolerance. A 25% holding falling 60% alone consumes 15% of total capital. Scores require walk-forward validation, transaction costs, turnover, crisis-path stress tests and observed calibration before they can justify allocations.

## 7. Required repairs before the weekly system proposes trades

**Data gate:** block affected daily signals until Sep 22 stock and benchmark prices are independently reconciled; preserve every raw response and adjustment basis. Unknown data remain UNKNOWN, never zero risk or a management pass. Separate pre-listing absence, market closure, halted trading, a provider outage and delisting.

**Historical gate:** obtain dated membership/security mappings, delisting and merger consideration, original filing vintages, enough prior fiscal periods, and estimates as published at the decision date. Archive successive weekly snapshots. Re-run features and portfolio decisions strictly using data then available; no current normalized fundamentals masquerading as past vintages.

**Research gate:** numerical guidance bridges, GAAP/non-GAAP reconciliation and full filings/footnotes must support each finalist. Three independent reviewers reusing Yahoo or one CSV lineage do not constitute three data-source validations.

**Mandate gate:** keep regime indicators advisory until complete and validated. Apply portfolio drawdown stress, position and correlated-sector risk limits first; revise the strategy's risk assumptions when evidence fails. The allowed variable holding period does not eliminate overnight gaps or make weekly reviews adequate for day trades. A weekly research refresh needs separately defined intraday/event triggers if positions may last only a day.

Artifacts: `03_lineage.json`, `03_document_ledger.csv`, `03_company_coverage_497.csv`, `03_price_gaps.csv`, `03_backtest_period_availability.csv`, `03_sep22_outage_497.csv`, `03_finalist_price_patch.csv`, `03_finalist_repair_impact.json`, `reports/03_druckenmiller_readiness.json` and genuine upstream reports. Reproduction scripts are `lineage_compute.py`, `repair_finalist_prices.py` and `skill_readiness_audit.py`. A final integrity recheck matched all 67 preserved source-file hashes; zero originals changed (`03_original_integrity_recheck.json`).
