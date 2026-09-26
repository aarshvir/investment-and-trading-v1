"""d2_validate.py - independent second-source validation + benchmark integrity for D2 price panels.

Second source: Stooq (requested) is behind a JavaScript proof-of-work 'verify your browser' challenge for
non-browser clients (checked 2026-09-25 ~20:17 UTC); D2 does not circumvent bot detection. Fallback: CNBC public
market-data endpoints (no key, no login):
  bars : https://ts-api.cnbc.com/harmony/app/bars/<SYM>/1D/<start>/<end>/adjusted/EST5EDT.json
         ('adjusted' = split-adjusted, not dividend-adjusted -> comparable to Yahoo 'Close')
  quote: https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=A|B|...
Also FRED (SP500, DGS10, DTB3) and CBOE (VIX_History.csv) for benchmark series.

Parts (python d2_validate.py <part>):
  sample    60-ticker x 25-date comparison (40 current, 20 historical still trading) + full-series diagnostics
  latest    2026-09-25 close for all current constituents (+US benchmarks) vs CNBC quote 'last'
  bench     SPY/IVV/VOO vs ^SP500TR, RSP vs ^GSPC, UCITS vs ^SP500TR, ^GSPC/^SP500TR vs CNBC, ^GSPC vs FRED,
            ^VIX vs CBOE, ^TNX/^IRX vs FRED
  badticks  cross-check flagged >50% moves of still-trading tickers against CNBC bars
  all
"""
import os
import io
import sys
import json
import time
import random
import requests
import numpy as np
import pandas as pd

from d2_common import (DATA, OUT, VAL_DIR, URLS, UA, CUTOFF, utcnow, write_meta, polite_get)

CUT = pd.Timestamp(CUTOFF)
S = requests.Session()
HDR = dict(UA, Accept="application/json, text/plain, */*")
RES_PATH = os.path.join(OUT, "d2_validation_results.json")


def load_res():
    return json.load(open(RES_PATH)) if os.path.exists(RES_PATH) else {}


def save_res(res):
    json.dump(res, open(RES_PATH, "w"), indent=1, default=str)


def cnbc_sym(t):
    m = {"^GSPC": ".SPX", "^SP500TR": ".SPXTR", "^VIX": ".VIX"}
    if t in m:
        return m[t]
    return t.replace("-", ".")


def cnbc_bars(t, start="19950101", end="20260926"):
    sym = cnbc_sym(t)
    path = os.path.join(VAL_DIR, f"cnbc_{sym.replace('.', '_')}_{start}_{end}.json")
    if os.path.exists(path):
        j = json.load(open(path))
    else:
        url = URLS["cnbc_bars"].format(sym=sym, start=start, end=end)
        j = None
        for attempt in range(4):
            try:
                r = polite_get(S, url, headers=HDR, timeout=40)
                if r.status_code == 200:
                    j = r.json(); break
                time.sleep(3 * (2 ** attempt))
            except Exception:
                time.sleep(3 * (2 ** attempt))
        if j is None:
            return pd.Series(dtype=float)
        json.dump(j, open(path, "w"))
    bars = (j or {}).get("barData", {}).get("priceBars", []) or []
    if not bars:
        return pd.Series(dtype=float)
    df = pd.DataFrame(bars)
    idx = pd.to_datetime(df["tradeTime"].str[:8], format="%Y%m%d")
    return pd.Series(pd.to_numeric(df["close"], errors="coerce").values, index=idx).dropna().sort_index()


def cnbc_quotes(tickers):
    out = {}
    for i in range(0, len(tickers), 40):
        chunk = tickers[i:i + 40]
        syms = "%7C".join(cnbc_sym(t) for t in chunk)
        url = URLS["cnbc_quote"].format(syms=syms)
        for attempt in range(4):
            try:
                r = polite_get(S, url, headers=HDR, timeout=40)
                j = r.json()
                break
            except Exception:
                time.sleep(3 * (2 ** attempt)); j = None
        qs = (j or {}).get("FormattedQuoteResult", {}).get("FormattedQuote", []) or []
        back = {cnbc_sym(t): t for t in chunk}
        for q in qs:
            t = back.get(q.get("symbol"))
            if t:
                out[t] = q
    return out


def num(x):
    if x is None:
        return np.nan
    try:
        return float(str(x).replace(",", "").replace("%", ""))
    except Exception:
        return np.nan


# ------------------------------------------------------------------------------------------------------------
def stooq_probe():
    info = {}
    for sym in ["aapl.us", "brk-b.us", "msft.us"]:
        try:
            r = polite_get(S, URLS["stooq"].format(sym=sym), timeout=30)
            body = r.text[:400]
            info[sym] = {"status": r.status_code, "content_type": r.headers.get("Content-Type"),
                         "js_challenge": ("verify your browser" in r.text.lower()) or ("__verify" in r.text),
                         "is_csv": body.lower().startswith("date,"), "snippet": body[:160]}
        except Exception as e:
            info[sym] = {"error": repr(e)}
    return {"probed_utc": utcnow(), "results": info,
            "decision": "Stooq CSV endpoint returns an HTML JavaScript proof-of-work browser-verification page instead "
                        "of CSV; solving it would mean circumventing bot detection, so Stooq was not used. "
                        "Fallback second source: CNBC public quote/bars endpoints (split-adjusted closes)."}


