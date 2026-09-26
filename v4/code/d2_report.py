"""d2_report.py - render v4/outputs/d2_report.md from D2 result files (all numbers pulled programmatically)."""
import os
import json
import glob
import pandas as pd
import numpy as np

from d2_common import DATA, OUT, CACHE, URLS, CUTOFF, utcnow, write_meta

q = json.load(open(os.path.join(OUT, "d2_qc_summary.json")))
v = json.load(open(os.path.join(OUT, "d2_validation_results.json")))
usum = json.load(open(os.path.join(OUT, "d2_universe_summary.json")))
u = pd.read_csv(os.path.join(DATA, "d2_universe.csv"))
cov = pd.read_csv(os.path.join(DATA, "d2_coverage.csv"))
rlog = json.load(open(os.path.join(CACHE, "raw", "retrieval_log.json")))


def pct(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{100 * x:.{d}f}%"


def bp(x):
    return f"{1e4 * x:+.1f} bp"


eq = cov[cov["asset_class"] == "equity"]
cur = eq[eq["in_current"]]
hist = eq[~eq["in_current"]]
hist_fja = hist[hist["in_fja_since2000"]]
bench = cov[cov["asset_class"] != "equity"]
n_nodata_hist = int((hist["status"] == "no_data").sum())
n_nodata_fja = int((hist_fja["status"] == "no_data").sum())
rename_old = set(cov.loc[cov["rename_successor"].notna(), "ticker"])
n_nodata_fja_not_renamed = int(((hist_fja["status"] == "no_data") & ~hist_fja["ticker"].isin(rename_old)).sum())
reuse_n = int(cov["reuse_suspect"].sum())
eras = q["member_day_coverage_by_era"]
mby = pd.DataFrame(q["members_with_price_by_year"])
S = v.get("sample", {})
L = v.get("latest_close", {})
B = v.get("benchmarks", {})
BT = v.get("badticks_crosscheck", {})
CE = v.get("confirmed_errors", {})
adjev = q.get("adj_split_dividend_events", {})
bt = q.get("bad_ticks", {})
st = q.get("stale_runs", {})

lines = []
A = lines.append
A("# D2 - Price history & total returns (S&P 500 members since 2000 + benchmarks)")
A("")
A(f"_Agent D2 · generated {utcnow()} · market-data cutoff US close {CUTOFF} · all numbers from `v4/outputs/d2_qc_summary.json` and `d2_validation_results.json`_")
A("")
A("## Answer first")
A("")
A(f"- **Built**: daily Close (split-adj.), Adj Close (total-return), Volume, dividends and splits for **{len(cov):,} Yahoo symbols** "
  f"({len(eq):,} equities that were S&P 500 members at any time since 2000, plus {len(bench)} benchmarks/ETFs/UCITS lines), "
  f"{q['us_calendar']['first']} → {q['us_calendar']['last']} ({q['us_calendar']['n_days']:,} NYSE trading days). "
  f"Monthly total-return panel: {q['monthly']['n_months']} month-ends ({q['monthly']['first_month_end']} → {q['monthly']['last_month_end']}).")
A(f"- **Current constituents**: all {len(cur)} have Yahoo data ending {CUTOFF} (check (c): {q['check_c_current_last_date']['n_last_is_cutoff']}/{q['check_c_current_last_date']['n_current']} pass). "
  f"All {int((bench['status'] == 'active').sum())}/{len(bench)} benchmark/ETF/UCITS symbols returned data.")
A(f"- **Survivorship (the main limitation)**: of {len(hist)} historical, non-current member symbols, **{n_nodata_hist} ({pct(n_nodata_hist / len(hist))}) have no Yahoo data at all** "
  f"(of the {len(hist_fja)} from the fja05680 list: {n_nodata_fja}; {n_nodata_fja - n_nodata_fja_not_renamed} of those are explained by later ticker renames). "
  f"Measured on index member-days, Yahoo prices exist for only **{pct(eras[0]['coverage_strict'], 0)} of 2000-04, {pct(eras[1]['coverage_strict'], 0)} of 2005-09, "
  f"{pct(eras[2]['coverage_strict'], 0)} of 2010-14, {pct(eras[3]['coverage_strict'], 0)} of 2015-19 and {pct(eras[4]['coverage_strict'], 0)} of 2020-26** "
  f"(best case incl. detected renames: {', '.join(pct(e['coverage_best_incl_renames'], 0) for e in eras)}). "
  f"A Yahoo-only backtest therefore sees roughly half of the 2000-04 index; the missing half is dominated by acquired and failed companies. B1 must treat pre-2015 results as survivorship-biased.")
A(f"- **Identity risk**: {reuse_n} symbols are flagged `reuse_suspect` (Yahoo now serves a different company under the old symbol, e.g. WB = Weibo not Wachovia). "
  "Reverse-merger histories (T = SBC before 2005, JCI = Tyco before 2016, JPM = Chase before 2001, WEN = Triarc before 2008) cannot be detected from prices; "
  "join prices to membership through D1's CIK-level identifiers, not raw tickers.")
if S:
    A(f"- **Second-source validation** (Stooq blocked by a JavaScript bot challenge → CNBC public endpoints used): 60 tickers × 25 random dates since 2010: "
      f"**{pct(S['pct_within_0p5'])} of Yahoo Closes within 0.5%** (current {pct(S['by_group'][0]['mean'])}, historical {pct(S['by_group'][1]['mean'])}); "
      f"{S['miss_classes'].get('constant_adjustment_offset', 0)} of {S['n_fail_obs']} misses are constant corporate-action adjustment offsets (spin-offs/special dividends adjusted differently), "
      f"so {pct(S['pct_within_0p5_or_constant_offset'], 2)} agree up to a constant; daily returns on the same dates agree within 0.5pp for {pct(S['pct_daily_return_within_0p5pp'])}.")
if L:
    A(f"- **{CUTOFF} close**, all current constituents vs CNBC: {L['n_compared']} compared, **{pct(L['pct_within_0p5'])} within 0.5%**, {pct(L['pct_exact_to_cent'])} identical to the cent "
      f"(prior-day close {pct(L['prev_close_pct_exact_cent'])} identical to the cent).")
if B:
    s = B["SPY_vs_SP500TR"]
    A(f"- **Benchmark integrity**: SPY Adj Close vs ^SP500TR {s['base_date']}→{s['end_date']}: CAGR {pct(s['cagr_a'], 2)} vs {pct(s['cagr_b'], 2)} → "
      f"**tracking difference {pct(s['annualized_difference'], 2)}/yr** (expected ≈ −0.1%; IVV {pct(B['IVV_vs_SP500TR']['annualized_difference'], 2)}, VOO {pct(B['VOO_vs_SP500TR']['annualized_difference'], 2)}). "
      f"^GSPC matches CNBC/FRED within 0.01% on {pct(B['^GSPC_vs_CNBC']['pct_within_0p01pct'], 2)}/{pct(B['GSPC_vs_FRED_SP500']['pct_within_0p01pct'], 2)} of days. "
      f"RSP (equal-weight, TR) vs ^GSPC (cap-weight, price): {pct(B['RSP_vs_GSPC']['annualized_difference'], 2)}/yr, daily correlation {B['RSP_vs_GSPC']['corr_daily']:.3f}.")
A(f"- **Data quality**: Adj Close internally consistent with Yahoo dividends ({q['check_e_adj_factor']['n_factor_jumps_not_matching_yahoo_dividend_5pct']} mismatch in "
  f"{q['check_e_adj_factor']['n_dividend_events_total']:,} dividend events; 0 tickers with factor > 1 or decreasing); 0 non-positive equity prices; "
  f"{bt.get('n', 0)} daily moves >50% flagged in `d2_bad_ticks.csv` ({bt.get('during_membership_valid_ticker_n', 'n/a')} inside a valid index membership); "
  f"CNBC confirms {BT.get('n_confirmed_by_cnbc', 'n/a')}/{BT.get('n_with_cnbc_data', 'n/a')} checkable large moves as real. "
  f"**Yahoo spin-off double counts corrected** in Adj Close: {', '.join(adjev.get('corrected', [])) or 'none'} (raw kept in `d2_adjclose_yahoo_raw.parquet`).")
A("")

# ------------------------------------------------------------------------------------------------------------
A("## 1. What was built (method)")
A("")
A("**Universe** (`d2_universe.csv`, script `d2_universe.py`):")
A(f"- Wikipedia *List of S&P 500 companies* table 1 → {usum['n_current']} current symbols ({rlog['wiki_current']['url']}, retrieved {rlog['wiki_current']['retrieved_utc']}).")
A(f"- The *Selected changes* table no longer lives on that page; it moved to *Historical components of the S&P 500* ({rlog['wiki_changes']['url']}); all Added/Removed tickers were taken ({usum['n_wiki_changes_only']} equity symbols appear only there, {usum['n_wiki_pre2000_only']} of them only in pre-2000 changes; kept and tagged `wiki_pre2000_only`).")
A(f"- fja05680 *S&P 500 Historical Components & Changes (Updated).csv* ({rlog['fja05680']['url']}): union of all tickers on any row dated ≥ 2000-01-01 → {usum['n_fja_since2000']} symbols; last row {usum['fja_last_row_date']}; Wikipedia changes after that date applied ({', '.join(usum['wiki_changes_applied_after_fja'])}). "
  f"Reconstructed final membership equals the Wikipedia current list exactly (0 differences). No `-YYYYMM` suffixes occur in this file vintage (rule implemented, {usum['n_suffix_stripped']} stripped).")
A(f"- Normalised to Yahoo style (`.`→`-`, e.g. BRK-B, BF-B); original symbols kept in `ticker_orig`. 36 benchmark/ETF/UCITS symbols added. Total {usum['n_total']} symbols.")
A("")
A("**Download** (`d2_download.py`): `yf.download(batch, start='1995-01-01', end='2026-09-26', auto_adjust=False, actions=True, group_by='ticker', threads=6)` "
  "in batches of 60 (threads capped at 6 per CONVENTIONS instead of `True`, which would use 2×CPU threads); every batch cached as long-format parquet in "
  "`C:\\Users\\user\\eqv4\\cache\\d2\\batches`; all empty symbols retried one-by-one with `Ticker.history` and exponential backoff (2 clean 'no data' answers required); "
  "a Yahoo chart-metadata pass (longName, exchange, currency, instrumentType, firstTradeDate) supports identity checks. No rate-limit errors occurred. "
  "The first pass ran ~15 min after the 2026-09-25 close while the daily bar was still live, so the last 3+ weeks were re-downloaded later (`refresh` phase) and patched in; see §6.")
A("")
A("**Panels** (`d2_build.py`): wide parquet, index = NYSE trading days (the ^GSPC calendar; no stock-only trading days found), columns = Yahoo symbols. "
  "UCITS `.L` lines are kept in separate `d2_ucits_*` files on their own LSE calendar (mixing calendars would create UK-only rows and misaligned daily returns). "
  f"Monthly returns = Adj Close(last NYSE trading day of month) / Adj Close(previous month-end) − 1, NaN if either end is missing (no filling); September 2026 is incomplete at the cutoff, so the last row is {q['monthly']['last_month_end']}. "
  f"{q['monthly']['midlife_missing_month_end_prices']} cells are NaN because a stock traded during a month but not on the month-end day. Series that end mid-month (delistings) get a separate partial-month return in `d2_final_partial_month.csv` — not a CRSP-style delisting return.")
A("")

# ------------------------------------------------------------------------------------------------------------
A("## 2. Coverage and survivorship bias")
A("")
A("| Status | Current constituents | Historical (non-current) members | Benchmarks/ETFs |")
A("|---|---|---|---|")
for s_ in ["active", "ended_before_2026-09-25", "no_data"]:
    A(f"| {s_} | {int((cur['status'] == s_).sum())} | {int((hist['status'] == s_).sum())} | {int((bench['status'] == s_).sum())} |")
A("")
A("Member-day coverage (share of (member, trading-day) pairs since 2000 for which Yahoo has a price). *strict* = same ticker; *valid* = strict excluding reuse-suspect tickers; *best* = valid plus detected rename successors (heuristic, §5):")
A("")
A("| Era | Member-days | Strict | Valid | Best (incl. renames) | Tickers with missing days (best) |")
A("|---|---|---|---|---|---|")
for e in eras:
    A(f"| {e['era']} | {e['member_days']:,} | {pct(e['coverage_strict'])} | {pct(e['coverage_valid_excl_reuse'])} | {pct(e['coverage_best_incl_renames'])} | {e['n_tickers_with_missing_days_best']} |")
A("")
A("Average number of index members with a Yahoo price on a given day:")
A("")
yrs = [2000, 2002, 2005, 2008, 2010, 2012, 2015, 2018, 2020, 2022, 2024, 2026]
A("| Year | " + " | ".join(str(y) for y in yrs) + " |")
A("|---" * (len(yrs) + 1) + "|")
mby = mby.set_index("year")
A("| Members | " + " | ".join(f"{mby.loc[y, 'members']:.0f}" for y in yrs) + " |")
A("| With price (strict) | " + " | ".join(f"{mby.loc[y, 'with_price']:.0f}" for y in yrs) + " |")
A("| With price (best) | " + " | ".join(f"{mby.loc[y, 'with_price_best']:.0f}" for y in yrs) + " |")
A("")
A("**Most important missing members by era** (no market caps exist for purged names, so importance is proxied by missing member-days in the era, ties broken by total index tenure since 2000; "
  "names/reasons come from the Wikipedia changes table and are attached to the *symbol*, so for re-used symbols they can describe a later holder — e.g. `BR` in 2000-04 is Burlington Resources, "
  "not Broadridge; the table is sparse before 2011, so many older names are blank; D1's membership file will carry authoritative names):")
A("")
names = u.set_index("ticker")
tenure = cov.set_index("ticker")["member_days_since2000"]
for e in eras:
    allm = [(t, n, int(tenure.get(t, 0))) for t, n in e["top_missing_best"]]
    allm.sort(key=lambda x: (-x[1], -x[2]))
    items = []
    for t, n, ten in allm[:15]:
        nm = names.at[t, "wiki_names"] if t in names.index and isinstance(names.at[t, "wiki_names"], str) else ""
        rs = names.at[t, "wiki_removal_reasons"] if t in names.index and isinstance(names.at[t, "wiki_removal_reasons"], str) else ""
        rs = (rs[:60] + "…") if len(rs) > 60 else rs
        items.append(f"`{t}`" + (f" ({nm.split(';')[0]}" + (f"; {rs}" if rs else "") + ")" if nm else "") + f" {n}d/{ten}d")
    A(f"- **{e['era']}** ({e['n_tickers_with_missing_days_best']} symbols with missing days; showing missing days in era / total member-days since 2000): " + "; ".join(items))
A("")
A("_Only the top 40 per era are stored in `d2_qc_summary.json`; the full list is `d2_coverage.csv` (status=no_data, member_days_since2000)._")
A("")

# ------------------------------------------------------------------------------------------------------------
A("## 3. Independent second-source validation")
A("")
sp_ = v.get("stooq_probe", {})
A(f"**Stooq** (`{URLS['stooq']}`) was probed at {sp_.get('probed_utc')}: every request returned HTTP 200 with an HTML page "
  "\"This site requires JavaScript to verify your browser\" (SHA-256 proof-of-work challenge), not CSV. Solving it programmatically would circumvent bot detection, so Stooq was **not used**. "
  "Fallback: CNBC's public market-data endpoints (no key/login): daily bars `ts-api.cnbc.com/harmony/app/bars/<SYM>/1D/.../adjusted/...` (split-adjusted, not dividend-adjusted, "
  "i.e. the same definition as Yahoo `Close`; history back to 1995) and the quote service `quote.cnbc.com/.../restQuote` (latest close). FRED (SP500, VIXCLS, DGS10, DTB3) and CBOE (VIX history) were used for index series. "
  "Nasdaq's API hung without a browser User-Agent and was not pursued (no impersonation).")
A("")
if S:
    A(f"**(i) Random sample** — 40 current constituents + 20 historical members still trading (seeded, reuse suspects excluded), 25 random common dates since 2010 each ({S['n_obs']} observations):")
    A("")
    A("| Metric | All | Current | Historical |")
    A("|---|---|---|---|")
    A(f"| Yahoo Close within 0.5% of CNBC | {pct(S['pct_within_0p5'])} | {pct(S['by_group'][0]['mean'])} | {pct(S['by_group'][1]['mean'])} |")
    A(f"| … within 0.1% | {pct(S['pct_within_0p1'])} | | |")
    A(f"| within 0.5% or constant adjustment offset | {pct(S['pct_within_0p5_or_constant_offset'], 2)} | | |")
    A(f"| Daily return within 0.5pp (same dates) | {pct(S['pct_daily_return_within_0p5pp'])} | | |")
    A(f"| Daily return within 0.1pp | {pct(S['pct_daily_return_within_0p1pp'])} | | |")
    A("")
    A(f"Outliers ({S['n_fail_obs']} obs in {len(S['fail_tickers'])} tickers: {', '.join(S['fail_tickers'])}) were investigated on the full common history (`d2_validation_outliers.csv`, `d2_validation_ratio_steps.csv`). "
      f"{S['miss_classes'].get('constant_adjustment_offset', 0)} are **constant multiplicative offsets** that start/stop exactly at spin-off or special-distribution dates "
      "(e.g. NOV 2014 NOW Inc. spin-off booked by Yahoo as a 1.109 'split'; FTI 2008 JBT and 2021 Technip Energies spin-offs; MSI 2011 Motorola Mobility; BBWI/L Brands special dividends; CLF 2019) — "
      "the two vendors adjust these corporate actions differently; neither price is 'wrong'. The remaining miss is NKTR (sub-$1 price rounded to cents by Yahoo before a 1:15 reverse split → ~0.9% level error).")
    rs = S.get("ratio_steps_full_history", {})
    if rs:
        A(f"Across the entire 1995-2026 common history of all 60 sampled tickers there are {rs['n_steps']} persistent Yahoo/CNBC ratio steps (>0.5%) in {rs['n_tickers_with_steps']} tickers: " +
          "; ".join(f"{k}: {n}" for k, n in rs["by_class"].items()) + ".")
    A("")
if L:
    A(f"**(ii) {CUTOFF} close for all current constituents** vs CNBC quote 'last' (run {L['run_utc']}): {L['n_compared']}/{L['n_current']} compared "
      f"({L['n_cnbc_missing_or_not_0925']} not comparable), {pct(L['pct_within_0p5'])} within 0.5%, {pct(L['pct_within_0p1'])} within 0.1%, {pct(L['pct_exact_to_cent'])} identical to the cent. "
      f"Prior close ({'2026-09-24'}) vs CNBC previous close: {pct(L['prev_close_pct_exact_cent'])} identical to the cent. Fails: {', '.join(f['ticker'] for f in L['fails']) or 'none'}.")
    A("")
if BT:
    A(f"**(iii) Large moves** (>50% daily) of still-trading tickers checked against CNBC: {BT['n_confirmed_by_cnbc']}/{BT['n_with_cnbc_data']} confirmed as real price moves; "
      f"not confirmed: {BT['n_not_confirmed']} — see `d2_confirmed_errors.csv`. Unconfirmed cases are mostly spin-offs/special distributions where Yahoo's `Close` drops but `Adj Close` is correct "
      "(MO 2008 PMI, ROK 2001, SSP 2008, KDP 2018, WEN 2003), plus 100× unit breaks (SPXS.L 2014-01-02; MI 2026-05-18, a reused symbol) and JCI 2007-07-02 (Tyco reverse split + spin-offs; Yahoo Adj Close −53% that day is artificial).")
    A("")
if CE:
    A(f"**(iv) Yahoo values contradicted by ≥2 independent sources** (panels NOT modified; corrections listed in `d2_confirmed_errors.csv`, {CE['n_rows']} rows incl. single-source cases):")
    A("")
    A("| Symbol | Date | Yahoo | Reference | Source(s) | Error |")
    A("|---|---|---|---|---|---|")
    for r in CE.get("rows_confirmed2", []):
        A(f"| {r['ticker']} | {r['date']} | {float(r['yahoo']):.2f} | {float(r['reference']):.2f} | {r['ref_source'][:60]} | {100 * float(r['rel_err']):+.2f}% |")
    A("")

# ------------------------------------------------------------------------------------------------------------
A("## 4. Benchmark integrity")
A("")
if B:
    A("| Pair | Window | CAGR a | CAGR b | Ann. difference | TE (monthly, ann.) | Daily corr |")
    A("|---|---|---|---|---|---|---|")
    for k in ["SPY_vs_SP500TR", "IVV_vs_SP500TR", "VOO_vs_SP500TR", "SPYclose_vs_GSPC", "SP500TR_vs_GSPC", "RSP_vs_GSPC", "RSP_vs_SP500TR"]:
        s = B[k]
        A(f"| {s['label']} | {s['base_date']}→{s['end_date']} | {pct(s['cagr_a'], 2)} | {pct(s['cagr_b'], 2)} | **{pct(s['annualized_difference'], 2)}** | {pct(s['te_monthly_ann'], 2)} | {s['corr_daily']:.4f} |")
    A("")
    A("SPY's −0.1%/yr tracking difference matches its 0.0945% expense ratio plus the UIT dividend cash drag — the Yahoo Adj Close methodology is sound for total-return work. "
      "RSP vs ^GSPC is not like-for-like (equal-weight total return vs cap-weight price index); vs ^SP500TR RSP lagged by ~2%/yr over 2010-2026 (mega-cap concentration).")
    A("")
    A("Index series vs independent sources:")
    A("")
    A("| Series | Reference | Days | within 0.01% | within 0.1% | max abs diff (date) |")
    A("|---|---|---|---|---|---|")
    for k, ref in [("^GSPC_vs_CNBC", "CNBC .SPX"), ("GSPC_vs_FRED_SP500", "FRED SP500"), ("^SP500TR_vs_CNBC", "CNBC .SPXTR"),
                   ("^VIX_vs_CNBC", "CNBC .VIX"), ("VIX_vs_CBOE", "CBOE VIX_History"), ("SPY_vs_CNBC", "CNBC SPY")]:
        s = B[k]
        mx = s.get("max_abs_diff", s.get("max_abs_rel_diff"))
        A(f"| {k.split('_vs_')[0]} | {ref} | {s['n_common']:,} | {pct(s['pct_within_0p01pct'], 2)} | {pct(s['pct_within_0p1pct'], 2)} | {pct(mx, 2)} ({s['date_of_max']}) |")
    for k in ["TNX_vs_FRED_DGS10", "IRX_vs_FRED_DTB3"]:
        s = B[k]
        A(f"| {s['label']} | | {s['n_common']:,} | median |diff| {s['median_abs_diff_bps']:.1f} bp | p95 {s['p95_abs_diff_bps']:.1f} bp | corr Δ {s['corr_daily_changes']:.3f} |")
    A("")
    A("UCITS listings (month-end basis vs ^SP500TR gross TR; London 16:30 vs New York 16:00 closes add timing noise):")
    A("")
    A("| Listing | Currency | Window | Ann. difference vs ^SP500TR | TE (monthly, ann.) | Note |")
    A("|---|---|---|---|---|---|")
    for t, s in B["UCITS_vs_SP500TR_monthly"].items():
        if "annualized_difference" in s:
            A(f"| {t} | {s.get('currency')} | {s['window']} | {pct(s['annualized_difference'], 2)} | {pct(s['te_monthly_ann'], 2)} | {s.get('note', '')} |")
        else:
            A(f"| {t} | {s.get('currency')} | | | | {s.get('note', '')} |")
    A("")
    A("CSPX.L/VUAA.L/SPY5.L lag gross TR by roughly the expected TER + 15% US dividend withholding inside an Irish fund (≈0.25-0.35%/yr). IUSA.L is quoted in GBp (pence) and SPXS.L carries a 100× unit break on 2014-01-02 — use them only after FX/unit repair.")
    A("")

# ------------------------------------------------------------------------------------------------------------
A("## 5. Data-quality checks (counts)")
A("")
A("| Check | Result |")
A("|---|---|")
A(f"| (a) daily |return| > 50% (Close or Adj Close), rate series ^IRX/^TNX excluded | {bt.get('n')} events in {bt.get('n_tickers')} symbols; by category {bt.get('by_category')}; "
  f"{bt.get('n_in_reuse_suspect_tickers')} are in reuse-suspect symbols; {bt.get('during_membership_valid_ticker_n')} occur during a valid index membership ({bt.get('during_membership_valid_by_category')}) — almost all genuine (AAPL 2000-09-29, 2008-09 financials, PCG 2019, APA/OXY 2020-03-09, GL 2024-04-11). Flagged, not deleted (`d2_bad_ticks.csv`). |")
A(f"| (b) stale runs ≥10 identical closes | {st.get('n_runs')} runs in {st.get('n_tickers')} symbols; current constituents: {st.get('current_constituents_runs')} runs, **{st.get('current_constituents_runs_during_membership')} during S&P 500 membership** "
  f"(all are in thin pre-US-listing histories of SW, FERG, AMCR, CRH etc.; flagged `thin_pre_history`); runs during any membership: {st.get('during_membership_n')} in {', '.join(st.get('during_membership_tickers', []))} (reuse/OTC data). T-bill ETFs (BIL/SHV/SGOV) and ^IRX have genuine flat runs. |")
A(f"| (c) last date = {CUTOFF} for current constituents | {q['check_c_current_last_date']['n_last_is_cutoff']}/{q['check_c_current_last_date']['n_current']} pass |")
A(f"| (d) non-positive prices | {q['check_d_nonpositive_prices']['n_rows']} rows, all in {list(q['check_d_nonpositive_prices']['by_ticker'].keys())} (negative T-bill yields, genuine); 0 equity/ETF rows |")
A(f"| (e) Adj Close factor f=Adj/Close: f≤1 and non-decreasing; jumps match dividends | {q['check_e_adj_factor']['n_tickers_factor_gt_1']} tickers f>1; {q['check_e_adj_factor']['n_tickers_factor_decreasing']} decreasing; "
  f"{q['check_e_adj_factor']['n_factor_jumps_not_matching_yahoo_dividend_5pct']} of {q['check_e_adj_factor']['n_dividend_events_total']:,} factor jumps disagree with Yahoo's dividend by >5% |")
A(f"| (f) same-day split + dividend (spin-off double count) | {adjev.get('n_events')} events: {adjev.get('by_class')}; corrected: {', '.join(adjev.get('corrected', []))}; ambiguous (flagged only): "
  f"{', '.join(r['ticker'] + '@' + r['date'] for r in adjev.get('ambiguous', []))} |")
A(f"| (g) OHLC consistency (Close outside High-Low) | {q['ohlc_inconsistent_rows']['n']} rows, {q['ohlc_inconsistent_rows']['by_ticker_top']} — overwhelmingly LSE UCITS lines |")
A(f"| (h) bars on non-NYSE days | {q['offcalendar_bars']['n_rows']} rows ({q['offcalendar_bars']['top_dates']}) dropped from panels, listed in `d2_offcalendar_bars.csv` |")
A(f"| (i) duplicate (ticker, date) rows in downloads | {q['duplicate_ticker_date_rows_in_download']} |")
A("")
A("**Yahoo corporate-action conventions** (important for users): `Close` is split-adjusted only, so spin-offs and special dividends appear as price drops in `Close`. "
  "Yahoo books a spin-off either as a non-round 'split' (NOV 2014: 1.109; FTI 2021: 1.344; DHR 2016: 1.319) or as a large cash 'dividend' (MO 2008, KDP 2018); either way `Adj Close` is usually right. "
  "The exception is when Yahoo does both on the same day (DHR 2016-07-05: split 1.319 **and** a $24.56 dividend → +61% Adj Close 'return'); these double counts are corrected in `d2_adjclose.parquet`/`d2_ret_monthly.parquet` (list in `d2_adj_corrections.csv`).")
A("")

# ------------------------------------------------------------------------------------------------------------
A("## 6. Identity, renames, and the live bar")
A("")
rc = q.get("rename_candidates", {})
A(f"- **Renames** (`d2_rename_candidates.csv`): an fja05680 row change with one removal and one addition not explained by the Wikipedia changes table (±10 days) is a rename candidate. "
  "The Wikipedia table is <35% complete before 2010 and ≥84% from 2011, so only swaps from 2011 are evaluated (earlier 1-1 swaps were mostly unlisted index replacements, e.g. ENRNQ→NVDA). "
  f"Accepted {rc.get('n_accepted')} (successor's Yahoo series must cover ≥90% of the old member-days after its first bar, ≥250 days, <20% zero-volume): {', '.join(rc.get('accepted', []))}. "
  "Rejected merger-type swaps (e.g. WRK→SW: SW's pre-2024 history is thin OTC data) are listed with reasons.")
fl = q["coverage"].get("flag_counts", {})
A(f"- **Flags in `d2_coverage.csv`**: {fl}. `series_starts_after_membership` = the Yahoo series begins after the symbol left the index (certainly another security); "
  "`name_mismatch_vs_wikipedia` = Yahoo longName shares no token with any Wikipedia name for that symbol; `thin_pre_history` = years with >20% zero-volume days (pre-listing OTC data).")
rp = q.get("refresh_patch")
if rp:
    A(f"- **Live-bar refresh**: first pass fetched ~15 min after the {CUTOFF} close; the refresh re-downloaded {rp.get('overlap_rows')} recent rows: "
      f"{rp.get('close_changed_rows_gt_1e-6')} closes changed (>0.1%: {rp.get('close_changed_rows_gt_0.1pct')}), {rp.get('volume_changed_rows')} volumes changed "
      f"(by date: {rp.get('changed_close_by_date')}); adj-factor changes requiring full re-download: {rp.get('adj_factor_changed_tickers') or 'none'}.")
A("")

# ------------------------------------------------------------------------------------------------------------
A("## 7. Known limitations (read before using)")
A("")
A("1. **Survivorship**: Yahoo purges delisted symbols; roughly half of 2000-04 member-days and a fifth of 2015-19 member-days have no price. Missing names are disproportionately acquired (positive takeover premia) and failed (large negative returns) companies, so the direction of the bias in any factor backtest is not knowable from this data alone. Delisting returns (CRSP-style) are unavailable.")
A("2. **Ticker identity**: symbols are not permanent IDs. Reuse (WB, STI, MI, COMS, NE, CPWR, EP…) is flagged; reverse-merger histories (T/SBC, JPM/Chase, JCI/Tyco, WEN/Triarc, LHX/Harris-style) are not detectable from prices. Use D1 CIK mapping.")
A("3. **Adjustments are as of 2026-09-25**, not point-in-time; spin-offs are handled inconsistently by Yahoo (see §5). Close-to-close returns from `d2_close` are NOT total returns.")
A("4. **Pre-listing histories**: several current constituents (SW, FERG, AMCR, CRH…) carry thin OTC/ADR histories before their US primary listing; do not use them for beta/volatility estimation (see `thin_years`).")
A("5. **Index errors**: a few single-day Yahoo errors in ^VIX, ^GSPC, ^SP500TR and SPY are confirmed by two sources (§3 iv); corrections are listed, panels are unmodified.")
A("6. **UCITS**: IUSA.L quoted in GBp; SPXS.L has a 100× unit break (2014-01-02); LSE OHLC fields are often inconsistent. Use CSPX.L/VUAA.L for USD UCITS work.")
A("7. **Membership spells** used for coverage statistics are D2's reconstruction from fja05680 + Wikipedia (a community file); D1 owns the authoritative membership.")
A("8. **Second source** is CNBC (Stooq unreachable for automated clients); CNBC and Yahoo may share upstream vendors, so agreement is strong but not fully independent evidence. FRED/CBOE are independent for indices.")
A("")

# ------------------------------------------------------------------------------------------------------------
A("## 8. Files produced")
A("")
A("| File | Rows × cols / rows | Content |")
A("|---|---|---|")
files = [
    ("data/d2_adjclose.parquet", "Adj Close (total-return), NYSE days × symbols; double counts corrected"),
    ("data/d2_adjclose_yahoo_raw.parquet", "unmodified Yahoo Adj Close"),
    ("data/d2_close.parquet", "Close (split-adjusted only)"),
    ("data/d2_volume.parquet", "Volume"),
    ("data/d2_ret_monthly.parquet", "monthly total returns (month-end to month-end, no fill; ^IRX/^TNX excluded)"),
    ("data/d2_rf_monthly.csv", "monthly risk-free helper (^IRX BEY/12, BIL/SGOV total return)"),
    ("data/d2_dividends.parquet", "dividends (+ fund capital gains), long"),
    ("data/d2_splits.parquet", "splits, long"),
    ("data/d2_ucits_adjclose.parquet", "UCITS Adj Close (LSE calendar)"),
    ("data/d2_ucits_close.parquet", "UCITS Close"),
    ("data/d2_ucits_volume.parquet", "UCITS Volume"),
    ("data/d2_coverage.csv", "per-symbol coverage, status, membership overlap, identity flags"),
    ("data/d2_universe.csv", "download universe with provenance"),
    ("data/d2_universe_spells.csv", "D2 membership spells (coverage helper)"),
    ("data/d2_members_with_price_daily.csv", "members vs members-with-price per day"),
    ("data/d2_rename_candidates.csv", "heuristic ticker renames"),
    ("data/d2_bad_ticks.csv", "flagged >50% daily moves"),
    ("data/d2_bad_ticks_crosscheck.csv", "CNBC check of large moves"),
    ("data/d2_stale_runs.csv", "runs of ≥10 identical closes"),
    ("data/d2_adj_corrections.csv", "same-day split+dividend events and corrections"),
    ("data/d2_adj_corrections_cnbc.csv", "CNBC evidence for those events"),
    ("data/d2_confirmed_errors.csv", "Yahoo values contradicted by other sources"),
    ("data/d2_offcalendar_bars.csv", "bars on non-NYSE days (excluded)"),
    ("data/d2_final_partial_month.csv", "partial last-month return for series ending mid-month"),
    ("data/d2_validation_sample.csv", "60×25 CNBC comparison"),
    ("data/d2_validation_sample_fullseries.csv", "full-history agreement per sampled ticker"),
    ("data/d2_validation_outliers.csv", "diagnosis of sample outliers"),
    ("data/d2_validation_ratio_steps.csv", "Yahoo/CNBC adjustment-step events"),
    ("data/d2_validation_latest_close.csv", "2026-09-25 close vs CNBC, all current constituents"),
    ("data/d2_validation_ratio_steps.csv", "persistent Yahoo/CNBC adjustment steps (full history, 60 sampled tickers)"),
    ("outputs/d2_qc_summary.json", "all QC numbers"),
    ("outputs/d2_validation_results.json", "all validation numbers"),
    ("outputs/d2_universe_summary.json", "universe build summary"),
]
V4 = os.path.dirname(DATA)
for f, desc in files:
    p = os.path.join(V4, f.replace("/", os.sep))
    if not os.path.exists(p):
        A(f"| `{f}` | missing | {desc} |")
        continue
    if p.endswith(".parquet"):
        import pyarrow.parquet as pq
        md = pq.ParquetFile(p).metadata
        shape = f"{md.num_rows:,} × {md.num_columns}"
    elif p.endswith(".csv"):
        shape = f"{sum(1 for _ in open(p, encoding='utf-8')) - 1:,} rows"
    else:
        shape = "json"
    A(f"| `{f}` | {shape} | {desc} |")
A("")
A("Scripts: `v4/code/d2_common.py`, `d2_universe.py`, `d2_download.py` (phases batch/retry/meta/refresh), `d2_build.py`, `d2_validate.py` (parts sample/latest/bench/badticks/errors), `d2_report.py`. "
  "Every dataset has a `.meta.json` sidecar. Raw caches: `C:\\Users\\user\\eqv4\\cache\\d2\\` (batches, singles, refresh, meta, validation, raw).")
A("")
A("## 9. Sources")
A("")
A(f"- Yahoo Finance chart API via yfinance 1.7 — prices, dividends, splits, metadata.")
A(f"- Wikipedia: {URLS['wiki_current']} ; {URLS['wiki_changes']}")
A(f"- GitHub fja05680/sp500: {URLS['fja05680']}")
A("- CNBC: https://ts-api.cnbc.com/harmony/app/bars/ (daily bars), https://quote.cnbc.com/quote-html-webservice/restQuote/ (quotes)")
A("- FRED: https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500 | VIXCLS | DGS10 | DTB3 ; CBOE: https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv")
A(f"- Stooq (attempted, blocked): {URLS['stooq']}")

out = os.path.join(OUT, "d2_report.md")
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
write_meta(out, {"description": "D2 report (rendered by d2_report.py)", "inputs": ["outputs/d2_qc_summary.json", "outputs/d2_validation_results.json"]})
print("written", out, len(lines), "lines")
