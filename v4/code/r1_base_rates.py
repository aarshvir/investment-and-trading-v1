"""
r1_base_rates.py  -- agent R1 (capital-market assumptions & regime research)

Computes historical base rates for US large-cap equities (S&P 500) from public data:
  A. Rolling-window return distributions (1/3/5/10y) - Shiller monthly total return (1926+/1950+/1990+),
     cross-checked with ^SP500TR month-end (1990+) and Damodaran calendar-year data (1928+).
  B. Stocks vs T-bills over rolling calendar-year windows (Damodaran, 1928-2025).
  C. Drawdown episodes (all-time-high based) from daily ^GSPC price closes (1928+), ^SP500TR (1988+),
     and Shiller monthly nominal total return (1926+).
  D. Probability of experiencing a >=10/20/30% drawdown / loss-from-entry within a 1y or 5y holding window.
  E. Calendar-year intra-year declines.
  F. Starting CAPE vs subsequent 10y (and 5y) real total returns: regressions, deciles, out-of-sample check.
  G. Realized volatility.

Inputs (raw downloads, cache): C:/Users/user/eqv4/cache/r1/
  shiller_ie_data.xls   (shillerdata.com, file saved 2026-09-02)
  yf_GSPC_daily.csv, yf_SP500TR_daily.csv, yf_VIX_daily.csv (yfinance, through 2026-09-25)
  damodaran_histretSP.xls (NYU Stern, updated 2026-01-01 data through 2025)
Outputs:
  v4/data/r1_base_rates.csv (+ .meta.json)
  v4/data/r1_drawdown_episodes.csv (+ .meta.json)
  v4/data/r1_cape_deciles.csv (+ .meta.json)

Run (Git Bash):  PYTHONPATH='C:\\Users\\user\\eqv4\\pylib' python r1_base_rates.py
"""
import json
import os
import warnings
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import statsmodels.api as sm

warnings.filterwarnings("ignore")

CACHE = r"C:\Users\user\eqv4\cache\r1"
V4 = r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4"
DATA = os.path.join(V4, "data")
os.makedirs(DATA, exist_ok=True)

SPX_CLOSE_2026_09_25 = 7743.41  # given by lead; verified against yfinance ^GSPC
rows = []  # long-format output


def add(section, metric, sample, horizon, statistic, value, unit, n_obs, source):
    rows.append(dict(section=section, metric=metric, sample=sample, horizon=horizon,
                     statistic=statistic, value=(None if value is None or (isinstance(value, float) and np.isnan(value)) else round(float(value), 6)),
                     unit=unit, n_obs=n_obs, source=source))


checks = []  # validation checks (name, passed, detail)


def check(name, cond, detail=""):
    checks.append((name, bool(cond), detail))


# ----------------------------------------------------------------------------------------------
# Load Shiller monthly data
# ----------------------------------------------------------------------------------------------
SRC_SHILLER = "Shiller ie_data.xls via shillerdata.com (file saved 2026-09-02); monthly avg prices"
raw = pd.read_excel(os.path.join(CACHE, "shiller_ie_data.xls"), sheet_name="Data", header=None, skiprows=8)
raw = raw.iloc[:, :22]
raw.columns = ["date", "P", "D", "E", "CPI", "date_frac", "GS10", "RP", "RD", "RTR", "RE", "RTRE",
               "CAPE", "blank1", "TRCAPE", "blank2", "ECY", "bond_ret", "real_bond_ret",
               "r10_stock_real", "r10_bond_real", "r10_excess"]
raw = raw[pd.to_numeric(raw["date"], errors="coerce").notna()].copy()
for c in ["date", "P", "D", "E", "CPI", "GS10", "RTR", "CAPE", "ECY", "TRCAPE"]:
    raw[c] = pd.to_numeric(raw[c], errors="coerce")
yr = np.floor(raw["date"]).astype(int)
mo = np.round((raw["date"] - yr) * 100).astype(int)
raw["month"] = pd.PeriodIndex.from_fields(year=yr.values, month=mo.values, freq="M")
sh = raw.set_index("month").sort_index()
check("shiller_months_monotonic_unique", sh.index.is_unique and sh.index.is_monotonic_increasing,
      f"{sh.index.min()}..{sh.index.max()} n={len(sh)}")
sh["D_ffill"] = sh["D"].ffill()
sh["CPI_ffill"] = sh["CPI"].ffill()
r_nom = (sh["P"] + sh["D_ffill"] / 12.0) / sh["P"].shift(1) - 1.0
sh["TR"] = (1 + r_nom.fillna(0)).cumprod()
sh["RTR_calc"] = sh["TR"] / sh["CPI_ffill"]
# validation: our real TR vs Shiller's RTR column (monthly growth rates should match closely)
g_ours = sh["RTR_calc"].pct_change()
g_shiller = sh["RTR"].pct_change()
diff = (g_ours - g_shiller).abs().loc["1872-01":"2026-06"]
check("real_TR_matches_shiller_column", diff.max() < 1e-6, f"max abs monthly growth diff={diff.max():.2e}")

LAST_FULL = pd.Period("2026-08", "M")  # last month with a full-month average price
shm = sh.loc[:LAST_FULL].copy()

