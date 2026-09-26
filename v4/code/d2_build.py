"""d2_build.py - assemble cached Yahoo downloads into clean panels + coverage + data-quality flags.

Inputs : C:\\Users\\user\\eqv4\\cache\\d2\\{batches,singles,refresh,redownload,meta}
Outputs (v4/data):
  d2_adjclose.parquet, d2_close.parquet, d2_volume.parquet     wide, index=date (NYSE trading days), cols=ticker
  d2_ucits_adjclose.parquet, d2_ucits_close.parquet, d2_ucits_volume.parquet   (LSE calendar, .L listings)
  d2_dividends.parquet (long), d2_splits.parquet (long)
  d2_ret_monthly.parquet   month-end -> month-end total return from Adj Close (no fill)
  d2_final_partial_month.csv  prior month-end -> last available price for series that end mid-month
  d2_coverage.csv, d2_bad_ticks.csv, d2_stale_runs.csv, d2_offcalendar_bars.csv
  ../outputs/d2_qc_summary.json
"""
import os
import re
import glob
import json
import difflib
import numpy as np
import pandas as pd

from d2_common import (DATA, OUT, CACHE, BATCH_DIR, SINGLE_DIR, META_DIR, CUTOFF, URLS, utcnow, write_meta)

PRICE_COLS = ["Open", "High", "Low", "Close", "Adj Close", "Volume", "Dividends", "Stock Splits", "Capital Gains"]
CUT = pd.Timestamp(CUTOFF)
RENAME_MIN_DATE = pd.Timestamp("2011-01-01")  # Wikipedia changes table >=84% complete from 2011 (see report)
US_EXCH_OK = {"NYQ", "NMS", "NGM", "NCM", "ASE", "PCX", "BTS", "NYS", "NAS", "NYSE", "NasdaqGS", "NasdaqGM", "NasdaqCM"}


# ----------------------------------------------------------------------------------------------------------
def load_raw():
    parts = []
    for pri, pattern in [(0, os.path.join(BATCH_DIR, "b*.parquet")),
                         (1, os.path.join(SINGLE_DIR, "s_*.parquet")),
                         (2, os.path.join(CACHE, "refresh", "refresh_*.parquet")),
                         (3, os.path.join(CACHE, "redownload", "r_*.parquet"))]:
        for f in sorted(glob.glob(pattern)):
            d = pd.read_parquet(f)
            if d.empty:
                continue
            d["_pri"] = pri
            d["_src"] = os.path.basename(f)
            parts.append(d)
    raw = pd.concat(parts, ignore_index=True)
    raw["date"] = pd.to_datetime(raw["date"]).dt.normalize()
    raw["ticker"] = raw["ticker"].astype(str)
    return raw


def apply_priority(raw):
    """Refresh rows overwrite the batch rows for the same (ticker,date); full re-downloads replace a ticker entirely."""
    info = {}
    red = raw[raw["_pri"] == 3]
    if len(red):
        red_t = set(red["ticker"])
        raw = raw[~(raw["ticker"].isin(red_t) & (raw["_pri"] < 3))]
        info["tickers_fully_redownloaded"] = sorted(red_t)
    # refresh patch: compare before overwrite
    ref = raw[raw["_pri"] == 2]
    base = raw[raw["_pri"] < 2]
    patch_stats = {}
    if len(ref):
        m = base.merge(ref, on=["ticker", "date"], suffixes=("_old", "_new"))
        dc = (m["Close_new"] / m["Close_old"] - 1).abs()
        da = (m["Adj Close_new"] / m["Adj Close_old"] - 1).abs()
        patch_stats = {
            "overlap_rows": int(len(m)),
            "close_changed_rows_gt_1e-6": int((dc > 1e-6).sum()),
            "close_changed_rows_gt_0.1pct": int((dc > 1e-3).sum()),
            "adj_changed_rows_gt_1e-6": int((da > 1e-6).sum()),
            "volume_changed_rows": int((m["Volume_new"] != m["Volume_old"]).sum()),
            "changed_close_by_date": m.loc[dc > 1e-6, "date"].dt.strftime("%Y-%m-%d").value_counts().to_dict(),
            "new_rows_not_in_base": int(len(ref) - len(m)),
        }
        # tickers whose adj factor changed on overlapping days before the last date -> need full re-download
        m["f_old"] = m["Adj Close_old"] / m["Close_old"]
        m["f_new"] = m["Adj Close_new"] / m["Close_new"]
        early = m[m["date"] < CUT]
        chg = early.loc[(early["f_new"] / early["f_old"] - 1).abs() > 1e-5, "ticker"].unique().tolist()
        patch_stats["adj_factor_changed_tickers"] = sorted(chg)
        info["refresh_patch"] = patch_stats
    raw = raw.sort_values(["ticker", "date", "_pri"]).drop_duplicates(["ticker", "date"], keep="last")
    return raw, info


def us_calendar(raw):
    us = raw[~raw["ticker"].str.endswith(".L")]
    g = us.loc[us["ticker"] == "^GSPC", "date"]
    cal = pd.DatetimeIndex(sorted(g.unique()))
    # alive counts per date for sanity: dates with many stock bars but no ^GSPC bar
    eq = us[~us["ticker"].str.startswith("^")]
    cnt = eq.groupby("date")["ticker"].nunique()
    span = eq.groupby("ticker")["date"].agg(["min", "max"])
    # alive tickers per date (approx): count of tickers whose [min,max] covers the date
    dates = cnt.index
    starts = np.searchsorted(np.sort(span["min"].values), dates.values, side="right")
    ends = np.searchsorted(np.sort(span["max"].values), dates.values, side="left")
    alive = starts - ends
    frac = pd.Series(cnt.values / np.maximum(alive, 1), index=dates)
    missing_in_gspc = frac[(~frac.index.isin(cal)) & (frac > 0.5)]
    cal = cal.union(pd.DatetimeIndex(missing_in_gspc.index))
    cal = cal[cal <= CUT]
    return cal, frac, missing_in_gspc


def lse_calendar(raw):
    uk = raw[raw["ticker"].str.endswith(".L")]
    cnt = uk.groupby("date")["ticker"].nunique()
    return pd.DatetimeIndex(sorted(cnt.index[cnt.index <= CUT]))


def norm_name(s):
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    stop = {"inc", "corp", "corporation", "company", "co", "ltd", "plc", "the", "group", "holdings", "holding",
            "class", "a", "b", "c", "and", "of", "international", "intl", "incorporated", "limited", "nv", "sa", "ag",
            "trust", "common", "stock", "new", "de", "lp", "llc", "cl", "shs", "ordinary", "shares", "the"}
    toks = [t for t in s.split() if t and t not in stop]
    return toks


def spells_dict(spells):
    d = {}
    for _, r in spells.iterrows():
        e = r["end_excl"] if pd.notna(r["end_excl"]) else CUT + pd.Timedelta(days=1)
        d.setdefault(r["ticker"], []).append((r["start"], e))
    return d


def in_spells(sd, t, a, b=None):
    """True if [a,b] overlaps any membership spell of ticker t."""
    b = a if b is None else b
    for s, e in sd.get(t, []):
        if a < e and b >= s:
            return True
    return False