def part_sample(res):
    cov = pd.read_csv(os.path.join(DATA, "d2_coverage.csv"))
    clo = pd.read_parquet(os.path.join(DATA, "d2_close.parquet"))
    rng = random.Random(20260926)
    eq = cov[cov["asset_class"] == "equity"]
    cur_pool = sorted(eq[(eq["in_current"]) & (eq["status"] == "active")]["ticker"])
    hist_pool = sorted(eq[(~eq["in_current"]) & (eq["in_fja_since2000"]) & (eq["status"] == "active") &
                          (~eq["reuse_suspect"]) & (pd.to_datetime(eq["first_date"]) <= "2016-01-01")]["ticker"])
    cur_s = rng.sample(cur_pool, len(cur_pool))
    hist_s = rng.sample(hist_pool, len(hist_pool))
    rows, full_rows, used, skipped = [], [], {"current": [], "historical": []}, []

    def take(pool, n, group):
        for t in pool:
            if len(used[group]) >= n:
                break
            c = cnbc_bars(t)
            y = clo[t].dropna() if t in clo.columns else pd.Series(dtype=float)
            common = y.index.intersection(c.index)
            common10 = common[common >= "2010-01-01"]
            if len(common10) < 250:
                skipped.append({"ticker": t, "group": group, "reason": f"cnbc_common_days_since2010={len(common10)}"})
                continue
            used[group].append(t)
            dates = sorted(rng.sample(list(common10), 25))
            yc, cc = y.reindex(common), c.reindex(common)
            ratio = yc / cc
            ry, rcn = yc / yc.shift(1) - 1, cc / cc.shift(1) - 1
            for d in dates:
                j = common.get_loc(d)
                win = ratio.iloc[max(0, j - 10): j + 11]
                rows.append(dict(group=group, ticker=t, date=d.date(), yahoo_close=y[d], cnbc_close=c[d],
                                 rel_diff=y[d] / c[d] - 1,
                                 local_ratio_std=float(win.std()), local_ratio_median=float(win.median()),
                                 yahoo_ret=ry.iloc[j], cnbc_ret=rcn.iloc[j], ret_absdiff=abs(ry.iloc[j] - rcn.iloc[j])))
            rel = (y.reindex(common) / c.reindex(common) - 1)
            r10 = rel[rel.index >= "2010-01-01"]
            full_rows.append(dict(group=group, ticker=t, n_common_all=len(common), n_common_since2010=len(r10),
                                  pct_within_0p5_since2010=float((r10.abs() <= 0.005).mean()),
                                  pct_within_0p5_all=float((rel.abs() <= 0.005).mean()),
                                  median_abs_diff_since2010=float(r10.abs().median()),
                                  max_abs_diff_since2010=float(r10.abs().max()),
                                  first_common=common[0].date(), yahoo_first=y.index[0].date(), cnbc_first=c.index[0].date()))

    take(cur_s, 40, "current")
    take(hist_s, 20, "historical")
    df = pd.DataFrame(rows)
    df["within_0p5pct"] = df["rel_diff"].abs() <= 0.005
    df["ret_within_0p5pp"] = df["ret_absdiff"] <= 0.005
    # classify level misses: constant multiplicative offset over +-10 days => adjustment-convention difference
    df["miss_class"] = np.where(df["within_0p5pct"], "",
                                np.where((df["local_ratio_std"] < 0.001) & ((df["local_ratio_median"] - 1).abs() > 0.005),
                                         "constant_adjustment_offset", "local_price_disagreement"))
    df.to_csv(os.path.join(DATA, "d2_validation_sample.csv"), index=False)
    full = pd.DataFrame(full_rows)
    full.to_csv(os.path.join(DATA, "d2_validation_sample_fullseries.csv"), index=False)

    # persistent Yahoo/CNBC ratio steps over the full common history of every sampled ticker: each step is a
    # corporate action adjusted differently by the two sources; classify against Yahoo's own split/dividend records
    spl = pd.read_parquet(os.path.join(DATA, "d2_splits.parquet"))
    dvd = pd.read_parquet(os.path.join(DATA, "d2_dividends.parquet"))
    steps = []
    for t in used["current"] + used["historical"]:
        c = cnbc_bars(t); y = clo[t].dropna()
        common = y.index.intersection(c.index)
        lr = np.log((y.reindex(common) / c.reindex(common)).values)
        n = len(lr)
        last = -99
        for i in range(20, n - 20):
            pre, post = lr[i - 20:i], lr[i:i + 20]
            dlt = np.median(post) - np.median(pre)
            if abs(dlt) > 0.005 and np.std(pre) < 0.002 and np.std(post) < 0.002 and i - last > 5:
                d = common[i]
                w0, w1 = common[max(0, i - 3)], common[min(n - 1, i + 3)]
                sp_ = spl[(spl["ticker"] == t) & (spl["date"] >= w0) & (spl["date"] <= w1)]
                dv_ = dvd[(dvd["ticker"] == t) & (dvd["date"] >= w0) & (dvd["date"] <= w1)]
                yprev = y.reindex(common).iloc[i - 1]
                big_div = dv_[dv_["dividend"].fillna(0) > 0.005 * yprev]
                if len(sp_):
                    cls = "yahoo_recorded_split(or spin-off encoded as split)"
                elif len(big_div):
                    cls = "yahoo_recorded_large_dividend (Close drops, Adj Close adjusted)"
                else:
                    cls = "no_yahoo_action (possible corporate action missing in Yahoo, or CNBC-only adjustment)"
                steps.append(dict(ticker=t, date=d.date(), log_step=float(dlt), ratio_before=float(np.exp(np.median(pre))),
                                  ratio_after=float(np.exp(np.median(post))), classification=cls,
                                  yahoo_split=";".join(f"{a.date()}:{b:g}" for a, b in zip(sp_["date"], sp_["split_ratio"])),
                                  yahoo_div=";".join(f"{a.date()}:{b:g}" for a, b in zip(dv_["date"], dv_["dividend"]))))
                last = i
    stp = pd.DataFrame(steps)
    stp.to_csv(os.path.join(DATA, "d2_validation_ratio_steps.csv"), index=False)
    res.setdefault("sample", {})
    ratio_steps_summary = {"n_steps": int(len(stp)), "n_tickers_with_steps": int(stp["ticker"].nunique()) if len(stp) else 0,
                           "by_class": stp["classification"].value_counts().to_dict() if len(stp) else {},
                           "rows": stp.astype(str).to_dict("records")}

    # outlier diagnosis on the full series for any ticker with a failing sampled date
    diag = []
    for t in sorted(df.loc[~df["within_0p5pct"], "ticker"].unique()):
        c = cnbc_bars(t); y = clo[t].dropna()
        common = y.index.intersection(c.index)
        ratio = (y.reindex(common) / c.reindex(common))
        bad = ratio[(ratio - 1).abs() > 0.005]
        # contiguous regimes of the ratio (rounded to 3 dp)
        rr = ratio.round(3)
        chg = rr.index[1:][rr.values[1:] != rr.values[:-1]]
        big_shift = []
        lr = np.log(ratio)
        jumps = lr.diff().abs()
        for d in jumps[jumps > 0.004].index[:10]:
            big_shift.append(f"{d.date()}:{ratio.shift(1)[d]:.4f}->{ratio[d]:.4f}")
        sp_t = spl[spl["ticker"] == t]
        diag.append(dict(ticker=t, n_common=len(common), n_bad_days=len(bad), first_bad=bad.index.min().date() if len(bad) else None,
                         last_bad=bad.index.max().date() if len(bad) else None,
                         ratio_min=float(ratio.min()), ratio_max=float(ratio.max()),
                         ratio_at_first=float(ratio.iloc[0]), ratio_at_last=float(ratio.iloc[-1]),
                         ratio_shifts=";".join(big_shift),
                         yahoo_splits=";".join(f"{d.date()}:{r:g}" for d, r in zip(sp_t["date"], sp_t["split_ratio"]))))
    dg = pd.DataFrame(diag)
    dg.to_csv(os.path.join(DATA, "d2_validation_outliers.csv"), index=False)
    by_group = df.groupby("group")["within_0p5pct"].agg(["mean", "sum", "count"]).reset_index().to_dict("records")
    res["sample"] = {"run_utc": utcnow(), "n_tickers": int(df["ticker"].nunique()), "n_obs": int(len(df)),
                     "pct_within_0p5": float(df["within_0p5pct"].mean()),
                     "pct_within_0p1": float((df["rel_diff"].abs() <= 0.001).mean()),
                     "by_group": by_group, "tickers": used, "skipped_for_insufficient_cnbc_history": skipped,
                     "n_fail_obs": int((~df["within_0p5pct"]).sum()),
                     "miss_classes": df.loc[~df["within_0p5pct"], "miss_class"].value_counts().to_dict(),
                     "pct_within_0p5_or_constant_offset": float((df["within_0p5pct"] | (df["miss_class"] == "constant_adjustment_offset")).mean()),
                     "pct_daily_return_within_0p5pp": float(df["ret_within_0p5pp"].mean()),
                     "pct_daily_return_within_0p1pp": float((df["ret_absdiff"] <= 0.001).mean()),
                     "return_misses": df.loc[~df["ret_within_0p5pp"], ["ticker", "date", "yahoo_ret", "cnbc_ret"]].astype(str).to_dict("records"),
                     "fail_tickers": sorted(df.loc[~df["within_0p5pct"], "ticker"].unique().tolist()),
                     "fullseries_median_pct_within_0p5_since2010": float(full["pct_within_0p5_since2010"].median()),
                     "fullseries_mean_pct_within_0p5_since2010": float(full["pct_within_0p5_since2010"].mean()),
                     "fullseries_tickers_below_99pct": full.loc[full["pct_within_0p5_since2010"] < 0.99, ["ticker", "pct_within_0p5_since2010"]].to_dict("records"),
                     "seed": 20260926,
                     "ratio_steps_full_history": ratio_steps_summary}
    save_res(res)
    print(json.dumps({k: v for k, v in res["sample"].items() if k != "ratio_steps_full_history"}, indent=1, default=str)[:4000])
    print(json.dumps({k: v for k, v in ratio_steps_summary.items() if k != "rows"}, indent=1))
    if len(stp):
        print(stp.to_string()[:8000])
    if len(dg):
        print(dg.to_string()[:6000])


