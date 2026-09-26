"""r3_stock_base_rates.py - Agent R3, task 4 (+ realized factor-ETF evidence for task 5).

A) Single-stock and random-portfolio base rates from the legacy price file equity_project/close10.pkl
   (daily closes 2015-09-25..2026-09-24 for ~497 CURRENT S&P 500 members + ^GSPC).
   *** SURVIVORSHIP-BIASED: only stocks that are in the index in Sept 2026 are included, so past winners are
   over-represented and delisted/dropped losers are missing. All beat-rates below are UPPER BOUNDS. ***
   close10 was built with yfinance auto_adjust=True, i.e. stock closes are split- AND dividend-adjusted (verified
   below), while ^GSPC is a price index. We therefore benchmark against ^SP500TR (total return, Yahoo).
B) Realized active returns of live large-cap long-only factor ETFs vs SPY (net of fees, adjusted closes).
Outputs: v4/data/r3_stock_base_rates.csv, r3_random_portfolio_base_rates.csv, r3_random_portfolio_te.csv,
         r3_calendar_year_beat_rates.csv, r3_etf_factor_evidence.csv (+ .meta.json); CACHE/r3/tables_stocks.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from r3_french_lib import CACHE, DATA, PROJECT, perf_stats, rolling_compound, utc_now, write_meta  # noqa: E402

RNG = np.random.default_rng(20260926)
checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + name + (f" - {detail}" if detail else ""))


# ------------------------------------------------------------------ inputs
C = pd.read_pickle(PROJECT / "equity_project" / "close10.pkl")
gspc = C.pop("^GSPC")
etf_path = CACHE / "yf_etf_bench_close_adj.parquet"
TICKERS = ["^SP500TR", "SPY", "RSP", "QUAL", "MTUM", "VLUE", "USMV", "LRGF", "GSLC"]
if not etf_path.exists() or not set(TICKERS) <= set(pd.read_parquet(etf_path).columns):
    import yfinance as yf
    d = yf.download(TICKERS, start="2011-01-01", end="2026-09-26", auto_adjust=True, progress=False, threads=4)["Close"]
    d.to_parquet(etf_path)
E = pd.read_parquet(etf_path)
E.index = pd.to_datetime(E.index)
sptr = E["^SP500TR"].dropna()

# verify dividend adjustment of close10 using MO and T (raw Close vs Adj Close from Yahoo)
raw_path = CACHE / "yf_T_MO_raw_adj.parquet"
if raw_path.exists():
    R = pd.read_parquet(raw_path)
    R.index = pd.to_datetime(R.index)
    for tk in ("MO", "T"):
        c10 = C[tk].dropna()
        d0, d1 = c10.index[0], c10.index[-1]
        g_c10 = c10.loc[d1] / c10.loc[d0]
        g_adj = R[("Adj Close", tk)].loc[d1] / R[("Adj Close", tk)].loc[d0]
        g_raw = R[("Close", tk)].loc[d1] / R[("Close", tk)].loc[d0]
        check(f"close10[{tk}] is dividend-adjusted (growth matches Adj Close, not Close)",
              abs(g_c10 / g_adj - 1) < 0.02 and abs(g_c10 / g_raw - 1) > 0.10,
              f"{d0.date()}->{d1.date()}: close10 x{g_c10:.3f}, AdjClose x{g_adj:.3f}, rawClose x{g_raw:.3f}")

# month-end panels (last trading day of each month); drop the partial last month (Sept 2026 ends 09-24)
me = C.groupby(C.index.to_period("M")).tail(1).index
P = C.loc[me]
P.index = P.index.to_period("M")
B = sptr.groupby(sptr.index.to_period("M")).last().reindex(P.index)
G = gspc.loc[me]
G.index = G.index.to_period("M")
P, B, G = P.iloc[:-1], B.iloc[:-1], G.iloc[:-1]  # last full month = 2026-08
check("benchmark ^SP500TR available for every month-end", B.notna().all(), f"months={len(B)}, {B.index[0]}..{B.index[-1]}")
check("stock universe size", 490 <= P.shape[1] <= 505, f"{P.shape[1]} stocks")

# ------------------------------------------------------------------ A1 single-stock horizon base rates
rows = []
for h_years in (1, 3, 5, 10):
    h = 12 * h_years
    starts = range(0, len(P) - h)
    s_pos, s_beat, s_beat_px, s_medx, s_n, s_ew_beat, s_ew_minus_b, s_mean_x, s_loss50 = [], [], [], [], [], [], [], [], []
    for i in starts:
        p0, p1 = P.iloc[i], P.iloc[i + h]
        ok = p0.notna() & p1.notna()
        r = (p1[ok] / p0[ok] - 1)
        b = B.iloc[i + h] / B.iloc[i] - 1
        g = G.iloc[i + h] / G.iloc[i] - 1
        s_n.append(ok.sum())
        s_pos.append((r > 0).mean())
        s_beat.append((r > b).mean())
        s_beat_px.append((r > g).mean())
        s_medx.append(r.median() - b)
        s_mean_x.append(r.mean() - b)
        s_ew_minus_b.append(r.mean() - b)
        s_loss50.append((r < -0.5).mean())
    nonover = list(range(0, len(P) - h, h))
    rows.append({
        "horizon_years": h_years, "n_start_months": len(list(starts)), "n_nonoverlapping": len(nonover),
        "avg_n_stocks": float(np.mean(s_n)),
        "pct_stocks_positive": float(np.mean(s_pos)),
        "pct_stocks_beat_SP500TR": float(np.mean(s_beat)),
        "pct_beat_SP500TR_min_over_starts": float(np.min(s_beat)), "pct_beat_SP500TR_max_over_starts": float(np.max(s_beat)),
        "pct_stocks_beat_GSPC_price_naive": float(np.mean(s_beat_px)),
        "median_stock_minus_SP500TR": float(np.mean(s_medx)),
        "EW_avg_stock_minus_SP500TR": float(np.mean(s_mean_x)),
        "pct_stocks_lost_50pct_plus": float(np.mean(s_loss50)),
        "pct_beat_SP500TR_nonoverlapping_avg": float(np.mean([s_beat[i] for i in nonover])),
    })
SB = pd.DataFrame(rows)
out1 = DATA / "r3_stock_base_rates.csv"
SB.to_csv(out1, index=False, float_format="%.4f")

# full-period single stock stat (stocks with full history)
full = P.iloc[0].notna() & P.iloc[-1].notna()
r_full = P.iloc[-1][full] / P.iloc[0][full] - 1
b_full = B.iloc[-1] / B.iloc[0] - 1
full_stat = {"period": f"{P.index[0]}..{P.index[-1]}", "n": int(full.sum()), "pct_beat": float((r_full > b_full).mean()),
             "median_stock": float(r_full.median()), "mean_stock": float(r_full.mean()), "SP500TR": float(b_full),
             "top10pct_share_of_total_gain": float(r_full.sort_values(ascending=False).head(int(0.1 * len(r_full))).clip(lower=0).sum() / r_full.clip(lower=0).sum())}
print("full-period:", full_stat)

# ------------------------------------------------------------------ A2 calendar-year beat rates (constituents as of 2026)
cal = []
Pd = C.copy()
for y in range(2016, 2027):
    a_idx = Pd.index[Pd.index.year == y - 1]
    z_idx = Pd.index[Pd.index.year == y]
    if len(a_idx) == 0 or len(z_idx) == 0:
        continue
    a, z = a_idx[-1], z_idx[-1]
    ok = Pd.loc[a].notna() & Pd.loc[z].notna()
    r = Pd.loc[z][ok] / Pd.loc[a][ok] - 1
    b = sptr.loc[:z].iloc[-1] / sptr.loc[:a].iloc[-1] - 1
    cal.append({"year": y if z.month == 12 else f"{y} YTD to {z.date()}", "n_stocks": int(ok.sum()), "SP500TR_return": b,
                "pct_stocks_beat_SP500TR": float((r > b).mean()), "pct_stocks_positive": float((r > 0).mean()),
                "median_stock_return": float(r.median())})
CY = pd.DataFrame(cal)
out_cy = DATA / "r3_calendar_year_beat_rates.csv"
CY.to_csv(out_cy, index=False, float_format="%.4f")

# ------------------------------------------------------------------ A3 random equal-weight portfolios
K = 400
prow = []
for h_years in (1, 3, 5):
    h = 12 * h_years
    for N in (1, 5, 10, 15, 20, 30, 50):
        pos, beat, act = [], [], []
        for i in range(0, len(P) - h, 3):  # quarterly start months to limit overlap/compute
            p0, p1 = P.iloc[i], P.iloc[i + h]
            ok = (p0.notna() & p1.notna()).values
            r = (p1.values[ok] / p0.values[ok] - 1)
            b = B.iloc[i + h] / B.iloc[i] - 1
            idx = np.argsort(RNG.random((K, len(r))), axis=1)[:, :N]
            port = r[idx].mean(axis=1)  # equal-weight buy-and-hold
            pos.append((port > 0).mean())
            beat.append((port > b).mean())
            act.append(np.median(port - b))
        prow.append({"horizon_years": h_years, "n_stocks": N, "draws_per_start": K, "n_starts": len(pos),
                     "P_portfolio_positive": float(np.mean(pos)), "P_portfolio_beats_SP500TR": float(np.mean(beat)),
                     "median_active_cum": float(np.mean(act))})
RP = pd.DataFrame(prow)
out_rp = DATA / "r3_random_portfolio_base_rates.csv"
# (RP is written after the survivorship-bias estimate below, which adds a crude bias-adjusted column)

# tracking error of random EW (monthly rebalanced) portfolios vs SP500TR, full-history stocks only
Rm = P.pct_change(fill_method=None).iloc[1:]
Bm = B.pct_change().iloc[1:]
fullcols = Rm.columns[Rm.notna().all()]
Rf = Rm[fullcols].values
terows = []
for N in (10, 15, 20, 30, 50, 100):
    tes, ars = [], []
    for _ in range(1000):
        cols = RNG.choice(Rf.shape[1], N, replace=False)
        a_ = Rf[:, cols].mean(axis=1) - Bm.values
        tes.append(a_.std(ddof=1) * np.sqrt(12))
        ars.append(a_.mean() * 12)
    terows.append({"n_stocks": N, "draws": 1000, "months": Rf.shape[0], "universe_n": Rf.shape[1],
                   "TE_median": float(np.median(tes)), "TE_p10": float(np.percentile(tes, 10)), "TE_p90": float(np.percentile(tes, 90)),
                   "active_mean_median": float(np.median(ars))})
TE = pd.DataFrame(terows)
out_te = DATA / "r3_random_portfolio_te.csv"
TE.to_csv(out_te, index=False, float_format="%.4f")

# ---- survivorship-bias estimate (needs RSP): EW of today's constituents vs real S&P 500 Equal Weight ETF
_E = E.groupby(E.index.to_period("M")).last().iloc[:-1]
_rsp = _E["RSP"].pct_change(fill_method=None)
_ew = P.pct_change(fill_method=None).mean(axis=1)
_both = pd.concat([_ew, _rsp], axis=1, sort=True).dropna()
BIAS_ANN = (1 + _both.iloc[:, 0]).prod() ** (12 / len(_both)) - (1 + _both.iloc[:, 1]).prod() ** (12 / len(_both))
print(f"survivorship bias (EW survivors - RSP), annualized: {BIAS_ANN:.4f} over {len(_both)} months")
# crude bias adjustment of random-portfolio outcomes: shrink every portfolio's growth by (1+bias)^h
adj = []
for _, r in RP.iterrows():
    h = int(r.horizon_years) * 12
    pb = []
    for i in range(0, len(P) - h, 3):
        p0, p1 = P.iloc[i], P.iloc[i + h]
        ok = (p0.notna() & p1.notna()).values
        rr = (p1.values[ok] / p0.values[ok] - 1)
        b = B.iloc[i + h] / B.iloc[i] - 1
        idx = np.argsort(RNG.random((K, len(rr))), axis=1)[:, : int(r.n_stocks)]
        port = (1 + rr[idx].mean(axis=1)) / (1 + BIAS_ANN) ** (h / 12) - 1
        pb.append((port > b).mean())
    adj.append(float(np.mean(pb)))
RP["P_beats_SP500TR_crude_bias_adj"] = adj
RP["bias_ann_used"] = BIAS_ANN
RP.to_csv(out_rp, index=False, float_format="%.4f")

common_caveats = ["SURVIVORSHIP-BIASED: universe = ~497 stocks in the S&P 500 as of Sept 2026 (legacy close10.pkl); "
                  "stocks that were dropped, acquired or went bankrupt 2015-2026 are missing and later entrants' pre-inclusion "
                  "run-ups are included -> beat-rates and P(positive) are UPPER BOUNDS.",
                  "close10 closes are yfinance auto_adjust=True (dividend-adjusted, verified on MO and T); benchmark ^SP500TR (total return).",
                  "Overlapping windows (monthly starts) -> strongly autocorrelated; one 11-year sample dominated by mega-cap growth leadership.",
                  "Sample 2015-09..2026-08 month-ends."]
for pth, desc in [(out1, "single-stock horizon base rates"), (out_cy, "calendar-year share of 2026 constituents beating SP500TR"),
                  (out_rp, "random equal-weight buy-and-hold portfolio base rates"), (out_te, "tracking error of random EW monthly-rebalanced portfolios")]:
    df_ = pd.read_csv(pth)
    write_meta(pth, {"description": desc, "source_files": [str(PROJECT / "equity_project" / "close10.pkl"), str(etf_path)],
                     "benchmark": "^SP500TR via yfinance (auto_adjust)", "rows": len(df_), "columns": list(df_.columns),
                     "rng_seed": 20260926, "caveats": common_caveats})

# ------------------------------------------------------------------ B realized factor-ETF evidence vs SPY
Em = E.groupby(E.index.to_period("M")).last()
Em = Em.iloc[:-1]  # drop partial Sept 2026
Em.index = Em.index.to_timestamp(how="end").normalize()
Rm_e = Em.pct_change(fill_method=None)
etf_info = {"QUAL": ("iShares MSCI USA Quality Factor", 0.0015), "MTUM": ("iShares MSCI USA Momentum Factor", 0.0015),
            "VLUE": ("iShares MSCI USA Value Factor", 0.0015), "USMV": ("iShares MSCI USA Min Vol Factor", 0.0015),
            "LRGF": ("iShares U.S. Equity Factor (multifactor)", 0.0008), "GSLC": ("Goldman Sachs ActiveBeta U.S. Large Cap (multifactor)", 0.0009)}
erows = []
for tk, (nm, fee) in etf_info.items():
    first = Em[tk].first_valid_index()
    ra = Rm_e[tk].loc[first:].iloc[1:]  # first full month after inception
    rb = Rm_e["SPY"].reindex(ra.index)
    act = (ra - rb).dropna()
    st = perf_stats(act)
    cum_e, cum_b = (1 + ra).prod(), (1 + rb).prod()
    yrs = len(ra) / 12
    X = np.column_stack([np.ones(len(ra)), rb.values])
    coef, *_ = np.linalg.lstsq(X, ra.values, rcond=None)
    erows.append({"ticker": tk, "name": nm, "expense_ratio_approx": fee, "start": str(ra.index[0]), "end": str(ra.index[-1]), "months": len(ra),
                  "ann_return_etf": cum_e ** (1 / yrs) - 1, "ann_return_SPY": cum_b ** (1 / yrs) - 1,
                  "ann_geo_active": cum_e ** (1 / yrs) - cum_b ** (1 / yrs), "ann_arith_active": st["ann_mean_arith"],
                  "TE": st["ann_vol"], "IR": st["sharpe_or_ir"], "beta_vs_SPY": coef[1], "alpha_ann_vs_SPY": coef[0] * 12,
                  "pct_calyears_outperform": st["pct_calyears_pos"], "n_calyears": st["n_calyears"],
                  "pct_roll12_outperform": st["pct_roll12_pos"], "pct_roll36_outperform": st["pct_roll36_pos"],
                  "max_relative_drawdown": st["max_drawdown"]})
# equal-weight mix of QUAL+MTUM+VLUE (monthly rebalanced) from QUAL start
mix = Rm_e[["QUAL", "MTUM", "VLUE"]].loc[Em["QUAL"].first_valid_index():].iloc[1:].mean(axis=1, skipna=False).dropna()
rb = Rm_e["SPY"].reindex(mix.index)
act = mix - rb
st = perf_stats(act)
yrs = len(mix) / 12
erows.append({"ticker": "MIX(QUAL,MTUM,VLUE)", "name": "EW monthly-rebalanced mix of quality, momentum, value ETFs", "expense_ratio_approx": 0.0015,
              "start": str(mix.index[0]), "end": str(mix.index[-1]), "months": len(mix),
              "ann_return_etf": (1 + mix).prod() ** (1 / yrs) - 1, "ann_return_SPY": (1 + rb).prod() ** (1 / yrs) - 1,
              "ann_geo_active": (1 + mix).prod() ** (1 / yrs) - (1 + rb).prod() ** (1 / yrs), "ann_arith_active": st["ann_mean_arith"],
              "TE": st["ann_vol"], "IR": st["sharpe_or_ir"], "pct_calyears_outperform": st["pct_calyears_pos"], "n_calyears": st["n_calyears"],
              "pct_roll12_outperform": st["pct_roll12_pos"], "pct_roll36_outperform": st["pct_roll36_pos"], "max_relative_drawdown": st["max_drawdown"]})
# ---- survivorship-bias estimate: EW of today's constituents (close10) vs the real S&P 500 Equal Weight ETF (RSP)
Pm = P.copy()
Pm.index = Pm.index.to_timestamp(how="end").normalize()
ew_surv = Pm.pct_change(fill_method=None).iloc[1:].mean(axis=1)  # monthly-rebalanced EW of available survivors
rsp = Rm_e["RSP"].reindex(ew_surv.index)
spy = Rm_e["SPY"].reindex(ew_surv.index)
nyr = len(ew_surv) / 12
ann = lambda x: (1 + x).prod() ** (1 / nyr) - 1  # noqa: E731
surv = {"period": f"{ew_surv.index[0].date()}..{ew_surv.index[-1].date()}", "EW_survivors_ann": ann(ew_surv), "RSP_ann": ann(rsp),
        "SPY_ann": ann(spy), "bias_ann_EWsurv_minus_RSP": ann(ew_surv) - ann(rsp), "RSP_minus_SPY_ann": ann(rsp) - ann(spy)}
print("survivorship check:", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in surv.items()})
st = perf_stats((rsp - spy).dropna())
erows.append({"ticker": "RSP", "name": "Invesco S&P 500 Equal Weight (real EW benchmark, reference)", "expense_ratio_approx": 0.0020,
              "start": str(rsp.index[0].date()), "end": str(rsp.index[-1].date()), "months": len(rsp),
              "ann_return_etf": ann(rsp), "ann_return_SPY": ann(spy), "ann_geo_active": ann(rsp) - ann(spy), "ann_arith_active": st["ann_mean_arith"],
              "TE": st["ann_vol"], "IR": st["sharpe_or_ir"], "pct_calyears_outperform": st["pct_calyears_pos"], "n_calyears": st["n_calyears"],
              "pct_roll12_outperform": st["pct_roll12_pos"], "pct_roll36_outperform": st["pct_roll36_pos"], "max_relative_drawdown": st["max_drawdown"]})
EV = pd.DataFrame(erows)
EV["start"] = EV["start"].str[:10]
EV["end"] = EV["end"].str[:10]
pd.DataFrame([surv]).to_csv(DATA / "r3_survivorship_bias_estimate.csv", index=False, float_format="%.4f")
write_meta(DATA / "r3_survivorship_bias_estimate.csv", {
    "description": "Annualized return of a monthly-rebalanced equal-weight portfolio of the ~497 Sept-2026 S&P 500 members (close10.pkl) "
                   "vs the investable S&P 500 Equal Weight ETF (RSP) over the same months. The gap approximates the survivorship/look-ahead "
                   "bias of back-testing on today's constituents (RSP also bears ~0.20% fee and quarterly rather than monthly rebalancing).",
    "rows": 1, "sources": [str(PROJECT / "equity_project" / "close10.pkl"), "Yahoo Finance RSP, SPY (yfinance auto_adjust=True)"]})
out_ev = DATA / "r3_etf_factor_evidence.csv"
EV.to_csv(out_ev, index=False, float_format="%.4f")
write_meta(out_ev, {"description": "Realized monthly total-return performance of live large-cap factor ETFs vs SPY (both net of fees; ETF expense ratios approx.)",
                    "source": "Yahoo Finance via yfinance auto_adjust=True (dividend-adjusted closes), month-end",
                    "rows": len(EV), "columns": list(EV.columns),
                    "caveats": ["Index methodologies differ from academic factors (sector/constraint-neutral, optimized); VLUE is sector-relative value.",
                                "Period 2011/2013/2015..2026-08 is one regime (mega-cap growth leadership); short samples -> wide confidence intervals.",
                                "Expense ratios quoted from memory of issuer pages (approximate); returns already net of them."]})

# ------------------------------------------------------------------ markdown
def pct(x, d=1):
    return "n/a" if pd.isna(x) else f"{x*100:.{d}f}%"


md = ["## Stock-outcome base rates from close10.pkl (SURVIVORSHIP-BIASED upper bounds; 2015-09..2026-08; benchmark ^SP500TR)\n",
      "| Horizon | # start months (non-overlapping) | Avg # stocks | % stocks with return >0 | % stocks beating S&P 500 TR (range across starts) | % beating ^GSPC price (naive, wrong) | Median stock minus index | % losing >50% |",
      "|---|---|---|---|---|---|---|---|"]
for _, r in SB.iterrows():
    md.append(f"| {int(r.horizon_years)}y | {int(r.n_start_months)} ({int(r.n_nonoverlapping)}) | {r.avg_n_stocks:.0f} | {pct(r.pct_stocks_positive)} | "
              f"{pct(r.pct_stocks_beat_SP500TR)} ({pct(r.pct_beat_SP500TR_min_over_starts,0)}-{pct(r.pct_beat_SP500TR_max_over_starts,0)}) | {pct(r.pct_stocks_beat_GSPC_price_naive)} | "
              f"{pct(r.median_stock_minus_SP500TR)} | {pct(r.pct_stocks_lost_50pct_plus)} |")
md.append(f"\nFull period {full_stat['period']}: {full_stat['n']} stocks with full history; {pct(full_stat['pct_beat'])} beat S&P 500 TR "
          f"(index {pct(full_stat['SP500TR'],0)}; median stock {pct(full_stat['median_stock'],0)}; mean stock {pct(full_stat['mean_stock'],0)}; "
          f"top 10% of stocks = {pct(full_stat['top10pct_share_of_total_gain'],0)} of summed gains).\n")
md.append("\n### Calendar-year share of (2026) constituents beating S&P 500 TR\n")
md.append("| Year | # stocks | S&P 500 TR | % beat index | % positive | Median stock |")
md.append("|---|---|---|---|---|---|")
for _, r in CY.iterrows():
    md.append(f"| {r.year} | {int(r.n_stocks)} | {pct(r.SP500TR_return)} | {pct(r.pct_stocks_beat_SP500TR,0)} | {pct(r.pct_stocks_positive,0)} | {pct(r.median_stock_return)} |")
md.append("\n### Random equal-weight buy-and-hold portfolios drawn from the same (biased) universe\n")
md.append(f"| Horizon | # stocks | P(portfolio > 0) | P(portfolio beats S&P 500 TR), biased | Same, crude bias-adjusted (-{BIAS_ANN*100:.1f}%/yr) | Median cumulative active (biased) |")
md.append("|---|---|---|---|---|---|")
for _, r in RP.iterrows():
    md.append(f"| {int(r.horizon_years)}y | {int(r.n_stocks)} | {pct(r.P_portfolio_positive)} | {pct(r.P_portfolio_beats_SP500TR)} | "
              f"{pct(r.P_beats_SP500TR_crude_bias_adj)} | {pct(r.median_active_cum)} |")
md.append("\n### Tracking error of random EW (monthly rebalanced) portfolios vs S&P 500 TR, 2015-10..2026-08\n")
md.append("| # stocks | TE median (p10-p90) | Median annual active return |")
md.append("|---|---|---|")
for _, r in TE.iterrows():
    md.append(f"| {int(r.n_stocks)} | {pct(r.TE_median)} ({pct(r.TE_p10)}-{pct(r.TE_p90)}) | {pct(r.active_mean_median)} |")
md.append("\n### Live large-cap factor ETFs vs SPY (net of fees, monthly total returns)\n")
md.append("| ETF | Period | ETF ann. | SPY ann. | Geo active | TE | IR | Beta | % cal. yrs beat (n) | % roll-36m beat | Max rel. DD |")
md.append("|---|---|---|---|---|---|---|---|---|---|---|")
for _, r in EV.iterrows():
    md.append(f"| {r.ticker} | {r.start}..{r.end} | {pct(r.ann_return_etf)} | {pct(r.ann_return_SPY)} | {pct(r.ann_geo_active,2)} | {pct(r.TE)} | {r.IR:.2f} | "
              f"{'' if pd.isna(r.get('beta_vs_SPY', np.nan)) else f'{r.beta_vs_SPY:.2f}'} | {pct(r.pct_calyears_outperform,0)} ({int(r.n_calyears)}) | {pct(r.pct_roll36_outperform,0)} | {pct(r.max_relative_drawdown)} |")
md.append(f"\nSurvivorship-bias estimate {surv['period']}: EW of today's constituents {pct(surv['EW_survivors_ann'])}/yr vs real S&P 500 Equal Weight ETF (RSP) "
          f"{pct(surv['RSP_ann'])}/yr -> bias ~{pct(surv['bias_ann_EWsurv_minus_RSP'],2)}/yr; RSP vs SPY {pct(surv['RSP_minus_SPY_ann'],2)}/yr.\n")
md.append("\n### Checks\n")
for n_, ok, d in checks:
    md.append(f"- {'PASS' if ok else 'FAIL'}: {n_} ({d})")
(CACHE / "tables_stocks.md").write_text("\n".join(md), encoding="utf-8")
print("\n".join(md))
print(f"checks {sum(c[1] for c in checks)}/{len(checks)} | built {utc_now()}")
