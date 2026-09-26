# Deep data audit 2: prices, estimate denominators, corporate actions and provenance

**Decision:** The 14 supplied 24 September 2026 closing prices are corroborated by dated external displays. This does not certify the whole historical price matrix, the original estimate vintages, or any investment recommendation. The most consequential unresolved issue is the meaning and timing of forecast earnings. A stock-price match cannot validate an EPS forecast.

The machine-readable deliverables are `02_market_ledger.json` (14 company records), `02_market_ledger.csv` (154 field observations), `02_market_manifest.json` (source-file hashes), and two explicitly labeled numerical observation records in `raw/`. Original source files remain unchanged. Audit observation hashes establish record integrity, not that an upstream provider supplied a raw payload.

## Three passes and their evidence boundaries

1. **Instrument/date/basis:** Recomputed quote timestamps, identified USD US equity instruments, compared the exact historical day rather than current web banners, and separated raw from dividend-adjusted prices. Rejected unavailable/stale Cboe snapshots. FMP authenticated access results are collected by the lead agent separately; access failures and sample payloads are not evidence.
2. **Denominator/period:** Recomputed current-FY and next-FY P/E from original EPS; checked 14 externally displayed forecast tables, their declared accounting basis, fiscal labels, dispersion and page-update dates.
3. **Adversarial reconciliation:** Tested whether a second website actually establishes independent collection, whether date labels mean vintage dates, whether an adjusted price from a later retrieval can repair a frozen earlier history, and whether low/high estimates exist for the period used in valuation.

These are data-audit passes, not three assertions that all data passed. The original dataset does not meet the proposed approval standard.

## What the price check establishes