# ----------------------------------------------------------------------------------------------
# A. Rolling-window return distributions (Shiller monthly TR)
# ----------------------------------------------------------------------------------------------
def rolling_stats(tr, real, starts_from, label, source, section="A_rolling_returns"):
    for h in [12, 36, 60, 120]:
        ann_nom = (tr.shift(-h) / tr) ** (12.0 / h) - 1.0
        ann_real = (real.shift(-h) / real) ** (12.0 / h) - 1.0 if real is not None else None
        s = ann_nom.loc[starts_from:].dropna()
        n = len(s)
        hz = f"{h // 12}y"
        add(section, "share_windows_positive_nominal_TR", label, hz, "share", (s > 0).mean(), "fraction", n, source)
        if ann_real is not None:
            sr = ann_real.loc[starts_from:].dropna()
            add(section, "share_windows_positive_real_TR", label, hz, "share", (sr > 0).mean(), "fraction", len(sr), source)
            add(section, "annualized_real_TR", label, hz, "median", sr.median(), "decimal/yr", len(sr), source)
        for q in [0.05, 0.25, 0.5, 0.75, 0.95]:
            add(section, "annualized_nominal_TR", label, hz, f"p{int(q * 100)}", s.quantile(q), "decimal/yr", n, source)
        add(section, "annualized_nominal_TR", label, hz, "min", s.min(), "decimal/yr", n, source)
        add(section, "annualized_nominal_TR", label, hz, "max", s.max(), "decimal/yr", n, source)
        add(section, "annualized_nominal_TR", label, hz, "mean", s.mean(), "decimal/yr", n, source)
        add(section, "share_windows_below_4pct_nominal", label, hz, "share", (s < 0.04).mean(), "fraction", n, source)
        add(section, "share_windows_above_10pct_nominal", label, hz, "share", (s >= 0.10).mean(), "fraction", n, source)


for lbl, start in [("1926+", "1926-01"), ("1950+", "1950-01"), ("1990+", "1990-01")]:
    rolling_stats(shm["TR"], shm["RTR_calc"], start, f"{lbl} (Shiller monthly, starts {start}..end 2026-08)", SRC_SHILLER)

# Cross-check with ^SP500TR month-end closes (exact total return), 1990+
tr_d = pd.read_csv(os.path.join(CACHE, "yf_SP500TR_daily.csv"), index_col=0, parse_dates=True)["Close"].dropna()
tr_me = tr_d.resample("ME").last()
tr_me.index = tr_me.index.to_period("M")
tr_me = tr_me.loc[:LAST_FULL]
rolling_stats(tr_me, None, "1990-01", "1990+ (^SP500TR month-end, starts 1990-01..end 2026-08)",
              "Yahoo Finance ^SP500TR daily closes (retrieved 2026-09-26), month-end", section="A_rolling_returns_xcheck")

# Cross-check: Damodaran calendar-year data
SRC_DAMO = "Damodaran histretSP.xls (NYU Stern; S&P 500 incl. dividends, 3m T-bill; 1928-2025; file dated 2026-01-01)"
dm = pd.read_excel(os.path.join(CACHE, "damodaran_histretSP.xls"), sheet_name="Returns by year", header=None)
dm = dm.iloc[20:, :4].copy()
dm.columns = ["year", "spx", "small", "tbill"]
dm = dm[pd.to_numeric(dm["year"], errors="coerce").notna()].copy()
dm["year"] = dm["year"].astype(int)
dm = dm[(dm["year"] >= 1928) & (dm["year"] <= 2025)].set_index("year")
dm = dm.astype(float)
check("damodaran_years_1928_2025", (dm.index.min() == 1928) and (dm.index.max() == 2025) and len(dm) == 98, f"n={len(dm)}")
spx_idx = (1 + dm["spx"]).cumprod()
tb_idx = (1 + dm["tbill"]).cumprod()
for lbl, y0 in [("1928+", 1928), ("1950+", 1950), ("1990+", 1990)]:
    for n in [1, 3, 5, 10]:
        res_s, res_b = [], []
        for y in range(y0, 2025 - n + 2):
            end = y + n - 1
            s_ret = spx_idx.loc[end] / (spx_idx.loc[y - 1] if y - 1 in spx_idx.index else 1.0)
            b_ret = tb_idx.loc[end] / (tb_idx.loc[y - 1] if y - 1 in tb_idx.index else 1.0)
            res_s.append(s_ret ** (1 / n) - 1)
            res_b.append(b_ret ** (1 / n) - 1)
        res_s, res_b = np.array(res_s), np.array(res_b)
        lab = f"{lbl} calendar-year windows (Damodaran), start years {y0}..{2025 - n + 1}"
        add("B_calendar_windows", "share_windows_positive_nominal_TR", lab, f"{n}y", "share", (res_s > 0).mean(), "fraction", len(res_s), SRC_DAMO)
        add("B_calendar_windows", "share_windows_stocks_beat_tbills", lab, f"{n}y", "share", (res_s > res_b).mean(), "fraction", len(res_s), SRC_DAMO)
        add("B_calendar_windows", "annualized_nominal_TR", lab, f"{n}y", "median", np.median(res_s), "decimal/yr", len(res_s), SRC_DAMO)
for lbl, y0 in [("1928-2025", 1928), ("1950-2025", 1950), ("1990-2025", 1990)]:
    sub = dm.loc[y0:2025]
    g_s = (1 + sub["spx"]).prod() ** (1 / len(sub)) - 1
    g_b = (1 + sub["tbill"]).prod() ** (1 / len(sub)) - 1
    add("B_calendar_windows", "geometric_mean_return_SP500_TR", lbl, "annual", "geo_mean", g_s, "decimal/yr", len(sub), SRC_DAMO)
    add("B_calendar_windows", "geometric_mean_return_3m_Tbill", lbl, "annual", "geo_mean", g_b, "decimal/yr", len(sub), SRC_DAMO)
    add("B_calendar_windows", "stdev_calendar_year_SP500_TR", lbl, "annual", "stdev", sub["spx"].std(ddof=1), "decimal", len(sub), SRC_DAMO)
    add("B_calendar_windows", "share_calendar_years_negative", lbl, "1y", "share", (sub["spx"] < 0).mean(), "fraction", len(sub), SRC_DAMO)

