"""b1x_backtest.py - Agent B1X: IC, portfolio returns, performance stats, survivorship bias-check.
Reads only b1x_panel_full.parquet / b1x_panel_current.parquet (built by b1x_build.py). No b1_*.py touched.
Writes v4/outputs/b1x_results.json.
"""
import sys
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

sys.path.insert(0, r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\code")
import b1x_common as c

ME = c.month_end_index()
FORM_MONTHS = ME[:-1]  # last month (Aug-2026) has no realized next-month return yet
REALIZED_MONTHS = ME[1:]  # calendar label of the realized return


def to_realized(signal_series: pd.Series) -> pd.Series:
    """re-index a series keyed by signal month t (value = return realized over (t,t+1]) to be keyed by the
    realized month t+1, so it lines up with benchmark series and can be compounded chronologically."""
    s = signal_series.reindex(ME)
    return pd.Series(s.values[:-1], index=REALIZED_MONTHS)


def monthly_ic(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for t, g in df.groupby("month_end"):
        gg = g[["composite", "next_ret"]].dropna()
        if len(gg) >= 10:
            rho, p = spearmanr(gg["composite"], gg["next_ret"])
        else:
            rho, p = np.nan, np.nan
        rows.append((t, rho, len(gg)))
    return pd.DataFrame(rows, columns=["month_end", "ic", "n"]).set_index("month_end").sort_index()


def select_portfolio(g: pd.DataFrame, mode: str):
    gg = g.dropna(subset=["composite"])
    if mode == "quintile":
        k = max(1, int(np.ceil(len(gg) * 0.2)))
    else:
        k = min(30, len(gg))
    return set(gg.sort_values("composite", ascending=False).head(k)["ticker"])


def portfolio_returns(df: pd.DataFrame, mode: str, cost_bps: float = c.ONE_WAY_COST_BPS):
    gross, net, turns, sizes = {}, {}, {}, {}
    prev_w = {}
    for t in FORM_MONTHS:
        g = df[df["month_end"] == t]
        if g.empty:
            continue
        names = select_portfolio(g, mode)
        rets = g[g["ticker"].isin(names)].set_index("ticker")["next_ret"].dropna()
        held = rets.index
        w_new = {tk: 1.0 / len(held) for tk in held} if len(held) else {}
        keys = set(w_new) | set(prev_w)
        turnover = 0.5 * sum(abs(w_new.get(k_, 0.0) - prev_w.get(k_, 0.0)) for k_ in keys) if keys else 0.0
        g_ret = float((rets * pd.Series(w_new)).sum()) if len(held) else np.nan
        # "10bps one-way cost" is charged on EACH leg of a rebalance (the sell of dropped names AND the buy of
        # added names); `turnover` as defined above (0.5*sum|delta w|) is a SINGLE leg, so total cost = 2x it.
        # (Caught via cross-check with B1: our original 1x formula understated net-of-cost drag by ~2x vs B1's
        # independent number; after this fix the two agree to within ~0.05pt of annual CAGR -- see b1x_report.md.)
        cost = 2.0 * turnover * (cost_bps / 10000.0)
        gross[t] = g_ret
        net[t] = g_ret - cost if pd.notna(g_ret) else np.nan
        turns[t] = turnover
        sizes[t] = len(names)
        prev_w = w_new
    idx = pd.DatetimeIndex(sorted(gross))
    return (pd.Series(gross).reindex(idx), pd.Series(net).reindex(idx),
            pd.Series(turns).reindex(idx), pd.Series(sizes).reindex(idx))


def ew_universe_returns(df: pd.DataFrame) -> pd.Series:
    return df.groupby("month_end")["next_ret"].mean()


def perf_block(monthly_ret: pd.Series, bench: pd.Series, label: str, window_start=None) -> dict:
    r = monthly_ret.dropna()
    b = bench.reindex(r.index).dropna()
    r = r.reindex(b.index)
    if window_start is not None:
        r = r[r.index >= window_start]
        b = b[b.index >= window_start]
    excess = r - b
    return {
        "label": label, "n_months": int(len(r)),
        "cagr": c.cagr(r), "ann_vol": c.ann_vol(r), "max_dd": c.max_drawdown(r),
        "bench_cagr": c.cagr(b),
        "excess_cagr": (c.cagr(r) - c.cagr(b)) if pd.notna(c.cagr(r)) and pd.notna(c.cagr(b)) else np.nan,
        "excess_mean_monthly": float(excess.mean()) if len(excess) else np.nan,
        "excess_tstat": c.tstat_mean(excess),
    }


def run(panel_path, tag):
    df = pd.read_parquet(panel_path)
    ic = monthly_ic(df)
    ic_series = ic["ic"]
    ic_stats = {"mean_ic": float(ic_series.mean()), "ic_ir": float(ic_series.mean() / ic_series.std(ddof=1)),
                "ic_tstat": c.tstat_mean(ic_series), "n_months": int(ic_series.notna().sum())}

    q_gross_sig, q_net_sig, q_turn, q_size = portfolio_returns(df, "quintile")
    t30_gross_sig, t30_net_sig, t30_turn, t30_size = portfolio_returns(df, "top30")
    ew_sig = ew_universe_returns(df)

    q_gross, q_net = to_realized(q_gross_sig), to_realized(q_net_sig)
    t30_gross, t30_net = to_realized(t30_gross_sig), to_realized(t30_net_sig)
    ew = to_realized(ew_sig)
    spy = pd.read_parquet(c.DATA / "d2_ret_monthly.parquet", columns=["SPY"])["SPY"].reindex(REALIZED_MONTHS)

    blocks = {}
    for lbl, series in [("top_quintile_gross", q_gross), ("top_quintile_net", q_net),
                         ("top30_gross", t30_gross), ("top30_net", t30_net)]:
        blocks[lbl + "_vs_ewuniverse_full"] = perf_block(series, ew, lbl + " vs EW universe (2010-02+)")
        blocks[lbl + "_vs_spy_full"] = perf_block(series, spy, lbl + " vs SPY (2010-02+)")
        blocks[lbl + "_vs_ewuniverse_headline"] = perf_block(series, ew, lbl + " vs EW universe (2012-01+)",
                                                               window_start=c.HEADLINE_START_MONTH)
        blocks[lbl + "_vs_spy_headline"] = perf_block(series, spy, lbl + " vs SPY (2012-01+)",
                                                        window_start=c.HEADLINE_START_MONTH)
    ew_level = {"cagr_full": c.cagr(ew), "cagr_headline": c.cagr(ew[ew.index >= c.HEADLINE_START_MONTH]),
                "ann_vol_full": c.ann_vol(ew), "max_dd_full": c.max_drawdown(ew)}
    spy_level = {"cagr_full": c.cagr(spy), "cagr_headline": c.cagr(spy[spy.index >= c.HEADLINE_START_MONTH]),
                 "ann_vol_full": c.ann_vol(spy), "max_dd_full": c.max_drawdown(spy)}

    ic_headline = ic_series[ic_series.index >= c.HEADLINE_START_MONTH]
    ic_stats_headline = {"mean_ic": float(ic_headline.mean()), "ic_ir": float(ic_headline.mean() / ic_headline.std(ddof=1)),
                          "ic_tstat": c.tstat_mean(ic_headline), "n_months": int(ic_headline.notna().sum())}

    return {
        "tag": tag,
        "ic_full_2010_02plus": ic_stats,
        "ic_headline_2012_01plus": ic_stats_headline,
        "portfolio_perf": blocks,
        "ew_universe": ew_level, "spy": spy_level,
        "avg_turnover_one_way": {"top_quintile": float(q_turn.mean()), "top30": float(t30_turn.mean())},
        "avg_names": {"top_quintile": float(q_size.mean()), "top30": float(t30_size.mean())},
    }, ic_series, {"q_gross": q_gross, "q_net": q_net, "t30_gross": t30_gross, "t30_net": t30_net, "ew": ew, "spy": spy}


if __name__ == "__main__":
    res_full, ic_full, series_full = run(c.DATA / "b1x_panel_full.parquet", "full_PIT_universe")
    res_cur, ic_cur, series_cur = run(c.DATA / "b1x_panel_current.parquet", "current_constituents_bias_check")

    bias = {
        "ic_mean_diff_headline_current_minus_full": res_cur["ic_headline_2012_01plus"]["mean_ic"] - res_full["ic_headline_2012_01plus"]["mean_ic"],
        "top30_cagr_diff_headline_current_minus_full": (
            res_cur["portfolio_perf"]["top30_gross_vs_spy_headline"]["cagr"] -
            res_full["portfolio_perf"]["top30_gross_vs_spy_headline"]["cagr"]
        ),
    }

    out = {
        "agent": "b1x", "generated_utc": pd.Timestamp.now("UTC").isoformat(),
        "methodology": "independent implementation per STATE.md 'Pre-registered primary model'; see b1x_report.md",
        "full_pit_universe": res_full,
        "current_constituents_bias_check": res_cur,
        "bias_check_deltas": bias,
    }
    c.write_json(c.DATA.parent / "outputs" / "b1x_results.json", out)

    ic_full.to_frame("ic").to_csv(c.DATA / "b1x_ic_series_full.csv")
    pd.DataFrame(series_full).to_csv(c.DATA / "b1x_monthly_returns_full.csv")
    pd.DataFrame(series_cur).to_csv(c.DATA / "b1x_monthly_returns_current.csv")
    print("wrote v4/outputs/b1x_results.json")
    import json
    print(json.dumps(out["full_pit_universe"]["ic_headline_2012_01plus"], indent=2))
    print(json.dumps(out["full_pit_universe"]["portfolio_perf"]["top30_gross_vs_spy_headline"], indent=2))
    print(json.dumps(out["full_pit_universe"]["portfolio_perf"]["top_quintile_gross_vs_ewuniverse_headline"], indent=2))
    print(json.dumps(out["bias_check_deltas"], indent=2))