def part_latest(res):
    cov = pd.read_csv(os.path.join(DATA, "d2_coverage.csv"))
    clo = pd.read_parquet(os.path.join(DATA, "d2_close.parquet"))
    vol = pd.read_parquet(os.path.join(DATA, "d2_volume.parquet"))
    cur = sorted(cov[(cov["asset_class"] == "equity") & (cov["in_current"])]["ticker"])
    bench = [t for t in cov[cov["asset_class"] != "equity"]["ticker"] if not t.endswith(".L") and t not in ("^IRX", "^TNX", "^SP500TR")]
    q = cnbc_quotes(cur + bench)
    json.dump(q, open(os.path.join(VAL_DIR, f"cnbc_quotes_{utcnow().replace(':', '')}.json"), "w"))
    rows = []
    for t in cur + bench:
        qq = q.get(t, {})
        lt = qq.get("last_time")
        y = clo.at[CUT, t] if (t in clo.columns and CUT in clo.index) else np.nan
        yprev = clo[t].loc[:CUT - pd.Timedelta(days=1)].dropna().iloc[-1] if t in clo.columns and clo[t].loc[:CUT - pd.Timedelta(days=1)].notna().any() else np.nan
        c = num(qq.get("last")); cp = num(qq.get("previous_day_closing"))
        rows.append(dict(ticker=t, group="current" if t in cur else "benchmark", yahoo_close_0925=y,
                         cnbc_last=c, cnbc_last_time=lt, cnbc_last_is_0925=str(lt or "").startswith(CUTOFF),
                         rel_diff=(y / c - 1) if (pd.notna(y) and pd.notna(c) and c) else np.nan,
                         yahoo_close_0924=yprev, cnbc_prev_close=cp,
                         rel_diff_prev=(yprev / cp - 1) if (pd.notna(yprev) and pd.notna(cp) and cp) else np.nan,
                         yahoo_volume_0925=vol.at[CUT, t] if t in vol.columns else np.nan,
                         cnbc_volume=num(qq.get("volume")), cnbc_name=qq.get("name")))
    df = pd.DataFrame(rows)
    df["within_0p5"] = df["rel_diff"].abs() <= 0.005
    df["exact_cent"] = (df["yahoo_close_0925"].round(2) == df["cnbc_last"].round(2))
    df.to_csv(os.path.join(DATA, "d2_validation_latest_close.csv"), index=False)
    c = df[df["group"] == "current"]
    comp = c[c["rel_diff"].notna() & c["cnbc_last_is_0925"]]
    res["latest_close"] = {"run_utc": utcnow(), "n_current": int(len(c)), "n_compared": int(len(comp)),
                           "n_cnbc_missing_or_not_0925": int(len(c) - len(comp)),
                           "pct_within_0p5": float(comp["within_0p5"].mean()) if len(comp) else None,
                           "pct_within_0p1": float((comp["rel_diff"].abs() <= 0.001).mean()) if len(comp) else None,
                           "pct_exact_to_cent": float(comp["exact_cent"].mean()) if len(comp) else None,
                           "prev_close_pct_within_0p5": float((c["rel_diff_prev"].abs() <= 0.005).mean()),
                           "prev_close_pct_exact_cent": float((c["yahoo_close_0924"].round(2) == c["cnbc_prev_close"].round(2)).mean()),
                           "fails": comp.loc[~comp["within_0p5"], ["ticker", "yahoo_close_0925", "cnbc_last", "rel_diff"]].to_dict("records"),
                           "not_compared": c.loc[~(c["rel_diff"].notna() & c["cnbc_last_is_0925"]), ["ticker", "cnbc_last_time", "yahoo_close_0925"]].astype(str).to_dict("records"),
                           "benchmarks": df[df["group"] == "benchmark"][["ticker", "yahoo_close_0925", "cnbc_last", "rel_diff"]].to_dict("records")}
    save_res(res)
    print(json.dumps({k: v for k, v in res["latest_close"].items() if k not in ("benchmarks",)}, indent=1, default=str)[:3000])


