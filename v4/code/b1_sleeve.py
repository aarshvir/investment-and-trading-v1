"""b1_sleeve.py - lead-requested tests of the pre-fixed construction rule (v4/code/lead_portfolio.py, 2026-09-26 ~00:30):
 (1) as-implemented sleeve: quarter-end, composite ranking among names with 1y daily vol <= 45%, top 20 with <=2 names
     per SIC-4 and <=25% of names per (SIC-derived) sector, weights ~ 1/vol clipped 3-8% with sector weight cap 25%
     solved by lead_portfolio.build_weights (caps never broken; infeasible residual held as T-bill cash), held quarterly;
 (2) blends SPY/sleeve 70/30 and 50/50, monthly rebalanced;
 (3) sensitivity: equal-weight top-20, inverse-vol top-30, equal-weight top-30 (same selection rules);
 plus the failed-bank sensitivity for the PIT EW universe (SIVB, SBNY, FRC at -100%).
Called from b1_phaseb.py; returns a dict for b1_results.json['phase_b']['lead_sleeve'].
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from b1_common import COST_BPS, LIVE_DATE, PENDING_DEAL_EXCLUDE, cagr, relative_block, nw_mean_test
from lead_portfolio import build_weights  # lead's construction code (read-only import)


def select(g, n, max_sic=2, sector_share=0.25, vol_max=0.45, exclude=()):
    d = g[g.composite.notna() & (g.vol_1y <= vol_max) & g.vol_1y.notna()]
    if len(exclude):
        d = d[~d.series.isin(exclude)]
    d = d.sort_values(["composite", "entity"], ascending=[False, True])
    cap_n = max(int(np.floor(sector_share * n)), 1)
    picks, sic, sc = [], {}, {}
    for r in d.itertuples(index=False):
        s4 = int(r.sic) if pd.notna(r.sic) else -1
        if s4 >= 0 and sic.get(s4, 0) >= max_sic:
            continue
        if sc.get(r.sector, 0) >= cap_n:
            continue
        picks.append(r.entity)
        sic[s4] = sic.get(s4, 0) + 1
        sc[r.sector] = sc.get(r.sector, 0) + 1
        if len(picks) == n:
            break
    return d.set_index("entity").loc[picks]


def weights_for(sel, scheme):
    if scheme == "ew":
        return pd.Series(1.0 / len(sel), index=sel.index), 0.0, True
    df = pd.DataFrame({"sector": sel.sector.values, "sub": sel.sic.fillna(-1).astype(int).astype(str).values,
                       "vol": sel.vol_1y.values, "mult": 1.0}, index=sel.index)
    try:
        w, cash, checks, _ = build_weights(df, hi=0.08, lo=0.03, sector_cap=0.25, sub_cap=0.16)
        w = w.clip(lower=0)
        if cash > 1e-9:
            w = pd.concat([w, pd.Series({"CASH": cash})])
        return w, float(cash), True
    except Exception:  # noqa - solver failure: fall back to equal weight (counted and reported)
        return pd.Series(1.0 / len(sel), index=sel.index), 0.0, False


def daily_nav(W, dates, nxt, ser_of, adj, cost_bps=COST_BPS):
    """daily NAV for a book re-set at W's dates and drifting otherwise; CASH flat intra-month (conservative)"""
    prev = pd.Series(dtype=float)
    level, parts = 1.0, []
    for t in dates:
        if not parts and t in W and len(W[t]):
            parts.append(pd.Series({t: 1.0}))
        if t in W and len(W[t]):
            w = W[t]
        elif len(prev):
            w = prev
        else:
            continue
        idx = w.index.union(prev.index)
        traded = float((w.reindex(idx, fill_value=0) - prev.reindex(idx, fill_value=0)).abs().sum())
        level *= (1 - cost_bps / 1e4 * traded)
        t1 = nxt[t]
        names = [e for e in w.index if e != "CASH"]
        sers = [ser_of.get((t, e)) for e in names]
        blk = adj.loc[t:t1, sers].ffill()
        rel = (blk / blk.iloc[0]).to_numpy()
        wn = w.reindex(names).to_numpy()
        path = (rel * wn).sum(axis=1) + float(w.get("CASH", 0.0))
        parts.append(pd.Series(level * path[1:], index=blk.index[1:]))
        end_rel = pd.Series(rel[-1], index=names)
        vals = pd.concat([w.reindex(names) * end_rel, pd.Series({"CASH": float(w.get("CASH", 0.0))})])
        vals = vals[vals > 0]
        level *= path[-1]
        prev = vals / vals.sum()
    return pd.concat(parts)


