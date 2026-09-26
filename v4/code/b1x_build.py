"""b1x_build.py - Agent B1X, independent build of month-end panels + pre-registered composite (STATE.md sec.
"Pre-registered primary model"). Reads only D1/D2/D3 DATA outputs (shared inputs, same as B1 uses) plus D1's
sic_to_sector() lookup function (a deterministic classification table, not backtest logic). No b1_*.py touched.

Outputs (v4/data): b1x_panel_full.parquet (PIT universe, 2010-01..2026-08), b1x_panel_current.parquet (bias
check universe = today's 503 constituents only, same window), b1x_live_scores.parquet (2026-09-25).
"""
import sys
import time
import numpy as np
import pandas as pd

sys.path.insert(0, r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\code")
import b1x_common as c

t0 = time.time()
log = lambda m: print(f"[{time.time()-t0:6.1f}s] {m}", flush=True)

# ---------- month-end grids ----------
full_idx = pd.read_parquet(c.DATA / "d2_adjclose.parquet", columns=["SPY"]).index
FULL_ME = pd.DatetimeIndex(sorted(full_idx.to_series().groupby(full_idx.to_period("M")).max().values))
ME = c.month_end_index()  # 2010-01..2026-08, 200 months (task 1 window)
log(f"month grid: {len(ME)} backtest months {ME[0].date()}..{ME[-1].date()}; full grid {len(FULL_ME)} months")

# ---------- prices / splits ----------
close = pd.read_parquet(c.DATA / "d2_close.parquet")
adjclose = pd.read_parquet(c.DATA / "d2_adjclose.parquet")
retm_raw = pd.read_parquet(c.DATA / "d2_ret_monthly.parquet")
splits = pd.read_parquet(c.DATA / "d2_splits.parquet")
tickers_priced = set(close.columns) & set(adjclose.columns) & set(retm_raw.columns)
log(f"priced tickers available: {len(tickers_priced)}")

close.index.name = "month_end"; close.columns.name = "ticker"
adjclose.index.name = "month_end"; adjclose.columns.name = "ticker"
retm_raw.index.name = "month_end"; retm_raw.columns.name = "ticker"

close_me = close.reindex(FULL_ME)
adj_me = adjclose.reindex(FULL_ME)
retm_me = retm_raw.reindex(FULL_ME)

mom_wide = adj_me.shift(1) / adj_me.shift(12) - 1          # 12-1 momentum, signal at t uses P(t-1)/P(t-12)-1
nextret_wide = retm_me.shift(-1)                            # next-month total return relative to signal date t

def _to_long(wide, me, colname):
    w = wide.reindex(me).rename_axis(index="month_end", columns="ticker")
    return w.stack().rename(colname).reset_index()


px_long = _to_long(close_me, ME, "px")
mom_long = _to_long(mom_wide, ME, "m_mom")
nextret_long = _to_long(nextret_wide, ME, "next_ret")
log("price/return/momentum long frames built")

# ---------- split factors (derived by B1X, not taken from any precomputed column) ----------


def split_factor_after_wide(splits_df, tickers, month_ends):
    sub = splits_df[splits_df["ticker"].isin(tickers)]
    mearr = np.asarray(month_ends, dtype="datetime64[ns]")
    cols = {}
    for tkr, g in sub.groupby("ticker"):
        d = np.sort(g["date"].values)
        r = g.set_index("date").loc[d, "split_ratio"].values if len(d) else np.array([])
        if len(d) == 0:
            continue
        order = np.argsort(g["date"].values)
        d = g["date"].values[order]; r = g["split_ratio"].values[order]
        rev_cum = np.cumprod(r[::-1])[::-1]
        pos = np.searchsorted(d, mearr, side="right")
        n = len(d)
        factor = np.ones(len(mearr))
        mask = pos < n
        factor[mask] = rev_cum[pos[mask]]
        cols[tkr] = factor
    out = pd.DataFrame(cols, index=pd.DatetimeIndex(mearr))
    out.index.name = "month_end"; out.columns.name = "ticker"
    return out


split_factor_wide = split_factor_after_wide(splits, tickers_priced, ME)
splitfac_long = split_factor_wide.stack().rename("split_factor_after").reset_index()
log(f"split factors derived for {split_factor_wide.shape[1]} tickers with any recorded split")

_splits_sorted = {}
for _tkr, _g in splits.sort_values("date").groupby("ticker"):
    _splits_sorted[_tkr] = (_g["date"].values, _g["split_ratio"].values)


def midwindow_split_factor(df):
    """product of split_ratio for splits with shares_out_date < split_date <= month_end, per row (d3_report.md
    sec.5.6: 'for market cap between the share-count date and t, apply splits after shares_out_date')."""
    factor = np.ones(len(df))
    so_date = df["shares_out_date"].values
    me_arr = df["month_end"].values
    valid = ~pd.isna(so_date)
    for tkr, idx in df.groupby("ticker").indices.items():
        if tkr not in _splits_sorted:
            continue
        idx = np.asarray([i for i in idx if valid[i]])
        if len(idx) == 0:
            continue
        dates, ratios = _splits_sorted[tkr]
        prefix = np.concatenate([[1.0], np.cumprod(ratios)])
        lo = np.searchsorted(dates, so_date[idx], side="right")
        hi = np.searchsorted(dates, me_arr[idx], side="right")
        factor[idx] = prefix[hi] / prefix[lo]
    return factor

# ---------- membership (PIT) ----------
src, spells = c.membership_spells()


def expand_spells(spells_df, month_ends):
    mearr = np.asarray(month_ends, dtype="datetime64[ns]")
    tk, mo = [], []
    for tkr, s, e in zip(spells_df["ticker"].values, spells_df["start"].values, spells_df["end_excl"].values):
        lo = np.searchsorted(mearr, s, side="left")
        hi = np.searchsorted(mearr, e, side="left")
        if hi > lo:
            tk.append(np.repeat(tkr, hi - lo)); mo.append(mearr[lo:hi])
    return pd.DataFrame({"ticker": np.concatenate(tk), "month_end": np.concatenate(mo)}).drop_duplicates()


mem = expand_spells(spells, ME)
mem = mem[mem["ticker"].isin(tickers_priced)].copy()
log(f"membership source={src}: {len(mem)} member-months, {mem['ticker'].nunique()} tickers")

# ---------- fundamentals (PIT, filed < t, per D3's own recommendation) ----------
fund = pd.read_parquet(c.DATA / "d3_pit_monthly_lag1.parquet")
fund = fund[fund["month_end"].isin(ME)].copy()
FUND_COLS = ["cik", "rev_ttm", "gp_ttm", "ni_ttm", "ocf_ttm", "capex_ttm", "assets", "assets_1y_ago",
             "equity", "equity_1y_ago", "total_debt", "cash_sti", "shares_out", "shares_1y_ago",
             "shares_out_date", "ebit_ttm", "sue", "is_financial"]
fund = fund[["month_end", "ticker"] + FUND_COLS]
log(f"fundamentals (lag1, filed<t): {len(fund)} rows, {fund['ticker'].nunique()} tickers")

sec_map = c.sic_sector_map()  # cik -> sic, sector, basis


def assemble(universe_long: pd.DataFrame, tag: str) -> pd.DataFrame:
    """universe_long: columns [month_end, ticker]. Returns enriched panel with prices/fundamentals/scores."""
    df = universe_long.merge(px_long, on=["month_end", "ticker"], how="left")
    df = df[df["px"].notna()].copy()  # universe = member (or current constituent) WITH a price at t
    df = df.merge(mom_long, on=["month_end", "ticker"], how="left")
    df = df.merge(nextret_long, on=["month_end", "ticker"], how="left")
    df = df.merge(splitfac_long, on=["month_end", "ticker"], how="left")
    df["split_factor_after"] = df["split_factor_after"].fillna(1.0)
    df = df.merge(fund, on=["month_end", "ticker"], how="left")
    df = df.merge(sec_map, left_on="cik", right_index=True, how="left")

    # BRK-B: companyfacts shares/EPS are Class-A equivalents (d3_report.md sec.5.6) -> scale to B-share count.
    is_brkb = df["ticker"].eq("BRK-B")
    shares_out = df["shares_out"].where(~is_brkb, df["shares_out"] * c.BRK_B_CLASS_CONVERSION)
    shares_1y = df["shares_1y_ago"].where(~is_brkb, df["shares_1y_ago"] * c.BRK_B_CLASS_CONVERSION)
    midfac = midwindow_split_factor(df)  # splits between shares_out_date and t, not yet reflected in shares_out
    df["mktcap"] = df["px"] * shares_out * midfac * df["split_factor_after"]

    fin = df["is_financial"].fillna(False).astype(bool)
    ocf_a = (df["ocf_ttm"] / df["assets"]).where(~fin)  # OCF not economically comparable for banks/insurers
    fcf = ((df["ocf_ttm"] - df["capex_ttm"]) / df["mktcap"]).where(~fin)
    lev = -(df["total_debt"] / df["assets"])
    lev = lev.where(~fin)  # total_debt excludes deposits -> not a meaningful leverage measure for financials
    accr = (-(df["ni_ttm"] - df["ocf_ttm"]) / df["assets"]).where(~fin)  # accruals need a reliable OCF too

    df["q_gpa"] = df["gp_ttm"] / df["assets"]
    df["q_roe"] = df["ni_ttm"] / df[["equity", "equity_1y_ago"]].mean(axis=1)
    df["q_ocfa"] = ocf_a
    df["q_accr"] = accr
    df["q_lev"] = lev
    df["q_agrow"] = -(df["assets"] / df["assets_1y_ago"] - 1)
    df["q_issu"] = -(shares_out / shares_1y - 1)

    df["v_ey"] = df["ni_ttm"] / df["mktcap"]
    df["v_fcfy"] = fcf
    ev = df["mktcap"] + df["total_debt"] - df["cash_sti"]
    df["v_ebitev"] = df["ebit_ttm"] / ev
    df["v_bp"] = df["equity"] / df["mktcap"]

    df["s_sue"] = df["sue"]

    df["sector_grp"] = df["sector"].fillna("Unknown")
    Q_COLS = ["q_gpa", "q_roe", "q_ocfa", "q_accr", "q_lev", "q_agrow", "q_issu"]
    V_COLS = ["v_ey", "v_fcfy", "v_ebitev", "v_bp"]
    # cross-sectional winsorisation at 1st/99th pct per month, on ALL raw ratios incl. momentum/SUE (lead
    # instruction; d3_report.md checks (e): early-XBRL scale errors, IPO/spin-off TTM discontinuities)
    for col in Q_COLS + V_COLS + ["m_mom", "s_sue"]:
        df[col] = c.winsorize_by_month(df, col)
    for col in Q_COLS + V_COLS:
        df[col + "_pr"] = c.sector_neutral_percentile(df, col, "month_end", "sector_grp")
    df["m_mom_pr"] = c.sector_neutral_percentile(df, "m_mom", "month_end", "sector_grp")
    df["s_sue_pr"] = c.sector_neutral_percentile(df, "s_sue", "month_end", "sector_grp")

    df["fam_Q_raw"] = df[[k + "_pr" for k in Q_COLS]].mean(axis=1, skipna=True)
    df["fam_Q_raw"] = df["fam_Q_raw"].where(df[[k + "_pr" for k in Q_COLS]].notna().sum(axis=1) > 0)
    df["fam_V_raw"] = df[[k + "_pr" for k in V_COLS]].mean(axis=1, skipna=True)
    df["fam_V_raw"] = df["fam_V_raw"].where(df[[k + "_pr" for k in V_COLS]].notna().sum(axis=1) > 0)
    df["fam_M_raw"] = df["m_mom_pr"]
    df["fam_S_raw"] = df["s_sue_pr"]

    df["Q"] = c.sector_neutral_percentile(df, "fam_Q_raw", "month_end", "sector_grp")
    df["V"] = c.sector_neutral_percentile(df, "fam_V_raw", "month_end", "sector_grp")
    df["M"] = c.sector_neutral_percentile(df, "fam_M_raw", "month_end", "sector_grp")
    df["S"] = c.sector_neutral_percentile(df, "fam_S_raw", "month_end", "sector_grp")

    fam = df[["Q", "V", "M", "S"]]
    n_avail = fam.notna().sum(axis=1)
    df["n_families"] = n_avail
    df["composite"] = fam.mean(axis=1, skipna=True).where(n_avail >= 3)
    log(f"[{tag}] assembled {len(df)} rows; composite available for {df['composite'].notna().sum()} "
        f"({df['composite'].notna().mean():.1%})")
    return df


panel_full = assemble(mem, "full-PIT-universe")
panel_full.to_parquet(c.DATA / "b1x_panel_full.parquet")

# ---------- bias-check universe: today's 503 constituents, same window, ignoring historical membership ----------
cur = pd.read_csv(c.DATA / "d1_current_constituents.csv")
cur_tickers = sorted(set(cur["ticker_yahoo"]) & tickers_priced)
cur_long = pd.MultiIndex.from_product([ME, cur_tickers], names=["month_end", "ticker"]).to_frame(index=False)
panel_cur = assemble(cur_long, "current-constituents-bias-check")
panel_cur.to_parquet(c.DATA / "b1x_panel_current.parquet")

c.write_json(c.DATA / "b1x_panel_meta.json", {
    "agent": "b1x", "built_utc": pd.Timestamp.now("UTC").isoformat(),
    "membership_source": src,
    "backtest_months": [str(ME[0].date()), str(ME[-1].date())],
    "n_months": int(len(ME)),
    "n_tickers_full_universe": int(mem["ticker"].nunique()),
    "n_current_constituents_used": len(cur_tickers),
    "rows_full": int(len(panel_full)), "rows_current": int(len(panel_cur)),
    "note": "market_cap = d2_close(t) * d3_pit_monthly_lag1.shares_out(t) * split_factor_after(t); "
            "split_factor_after derived by B1X from d2_splits.parquet (product of split_ratio for splits "
            "with date>t), not read from any precomputed column.",
})
log("DONE build")