def ann(x0, x1, days):
    return (x1 / x0) ** (365.25 / days) - 1


def pair_stats(a, b, start, end, label):
    """a, b: price series (total-return or price). Returns CAGR diff, TE."""
    s = pd.concat([a, b], axis=1, keys=["a", "b"]).loc[:end].dropna()
    base = s.loc[:pd.Timestamp(start) - pd.Timedelta(days=1)]
    if len(base):
        s = s.loc[base.index[-1]:]
    else:
        s = s.loc[start:]
    d0, d1 = s.index[0], s.index[-1]
    days = (d1 - d0).days
    ca, cb = ann(s["a"].iloc[0], s["a"].iloc[-1], days), ann(s["b"].iloc[0], s["b"].iloc[-1], days)
    rd = s.pct_change().dropna()
    diff = rd["a"] - rd["b"]
    m = s.resample("ME").last()
    rm = m.pct_change().dropna()
    y = s.resample("YE").last()
    yr = y.pct_change().dropna()
    return {"label": label, "base_date": str(d0.date()), "end_date": str(d1.date()), "years": round(days / 365.25, 3),
            "cagr_a": ca, "cagr_b": cb, "annualized_difference": ca - cb,
            "cum_a": float(s["a"].iloc[-1] / s["a"].iloc[0] - 1), "cum_b": float(s["b"].iloc[-1] / s["b"].iloc[0] - 1),
            "te_daily_ann": float(diff.std() * np.sqrt(252)), "te_monthly_ann": float((rm["a"] - rm["b"]).std() * np.sqrt(12)),
            "corr_daily": float(rd["a"].corr(rd["b"])),
            "yearly_diff_mean": float((yr["a"] - yr["b"]).mean()) if len(yr) else None,
            "yearly_diff_by_year": {str(k.year): round(float(v), 5) for k, v in (yr["a"] - yr["b"]).items()}}


