"""b1_phaseb.py - Phase B of the B1 PIT backtest: all variants, legacy-model replications (backtest3 v1/v2 pillars,
v3 conviction proxy), bias quantification (today's constituents vs PIT), walk-forward year table, cost stress,
implementation lag, plateau tests (size / rebalance frequency / Dirichlet family weights), robustness, and the
backtest-expert evaluator. Adds key 'phase_b' to v4/outputs/b1_results.json and writes b1_phaseb_*.csv tables.
"""
from __future__ import annotations

import json
import math
import os
import subprocess
from pathlib import Path
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b1_common import (COST_BPS, DATA, EXPLORATORY_FIRST_FORMATION, FIRST_FORMATION, LAST_RETURN_ME, OUT,  # noqa
                       cagr, calendar_year_table, max_drawdown, nw_mean_test, perf_block, relative_block, to_jsonable,
                       utcnow, write_meta)
from b1_backtest import load, next_me, sel_all, sel_quantile, sel_top_n  # noqa: E402

EVAL = (r"C:\Users\user\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\535c081e-b430-4ec4-ba06-"
        r"bb048da8b9f2\1a9fb34f-68f3-425c-97e9-1f78f2ad8b73\skills\backtest-expert\scripts\evaluate_backtest.py")
FIN_SECTORS = ("Financials", "Real Estate")


# ------------------------------------------------------------------------------------------------ engine
def sim(weights: dict, rets: dict, dates, nxt, cost_bps=COST_BPS, lag=0):
    """weights[t] = target at rebalance date t; months without an entry hold the drifted book (no trading).
    lag=1: the book formed at t is traded at the next month-end."""
    prev = pd.Series(dtype=float)
    rows = []
    dates = list(dates)
    for i, t in enumerate(dates):
        src = dates[i - lag] if i - lag >= 0 else None
        if src is not None and src in weights and len(weights[src]):
            w = weights[src]
        elif len(prev):
            w = prev
        else:
            continue
        idx = w.index.union(prev.index)
        traded = float((w.reindex(idx, fill_value=0) - prev.reindex(idx, fill_value=0)).abs().sum())
        r = rets[t].reindex(w.index)
        valid = r.notna()
        if valid.sum() == 0:
            continue
        wv = w[valid] / w[valid].sum()
        gross = float((wv * r[valid]).sum())
        net = (1 + gross) * (1 - cost_bps / 1e4 * traded) - 1
        prev = wv * (1 + r[valid]) / (1 + gross)
        rows.append({"month_end": nxt[t], "gross": gross, "net": net, "traded": traded, "n": int(len(w)),
                     "n_noret": int((~valid).sum())})
    return pd.DataFrame(rows).set_index("month_end")


def cstats(net: pd.Series, B: pd.DataFrame, extra=None) -> dict:
    r = net.dropna()
    d = perf_block(r, B.rf)
    for nm, col in (("SPY", "bench_SPY"), ("PIT_EW", "pit_ew_universe_net")):
        rb = relative_block(r, B[col])
        d[f"vs_{nm}"] = {k: rb[k] for k in ("excess_cagr", "ann_mean_excess", "nw_t", "ci95_ann_mean_excess",
                                             "information_ratio", "tracking_error", "share_months_beating")}
        d[f"vs_{nm}"]["roll12_pos"] = rb["rolling_12m"]["share_positive"]
        d[f"vs_{nm}"]["roll36_pos"] = rb["rolling_36m"]["share_positive"]
        d[f"vs_{nm}"]["roll60_pos"] = rb["rolling_60m"]["share_positive"]
    if extra:
        d.update(extra)
    return d


def flat(name, d):
    return {"strategy": name, "cagr": d["cagr"], "vol": d["vol"], "sharpe": d.get("sharpe"), "mdd_m": d["mdd_monthly"],
            "n_months": d["n_months"], "ex_spy": d["vs_SPY"]["excess_cagr"], "t_spy": d["vs_SPY"]["nw_t"],
            "ir_spy": d["vs_SPY"]["information_ratio"], "ex_ew": d["vs_PIT_EW"]["excess_cagr"],
            "t_ew": d["vs_PIT_EW"]["nw_t"], "roll36_pos_spy": d["vs_SPY"]["roll36_pos"],
            "turnover_1w_yr": d.get("turnover_1w_yr"), "avg_names": d.get("avg_names")}


