# D4 — Live S&P 500 snapshot at the 2026-09-25 close, NTM calendarization and data validation

Agent D4 · market-data cutoff US close Friday 2026-09-25 · Yahoo pull 2026-09-25T20:23:25Z → 2026-09-25T20:39:38Z (UTC, i.e. 23–40 minutes after the 16:00 ET close) · independent quotes 2026-09-25T20:36:06Z → 2026-09-25T20:49:03Z UTC · report generated 2026-09-25T20:59:40Z

## 1. Answer first

1. **Snapshot complete: 503/503 constituents**, 269 columns, in `v4/data/d4_live_snapshot.parquet`. Every price is the 2026-09-25 regular-session close (`regularMarketTime` = 2026-09-25 ~20:00 UTC for all 503; **0 stale**).
2. **Prices independently confirmed for all 503.** Every Yahoo close is within 0.5% of the Cboe `close` (503/503; 501 exact) **and** of CNBC's 16:00 ET last (503/503; 498 exact). The largest gap is 0.083%. Stooq, the source named in the brief, now answers scripted requests with a JavaScript proof-of-work "verify your browser" page. That is a bot challenge, so it was **not** solved or bypassed; Cboe and CNBC were used instead.
3. **Yahoo's `forwardPE` is price ÷ next-fiscal-year ('+1y') consensus EPS, not a next-twelve-months (NTM) multiple.** `forwardEps` equals the +1y consensus exactly for 433/503 names and within 3% for 469/503. It matches the current-year (0y) consensus for only 5, and is more than 3% away from both for 26 (these are basis or staleness errors; see §3.6).
4. **Yahoo forward P/E vs calendarized NTM P/E: 55/497 names (11.1%) differ by more than 10%.** The median ratio of Yahoo to NTM P/E is 0.975, and Yahoo's figure is lower for 90% of names, so it systematically understates the multiple. The error grows with the share of the current fiscal year still to run (f). It exceeds 10% for 2% of names with f ≤ 0.25, 9% with 0.25–0.5 (most December year-ends), 26% with 0.5–0.75 and 40% with f > 0.75. Among the 366 names whose consensus passes every consistency check, 16 differ by more than 10%. These are pure horizon effects: ORCL 12.5x (Yahoo) vs 15.1x (NTM), MSFT 21.8x vs 24.9x, and NVDA 14.4x vs 16.7x.
5. **v3 portfolio: the NTM P/E is higher than Yahoo's forward P/E for all 14 holdings** (median +3.4%). The largest gaps are MSFT +14.4%, NVDA +16.6% and ORCL-like June/May fiscal years (PAYX +4.9%, NTAP +6.3%).
6. **Consensus data quality, graded per ticker (`ntm_quality`): 366 ok, 92 caution, 45 unreliable.** The unreliable group includes 28 REITs, where EPS is not the valuation earnings measure (FFO is). It also includes names whose Yahoo annual row contradicts its own quarterly rows by more than 25% (for example CDNS, where the FY0 row looks GAAP and the quarterly and FY1 rows look adjusted), names with a +1y row whose 'year-ago' figure ≠ the 0y consensus (PANW, DELL, REGN), and names with negative or missing EPS.
7. **Market cap: 455/503 are within 3% of price × `sharesOutstanding`, and all 503/503 match price × `impliedSharesOutstanding`.** The 48 exceptions are multi-class, UP-C or operating-partnership-unit structures (GOOGL/GOOG, BRK-B, IBKR, BX, SPG, …). Yahoo's `marketCap` counts all classes and units; its `sharesOutstanding` counts only the listed class.
8. **SEC XBRL cross-check (CY2025 frames vs Yahoo FY2025, December year-ends): revenue within 2% for 335/353 (94.9%); net income 327/350 (93.4%).** The largest gaps come from mismatched concepts or definitions: banks' fee-only contract revenue, REIT lease revenue, excise taxes, non-controlling interests and discontinued operations. They also include **SEC-side XBRL scale errors: PG&E net income is tagged as $2,593, Arista as $3,511, and ConEd and Schwab are 1,000× too small. In these cases Yahoo is right.**
9. **Fiscal calendars: the Yahoo FY0 end month agrees with SEC for 500/503.** All three exceptions are explained. AMCR (8-K Item 5.03, 2026-05-06) and FDX (8-K Item 2.02, 2026-07-21) moved their fiscal year-ends to 31 December, so Yahoo is right and the SEC metadata is stale. BRO's SEC `fiscalYearEnd` field is wrong. Yahoo `lastFiscalYearEnd` matches the latest 10-K period for 497/500; the 3 misses (AZO, CPRT, COST) have released results but not yet filed the 10-K.
10. **Metadata quarantine.** `prevName` is populated for 45 names. `nameChangeDate` **always equals the retrieval date** (2026-09-25 here, 2026-09-24 in the legacy file), so it is a fetch stamp, not an event date. 4 `prevName` values are not company names: **NVDA 'Usual Stablecoin' (still present), CPAY 'VaporWallet', NFLX 'VIVEK' and TFC 'Supernova'**. They look like crypto-token names bleeding into equity metadata. Both fields should be quarantined. Separately, yfinance's `calendar` converts epoch times using the machine's local timezone (UTC+4), which **shifts 218 after-close earnings dates one day late**. `next_earnings_date` in the snapshot uses America/New_York.
11. **Change log vs the legacy snapshot (2026-09-24, one session earlier): 0/14 v3 names have a consensus EPS or target change above 2%.** The largest price moves are MSFT +3.7% and ABNB +4.0%. PAYX, which reported on 2026-09-23, shows a 30-day FY0 revision of -0.32%. The large recent revisions are NVDA FY1 +21.7% and NTAP FY1 +11.6% over 30 days. HIG has 17 downward and 2 upward FY1 revisions in 30 days.
12. **Corporate events (best-effort, evidence in `d4_corporate_events.csv`).** Constituents that are targets or merging parties in pending deals: WBD (Paramount Skydance; SC 14D-9 and merger proxy), KVUE (Kimberly-Clark), TECH (Merck KGaA; holders approved 2026-09-23), AES (GIP/EQT consortium), NSC (Union Pacific; STB review) and D (all-stock combination with NEE; NEE filed an S-4). Merger-proxy flags that are *not* pending takeovers: DVN (Coterra merger completed 2026-05-07; an activist letter on 2026-09-23 urges a sale) and CCL (DLC unification). MGM: People Inc. dropped its bid on 2026-09-24. Recent or planned separations: FDXF and HONA (completed 2026 spins), CTVA (Vylor), FLEX, GPC, SOLV, MDT (MiniMed) and KDP. AME's $5bn Indicor acquisition closed on 2026-08-26 (8-K 2.01 and press release).