def part_bench(res):
    adj = pd.read_parquet(os.path.join(DATA, "d2_adjclose.parquet"))
    clo = pd.read_parquet(os.path.join(DATA, "d2_close.parquet"))
    uadj = pd.read_parquet(os.path.join(DATA, "d2_ucits_adjclose.parquet"))
    out = {"run_utc": utcnow()}
    tr = adj["^SP500TR"]
    out["SPY_vs_SP500TR"] = pair_stats(adj["SPY"], tr, "2010-01-01", CUT, "SPY AdjClose vs ^SP500TR")
    out["IVV_vs_SP500TR"] = pair_stats(adj["IVV"], tr, "2010-01-01", CUT, "IVV AdjClose vs ^SP500TR")
    voo_start = adj["VOO"].first_valid_index()
    out["VOO_vs_SP500TR"] = pair_stats(adj["VOO"], tr, str((voo_start + pd.Timedelta(days=1)).date()), CUT, "VOO AdjClose vs ^SP500TR (since inception)")
    out["RSP_vs_GSPC"] = pair_stats(adj["RSP"], clo["^GSPC"], "2010-01-01", CUT, "RSP AdjClose (EW, TR) vs ^GSPC (CW, price)")
    out["RSP_vs_SP500TR"] = pair_stats(adj["RSP"], tr, "2010-01-01", CUT, "RSP AdjClose (EW, TR) vs ^SP500TR (CW, TR)")
    out["SP500TR_vs_GSPC"] = pair_stats(tr, clo["^GSPC"], "2010-01-01", CUT, "^SP500TR vs ^GSPC (dividend contribution)")
    # SPY price (Close) vs ^GSPC to isolate dividend handling
    out["SPYclose_vs_GSPC"] = pair_stats(clo["SPY"], clo["^GSPC"], "2010-01-01", CUT, "SPY Close (price) vs ^GSPC (price)")
    # UCITS vs ^SP500TR, month-end basis (London close vs NY close timing noise)
    uc = {}
    mpath = os.path.join(os.path.dirname(VAL_DIR), "meta", "yahoo_meta.json")
    ymeta = json.load(open(mpath)) if os.path.exists(mpath) else {}
    for t in uadj.columns:
        s = uadj[t].dropna()
        cur = (ymeta.get(t) or {}).get("currency")
        note = []
        rr = s / s.shift(1)
        brk = rr[(rr > 50) | (rr < 1 / 50)].index
        if len(brk):
            note.append(f"100x unit break(s) at {[str(b.date()) for b in brk]}; stats use data after the last break")
            s = s[s.index >= brk[-1]]
        if cur != "USD":
            uc[t] = {"currency": cur, "name": (ymeta.get(t) or {}).get("longName"),
                     "note": "quoted in %s, not USD: not compared with USD ^SP500TR (no FX conversion)" % cur}
            continue
        if len(s) < 300:
            uc[t] = {"note": "insufficient history", "n": int(len(s))}
            continue
        me_u = s.resample("ME").last()
        me_t = tr.dropna().resample("ME").last()
        j = pd.concat([me_u, me_t], axis=1, keys=["a", "b"]).dropna()
        j = j.iloc[1:]  # start at first full month-end
        j = j.loc[:"2026-08-31"]
        days = (j.index[-1] - j.index[0]).days
        uc[t] = {"currency": cur, "name": (ymeta.get(t) or {}).get("longName"), "note": "; ".join(note),
                 "window": f"{j.index[0].date()}..{j.index[-1].date()} (month-ends)", "cagr_ucits": ann(j['a'].iloc[0], j['a'].iloc[-1], days),
                 "cagr_sp500tr": ann(j['b'].iloc[0], j['b'].iloc[-1], days),
                 "annualized_difference": ann(j['a'].iloc[0], j['a'].iloc[-1], days) - ann(j['b'].iloc[0], j['b'].iloc[-1], days),
                 "te_monthly_ann": float((j.pct_change()["a"] - j.pct_change()["b"]).std() * np.sqrt(12))}
    out["UCITS_vs_SP500TR_monthly"] = uc
    # ^GSPC and ^SP500TR vs CNBC .SPX / .SPXTR (full history)
    for t in ("^GSPC", "^SP500TR", "^VIX", "SPY"):
        c = cnbc_bars(t)
        y = clo[t].dropna()
        common = y.index.intersection(c.index)
        rel = (y.reindex(common) / c.reindex(common) - 1)
        out[f"{t}_vs_CNBC"] = {"n_common": int(len(common)), "first": str(common[0].date()) if len(common) else None,
                               "pct_within_0p01pct": float((rel.abs() <= 1e-4).mean()), "pct_within_0p1pct": float((rel.abs() <= 1e-3).mean()),
                               "pct_within_0p5pct": float((rel.abs() <= 5e-3).mean()),
                               "max_abs_diff": float(rel.abs().max()), "date_of_max": str(rel.abs().idxmax().date()) if len(rel) else None,
                               "n_yahoo_only_dates": int(len(y.index.difference(c.index).intersection(pd.date_range(c.index.min(), c.index.max())))) if len(c) else None,
                               "n_cnbc_only_dates": int(len(c.index.difference(y.index).intersection(pd.date_range(y.index.min(), CUT)))) if len(c) else None}
    # ^GSPC vs FRED SP500
    fred = {}
    for sid in ("SP500", "DGS10", "DTB3", "VIXCLS"):
        path = os.path.join(VAL_DIR, f"fred_{sid}.csv")
        if not os.path.exists(path):
            r = polite_get(S, URLS["fred_csv"].format(sid=sid), timeout=60)
            open(path, "wb").write(r.content)
        f = pd.read_csv(path)
        f.columns = ["date", "v"]
        f["date"] = pd.to_datetime(f["date"])
        fred[sid] = pd.Series(pd.to_numeric(f["v"], errors="coerce").values, index=f["date"]).dropna()

    def cmp(y, f, label, kind="rel"):
        common = y.dropna().index.intersection(f.index)
        common = common[common <= CUT]
        if kind == "rel":
            d = y.reindex(common) / f.reindex(common) - 1
            return {"label": label, "n_common": int(len(common)), "first": str(common[0].date()),
                    "pct_within_0p01pct": float((d.abs() <= 1e-4).mean()), "pct_within_0p1pct": float((d.abs() <= 1e-3).mean()),
                    "max_abs_rel_diff": float(d.abs().max()), "date_of_max": str(d.abs().idxmax().date())}
        d = (y.reindex(common) - f.reindex(common)) * 100  # bps
        dc = y.reindex(common).diff() - f.reindex(common).diff()
        return {"label": label, "n_common": int(len(common)), "first": str(common[0].date()),
                "mean_diff_bps": float(d.mean()), "median_abs_diff_bps": float(d.abs().median()),
                "p95_abs_diff_bps": float(d.abs().quantile(0.95)),
                "corr_daily_changes": float(y.reindex(common).diff().corr(f.reindex(common).diff()))}
    out["GSPC_vs_FRED_SP500"] = cmp(clo["^GSPC"], fred["SP500"], "^GSPC vs FRED SP500 (S&P DJI via FRED)")
    out["VIX_vs_FRED_VIXCLS"] = cmp(clo["^VIX"], fred["VIXCLS"], "^VIX vs FRED VIXCLS (CBOE via FRED)")
    out["TNX_vs_FRED_DGS10"] = cmp(clo["^TNX"], fred["DGS10"], "^TNX (CBOE) vs FRED DGS10 (Treasury CMT)", kind="bps")
    out["IRX_vs_FRED_DTB3"] = cmp(clo["^IRX"], fred["DTB3"], "^IRX (CBOE 13w) vs FRED DTB3 (3m bill, discount basis)", kind="bps")
    # ^VIX vs CBOE file
    path = os.path.join(VAL_DIR, "cboe_VIX_History.csv")
    if not os.path.exists(path):
        r = polite_get(S, URLS["cboe_vix"], timeout=60)
        open(path, "wb").write(r.content)
    v = pd.read_csv(path)
    v["DATE"] = pd.to_datetime(v["DATE"], format="%m/%d/%Y")
    out["VIX_vs_CBOE"] = cmp(clo["^VIX"], v.set_index("DATE")["CLOSE"], "^VIX vs CBOE VIX_History.csv")
    res["benchmarks"] = out
    save_res(res)
    print(json.dumps(out, indent=1, default=str)[:7000])