# ----------------------------------------------------------------------------------------------
# C. Drawdown episodes (ATH-based underwater periods)
# ----------------------------------------------------------------------------------------------
def drawdown_episodes(p):
    """p: pd.Series (DatetimeIndex or PeriodIndex), positive values. Returns DataFrame of underwater episodes."""
    vals = p.values.astype(float)
    idx = p.index
    runmax = np.maximum.accumulate(vals)
    out = []
    i = 0
    n = len(vals)
    while i < n:
        if vals[i] < runmax[i]:
            # underwater stretch starts at i; peak is at last index where vals==runmax before i
            start = i
            peak_val = runmax[i]
            j = i
            while j < n and vals[j] < peak_val:
                j += 1
            seg = vals[start:j]
            t_rel = int(np.argmin(seg))
            trough_i = start + t_rel
            peak_i = start - 1
            while peak_i > 0 and vals[peak_i] < peak_val:
                peak_i -= 1
            rec_i = j if j < n else None
            out.append(dict(peak_date=idx[peak_i], peak_value=peak_val, trough_date=idx[trough_i],
                            trough_value=vals[trough_i], depth=vals[trough_i] / peak_val - 1.0,
                            recovery_date=(idx[rec_i] if rec_i is not None else None),
                            recovered=rec_i is not None))
            i = j
        else:
            i += 1
    return pd.DataFrame(out)


def months_between(a, b):
    if a is None or b is None or (isinstance(b, float) and np.isnan(b)):
        return np.nan
    if isinstance(a, pd.Period):
        return (b - a).n
    return (pd.Timestamp(b) - pd.Timestamp(a)).days / 30.4375


gspc = pd.read_csv(os.path.join(CACHE, "yf_GSPC_daily.csv"), index_col=0, parse_dates=True)["Close"].dropna()
check("gspc_last_close_matches_lead", abs(gspc.iloc[-1] - SPX_CLOSE_2026_09_25) < 0.01 and gspc.index[-1] == pd.Timestamp("2026-09-25"),
      f"last={gspc.index[-1].date()} {gspc.iloc[-1]:.2f}")
check("gspc_no_nonpositive", (gspc > 0).all(), "")
rets = gspc.pct_change().dropna()
check("gspc_no_extreme_jumps_except_1987", (rets.abs() > 0.25).sum() <= 1, f"days |ret|>25%: {(rets.abs() > 0.25).sum()}")

ep_px = drawdown_episodes(gspc)
ep_px["series"] = "^GSPC daily close (price only)"
tr_ep = drawdown_episodes(tr_d)
tr_ep["series"] = "^SP500TR daily close (total return)"
sh_tr_ep = drawdown_episodes(shm["TR"].loc["1926-01":])
sh_tr_ep["series"] = "Shiller monthly nominal TR (monthly avg prices; understates depth)"
sh_rtr_ep = drawdown_episodes(shm["RTR_calc"].loc["1926-01":])
sh_rtr_ep["series"] = "Shiller monthly REAL TR (monthly avg prices; understates depth)"

all_eps = []
for e in [ep_px, tr_ep, sh_tr_ep, sh_rtr_ep]:
    e = e.copy()
    e["months_peak_to_trough"] = [months_between(a, b) for a, b in zip(e["peak_date"], e["trough_date"])]
    e["months_trough_to_recovery"] = [months_between(a, b) if r else np.nan for a, b, r in zip(e["trough_date"], e["recovery_date"], e["recovered"])]
    e["months_peak_to_recovery"] = [months_between(a, b) if r else np.nan for a, b, r in zip(e["peak_date"], e["recovery_date"], e["recovered"])]
    all_eps.append(e)
ep_px, tr_ep, sh_tr_ep, sh_rtr_ep = all_eps

END_TS = pd.Timestamp("2026-09-25")


def ep_stats(e, label, sample_start, series_src, end=END_TS):
    if isinstance(e["peak_date"].iloc[0], pd.Period):
        sel = e[e["peak_date"] >= pd.Period(sample_start, "M")]
        yrs = (pd.Period("2026-08", "M") - pd.Period(sample_start, "M")).n / 12.0
    else:
        sel = e[pd.to_datetime(e["peak_date"]) >= pd.Timestamp(sample_start)]
        yrs = (end - pd.Timestamp(sample_start)).days / 365.25
    for thr in [0.10, 0.20, 0.30]:
        s = sel[sel["depth"] <= -thr]
        hz = f">={int(thr * 100)}%"
        add("C_drawdowns", "episode_count", label, hz, "count", len(s), "episodes", len(s), series_src)
        add("C_drawdowns", "episodes_per_decade", label, hz, "rate", len(s) / yrs * 10 if yrs > 0 else np.nan, "per decade", len(s), series_src)
        add("C_drawdowns", "avg_years_between_episodes", label, hz, "mean", yrs / len(s) if len(s) else np.nan, "years", len(s), series_src)
        if len(s):
            add("C_drawdowns", "depth", label, hz, "median", s["depth"].median(), "decimal", len(s), series_src)
            add("C_drawdowns", "depth", label, hz, "mean", s["depth"].mean(), "decimal", len(s), series_src)
            add("C_drawdowns", "months_peak_to_trough", label, hz, "median", s["months_peak_to_trough"].median(), "months", len(s), series_src)
            rec = s[s["recovered"]]
            add("C_drawdowns", "months_trough_to_recovery", label, hz, "median", rec["months_trough_to_recovery"].median(), "months", len(rec), series_src)
            add("C_drawdowns", "months_peak_to_recovery", label, hz, "median", rec["months_peak_to_recovery"].median(), "months", len(rec), series_src)
            add("C_drawdowns", "months_peak_to_recovery", label, hz, "max", rec["months_peak_to_recovery"].max(), "months", len(rec), series_src)
            add("C_drawdowns", "unrecovered_episodes", label, hz, "count", int((~s["recovered"]).sum()), "episodes", len(s), series_src)