def run_sleeve_tests(G, rets, dates, q_dates, nxt, B, U, adj, sim, cstats, P):
    out = {}
    ser_of = U.set_index(["month_end", "entity"]).series
    rets_c = {t: pd.concat([r, pd.Series({"CASH": B.rf.get(nxt[t], 0.0)})]) for t, r in rets.items()}
    specs = {"sleeve_top20_invvol_q (as implemented)": (20, "invvol"), "top20_ew_q": (20, "ew"),
             "top30_invvol_q": (30, "invvol"), "top30_ew_q": (30, "ew")}
    series_net = {}
    for name, (n, scheme) in specs.items():
        W, cash_l, fails = {}, [], 0
        for t in q_dates:
            sel = select(G[t], n)
            w, cash, ok = weights_for(sel, scheme)
            W[t] = w
            cash_l.append(cash)
            fails += (not ok)
        s = sim(W, rets_c, [t for t in dates if t >= q_dates[0]], nxt)
        st = cstats(s.net, B, {"turnover_1w_yr": float(s.traded.iloc[1:].mean() / 2 * 12), "avg_names": float(s.n.mean()),
                               "avg_cash": float(np.mean(cash_l)), "max_cash": float(np.max(cash_l)),
                               "solver_failures_fallback_ew": int(fails)})
        nav = daily_nav(W, [t for t in dates if t >= q_dates[0]], nxt, ser_of, adj)
        st["mdd_daily"] = float((nav / nav.cummax() - 1).min())
        st["mdd_daily_date"] = str((nav / nav.cummax() - 1).idxmin().date())
        series_net[name] = (s.net, nav)
        out[name] = st
    # (2) blends with SPY (monthly rebalanced), based on the as-implemented sleeve
    s_net, s_nav = series_net["sleeve_top20_invvol_q (as implemented)"]
    spy_d = adj["SPY"]
    for a in (0.7, 0.5):
        r = (a * B.bench_SPY.reindex(s_net.index) + (1 - a) * s_net).dropna()
        st = cstats(r, B)
        # daily path: monthly rebalanced mix of SPY and sleeve NAV
        parts, level = [], 1.0
        me = list(s_net.index)
        prev_me = [s_nav.index[0]] + me[:-1]      # s_nav starts with 1.0 at the first formation date
        for t0, t1 in zip(prev_me, me):
            sl = s_nav.loc[t0:t1]
            sp = spy_d.loc[sl.index[0]:t1]
            rel = a * (sp / sp.iloc[0]) + (1 - a) * (sl.reindex(sp.index).ffill() / sl.iloc[0])
            parts.append(level * rel.iloc[1:])
            level *= float(rel.iloc[-1])
        bnav = pd.concat(parts)
        st["mdd_daily"] = float((bnav / bnav.cummax() - 1).min())
        rel12 = ((1 + r).rolling(12).apply(np.prod, raw=True) - (1 + B.bench_SPY.reindex(r.index)).rolling(12).apply(np.prod, raw=True)).dropna()
        st["worst_12m_relative_vs_spy"] = float(rel12.min())
        st["worst_12m_relative_end"] = str(rel12.idxmin().date())
        out[f"blend_SPY{int(a * 100)}_sleeve{int(round((1 - a) * 100))}"] = st
    # live sleeve (same rule, pending-deal names excluded) as of 2026-09-25
    L = P[(P.month_end == LIVE_DATE) & P.in_universe]
    sel = select(L, 20, exclude=PENDING_DEAL_EXCLUDE)
    w, cash, ok = weights_for(sel, "invvol")
    out["live_sleeve_2026-09-25"] = {"names": [{"ticker": str(sel.series.get(e)), "sector": str(sel.sector.get(e)),
                                                "sic": (None if pd.isna(sel.sic.get(e)) else int(sel.sic.get(e))),
                                                "composite": round(float(sel.composite.get(e)), 4),
                                                "vol_1y": round(float(sel.vol_1y.get(e)), 4),
                                                "weight": round(float(w.get(e, 0.0)), 4)} for e in sel.index],
                                     "cash": round(float(cash), 4), "solver_ok": bool(ok),
                                     "note": "screen output under the pre-fixed rule; the backtest shows no evidence of alpha"}
    # failed members missing from Yahoo: -100% sensitivity for the PIT EW universe
    fails = {"SIVB": "2023-02-28", "SBNY": "2023-02-28", "FRC": "2023-04-28"}
    harsh = {"SIVB": "2023-02-28", "SBNY": "2023-02-28", "FRC": "2023-02-28"}
    ew = B.pit_ew_universe_net.copy()
    nuniv = {t: len(g) for t, g in G.items()}
    res_f = {}
    for lab, spec in (("as_instructed (SIVB,SBNY 2023-03; FRC 2023-05)", fails),
                      ("harsh (FRC total loss from 2023-02-28)", harsh)):
        adj_ew = ew.copy()
        for tk, d0 in spec.items():
            t = pd.Timestamp(d0)
            m = nxt[t]
            n = nuniv.get(t, 500)
            adj_ew.loc[m] = (adj_ew.loc[m] * n - 1.0) / (n + 1)
        res_f[lab] = {"pit_ew_cagr": cagr(ew), "pit_ew_cagr_adj": cagr(adj_ew), "delta_cagr": cagr(adj_ew) - cagr(ew),
                      "top30_excess_vs_adj_ew": cagr(B.primary_top30_ew_net) - cagr(adj_ew),
                      "pit_ew_adj_minus_rsp_cagr": cagr(adj_ew) - cagr(B.bench_RSP)}
    out["failed_member_sensitivity"] = res_f
    return out