## 2. What was done

* **Universe**: Wikipedia *List of S&P 500 companies*, table 1 (`id=constituents`): 503 lines, 500 CIKs (GOOGL/GOOG, FOXA/FOX and NWSA/NWS share CIKs), converted to Yahoo tickers (BRK-B, BF-B). The page no longer carries the 'selected changes' table. Output: `v4/data/d4_universe.csv`.
* **Yahoo pull** (`d4_fetch_yahoo.py`, yfinance 1.7.0, 5 threads, global limit of 8 requests/s, exponential backoff, one pickle per ticker in `C:\Users\user\eqv4\cache\d4\yahoo\`). Per ticker: `info`, `earnings_estimate`, `revenue_estimate`, `eps_trend`, `eps_revisions` (plus the raw earningsTrend list, which carries each period's `endDate`), `earnings_history`, `get_earnings_dates(limit=16)`, `analyst_price_targets`, `recommendations_summary`, `upgrades_downgrades`, `calendar` (plus raw calendarEvents epochs), annual `income_stmt`, and news and press-release headlines. UTC start and end times are recorded per ticker (`retrieved_utc_start/end`). Only 404s (no data) remained: FOX has no consensus of its own, so the FOXA consensus was borrowed and flagged (`estimates_from_sibling`); ERIE has no upgrades or downgrades; NEM's press-release tab failed.
* **Independent prices** (`d4_fetch_indep_prices.py`): Cboe delayed-quotes JSON (`close`; 503 single-symbol requests, slowed to 1 every 2.5 s after Cloudflare rate-limited 2 per second) and CNBC's quote service (`last`, `last_time`, `previous_day_closing`, `eps`, `sharesout`, `feps`, `fpe`; batched). One Stooq probe is kept as evidence of the block.
* **SEC** (`d4_fetch_sec.py`; SEC User-Agent, ≤2 requests/s): XBRL frames for CY2025 (Revenues, RevenueFromContractWithCustomerExcludingAssessedTax, NetIncomeLoss, plus the diagnostics RevenueFromContractWithCustomerIncludingAssessedTax, RevenuesNetOfInterestExpense, ProfitLoss, NetIncomeLossAvailableToCommonStockholdersBasic), and submissions JSON for all 500 CIKs. Three 8-K documents were read to settle fiscal-calendar questions (AMCR 2026-05-06, AMCR 2026-01-15, FDX 2026-07-21).
* **Build and validation**: `d4_build_snapshot.py` (fields, NTM, quality grade), `d4_validate.py`, `d4_events.py`, `d4_changelog.py` and `d4_report.py`. Re-running the chain reproduces every number here from the cache.

## 3. NTM calendarization (the key fix)

### 3.1 Rule

* **FY0** is the current, not-yet-reported fiscal year, i.e. the period Yahoo labels `0y`. Its end date comes from the raw earningsTrend `endDate` of `0y`. That is exactly the period the FY0 consensus refers to, and it is normalised to month-end (NVDA 2027-01-31, where the true year-end is the last Sunday of January). Cross-checks: `info.nextFiscalYearEnd` (= `lastFiscalYearEnd` + 1 year) must agree within 20 days; `mostRecentQuarter` must fall between `lastFiscalYearEnd` and the FY0 end; and the FY0 end month is compared with SEC. Disagreements are resolved from SEC primary documents (§1 item 9). The only manual override is HONA, a 2026 spin-off: its calendar fiscal year is taken from SEC because Yahoo's label reads Jan-2027.
* **f** = share of FY0 still to run at 2026-09-25 = clip((FY0_end − 2026-09-25) / (FY1_end − FY0_end), 0, 1). f = 0 when FY0 has ended but is not yet reported (ACN, FDS, JBL, MU, FDXF). In that case NTM = FY1.
* **EPS_NTM = f·EPS_FY0 + (1−f)·EPS_FY1** and **REV_NTM = f·REV_FY0 + (1−f)·REV_FY1**, using the earnings_estimate and revenue_estimate averages. `pe_ntm` = price/EPS_NTM (NaN with a reason when EPS_NTM ≤ 0 or estimates are missing), `ev_sales_ntm` = EV/REV_NTM, plus `pe_fy0` and `pe_fy1`.
* Two diagnostics that are not the primary measure: **quarter-aware NTM** = (FY0 − EPS already reported for FY0 quarters) + FY1·q/4, where q = FY0 quarters reported; and **quarterly-sum NTM** = remaining 0q/+1q estimates + FY1·q/4. They expose seasonality and one-off items that the time-weighted formula assumes away.

### 3.2 Verification on the requested companies

| ticker | FY0 | last FYE (Yahoo) | MRQ | FY0 end (0y endDate) | SEC FYE (MMDD) | f | EPS FY0 | EPS FY1 | EPS NTM | P/E FY0 | P/E NTM | P/E FY1 | Yahoo fwd P/E | Yahoo horizon |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | FY2027 (FYE late Jan) | 2026-01-25 | 2026-07-26 | 2027-01-31 | 0131 | 0.351 | 9.31 | 15.68 | 13.45 | 24.2 | 16.7 | 14.4 | 14.4 | FY1(+1y) |
| MSFT | FY2027 (FYE 30 Jun) | 2026-06-30 | 2026-06-30 | 2027-06-30 | 0630 | 0.760 | 19.76 | 23.68 | 20.70 | 26.1 | 24.9 | 21.8 | 21.8 | FY1(+1y) |
| AAPL | FY2026 (FYE late Sep) | 2025-09-27 | 2026-06-27 | 2026-09-30 | 0926 | 0.014 | 8.82 | 9.58 | 9.57 | 38.7 | 35.6 | 35.6 | 35.6 | FY1(+1y) |
| ORCL | FY2027 (FYE 31 May) | 2026-05-31 | 2026-08-31 | 2027-05-31 | 0531 | 0.678 | 8.14 | 11.00 | 9.06 | 16.8 | 15.1 | 12.5 | 12.5 | FY1(+1y) |
| WMT | FY2027 (FYE 31 Jan) | 2026-01-31 | 2026-07-31 | 2027-01-31 | 0131 | 0.351 | 2.89 | 3.23 | 3.11 | 37.4 | 34.7 | 33.4 | 33.4 | FY1(+1y) |
| PAYX | FY2027 (FYE 31 May) | 2026-05-31 | 2026-08-31 | 2027-05-31 | 0531 | 0.678 | 5.96 | 6.39 | 6.10 | 17.0 | 16.6 | 15.9 | 15.8 | FY1(+1y) |
| AME | CY2026 (calendar) | 2025-12-31 | 2026-06-30 | 2026-12-31 | 1231 | 0.266 | 8.34 | 9.62 | 9.28 | 30.1 | 27.0 | 26.1 | 26.2 | FY1(+1y) |
| JPM | CY2026 (calendar) | 2025-12-31 | 2026-06-30 | 2026-12-31 | 1231 | 0.266 | 24.20 | 25.04 | 24.82 | 14.2 | 13.8 | 13.7 | 13.7 | FY1(+1y) |

Reading: for all eight names the FY0 end from earningsTrend agrees with `nextFiscalYearEnd` (within the 52/53-week offset) and with the SEC fiscal year-end, and `mostRecentQuarter` falls inside FY0. AAPL has 5 days of FY2026 left, so f ≈ 0.01 and NTM ≈ FY2027; that is why Yahoo's +1y multiple is nearly right for September year-ends. For MSFT (f = 0.76) the NTM window is still mostly FY2027, so Yahoo's FY2028-based 21.8x understates the 24.9x NTM multiple by 12.6%. For NVDA (f = 0.35) the 14.4x → 16.7x gap reproduces the prior review's finding (14.3x on FY+1 vs 24.1x on FY0). The correct NTM figure lies between the two.

### 3.3 How often Yahoo forwardPE differs from NTM P/E by more than 10% (universe table)

| group | n | n_gt10pct | share >10% | median Yahoo/NTM | p10 | p90 | share Yahoo lower |
|---|---|---|---|---|---|---|---|
| ALL | 497 | 55 | 11.1% | 0.975 | 0.904 | 1.000 | 89.7% |
| fye_group=Dec FYE | 380 | 34 | 8.9% | 0.975 | 0.927 | 1.001 | 89.5% |
| fye_group=non-Dec FYE | 117 | 21 | 17.9% | 0.974 | 0.857 | 1.000 | 90.6% |
| f_bucket=f=0 (FY0 ended) | 5 | 0 | 0.0% | 1.000 | 1.000 | 1.000 | 40.0% |
| f_bucket=0<f<=0.25 | 40 | 1 | 2.5% | 0.998 | 0.974 | 0.999 | 92.5% |
| f_bucket=0.25<f<=0.5 | 403 | 37 | 9.2% | 0.975 | 0.925 | 1.002 | 89.3% |
| f_bucket=0.5<f<=0.75 | 19 | 5 | 26.3% | 0.941 | 0.825 | 0.965 | 100.0% |
| f_bucket=0.75<f<=1 | 30 | 12 | 40.0% | 0.904 | 0.751 | 0.957 | 93.3% |
| yahoo_fwd_horizon=FY0(0y) | 1 | 0 | 0.0% | 0.996 | 0.996 | 0.996 | 100.0% |
| yahoo_fwd_horizon=FY1(+1y) | 431 | 37 | 8.6% | 0.976 | 0.925 | 0.999 | 91.0% |
| yahoo_fwd_horizon=missing_forwardEps | 1 | 0 | 0.0% | 0.973 | 0.973 | 0.973 | 100.0% |
| yahoo_fwd_horizon=~FY0(0y) | 4 | 0 | 0.0% | 0.955 | 0.918 | 1.022 | 75.0% |
| yahoo_fwd_horizon=~FY0(0y)>3%off | 5 | 4 | 80.0% | 0.847 | 0.804 | 0.990 | 80.0% |
| yahoo_fwd_horizon=~FY1(+1y) | 36 | 5 | 13.9% | 0.969 | 0.911 | 1.061 | 80.6% |
| yahoo_fwd_horizon=~FY1(+1y)>3%off | 19 | 9 | 47.4% | 0.908 | 0.459 | 1.007 | 84.2% |
| gics_sector=Communication Services | 22 | 7 | 31.8% | 0.980 | 0.705 | 1.095 | 72.7% |
| gics_sector=Consumer Discretionary | 47 | 3 | 6.4% | 0.971 | 0.925 | 0.986 | 95.7% |
| gics_sector=Consumer Staples | 33 | 1 | 3.0% | 0.983 | 0.944 | 0.996 | 97.0% |
| gics_sector=Energy | 21 | 3 | 14.3% | 1.021 | 0.939 | 1.086 | 38.1% |
| gics_sector=Financials | 74 | 4 | 5.4% | 0.975 | 0.949 | 0.998 | 94.6% |
| gics_sector=Health Care | 59 | 5 | 8.5% | 0.974 | 0.917 | 0.997 | 94.9% |
| gics_sector=Industrials | 82 | 2 | 2.4% | 0.971 | 0.933 | 0.997 | 93.9% |
| gics_sector=Information Technology | 74 | 20 | 27.0% | 0.951 | 0.833 | 0.999 | 93.2% |
| gics_sector=Materials | 25 | 6 | 24.0% | 0.971 | 0.862 | 1.051 | 84.0% |
| gics_sector=Real Estate | 29 | 4 | 13.8% | 0.991 | 0.932 | 1.081 | 72.4% |
| gics_sector=Utilities | 31 | 0 | 0.0% | 0.981 | 0.975 | 0.985 | 100.0% |

(Full table: `v4/outputs/d4_ntm_vs_yahoo_table.csv`. Groups: FY-end month of FY0, f bucket, Yahoo horizon flag and GICS sector.)

### 3.4 Largest horizon effects among clean names (ntm_quality = ok)

| ticker | FY0 end month | f | eps_fy0 | eps_fy1 | eps_ntm | Yahoo fwd P/E | NTM P/E | FY0 P/E | Yahoo/NTM |
|---|---|---|---|---|---|---|---|---|---|
| ORCL | 5 | 0.68 | 8.14 | 11.00 | 9.06 | 12.5 | 15.1 | 16.8 | 0.824 |
| NKE | 5 | 0.68 | 1.68 | 2.13 | 1.82 | 16.2 | 19.6 | 21.3 | 0.825 |
| FLEX | 3 | 0.51 | 4.72 | 7.11 | 5.89 | 16.1 | 19.5 | 24.3 | 0.829 |
| IP | 12 | 0.27 | 1.33 | 3.02 | 2.57 | 11.6 | 13.6 | 26.3 | 0.851 |
| LRCX | 6 | 0.76 | 9.51 | 11.74 | 10.04 | 26.9 | 31.4 | 33.2 | 0.855 |
| SNDK | 6 | 0.76 | 213.90 | 263.49 | 225.82 | 6.7 | 7.9 | 8.3 | 0.857 |
| NVDA | 1 | 0.35 | 9.31 | 15.68 | 13.45 | 14.4 | 16.7 | 24.2 | 0.857 |
| KLAC | 6 | 0.76 | 5.45 | 6.71 | 5.76 | 28.0 | 32.7 | 34.5 | 0.858 |
| SMCI | 6 | 0.76 | 4.34 | 5.33 | 4.58 | 8.1 | 9.5 | 10.0 | 0.859 |
| AMD | 12 | 0.27 | 7.58 | 15.58 | 13.45 | 40.5 | 46.9 | 83.2 | 0.864 |
| MRVL | 1 | 0.35 | 4.21 | 6.76 | 5.86 | 38.8 | 44.7 | 62.2 | 0.868 |
| MSFT | 6 | 0.76 | 19.76 | 23.68 | 20.70 | 21.8 | 24.9 | 26.1 | 0.874 |
| BE | 12 | 0.27 | 2.71 | 4.93 | 4.34 | 58.6 | 66.6 | 106.7 | 0.880 |
| AZO | 8 | 0.93 | 170.09 | 190.52 | 171.54 | 14.8 | 16.7 | 16.9 | 0.884 |
| EL | 6 | 0.76 | 3.32 | 3.92 | 3.47 | 24.1 | 27.3 | 28.4 | 0.885 |

### 3.5 Which horizon Yahoo's forwardEps / forwardPE uses (per ticker: `yahoo_fwd_horizon`)

| horizon flag | tickers |
|---|---|
| FY1(+1y) | 433 |
| ~FY1(+1y) | 36 |
| ~FY1(+1y)>3%off | 20 |
| ~FY0(0y)>3%off | 6 |
| ~FY0(0y) | 4 |
| undetermined | 2 |
| missing_forwardEps | 1 |
| FY0(0y) | 1 |

`FY1(+1y)` means within 0.5% of the +1y consensus; `~` means the nearest horizon within 3%; `>3%off` means neither. `forwardPE` = price/`forwardEps` holds for all names with both fields. The 26 '>3% off' cases show that `info.forwardEps` and `info.epsCurrentYear` come from a different estimate feed or basis than earningsTrend. Examples: TTWO (earningsTrend FY1 5.29 on what appears to be a GAAP basis vs `forwardEps` 10.29), DASH (4.48 vs 8.14), TPL (`forwardEps` 73.12 is not adjusted for the 3:1 split of 2025-12-23), and PANW, DELL and REGN (a thin or stale +1y row). **Never mix `forwardEps` with earningsTrend rows.**

### 3.6 Consensus quality grade (`ntm_quality`, `ntm_flags`)

| flag | tickers |
|---|---|
| ntm_timeweighted_vs_quarteraware | 56 |
| fy0_vs_quarterly_rows | 47 |
| reit_eps_not_ffo | 28 |
| info_epsCurrentYear_vs_trend | 24 |
| fy1_below_fy0_by_15pct+ | 21 |
| fy1_thin_coverage | 20 |
| fy1_row_yearAgo_ne_fy0 | 15 |
| fy1_dispersion_extreme | 14 |
| fiscal_date_check | 6 |
| ntm_eps_nonpositive | 3 |
| ntm_missing | 3 |
| estimates_from_sibling | 1 |

'unreliable' means at least one major issue: missing or non-positive NTM EPS; a REIT (EPS is not FFO); the FY0 annual row inconsistent with (reported YTD + remaining quarterly estimates) by more than 25%; or the +1y row's `yearAgoEps` ≠ the 0y consensus by more than 10%. Examples: CDNS (FY0 row 4.81 against reported YTD 4.07 plus remaining quarters 4.06), GOOGL and AMZN (the FY0 consensus includes large already-reported investment gains, so FY1 < FY0 and the quarter-aware NTM is 16% and 14% below the time-weighted figure), ECHO, DOC and VRTX (one-offs in FY0), and HON (the spin-off changed the perimeter). **Recommendation for downstream agents:** use `pe_ntm` where `ntm_quality == 'ok'`. For 'caution' names, also look at `pe_ntm_qaware` and `pe_ntm_qsum`. Do not rank 'unreliable' names on P/E without primary-source work (for REITs use FFO or AFFO).

**Independent comparator.** CNBC's forward P/E (LSEG data, horizon undocumented) is closest to our NTM P/E for 258/489 names, to FY0 for 183 and to FY1 for 48. Median absolute gaps: NTM 3.6%, FY0 5.1%, FY1 6.7%. A second vendor therefore also puts the forward multiple nearer our NTM figure than Yahoo's +1y figure. The two consensus datasets differ, so this is corroboration, not validation.

## 4. Validation (pass rates and failures)

| check | compared | pass | pass rate | tolerance | note |
|---|---|---|---|---|---|
| (a) Price vs Cboe close 2026-09-25 | 503 | 503 | 100.0% | ±0.5% | 501 exact; max gap 0.083% |
| (a) Price vs CNBC last 16:00 ET | 503 | 503 | 100.0% | ±0.5% | 498 exact |
| (a) Price vs Stooq (requested) | 0 | 0 | n/a | ±0.5% | source blocked by a JS proof-of-work bot challenge; not circumvented |
| (b) marketCap vs price×sharesOutstanding | 503 | 455 | 90.5% | ±3% | all 48 failures are multi-class/UP-C/OP-unit |
| (b') marketCap vs price×impliedSharesOutstanding | 503 | 503 | 100.0% | ±3% | Yahoo's marketCap definition |
| (c) SEC CY2025 revenue (primary concept) vs Yahoo FY2025 | 353 | 335 | 94.9% | ±2% | 381 Dec-FYE companies (unique CIK) |
| (c) SEC revenue, best of 4 concepts | 369 | 354 | 95.9% | ±2% | diagnostic (lenient) |
| (c) SEC NetIncomeLoss vs Yahoo Net Income | 350 | 327 | 93.4% | ±2% | 4 SEC XBRL scale errors among failures |
| (c) SEC net income, best pair | 378 | 375 | 99.2% | ±2% | diagnostic (NCI/preferred/ProfitLoss) |
| (d) Staleness: regularMarketTime NY date = 2026-09-25 | 503 | 503 | 100.0% | exact date | 0 stale |
| (f) FY0 end month vs SEC fiscalYearEnd | 503 | 500 | 99.4% | month (52/53-wk tol.) | 3 exceptions explained |
| (f) lastFiscalYearEnd vs latest 10-K period | 500 | 497 | 99.4% | ±7 days | 3 = results out, 10-K pending |
| (extra) trailing EPS vs CNBC | 498 | 459 | 92.2% | ±5% | 402 within 1% |
| (extra) sharesOutstanding vs CNBC | 503 | 454 | 90.3% | ±3% | 495 using either Yahoo share field |

**(a) Prices.** No failures. Cboe `last_trade_time` and CNBC `last_time` are both dated 2026-09-25 for all 503. NYSE names print at 16:00–16:04 ET (closing auction), which is why a few `regularMarketTime` values read 20:03 UTC.

**(b) Market cap.** The 48 names outside ±3% (price × `sharesOutstanding`): AOS, ABNB, GOOGL, GOOG, APP, ARES, BRK-B, BLK, BX, XYZ, BF-B, BXP, CVNA, CHTR, COIN, DDOG, DELL, DASH, ECHO, ERIE, ESS, EL, EXPE, EXR, FOXA, FOX, HSY, IBKR, LEN, LULU, MKC, META, NWSA, NWS, NKE, PLTR, PCG, RL, RDDT, HOOD, SPG, TKO, TSN, UDR, UPS, UHS, V, WDAY. Every one reconciles to 0.0% with `impliedSharesOutstanding`. Causes: listed dual classes (GOOGL/GOOG, FOXA/FOX, NWSA/NWS, BRK-B, BF-B), unlisted high-vote or founder classes (META, ABNB, DASH, PLTR, HOOD, COIN, DDOG, RDDT, WDAY, EL, NKE, HSY, TSN, RL, UPS, LEN, ...), and UP-C or operating-partnership units (IBKR +276%, TKO, BX, ARES, CHTR, SPG, ESS, EXR, UDR, BXP, ...). PCG (+36%) and BLK (+4.9%) have no obvious class structure and should be checked if their market cap is used. **Rule: use `marketCap` (all classes) for EV and size; use price and per-share EPS for P/E.**

**(c) SEC fundamentals.** Revenue failures (18): CPT (+12035%, definition_or_unexplained), MTB (+481%, definition_or_unexplained), HBAN (+421%, definition_or_unexplained), FIX (+397%, definition_or_unexplained), IBKR (+319%, definition_or_unexplained), AXP (+75%, concept_mismatch(other SEC concept/pair within 2%)), ARES (+18%, concept_mismatch(other SEC concept/pair within 2%)), BX (-14%, definition_or_unexplained), MO (-13%, definition_or_unexplained), RSG (-13%, concept_mismatch(other SEC concept/pair within 2%)), HAS (-12%, concept_mismatch(other SEC concept/pair within 2%)), BRK-B (+11%, definition_or_unexplained), EQT (-3%, definition_or_unexplained), ACGL (-3%, definition_or_unexplained), KEY (-3%, definition_or_unexplained), CVX (-2%, concept_mismatch(other SEC concept/pair within 2%)), BRO (-2%, definition_or_unexplained), AMP (-2%, concept_mismatch(other SEC concept/pair within 2%)).

Investigation of the largest revenue gaps:
* **Concept mismatch, not data error.** CPT (a REIT whose rental income is lease revenue; the ASC 606 concept captures only $13m), MTB, HBAN and IBKR (ASC 606 revenue is fee income only; Yahoo 'Total Revenue' is net revenue), AXP, ARES, RSG and HAS (another SEC revenue concept matches Yahoo within 2%).
* **Definition.** MO: Yahoo revenue is net of excise taxes ($20.1bn) vs $23.3bn gross. BRK-B: Yahoo includes investment and derivative gains. BX: performance allocations. EQT, ACGL, KEY: hedging, insurance and bank revenue definitions (about 3%).
* **SEC-side tagging anomaly.** FIX: the CY2025 `Revenues` frame holds $1.83bn against about $9.1bn total revenue (the tag is attached to a sub-total).

Net-income failures (23): PCG (concept_mismatch(other SEC concept/pair within 2%)), ANET (sec_xbrl_scale_error), ED (sec_xbrl_scale_error), SCHW (sec_xbrl_scale_error), ECHO (concept_mismatch(other SEC concept/pair within 2%)), DD (concept_mismatch(other SEC concept/pair within 2%)), TKO (concept_mismatch(other SEC concept/pair within 2%)), DVA (concept_mismatch(other SEC concept/pair within 2%)), ARES (definition_or_unexplained), FTV (definition_or_unexplained), CSGP (concept_mismatch(other SEC concept/pair within 2%)), FANG (concept_mismatch(other SEC concept/pair within 2%)), MET (concept_mismatch(other SEC concept/pair within 2%)), VMRK (definition_or_unexplained), PFG (concept_mismatch(other SEC concept/pair within 2%)), KIM (concept_mismatch(other SEC concept/pair within 2%)), EIX (concept_mismatch(other SEC concept/pair within 2%)), Q (concept_mismatch(other SEC concept/pair within 2%)), HSIC (concept_mismatch(other SEC concept/pair within 2%)), COIN (concept_mismatch(other SEC concept/pair within 2%)), GM (concept_mismatch(other SEC concept/pair within 2%)), APO (concept_mismatch(other SEC concept/pair within 2%)), VZ (concept_mismatch(other SEC concept/pair within 2%)).
* **SEC XBRL scale errors.** PCG NetIncomeLoss = 2,593 (should be $2.593bn), ANET = 3,511 ($3.511bn), ED = 2,023,000 ($2.023bn) and SCHW = 8,852,000 ($8.852bn). The frames API returns the value as filed, so primary-source XBRL needs a magnitude sanity check before use (a lesson for the D3 PIT-fundamentals agent).
* **Definition.** Non-controlling interests (TKO, DVA, FANG, CSGP), preferred dividends (MET), discontinued operations (DD after the Qnity spin, FTV after the Ralliant spin), and ECHO, where the NetIncomeLoss frame (−$52m) comes from a different filing than ProfitLoss (−$14.5bn, which matches Yahoo).
* Coverage: 28 December-year-end companies have no revenue frame in the concepts used (mostly banks, brokers and utilities that tag other concepts), and 31 have no NetIncomeLoss frame for CY2025.

**(d) Staleness.** None: all 503 `regularMarketTime` values fall on 2026-09-25 between 20:00:00 and 20:04 UTC.

## 5. Anomalies

| check | severity | tickers |
|---|---|---|
| metadata_prevName | high | 4 |
| missing_estimates | high | 3 |
| metadata_prevName | info | 41 |
| metadata_ipoExpectedDate_present | info | 20 |
| enterprise_value_nonpositive | info | 4 |
| name_differs_yahoo_vs_wikipedia | info | 3 |
| yahoo_forwardEps_not_exact_FY1 | low | 70 |
| eps_fy1_dispersion_high | low | 46 |
| target_mean_far_from_price | low | 7 |
| rec_mean_inconsistent_beyond_systematic_offset | low | 5 |
| missing_price_target | low | 4 |
| ntm_method_divergence_gt10pct | medium | 56 |
| pe_gt_100 | medium | 26 |
| eps_fy1_below_fy0_15pct | medium | 21 |
| eps_fy1_dispersion_extreme | medium | 14 |
| thin_coverage | medium | 9 |
| negative_forward_eps | medium | 7 |
| fiscal_date_inconsistency | medium | 6 |
| fetch_errors | medium | 1 |

* **Negative forward EPS**: ARE, BA, COIN, GILD, LYV, MRNA, WBD. These are GAAP-basis consensus figures with charges (IPR&D at GILD, impairments at ARE); P/E is undefined (`pe_ntm_reason`).
* **P/E > 100 on NTM, trailing or forward EPS**: ALB, AMD, AXON, BE, COIN, CRWD, CSGP, DASH, DDOG, DOC, EL, GPC, LYV, MCHP, MRK, OMC, P, PANW, PLTR, PSKY, TSLA, VTR, WAT, WBD, WELL, XYZ.
* **Missing estimates**: CPRT (Yahoo's 0y row is empty and +1y is labelled with the same 2027-07-31 end), ERIE (no +1y), L (no coverage; its last earnings-calendar row is from 2020). Thin +1y coverage (≤2 analysts): ARE, CPT, DOC, ECHO, PGR, TPL, UDR, VICI, VTR.
* **Extreme FY1 dispersion ((high−low)/|avg| > 1)**: APA, BA, COIN, EXE, INTC, LYV, MOS, MPC, PSKY, TKO, TSLA, TTWO, VLO, WBD. The NVDA FY1 range is 9.80–18.75 on 53 analysts, so a mean-based NTM P/E is spuriously precise.
* **Metadata**: prevName (see §1 item 10). `ipoExpectedDate` is populated for 20 long-listed stocks (e.g. WMT 2025-12-09, LIN 2023-11-07, DPZ 2025-01-02), apparently a listing or ticker-change date; do not use it. FISV has no fiscal-date fields in `info` (the new ticker since 2025-11). The `recommendationMean` field sits a median -0.30 points below the mean implied by `recommendations_summary` counts, so the two are not the same measure; use one consistently.
* **EV ≤ 0**: BRK-B, BNY, IBKR and STT (cash-rich financials). EV/sales is not meaningful for financials generally.

## 6. Change log vs the legacy v3 snapshot (equity_project/info.json + est_all.pkl, Yahoo 2026-09-24)

| ticker | legacy_price | fresh_price | chg_price | chg_forwardEps | chg_eps_fy0 | chg_eps_fy1 | chg_targetMean | legacy_forwardPE | fresh_pe_ntm | flags_gt2pct | 30d FY1 rev | ntm_quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | 224.58 | 225.07 | +0.22% | +0.00% | +0.00% | +0.00% | +0.00% | 14.3 | 16.7 | none | +21.7% | ok |
| CPAY | 400.32 | 398.11 | -0.55% | +0.00% | +0.00% | +0.00% | +0.00% | 12.7 | 13.1 | none | +0.7% | ok |
| AMP | 485.15 | 493.00 | +1.62% | +0.00% | +0.00% | +0.00% | +0.00% | 9.4 | 9.8 | none | +0.0% | ok |
| RL | 351.86 | 357.10 | +1.49% | +0.00% | +0.00% | +0.00% | +0.00% | 16.8 | 18.0 | none | +0.1% | ok |
| AME | 247.74 | 250.74 | +1.21% | +0.00% | +0.03% | +0.37% | +0.00% | 25.8 | 27.0 | none | +6.7% | caution |
| SNA | 367.71 | 369.20 | +0.41% | -0.26% | -0.04% | +0.21% | +0.67% | 17.2 | 17.6 | none | +0.2% | ok |
| ABNB | 151.39 | 157.47 | +4.02% | +0.00% | +0.00% | +0.00% | +0.00% | 24.5 | 26.3 | none | +0.9% | caution |
| NTAP | 197.24 | 201.15 | +1.98% | +0.00% | +0.00% | +0.00% | +0.00% | 17.7 | 19.2 | none | +11.6% | ok |
| PAYX | 101.59 | 101.37 | -0.22% | +0.03% | -0.02% | -0.09% | +0.00% | 15.9 | 16.6 | none | +0.1% | ok |
| MSFT | 497.93 | 516.17 | +3.66% | +0.00% | +0.00% | +0.00% | +0.00% | 21.0 | 24.9 | none | +0.4% | ok |
| IBKR | 89.82 | 89.24 | -0.65% | +0.00% | +0.00% | +0.00% | +0.00% | 28.1 | 29.1 | none | +0.4% | ok |
| HIG | 125.69 | 124.23 | -1.16% | +0.00% | +0.00% | +0.00% | +0.00% | 9.2 | 9.2 | none | -0.1% | ok |
| ALLE | 152.48 | 154.47 | +1.31% | +0.00% | +0.00% | +0.00% | +0.00% | 15.6 | 16.2 | none | -0.0% | ok |
| AIZ | 261.86 | 265.00 | +1.20% | +0.00% | +0.00% | +0.00% | +0.00% | 11.2 | 11.5 | none | +0.7% | ok |

There are no estimate changes above 2% between the two snapshots, which are one session apart. PAYX reported before the legacy pull; its FY0 consensus moved −0.3% over 30 days and 0.0% over 7 days, so the legacy estimates were not stale in a material way. What *does* change materially is the multiple once it is calendarized: every v3 name's NTM P/E is above the v3 'Fwd P/E'. ABNB carries a 'caution' flag because seasonality makes the time-weighted and quarter-aware NTM differ by 13%. AME's thin +1y coverage is 3 analysts out of 12 on FY0; its Indicor acquisition closed on 2026-08-26 and may not be in all estimates.

## 7. Corporate events (best-effort)

Method: SEC submissions (primary source) plus Yahoo headlines. Signals: SC 14D-9 (target of a tender offer); PREM14A/DEFM14A (merger vote); SC TO-T without 14D-9 (the company is the bidder); S-4 (stock deal, usually the acquirer); 8-K Item 2.01 (completed acquisition or disposition, last 180 days). Headlines are read for the company's position relative to the deal verb. 25-NSE is ignored because it is routinely filed for delisted notes.

| flag | tickers |
|---|---|
| evt_being_acquired | 9 |
| evt_acquirer_pending_or_recent | 96 |
| evt_recent_completed_deal | 79 |
| evt_spinoff_separation | 9 |

Reviewed target and merger-party list (each checked against headline and SEC evidence):

| ticker | role | evidence |
|---|---|---|
| WBD | target | Paramount Skydance acquisition; SC 14D-9 (Feb 2026), DEFM14A (Mar 2026) |
| KVUE | target | Kimberly-Clark acquisition; holders approved 2026-01-29; regulatory review ongoing |
| TECH | target | Merck KGaA, Darmstadt; DEFM14A 2026-08-20; holders approved 2026-09-23 |
| AES | target | GIP/EQT-led consortium (announced 2026-03-02); DEFM14A 2026-05-15 |
| NSC | target | Union Pacific merger; DEFM14A 2025-10-01; STB review ongoing |
| D | merger party | all-stock combination with NEE (announced 2026-05-18); D DEFM14A 2026-07-28, NEE S-4 2026-07-09 |
| DVN | not pending | Coterra merger completed 2026-05-07; activist letter 2026-09-23 urges a sale |
| CCL | reorganisation | DEFM14A 2026-02-27 and S-4: DLC unification (Yahoo longName now 'Carnival Corporation Ltd.') |
| MGM | bid withdrawn | People Inc. $48.30 cash proposal (2026-06-01) dropped 2026-09-24 |

Other acquirers with SEC S-4 or tender filings in the last 12 months include AWK, BSX, CTAS, FITB, HBAN, KMB, NEE, ON, SWKS, UNP, VICI, AVGO, AMZN, A, CMCSA, DD, PSA and SPGI, plus FOXA and FOX (Roku), and the tender bidders CPRT (ACV), MRK, GILD, LLY, BIIB and PSKY. The full list with evidence strings is in the CSV. Spin-offs and separations: FDXF and HONA (completed 2026; both new constituents), Q (Qnity, from DD), CTVA (Vylor), FLEX (cloud and power infrastructure, Form 10 filed), GPC (automotive/industrial split), SOLV (health-information systems), MDT (MiniMed exchange offer) and KDP (breakup).

## 8. Limitations

* Yahoo consensus is a vendor snapshot with an undocumented, company-specific basis (GAAP for some, adjusted for others) and undocumented analyst sets. The NTM figure inherits this; `ntm_quality` flags only detectable inconsistencies.
* Time-weighted NTM assumes earnings are spread evenly within each fiscal year. Seasonal businesses (ABNB, retailers) and years with large booked one-offs (GOOGL, AMZN, ECHO) are better read with `pe_ntm_qaware`/`pe_ntm_qsum`. There is no FY2 estimate, so NTM for f = 0 names is approximated by FY1.
* Independent price sources are delayed-quote vendors (Cboe, CNBC), not an exchange-certified official close. Stooq could not be used without solving a bot challenge.
* SEC frames cover only filers tagging the chosen concepts and contain filer errors; the check is limited to December year-ends (381 companies) and FY2025.
* Corporate-event flags rely on heuristics: headline tabs hold only about 30 items, and merger proxies can be filed by acquirers or for reorganisations. Treat them as leads for the diligence agents, not facts.
* This is live, not point-in-time, data. It must not be used in backtests (see CONVENTIONS: PIT rule).

## 9. Files produced

| file | rows | content |
|---|---|---|
| v4/data/d4_live_snapshot.parquet | 503 | one row per constituent; 269 columns incl. NTM fields, quality grade, retrieval times |
| v4/data/d4_universe.csv | 503 | Wikipedia constituents (ticker, name, GICS, CIK) |
| v4/data/d4_indep_prices.csv | 503 | Cboe close + CNBC last/eps/shares/fpe |
| v4/data/d4_validation_prices.csv | 503 | price + vendor cross-checks |
| v4/data/d4_validation_mcap.csv | 503 | market-cap reconciliation |
| v4/data/d4_validation_sec.csv | 500 | SEC frames vs Yahoo income statement (per CIK) |
| v4/data/d4_validation_fye.csv | 503 | fiscal-year-end vs SEC |
| v4/data/d4_anomalies.csv | 361 | long-format anomaly flags |
| v4/data/d4_changelog_v3.csv | 14 | legacy vs fresh for 14 v3 names |
| v4/data/d4_corporate_events.csv | 503 | event flags with evidence |
| v4/outputs/d4_ntm_vs_yahoo_table.csv | 26 | universe table of Yahoo fwd P/E vs NTM P/E |
| v4/outputs/d4_validation_summary.json | 1 | all validation statistics |

Each dataset has a `<name>.meta.json` sidecar. Scripts: `v4/code/d4_common.py`, `d4_universe.py`, `d4_fetch_yahoo.py`, `d4_fetch_indep_prices.py`, `d4_fetch_sec.py`, `d4_build_snapshot.py`, `d4_validate.py`, `d4_events.py`, `d4_changelog.py`, `d4_report.py`. Raw cache (not synced): `C:\Users\user\eqv4\cache\d4\`.

## 10. Sources

* Constituents: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies (retrieved 2026-09-25).
* Yahoo Finance via yfinance 1.7.0: https://query2.finance.yahoo.com/v10/finance/quoteSummary/{T} (earningsTrend, earningsHistory, financialData, recommendationTrend, upgradeDowngradeHistory, calendarEvents), https://query1.finance.yahoo.com/v7/finance/quote, https://finance.yahoo.com/calendar/earnings?symbol={T}.
* Cboe delayed quotes: https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json; CNBC: https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols={A|B}.
* Stooq (blocked): https://stooq.com/q/d/l/?s=nvda.us&i=d (bot-challenge page cached as `cache/d4/indep_prices/stooq_probe_nvda.txt`).
* SEC XBRL frames: https://data.sec.gov/api/xbrl/frames/us-gaap/{Concept}/USD/CY2025.json; submissions: https://data.sec.gov/submissions/CIK##########.json.
* Amcor FYE change: https://www.sec.gov/Archives/edgar/data/1748790/000110465926055873/tm2613113d1_8k.htm (8-K Item 5.03, filed 2026-05-06).
* FedEx FYE change: https://www.sec.gov/Archives/edgar/data/1048911/000104891126000108/fdx-20260721.htm (8-K Item 2.02, filed 2026-07-21).
* Prior review being tested: `review/agents/02_market_data.md` (NVDA 14.32x vs 24.13x horizon finding and the NVDA prevName anomaly; both reproduced).