for lbl, st in [("peaks 1928+", "1928-01-01"), ("peaks 1950+", "1950-01-01"), ("peaks 1990+", "1990-01-01")]:
    ep_stats(ep_px, f"{lbl} (^GSPC daily price)", st, "Yahoo Finance ^GSPC daily closes 1927-12-30..2026-09-25 (price only)")
ep_stats(tr_ep, "peaks 1990+ (^SP500TR daily total return)", "1990-01-01", "Yahoo Finance ^SP500TR daily closes 1988-01-04..2026-09-25")
ep_stats(sh_tr_ep, "peaks 1926+ (Shiller monthly nominal TR)", "1926-01", SRC_SHILLER)
ep_stats(sh_rtr_ep, "peaks 1926+ (Shiller monthly real TR)", "1926-01", SRC_SHILLER)

# C2. Swing (zigzag) declines: a decline of >= r from the running swing high; it ends when the index rallies >= r
# from the running swing low (symmetric reversal). Captures bear markets nested inside long underwater periods
# (e.g., 1937-38 inside the 1929-54 episode). Time-to-recover = trough -> first close >= that swing high.
def zigzag_declines(p, r):
    v = p.values.astype(float)
    idx = p.index
    n = len(v)
    out = []
    mode = "up"
    hi_i = 0
    lo_i = 0
    for t in range(1, n):
        if mode == "up":
            if v[t] > v[hi_i]:
                hi_i = t
            elif v[t] <= v[hi_i] * (1 - r):
                mode = "down"
                lo_i = t
        else:
            if v[t] < v[lo_i]:
                lo_i = t
            elif v[t] >= v[lo_i] * (1 + r):
                out.append((hi_i, lo_i))
                mode = "up"
                hi_i = t
    if mode == "down":
        out.append((hi_i, lo_i))
    rec = []
    for h_i, l_i in out:
        after = np.nonzero(v[l_i:] >= v[h_i])[0]
        r_i = l_i + after[0] if len(after) else None
        rec.append(dict(peak_date=idx[h_i], peak_value=v[h_i], trough_date=idx[l_i], trough_value=v[l_i], depth=v[l_i] / v[h_i] - 1.0,
                        recovery_date=(idx[r_i] if r_i is not None else None), recovered=r_i is not None,
                        months_peak_to_trough=months_between(idx[h_i], idx[l_i]),
                        months_trough_to_recovery=(months_between(idx[l_i], idx[r_i]) if r_i is not None else np.nan),
                        months_peak_to_recovery=(months_between(idx[h_i], idx[r_i]) if r_i is not None else np.nan)))
    return pd.DataFrame(rec)


zz_all = []
SRC_ZZ = "Yahoo Finance ^GSPC daily closes (price only); zigzag: decline >= r from swing high, ends on >= r rally from swing low"
for r in [0.10, 0.20, 0.30]:
    zz = zigzag_declines(gspc, r)
    zz["threshold"] = r
    zz_all.append(zz)
    for lbl, st in [("swing highs 1928+", "1928-01-01"), ("swing highs 1950+", "1950-01-01"), ("swing highs 1990+", "1990-01-01")]:
        s = zz[pd.to_datetime(zz["peak_date"]) >= pd.Timestamp(st)]
        yrs = (END_TS - pd.Timestamp(st)).days / 365.25
        hz = f">={int(r * 100)}% (zigzag)"
        lab = f"{lbl} (^GSPC daily price)"
        add("C2_swing_declines", "decline_count", lab, hz, "count", len(s), "declines", len(s), SRC_ZZ)
        add("C2_swing_declines", "declines_per_decade", lab, hz, "rate", len(s) / yrs * 10, "per decade", len(s), SRC_ZZ)
        add("C2_swing_declines", "avg_years_between_declines", lab, hz, "mean", yrs / len(s) if len(s) else np.nan, "years", len(s), SRC_ZZ)
        if len(s):
            add("C2_swing_declines", "depth", lab, hz, "median", s["depth"].median(), "decimal", len(s), SRC_ZZ)
            add("C2_swing_declines", "months_peak_to_trough", lab, hz, "median", s["months_peak_to_trough"].median(), "months", len(s), SRC_ZZ)
            rr = s[s["recovered"]]
            add("C2_swing_declines", "months_trough_to_regain_prior_high", lab, hz, "median", rr["months_trough_to_recovery"].median(), "months", len(rr), SRC_ZZ)
            add("C2_swing_declines", "months_peak_to_regain_prior_high", lab, hz, "median", rr["months_peak_to_recovery"].median(), "months", len(rr), SRC_ZZ)
            add("C2_swing_declines", "months_peak_to_regain_prior_high", lab, hz, "max", rr["months_peak_to_recovery"].max(), "months", len(rr), SRC_ZZ)
zz_all = pd.concat(zz_all, ignore_index=True)

# current drawdown status
ath = gspc.max()
ath_date = gspc.idxmax()
add("C_drawdowns", "current_drawdown_from_ATH", "as of 2026-09-25 (^GSPC)", "spot", "value", gspc.iloc[-1] / ath - 1.0, "decimal", 1,
    f"ATH {ath:.2f} on {ath_date.date()}")

# ----------------------------------------------------------------------------------------------
# D. Probability of experiencing a drawdown / loss-from-entry within a holding window (daily ^GSPC)
# ----------------------------------------------------------------------------------------------
def window_dd_probs(p, start, win, step=1):
    p = p.loc[start:]
    v = p.values.astype(float)
    n = len(v)
    starts = np.arange(0, n - win, step)
    mdd = np.empty(len(starts))
    mloss = np.empty(len(starts))
    endret = np.empty(len(starts))
    chunk = 1500
    from numpy.lib.stride_tricks import sliding_window_view
    W = sliding_window_view(v, win + 1)  # rows: start i, cols i..i+win
    for k in range(0, len(starts), chunk):
        rs = starts[k:k + chunk]
        M = W[rs]
        runmax = np.maximum.accumulate(M, axis=1)
        mdd[k:k + chunk] = (M / runmax - 1.0).min(axis=1)
        mloss[k:k + chunk] = (M / M[:, :1] - 1.0).min(axis=1)
        endret[k:k + chunk] = M[:, -1] / M[:, 0] - 1.0
    return mdd, mloss, endret