# ------------------------------------------------------------------------------------------------ legacy features
def legacy_price_features(adj_close: pd.DataFrame, dates, series):
    C = adj_close[[s for s in series if s in adj_close.columns] + ["^GSPC"]].ffill(limit=5)
    feats = {}
    sma50, sma150, sma200 = (C.rolling(n, min_periods=n).mean() for n in (50, 150, 200))
    hi = C.rolling(252, min_periods=200).max()
    lo = C.rolling(252, min_periods=200).min()
    ret12 = C / C.shift(252) - 1
    ret6 = C / C.shift(126) - 1
    rC = C.pct_change(fill_method=None)
    vol = rC.rolling(252, min_periods=200).std() * np.sqrt(252)
    m = rC["^GSPC"]
    beta = rC.rolling(252, min_periods=200).cov(m).div(m.rolling(252, min_periods=200).var(), axis=0)
    D = pd.DatetimeIndex(dates)
    p = C.loc[D]
    tt = ((p > sma50.loc[D]).astype(int) + (sma50.loc[D] > sma150.loc[D]).astype(int) +
          (sma150.loc[D] > sma200.loc[D]).astype(int) + (p > sma200.loc[D]).astype(int) +
          (p / hi.loc[D] - 1 > -0.25).astype(int) + (p / lo.loc[D] - 1 > 0.3).astype(int))
    tt = tt.where(sma200.loc[D].notna())
    mdd = {}
    A = C.to_numpy(dtype=float)
    pos = {d: i for i, d in enumerate(C.index)}
    for d in D:
        i = pos[d]
        blk = A[max(0, i - 755): i + 1]
        with np.errstate(invalid="ignore", divide="ignore"):
            cm = np.fmax.accumulate(blk, axis=0)
            dd = np.nanmin(blk / cm - 1, axis=0)
        n_ok = np.isfinite(blk).sum(axis=0)
        dd[n_ok < 500] = np.nan
        mdd[d] = dd
    mdd = pd.DataFrame(mdd, index=C.columns).T
    out = []
    for nm, fr in (("tt", tt), ("ret12", ret12.loc[D]), ("ret6", ret6.loc[D]), ("vol_legacy", vol.loc[D]),
                   ("beta", beta.loc[D]), ("mdd3y", mdd)):
        s = fr.drop(columns=["^GSPC"], errors="ignore").stack().rename(nm)
        out.append(s)
    F = pd.concat(out, axis=1)
    F.index.names = ["month_end", "series"]
    return F.reset_index()


def legacy_scores(g: pd.DataFrame):
    d = g[g.rev_ttm.notna() & g.mktcap.notna()].copy()
    if len(d) < 30:
        return None
    sec = d.sector

    def pr(col, asc=True, bys=False, clip=None):
        s = d[col].astype(float).replace([np.inf, -np.inf], np.nan)
        s = s.clip(*clip) if clip else s
        s = s.fillna(s.median())
        return s.groupby(sec).rank(pct=True, ascending=asc) if bys else s.rank(pct=True, ascending=asc)

    gp = d.gp_ttm.fillna(d.rev_ttm - d.cogs_ttm)
    capex = d.capex_ttm.abs().fillna(0)
    fcf = d.ocf_ttm - capex
    ebitda = d.ebit_ttm + d.da_ttm
    d["l_roe"] = (d.ni_ttm / d.equity).where(d.equity > 0)
    d["l_om"] = d.opinc_ttm / d.rev_ttm
    d["l_fcfm"] = fcf / d.rev_ttm
    d["l_gm"] = gp / d.rev_ttm
    d["l_nde"] = ((d.total_debt.fillna(0) - d.cash_sti.fillna(0)) / ebitda).where(ebitda > 0)
    d["l_revg"] = (d.rev_ttm / d.rev_ttm_lag12 - 1).where(d.rev_ttm_lag12 > 0)
    e0 = d[[f"eps_q{i}" for i in range(4)]].sum(axis=1, min_count=4)
    e1 = d[[f"eps_q{i}" for i in range(4, 8)]].sum(axis=1, min_count=4)
    d["l_epsg"] = (e0 / e1 - 1).where(e1 > 0)
    d["l_ey"] = d.ni_ttm / d.mktcap
    d["l_fcfy"] = fcf / d.mktcap
    d["l_sy"] = d.rev_ttm / d.mktcap
    d["L_Q"] = (pr("l_roe", True, True, (-1, 1.5)) + pr("l_om", True, True) + pr("l_fcfm", True, True, (-1, 1)) +
                pr("l_gm", True, True) + pr("l_nde", False, False, (-5, 10))) / 5
    d["L_G"] = (pr("l_revg", clip=(-.5, 1.5)) + pr("l_epsg", clip=(-1, 2))) / 2
    d["L_V"] = (pr("l_ey", True, True, (-.5, .5)) + pr("l_fcfy", True, True, (-.3, .3)) + pr("l_sy", True, True)) / 3
    d["L_M"] = (d.tt.fillna(d.tt.median()) / 6 + pr("ret6") + pr("ret12", clip=(-1, 3))) / 3
    d["L_R"] = (pr("vol_legacy", False) + pr("mdd3y") + pr("beta", False)) / 3
    d["l_veto"] = (d.ni_ttm <= 0) | ((fcf < 0) & ~sec.isin(FIN_SECTORS)) | (d.mdd3y < -0.6)
    d["score_v2"] = .20 * d.L_Q + .10 * d.L_G + .35 * d.L_V + .35 * d.L_M
    d["score_v1"] = .25 * d.L_Q + .18 * d.L_G + .20 * d.L_V + .14 * d.L_M + .23 * d.L_R
    e = d[~d.l_veto].copy()
    for s in ("score_v1", "score_v2"):
        e[f"{s}_pct"] = e[s].rank(pct=True)
    d = d.join(e[["score_v1_pct", "score_v2_pct"]])
    d["qpct"] = d.L_Q.rank(pct=True)
    fin = sec.isin(FIN_SECTORS)
    bal = np.where(fin, d.l_roe > 0.10, d.l_nde <= 2.5)
    d["conv_v3"] = (~d.l_veto & (d.qpct >= 0.6) & (d.l_revg >= 0.03) & bal & (d.l_ey > 0) & (d.vol_legacy <= 0.45)
                    & (d.mdd3y >= -0.45) & (d.tt >= 4) & (d.score_v2_pct >= 0.6))
    return d


