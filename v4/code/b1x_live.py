"""b1x_live.py - Agent B1X: live composite scores for current S&P 500 constituents as of 2026-09-25 (task 3g).
Mirrors the exact metric formulas in b1x_build.py's assemble() for consistency, using D3's NON-lag panel
(filed<=t; appropriate for a "as of today" live snapshot, vs the extra-conservative lag1 used for backtests).
Writes v4/data/b1x_live_scores.parquet.
"""
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\code")
import b1x_common as c

LIVE = pd.Timestamp(c.LIVE_DATE)

full_idx = pd.read_parquet(c.DATA / "d2_adjclose.parquet", columns=["SPY"]).index
FULL_ME = pd.DatetimeIndex(sorted(full_idx.to_series().groupby(full_idx.to_period("M")).max().values))
assert FULL_ME[-1] == LIVE, f"expected last full month-end grid point = live date, got {FULL_ME[-1]}"
t_minus1, t_minus12 = FULL_ME[-2], FULL_ME[-13]  # P(t-1)/P(t-12)-1, t itself = live date

close = pd.read_parquet(c.DATA / "d2_close.parquet")
adjclose = pd.read_parquet(c.DATA / "d2_adjclose.parquet")
splits = pd.read_parquet(c.DATA / "d2_splits.parquet")

cur = pd.read_csv(c.DATA / "d1_current_constituents.csv")
tickers = [t for t in cur["ticker_yahoo"] if t in close.columns]
px = close.loc[LIVE, tickers]
mom = (adjclose.loc[t_minus1, tickers] / adjclose.loc[t_minus12, tickers] - 1)

fund = pd.read_parquet(c.DATA / "d3_pit_monthly.parquet")  # filed<=t: best available "as of today" info
fund = fund[fund["month_end"] == LIVE]
FUND_COLS = ["cik", "gp_ttm", "ni_ttm", "ocf_ttm", "capex_ttm", "assets", "assets_1y_ago",
             "equity", "equity_1y_ago", "total_debt", "cash_sti", "shares_out", "shares_1y_ago",
             "shares_out_date", "ebit_ttm", "sue", "is_financial"]
fund = fund[["ticker"] + FUND_COLS]

df = pd.DataFrame({"ticker": tickers, "px": px.values, "m_mom": mom.values})
df = df.merge(fund, on="ticker", how="left")
sec_map = c.sic_sector_map()
df = df.merge(sec_map, left_on="cik", right_index=True, how="left")
df["sector_grp"] = df["sector"].fillna("Unknown")

# splits between shares_out_date and the live date (same logic as b1x_build.midwindow_split_factor)
_splits_sorted = {tkr: (g.sort_values("date")["date"].values, g.sort_values("date")["split_ratio"].values)
                  for tkr, g in splits[splits["ticker"].isin(tickers)].groupby("ticker")}
midfac = np.ones(len(df))
so_date = df["shares_out_date"].values
for tkr, idx in df.groupby("ticker").indices.items():
    if tkr not in _splits_sorted:
        continue
    idx = np.asarray([i for i in idx if not pd.isna(so_date[i])])
    if len(idx) == 0:
        continue
    dates, ratios = _splits_sorted[tkr]
    prefix = np.concatenate([[1.0], np.cumprod(ratios)])
    lo = np.searchsorted(dates, so_date[idx], side="right")
    hi = np.searchsorted(dates, np.full(len(idx), LIVE.to_datetime64()), side="right")
    midfac[idx] = prefix[hi] / prefix[lo]

is_brkb = df["ticker"].eq("BRK-B")
shares_out = df["shares_out"].where(~is_brkb, df["shares_out"] * c.BRK_B_CLASS_CONVERSION)
shares_1y = df["shares_1y_ago"].where(~is_brkb, df["shares_1y_ago"] * c.BRK_B_CLASS_CONVERSION)
df["mktcap"] = df["px"] * shares_out * midfac  # no split_factor_after term: live date IS the data cutoff

fin = df["is_financial"].fillna(False).astype(bool)
ocf_a = (df["ocf_ttm"] / df["assets"]).where(~fin)
fcf = ((df["ocf_ttm"] - df["capex_ttm"]) / df["mktcap"]).where(~fin)
lev = (-(df["total_debt"] / df["assets"])).where(~fin)
accr = (-(df["ni_ttm"] - df["ocf_ttm"]) / df["assets"]).where(~fin)

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

Q_COLS = ["q_gpa", "q_roe", "q_ocfa", "q_accr", "q_lev", "q_agrow", "q_issu"]
V_COLS = ["v_ey", "v_fcfy", "v_ebitev", "v_bp"]
df["_one"] = 1  # single cross-section -> winsorize/rank "by month" collapses to a global group
for col in Q_COLS + V_COLS + ["m_mom", "s_sue"]:
    df[col] = c.winsorize_by_month(df, col, month_col="_one")
for col in Q_COLS + V_COLS:
    df[col + "_pr"] = c.sector_neutral_percentile(df, col, "_one", "sector_grp")
df["m_mom_pr"] = c.sector_neutral_percentile(df, "m_mom", "_one", "sector_grp")
df["s_sue_pr"] = c.sector_neutral_percentile(df, "s_sue", "_one", "sector_grp")

df["fam_Q_raw"] = df[[k + "_pr" for k in Q_COLS]].mean(axis=1, skipna=True)
df["fam_V_raw"] = df[[k + "_pr" for k in V_COLS]].mean(axis=1, skipna=True)
df["fam_M_raw"] = df["m_mom_pr"]
df["fam_S_raw"] = df["s_sue_pr"]

df["Q"] = c.sector_neutral_percentile(df, "fam_Q_raw", "_one", "sector_grp")
df["V"] = c.sector_neutral_percentile(df, "fam_V_raw", "_one", "sector_grp")
df["M"] = c.sector_neutral_percentile(df, "fam_M_raw", "_one", "sector_grp")
df["S"] = c.sector_neutral_percentile(df, "fam_S_raw", "_one", "sector_grp")

fam = df[["Q", "V", "M", "S"]]
n_avail = fam.notna().sum(axis=1)
df["n_families"] = n_avail
df["composite"] = fam.mean(axis=1, skipna=True).where(n_avail >= 3)
df["live_date"] = LIVE

out_cols = ["ticker", "live_date", "sector_grp", "mktcap", "Q", "V", "M", "S", "n_families", "composite"] + \
    [k for k in Q_COLS + V_COLS] + ["m_mom", "s_sue"]
result = df[out_cols].sort_values("composite", ascending=False)
result.to_parquet(c.DATA / "b1x_live_scores.parquet")
c.write_json(c.DATA / "b1x_live_scores.meta.json", {
    "agent": "b1x", "as_of": c.LIVE_DATE, "rows": int(len(result)),
    "composite_available": int(result["composite"].notna().sum()),
    "source": "d3_pit_monthly.parquet (filed<=t, non-lag) for live 'as of today' use; d2_close/d2_adjclose for "
              "price/momentum; sector via D1's sic_to_sector() on D3 company_meta SIC codes.",
})
print(result.head(20).to_string())
print("composite available:", result["composite"].notna().sum(), "/", len(result))