for start, lbl in [("1928-01-01", "1928+"), ("1950-01-01", "1950+"), ("1990-01-01", "1990+")]:
    for win, hz in [(252, "1y"), (1260, "5y")]:
        mdd, mloss, endret = window_dd_probs(gspc, start, win, step=1)
        lab = f"{lbl} daily starts (^GSPC price only)"
        src = "Yahoo Finance ^GSPC daily closes; window = trading days (252=1y, 1260=5y)"
        for thr in [0.10, 0.20, 0.30]:
            add("D_holding_window_risk", "prob_max_drawdown_within_window_ge", lab, hz, f">={int(thr * 100)}%", (mdd <= -thr).mean(), "fraction", len(mdd), src)
            add("D_holding_window_risk", "prob_price_falls_below_entry_by_ge", lab, hz, f">={int(thr * 100)}%", (mloss <= -thr).mean(), "fraction", len(mloss), src)
        add("D_holding_window_risk", "prob_price_below_entry_at_window_end", lab, hz, "share", (endret < 0).mean(), "fraction", len(endret), src)
        add("D_holding_window_risk", "max_drawdown_within_window", lab, hz, "median", np.median(mdd), "decimal", len(mdd), src)

# ----------------------------------------------------------------------------------------------
# E. Calendar-year intra-year declines (daily price, prior year-end close as starting point)
# ----------------------------------------------------------------------------------------------
intra = []
for y in range(1928, 2026):
    prev = gspc.loc[:f"{y - 1}-12-31"]
    seg = gspc.loc[f"{y}-01-01":f"{y}-12-31"]
    if len(seg) == 0 or len(prev) == 0:
        continue
    v = np.concatenate([[prev.iloc[-1]], seg.values])
    rm = np.maximum.accumulate(v)
    intra.append(dict(year=y, intra_year_decline=(v / rm - 1).min(), year_price_return=v[-1] / v[0] - 1))
intra = pd.DataFrame(intra)
src = "Yahoo Finance ^GSPC daily closes (price only); decline measured from running high within the calendar year"
for lbl, y0 in [("1928-2025", 1928), ("1950-2025", 1950), ("1990-2025", 1990)]:
    s = intra[intra["year"] >= y0]
    add("E_intra_year", "intra_year_max_decline", lbl, "1y", "median", s["intra_year_decline"].median(), "decimal", len(s), src)
    add("E_intra_year", "intra_year_max_decline", lbl, "1y", "mean", s["intra_year_decline"].mean(), "decimal", len(s), src)
    add("E_intra_year", "share_years_with_decline_ge10pct", lbl, "1y", "share", (s["intra_year_decline"] <= -0.10).mean(), "fraction", len(s), src)
    add("E_intra_year", "share_years_with_decline_ge20pct", lbl, "1y", "share", (s["intra_year_decline"] <= -0.20).mean(), "fraction", len(s), src)
    s10 = s[s["intra_year_decline"] <= -0.10]
    add("E_intra_year", "share_of_ge10pct_decline_years_ending_positive", lbl, "1y", "share", (s10["year_price_return"] > 0).mean() if len(s10) else np.nan, "fraction", len(s10), src)
ytd = gspc.loc["2026-01-01":]
v = np.concatenate([[gspc.loc[:"2025-12-31"].iloc[-1]], ytd.values])
add("E_intra_year", "intra_year_max_decline", "2026 YTD through 2026-09-25", "YTD", "value", (v / np.maximum.accumulate(v) - 1).min(), "decimal", len(ytd), src)
add("E_intra_year", "price_return_ytd", "2026 YTD through 2026-09-25", "YTD", "value", v[-1] / v[0] - 1, "decimal", len(ytd), src)

# ----------------------------------------------------------------------------------------------
# F. Starting CAPE vs subsequent real returns
# ----------------------------------------------------------------------------------------------
SRC_CAPE = SRC_SHILLER + "; CAPE = Shiller P/E10; forward returns = real total return (CPI-deflated)"
cape_rows = []
cape_now = float(sh.loc["2026-09", "CAPE"]) * SPX_CLOSE_2026_09_25 / float(sh.loc["2026-09", "P"])
add("F_valuation", "CAPE_estimate_at_2026-09-25", "Shiller Sept-2026 CAPE scaled to 2026-09-25 close", "spot", "value", cape_now, "x", 1,
    SRC_SHILLER + " (Sept P = Sept-1 close 7631.47; scaled by 7743.41/7631.47)")
add("F_valuation", "CAPE_Aug_2026_monthly_avg", "Shiller", "spot", "value", float(sh.loc["2026-08", "CAPE"]), "x", 1, SRC_SHILLER)
cape_hist = sh["CAPE"].loc["1881-01":"2026-08"].dropna()
add("F_valuation", "CAPE_percentile_vs_history_1881_2026", "Shiller", "spot", "percentile", (cape_hist < cape_now).mean(), "fraction", len(cape_hist), SRC_SHILLER)
add("F_valuation", "CAPE_max_1881_2026", "Shiller", "spot", "max", cape_hist.max(), "x", len(cape_hist), f"max month {cape_hist.idxmax()}")
add("F_valuation", "CAPE_median_1881_2026", "Shiller", "spot", "median", cape_hist.median(), "x", len(cape_hist), SRC_SHILLER)
add("F_valuation", "CAPE_median_1990_2026", "Shiller", "spot", "median", cape_hist.loc["1990-01":].median(), "x", len(cape_hist.loc["1990-01":]), SRC_SHILLER)
ecy_latest = sh["ECY"].dropna()
add("F_valuation", "Shiller_excess_CAPE_yield_latest", f"Shiller {ecy_latest.index[-1]}", "spot", "value", float(ecy_latest.iloc[-1]), "decimal", 1, SRC_SHILLER)
pe_trailing = SPX_CLOSE_2026_09_25 / float(sh["E"].dropna().iloc[-1])
add("F_valuation", "trailing_PE_reported_EPS_Shiller", f"price 2026-09-25 / E ({sh['E'].dropna().index[-1]})", "spot", "value", pe_trailing, "x", 1, SRC_SHILLER)

