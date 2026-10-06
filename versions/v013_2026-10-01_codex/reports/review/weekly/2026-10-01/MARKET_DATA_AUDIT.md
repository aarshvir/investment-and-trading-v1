# September 30, 2026 price and source audit

**Cutoff:** completed US regular session of September 30, 2026. **Prepared:** October 1, 2026 Dubai. These are research reference prices, not executable orders or a guaranteed official closing-auction tape.

The candidate scope is exactly **90 unique USD tickers**: the frozen v011 twenty, the frozen v012 fourteen, fifty eligible near misses selected by the archived v011 original rank for *coverage*, and large-cap/benchmark comparators. Rank inclusion does not imply investment merit. The broader archived universe has 503 September 25 USD rows. The 90-name sweep includes benchmarks and is **not a complete fresh 503-name universe**; do not subtract 90 from 503 to claim an exact constituent count without checking membership. The scope is not a claim that every S&P 500 constituent received current prices or fresh filing diligence.

The public Yahoo daily chart returned a dated September 30 regular-session OHLC row and matched USD ticker/currency for **90/90**. Its unadjusted `close`, not the separately retained `adjclose`, is the valuation input. The public Cboe delayed-quote endpoint returned a same-session observation for **32/90**; **58/90 requests were rate limited**. For 32 overlaps, the maximum absolute relative close difference is **0.06043%** and all are below 0.1%. Two public endpoints are useful corroboration, but they do not amount to an independent official exchange close or a live ask. The Cboe value is a late last-sale observation; the Yahoo value is a daily close. We have not averaged unlike fields. The complete `MARKET_RECONCILIATION.csv` records time, source URLs, raw payload SHA-256, source difference, daily range, currency and failure status. The builder verifies each available payload hash byte-for-byte and rejects closes outside their OHLC low/high.

| Ticker | Yahoo Sep 30 close | Cboe late observation | Difference | Prior v012 ceiling | Price gate only |
|---|---:|---:|---:|---:|---|
| AMP | $492.35 | $492.20 | 0.030% | $500.00 | Below |
| PAYX | $98.50 | $98.50 | 0.000% | $101.80 | Below |
| MSFT | $512.90 | $512.90 | 0.000% | $500.00 | Above |
| NVDA | $228.38 | $228.38 | 0.000% | $215.00 | Above |
| HIG | $122.36 | $122.42 | 0.049% | $120.00 | Above |
| ADP | $258.06 | $258.06 | 0.000% | No funded v012 limit | Unfunded |
| TJX | $132.31 | $132.39 | 0.060% | No funded v012 limit | Unfunded |
| LH | $308.11 | $308.11 | 0.000% | No funded v012 limit | Unfunded |

The StockAnalysis web history snippets for AMP and several other names conflicted with their own displayed quote/vintage: its AMP September 30 historical row of $495.74 is below that row's stated $495.98 low. The same site showed a September 29 AMP close inconsistent with both Yahoo and Cboe's `prev_day_close` of $497.32. We rejected that row rather than laundering it into a third confirmation. These observations do not establish that either accepted public feed is perfect.

The **14 v012 company scenarios were repriced** to the new Yahoo reference close with prior annual dividends, normalized earnings, terminal P/E, 30% dividend withholding, 25bp entry and 25bp exit costs. No operating forecast, fund holding or reserve yield was relabeled current. The scenario file reproduces archived September 25 IRRs exactly before applying the new prices. A live quote, applicable trading currency, fees, current fund look-through and event calendar are still required before any purchase decision. [Cboe delayed quote specification](https://cdn.cboe.com/resources/membership/Cboe_Global_Cloud_Specification.pdf) and [Yahoo chart endpoint example](https://query1.finance.yahoo.com/v8/finance/chart/AMP?range=5d&interval=1d) explain the fields being compared; raw responses with timestamps and hashes are preserved locally.