def part_badticks(res):
    bt = pd.read_csv(os.path.join(DATA, "d2_bad_ticks.csv"), parse_dates=["date", "prev_date"])
    cov = pd.read_csv(os.path.join(DATA, "d2_coverage.csv"))
    active = set(cov.loc[cov["status"] == "active", "ticker"])
    sub = bt[bt["ticker"].isin(active) & ~bt["ticker"].str.startswith("^")]
    rows = []
    for t, g in sub.groupby("ticker"):
        c = cnbc_bars(t)
        for _, r in g.iterrows():
            d, pdt = r["date"], r["prev_date"]
            if d in c.index and pdt in c.index:
                cr = c[d] / c[pdt] - 1
                rows.append(dict(ticker=t, date=d.date(), yahoo_ret=r["ret_close"], cnbc_ret=cr, category=r["category"],
                                 confirmed=bool(np.sign(cr) == np.sign(r["ret_close"]) and abs(np.log1p(cr) - np.log1p(r["ret_close"])) < np.log(1.1))))
            else:
                rows.append(dict(ticker=t, date=d.date(), yahoo_ret=r["ret_close"], cnbc_ret=np.nan, category=r["category"], confirmed=None))
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA, "d2_bad_ticks_crosscheck.csv"), index=False)
    # CNBC evidence for Yahoo split+dividend events (corrected double counts and ambiguous cases)
    acp = os.path.join(DATA, "d2_adj_corrections.csv")
    if os.path.exists(acp):
        ac = pd.read_csv(acp, parse_dates=["date"])
        ac = ac[ac["classification"].isin(["double_count_corrected", "ambiguous_flagged"])]
        clo = pd.read_parquet(os.path.join(DATA, "d2_close.parquet"))
        ev = []
        for r in ac.itertuples():
            c = cnbc_bars(r.ticker)
            cr = np.nan
            if r.date in c.index:
                j = c.index.get_loc(r.date)
                if j > 0:
                    cr = c.iloc[j] / c.iloc[j - 1] - 1
            ev.append(dict(ticker=r.ticker, date=r.date.date(), classification=r.classification, ret_close=r.ret_close,
                           ret_adj_yahoo=r.ret_adj_yahoo, ret_adj_after_d2=getattr(r, "ret_adj_after", np.nan),
                           cnbc_ret=cr))
        evd = pd.DataFrame(ev)
        evd.to_csv(os.path.join(DATA, "d2_adj_corrections_cnbc.csv"), index=False)
        res["adj_events_cnbc"] = evd.astype(str).to_dict("records")
    chk = df[df["confirmed"].notna()]
    res["badticks_crosscheck"] = {"run_utc": utcnow(), "n_events_active_tickers_nonsplit": int(len(sub)),
                                  "n_with_cnbc_data": int(len(chk)),
                                  "n_confirmed_by_cnbc": int(chk["confirmed"].astype(bool).sum()),
                                  "n_not_confirmed": int((~chk["confirmed"].astype(bool)).sum()),
                                  "by_category": chk.groupby("category")["confirmed"].agg(lambda s: f"{int(s.astype(bool).sum())}/{len(s)} confirmed").to_dict(),
                                  "not_confirmed_examples": chk.loc[~chk["confirmed"].astype(bool)].head(40).astype(str).to_dict("records")}
    save_res(res)
    print(json.dumps(res["badticks_crosscheck"], indent=1, default=str)[:5000])


