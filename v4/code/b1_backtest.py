"""b1_backtest.py - Phase A of the B1 PIT backtest: primary composite portfolios, benchmarks, statistics,
decile table, IC, calibration tables, live scores.  Reads v4/data/b1_panel.parquet (b1_panel.py).
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats as sps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b1_common import (COST_BPS, DATA, FAMILIES, FIRST_FORMATION, EXPLORATORY_FIRST_FORMATION, LAST_RETURN_ME, LIVE_DATE, METRICS, OUT,  # noqa
                       PENDING_DEAL_EXCLUDE, calendar_year_table, cagr, max_drawdown, month_end_days, nw_mean_test,
                       perf_block, relative_block, subperiods, to_jsonable, utcnow, wilson, write_meta)

BENCH = ["SPY", "RSP", "^SP500TR"]


# ------------------------------------------------------------------------------------------------ data
def load():
    P = pd.read_parquet(DATA / "b1_panel.parquet")
    P["month_end"] = pd.DatetimeIndex(P.month_end)
    adj = pd.read_parquet(DATA / "d2_adjclose.parquet")
    adj.index = pd.DatetimeIndex(adj.index)
    ME_ALL = month_end_days(adj.index)
    return P, adj, ME_ALL


def formation_dates(ME_ALL):
    return [t for t in ME_ALL if FIRST_FORMATION <= t < LAST_RETURN_ME]


def next_me(ME_ALL):
    s = pd.Series(ME_ALL[1:], index=ME_ALL[:-1])
    return s.to_dict()


# ------------------------------------------------------------------------------------------------ portfolios
def simulate(weights: dict, rets: dict, dates, nxt, cost_bps=COST_BPS, lag=0):
    """weights[t]: Series entity->target weight formed at t (uses data <= t). rets[t]: Series entity->return t->t+1.
    lag=1: weights formed at t are traded at t+1 (implementation lag)."""
    prev = pd.Series(dtype=float)
    rows = []
    dates = list(dates)
    for i, t in enumerate(dates):
        src = dates[i - lag] if i - lag >= 0 else None
        if src is None or src not in weights or len(weights[src]) == 0:
            continue
        w = weights[src]
        idx = w.index.union(prev.index)
        traded = float((w.reindex(idx, fill_value=0) - prev.reindex(idx, fill_value=0)).abs().sum())
        r = rets[t].reindex(w.index)
        valid = r.notna()
        if valid.sum() == 0:
            continue
        wv = w[valid] / w[valid].sum()
        gross = float((wv * r[valid]).sum())
        cost = cost_bps / 1e4 * traded
        net = (1 + gross) * (1 - cost) - 1
        prev = wv * (1 + r[valid]) / (1 + gross)
        rows.append({"month_end": nxt[t], "gross": gross, "net": net, "turnover_oneway": traded / 2,
                     "n_names": int(len(w)), "n_no_return": int((~valid).sum())})
    return pd.DataFrame(rows).set_index("month_end")


def sel_top_n(df, n, col="composite"):
    d = df[df[col].notna()].sort_values([col, "entity"], ascending=[False, True]).head(n)
    return pd.Series(1.0 / len(d), index=d.entity) if len(d) else pd.Series(dtype=float)


def sel_quantile(df, lo, hi, col="composite"):
    d = df[(df[col] > lo) & (df[col] <= hi)]
    return pd.Series(1.0 / len(d), index=d.entity) if len(d) else pd.Series(dtype=float)


def sel_all(df):
    return pd.Series(1.0 / len(df), index=df.entity) if len(df) else pd.Series(dtype=float)


# ------------------------------------------------------------------------------------------------ main
def main():
    P, adj, ME_ALL = load()
    dates = formation_dates(ME_ALL)
    dates_x = [t for t in ME_ALL if EXPLORATORY_FIRST_FORMATION <= t < LAST_RETURN_ME]
    nxt = next_me(ME_ALL)
    U = P[P.in_universe & P.month_end.isin(dates_x)]
    G = {t: g for t, g in U.groupby("month_end")}
    rets = {t: g.set_index("entity").ret_next for t, g in G.items()}

    # benchmarks (month-end TR from adjusted closes on the same calendar)
    adj_me = adj.loc[ME_ALL]
    bret = (adj_me[BENCH] / adj_me[BENCH].shift(1) - 1)
    irx = adj.loc[ME_ALL, "^IRX"]
    rf = (irx.shift(1) / 1200.0)            # T-bill yield known at start of month, simple monthly
    ret_months = [nxt[t] for t in dates]
    bret = bret.loc[ret_months]
    rf = rf.loc[ret_months]

    strat_w = {
        "primary_top30_ew": {t: sel_top_n(g, 30) for t, g in G.items()},
        "primary_topquintile_ew": {t: sel_quantile(g, 0.8, 1.0) for t, g in G.items()},
        "primary_bottomquintile_ew": {t: sel_quantile(g, 0.0, 0.2) for t, g in G.items()},
        "pit_ew_universe": {t: sel_all(g) for t, g in G.items()},
        "pit_ew_scored_universe": {t: sel_all(g[g.composite.notna()]) for t, g in G.items()},
    }
    sims = {k: simulate(w, rets, dates, nxt, cost_bps=(0 if k.startswith("pit_ew") else COST_BPS))
            for k, w in strat_w.items()}
    sims_x = {k: simulate(strat_w[k], rets, dates_x, nxt, cost_bps=(0 if k.startswith("pit_ew") else COST_BPS))
              for k in ("primary_top30_ew", "primary_topquintile_ew", "pit_ew_universe")}
    R = pd.DataFrame({f"{k}_net": v.net for k, v in sims.items()})
    for k, v in sims.items():
        R[f"{k}_gross"] = v.gross
        R[f"{k}_turnover"] = v.turnover_oneway
        R[f"{k}_n"] = v.n_names
        R[f"{k}_n_noret"] = v.n_no_return
    q5 = sims["primary_topquintile_ew"]
    q1 = sims["primary_bottomquintile_ew"]
    R["q5_minus_q1_gross"] = q5.gross - q1.gross
    for b in BENCH:
        R[f"bench_{b}"] = bret[b]
    R["rf"] = rf
    R.index.name = "month_end"
    R.to_parquet(DATA / "b1_strategy_returns_monthly.parquet")
    write_meta(DATA / "b1_strategy_returns_monthly.parquet", {
        "rows": len(R), "columns": list(R.columns), "index": "return month-end (last NYSE trading day)",
        "definitions": {"*_net": "EW, rebalanced monthly at month-end close, 10 bps per unit traded (buys+sells)",
                        "*_turnover": "one-way turnover = sum|w_target - w_drifted|/2",
                        "*_n_noret": "holdings without a next-month price (delisted mid-month): excluded from that month's return (primary treatment)",
                        "pit_ew_universe": "all PIT members with a valid price at t, equal weight, no costs",
                        "rf": "^IRX (13-week T-bill) at start of month / 1200"},
        "phase": "A"})

    # ---------------------------------------------------------------- statistics
    res = {"phase": "A", "generated_utc": utcnow(),
           "membership_source": str(P.mem_src.iloc[0]),
           "sample": {"first_return_month": str(R.index.min().date()), "last_return_month": str(R.index.max().date()),
                      "n_months": int(len(R))}}
    strat_stats = {}
    benches = {"SPY": R["bench_SPY"], "RSP": R["bench_RSP"], "SP500TR": R["bench_^SP500TR"],
               "PIT_EW": R["pit_ew_universe_net"]}
    for k in ["primary_top30_ew", "primary_topquintile_ew", "primary_bottomquintile_ew", "pit_ew_universe",
              "pit_ew_scored_universe"]:
        r = R[f"{k}_net"]
        d = {"net": perf_block(r, R.rf), "gross": perf_block(R[f"{k}_gross"], R.rf),
             "avg_turnover_oneway_monthly": float(R[f"{k}_turnover"].iloc[1:].mean()),
             "annual_turnover_oneway": float(R[f"{k}_turnover"].iloc[1:].mean() * 12),
             "avg_names": float(R[f"{k}_n"].mean()), "total_holding_months_without_return": int(R[f"{k}_n_noret"].sum())}
        d["vs"] = {b: relative_block(r, s) for b, s in benches.items() if not (k == "pit_ew_universe" and b == "PIT_EW")}
        d["subperiods_vs_SPY"] = subperiods(r, R.bench_SPY)
        d["subperiods_vs_PIT_EW"] = subperiods(r, R.pit_ew_universe_net)
        strat_stats[k] = d
    for b in BENCH:
        strat_stats[f"bench_{b}"] = {"net": perf_block(R[f"bench_{b}"], R.rf)}
    ls = R.q5_minus_q1_gross
    strat_stats["q5_minus_q1_gross"] = {"mean_monthly": float(ls.mean()), "ann_mean": float(ls.mean() * 12),
                                        "nw": nw_mean_test(ls, 3), "cagr_longshort": cagr(ls)}
    res["strategies"] = strat_stats
    # exploratory extension 2010-01 start (thin 2010-11 fundamentals coverage; NOT headline)
    bx = pd.DataFrame({b: (adj_me[b] / adj_me[b].shift(1) - 1) for b in BENCH})
    rfx = (irx.shift(1) / 1200.0)
    ex = {}
    for k in ("primary_top30_ew", "primary_topquintile_ew"):
        r = sims_x[k].net
        ex[k] = {"net": perf_block(r, rfx), "vs_SPY": relative_block(r, bx.SPY.reindex(r.index)),
                 "vs_PIT_EW": relative_block(r, sims_x["pit_ew_universe"].net)}
    res["exploratory_2010_start"] = ex
    cal = calendar_year_table({"top30_net": R.primary_top30_ew_net, "topQ_net": R.primary_topquintile_ew_net,
                               "PIT_EW": R.pit_ew_universe_net, "SPY": R.bench_SPY, "RSP": R["bench_RSP"],
                               "SP500TR": R["bench_^SP500TR"]})
    cal["top30_minus_SPY"] = cal.top30_net - cal.SPY
    cal["top30_minus_PIT_EW"] = cal.top30_net - cal.PIT_EW
    cal["PIT_EW_minus_RSP"] = cal.PIT_EW - cal.RSP
    res["calendar_years"] = cal.round(4).reset_index().rename(columns={"month_end": "year"}).to_dict(orient="records")

    # FF5 + UMD regression of monthly excess over rf
    try:
        ff = pd.read_parquet(DATA / "r3_ff_factors_monthly.parquet")
        ff.index = pd.DatetimeIndex(ff.index).to_period("M")
        fac = ["mkt_rf", "smb", "hml", "rmw", "cma", "umd"]
        ffr = {}
        for k in ["primary_top30_ew", "primary_topquintile_ew", "pit_ew_universe"]:
            y = R[f"{k}_net"].copy()
            y.index = y.index.to_period("M")
            df = pd.concat([y.rename("y"), ff[fac + ["rf"]]], axis=1, join="inner").dropna()
            X = sm.add_constant(df[fac])
            m = sm.OLS(df.y - df.rf, X).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
            ffr[k] = {"n": int(len(df)), "alpha_monthly": float(m.params["const"]),
                      "alpha_ann": float(m.params["const"] * 12), "alpha_t_nw": float(m.tvalues["const"]),
                      "loadings": {f: float(m.params[f]) for f in fac},
                      "t": {f: float(m.tvalues[f]) for f in fac}, "r2": float(m.rsquared)}
        res["ff5_umd_regression"] = ffr
    except Exception as e:  # noqa
        res["ff5_umd_regression"] = {"error": str(e)}

    # ---------------------------------------------------------------- IC, deciles
    S = U[U.composite.notna() & U.month_end.isin(dates)]
    ic1 = S.groupby("month_end").apply(lambda g: sps.spearmanr(g.composite, g.ret_next, nan_policy="omit")[0]
                                       if g.ret_next.notna().sum() > 20 else np.nan)
    ic12 = S.groupby("month_end").apply(lambda g: sps.spearmanr(g.composite, g.fwd12, nan_policy="omit")[0]
                                        if g.fwd12.notna().sum() > 20 else np.nan)
    res["ic"] = {}
    for nm, ic, lags in (("composite_1m", ic1, 3), ("composite_12m", ic12, 12)):
        ic = ic.dropna()
        nw = nw_mean_test(ic, lags)
        res["ic"][nm] = {"n_months": int(len(ic)), "mean": float(ic.mean()), "std": float(ic.std()),
                         "ir": float(ic.mean() / ic.std()), "nw_t": nw["t"], "nw_lags": lags,
                         "share_positive": float((ic > 0).mean())}
    # per family IC (1m)
    for fam in FAMILIES:
        c = f"fam_{fam}"
        icf = U[U[c].notna()].groupby("month_end").apply(
            lambda g: sps.spearmanr(g[c], g.ret_next, nan_policy="omit")[0] if g.ret_next.notna().sum() > 20 else np.nan).dropna()
        res["ic"][f"family_{fam}_1m"] = {"mean": float(icf.mean()), "nw_t": nw_mean_test(icf, 3)["t"],
                                         "n_months": int(len(icf))}
    dec = S.groupby(["month_end", "decile"]).agg(f12=("fwd12", "mean"), r1=("ret_next", "mean")).reset_index()
    dt_ = dec.groupby("decile").agg(mean_fwd12=("f12", "mean"), mean_ret1m_ann=("r1", lambda x: x.mean() * 12),
                                    n_months=("f12", lambda x: x.notna().sum()))
    cnt = S.groupby("decile").size()
    dt_["n_stock_months"] = cnt
    rho = sps.spearmanr(dt_.index, dt_.mean_fwd12)[0]
    steps = int((np.diff(dt_.mean_fwd12.values) > 0).sum())
    res["decile_table"] = {"rows": dt_.round(5).reset_index().to_dict(orient="records"),
                           "spearman_decile_vs_fwd12": float(rho), "n_increasing_steps_of_9": steps,
                           "d10_minus_d1_fwd12": float(dt_.mean_fwd12.iloc[-1] - dt_.mean_fwd12.iloc[0]),
                           "note": "time-series average of cross-sectional decile means; fwd12 excludes names without a price 12m later (acquired/delisted)"}

    # ---------------------------------------------------------------- calibration panel & tables
    C = P[P.in_universe & P.composite.notna() & (P.month_end >= FIRST_FORMATION)][
        ["month_end", "entity", "series", "sector", "composite", "decile", "quintile", "vol_1y", "vol_tercile",
         "ret_next", "fwd12", "fwd12_excess_spy", "fwd12_maxdd", "fwd36", "fwd36_excess_spy"]].copy()
    C.to_parquet(DATA / "b1_calibration_panel.parquet", index=False)
    write_meta(DATA / "b1_calibration_panel.parquet", {
        "rows": len(C), "columns": list(C.columns),
        "definitions": {"fwd12": "TR from t to t+12 month-ends (NaN if no price at t+12: acquired/delisted - survivorship within window)",
                        "fwd12_excess_spy": "fwd12 - SPY TR over the same window (arithmetic)",
                        "fwd12_maxdd": "max drawdown of daily adjusted close from t to t+12 month-end",
                        "vol_tercile": "cross-sectional tercile of 1y daily vol at t (1=low)"},
        "caveat": "overlapping 12m windows: stock-months are not independent; Wilson CIs on raw n are too narrow - see n_eff columns"})

    def calib(df, keys):
        rows = []
        for k, g in df.groupby(keys):
            g12 = g[g.fwd12.notna()]
            n = len(g12)
            if n == 0:
                continue
            ge = g[g.fwd12_excess_spy.notna()]
            gd = g[g.fwd12_maxdd.notna()]
            k1 = int((g12.fwd12 > 0).sum())
            k2 = int((ge.fwd12_excess_spy > 0).sum())
            k3 = int((gd.fwd12_maxdd < -0.20).sum())
            neff = max(int(n / 12), 1)
            row = dict(zip(keys if isinstance(keys, list) else [keys], k if isinstance(k, tuple) else (k,)))
            row.update({"n": n, "n_eff": neff,
                        "p_fwd12_pos": k1 / n, "p_fwd12_pos_ci": wilson(k1, n), "p_fwd12_pos_ci_neff": wilson(k1 / n * neff, neff),
                        "p_excess_pos": k2 / len(ge) if len(ge) else np.nan, "p_excess_pos_ci": wilson(k2, len(ge)),
                        "p_excess_pos_ci_neff": wilson(k2 / max(len(ge), 1) * neff, neff),
                        "median_fwd12": float(g12.fwd12.median()), "p10_fwd12": float(g12.fwd12.quantile(0.1)),
                        "p90_fwd12": float(g12.fwd12.quantile(0.9)),
                        "median_excess": float(ge.fwd12_excess_spy.median()) if len(ge) else np.nan,
                        "p_maxdd_worse_20": k3 / len(gd) if len(gd) else np.nan, "p_maxdd_worse_20_ci": wilson(k3, len(gd)),
                        "n_fwd36": int(g.fwd36.notna().sum()),
                        "p_fwd36_excess_pos": float((g.fwd36_excess_spy.dropna() > 0).mean()) if g.fwd36.notna().any() else np.nan})
            rows.append(row)
        return pd.DataFrame(rows)

    cal_dec = calib(C, ["decile"])
    cal_dv = calib(C, ["decile", "vol_tercile"])
    cal_dec.to_csv(OUT / "b1_calibration_by_decile.csv", index=False)
    cal_dv.to_csv(OUT / "b1_calibration_by_decile_vol.csv", index=False)
    res["calibration_by_decile"] = cal_dec.round(4).to_dict(orient="records")
    res["calibration_by_decile_x_vol"] = cal_dv.round(4).to_dict(orient="records")

    # ---------------------------------------------------------------- daily max drawdown of primary top-30
    adjd = adj
    nav = []
    level = 1.0
    top30 = strat_w["primary_top30_ew"]
    ser_of = U.set_index(["month_end", "entity"]).series
    prev = pd.Series(dtype=float)
    for t in dates:
        w = top30[t]  # headline window only
        if len(w) == 0:
            continue
        t1 = nxt[t]
        sers = [ser_of.get((t, e)) for e in w.index]
        blk = adjd.loc[t:t1, sers].copy()
        blk = blk.ffill()                                  # delisted mid-month: hold last price (excluded later)
        rel = blk / blk.iloc[0]
        idx = w.index.union(prev.index)
        traded = float((w.reindex(idx, fill_value=0) - prev.reindex(idx, fill_value=0)).abs().sum())
        level *= (1 - COST_BPS / 1e4 * traded)
        path = (rel.values * w.values).sum(axis=1)
        path = path / path[0]
        nav.append(pd.Series(level * path[1:], index=blk.index[1:]))
        level = level * path[-1]
        r = rets[t].reindex(w.index)
        v = r.notna()
        g = float((w[v] / w[v].sum() * r[v]).sum())
        prev = (w[v] / w[v].sum()) * (1 + r[v]) / (1 + g)
    navd = pd.concat(nav)
    res["primary_top30_daily"] = {"mdd_daily": float((navd / navd.cummax() - 1).min()),
                                  "mdd_date": str((navd / navd.cummax() - 1).idxmin().date()),
                                  "cagr_daily_path": float(navd.iloc[-1] ** (252 / len(navd)) - 1)}
    spyd = adjd.loc[navd.index[0]:navd.index[-1], "SPY"]
    res["spy_daily_mdd_same_window"] = float((spyd / spyd.cummax() - 1).min())

    # ---------------------------------------------------------------- live scores
    L = P[P.month_end == LIVE_DATE].copy()
    cur = pd.read_csv(DATA / "d1_current_constituents.csv")
    cur["ticker_yahoo"] = cur.ticker_yahoo.str.upper().str.replace(".", "-", regex=False)
    # map each current constituent line to the panel entity: same CIK, else a lineage-related CIK (holding-company
    # reorganisation, e.g. XOM 2115436 <- 34088), else the entity whose current Yahoo symbol / series is the ticker
    Lc = L.drop(columns=["name"], errors="ignore").copy()
    ent_of_cik = {int(c): e for c, e in zip(Lc.cik, Lc.entity) if pd.notna(c)}
    lin = pd.read_csv(DATA / "d3_lineage.csv")
    for r_ in lin.itertuples(index=False):
        if int(r_.predecessor_cik) in ent_of_cik and int(r_.successor_cik) not in ent_of_cik:
            ent_of_cik[int(r_.successor_cik)] = ent_of_cik[int(r_.predecessor_cik)]
        if int(r_.successor_cik) in ent_of_cik and int(r_.predecessor_cik) not in ent_of_cik:
            ent_of_cik[int(r_.predecessor_cik)] = ent_of_cik[int(r_.successor_cik)]
    ent_of_tk = {}
    for c_ in ("series", "ycur", "ticker"):
        if c_ in Lc:
            for t_, e_ in zip(Lc[c_], Lc.entity):
                if isinstance(t_, str):
                    ent_of_tk.setdefault(t_, e_)
    cur["entity"] = [ent_of_cik.get(int(c)) or ent_of_tk.get(t) for c, t in zip(cur.cik, cur.ticker_yahoo)]
    live = cur[["ticker_yahoo", "name", "gics_sector", "gics_sub_industry", "cik", "entity"]].merge(
        Lc.drop(columns=["cik"]), on="entity", how="left")
    live = live.rename(columns={"sector": "sector_sic_based"})
    pr = cal_dec.set_index("decile")
    prv = cal_dv.set_index(["decile", "vol_tercile"])
    for c_ in ["p_fwd12_pos", "p_excess_pos", "median_fwd12", "p10_fwd12", "p90_fwd12", "p_maxdd_worse_20"]:
        live[f"cal_dec_{c_}"] = live.decile.map(pr[c_])
        live[f"cal_decvol_{c_}"] = [prv[c_].get((d, v), np.nan) if pd.notna(d) and pd.notna(v) else np.nan
                                    for d, v in zip(live.decile, live.vol_tercile)]
        live[f"cal_decvol_n_{c_}"] = [prv["n"].get((d, v), np.nan) if pd.notna(d) and pd.notna(v) else np.nan
                                      for d, v in zip(live.decile, live.vol_tercile)] if c_ == "p_fwd12_pos" else None
    live = live.drop(columns=[c for c in live.columns if live[c].isna().all() and c.startswith("cal_decvol_n_")
                              and c != "cal_decvol_n_p_fwd12_pos"])
    live["exclude_pending_deal"] = live.ticker_yahoo.isin(PENDING_DEAL_EXCLUDE)
    live["coverage_flag"] = np.select(
        [live.series.isna(), live.composite.isna(), live.n_families < 4],
        ["no_price_series", "insufficient_families_no_composite", "composite_from_3_of_4_families"], "full")
    live = live.sort_values("composite", ascending=False)
    # top-30 live (entity level, same rule as backtest; pending-deal names excluded from selection)
    ent_rank = live.drop_duplicates("entity")
    sel = ent_rank[~ent_rank.exclude_pending_deal & ent_rank.composite.notna()].head(30).entity
    live["live_top30"] = live.entity.isin(set(sel))
    live["live_rank"] = live.composite.rank(ascending=False, method="min")
    keep_cols = (["ticker_yahoo", "name", "gics_sector", "gics_sub_industry", "sector_sic_based", "sic", "cik",
                  "series", "mktcap", "mktcap_flag", "px_actual", "vol_1y", "vol_tercile", "financial"] +
                 [m for m, *_ in METRICS] + [f"pct_{m}" for m, *_ in METRICS] +
                 [f"fam_{f}" for f in FAMILIES] + [f"n_{f}" for f in FAMILIES] +
                 ["n_families", "composite_raw", "composite", "composite_qvm", "decile", "quintile", "live_rank",
                  "live_top30", "exclude_pending_deal", "coverage_flag", "staleness_days", "last_filed_date",
                  "max_filed_used"] + [c for c in live.columns if c.startswith("cal_")])
    live = live[[c for c in keep_cols if c in live.columns]]
    live["as_of"] = str(LIVE_DATE.date())
    live.to_parquet(DATA / "b1_live_scores.parquet", index=False)
    live.to_csv(DATA / "b1_live_scores.csv", index=False)
    for pth in (DATA / "b1_live_scores.parquet", DATA / "b1_live_scores.csv"):
        write_meta(pth, {"rows": len(live), "as_of": str(LIVE_DATE.date()), "columns": list(live.columns),
                         "method": "same code path as backtest (b1_panel.py): D3 lag1 fundamentals filed < 2026-09-25, prices <= 2026-09-25, PIT members at 2026-09-25",
                         "calibration": "cal_dec_* = empirical frequencies by composite decile 2009-12..2025-08 formation months (b1_calibration_by_decile.csv); cal_decvol_* by decile x vol tercile",
                         "exclusions": f"exclude_pending_deal for {PENDING_DEAL_EXCLUDE} (D4 report)",
                         "membership_source": str(P.mem_src.iloc[0]), "phase": "A"})
    res["live"] = {"as_of": str(LIVE_DATE.date()), "n_rows": int(len(live)),
                   "n_with_composite": int(live.composite.notna().sum()),
                   "coverage_flags": live.coverage_flag.value_counts().to_dict(),
                   "top30": live[live.live_top30].drop_duplicates("cik")[
                       ["ticker_yahoo", "name", "sector_sic_based", "composite", "fam_Q", "fam_V", "fam_M", "fam_S",
                        "vol_1y"]].round(3).to_dict(orient="records")}

    # market-cap validation vs legacy info.json (Yahoo marketCap, 2026-09-25)
    try:
        info = json.load(open(DATA.parent.parent / "equity_project" / "info.json", encoding="utf-8"))
        mc = {k.replace(".", "-"): v.get("marketCap") for k, v in info.items()}
        Lv = L[L.series.notna()].copy()
        Lv["mc_info"] = Lv.series.map(mc)
        Lv["ratio"] = Lv.mktcap / Lv.mc_info
        okv = (Lv.ratio - 1).abs() <= 0.05
        nv = int(Lv.mc_info.notna().sum())
        fails = Lv[~okv & Lv.mc_info.notna()].sort_values("ratio")
        res["mktcap_validation"] = {"n_compared": nv, "n_within_5pct": int(okv.sum()), "share_within_5pct": float(okv.sum() / nv),
                                    "pass_90pct_rule": bool(okv.sum() / nv >= 0.9),
                                    "failures": [{"ticker": a_, "ratio_b1_over_yahoo": (None if pd.isna(b_) else round(float(b_), 3)),
                                                  "flag": c_} for a_, b_, c_ in zip(fails.series, fails.ratio, fails.mktcap_flag)],
                                    "note": "failures dominated by Up-C/dual-class/OP-unit structures (Class-A-only share counts), ERIE Class-B count, and missing XBRL share counts"}
    except Exception as e:  # noqa
        res["mktcap_validation"] = {"error": str(e)}

    # coverage
    cov = pd.read_csv(OUT / "b1_coverage_monthly.csv", parse_dates=["month_end"]).set_index("month_end")
    cov = cov.loc[FIRST_FORMATION:]
    res["coverage"] = {"by_year": cov.groupby(cov.index.year)[["pit_members", "with_price", "with_composite"]].mean()
                       .round(1).reset_index().to_dict(orient="records"),
                       "mean_pct_with_price": float(cov.pct_with_price.mean()),
                       "mean_pct_with_composite": float(cov.pct_with_composite.mean()),
                       "delist_next_total": int(cov.delist_next.sum())}
    (OUT / "b1_results.json").write_text(json.dumps(to_jsonable(res), indent=1), encoding="utf-8")
    print("results written")
    return res, R


if __name__ == "__main__":
    main()