def rename_candidates(clo, vol, spells, universe, meta):
    """Heuristic ticker-rename detection from the fja05680 file: on a row-to-row change, a removal and an addition
    that the Wikipedia changes table does not explain (within +-10 days) are paired when exactly one of each exists.
    Accepted if: the old ticker has no Yahoo data (or it ends within 10 days of the swap) AND the new ticker's Yahoo
    series starts >= 250 trading days before the swap with <20% zero-volume days in the prior year."""
    import io as _io
    from d2_common import RAW, to_yahoo
    h = pd.read_csv(os.path.join(RAW, "fja05680_hist.csv"))
    h["date"] = pd.to_datetime(h["date"])
    sets = [set(s.split(",")) for s in h["tickers"]]
    ch = pd.read_html(_io.StringIO(open(os.path.join(RAW, "wiki_sp500_historical.html"), "rb").read().decode("utf-8")))[0]
    ch.columns = ["date", "add_t", "add_n", "rem_t", "rem_n", "reason", "refs"]
    ch["date"] = pd.to_datetime(ch["date"], format="mixed")
    cl = lambda x: re.findall(r"[A-Z][A-Z0-9]*(?:\.[A-Z])?", str(x).upper()) if isinstance(x, str) else []
    out = []
    for i in range(1, len(h)):
        d = h["date"][i]
        if d < pd.Timestamp("2000-01-01"):
            continue
        rem = sets[i - 1] - sets[i]; add = sets[i] - sets[i - 1]
        w = ch[(ch["date"] >= d - pd.Timedelta(days=10)) & (ch["date"] <= d + pd.Timedelta(days=10))]
        ka = set(x for c in w["add_t"] for x in cl(c)); kr = set(x for c in w["rem_t"] for x in cl(c))
        ru, au = sorted(rem - kr), sorted(add - ka)
        if len(ru) == 1 and len(au) == 1:
            out.append(dict(swap_date=d, old_ticker=to_yahoo(ru[0])[0], new_ticker=to_yahoo(au[0])[0], pair="1-1"))
        elif ru or au:
            out.append(dict(swap_date=d, old_ticker=";".join(ru), new_ticker=";".join(au), pair="ambiguous"))
    rc = pd.DataFrame(out)
    # resolve chains (e.g. VIAC->PARA->PSKY) forward in time, using only swaps >= RENAME_MIN_DATE
    succ = {}
    for r in rc[(rc["pair"] == "1-1") & (rc["swap_date"] >= RENAME_MIN_DATE)].sort_values("swap_date").itertuples():
        succ.setdefault(r.old_ticker, []).append((r.new_ticker, r.swap_date))
    sd = spells_dict(spells)
    cal = clo.index
    ucur = universe.set_index("ticker")
    zero_vol = (vol.fillna(-1) == 0) & clo.notna()

    def reuse_like(t, swap_date):
        """old symbol's own Yahoo data looks like a different security."""
        if t not in clo.columns or clo[t].notna().sum() == 0:
            return False
        names = []
        if t in ucur.index:
            for c in ("current_name", "wiki_names"):
                v = ucur.at[t, c]
                if isinstance(v, str):
                    names += v.split(";")
        ym = meta.get(t, {})
        if name_match(ym.get("longName") or ym.get("shortName"), names) == "mismatch":
            return True
        mdays = pd.DatetimeIndex([])
        for s, e in sd.get(t, []):
            mdays = mdays.union(cal[(cal >= max(s, pd.Timestamp("2000-01-01"))) & (cal < min(e, swap_date))])
        have = clo[t].reindex(mdays).notna()
        if have.sum() >= 20 and zero_vol[t].reindex(mdays)[have].mean() > 0.2:
            return True
        return False
    res = []
    for r in rc.itertuples():
        if r.pair != "1-1":
            res.append(dict(swap_date=r.swap_date.date(), old_ticker=r.old_ticker, new_ticker=r.new_ticker, chain="",
                            successor_used=None, old_has_yahoo=None, successor_cover_old_member_days=None,
                            successor_zero_vol_frac=None, accepted=False,
                            note="unpaired/ambiguous change not explained by Wikipedia table (not a 1-1 swap)"))
            continue
        if r.swap_date < RENAME_MIN_DATE:
            res.append(dict(swap_date=r.swap_date.date(), old_ticker=r.old_ticker, new_ticker=r.new_ticker, chain="",
                            successor_used=None, old_has_yahoo=None, successor_cover_old_member_days=None,
                            successor_zero_vol_frac=None, accepted=False,
                            note="not evaluated: Wikipedia changes table <85% complete before 2011, so an unexplained "
                                 "1-1 swap is more likely an unlisted index replacement than a rename"))
            continue
        old = r.old_ticker
        chain, t, seen, tdate = [old], old, {old}, r.swap_date
        while t in succ and len(chain) < 10:
            nxt = [(n, d) for n, d in succ[t] if d >= tdate and n not in seen]
            if not nxt:
                break
            t, tdate = nxt[0]; chain.append(t); seen.add(t)
        so = clo[old].dropna() if old in clo.columns else pd.Series(dtype=float)
        # old symbol usable for remap if Yahoo has nothing for it, its data ends at the swap, its Yahoo series only
        # starts after the swap, or its data looks like a different security (name mismatch / thin during membership)
        old_ok = ((len(so) == 0) or (abs((so.index[-1] - r.swap_date).days) <= 10) or (so.index[0] > r.swap_date)
                  or reuse_like(old, r.swap_date))
        # old ticker's member days since 2000 up to the swap date
        mdays = pd.DatetimeIndex([])
        for s, e in sd.get(old, []):
            mdays = mdays.union(cal[(cal >= max(s, pd.Timestamp("2000-01-01"))) & (cal < min(e, r.swap_date))])
        used, cover, zvf, acc = None, None, None, False
        for cand in chain[1:]:
            if cand not in clo.columns or len(mdays) == 0 or clo[cand].notna().sum() == 0:
                continue
            first_c = clo[cand].first_valid_index()
            md_c = mdays[mdays >= first_c]          # successor can only speak for days after its own first bar
            if len(md_c) < 250:
                continue
            have = clo[cand].reindex(md_c).notna()
            v = vol[cand].reindex(md_c)
            cov_ = float(have.mean())
            zv_ = float((v[have].fillna(0) == 0).mean()) if have.any() else 1.0
            if cov_ >= 0.9 and zv_ < 0.2:
                used, cover, zvf, acc = cand, float(have.sum() / len(mdays)), zv_, bool(old_ok)
                break
            if used is None:
                cover, zvf = cov_, zv_
        note = []
        if not old_ok:
            note.append("old ticker has independent, plausible Yahoo data - not remapped")
        if used is None:
            note.append("no successor in chain has liquid Yahoo data (>=250 days, >=90% of old member-days after its first bar)")
        res.append(dict(swap_date=r.swap_date.date(), old_ticker=old, new_ticker=r.new_ticker, chain=">".join(chain),
                        successor_used=used, old_has_yahoo=len(so) > 0, successor_cover_old_member_days=cover,
                        successor_zero_vol_frac=zvf, accepted=acc and used is not None, note="; ".join(note)))
    return pd.DataFrame(res)


def name_match(yname, names):
    if not yname or not names:
        return "n/a"
    yt = norm_name(yname)
    if not yt:
        return "n/a"
    best = 0.0
    for n in names:
        nt = norm_name(n)
        if not nt:
            continue
        if set(yt) & set(nt):
            return "match"
        # prefix match for abbreviations (e.g. 'jpmorgan' vs 'jp morgan')
        a, b = "".join(yt), "".join(nt)
        if a[:5] == b[:5] and len(a) >= 5:
            return "match"
        best = max(best, difflib.SequenceMatcher(None, " ".join(yt), " ".join(nt)).ratio())
    return "match" if best >= 0.6 else "mismatch"