rtr = shm["RTR_calc"]
for h, hz in [(120, "10y"), (60, "5y")]:
    fwd = (rtr.shift(-h) / rtr) ** (12.0 / h) - 1.0
    df = pd.DataFrame({"cape": shm["CAPE"], "fwd": fwd}).loc["1926-01":].dropna()
    df["logcape"] = np.log(df["cape"])
    df["ey"] = 1.0 / df["cape"]
    for xname in ["logcape", "ey"]:
        X = sm.add_constant(df[[xname]])
        m = sm.OLS(df["fwd"], X).fit(cov_type="HAC", cov_kwds={"maxlags": h})
        xnow = np.log(cape_now) if xname == "logcape" else 1.0 / cape_now
        pred = m.params["const"] + m.params[xname] * xnow
        lab = f"starts 1926-01..{df.index[-1]} ({xname})"
        add("F_valuation", "regression_R2", lab, hz, "R2", m.rsquared, "fraction", len(df), SRC_CAPE)
        add("F_valuation", "regression_slope", lab, hz, "coef", m.params[xname], "per unit x", len(df), SRC_CAPE)
        add("F_valuation", "regression_slope_tstat_HAC", lab, hz, "t", m.tvalues[xname], "t", len(df), SRC_CAPE + f"; Newey-West maxlags={h}")
        add("F_valuation", "predicted_real_return_at_current_CAPE", lab, hz, "fitted", pred, "decimal/yr", len(df), SRC_CAPE + f"; CAPE_now={cape_now:.1f}")
        add("F_valuation", "regression_residual_sd", lab, hz, "sd", np.sqrt(m.scale), "decimal/yr", len(df), SRC_CAPE)
    # subsample fits
    for lab0, a, b in [("1950+", "1950-01", None), ("1990+", "1990-01", None)]:
        d2 = df.loc[a:] if b is None else df.loc[a:b]
        X = sm.add_constant(d2[["logcape"]])
        m = sm.OLS(d2["fwd"], X).fit()
        pred = m.params["const"] + m.params["logcape"] * np.log(cape_now)
        add("F_valuation", "regression_R2", f"starts {a}..{d2.index[-1]} (logcape)", hz, "R2", m.rsquared, "fraction", len(d2), SRC_CAPE)
        add("F_valuation", "predicted_real_return_at_current_CAPE", f"starts {a}..{d2.index[-1]} (logcape)", hz, "fitted", pred, "decimal/yr", len(d2), SRC_CAPE)
    # out-of-sample: fit 1926-1989 starts, evaluate 1990+ starts
    tr_ = df.loc[:"1989-12"]
    te_ = df.loc["1990-01":]
    X = sm.add_constant(tr_[["logcape"]])
    m = sm.OLS(tr_["fwd"], X).fit()
    pred_te = m.params["const"] + m.params["logcape"] * te_["logcape"]
    err = te_["fwd"] - pred_te
    add("F_valuation", "out_of_sample_mean_error_realized_minus_fitted", f"fit 1926-1989 starts; test 1990-01..{te_.index[-1]}", hz, "mean", err.mean(), "decimal/yr", len(te_), SRC_CAPE)
    add("F_valuation", "out_of_sample_RMSE", f"fit 1926-1989 starts; test 1990-01..{te_.index[-1]}", hz, "rmse", np.sqrt((err ** 2).mean()), "decimal/yr", len(te_), SRC_CAPE)
    add("F_valuation", "out_of_sample_share_realized_above_fitted", f"fit 1926-1989 starts; test 1990-01..{te_.index[-1]}", hz, "share", (err > 0).mean(), "fraction", len(te_), SRC_CAPE)
    # high-CAPE starts
    for cut in [25, 30, 35]:
        s = df[df["cape"] >= cut]
        if len(s):
            lab = f"starts with CAPE>={cut} (1926-01..{df.index[-1]})"
            add("F_valuation", "subsequent_real_return_when_CAPE_high", lab, hz, "mean", s["fwd"].mean(), "decimal/yr", len(s), SRC_CAPE)
            add("F_valuation", "subsequent_real_return_when_CAPE_high", lab, hz, "min", s["fwd"].min(), "decimal/yr", len(s), SRC_CAPE)
            add("F_valuation", "subsequent_real_return_when_CAPE_high", lab, hz, "max", s["fwd"].max(), "decimal/yr", len(s), SRC_CAPE)
            add("F_valuation", "subsequent_real_return_when_CAPE_high", lab, hz, "share_positive", (s["fwd"] > 0).mean(), "fraction", len(s), SRC_CAPE)
            yrs_ = sorted(set(p.year for p in s.index))
            add("F_valuation", "high_CAPE_start_years_covered", lab, hz, "years", len(yrs_), "count",
                len(s), "years: " + ",".join(str(y) for y in yrs_))
    # nominal forward total returns conditional on high starting CAPE
    trn = shm["TR"]
    fwd_nom = (trn.shift(-h) / trn) ** (12.0 / h) - 1.0
    dn = pd.DataFrame({"cape": shm["CAPE"], "fwd": fwd_nom}).loc["1926-01":].dropna()
    add("F_valuation", "subsequent_nominal_return_all_starts", f"all starts 1926-01..{dn.index[-1]}", hz, "share_positive", (dn["fwd"] > 0).mean(), "fraction", len(dn), SRC_CAPE)
    for cut in [25, 30, 35]:
        s = dn[dn["cape"] >= cut]
        if len(s):
            lab = f"starts with CAPE>={cut} (1926-01..{dn.index[-1]}) NOMINAL"
            add("F_valuation", "subsequent_nominal_return_when_CAPE_high", lab, hz, "mean", s["fwd"].mean(), "decimal/yr", len(s), SRC_CAPE)
            add("F_valuation", "subsequent_nominal_return_when_CAPE_high", lab, hz, "median", s["fwd"].median(), "decimal/yr", len(s), SRC_CAPE)
            add("F_valuation", "subsequent_nominal_return_when_CAPE_high", lab, hz, "min", s["fwd"].min(), "decimal/yr", len(s), SRC_CAPE)
            add("F_valuation", "subsequent_nominal_return_when_CAPE_high", lab, hz, "share_positive", (s["fwd"] > 0).mean(), "fraction", len(s), SRC_CAPE)
    if h == 120:
        df["decile"] = pd.qcut(df["cape"], 10, labels=False) + 1
        for d_, g in df.groupby("decile"):
            cape_rows.append(dict(horizon=hz, decile=int(d_), cape_low=g["cape"].min(), cape_high=g["cape"].max(),
                                  n_months=len(g), avg_real_10y=g["fwd"].mean(), worst_real_10y=g["fwd"].min(),
                                  best_real_10y=g["fwd"].max(), sd_real_10y=g["fwd"].std(ddof=1),
                                  share_positive=(g["fwd"] > 0).mean(), first_start=str(g.index.min()), last_start=str(g.index.max())))

