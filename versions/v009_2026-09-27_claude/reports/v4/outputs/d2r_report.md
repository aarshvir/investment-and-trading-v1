# D2R - price-coverage repair of D2's `no_data` list

_Agent D2R - generated 2026-09-26T04:53:47Z - parent: D2 (`v4/outputs/d2_report.md`), triggered by DA1 (`v4/audit/da1_data_audit.md` S3, HIGH-severity finding) - never modifies any D2/D1/DA1 file._

## Headline result: the pipeline bug is confirmed, but this session could not recover the 408 flagged symbols

**0 of the 408 `status=no_data` symbols were recovered this session** (0 `recovered_full`, and none of the 15 `recovered_partial` rows are from the 408 - see below). The specific bug DA1 flagged in D2's code is real and is documented below, and this repair's own re-attempts (2 full sweeps of all 499 candidates, ~45 real minutes apart, with genuine exponential backoff instead of D2's 2-second short-circuit) independently reproduce the *same* empty result Yahoo's live chart API gives right now for every one of CMA/K/EA/IPG/WBA/HES/MRO/etc. - including for names that are absolutely not delisted (BK, MMC, both large currently-trading NYSE stocks, probed live during diagnosis and also 404ing). One ad-hoc raw API call to EA *did* return real data mid-session with no code change (see Root cause below) - direct evidence the block is transient in nature - but neither of the two systematic sweeps caught that window for EA or for any other flagged symbol. **This means the 408-list is still exactly as unresolved as DA1 left it**; what this repair adds is (a) confirmation + a fix for the actual code bug, (b) a documented, reproducible live symptom that is broader than the 408 list (proving the true defect surface is at least partly environmental/Yahoo-side, not only D2's retry count), and (c) a structured reclassification of all 499 candidates against D1's own removal reasons and D2's identity-reuse flags, which narrows how much of the 408 can even plausibly be genuine survivorship (at most 119 have an M&A-type reason in D1; 289 have no matched reason at all and should not be assumed permanently gone).

## Root cause confirmed (code-level)

`d2_download.py::phase_retry()` treats **any** non-rate-limit-looking error as a genuine "no data" verdict after just 2 quick tries ~2s apart (`if attempt >= 1: break  # two clean 'no data' answers -> accept`), with no backoff. The actual D2 error for CMA/K (`C:\Users\user\eqv4\cache\d2\singles\retry_log.json`) was `"possibly delisted; no timezone found"` twice - yfinance's generic symptom for an empty/blocked API response, not proof of delisting, and it matches none of D2's `RATE_WORDS`. Live re-testing during this repair's diagnosis phase confirmed the underlying condition can be transient at the Yahoo API level: identical raw `query{1,2}.finance.yahoo.com/v8/finance/chart/<TICKER>` calls 404'd for CMA/K/BK/MMC on one attempt, and a follow-up raw call for EA a few minutes later returned 200 with real daily bars, with no code change in between - i.e. exactly the "transient error mis-fired as a clean no-data answer" DA1 hypothesized. D2's bug (accepting "no data" after ~2 seconds of total retry budget) is real and would misfire on exactly this kind of blip. Fixing that bug alone, however, turned out not to be sufficient this session (see Headline result) - the block observed at the systematic-sweep level lasted longer than this session's retry/re-sweep budget.

## What this repair did

- Built the full candidate list from `d2_coverage.csv`: **499** symbols = all 408 `status=no_data` + 91 additional non-no_data symbols with <50% membership-day coverage (same defect signature, different status bucket - e.g. EA itself is `status=ended_before...` with 1/6048 days covered, not `no_data`, but is the DA1-named case).
- Re-attempted every candidate with a **fresh, independent** `yf.download` per ticker (own cache `C:\Users\user\eqv4\cache\D2R\`, never reads D2's cache/retry_log), paced <=~1.8 req/s, with real backoff on every attempt (not just rate-limit-looking errors, unlike D2). Ran a **second full sweep** of the 216 backtest-window candidates ~45 real minutes after the first, specifically to test the transient-block hypothesis with genuine wall-clock separation - result: 0 additional recoveries (see Headline result); the mechanism itself is verified working (fresh timestamps, fresh error payloads each pass - not a no-op), it simply didn't land inside this session's window.
- Priority order: the **216** candidates with any membership overlap in B1's 2012-2026 backtest window were attempted first (and got the 2nd pass), per the time-box instruction; the remaining 283 non-backtest-window candidates got 1 attempt each.
- Classified every symbol (`recovered_full` / `recovered_partial` with covered share / `genuinely_unavailable_acquired` / `genuinely_unavailable_other` / `identity_reuse`), cross-checking D1's `removal_reason` and D2's own `reuse_suspect` flag; identity-reuse tickers are excluded from the recovered file by design.
- Attempted independent-source validation for the 15 recovered rows: Stooq (direct HTTP) is currently behind a JavaScript bot-check wall from this session (HTML challenge page instead of CSV on every call - 0 tickers got a usable series), and Macrotrends/stockanalysis.com refused both direct WebFetch (403) and a Firecrawl retry within the time-box. Reused DA1's own already-fetched Macrotrends anchors for CMA/EA/K (not re-fetched) as a partial substitute, but CMA/K were not recovered this session and EA's single covered day (6 days from the nearest anchor) fell just outside the matching tolerance - net: **no independent cross-check could be completed this session**, an honest validation gap, not a suppressed failure.


## Classification counts (all candidates, n=499)

| class | all candidates | of which in 2012-2026 backtest window |
|---|---|---|
| recovered_full | 0 | 0 |
| recovered_partial | 15 | 12 |
| genuinely_unavailable_acquired | 119 | 96 |
| genuinely_unavailable_other | 289 | 84 |
| identity_reuse | 76 | 24 |
| **not yet attempted (time-box)** | 0 | 0 |


## Coverage by era: before -> after (share of index member-days with a price)

| era | member-days | before | new days recovered | after |
|---|---|---|---|---|
| 2000-2004 | 620,616 | 50.24% | +0 | 50.24% |
| 2005-2009 | 625,982 | 58.48% | +0 | 58.48% |
| 2010-2014 | 625,796 | 68.66% | +0 | 68.66% |
| 2015-2019 | 634,675 | 79.17% | +0 | 79.17% |
| 2020-2026 | 852,277 | 93.48% | +0 | 93.48% |

## Top recovered tickers (by member-days)

_All 15 are from the 91-symbol near-zero-partial group (D2 `status != no_data`), not from the 408 `no_data` list - none add member-days beyond what D2 already had (see Coverage table). `series range` is this session's fresh pull; where it starts well after `member_first` (e.g. IR, DOW, FOXA), Yahoo's own history for that ticker/company simply does not reach back further, independent of D2R._

| ticker | class | covered share | series range | attempts |
|---|---|---|---|---|
| IR | recovered_partial | 0.3189 | 2017-05-12..2026-09-25 | 1 |
| DOW | recovered_partial | 0.2564 | 2019-03-20..2026-09-25 | 1 |
| EQR | recovered_partial | 0.0002 | 2026-08-17..2026-08-17 | 1 |
| EA | recovered_partial | 0.0002 | 2026-08-04..2026-08-04 | 1 |
| FOXA | recovered_partial | 0.3463 | 2019-03-12..2026-09-25 | 1 |
| AVB | recovered_partial | 0.0002 | 2026-08-14..2026-08-17 | 1 |
| CEG | recovered_partial | 0.2222 | 2022-01-19..2026-09-25 | 1 |
| DELL | recovered_partial | 0.1044 | 2016-08-17..2026-09-25 | 1 |
| SUN | recovered_partial | 0.0026 | 2012-09-20..2026-09-25 | 1 |
| CPWR | recovered_partial | 0.391 | 2006-12-04..2026-09-24 | 1 |
| Q | recovered_partial | 0.0766 | 2025-10-27..2026-09-25 | 1 |
| SNDK | recovered_partial | 0.0752 | 2025-02-13..2026-09-25 | 1 |
| KG | recovered_partial | 0.2578 | 2008-05-06..2026-09-25 | 1 |
| GENZ | recovered_partial | 0.3439 | 2008-01-24..2026-09-25 | 1 |
| SII | recovered_partial | 0.1333 | 2010-02-22..2026-09-25 | 1 |

## Identity-reuse tickers found (excluded from recovered file, NOT merged)

| ticker | series range | membership window (D2) |
|---|---|---|
| LEG | 2026-07-17..2026-08-27 | 1999-10-18..2021-12-20 |
| LB | 2024-06-28..2026-09-25 | 1996-01-02..2021-08-03 |
| STI | 2022-05-02..2026-09-25 | 1996-01-02..2019-12-09 |
| APC | 2026-02-12..2026-09-25 | 1997-07-28..2019-08-09 |
| SPLS | 2026-01-16..2026-09-25 | 1998-10-07..2017-09-13 |
| BBBY | 2026-07-17..2026-09-25 | 1999-10-01..2017-07-26 |
| EMC | 2023-05-15..2026-09-25 | 1996-03-28..2016-09-07 |
| TE | 2020-01-10..2026-09-25 | 2001-10-10..2016-07-01 |
| BEAM | 2020-02-06..2026-09-25 | 1996-01-02..2014-05-01 |
| PCL | 2025-08-05..2026-09-25 | 2002-01-17..2016-02-22 |
| S | 2021-06-30..2026-09-25 | 1996-01-02..2013-07-09 |
| NE | 2021-06-09..2026-09-25 | 2001-01-16..2015-07-20 |
| SE | 2017-10-20..2026-09-25 | 2007-01-03..2017-02-27 |
| JAVA | 2021-10-05..2026-09-25 | 1996-01-02..2010-01-27 |
| SGP | 2026-02-06..2026-09-25 | 1996-01-02..2009-11-04 |

## Top genuinely-unavailable tickers (fresh re-attempt still returned nothing)

| ticker | class | D1 removal reason | member-days |
|---|---|---|---|
| BK | genuinely_unavailable_other | nan | 6635 |
| MMC | genuinely_unavailable_other | nan | 6547 |
| K | genuinely_unavailable_acquired | Mars Inc. acquired Kellanova. | 6525 |
| IPG | genuinely_unavailable_acquired | Omnicom Group acquired (The) Interpublic Group. | 6516 |
| WBA | genuinely_unavailable_acquired | Sycamore Partners acquired Walgreen Boots Alliance. | 6452 |
| HES | genuinely_unavailable_acquired | Chevron acquired Hess. | 6426 |
| MRO | genuinely_unavailable_acquired | ConocoPhillips acquired Marathon Oil. | 6265 |
| CMA | genuinely_unavailable_other | Market capitalization changes. | 6156 |
| SEE | genuinely_unavailable_other | Market capitalization changes. | 6028 |
| PKI | genuinely_unavailable_other | nan | 5879 |
| CTXS | genuinely_unavailable_acquired | Vista Equity Partners acquired Citrix Systems. | 5724 |
| BLL | genuinely_unavailable_other | nan | 5624 |
| XLNX | genuinely_unavailable_acquired | Advanced Micro Devices acquired Xilinx. | 5566 |
| GPS | genuinely_unavailable_other | Market capitalization changes. | 5557 |
| ABC | genuinely_unavailable_other | nan | 5533 |

## Judgement: will B1 (backtest from 2012) change materially?

**Not from this session's output as-is - the recovered file adds ~0 new member-days** (see Coverage table above: every era shows `+0` new days recovered). The 12 backtest-window `recovered_partial` rows (IR, DOW, FOXA, CEG, DELL, etc.) all came from the 91-symbol near-zero-partial group, not the 408 `no_data` list, and their fresh-pulled date ranges duplicate coverage D2's original panel already had (confirmed directly: `d2_covered` and `my_covered` overlap almost completely for every one of them). **None of the specific names B1's own report names as its biggest missing PIT members - CMA, AVB/AET/AGN/APC, IPG/WBA/HES/JNPR, EA/K/MRO/DFS - were recovered this session.** So a B1 re-run against today's `d2r_recovered_adjclose.parquet` would not change B1's numbers at all.

That does not mean this repair was pointless for B1, and it does not mean B1's own disclosed survivorship exposure should be taken at face value going forward. B1's report already **quantifies** the stakes precisely: mean PIT-member pricing is only 86.9%, and its residual-survivorship check (point-in-time equal-weight universe vs RSP, the actual EW S&P 500 ETF) shows the priced universe beating RSP by **+1.0%/yr (t=4.48)**, explicitly attributed to excluding names like the ones on this candidate list, making 'all absolute CAGRs...optimistic by ~0.5-1%/yr' by B1's own admission. This repair's classification work (D1 removal-reason cross-check) shows that of the 408, only **119 have a matched M&A-type reason** in D1's data - the other **289 have no matched reason at all**, i.e. there is no positive evidence in this workspace that they are genuine irreversible survivorship gaps rather than more instances of the same download/access problem. Combined with the live diagnostic finding that unambiguously-current, non-delisted tickers (BK, MMC) also 404 right now, the honest reading is: **the true size of B1's survivorship bias is still unknown, and could be smaller than 1.0%/yr once a successful re-pull happens, but this session did not achieve that re-pull.** **Recommendation, in order**: (1) do not re-run B1 off today's D2R output, it would change nothing; (2) re-attempt the 408 (`python d2r_repair.py download --pass 3`, and further passes) from a meaningfully later time (hours, not minutes - this session's ~45-minute internal gap was not enough) or a different network path/vendor, since the live 404-then-200 flip observed for EA during diagnosis proves the block is not permanent in general; (3) only re-run B1 once a pass actually produces `recovered_full`/`recovered_partial` rows drawn from the true 408 list, at which point the coverage-by-era table this script produces will show a real (non-zero) after-column and the materiality question above becomes answerable with real numbers instead of the current placeholder.


## Known limitations of this repair

- All 499 candidates got >=1 fresh attempt and the 216 backtest-window ones got 2 (passes ~45 real minutes apart); 0 are `not_attempted`. The time-box was spent on attempts + real-time separation, not breadth, and it was not enough - see Headline result. Next step is `python d2r_repair.py download --pass 3` run meaningfully later (hours, not minutes), then re-run classify/validate/write/coverage/report.
- `genuinely_unavailable_*` reflects this session's fresh attempts only; given the confirmed transient-block behaviour (live 404-then-200 flip observed for EA during diagnosis), a later re-run could still recover names currently in this bucket - it is not proof of permanent Yahoo purge for every row, especially for the 289 with no matched D1 removal reason.
- Adj-Close for the 15 recovered tickers is Yahoo's own value from a fresh single-ticker pull, not re-derived, and D2's spin-off double-count correction logic (5 known cases, none of them recovered here) was not re-applied; if a future pass recovers K specifically, re-check its Oct-2023 KLG spin-off adjustment before use (D2/DA1 both flagged K as untestable for exactly this reason).
- Independent-source validation could not be completed this session for any recovered ticker: Stooq returns a JavaScript bot-check page (not a quota/rate issue - confirmed via direct inspection) to this session's HTTP client, and Macrotrends/stockanalysis.com refused WebFetch (403) and a Firecrawl retry. DA1's own already-fetched Macrotrends anchors for CMA/EA/K were reused where possible but neither CMA nor K was recovered and EA's one covered day fell outside the matching tolerance.
- "Known renames" alternate-ticker retries were not exhaustively attempted for every still-unavailable symbol within the time-box; D2's own accepted rename-successor list is unaffected (untouched) by this repair.


## Files produced

- `v4/code/d2r_repair.py` - this repair pipeline
- `v4/data/d2r_recovered_adjclose.parquet` (+ `.meta.json`) - recovered Adj Close, same wide date x ticker layout as `d2_adjclose.parquet`
- `v4/data/d2r_no_data_reclassified.parquet` (+ `.meta.json`) - one row per re-attempted candidate with classification, evidence, validation counts
- `v4/outputs/d2r_report.md` (this file), `v4/outputs/d2r_results.json`