# ------------------------------------------------------------------------------------------------ main
def main():
    P, adj, ME_ALL = load()
    close = pd.read_parquet(DATA / "d2_close.parquet")
    close.index = pd.DatetimeIndex(close.index)
    nxt = next_me(ME_ALL)
    dates = [t for t in ME_ALL if FIRST_FORMATION <= t < LAST_RETURN_ME]
    dates_x = [t for t in ME_ALL if EXPLORATORY_FIRST_FORMATION <= t < LAST_RETURN_ME]
    B = pd.read_parquet(DATA / "b1_strategy_returns_monthly.parquet")
    B.index = pd.DatetimeIndex(B.index)
    U = P[P.in_universe & P.month_end.isin(dates_x)].copy()
    G = {t: g for t, g in U.groupby("month_end")}
    rets = {t: g.set_index("entity").ret_next for t, g in G.items()}
    out = {"generated_utc": utcnow()}
    table = []

    def run(name, W, ds=dates, cost=COST_BPS, lag=0, store=True, extra=None):
        s = sim(W, rets, ds, nxt, cost, lag)
        ex = {"turnover_1w_yr": float(s.traded.iloc[1:].mean() / 2 * 12), "avg_names": float(s.n.mean()),
              "holding_months_without_return": int(s.n_noret.sum())}
        if extra:
            ex.update(extra)
        st = cstats(s.net, B, ex)
        if store:
            table.append(flat(name, st))
        return s, st

    # ------------------------------------------------ 1. pre-registered variants
    V = {}
    W30 = {t: sel_top_n(g, 30) for t, g in G.items()}
    s30, V["top30_monthly"] = run("primary top-30 monthly (baseline)", W30)
    for n in (20, 40, 50):
        _, V[f"top{n}_monthly"] = run(f"primary top-{n} monthly", {t: sel_top_n(g, n) for t, g in G.items()})
    q_dates = [t for t in dates if t.month in (3, 6, 9, 12)]
    a_dates = [t for t in dates if t.month == 9]
    _, V["top30_quarterly"] = run("primary top-30 quarterly", {t: W30[t] for t in q_dates})
    s30a, V["top30_annual_sep"] = run("primary top-30 annual (end-Sep)", {t: W30[t] for t in a_dates},
                                      ds=[t for t in dates if t >= a_dates[0]])

    def sel_capped(g, n=30, max_sector=7, max_sic=2):
        d = g[g.composite.notna()].sort_values(["composite", "entity"], ascending=[False, True])
        picks, sc, sic = [], {}, {}
        for r in d.itertuples(index=False):
            s4 = int(r.sic) if pd.notna(r.sic) else -1
            if sc.get(r.sector, 0) >= max_sector or (s4 >= 0 and sic.get(s4, 0) >= max_sic):
                continue
            picks.append(r.entity)
            sc[r.sector] = sc.get(r.sector, 0) + 1
            sic[s4] = sic.get(s4, 0) + 1
            if len(picks) == n:
                break
        return pd.Series(1.0 / len(picks), index=picks)
    _, V["top30_capped"] = run("primary top-30, <=25% sector (7 names), <=2 per SIC4", {t: sel_capped(g) for t, g in G.items()})
    # buffer rule
    Wb, held = {}, set()
    for t in dates_x:
        g = G[t]
        c = g.set_index("entity").composite
        keep = {e for e in held if c.get(e, np.nan) > 0.75}
        new = set(c[c > 0.9].index)
        held = keep | new
        Wb[t] = pd.Series(1.0 / len(held), index=sorted(held)) if held else pd.Series(dtype=float)
    _, V["buffer_10_25"] = run("primary buffer: buy top-10%, hold while top-25%", Wb)
    _, V["topQ_monthly"] = run("primary top-quintile monthly", {t: sel_quantile(g, 0.8, 1.0) for t, g in G.items()})
    _, V["bottomQ_monthly"] = run("primary bottom-quintile monthly", {t: sel_quantile(g, 0.0, 0.2) for t, g in G.items()})
    _, V["qvm_top30"] = run("QVM-only composite top-30", {t: sel_top_n(g, 30, "composite_qvm") for t, g in G.items()})
    _, V["qvm_topQ"] = run("QVM-only composite top-quintile", {t: sel_quantile(g, 0.8, 1.0, "composite_qvm") for t, g in G.items()})
    for f in ("Q", "V", "M", "S"):
        _, V[f"fam_{f}_top30"] = run(f"family {f} alone top-30", {t: sel_top_n(g, 30, f"fam_{f}") for t, g in G.items()})
        _, V[f"fam_{f}_topQ"] = run(f"family {f} alone top-quintile", {t: sel_quantile(g, 0.8, 1.0, f"fam_{f}") for t, g in G.items()})

    def lowvol(g):
        v = g.vol_1y.rank(pct=True)
        d = g[v <= 0.2]
        return pd.Series(1.0 / len(d), index=d.entity) if len(d) else pd.Series(dtype=float)
    _, V["lowvol_quintile"] = run("low-volatility quintile (1y daily vol)", {t: lowvol(g) for t, g in G.items()})
    out["variants"] = V

    # ------------------------------------------------ 2. legacy replications
    feats = legacy_price_features(close, dates_x, sorted(U.series.dropna().unique()))
    feats["month_end"] = pd.DatetimeIndex(feats.month_end).as_unit("ns")
    UL = U.merge(feats, on=["month_end", "series"], how="left")
    LG = {}
    for t, g in UL.groupby("month_end"):
        d = legacy_scores(g)
        if d is not None:
            LG[t] = d
    Lg = {}
    for wname in ("v2", "v1"):
        sc = f"score_{wname}"
        Wt = {t: sel_top_n(d[~d.l_veto], 30, sc) for t, d in LG.items()}
        Wq = {t: sel_quantile(d[~d.l_veto], 0.8, 1.0, f"{sc}_pct") for t, d in LG.items()}
        _, Lg[f"{wname}_top30_monthly"] = run(f"legacy {wname} weights top-30 monthly", Wt)
        _, Lg[f"{wname}_topQ_monthly"] = run(f"legacy {wname} weights top-quintile monthly", Wq)
        _, Lg[f"{wname}_top30_annual_sep"] = run(f"legacy {wname} weights top-30 annual (end-Sep)",
                                                 {t: Wt[t] for t in a_dates}, ds=[t for t in dates if t >= a_dates[0]])
    Wc = {t: sel_all(d[d.conv_v3]) for t, d in LG.items()}
    npicks = pd.Series({t: len(w) for t, w in Wc.items()})
    _, Lg["v3_conviction_monthly"] = run("legacy v3 conviction-filter proxy, monthly", Wc,
                                         extra={"avg_picks": float(npicks.loc[dates].mean()),
                                                "min_picks": int(npicks.loc[dates].min())})
    _, Lg["v3_conviction_annual_sep"] = run("legacy v3 conviction-filter proxy, annual (late-Sep)",
                                            {t: Wc[t] for t in a_dates}, ds=[t for t in dates if t >= a_dates[0]],
                                            extra={"picks_by_year": {str(t.year): int(npicks[t]) for t in a_dates}})
    # hit-rate table comparable to handoff 9.3 loop 3 (12m buy-and-hold from late September)
    hit = []
    for t in [x for x in ME_ALL if x.month == 9 and pd.Timestamp("2012-09-01") <= x <= pd.Timestamp("2025-09-30")]:
        d = LG.get(t)
        if d is None:
            continue
        pk = d[d.conv_v3]
        spy12 = pk.fwd12_SPY.iloc[0] if len(pk) else d.fwd12_SPY.iloc[0]
        pk12 = pk[pk.fwd12.notna()]
        d12 = d[d.fwd12.notna()]
        ok_ = len(pk12) > 0
        hit.append({"start": str(t.date()), "picks": int(len(pk)), "avg_fwd12": float(pk12.fwd12.mean()) if ok_ else None,
                    "pct_up": float((pk12.fwd12 > 0).mean()) if ok_ else None,
                    "pct_beat_spy": float((pk12.fwd12 > spy12).mean()) if ok_ else None,
                    "universe_pct_up": float((d12.fwd12 > 0).mean()) if len(d12) else None,
                    "universe_avg": float(d12.fwd12.mean()) if len(d12) else None,
                    "n_with_fwd12": int(len(pk12)), "tickers": ",".join(sorted(pk.series.dropna().astype(str)))})
    Lg["v3_conviction_sep_hit_table"] = hit
    out["legacy"] = Lg

    # ------------------------------------------------ 3. cost stress, lag, walk-forward
    CS = {}
    for bps in (20, 25, 30):
        net = (1 + s30.gross) * (1 - bps / 1e4 * s30.traded) - 1
        st = cstats(net, B)
        table.append(flat(f"primary top-30 monthly @ {bps} bps", st))
        cy = calendar_year_table({"s": net, "spy": B.bench_SPY, "ew": B.pit_ew_universe_net})
        st["share_years_pos_vs_spy"] = float((cy.s > cy.spy).mean())
        st["share_years_pos_vs_ew"] = float((cy.s > cy.ew).mean())
        CS[f"{bps}bps"] = st
    _, CS["lag1_10bps"] = run("primary top-30 monthly, 1-month implementation lag", W30, lag=1)
    out["cost_stress"] = CS
    cy = calendar_year_table({"top30": s30.net, "SPY": B.bench_SPY, "PIT_EW": B.pit_ew_universe_net})
    cy["ex_spy"] = cy.top30 - cy.SPY
    cy["ex_ew"] = cy.top30 - cy.PIT_EW
    wf = cy.loc[2014:]
    out["walk_forward"] = {"years": cy.round(4).reset_index().rename(columns={"month_end": "year"}).to_dict(orient="records"),
                           "share_years_pos_vs_spy_2014on": float((wf.ex_spy > 0).mean()),
                           "share_years_pos_vs_ew_2014on": float((wf.ex_ew > 0).mean()),
                           "worst3_vs_spy": wf.ex_spy.nsmallest(3).round(4).to_dict(),
                           "worst3_vs_ew": wf.ex_ew.nsmallest(3).round(4).to_dict(),
                           "majority_years_positive_vs_spy_10bps": bool((wf.ex_spy > 0).mean() > 0.5),
                           "note": "no parameters are fitted; each year is out-of-sample with the frozen pre-registered rules"}

    # ------------------------------------------------ 4. Dirichlet family weights (500 draws, alpha=5) - vectorised
    rng = np.random.default_rng(42)
    Wd = rng.dirichlet([5, 5, 5, 5], 500)
    ents = sorted(U.entity.unique())
    eix = {e: i for i, e in enumerate(ents)}
    N, K = len(ents), len(Wd)
    Wprev = np.zeros((N, K))
    gross_m, net_m = [], []
    fams = ["fam_Q", "fam_V", "fam_M", "fam_S"]
    for t in dates:
        g = G[t]
        ix = g.entity.map(eix).to_numpy()
        F = g[fams].to_numpy(dtype=float)
        M = np.isfinite(F)
        num = np.nan_to_num(F) @ Wd.T
        den = M.astype(float) @ Wd.T
        comp = num / den
        comp[M.sum(axis=1) < 3] = -np.inf
        top = np.argpartition(-comp, 30, axis=0)[:30]
        Wt = np.zeros((N, K))
        Wt[ix[top], np.arange(K)[None, :]] = 1 / 30
        r = np.full(N, np.nan)
        r[ix] = g.ret_next.to_numpy(dtype=float)
        valid = np.isfinite(r)
        traded = np.abs(Wt - Wprev).sum(axis=0)
        wv = Wt * valid[:, None]
        wv = wv / wv.sum(axis=0, keepdims=True)
        gr = (wv * np.nan_to_num(r)[:, None]).sum(axis=0)
        gross_m.append(gr)
        net_m.append((1 + gr) * (1 - COST_BPS / 1e4 * traded) - 1)
        Wprev = wv * (1 + np.nan_to_num(r))[:, None] / (1 + gr)[None, :]
    idx = [nxt[t] for t in dates]
    NET = pd.DataFrame(np.array(net_m), index=idx)
    spy = B.bench_SPY.reindex(idx)
    ew = B.pit_ew_universe_net.reindex(idx)
    yrs = len(idx) / 12
    cg = (1 + NET).prod() ** (1 / yrs) - 1
    ex_spy = cg - ((1 + spy).prod() ** (1 / yrs) - 1)
    ex_ew = cg - ((1 + ew).prod() ** (1 / yrs) - 1)
    q = [0.05, 0.25, 0.5, 0.75, 0.95]
    out["dirichlet_500"] = {"alpha": 5, "n": K, "excess_cagr_vs_spy_q": dict(zip(map(str, q), ex_spy.quantile(q).round(4))),
                            "excess_cagr_vs_ew_q": dict(zip(map(str, q), ex_ew.quantile(q).round(4))),
                            "share_positive_vs_spy": float((ex_spy > 0).mean()),
                            "share_positive_vs_ew": float((ex_ew > 0).mean()),
                            "equal_weight_point": V["top30_monthly"]["vs_SPY"]["excess_cagr"]}
    pd.DataFrame({"w_Q": Wd[:, 0], "w_V": Wd[:, 1], "w_M": Wd[:, 2], "w_S": Wd[:, 3], "cagr_net": cg.values,
                  "excess_vs_spy": ex_spy.values, "excess_vs_pit_ew": ex_ew.values}).to_csv(OUT / "b1_phaseb_dirichlet.csv", index=False)

    # ------------------------------------------------ 5. robustness
    RB = {}
    keep = ~((s30.index.year == 2020) | (s30.index.year == 2021))
    RB["exclude_2020_21"] = cstats(s30.net[keep], B)
    # 5 largest contributors to excess vs PIT EW
    contrib = {}
    for t in dates:
        w = W30[t]
        r = rets[t].reindex(w.index)
        ewr = B.pit_ew_universe_net.get(nxt[t], np.nan)
        for e, wi in w.items():
            if pd.notna(r[e]):
                contrib[e] = contrib.get(e, 0.0) + wi * (r[e] - ewr)
    top5 = pd.Series(contrib).nlargest(5)
    tick = U.drop_duplicates("entity", keep="last").set_index("entity").series
    W30d = {t: sel_top_n(g[~g.entity.isin(top5.index)], 30) for t, g in G.items()}
    _, RB["drop_top5_contributors"] = run("primary top-30 without 5 largest excess contributors", W30d,
                                          extra={"dropped": {str(tick.get(e, e)): round(float(v), 4) for e, v in top5.items()}})
    RB["start_2010_exploratory"] = cstats(sim(W30, rets, dates_x, nxt).net, B)
    RB["costs_25bps"] = CS["25bps"]
    out["robustness"] = RB

    # ------------------------------------------------ 6. bias quantification: today's constituents vs PIT
    PT = pd.read_parquet(DATA / "b1_panel_today.parquet")
    PT["month_end"] = pd.DatetimeIndex(PT.month_end)
    UT = PT[PT.in_universe & PT.month_end.isin(dates_x)]
    GT = {t: g for t, g in UT.groupby("month_end")}
    retsT = {t: g.set_index("entity").ret_next for t, g in GT.items()}
    BI = {}

    def s_(W, R_, ds=dates, cost=COST_BPS):
        return sim(W, R_, ds, nxt, cost)

    today30 = s_({t: sel_top_n(g, 30) for t, g in GT.items()}, retsT)
    todayQ = s_({t: sel_quantile(g, 0.8, 1.0) for t, g in GT.items()}, retsT)
    todayEW = s_({t: sel_all(g) for t, g in GT.items()}, retsT, cost=0)
    pit30 = s30
    pitQ = sim({t: sel_quantile(g, 0.8, 1.0) for t, g in G.items()}, rets, dates, nxt)
    BI["primary_top30"] = {"today_cagr": cagr(today30.net), "pit_cagr": cagr(pit30.net),
                           "bias_cagr": cagr(today30.net) - cagr(pit30.net),
                           "today_excess_vs_spy": cstats(today30.net, B)["vs_SPY"]["excess_cagr"],
                           "pit_excess_vs_spy": V["top30_monthly"]["vs_SPY"]["excess_cagr"]}
    BI["primary_topQ"] = {"today_cagr": cagr(todayQ.net), "pit_cagr": cagr(pitQ.net),
                          "bias_cagr": cagr(todayQ.net) - cagr(pitQ.net)}
    BI["ew_universe"] = {"today_cagr": cagr(todayEW.net), "pit_cagr": cagr(B.pit_ew_universe_net.loc[todayEW.index]),
                         "rsp_cagr": cagr(B.bench_RSP.loc[todayEW.index]),
                         "today_minus_pit": cagr(todayEW.net) - cagr(B.pit_ew_universe_net.loc[todayEW.index]),
                         "pit_minus_rsp": cagr(B.pit_ew_universe_net.loc[todayEW.index]) - cagr(B.bench_RSP.loc[todayEW.index])}

    def mom50(GG, RR, ds):
        W = {t: sel_top_n(g.assign(_m=g.mom_12_1), 50, "_m") for t, g in GG.items() if t in set(ds)}
        return sim(W, RR, ds, nxt, 0)
    for lab, ds in (("2012-01..2026-08", dates), ("2016-10..2026-08 (lead v3-audit window)",
                                                  [t for t in dates if t >= pd.Timestamp("2016-09-30")])):
        a_ = mom50(GT, retsT, ds).net
        b_ = mom50(G, rets, ds).net
        BI[f"momentum_top50_gross {lab}"] = {"today_cagr": cagr(a_), "pit_cagr": cagr(b_), "bias_cagr": cagr(a_) - cagr(b_)}
    cyb = calendar_year_table({"PIT_EW": B.pit_ew_universe_net, "RSP": B.bench_RSP, "TODAY_EW": todayEW.net})
    cyb["PIT_minus_RSP"] = cyb.PIT_EW - cyb.RSP
    gap = (B.pit_ew_universe_net - B.bench_RSP).dropna()
    BI["residual_survivorship_pit_ew_vs_rsp"] = {
        "by_year": cyb.round(4).reset_index().rename(columns={"month_end": "year"}).to_dict(orient="records"),
        "ann_mean_gap": float(gap.mean() * 12), "nw_t": nw_mean_test(gap, 3)["t"],
        "cagr_gap": cagr(B.pit_ew_universe_net) - cagr(B.bench_RSP),
        "share_years_pit_above_rsp": float((cyb.PIT_minus_RSP > 0).mean()),
        "interpretation": ("PIT EW excludes unpriced (acquired/failed) members; the gap to RSP (which holds them, "
                           "rebalances quarterly and charges ~0.20%) estimates residual survivorship + construction "
                           "differences. Conclusions sensitive to a bias of this size: absolute CAGR levels and "
                           "small positive/negative excess estimates; not the sign of a -1% to -2.5%/yr excess.")}
    out["bias"] = BI

    # ------------------------------------------------ 6b. lead-requested construction-rule tests (b1_sleeve.py)
    from b1_sleeve import run_sleeve_tests
    out["lead_sleeve"] = run_sleeve_tests(G, rets, dates, q_dates, nxt, B, U, adj, sim, cstats, P)
    for k, v in out["lead_sleeve"].items():
        if isinstance(v, dict) and "cagr" in v:
            table.append(flat(f"lead rule: {k}", v))

    # ------------------------------------------------ 7. delisting sensitivity
    out["delisting"] = {"top30_holding_months_without_next_price": int(s30.n_noret.sum()),
                        "note": "Yahoo purges most delisted symbols, so names rarely delist in-sample; the -30%/0% "
                                "sensitivity changes nothing when the count is ~0. The survivorship problem is the "
                                "unpriced members (see coverage) rather than in-sample delistings."}

    # ------------------------------------------------ 8. backtest-expert evaluator on primary top-30
    spells = []
    for e in {e for t in dates for e in W30[t].index}:
        cur_, rr, sp = None, [], []
        for t in dates:
            if e in W30[t].index:
                r = rets[t].get(e, np.nan)
                rr.append((nxt[t], r))
            elif rr:
                spells.append((e, rr))
                rr = []
        if rr:
            spells.append((e, rr))
    trades = []
    for e, rr in spells:
        s = pd.Series(dict(rr)).dropna()
        if len(s) == 0:
            continue
        tr = float((1 + s).prod() - 1)
        bs = float((1 + B.bench_SPY.reindex(s.index)).prod() - 1)
        trades.append({"entity": e, "months": len(s), "ret": tr, "excess_vs_spy": tr - bs})
    T = pd.DataFrame(trades)
    T.to_csv(OUT / "b1_phaseb_top30_spells.csv", index=False)
    evals = {}
    mdd_daily = json.load(open(OUT / "b1_results.json", encoding="utf-8"))["primary_top30_daily"]["mdd_daily"]
    for mode, col in (("absolute_spell_return", "ret"), ("excess_vs_spy_spell_return", "excess_vs_spy")):
        wins = T[T[col] > 0][col]
        loss = T[T[col] <= 0][col]
        args = ["--total-trades", str(len(T)), "--win-rate", f"{100 * len(wins) / len(T):.2f}",
                "--avg-win-pct", f"{100 * wins.mean():.2f}", "--avg-loss-pct", f"{100 * abs(loss.mean()):.2f}",
                "--max-drawdown-pct", f"{100 * abs(mdd_daily):.2f}", "--years-tested", str(int(len(dates) // 12)),
                "--num-parameters", "6", "--slippage-tested", "--output-dir", str(OUT / "b1_backtest_expert" / mode)]
        try:
            pr_ = subprocess.run([sys.executable, EVAL] + args, capture_output=True, text=True, timeout=120)
            evals[mode] = {"args": " ".join(args), "stdout": pr_.stdout[-3000:], "stderr": pr_.stderr[-500:]}
        except Exception as ex_:  # noqa
            evals[mode] = {"error": str(ex_)}
    evals["mapping"] = ("trade = one contiguous holding spell of a name in the monthly top-30 (entry at month-end "
                        "t, exit when it leaves the top-30); trade return = compounded monthly TR over the spell "
                        "(absolute mode) or minus SPY TR over the same months (excess mode); max drawdown = daily "
                        "top-30 portfolio MDD; parameters = 6 (portfolio size, rebalance frequency, 3 free family "
                        "weights, composite family threshold) although none were tuned; costs modelled (10 bps).")
    out["backtest_expert"] = evals

    # ------------------------------------------------ 9. membership-source robustness (D1 primary vs D2 spells)
    try:
        from scipy.stats import spearmanr
        d2 = json.load(open(OUT / "b1_results_d2spells.json", encoding="utf-8"))
        cur_ = json.load(open(OUT / "b1_results.json", encoding="utf-8"))
        rows_ = []
        for lab, x in (("D1 CIK-level membership (primary)", cur_), ("D2 fja05680 spells (sensitivity)", d2)):
            cov_ = x["coverage"]
            for k in ("primary_top30_ew", "primary_topquintile_ew", "pit_ew_universe"):
                v = x["strategies"][k]
                rows_.append({"membership": lab, "strategy": k, "cagr": v["net"]["cagr"],
                              "excess_vs_spy": v["vs"]["SPY"]["excess_cagr"], "t_vs_spy": v["vs"]["SPY"]["nw_t"],
                              "excess_vs_pit_ew": v["vs"].get("PIT_EW", {}).get("excess_cagr"),
                              "ic_1m": x["ic"]["composite_1m"]["mean"], "ic_1m_t": x["ic"]["composite_1m"]["nw_t"],
                              "pct_members_priced": cov_["mean_pct_with_price"],
                              "pct_members_scored": cov_["mean_pct_with_composite"]})
        l1 = pd.read_csv(DATA / "b1_live_scores.csv")
        l2 = pd.read_csv(DATA / "b1_live_scores_d2spells.csv")
        mm = l1[["ticker_yahoo", "composite", "live_top30"]].merge(l2[["ticker_yahoo", "composite", "live_top30"]],
                                                                   on="ticker_yahoo", suffixes=("_d1", "_d2")).dropna()
        rho = float(spearmanr(mm.composite_d1, mm.composite_d2)[0])
        t1 = set(mm.loc[mm.live_top30_d1.astype(bool), "ticker_yahoo"])
        t2 = set(mm.loc[mm.live_top30_d2.astype(bool), "ticker_yahoo"])
        out["membership_robustness"] = {"table": rows_, "live_rank_spearman_d1_vs_d2": rho,
                                        "live_top30_overlap": len(t1 & t2), "only_d1": sorted(t1 - t2), "only_d2": sorted(t2 - t1),
                                        "material_difference": bool(abs(rows_[0]["cagr"] - rows_[3]["cagr"]) > 0.005 or rho < 0.97)}
    except Exception as ex_:  # noqa
        out["membership_robustness"] = {"error": str(ex_)}

    # ------------------------------------------------ 10. DA2 fix impact on live ranks (isolated run, then lineage fix)
    iso = Path(r"C:\Users\user\eqv4\cache\b1\da2_fix_impact_isolated.json")
    try:
        pre = DATA / "b1_live_scores_pre_lineage.csv"
        if pre.exists():
            a_ = pd.read_csv(pre)[["ticker_yahoo", "composite", "live_rank"]]
            b_ = pd.read_csv(DATA / "b1_live_scores.csv")[["ticker_yahoo", "composite", "live_rank"]]
            mm = a_.merge(b_, on="ticker_yahoo", suffixes=("_pre", "_post"))
            top70 = mm[(mm.live_rank_pre <= 70) | (mm.live_rank_post <= 70)]
            ch = top70[top70.live_rank_pre != top70.live_rank_post]
            out["lineage_fix_impact"] = {
                "what": "XOM (entity CIK 34088) was wrongly rejected as ticker reuse because SEC now lists XOM under "
                        "ExxonMobil Holdings Corp (CIK 2115436, reorganisation 2026-08); fixed with D3 lineage / D1 "
                        "multi-CIK links (reuse check + fundamentals fallback). Affects the D1 run only.",
                "n_live_top70_rank_changes": int(len(ch)),
                "max_abs_rank_change_top70": float((ch.live_rank_pre - ch.live_rank_post).abs().max()) if len(ch) else 0.0,
                "xom_live_rank_post": (None if mm[mm.ticker_yahoo == "XOM"].live_rank_post.isna().all()
                                       else float(mm.loc[mm.ticker_yahoo == "XOM", "live_rank_post"].iloc[0]))}
    except Exception as ex_:  # noqa
        out["lineage_fix_impact"] = {"error": str(ex_)}
    try:
        pre = DATA / "b1_live_scores_pre_da2.csv"
        if iso.exists():
            out["da2_fix_impact"] = json.load(open(iso, encoding="utf-8"))
            out["da2_fix_impact"]["note"] = "measured in an isolated re-run (DA2 fixes only, before the lineage fix)"
        elif pre.exists():
            a_ = pd.read_csv(pre)[["ticker_yahoo", "composite", "live_rank", "fam_S", "sue"]]
            b_ = pd.read_csv(DATA / "b1_live_scores.csv")[["ticker_yahoo", "composite", "live_rank", "fam_S", "sue"]]
            mm = a_.merge(b_, on="ticker_yahoo", suffixes=("_pre", "_post"))
            top70 = mm[(mm.live_rank_pre <= 70) | (mm.live_rank_post <= 70)]
            ch = top70[top70.live_rank_pre != top70.live_rank_post]
            hig = mm[mm.ticker_yahoo.isin(["HIG", "HAL", "ICE", "BBWI", "DXCM", "TMO", "VTRS", "BRK-B", "APA", "ERIE"])]
            out["da2_fix_impact"] = {"n_live_top70_rank_changes": int(len(ch)),
                                     "max_abs_rank_change_top70": float((ch.live_rank_pre - ch.live_rank_post).abs().max()) if len(ch) else 0.0,
                                     "entered_top70": sorted(top70.loc[(top70.live_rank_pre > 70) & (top70.live_rank_post <= 70), "ticker_yahoo"]),
                                     "left_top70": sorted(top70.loc[(top70.live_rank_pre <= 70) & (top70.live_rank_post > 70), "ticker_yahoo"]),
                                     "affected_names": hig.round(4).to_dict(orient="records")}
    except Exception as ex_:  # noqa
        out["da2_fix_impact"] = {"error": str(ex_)}

    TB = pd.DataFrame(table)
    TB.to_csv(OUT / "b1_phaseb_variants.csv", index=False)
    out["variants_table"] = TB.round(4).to_dict(orient="records")
    res = json.load(open(OUT / "b1_results.json", encoding="utf-8"))
    res["phase"] = "B"
    res["phase_b"] = to_jsonable(out)
    (OUT / "b1_results.json").write_text(json.dumps(to_jsonable(res), indent=1), encoding="utf-8")
    print("phase B written")


if __name__ == "__main__":
    main()