# ----------------------------------------------------------------------------------------------
# G. Volatility
# ----------------------------------------------------------------------------------------------
lr = np.log(gspc).diff().dropna()
for lbl, a in [("1928-2026", "1928-01-01"), ("1950-2026", "1950-01-01"), ("1990-2026", "1990-01-01"),
               ("last 10y to 2026-09-25", "2016-09-26"), ("last 1y to 2026-09-25", "2025-09-26")]:
    s = lr.loc[a:]
    add("G_volatility", "realized_vol_daily_log_returns_annualized", lbl, "1y", "sd*sqrt(252)", s.std(ddof=1) * np.sqrt(252), "decimal", len(s),
        "Yahoo Finance ^GSPC daily closes (price)")
mtr = np.log(tr_me).diff().dropna()
add("G_volatility", "realized_vol_monthly_TR_annualized", "1988-02..2026-08 (^SP500TR month-end)", "1y", "sd*sqrt(12)", mtr.std(ddof=1) * np.sqrt(12), "decimal", len(mtr),
    "Yahoo Finance ^SP500TR month-end")
m12 = (shm["TR"].pct_change(12)).loc["1926-12":].dropna()
add("G_volatility", "sd_rolling_12m_nominal_TR", "1926-2026 (Shiller monthly, overlapping)", "1y", "sd", m12.std(ddof=1), "decimal", len(m12), SRC_SHILLER)
vix = pd.read_csv(os.path.join(CACHE, "yf_VIX_daily.csv"), index_col=0, parse_dates=True)["Close"].dropna()
add("G_volatility", "VIX_close", "2026-09-25", "30d implied", "value", vix.iloc[-1] / 100, "decimal", 1, "Yahoo Finance ^VIX")
add("G_volatility", "VIX_mean", "1990-01-02..2026-09-25", "30d implied", "mean", vix.mean() / 100, "decimal", len(vix), "Yahoo Finance ^VIX")
add("G_volatility", "VIX_median", "1990-01-02..2026-09-25", "30d implied", "median", vix.median() / 100, "decimal", len(vix), "Yahoo Finance ^VIX")

# ----------------------------------------------------------------------------------------------
# Validation checks on outputs
# ----------------------------------------------------------------------------------------------
out = pd.DataFrame(rows)
check("no_duplicate_rows", not out.duplicated(["section", "metric", "sample", "horizon", "statistic"]).any(), "")
shares = out[out["unit"] == "fraction"]["value"].dropna()
check("fractions_in_0_1", ((shares >= 0) & (shares <= 1)).all(), f"n={len(shares)}")
a1 = out[(out.section == "A_rolling_returns") & (out.metric == "share_windows_positive_nominal_TR")]
check("positive_share_increases_with_horizon_1926", a1[a1["sample"].str.startswith("1926+")].sort_values("horizon", key=lambda s: s.str.replace("y", "").astype(int))["value"].is_monotonic_increasing, "")
# cross-check Shiller vs ^SP500TR for 1990+ 1y positive share within 5pp
s1 = out[(out.section == "A_rolling_returns") & (out.metric == "share_windows_positive_nominal_TR") & out["sample"].str.startswith("1990+") & (out.horizon == "1y")]["value"].iloc[0]
s2 = out[(out.section == "A_rolling_returns_xcheck") & (out.metric == "share_windows_positive_nominal_TR") & (out.horizon == "1y")]["value"].iloc[0]
check("shiller_vs_SP500TR_1990_1y_within_5pp", abs(s1 - s2) < 0.05, f"shiller={s1:.3f} sp500tr={s2:.3f}")
# known episodes present
big = ep_px[ep_px["depth"] <= -0.30]
check("known_bear_markets_found", all(any(str(pd.Timestamp(d).year) == str(y) for d in big["peak_date"]) for y in [1929, 1973, 2000, 2007]),
      "peaks: " + ",".join(str(pd.Timestamp(d).date()) for d in big["peak_date"]))