For NVDA and MSFT, the Barchart-hosted dated historical rows show $224.58 and $497.93, respectively, and explicitly identify Barchart as the quote provider: [NVDA](https://sogotrade2.websol.barchart.com/?1_selected=stockQuote&module=stockDetail&region=US&symbol=NVDA), [MSFT](https://sogotrade2.websol.barchart.com/?1_selected=stockQuote&module=stockDetail&region=US&symbol=MSFT). AME is also $247.74 at 16:00 ET on the [Cboe quote page](https://www.cboe.com/delayed_quotes/AME/quote_table/). A last price shown at 16:00 is corroboration, not a certified closing-auction record.

The other twelve historical closes were read directly from dated StockAnalysis rows (including AME). The site identifies Cboe real-time pricing and primarily Nasdaq UTP delayed consolidated opening/closing pricing in its [source policy](https://stockanalysis.com/data-sources/). This documents a separate distributor and gives useful upstream lineage; a raw exchange feed, contract-level entitlements and per-record vendor metadata were not acquired. Market-wide volume differences across websites remain unadjudicated and should not be overwritten merely because the closing prices match.

| Stock | 24 Sep raw close | 22 Sep missing-day observation | Direct dated table |
|---|---:|---:|---|
| CPAY | 400.32 | 392.95 | [History](https://stockanalysis.com/stocks/cpay/history/) |
| AMP | 485.15 | 512.37 | [History](https://stockanalysis.com/stocks/amp/history/) |
| RL | 351.86 | 346.06 | [History](https://stockanalysis.com/stocks/rl/history/) |
| AME | 247.74 | 245.41 | [History](https://stockanalysis.com/stocks/ame/history/) |
| SNA | 367.71 | 371.80 | [History](https://stockanalysis.com/stocks/sna/history/) |
| ABNB | 151.39 | 161.81 | [History](https://stockanalysis.com/stocks/abnb/history/) |
| NTAP | 197.24 | 192.91 | [History](https://stockanalysis.com/stocks/ntap/history/) |
| PAYX | 101.59 | 114.53 | [History](https://stockanalysis.com/stocks/payx/history/) |
| IBKR | 89.82 | 91.88 | [History](https://stockanalysis.com/stocks/ibkr/history/) |
| HIG | 125.69 | 128.73 | [History](https://stockanalysis.com/stocks/hig/history/) |
| ALLE | 152.48 | 153.95 | [History](https://stockanalysis.com/stocks/alle/history/) |
| AIZ | 261.86 | 271.08 | [History](https://stockanalysis.com/stocks/aiz/history/) |

The 22 September observations address the separate lineage auditor's discovery of a broad missing-day outage. They are a candidate repair layer with attribution; they do not fix the remaining affected universe or validate the full eleven-year history. Never fill a missing trading day with zero return merely because the download failed.

### A concrete dividend-vintage trap

RL's current table shows 24 September **raw close $351.86 but adjusted close $350.86**, and 22 September **raw $346.06 but adjusted $345.08**. The original snapshot ended before the 25 September dividend adjustment. Mixing today's adjusted $345.08 into that frozen series would manufacture a return distortion. The issuer announced a $1 quarterly dividend on 11 September, payable 9 October to holders of record on 25 September; the [original issuer declaration](https://corporate.ralphlauren.com/pr_260911_QuarterlyDividend.html?q=lauren+ralph) and [dated ex-dividend table](https://www.investing.com/equities/polo-ralph-laur-dividends) support the event. Reconstruct and freeze the corporate-action adjustment vintage before merging history.

IBKR's [issuer filing](https://investors.interactivebrokers.com/mkt/getSecFiling.php?date_added=2025-05-08+08%3A56%3A51.252628&id=101) specifies four-for-one split trading from 18 June 2025. Cached adjusted closes around the event are $52.1277, $51.7572, $52.3116 and $51.0586 for June 16, 17, 18 and 20: no spurious 75% fall is present in that local sample. This is an event sanity check, not a complete corporate-action reconciliation. Historical EPS and share counts must use the same split convention; issuer common shares and ownership-adjusted parent earnings cannot be mixed casually.

## The valuation denominator must be explicit

All fourteen external forecast pages say their EPS/P/E use non-GAAP adjusted earnings. The original cache does not retain the underlying adjustment dictionary or analyst submission timestamps. The pages attribute financial forecasts to S&P Global, whereas the original Yahoo upstream is not documented in the source bundle. Agreement across those two distributors is useful corroboration, **not proof of independent estimate collection**.

| Stock | Current FY | Cached current EPS | Cached next EPS | Current-FY P/E | Next-FY P/E | External current / next EPS |
|---|---|---:|---:|---:|---:|---:|
| NVDA | FY2027, January end | 9.307 | 15.683 | 24.13 | 14.32 | 9.31 / 15.68 |
| CPAY | FY2026, December end | 27.393 | 31.448 | 14.61 | 12.73 | 27.39 / 31.45 |
| AMP | FY2026, December end | 46.527 | 51.668 | 10.43 | 9.39 | 46.53 / 51.67 |
| RL | FY2027, March end | 18.898 | 20.914 | 18.62 | 16.82 | 18.90 / 20.91 |
| AME | FY2026, December end | 8.339 | 9.585 | 29.71 | 25.85 | 8.34 / 9.59 |
| SNA | FY2026, December/January week-end | 19.830 | 21.360 | 18.54 | 17.21 | 19.82 / 21.34 |
| ABNB | FY2026, December end | 5.313 | 6.245 | 28.49 | 24.24 | 5.30 / 6.19 |
| NTAP | FY2027, April end | 10.006 | 11.121 | 19.71 | 17.74 | 10.01 / 11.12 |
| PAYX | FY2027, May end | 5.961 | 6.400 | 17.04 | 15.87 | 5.96 / 6.39 |
| MSFT | FY2027, June end | 19.760 | 23.676 | 25.20 | 21.03 | 19.76 / 23.68 |
| IBKR | FY2026, December end | 2.707 | 3.196 | 33.19 | 28.10 | 2.71 / 3.20 |
| HIG | FY2026, December end | 12.758 | 13.678 | 9.85 | 9.19 | 12.76 / 13.68 |
| ALLE | FY2026, December end | 8.956 | 9.773 | 17.02 | 15.60 | 8.96 / 9.77 |
| AIZ | FY2026, December end | 22.265 | 23.433 | 11.76 | 11.17 | 22.27 / 23.43 |

Each row's direct source is `https://stockanalysis.com/stocks/{lowercase ticker}/forecast/`, recorded explicitly in the JSON and CSV. Illustrative primary-source fiscal anchors: [NVDA actual quarter ended July 26, FY2027](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/), [Microsoft FY2026 ended June 30](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast), and [RL actual FY2026 ended March 28](https://investor.ralphlauren.com/frequently-asked-questions). Vendor forecast tables use normalized month ends for week-based calendars; their future exact day is not issuer-confirmed.

**Three cache mismatches matter.** ABNB's cached `info.forwardEps=6.18687` matches the external 6.19 more closely than `trend[+1y]=6.24489`; PAYX's 6.39435 similarly matches 6.39 more closely than trend 6.40014. SNA's 21.39375 info value, 21.36010 trend value and external 21.34 differ. The report must not silently mix the cheapest ratio from one snapshot with growth from another. Small numerical differences can be ordinary timing or coverage differences; their cause is not established here.

**Period correction:** These next-FY ratios are not NTM ratios. Build NTM earnings from a single timestamped quarterly consensus covering the next four quarters, then apply a clearly documented partial-quarter convention if needed. Linear weighting of two annual EPS figures is only a seasonality-blind approximation and must not be labeled a verified NTM series.

**Vintage correction:** AME, PAYX and MSFT pages explicitly showed updates on 25 September, after the frozen cutoff. RL showed 24 September without a field-level timestamp. Other page updates ranged from 20 August to 22 September. These are page metadata, not a documented EPS-vintage contract. Even a page update before cutoff cannot prove that all fields were known at cutoff. The table is an external-display cross-check accessed on 26 September, not an as-of replay.

**Dispersion correction:** Original next-FY low/high/count values exist for only seven finalists in `deep.pkl`; absent for AMP, RL, AME, NTAP, PAYX, IBKR and ALLE. The public site's next-FY dispersion is gated. Its visible table analyst count is not certified as the EPS denominator count. NVDA's cached next-FY range $9.80–$18.746 across 53 analysts corresponds to 22.92x–11.98x at $224.58; that is coverage dispersion, not a prediction interval. The public current-FY range is only $9.01–$10.10, which must not substitute for next-FY uncertainty.

**Identity correction:** NVDA's original metadata says `prevName=Usual Stablecoin` and name-change date 24 September. Other fields identify NVIDIA equity on Nasdaq in USD. Quarantine the anomalous metadata and require issuer CIK + exchange/MIC + share class + security identifier mapping. Do not propagate a metadata anomaly into an unsupported claim that all NVIDIA earnings are false.

## Deep provider documentation: what it does and does not promise

**FMP.** [Stable reference](https://site.financialmodelingprep.com/developer/docs) separates ordinary historical prices, non-split-adjusted prices and dividend-adjusted prices, and exposes estimate mean/low/high/count by annual or quarterly period. Its standard analyst endpoint parameters do not document a historical as-of selector; its [FAQ](https://site.financialmodelingprep.com/de/faqs?code=statements) clarifies that estimate dates are period-end dates and that historical snapshots must be requested for older forecast vintages. A reference to snapshots does not demonstrate our account can retrieve them. The stable reference lists historical constituent changes while the same FAQ says complete historical S&P constituent lists/add-exit dates are unavailable. Obtain actual coverage, effective-date rules and missing-event diagnostics before asserting survivorship-free backtests. As-reported endpoints are useful, but their label alone does not prove all original/amended vintages are preserved.

**Financial Datasets.** The deeper [provenance documentation](https://docs.financialdatasets.ai/data-provenance) names **Databento** for equity prices and direct SEC EDGAR parsing for statements. [Earnings schema](https://docs.financialdatasets.ai/api/earnings) includes accession, filing URL and filing datetime, which are suitable lineage keys. Its descriptions of macro series explicitly say latest revised values are stored, so do not infer historical publication vintages. No authenticated Financial Datasets output was acquired for this audit. Its provider documentation improves source selection but does not validate any portfolio number.

## Required weekly data gate and minimum missing export

For every actionable field retain security identity, source endpoint/accession, raw response/file hash, source period, currency/unit, accounting definition, publication time, ingestion time, forecast vintage, effective corporate-action date and transformation. A second reviewer must recompute the dependent valuation rather than merely approve the first review's prose.

The minimum outstanding estimate export is **all 14 identifiers, FY0/FY1 and the next five quarterly EPS estimates, GAAP/adjusted definitions, mean/median/low/high/analyst count, contributor timestamps and a frozen 24 September 2026 20:00 UTC vintage**. Keep the fresh weekly snapshot separately. Also export a complete raw-close/adjusted-close/corporate-action history covering the risk window, with session timezone and missing-record flags. Do not purchase a feed on the strength of a generic endpoint name: first test these fields and date semantics on NVDA, PAYX, RL and IBKR.

No new purchase is cleared by this market-data audit. Closing-price corroboration is now substantially better; estimate lineage, economic underwriting and strategy validation remain separate approval gates.