# ----------------------------------------------------------------------------------------------------------
def main():
    qc = {"built_utc": utcnow()}
    raw = load_raw()
    qc["raw_rows_all_sources"] = int(len(raw))
    dup = raw[raw["_pri"] < 2].duplicated(["ticker", "date"]).sum()
    qc["duplicate_ticker_date_rows_in_download"] = int(dup)
    raw, info = apply_priority(raw)
    qc.update(info)
    raw = raw[raw["date"] <= CUT]
    u = pd.read_csv(os.path.join(DATA, "d2_universe.csv"))
    meta = json.load(open(os.path.join(META_DIR, "yahoo_meta.json"))) if os.path.exists(
        os.path.join(META_DIR, "yahoo_meta.json")) else {}

    # ---------------- calendars ----------------
    cal, frac, extra_days = us_calendar(raw)
    lcal = lse_calendar(raw)
    qc["us_calendar"] = {"first": str(cal[0].date()), "last": str(cal[-1].date()), "n_days": int(len(cal)),
                         "days_added_beyond_gspc": [str(d.date()) for d in extra_days.index]}
    qc["lse_calendar"] = {"first": str(lcal[0].date()) if len(lcal) else None, "n_days": int(len(lcal))}

    is_uk = raw["ticker"].str.endswith(".L")
    us = raw[~is_uk].copy()
    uk = raw[is_uk].copy()

    # ---------------- off-calendar bars ----------------
    off = us[~us["date"].isin(cal)]
    off_tab = off[["ticker", "date", "Close", "Volume", "Dividends", "Stock Splits"]].copy()
    off_tab["weekday"] = off_tab["date"].dt.day_name()
    off_tab.to_csv(os.path.join(DATA, "d2_offcalendar_bars.csv"), index=False)
    qc["offcalendar_bars"] = {"n_rows": int(len(off)), "n_with_price": int(off["Close"].notna().sum()),
                              "n_dividend_only": int((off["Close"].isna() & (off["Dividends"].fillna(0) != 0)).sum()),
                              "n_weekend": int(off["date"].dt.weekday.ge(5).sum()),
                              "top_dates": off["date"].dt.strftime("%Y-%m-%d").value_counts().head(15).to_dict()}

    # ---------------- dividends / splits (keep all, incl. off-calendar) ----------------
    div = raw.loc[raw["Dividends"].fillna(0) != 0, ["date", "ticker", "Dividends"]].rename(columns={"Dividends": "dividend"})
    cg = raw.loc[raw["Capital Gains"].fillna(0) != 0, ["date", "ticker", "Capital Gains"]].rename(columns={"Capital Gains": "capital_gain"})
    divs = div.merge(cg, on=["date", "ticker"], how="outer").sort_values(["ticker", "date"])
    divs["on_trading_day"] = divs["date"].isin(cal) | divs["ticker"].str.endswith(".L")
    divs.to_parquet(os.path.join(DATA, "d2_dividends.parquet"), index=False)
    spl = raw.loc[raw["Stock Splits"].fillna(0) != 0, ["date", "ticker", "Stock Splits"]].rename(
        columns={"Stock Splits": "split_ratio"}).sort_values(["ticker", "date"])
    spl.to_parquet(os.path.join(DATA, "d2_splits.parquet"), index=False)

    # ---------------- wide panels ----------------
    us_on = us[us["date"].isin(cal)]
    adj = us_on.pivot(index="date", columns="ticker", values="Adj Close").reindex(cal).sort_index(axis=1)
    clo = us_on.pivot(index="date", columns="ticker", values="Close").reindex(cal).sort_index(axis=1)
    vol = us_on.pivot(index="date", columns="ticker", values="Volume").reindex(cal).sort_index(axis=1)
    # rows present but with NaN close are dropped by construction (keep NaN)
    for df in (adj, clo, vol):
        df.index.name = "date"
        df.columns.name = None
    # ---- same-day split + dividend events: detect Yahoo double-counting of spin-offs ----
    # Yahoo sometimes encodes a spin-off as a (non-round) split AND books the spun-off value as a cash dividend on
    # the same ex-date, so Adj Close counts the distribution twice. Signature: dividend >= 5% of prior close, |Close
    # return| < 10% (no price drop from the 'dividend'), Adj return exceeds Close return by > 5pp. Only this
    # unambiguous signature is corrected (pre-event Adj Close history rescaled so the factor is continuous).
    adj_raw = adj.copy()
    adj_raw.to_parquet(os.path.join(DATA, "d2_adjclose_yahoo_raw.parquet"))
    sde = div.merge(spl, on=["date", "ticker"], how="inner")
    ev_rows = []
    for r in sde.itertuples():
        t = r.ticker
        if t not in clo.columns:
            continue
        cc = clo[t].dropna()
        if r.date not in cc.index:
            continue
        i = cc.index.get_loc(r.date)
        if i == 0:
            continue
        d0 = cc.index[i - 1]
        pc = cc.iloc[i - 1]
        rc = cc.iloc[i] / pc - 1
        ra = adj_raw.at[r.date, t] / adj_raw.at[d0, t] - 1
        frac = r.dividend / pc
        if frac < 0.02:
            cls = "small_dividend_with_split (plausible stock dividend + cash)"
        elif frac >= 0.05 and abs(rc) < 0.10 and (ra - rc) > 0.05:
            cls = "double_count_corrected"
        elif (ra - rc) > 0.05 or abs(rc) > 0.15:
            cls = "ambiguous_flagged"
        else:
            cls = "plausible"
        ev_rows.append(dict(ticker=t, date=r.date.date(), split_ratio=r.split_ratio, dividend=r.dividend,
                            dividend_frac_prev_close=frac, ret_close=rc, ret_adj_yahoo=ra, classification=cls))
    sdev = pd.DataFrame(ev_rows)
    corr = []
    for r in sdev[sdev["classification"] == "double_count_corrected"].itertuples() if len(sdev) else []:
        d = pd.Timestamp(r.date)
        cc = clo[r.ticker].dropna()
        d0 = cc.index[cc.index.get_loc(d) - 1]
        f_prev = adj.at[d0, r.ticker] / clo.at[d0, r.ticker]
        f_now = adj.at[d, r.ticker] / clo.at[d, r.ticker]
        k = f_now / f_prev
        adj.loc[adj.index < d, r.ticker] = adj.loc[adj.index < d, r.ticker] * k
        corr.append(dict(ticker=r.ticker, date=r.date, prior_history_scale=k,
                         ret_adj_after=float(adj.at[d, r.ticker] / adj.at[d0, r.ticker] - 1)))
    if len(sdev):
        sdev = sdev.merge(pd.DataFrame(corr) if corr else pd.DataFrame(columns=["ticker", "date", "prior_history_scale", "ret_adj_after"]),
                          on=["ticker", "date"], how="left")
    sdev.to_csv(os.path.join(DATA, "d2_adj_corrections.csv"), index=False)
    qc["adj_split_dividend_events"] = {"n_events": int(len(sdev)),
                                       "by_class": sdev["classification"].value_counts().to_dict() if len(sdev) else {},
                                       "corrected": [f"{c['ticker']}@{c['date']} x{c['prior_history_scale']:.4f}" for c in corr],
                                       "ambiguous": sdev[sdev["classification"] == "ambiguous_flagged"][["ticker", "date", "ret_close", "ret_adj_yahoo"]].astype(str).to_dict("records") if len(sdev) else []}
    adj.to_parquet(os.path.join(DATA, "d2_adjclose.parquet"))
    clo.to_parquet(os.path.join(DATA, "d2_close.parquet"))
    vol.to_parquet(os.path.join(DATA, "d2_volume.parquet"))
    uadj = uk.pivot(index="date", columns="ticker", values="Adj Close").reindex(lcal).sort_index(axis=1)
    uclo = uk.pivot(index="date", columns="ticker", values="Close").reindex(lcal).sort_index(axis=1)
    uvol = uk.pivot(index="date", columns="ticker", values="Volume").reindex(lcal).sort_index(axis=1)
    for df, nm in ((uadj, "adjclose"), (uclo, "close"), (uvol, "volume")):
        df.index.name = "date"; df.columns.name = None
        df.to_parquet(os.path.join(DATA, f"d2_ucits_{nm}.parquet"))

    # ---------------- monthly total returns ----------------
    me = pd.Series(cal, index=cal).groupby([cal.year, cal.month]).max()
    me_dates = pd.DatetimeIndex(me.values)
    # only complete months: the last month-end must be a true month end (Sept 2026 is partial at the cutoff)
    last_complete = me_dates[me_dates < pd.Timestamp("2026-09-01")]
    me_dates = last_complete
    adj_me = adj.reindex(me_dates)
    ret_m = adj_me / adj_me.shift(1) - 1.0
    ret_m = ret_m.drop(columns=[c for c in ("^IRX", "^TNX") if c in ret_m.columns])  # yields, not prices
    # risk-free helper: ^IRX is the 13-week T-bill discount yield (%); convert to bond-equivalent yield and use the
    # previous month-end value / 12 as the (ex-ante) monthly risk-free rate; BIL total return as investable proxy
    irx = clo["^IRX"].reindex(me_dates) / 100.0
    bey = 365 * irx / (360 - 91 * irx)
    rf = pd.DataFrame({"irx_discount_yield_pct": irx * 100, "irx_bond_equiv_yield": bey,
                       "rf_month_from_prev_irx": bey.shift(1) / 12.0,
                       "bil_total_return": ret_m["BIL"] if "BIL" in ret_m.columns else np.nan,
                       "sgov_total_return": ret_m["SGOV"] if "SGOV" in ret_m.columns else np.nan})
    rf.index.name = "month_end"
    rf.to_csv(os.path.join(DATA, "d2_rf_monthly.csv"))
    write_meta(os.path.join(DATA, "d2_rf_monthly.csv"), {"source": "derived from Yahoo ^IRX (CBOE 13-week T-bill discount yield) and BIL/SGOV Adj Close",
        "rows": int(len(rf)), "definition": "rf_month_from_prev_irx = BEY(previous month-end)/12 with BEY = 365*d/(360-91*d); "
        "bil_total_return/sgov_total_return = ETF monthly total returns (investable cash proxies, net of fees).",
        "caveats": ["^IRX is a 13-week (not 1-month) bill yield; differs from Fama-French RF (1-month bill) by a few bp/month in steep curves."]})
    # UCITS: own LSE month-ends, labelled with the US month-end of the same month
    if len(lcal):
        lme = pd.Series(lcal, index=lcal).groupby([lcal.year, lcal.month]).max()
        uadj_me = uadj.reindex(pd.DatetimeIndex(lme.values))
        uret = uadj_me / uadj_me.shift(1) - 1.0
        key = {(d.year, d.month): d for d in me_dates}
        uret.index = [key.get((d.year, d.month), pd.NaT) for d in uret.index]
        uret = uret[uret.index.notna()]
        ret_m = ret_m.join(uret, how="left")
    ret_m.index.name = "month_end"
    ret_m.to_parquet(os.path.join(DATA, "d2_ret_monthly.parquet"))
    # mid-life missing month-end prices (ticker trades in the month but not on the month-end day)
    first = adj.apply(lambda s: s.first_valid_index())
    last = adj.apply(lambda s: s.last_valid_index())
    has_month = adj.notna().groupby([adj.index.year, adj.index.month]).any()
    has_month.index = pd.DatetimeIndex([me.loc[(y, m)] for y, m in has_month.index])
    has_month = has_month.reindex(me_dates)
    alive_mask = pd.DataFrame(False, index=me_dates, columns=adj.columns)
    for t in adj.columns:
        if pd.notna(first[t]):
            alive_mask[t] = (me_dates >= first[t]) & (me_dates <= last[t])
    miss_me = (has_month & adj_me.isna() & alive_mask)
    qc["monthly"] = {"n_months": int(len(me_dates)), "first_month_end": str(me_dates[0].date()),
                     "last_month_end": str(me_dates[-1].date()),
                     "n_nonnull_returns": int(ret_m.notna().sum().sum()),
                     "midlife_missing_month_end_prices": int(miss_me.sum().sum()),
                     "midlife_missing_examples": [f"{t}@{d.date()}" for d, t in
                                                  list(miss_me.stack()[lambda s: s].index)[:20]]}
    # final partial month for series that end before the cutoff
    fp = []
    for t in adj.columns:
        lv = last[t]
        if pd.isna(lv) or lv >= CUT:
            continue
        prior_me = me_dates[me_dates < lv]
        if len(prior_me) == 0:
            continue
        pme = prior_me[-1]
        if lv in set(me_dates):
            continue  # ended exactly on a month-end: monthly panel already has the last full return
        p0, p1 = adj.at[pme, t], adj.at[lv, t]
        fp.append(dict(ticker=t, prior_month_end=pme.date(), last_date=lv.date(),
                       partial_return=(p1 / p0 - 1) if pd.notna(p0) and pd.notna(p1) else np.nan))
    fpd = pd.DataFrame(fp)
    fpd.to_csv(os.path.join(DATA, "d2_final_partial_month.csv"), index=False)

    # ---------------- per-ticker coverage ----------------
    cal_pos = pd.Series(np.arange(len(cal)), index=cal)
    spells = pd.read_csv(os.path.join(DATA, "d2_universe_spells.csv"), parse_dates=["start", "end_excl"])
    sd = spells_dict(spells)
    rc = rename_candidates(clo, vol, spells, u, meta)
    rc.to_csv(os.path.join(DATA, "d2_rename_candidates.csv"), index=False)
    remap = {r.old_ticker: r.successor_used for r in rc.itertuples() if r.accepted}
    qc["rename_candidates"] = {"n_rows": int(len(rc)), "n_1to1": int((rc["chain"] != "").sum()),
                               "n_accepted": int(rc["accepted"].sum()),
                               "accepted": [f"{r.old_ticker}->{r.successor_used}@{r.swap_date}" for r in rc.itertuples() if r.accepted],
                               "rejected_1to1": [f"{r.old_ticker}->{r.new_ticker}@{r.swap_date}: {r.note}" for r in rc.itertuples() if (not r.accepted) and r.chain]}
    # zero-volume / thin-history statistics (US panel)
    zero_vol = ((vol.fillna(-1) == 0) & clo.notna())
    zv_year = zero_vol.groupby(zero_vol.index.year).sum() / clo.notna().groupby(clo.index.year).sum().replace(0, np.nan)
    cov = []
    for _, r in u.iterrows():
        t = r["ticker"]
        rec = dict(ticker=t, ticker_orig=r["ticker_orig"], asset_class=r["asset_class"], in_current=r["in_current"],
                   in_fja_since2000=r["in_fja_since2000"], source_lists=r["sources"])
        if t.endswith(".L"):
            s = uclo[t].dropna() if t in uclo.columns else pd.Series(dtype=float)
            pos = pd.Series(np.arange(len(lcal)), index=lcal)
        else:
            s = clo[t].dropna() if t in clo.columns else pd.Series(dtype=float)
            pos = cal_pos
        if len(s) == 0:
            rec.update(first_date=None, last_date=None, n_obs=0, n_gaps_gt5=0, max_gap_days=None, status="no_data")
        else:
            p = pos.reindex(s.index).values
            gaps = np.diff(p) - 1
            rec.update(first_date=s.index[0].date(), last_date=s.index[-1].date(), n_obs=int(len(s)),
                       n_gaps_gt5=int((gaps > 5).sum()), max_gap_days=int(gaps.max()) if len(gaps) else 0,
                       status="active" if s.index[-1] >= CUT else "ended_before_2026-09-25")
        if t in clo.columns and len(s):
            nz = int(zero_vol[t].sum())
            thin_years = zv_year[t][zv_year[t] > 0.2].index.tolist() if t in zv_year.columns else []
            rec.update(n_zero_volume_days=nz, zero_volume_frac=nz / len(s),
                       thin_years=";".join(str(y) for y in thin_years),
                       thin_history_until=(str(max(thin_years)) if thin_years else None))
        else:
            rec.update(n_zero_volume_days=None, zero_volume_frac=None, thin_years=None, thin_history_until=None)
        rec["rename_successor"] = remap.get(t)
        m = meta.get(t, {})
        rec.update(yahoo_name=m.get("longName") or m.get("shortName"), yahoo_type=m.get("instrumentType"),
                   yahoo_exchange=m.get("exchangeName"), yahoo_currency=m.get("currency"),
                   yahoo_first_trade=(str(m.get("firstTradeDate"))[:10] if m.get("firstTradeDate") else None))
        # membership overlap
        spt = spells[spells["ticker"] == t]
        md = 0; mc = 0; mz = 0; mcr = 0
        mfirst = spt["start"].min() if len(spt) else pd.NaT
        mlast = (CUT if spt["end_excl"].isna().any() else spt["end_excl"].max()) if len(spt) else pd.NaT
        succ_t = remap.get(t)
        s_succ = clo[succ_t].dropna() if (succ_t and succ_t in clo.columns) else pd.Series(dtype=float)
        for _, sp_ in spt.iterrows():
            a = max(sp_["start"], pd.Timestamp("2000-01-01"))
            b = sp_["end_excl"] if pd.notna(sp_["end_excl"]) else CUT + pd.Timedelta(days=1)
            days = cal[(cal >= a) & (cal < b)]
            md += len(days)
            if len(s):
                inm = s.index.isin(days)
                mc += int(inm.sum())
                if t in zero_vol.columns:
                    mz += int(zero_vol[t].reindex(s.index[inm]).sum())
            own = s.index[s.index.isin(days)] if len(s) else pd.DatetimeIndex([])
            extra = s_succ.index[s_succ.index.isin(days) & ~s_succ.index.isin(own)] if len(s_succ) else []
            mcr += len(own) + len(extra)
        rec.update(member_first=mfirst.date() if pd.notna(mfirst) else None,
                   member_last_excl=(None if (len(spt) and spt["end_excl"].isna().any()) else (mlast.date() if pd.notna(mlast) else None)),
                   member_days_since2000=md, member_days_covered=mc,
                   member_coverage=(mc / md) if md else np.nan,
                   member_days_covered_incl_rename=mcr,
                   member_zero_volume_frac=(mz / mc) if mc else np.nan)
        # identity / reuse heuristics
        names = []
        for c in ("current_name", "wiki_names"):
            v = r.get(c)
            if isinstance(v, str):
                names += v.split(";")
        rec["wiki_names"] = r.get("wiki_names") if isinstance(r.get("wiki_names"), str) else None
        rec["name_check"] = name_match(rec["yahoo_name"], names)
        flags = []
        if len(s) and md:
            if pd.notna(mlast) and s.index[0] >= mlast:
                flags.append("series_starts_after_membership")  # certainly a different/relisted security
            elif pd.notna(mfirst) and s.index[0] > max(mfirst, pd.Timestamp("2000-01-01")) + pd.Timedelta(days=45):
                flags.append("series_starts_after_member_start")
            if pd.notna(mlast) and mlast < CUT and s.index[-1] < mlast - pd.Timedelta(days=10):
                flags.append("series_ends_before_membership_end")
        if rec["name_check"] == "mismatch":
            flags.append("name_mismatch_vs_wikipedia")
        if rec["yahoo_exchange"] and r["asset_class"] == "equity" and rec["yahoo_exchange"] not in US_EXCH_OK:
            flags.append(f"non_major_exchange:{rec['yahoo_exchange']}")
        if pd.notna(rec.get("member_zero_volume_frac")) and rec["member_zero_volume_frac"] > 0.05:
            flags.append("thin_during_membership")
        if rec.get("thin_history_until") and r["asset_class"] == "equity":
            flags.append("thin_pre_history")
        rec["flags"] = ";".join(flags)
        rec["reuse_suspect"] = bool(("series_starts_after_membership" in flags) or
                                    ("name_mismatch_vs_wikipedia" in flags and not r["in_current"]))
        cov.append(rec)
    cov = pd.DataFrame(cov)

    # ---------------- QC (a): large daily moves ----------------
    splits_by_t = {t: g for t, g in spl.groupby("ticker")}
    divmap_all = {(t, d): v for t, d, v in zip(div["ticker"], div["date"], div["dividend"])}
    bad = []
    RATE_SERIES = {"^IRX", "^TNX"}   # yields: % changes are not price returns -> excluded from (a)
    lse_pos = pd.Series(np.arange(len(lcal)), index=lcal)
    panels = [(t, clo, adj, vol, cal_pos) for t in clo.columns] + [(t, uclo, uadj, uvol, lse_pos) for t in uclo.columns]
    for t, P_c, P_a, P_v, P_pos in panels:
        if t in RATE_SERIES:
            continue
        s = P_c[t].dropna()
        if len(s) < 3:
            continue
        a = P_a[t].reindex(s.index)
        v = P_v[t].reindex(s.index)
        r_c = s / s.shift(1) - 1
        r_a = a / a.shift(1) - 1
        hit = r_c.index[(r_c.abs() > 0.5) | (r_a.abs() > 0.5)]
        if len(hit) == 0:
            continue
        p = P_pos.reindex(s.index).values
        idx = {d: i for i, d in enumerate(s.index)}
        sg = splits_by_t.get(t)
        for d in hit:
            i = idx[d]
            ratio = s.iloc[i] / s.iloc[i - 1]
            gap = int(p[i] - p[i - 1] - 1)
            near = None; explained = False
            if sg is not None:
                w = sg[(sg["date"] >= s.index[max(0, i - 5)]) & (sg["date"] <= s.index[min(len(s) - 1, i + 5)])]
                for _, sr in w.iterrows():
                    sr_ = float(sr["split_ratio"])
                    near = f"{sr['date'].date()}:{sr_:g}"
                    for target in (1.0 / sr_, sr_):
                        if abs(np.log(ratio) - np.log(target)) < np.log(1.25):
                            explained = True
            # reversal: cumulative move over next 1..5 obs brings price back within 25% of pre-jump level
            rev = False
            for k in range(1, 6):
                if i + k < len(s):
                    if abs(np.log(s.iloc[i + k] / s.iloc[i - 1])) < np.log(1.25):
                        rev = True; break
            unit100 = abs(abs(np.log(ratio)) - np.log(100)) < np.log(1.25)
            ra_i = r_a.iloc[i]
            dv_i = float(divmap_all.get((t, d), 0.0))
            if explained:
                cat = "split_related"
            elif unit100 and not rev:
                cat = "unit_100x_break"
            elif pd.notna(ra_i) and abs(ra_i) <= 0.5 and dv_i > 0.2 * s.iloc[i - 1]:
                cat = "distribution_close_only"   # spin-off/special dividend booked as dividend: Adj Close is fine
            elif gap > 5:
                cat = "spans_data_gap"
            elif rev:
                cat = "spike_reversal"
            else:
                cat = "persistent_move"
            bad.append(dict(ticker=t, date=d.date(), prev_date=s.index[i - 1].date(), prev_close=s.iloc[i - 1],
                            close=s.iloc[i], ret_close=r_c.iloc[i], ret_adj=r_a.iloc[i], gap_trading_days=gap,
                            volume=v.iloc[i], split_near=near, explained_by_split=explained,
                            reverses_within_5d=rev, category=cat,
                            during_membership=in_spells(sd, t, pd.Timestamp(d))))
    badf = pd.DataFrame(bad)
    if len(badf):
        badf = badf.merge(u[["ticker", "in_current", "asset_class"]], on="ticker", how="left")
        rs = set(cov.loc[cov["reuse_suspect"], "ticker"])
        badf["ticker_reuse_suspect"] = badf["ticker"].isin(rs)
    badf.to_csv(os.path.join(DATA, "d2_bad_ticks.csv"), index=False)

    # ---------------- QC (b): stale runs ----------------
    stale = []
    for t in clo.columns:
        s = clo[t].dropna()
        if len(s) < 10:
            continue
        x = s.round(6).values
        brk = np.r_[True, x[1:] != x[:-1]]
        grp = np.cumsum(brk)
        runs = pd.Series(grp).value_counts()
        long_runs = runs[runs >= 10]
        if long_runs.empty:
            continue
        vv = vol[t].reindex(s.index).values
        for g, n in long_runs.items():
            ii = np.where(grp == g)[0]
            st, en = s.index[ii[0]], s.index[ii[-1]]
            pos_ = "tail" if en == s.index[-1] else ("head" if st == s.index[0] else "middle")
            stale.append(dict(ticker=t, start=st.date(), end=en.date(), n_days=int(n), close=float(x[ii[0]]),
                              zero_volume_frac=float(np.mean(np.nan_to_num(vv[ii], nan=0) == 0)), position=pos_,
                              during_membership=in_spells(sd, t, st, en)))
    stf = pd.DataFrame(stale)
    if len(stf):
        stf = stf.merge(u[["ticker", "in_current", "asset_class"]], on="ticker", how="left")
    stf.to_csv(os.path.join(DATA, "d2_stale_runs.csv"), index=False)

    # ---------------- QC (c)/(d)/(e) ----------------
    cur = cov[(cov["in_current"]) & (cov["asset_class"] == "equity")]
    not_last = cur[cur["last_date"].astype(str) != CUTOFF][["ticker", "last_date", "status"]]
    ohlc = raw[["Open", "High", "Low", "Close", "Adj Close"]]
    nonpos = raw[(ohlc <= 0).any(axis=1)]
    qc["check_c_current_last_date"] = {"n_current": int(len(cur)), "n_last_is_cutoff": int((cur["last_date"].astype(str) == CUTOFF).sum()),
                                       "exceptions": not_last.astype(str).to_dict("records")}
    qc["check_d_nonpositive_prices"] = {"n_rows": int(len(nonpos)),
                                        "by_ticker": nonpos["ticker"].value_counts().head(30).to_dict(),
                                        "n_zero_close": int((raw["Close"] == 0).sum()),
                                        "n_negative_any": int((ohlc < 0).any(axis=1).sum())}
    # OHLC internal consistency
    hl = raw[(raw["High"] < raw["Low"]) | (raw["Close"] > raw["High"] * 1.0001) | (raw["Close"] < raw["Low"] * 0.9999)]
    qc["ohlc_inconsistent_rows"] = {"n": int(len(hl)), "by_ticker_top": hl["ticker"].value_counts().head(15).to_dict()}
    # (e) adjustment-factor checks: f = Adj/Close must be <= 1 and non-decreasing in time; jumps must match dividends
    fac_viol, fac_gt1, divmis = [], [], []
    divmap = {t: g.set_index("date")["dividend"] for t, g in div.groupby("ticker")}
    for t in clo.columns:
        c = clo[t].dropna()
        if len(c) < 3:
            continue
        f = (adj[t].reindex(c.index) / c)
        if (f > 1 + 1e-4).any():
            fac_gt1.append(t)
        dec = f.values[1:] < f.values[:-1] * (1 - 1e-4)
        if dec.any():
            fac_viol.append((t, int(dec.sum())))
        # implied dividend at each factor jump: D = C_{t-1} * (1 - f_{t-1}/f_t)
        jumps = np.where(f.values[1:] > f.values[:-1] * (1 + 2e-4))[0] + 1
        dv = divmap.get(t)
        for j in jumps:
            d = c.index[j]
            implied = c.iloc[j - 1] * (1 - f.iloc[j - 1] / f.iloc[j])
            actual = float(dv.get(d, 0.0)) if dv is not None else 0.0
            if actual == 0 or abs(implied / actual - 1) > 0.05:
                divmis.append(dict(ticker=t, date=d.date(), implied_div=implied, yahoo_div=actual))
    dmf = pd.DataFrame(divmis)
    dmf.to_csv(os.path.join(CACHE, "adjfactor_dividend_mismatch.csv"), index=False)
    n_div_events = int(sum(((div["ticker"] == t).sum()) for t in clo.columns[:0]))
    qc["check_e_adj_factor"] = {"tickers_factor_gt_1": fac_gt1[:50], "n_tickers_factor_gt_1": len(fac_gt1),
                                "n_tickers_factor_decreasing": len(fac_viol),
                                "factor_decreasing_examples": fac_viol[:30],
                                "n_factor_jumps_not_matching_yahoo_dividend_5pct": int(len(dmf)),
                                "n_tickers_with_mismatch": int(dmf["ticker"].nunique()) if len(dmf) else 0,
                                "n_dividend_events_total": int(len(div))}

    # bad tick / stale counts into coverage
    if len(badf):
        cov = cov.merge(badf.groupby("ticker").size().rename("n_bad_ticks"), left_on="ticker", right_index=True, how="left")
    else:
        cov["n_bad_ticks"] = 0
    if len(stf):
        cov = cov.merge(stf.groupby("ticker")["n_days"].max().rename("max_stale_run"), left_on="ticker", right_index=True, how="left")
    else:
        cov["max_stale_run"] = np.nan
    cov["n_bad_ticks"] = cov["n_bad_ticks"].fillna(0).astype(int)
    cov.to_csv(os.path.join(DATA, "d2_coverage.csv"), index=False)

    # ---------------- survivorship statistics ----------------
    eq = cov[cov["asset_class"] == "equity"]
    hist = eq[~eq["in_current"]]
    qc["coverage"] = {
        "n_universe": int(len(cov)), "n_equity": int(len(eq)),
        "equity_status": eq["status"].value_counts().to_dict(),
        "current_status": eq[eq["in_current"]]["status"].value_counts().to_dict(),
        "historical_nonconstituent_equities": int(len(hist)),
        "historical_no_data": int((hist["status"] == "no_data").sum()),
        "historical_no_data_fja_since2000": int(((hist["status"] == "no_data") & hist["in_fja_since2000"]).sum()),
        "historical_fja_since2000_total": int(hist["in_fja_since2000"].sum()),
        "benchmarks_status": cov[cov["asset_class"] != "equity"][["ticker", "status", "first_date"]].astype(str).to_dict("records"),
        "reuse_suspect_n": int(cov["reuse_suspect"].sum()),
        "flag_counts": pd.Series([f for fl in cov["flags"].fillna("") for f in fl.split(";") if f]).str.replace(r":.*", "", regex=True).value_counts().to_dict(),
    }
    # member-day coverage by era (all tickers; and excluding reuse suspects)
    eras = [("2000-2004", "2000-01-01", "2004-12-31"), ("2005-2009", "2005-01-01", "2009-12-31"),
            ("2010-2014", "2010-01-01", "2014-12-31"), ("2015-2019", "2015-01-01", "2019-12-31"),
            ("2020-2026", "2020-01-01", CUTOFF)]
    reuse = set(cov.loc[cov["reuse_suspect"], "ticker"])
    era_stats = []
    # membership x day matrix, three coverage definitions:
    #   strict  : Yahoo has a price under the same ticker
    #   valid   : strict, excluding reuse-suspect tickers (data belongs to another company)
    #   best    : valid, plus accepted rename successors' data for days the old ticker lacks
    mdays_idx = cal[cal >= "2000-01-01"]
    mem = pd.DataFrame(0, index=mdays_idx, columns=["members", "with_price", "with_price_valid", "with_price_best"])
    miss_by_t = {}
    for _, sp_ in spells.iterrows():
        t = sp_["ticker"]
        e0 = sp_["end_excl"] if pd.notna(sp_["end_excl"]) else CUT + pd.Timedelta(days=1)
        dd = mdays_idx[(mdays_idx >= sp_["start"]) & (mdays_idx < e0)]
        if len(dd) == 0:
            continue
        mem.loc[dd, "members"] += 1
        own = clo[t].reindex(dd).notna() if t in clo.columns else pd.Series(False, index=dd)
        valid = own & (t not in reuse)
        succ = remap.get(t)
        if succ and succ in clo.columns:
            best = valid | clo[succ].reindex(dd).notna()
        else:
            best = valid
        mem.loc[dd, "with_price"] += own.values.astype(int)
        mem.loc[dd, "with_price_valid"] += valid.values.astype(int)
        mem.loc[dd, "with_price_best"] += best.values.astype(int)
        missing = dd[~best.values]
        if len(missing):
            miss_by_t.setdefault(t, []).append(missing)
    for label, a, b in eras:
        sub = mem.loc[a:b]
        tot = int(sub["members"].sum())
        top = []
        for t, lst in miss_by_t.items():
            n = sum(int(((x >= a) & (x <= b)).sum()) for x in lst)
            if n:
                top.append((t, n))
        top.sort(key=lambda kv: -kv[1])
        era_stats.append(dict(era=label, member_days=tot,
                              coverage_strict=float(sub["with_price"].sum() / tot),
                              coverage_valid_excl_reuse=float(sub["with_price_valid"].sum() / tot),
                              coverage_best_incl_renames=float(sub["with_price_best"].sum() / tot),
                              n_tickers_with_missing_days_best=len(top),
                              top_missing_best=top[:40]))
    qc["member_day_coverage_by_era"] = era_stats
    yearly = mem.groupby(mem.index.year).mean().round(1)
    qc["members_with_price_by_year"] = yearly.reset_index().rename(columns={"index": "year"}).to_dict("records")
    mem.to_csv(os.path.join(DATA, "d2_members_with_price_daily.csv"))
    write_meta(os.path.join(DATA, "d2_members_with_price_daily.csv"), {"source": "derived (D2 spells x Yahoo Close)",
        "rows": int(len(mem)), "definitions": {"members": "index members per D2 spells (fja05680 + Wikipedia)",
        "with_price": "members with a Yahoo Close under the same ticker",
        "with_price_valid": "... excluding reuse-suspect tickers",
        "with_price_best": "... plus accepted heuristic rename successors (d2_rename_candidates.csv)"}})

    # counts
    if len(badf):
        bm = badf[badf["during_membership"]]
        bmv = bm[~bm["ticker_reuse_suspect"]]
        qc["bad_ticks"] = {"n": int(len(badf)), "note": "rate series ^IRX/^TNX excluded (yields, not prices)",
                           "by_category": badf["category"].value_counts().to_dict(),
                           "n_tickers": int(badf["ticker"].nunique()),
                           "not_explained_by_split": int((~badf["explained_by_split"]).sum()),
                           "n_in_reuse_suspect_tickers": int(badf["ticker_reuse_suspect"].sum()),
                           "during_membership_n": int(len(bm)),
                           "during_membership_valid_ticker_n": int(len(bmv)),
                           "during_membership_valid_by_category": bmv["category"].value_counts().to_dict(),
                           "during_membership_valid_tickers": int(bmv["ticker"].nunique()),
                           "current_constituents_n": int(badf["in_current"].fillna(False).sum()),
                           "current_constituents_by_category": badf[badf["in_current"] == True]["category"].value_counts().to_dict()}
    else:
        qc["bad_ticks"] = {"n": 0}
    if len(stf):
        cur_stale = stf[(stf["in_current"] == True)]
        qc["stale_runs"] = {"n_runs": int(len(stf)), "n_tickers": int(stf["ticker"].nunique()),
                            "by_position": stf["position"].value_counts().to_dict(),
                            "during_membership_n": int(stf["during_membership"].sum()),
                            "during_membership_tickers": sorted(stf.loc[stf["during_membership"], "ticker"].unique().tolist()),
                            "current_constituents_runs": int(len(cur_stale)),
                            "current_constituents_runs_during_membership": int(cur_stale["during_membership"].sum()),
                            "current_constituents_runs_during_membership_detail": cur_stale[cur_stale["during_membership"]].astype(str).to_dict("records"),
                            "current_constituents_runs_since_2010": int((pd.to_datetime(cur_stale["start"]) >= "2010-01-01").sum()),
                            "current_examples": cur_stale.sort_values("n_days", ascending=False).head(10).astype(str).to_dict("records")}
    else:
        qc["stale_runs"] = {"n_runs": 0}
    qc["panel_shapes"] = {"adjclose": list(adj.shape), "close": list(clo.shape), "volume": list(vol.shape),
                          "ret_monthly": list(ret_m.shape), "ucits_adjclose": list(uadj.shape),
                          "dividends_rows": int(len(divs)), "splits_rows": int(len(spl)),
                          "final_partial_month_rows": int(len(fpd))}
    json.dump(qc, open(os.path.join(OUT, "d2_qc_summary.json"), "w"), indent=1, default=str)

    # ---------------- sidecars ----------------
    src = {"yahoo": "Yahoo Finance chart API via yfinance 1.7 yf.download(start=1995-01-01, end=2026-09-26, "
                    "auto_adjust=False, actions=True, group_by='ticker', threads=6)",
           "universe": os.path.join(DATA, "d2_universe.csv")}
    common_cav = ["Survivorship: tickers Yahoo no longer serves (most acquired/bankrupt names) are absent; see "
                  "d2_coverage.csv status=no_data and d2_report.md.",
                  "Ticker reuse: some historical symbols now map to a different company on Yahoo "
                  "(d2_coverage.csv reuse_suspect/flags). Join to membership by (ticker, date) with care.",
                  "Yahoo data is not point-in-time: Close is split-adjusted as of the retrieval date; Adj Close is "
                  "split+dividend adjusted (CRSP-style multiplicative) as of the retrieval date."]
    rt = utcnow()
    write_meta(os.path.join(DATA, "d2_adjclose.parquet"), {"source": src, "retrieved_utc_approx": rt,
        "shape": list(adj.shape), "index": "NYSE trading days (^GSPC calendar) 1995-01-03..2026-09-25",
        "columns": "Yahoo tickers (US-listed equities, ETFs, indices; UCITS .L listings are in d2_ucits_*.parquet)",
        "values": "Yahoo 'Adj Close' (split + dividend adjusted, total-return proxy). NaN = no Yahoo bar. "
                  "Corrected ONLY for Yahoo spin-off double counts (split + same-day dividend), listed in "
                  "d2_adj_corrections.csv (classification=double_count_corrected): history before the event is rescaled "
                  "by prior_history_scale. Unmodified Yahoo values: d2_adjclose_yahoo_raw.parquet.",
        "corrections": qc["adj_split_dividend_events"]["corrected"],
        "caveats": common_cav})
    write_meta(os.path.join(DATA, "d2_adjclose_yahoo_raw.parquet"), {"source": src, "shape": list(adj_raw.shape),
        "values": "Unmodified Yahoo 'Adj Close' (before D2 double-count corrections)."})
    write_meta(os.path.join(DATA, "d2_adj_corrections.csv"), {"source": "derived from Yahoo splits/dividends", "rows": int(len(sdev)),
        "definition": "All same-day split + dividend events. double_count_corrected: dividend >=5% of prior close, |Close "
                      "return|<10%, Adj return - Close return > 5pp -> spin-off counted twice by Yahoo; corrected in "
                      "d2_adjclose/d2_ret_monthly. ambiguous_flagged: large distribution with an unreliable split encoding; "
                      "NOT corrected (see CNBC evidence in d2_bad_ticks_crosscheck.csv/d2_report.md)."})
    write_meta(os.path.join(DATA, "d2_close.parquet"), {"source": src, "shape": list(clo.shape),
        "values": "Yahoo 'Close' (split-adjusted, NOT dividend-adjusted).", "caveats": common_cav})
    write_meta(os.path.join(DATA, "d2_volume.parquet"), {"source": src, "shape": list(vol.shape),
        "values": "Yahoo daily share volume (split-adjusted by Yahoo).", "caveats": common_cav})
    for nm, df in (("adjclose", uadj), ("close", uclo), ("volume", uvol)):
        write_meta(os.path.join(DATA, f"d2_ucits_{nm}.parquet"), {"source": src, "shape": list(df.shape),
            "index": "LSE trading days (dates where any .L listing has a bar)",
            "currency": {t: meta.get(t, {}).get("currency") for t in df.columns},
            "caveats": ["London close timing (16:30 UK) differs from NY close; do not mix daily returns with US panel."]})
    write_meta(os.path.join(DATA, "d2_dividends.parquet"), {"source": src, "rows": int(len(divs)),
        "columns": ["date (ex-date)", "ticker", "dividend (per share, split-adjusted by Yahoo)", "capital_gain (fund distributions)",
                    "on_trading_day"], "caveats": ["Yahoo dividend records; special dividends included; spin-offs NOT represented."]})
    write_meta(os.path.join(DATA, "d2_splits.parquet"), {"source": src, "rows": int(len(spl)),
        "columns": ["date", "ticker", "split_ratio (new shares per old share; <1 = reverse split)"]})
    write_meta(os.path.join(DATA, "d2_ret_monthly.parquet"), {"source": "derived from d2_adjclose.parquet",
        "shape": list(ret_m.shape), "definition": "Adj Close(last NYSE trading day of month m) / Adj Close(last trading day of m-1) - 1; "
        "NaN if either end has no price (no filling). UCITS columns use their own last LSE trading day of each month. "
        "Last row = 2026-08-31 (September 2026 incomplete at the 2026-09-25 cutoff).",
        "caveats": common_cav + ["Delisting-month returns are NaN when a series ends mid-month; see d2_final_partial_month.csv.",
                                 f"{qc['monthly']['midlife_missing_month_end_prices']} (ticker, month) cells are NaN because the stock has "
                                 "prices in the month but none on the exact month-end day."]})
    write_meta(os.path.join(DATA, "d2_final_partial_month.csv"), {"source": "derived", "rows": int(len(fpd)),
        "definition": "For series ending before the cutoff and not on a month-end: Adj Close(last date)/Adj Close(prior month-end)-1. "
                      "NOT a CRSP delisting return (no cash/merger consideration after the last Yahoo bar)."})
    write_meta(os.path.join(DATA, "d2_coverage.csv"), {"source": "derived", "rows": int(len(cov)),
        "definitions": {"n_obs": "days with non-NaN Close on the ticker's calendar", "n_gaps_gt5": "gaps between consecutive "
                        "observations with >5 missing trading days", "status": "active=last bar on 2026-09-25; "
                        "ended_before_2026-09-25; no_data=Yahoo returned nothing for the symbol",
                        "member_*": "overlap with D2-derived membership spells since 2000 (d2_universe_spells.csv)",
                        "reuse_suspect": "Yahoo series starts after membership ended, or Yahoo name does not match any "
                                         "Wikipedia name for a non-current ticker",
                        "name_check": "fuzzy token match of Yahoo longName vs Wikipedia names (current list + changes table)"}})
    write_meta(os.path.join(DATA, "d2_bad_ticks.csv"), {"source": "derived", "rows": int(len(badf)),
        "definition": "|daily return| > 50% on Close or Adj Close (consecutive observations). Flagged, NOT removed. "
                      "category: split_related (jump matches a split ratio within +-5 obs), spans_data_gap (>5 missing "
                      "trading days before the move), spike_reversal (price returns within 25% of pre-jump level within 5 obs), "
                      "persistent_move (otherwise; often genuine: bankruptcy, takeover, biotech readout)."})
    write_meta(os.path.join(DATA, "d2_stale_runs.csv"), {"source": "derived", "rows": int(len(stf)),
        "definition": "runs of >=10 consecutive observations with identical Close (6 dp)."})
    write_meta(os.path.join(DATA, "d2_offcalendar_bars.csv"), {"source": "derived", "rows": int(len(off_tab)),
        "definition": "Yahoo bars for US tickers dated on non-NYSE-trading days (excluded from wide panels; dividends kept)."})
    print(json.dumps({k: qc[k] for k in ("us_calendar", "coverage", "bad_ticks", "stale_runs", "check_c_current_last_date",
                                         "check_d_nonpositive_prices", "panel_shapes")}, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