gfc = ep_px[(pd.to_datetime(ep_px["peak_date"]) >= "2007-01-01") & (pd.to_datetime(ep_px["peak_date"]) <= "2007-12-31")]
check("GFC_depth_about_minus_56pct", len(gfc) and abs(gfc["depth"].min() + 0.5678) < 0.01, f"{gfc['depth'].min():.4f}" if len(gfc) else "missing")
zz20 = zz_all[zz_all["threshold"] == 0.20]
zz_years = set(pd.to_datetime(zz20["peak_date"]).dt.year)
check("zigzag20_finds_nested_and_recent_bears", all(y in zz_years for y in [1937, 1946, 1961, 1966, 2020, 2022]),
      f"n={len(zz20)} peak years: {sorted(zz_years)}")
dd1929 = ep_px[(pd.to_datetime(ep_px["peak_date"]).dt.year == 1929)]
check("1929_depth_about_minus_86pct", len(dd1929) and abs(dd1929["depth"].min() + 0.862) < 0.01, f"{dd1929['depth'].min():.4f}" if len(dd1929) else "missing")

# ----------------------------------------------------------------------------------------------
# Write outputs
# ----------------------------------------------------------------------------------------------
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
p_csv = os.path.join(DATA, "r1_base_rates.csv")
out.to_csv(p_csv, index=False)

zz_out = zz_all.copy()
zz_out["series"] = "^GSPC daily price zigzag r=" + (zz_out["threshold"] * 100).round().astype(int).astype(str) + "%"
eps = pd.concat([ep_px, tr_ep, sh_tr_ep, sh_rtr_ep], ignore_index=True)
eps = eps[eps["depth"] <= -0.10].copy()
eps = pd.concat([eps, zz_out.drop(columns=["threshold"])], ignore_index=True)
for c in ["peak_date", "trough_date", "recovery_date"]:
    eps[c] = eps[c].astype(str).str.slice(0, 10).replace({"None": None, "NaT": None})
p_eps = os.path.join(DATA, "r1_drawdown_episodes.csv")
eps[["series", "peak_date", "peak_value", "trough_date", "trough_value", "depth", "recovery_date", "recovered",
     "months_peak_to_trough", "months_trough_to_recovery", "months_peak_to_recovery"]].to_csv(p_eps, index=False)

cape_df = pd.DataFrame(cape_rows)
p_cape = os.path.join(DATA, "r1_cape_deciles.csv")
cape_df.to_csv(p_cape, index=False)

common_sources = {
    "shiller": "https://shillerdata.com/ -> ie_data.xls (https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/70fec4f5-727f-4e53-b5f1-179af109c5fa/ie_data.xls), file saved 2026-09-02",
    "gspc": "Yahoo Finance ^GSPC daily (yfinance 1.7), 1927-12-30..2026-09-25",
    "sp500tr": "Yahoo Finance ^SP500TR daily, 1988-01-04..2026-09-25",
    "vix": "Yahoo Finance ^VIX daily, 1990-01-02..2026-09-25",
    "damodaran": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls (data 1928-2025)",
}
meta = {
    "name": "r1_base_rates", "agent": "r1", "retrieved_utc": now,
    "description": "Long-format table of S&P 500 historical base rates: rolling-window returns, calendar-window stock vs T-bill, "
                   "drawdown episode stats, holding-window drawdown probabilities, intra-year declines, CAPE vs forward returns, volatility.",
    "sources": common_sources, "rows": len(out), "columns": list(out.columns),
    "coverage": "1926-01..2026-09-25 depending on section (see 'sample' column)",
    "caveats": [
        "Shiller prices are monthly averages of daily closes: rolling returns are smoothed and drawdown depths understated vs daily data.",
        "Shiller Jul-Sep 2026 dividends are forward-filled from Jun 2026; Aug/Sep 2026 CPI are Shiller estimates; Sept-2026 price is Sept-1 close.",
        "Overlapping rolling windows are highly autocorrelated: effective independent sample sizes are far smaller than n_obs (e.g., ~9 independent 10y windows since 1926).",
        "^GSPC drawdown statistics are price-only (exclude dividends); total-return recoveries are shorter.",
        "Drawdown episodes are defined between successive all-time highs (underwater periods); nested sell-offs inside a larger episode are not counted separately.",
        "CAPE regressions use overlapping monthly observations; Newey-West HAC t-stats reported; current CAPE (~41) is near the top of the historical range, so fitted values are extrapolations.",
    ],
    "validation_checks": [{"check": n, "passed": p, "detail": d} for n, p, d in checks],
}
json.dump(meta, open(p_csv.replace(".csv", ".meta.json"), "w"), indent=2, default=str)
json.dump({"name": "r1_drawdown_episodes", "agent": "r1", "retrieved_utc": now, "sources": common_sources,
           "rows": len(eps), "columns": list(eps.columns),
           "description": "All underwater episodes (between successive all-time highs) with depth <= -10% for 4 series.",
           "caveats": meta["caveats"][:1] + meta["caveats"][3:5]},
          open(p_eps.replace(".csv", ".meta.json"), "w"), indent=2, default=str)
json.dump({"name": "r1_cape_deciles", "agent": "r1", "retrieved_utc": now, "sources": {"shiller": common_sources["shiller"]},
           "rows": len(cape_df), "columns": list(cape_df.columns),
           "description": "Subsequent 10-year annualized REAL total return of the S&P 500 by decile of starting Shiller CAPE (monthly starts 1926-01..2016-08).",
           "caveats": [meta["caveats"][2]]},
          open(p_cape.replace(".csv", ".meta.json"), "w"), indent=2, default=str)

print(f"rows={len(out)} episodes={len(eps)} cape_deciles={len(cape_df)}")
print(f"CAPE_now={cape_now:.2f}  ATH={ath:.2f} on {ath_date.date()}")
for n, p, d in checks:
    print(("PASS" if p else "FAIL"), n, d)