def part_errors(res):
    """Systematic scan for Yahoo values contradicted by >=2 independent sources (or 1 source + internal consistency)."""
    clo = pd.read_parquet(os.path.join(DATA, "d2_close.parquet"))
    rows = []
    fr = {}
    for sid in ("SP500", "VIXCLS"):
        f = pd.read_csv(os.path.join(VAL_DIR, f"fred_{sid}.csv"))
        f.columns = ["date", "v"]
        fr[sid] = pd.Series(pd.to_numeric(f["v"], errors="coerce").values, index=pd.to_datetime(f["date"])).dropna()
    v = pd.read_csv(os.path.join(VAL_DIR, "cboe_VIX_History.csv"))
    cboe = pd.Series(v["CLOSE"].values, index=pd.to_datetime(v["DATE"], format="%m/%d/%Y"))
    # ^GSPC: Yahoo vs CNBC .SPX and FRED SP500 (FRED only last ~10y)
    y = clo["^GSPC"].dropna(); c = cnbc_bars("^GSPC")
    for d in y.index.intersection(c.index):
        e1 = y[d] / c[d] - 1
        if abs(e1) > 5e-4:
            f = fr["SP500"].get(d, np.nan)
            ok2 = (not np.isnan(f)) and abs(c[d] / f - 1) < 1e-4
            rows.append(dict(ticker="^GSPC", date=d.date(), yahoo=y[d], reference=c[d], ref_source="CNBC .SPX" + (" = FRED SP500" if ok2 else ""),
                             rel_err=e1, confirmed_by=2 if ok2 else 1, field="Close"))
    # ^VIX: Yahoo vs CBOE (+FRED)
    y = clo["^VIX"].dropna()
    for d in y.index.intersection(cboe.index):
        e1 = y[d] / cboe[d] - 1
        if abs(e1) > 5e-3:
            f = fr["VIXCLS"].get(d, np.nan)
            ok2 = (not np.isnan(f)) and abs(cboe[d] / f - 1) < 1e-3
            rows.append(dict(ticker="^VIX", date=d.date(), yahoo=y[d], reference=cboe[d], ref_source="CBOE VIX_History" + (" = FRED VIXCLS" if ok2 else ""),
                             rel_err=e1, confirmed_by=2 if ok2 else 1, field="Close"))
    # ^SP500TR: Yahoo vs CNBC .SPXTR, arbitrated by consistency with ^GSPC daily return
    y = clo["^SP500TR"].dropna(); c = cnbc_bars("^SP500TR"); g = clo["^GSPC"]
    common = y.index.intersection(c.index)
    yr, cr, gr = y.pct_change(), c.pct_change(), g.pct_change()
    for d in common:
        e1 = y[d] / c[d] - 1
        if abs(e1) > 1e-3:
            ycons = abs(yr.get(d, np.nan) - gr.get(d, np.nan)) < 0.002
            ccons = abs(cr.get(d, np.nan) - gr.get(d, np.nan)) < 0.002
            rows.append(dict(ticker="^SP500TR", date=d.date(), yahoo=y[d], reference=c[d],
                             ref_source="CNBC .SPXTR; arbiter=^GSPC daily return (yahoo consistent=%s, cnbc consistent=%s)" % (ycons, ccons),
                             rel_err=e1, confirmed_by=2 if (ccons and not ycons) else 1, field="Close"))
    # SPY: Yahoo vs CNBC, arbitrated by ^GSPC ratio stability
    y = clo["SPY"].dropna(); c = cnbc_bars("SPY")
    for d in y.index.intersection(c.index):
        e1 = y[d] / c[d] - 1
        if abs(e1) > 5e-3:
            k = (y / g).rolling(11, center=True).median().get(d, np.nan)
            ycons = abs((y[d] / g[d]) / k - 1) < 2e-3
            ccons = abs((c[d] / g[d]) / k - 1) < 2e-3
            rows.append(dict(ticker="SPY", date=d.date(), yahoo=y[d], reference=c[d],
                             ref_source="CNBC SPY; arbiter=SPY/^GSPC ratio (yahoo consistent=%s, cnbc consistent=%s)" % (ycons, ccons),
                             rel_err=e1, confirmed_by=(2 if (ccons and not ycons) else (0 if ycons else 1)), field="Close"))
    # stock-level: unconfirmed large moves from the CNBC cross-check
    bx = os.path.join(DATA, "d2_bad_ticks_crosscheck.csv")
    if os.path.exists(bx):
        x = pd.read_csv(bx)
        bt = pd.read_csv(os.path.join(DATA, "d2_bad_ticks.csv"))
        x = x.merge(bt[["ticker", "date", "ret_adj", "category"]], on=["ticker", "date"], how="left", suffixes=("", "_bt"))
        for r in x[x["confirmed"] == False].itertuples():
            adj_ok = pd.notna(r.ret_adj) and abs(r.ret_adj - r.cnbc_ret) < 0.05
            rows.append(dict(ticker=r.ticker, date=r.date, yahoo=r.yahoo_ret, reference=r.cnbc_ret,
                             ref_source="CNBC daily return (values are returns); Yahoo Adj Close return=%.4f" % r.ret_adj,
                             rel_err=r.yahoo_ret - r.cnbc_ret, confirmed_by=1,
                             field="Close return" + (" (Adj Close OK)" if adj_ok else " (Adj Close also affected)")))
    er = pd.DataFrame(rows)
    er.to_csv(os.path.join(DATA, "d2_confirmed_errors.csv"), index=False)
    write_meta(os.path.join(DATA, "d2_confirmed_errors.csv"), {"source": "d2_validate.py part_errors", "rows": int(len(er)),
        "definition": "Yahoo values contradicted by independent sources. confirmed_by=2: two independent sources (or one source "
                      "plus an internal-consistency arbiter) agree against Yahoo; 1: single-source disagreement; 0: the other "
                      "source is the outlier. Panels are NOT modified; apply corrections downstream if desired."})
    res["confirmed_errors"] = {"n_rows": int(len(er)), "by_ticker_confirmed2": er[er["confirmed_by"] == 2]["ticker"].value_counts().to_dict() if len(er) else {},
                               "rows_confirmed2": er[er["confirmed_by"] == 2].astype(str).to_dict("records") if len(er) else []}
    save_res(res)
    print(er.to_string()[:6000])


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "all"
    res = load_res()
    if "stooq_probe" not in res or part == "stooq":
        res["stooq_probe"] = stooq_probe(); save_res(res)
    if part in ("sample", "all"):
        part_sample(res)
    if part in ("latest", "all"):
        part_latest(res)
    if part in ("bench", "all"):
        part_bench(res)
    if part in ("badticks", "all"):
        part_badticks(res)
    if part in ("errors", "all"):
        part_errors(res)
