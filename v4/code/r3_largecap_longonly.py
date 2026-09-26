"""r3_largecap_longonly.py - Agent R3: how much of the long-short factor premium does a LARGE-CAP LONG-ONLY tilt capture?

Uses Kenneth French size-by-characteristic portfolios (value-weighted within portfolio):
  2x3 sorts (Big = above NYSE median ME; characteristic tercile at NYSE 30/70th pct):  BM, OP, INV, Prior(12-2)
  5x5 sorts (BIG = top NYSE ME quintile; characteristic quintile at NYSE breakpoints): BM, OP, INV, Prior, AC, NI, VAR, BETA
For each characteristic:
  LS_all  = the published all-cap long-short factor (HML/RMW/CMA/UMD) - 2x3 only
  LS_big  = Big favoured portfolio - Big unfavoured portfolio (large-cap long-short)
  LO_big  = Big favoured portfolio - value-weighted Big universe (large-cap LONG-ONLY active return)
Big-universe benchmark = sum_i N_i * AvgCap_i * r_i / sum_i N_i * AvgCap_i over all big-size portfolios of that file
(AvgCap in month t is the beginning-of-month cap: verified - same-month weights track CRSP Mkt with TE 0.5-0.7%/yr
 vs 0.7-1.0% for lagged weights).
Outputs: v4/data/r3_largecap_longonly_monthly.parquet, v4/data/r3_largecap_longonly_stats.csv (+meta), CACHE tables md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from r3_french_lib import CACHE, DATA, FRENCH_FTP, download_french, get_section, parse_french_csv, perf_stats, utc_now, write_meta  # noqa: E402

f = pd.read_parquet(DATA / "r3_ff_factors_monthly.parquet")
mkt = f["mkt_rf_ff3"] + f["rf_ff3"]

# (key, label, zip, favoured col, unfavoured col, big-row prefix(es), ls_all factor)
SPECS = [
    ("value_2x3", "Value (high B/M)", "6_Portfolios_2x3_CSV.zip", "BIG HiBM", "BIG LoBM", ("BIG", "ME2"), "hml"),
    ("prof_2x3", "Profitability (high OP)", "6_Portfolios_ME_OP_2x3_CSV.zip", "BIG HiOP", "BIG LoOP", ("BIG", "ME2"), "rmw"),
    ("inv_2x3", "Conservative investment (low asset growth)", "6_Portfolios_ME_INV_2x3_CSV.zip", "BIG LoINV", "BIG HiINV", ("BIG", "ME2"), "cma"),
    ("mom_2x3", "Momentum (high 12-2 return)", "6_Portfolios_ME_Prior_12_2_CSV.zip", "BIG HiPRIOR", "BIG LoPRIOR", ("BIG", "ME2"), "umd"),
    ("value_5x5", "Value (top B/M quintile)", "25_Portfolios_5x5_CSV.zip", "BIG HiBM", "BIG LoBM", ("BIG", "ME5"), "hml"),
    ("prof_5x5", "Profitability (top OP quintile)", "25_Portfolios_ME_OP_5x5_CSV.zip", "BIG HiOP", "BIG LoOP", ("BIG", "ME5"), "rmw"),
    ("inv_5x5", "Conservative investment (bottom INV quintile)", "25_Portfolios_ME_INV_5x5_CSV.zip", "BIG LoINV", "BIG HiINV", ("BIG", "ME5"), "cma"),
    ("mom_5x5", "Momentum (top 12-2 quintile)", "25_Portfolios_ME_Prior_12_2_CSV.zip", "BIG HiPRIOR", "BIG LoPRIOR", ("BIG", "ME5"), "umd"),
    ("accr_5x5", "Low accruals (bottom AC quintile)", "25_Portfolios_ME_AC_5x5_CSV.zip", "BIG LoAC", "BIG HiAC", ("BIG", "ME5"), None),
    ("nsi_5x5", "Net repurchasers (negative net issuance)", "25_Portfolios_ME_NI_5x5_CSV.zip", "BIG NegNI", "BIG HiNI", ("BIG", "ME5"), None),
    ("lowvar_5x5", "Low variance (bottom 60d VAR quintile)", "25_Portfolios_ME_VAR_5x5_CSV.zip", "BIG LoVAR", "BIG HiVAR", ("BIG", "ME5"), None),
    ("lowbeta_5x5", "Low beta (bottom 60m beta quintile)", "25_Portfolios_ME_BETA_5x5_CSV.zip", "BIG LoBETA", "BIG HiBETA", ("BIG", "ME5"), None),
]

series: dict[str, pd.Series] = {}
nfirms_latest, nfirms_median = {}, {}
for key, label, zname, fav, unf, prefixes, ls in SPECS:
    s = parse_french_csv(download_french(zname))
    vw = get_section(s, r"Value Weighted Returns -- Monthly") / 100.0
    n = get_section(s, r"Number of Firms")
    cap = get_section(s, r"Average (Market Cap|Firm Size)")
    bigcols = [c for c in vw.columns if c.split()[0] in prefixes]
    w = (n[bigcols] * cap[bigcols]).where(vw[bigcols].notna())
    uni = (vw[bigcols] * w).sum(axis=1, min_count=1) / w.sum(axis=1)
    series[f"{key}__fav"] = vw[fav]
    series[f"{key}__universe"] = uni
    series[f"{key}__LO_big"] = vw[fav] - uni
    series[f"{key}__LS_big"] = vw[fav] - vw[unf]
    nfirms_latest[key] = int(n[fav].dropna().iloc[-1])
    nfirms_median[key] = float(n[fav].loc["2010-01-31":].median())

M = pd.DataFrame(series).sort_index()
M.index.name = "month_end"
# multi-factor long-only mixes (equal-weight average of the four single-characteristic active returns)
for tag in ("2x3", "5x5"):
    keys = [f"value_{tag}", f"prof_{tag}", f"inv_{tag}", f"mom_{tag}"]
    M[f"combo4_{tag}__LO_big"] = M[[f"{k}__LO_big" for k in keys]].mean(axis=1, skipna=False)
    M[f"combo4_{tag}__LS_big"] = M[[f"{k}__LS_big" for k in keys]].mean(axis=1, skipna=False)
M["combo4_all__LS_all"] = f[["hml", "rmw", "cma", "umd"]].mean(axis=1, skipna=False)

out_m = DATA / "r3_largecap_longonly_monthly.parquet"
M.to_parquet(out_m)
write_meta(out_m, {
    "source_urls": [FRENCH_FTP + z for _, _, z, *_ in SPECS],
    "rows": len(M), "columns": list(M.columns),
    "units": "decimal monthly returns",
    "definitions": {"__fav": "value-weighted favoured big-cap portfolio return", "__universe": "value-weighted big-cap universe return (all big portfolios of that sort)",
                    "__LO_big": "fav - universe = large-cap long-only active return", "__LS_big": "fav - unfavoured big portfolio",
                    "combo4_*": "equal-weight mix of value, profitability, conservative investment, momentum"},
    "caveats": ["gross of costs and fees; momentum portfolios rebalance monthly (high turnover), others annually each June",
                "value-weighted within portfolio; a 15-30 stock equal-weighted portfolio has more idiosyncratic risk",
                "a 'mix' of four separately sorted portfolios is not the same as an integrated composite ranking",
                f"latest # firms in favoured portfolio: {nfirms_latest}"],
})

windows = {"1963-07..2026-07": "1963-07-31", "2010-01..2026-07": "2010-01-31", "2015-01..2026-07": "2015-01-31"}
rows = []
labels = {k: lab for k, lab, *_ in SPECS}
lsmap = {k: ls for k, *_, ls in SPECS}
for wname, a in windows.items():
    for key in list(labels) + ["combo4_2x3", "combo4_5x5"]:
        lo = M[f"{key}__LO_big"].loc[a:].dropna()
        lsb = M[f"{key}__LS_big"].loc[a:].dropna()
        ls_col = lsmap.get(key) if key in lsmap else "combo4"
        if key.startswith("combo4"):
            lsa = M["combo4_all__LS_all"].loc[a:].dropna()
        elif ls_col:
            lsa = f[ls_col].loc[a:].dropna()
        else:
            lsa = pd.Series(dtype=float)
        st = perf_stats(lo)
        # beta-adjusted alpha of the favoured portfolio vs its big-cap universe (excess of RF), OLS
        if key.startswith("combo4"):
            ks = [f"{k}_{key[-3:]}" for k in ("value", "prof", "inv", "mom")]
            fav_ = M[[f"{k}__fav" for k in ks]].mean(axis=1)
            uni_ = M[[f"{k}__universe" for k in ks]].mean(axis=1)
        else:
            fav_, uni_ = M[f"{key}__fav"], M[f"{key}__universe"]
        reg = pd.concat([fav_ - f["rf"], uni_ - f["rf"]], axis=1, sort=True).loc[a:].dropna()
        X = np.column_stack([np.ones(len(reg)), reg.iloc[:, 1].values])
        coef, *_ = np.linalg.lstsq(X, reg.iloc[:, 0].values, rcond=None)
        resid = reg.iloc[:, 0].values - X @ coef
        se_a = np.sqrt((resid @ resid) / (len(reg) - 2) * np.linalg.inv(X.T @ X)[0, 0])
        rows.append({
            "capm_alpha_ann": coef[0] * 12, "capm_alpha_t": coef[0] / se_a, "beta_vs_universe": coef[1],
            "key": key, "label": labels.get(key, "EW mix: value+profitability+investment+momentum (" + key[-3:] + ")"),
            "window": wname, "n_fav_firms_latest": nfirms_latest.get(key, np.nan), "n_fav_firms_median_2010on": nfirms_median.get(key, np.nan),
            "LO_active_ann_mean": st["ann_mean_arith"], "LO_TE": st["ann_vol"], "LO_IR": st["sharpe_or_ir"], "LO_t": st["t_stat"],
            "LO_pct_calyears_pos": st["pct_calyears_pos"], "LO_pct_roll12_pos": st["pct_roll12_pos"],
            "LO_pct_roll36_pos": st["pct_roll36_pos"], "LO_pct_roll60_pos": st["pct_roll60_pos"],
            "LO_max_rel_drawdown": st["max_drawdown"], "LO_worst_12m": st["worst_12m"],
            "LS_big_ann_mean": lsb.mean() * 12, "LS_all_ann_mean": lsa.mean() * 12 if len(lsa) else np.nan,
            "capture_LO_vs_LS_all": (lo.mean() / lsa.mean()) if len(lsa) and lsa.mean() > 0 else np.nan,
            "capture_LSbig_vs_LS_all": (lsb.mean() / lsa.mean()) if len(lsa) and lsa.mean() > 0 else np.nan,
        })
S = pd.DataFrame(rows)
out_s = DATA / "r3_largecap_longonly_stats.csv"
S.to_csv(out_s, index=False, float_format="%.6f")
write_meta(out_s, {"source": "computed from r3_largecap_longonly_monthly.parquet and r3_ff_factors_monthly.parquet",
                   "rows": len(S), "columns": list(S.columns),
                   "definitions": {"LO_*": "stats of the large-cap long-only active return vs the big-cap VW universe",
                                   "capm_alpha_ann / beta_vs_universe": "OLS of (favoured - RF) on (big universe - RF), monthly, alpha x 12",
                                   "capture_LO_vs_LS_all": "mean(LO_big active) / mean(published all-cap long-short factor); NaN when factor mean <= 0",
                                   "LO_pct_*_pos": "share of calendar years / rolling windows with positive compounded active return (relative wealth)"},
                   "caveats": ["gross of costs; windows after 2010 are short and noisy"]})

# ---- checks
checks = []
u2 = M["value_2x3__universe"].loc["1963-07-31":].dropna()
te = ((u2 - mkt.reindex(u2.index)).std() * np.sqrt(12))
checks.append(("Big-universe (2x3 BM) vs CRSP market TE < 3%/yr (big stocks ~ market)", te < 0.03, f"TE={te:.4f}"))
for key in labels:
    lo = M[f"{key}__LO_big"].loc["1963-07-31":]
    checks.append((f"{key}: no missing months 1963-07..2026-07", lo.isna().sum() == 0, f"missing={int(lo.isna().sum())}, n={len(lo)}"))

def pct(x, d=1):
    return "n/a" if pd.isna(x) else f"{x*100:.{d}f}%"

md = ["## Large-cap long-only capture (French size x characteristic portfolios, value-weighted, gross)\n"]
for wname in windows:
    md.append(f"\n### {wname}\n")
    md.append("| Tilt (large caps) | # firms in favoured pf (latest / median since 2010) | LO active mean | TE | IR | t | Beta | CAPM alpha (t) | % cal. yrs >0 | % roll-36m >0 | % roll-60m >0 | Max rel. DD | LS big | LS all-cap | Capture LO/LS-all |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in S[S.window == wname].iterrows():
        nf = "mix" if pd.isna(r.n_fav_firms_latest) else f"{int(r.n_fav_firms_latest)} / {r.n_fav_firms_median_2010on:.0f}"
        cap_ = "n/a" if pd.isna(r.capture_LO_vs_LS_all) else f"{r.capture_LO_vs_LS_all*100:.0f}%"
        lab = r.label if r.key.startswith("combo4") else f"{r.label} ({r.key[-3:]})"
        md.append(f"| {lab} | {nf} | {pct(r.LO_active_ann_mean,2)} | {pct(r.LO_TE)} | {r.LO_IR:.2f} | {r.LO_t:.2f} | {r.beta_vs_universe:.2f} | "
                  f"{pct(r.capm_alpha_ann,2)} ({r.capm_alpha_t:.2f}) | "
                  f"{pct(r.LO_pct_calyears_pos,0)} | {pct(r.LO_pct_roll36_pos,0)} | {pct(r.LO_pct_roll60_pos,0)} | {pct(r.LO_max_rel_drawdown)} | "
                  f"{pct(r.LS_big_ann_mean)} | {pct(r.LS_all_ann_mean)} | {cap_} |")
md.append("\n### Checks\n")
for n_, ok, d in checks:
    md.append(f"- {'PASS' if ok else 'FAIL'}: {n_} ({d})")
(CACHE / "tables_longonly.md").write_text("\n".join(md), encoding="utf-8")
print("\n".join(md))
print(f"\nchecks {sum(c[1] for c in checks)}/{len(checks)} pass | built {utc_now()}")
