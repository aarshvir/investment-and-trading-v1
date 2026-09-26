"""r3_ff_factors.py - Agent R3, task 2: long-sample factor statistics from the Kenneth French Data Library.

Outputs (v4/data):
  r3_ff_factors_monthly.parquet      monthly factors (decimal), FF5 2x3 + UMD + FF3 (1926+)
  r3_factor_stats.csv                mean/vol/Sharpe/t/MDD/rolling hit-rates by factor x window
  r3_factor_pub_decay.csv            in-sample vs post-publication means (McLean-Pontiff style check)
  r3_factor_corr.csv                 factor correlations by window
  r3_market_horizon_base_rates.csv   P(US market total return > 0 / > T-bills / > inflation) over 1-20y windows
Also writes CACHE/r3/tables_factors.md (markdown tables used in the report).
Run: $env:PYTHONPATH='C:\\Users\\user\\eqv4\\pylib'; python v4\\code\\r3_ff_factors.py
"""
from __future__ import annotations

import io
import sys

import numpy as np
import pandas as pd
import requests

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from r3_french_lib import (CACHE, DATA, FRENCH_FTP, FRENCH_HOME, UA, download_french, file_header,  # noqa: E402
                           parse_french_csv, perf_stats, rolling_compound, utc_now, write_meta)

checks: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    checks.append((name, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + name + (f" - {detail}" if detail else ""))


def first_monthly(sections: dict) -> pd.DataFrame:
    for df in sections.values():
        if isinstance(df.index, pd.DatetimeIndex):
            return df
    raise ValueError("no monthly section")


def first_annual(sections: dict) -> pd.DataFrame:
    for df in sections.values():
        if not isinstance(df.index, pd.DatetimeIndex):
            return df
    raise ValueError("no annual section")


# ---------------------------------------------------------------- download + parse
files = {
    "ff5": "F-F_Research_Data_5_Factors_2x3_CSV.zip",
    "mom": "F-F_Momentum_Factor_CSV.zip",
    "ff3": "F-F_Research_Data_Factors_CSV.zip",
}
paths = {k: download_french(v, refresh=True) for k, v in files.items()}
secs = {k: parse_french_csv(p) for k, p in paths.items()}
ff5 = first_monthly(secs["ff5"]) / 100.0
mom = first_monthly(secs["mom"]) / 100.0
ff3 = first_monthly(secs["ff3"]) / 100.0

f = pd.DataFrame(index=ff3.index.union(mom.index).union(ff5.index))
f["mkt_rf"] = ff5["Mkt-RF"]
f["smb"] = ff5["SMB"]
f["hml"] = ff5["HML"]
f["rmw"] = ff5["RMW"]
f["cma"] = ff5["CMA"]
f["rf"] = ff5["RF"]
f["umd"] = mom[mom.columns[0]]
f["mkt_rf_ff3"] = ff3["Mkt-RF"]
f["smb_ff3"] = ff3["SMB"]
f["hml_ff3"] = ff3["HML"]
f["rf_ff3"] = ff3["RF"]
f.index.name = "month_end"
latest = f["hml"].last_valid_index()
print("latest month with FF5 data:", latest.date(), "| UMD latest:", f["umd"].last_valid_index().date())

# ---------------------------------------------------------------- validation
core = f.loc["1963-07-31":latest, ["mkt_rf", "smb", "hml", "rmw", "cma", "rf", "umd"]]
check("no missing FF5+UMD values 1963-07..latest", core.isna().sum().sum() == 0, f"n_missing={int(core.isna().sum().sum())}, months={len(core)}")
d = (f["hml"] - f["hml_ff3"]).abs().dropna()
check("HML(FF5 file) == HML(FF3 file) on overlap", d.max() < 0.00015, f"max abs diff={d.max():.6f} over {len(d)} months")
d2 = (f["mkt_rf"] - f["mkt_rf_ff3"]).abs().dropna()
# French's FF3 and FF5 files report slightly different Mkt-RF in some months (<=8bp); immaterial here.
check("Mkt-RF FF5 vs FF3 files: mean abs diff <0.5bp and max <=10bp", d2.mean() < 0.00005 and d2.max() <= 0.001,
      f"mean abs diff={d2.mean()*1e4:.2f}bp, max={d2.max()*1e4:.1f}bp, months differing>=1bp={(d2 >= 0.00005).sum()}/{len(d2)}")
ann5 = first_annual(secs["ff5"]) / 100.0
rf_comp = (1 + f["rf"].dropna()).groupby(f["rf"].dropna().index.year).prod() - 1
yrs = [y for y in ann5.index if y in rf_comp.index and y < latest.year]
drf = (rf_comp.loc[yrs] - ann5.loc[yrs, "RF"]).abs()
# monthly RF is rounded to 0.01%, so 12 compounded months can differ from the annual figure by up to ~6bp
check("annual RF == compounded monthly RF (<=6bp, 2-decimal rounding)", drf.max() <= 0.0006, f"max abs diff={drf.max()*1e4:.1f}bp over {len(yrs)} yrs")
# Reconstruct each factor from its underlying 2x3 portfolio file (value-weighted returns):
#   X = 1/2(Small Hi + Big Hi) - 1/2(Small Lo + Big Lo)  [CMA: Lo INV minus Hi INV]
recon = [("hml", "6_Portfolios_2x3_CSV.zip", ["SMALL HiBM", "BIG HiBM"], ["SMALL LoBM", "BIG LoBM"]),
         ("rmw", "6_Portfolios_ME_OP_2x3_CSV.zip", ["SMALL HiOP", "BIG HiOP"], ["SMALL LoOP", "BIG LoOP"]),
         ("cma", "6_Portfolios_ME_INV_2x3_CSV.zip", ["SMALL LoINV", "BIG LoINV"], ["SMALL HiINV", "BIG HiINV"]),
         ("umd", "6_Portfolios_ME_Prior_12_2_CSV.zip", ["SMALL HiPRIOR", "BIG HiPRIOR"], ["SMALL LoPRIOR", "BIG LoPRIOR"])]
for fac, zname, longs, shorts in recon:
    vw = first_monthly(parse_french_csv(download_french(zname))) / 100.0
    rec = vw[longs].mean(axis=1) - vw[shorts].mean(axis=1)
    both = pd.concat([rec, f[fac]], axis=1, sort=True).dropna()
    dd = (both.iloc[:, 0] - both.iloc[:, 1]).abs()
    check(f"{fac.upper()} reconstructed from {zname.replace('_CSV.zip','')} (max abs diff <=2bp)", dd.max() <= 0.0002,
          f"max={dd.max()*1e4:.2f}bp, mean={dd.mean()*1e4:.3f}bp, corr={both.corr().iloc[0,1]:.6f}, n={len(both)}")
check("data vintage is 202607 CRSP (latest month 2026-07)", str(latest.date()) == "2026-07-31", file_header(paths["ff5"], 1))

# ---------------------------------------------------------------- save monthly factors
out_f = DATA / "r3_ff_factors_monthly.parquet"
f.to_parquet(out_f)
write_meta(out_f, {
    "source_urls": [FRENCH_HOME] + [FRENCH_FTP + v for v in files.values()],
    "source_vintage": file_header(paths["ff5"], 1),
    "units": "decimal monthly returns (French files are in percent; divided by 100)",
    "rows": len(f), "columns": list(f.columns),
    "coverage": {c: [str(f[c].first_valid_index().date()), str(f[c].last_valid_index().date())] for c in f.columns},
    "definitions": {
        "mkt_rf,smb,hml,rmw,cma,rf": "Fama/French 5 factors (2x3), US, CRSP NYSE/AMEX/NASDAQ; value-weighted long-short",
        "umd": "Momentum factor (Mom): avg(small high, big high prior 2-12 return) - avg(small low, big low); monthly rebalanced",
        "*_ff3": "Fama/French 3-factor file, available from 1926-07 (HML identical to FF5 HML on overlap)",
    },
    "caveats": ["Long-short, all-cap (includes small caps at 50% weight), gross of trading costs and fees, "
                "no shorting constraints; large-cap long-only tilts capture only part of these premia (see r3_largecap_longonly_*).",
                "Factor definitions and back-history are occasionally revised by French (CRSP vintage changes)."],
})

# ---------------------------------------------------------------- stats by window
f["combo4"] = f[["hml", "rmw", "cma", "umd"]].mean(axis=1, skipna=False)  # equal-weight, monthly rebalanced
f["mkt"] = f["mkt_rf"] + f["rf"]
windows = {
    "1963-07..2026-07": ("1963-07-31", latest),
    "2010-01..2026-07": ("2010-01-31", latest),
    "2015-01..2026-07": ("2015-01-31", latest),
}
factor_names = {"hml": "HML (value)", "rmw": "RMW (profitability)", "cma": "CMA (conservative investment)",
                "umd": "UMD (momentum)", "combo4": "EW combo HML+RMW+CMA+UMD", "mkt_rf": "Mkt-RF (equity premium, ref.)",
                "smb": "SMB (size, ref.)"}
rows = []
for wname, (a, b) in windows.items():
    for col, label in factor_names.items():
        s = perf_stats(f.loc[a:b, col])
        rows.append({"factor": col, "label": label, "window": wname, **s})
# long history for the two factors that have it
for col, label, a in [("hml_ff3", "HML (value, FF3 file)", "1926-07-31"), ("umd", "UMD (momentum)", "1927-01-31"),
                      ("mkt_rf_ff3", "Mkt-RF (FF3 file)", "1926-07-31")]:
    s = perf_stats(f.loc[a:latest, col])
    rows.append({"factor": col, "label": label, "window": f"{a[:7]}..2026-07", **s})
stats = pd.DataFrame(rows)
out_s = DATA / "r3_factor_stats.csv"
stats.to_csv(out_s, index=False, float_format="%.6f")
write_meta(out_s, {
    "source": "computed from r3_ff_factors_monthly.parquet", "rows": len(stats), "columns": list(stats.columns),
    "definitions": {
        "ann_mean_arith": "12 x mean monthly return", "ann_vol": "sqrt(12) x monthly std (ddof=1)",
        "sharpe_or_ir": "ann_mean_arith / ann_vol (factors are zero-cost long-short, so no RF deduction)",
        "t_stat": "mean / (std/sqrt(n)), iid", "max_drawdown": "of cumulative prod(1+r) starting at 1.0",
        "pct_roll12_pos / 36 / 60": "share of overlapping rolling windows with compounded return > 0",
        "pct_calyears_pos": "share of complete calendar years with compounded return > 0",
        "combo4": "equal-weight (monthly rebalanced) average of HML, RMW, CMA, UMD",
    },
    "caveats": ["gross of costs; long-short; all-cap; overlapping windows are highly autocorrelated (effective N small)"],
})

# ---------------------------------------------------------------- publication decay check (our own data)
pubs = [
    # factor, paper, in-sample start, in-sample end, publication month
    ("hml_ff3", "Fama & French (1992, JF) value; sample 1963-07..1990-12", "1963-07-31", "1990-12-31", "1992-06-30"),
    ("umd", "Jegadeesh & Titman (1993, JF) momentum; sample 1965..1989", "1965-01-31", "1989-12-31", "1993-03-31"),
    ("rmw", "Fama & French (2015, JFE) RMW; sample 1963-07..2013-12", "1963-07-31", "2013-12-31", "2015-04-30"),
    ("cma", "Fama & French (2015, JFE) CMA; sample 1963-07..2013-12", "1963-07-31", "2013-12-31", "2015-04-30"),
    ("cma", "Cooper, Gulen & Schill (2008, JF) asset growth; sample 1968..2003", "1968-01-31", "2003-12-31", "2008-08-31"),
]
prow = []
for col, paper, a, b, pub in pubs:
    ins = f.loc[a:b, col].dropna()
    oos = f.loc[pd.Timestamp(b) + pd.offsets.MonthEnd(1):latest, col].dropna()
    post = f.loc[pd.Timestamp(pub) + pd.offsets.MonthEnd(1):latest, col].dropna()

    def _t(x):
        return x.mean() / (x.std(ddof=1) / np.sqrt(len(x)))
    prow.append({
        "factor": col, "paper_sample": paper, "insample": f"{a[:7]}..{b[:7]}", "pub_month": pub[:7],
        "ann_mean_insample": ins.mean() * 12, "t_insample": _t(ins), "n_insample": len(ins),
        "ann_mean_post_sample": oos.mean() * 12, "t_post_sample": _t(oos), "n_post_sample": len(oos),
        "ann_mean_post_pub": post.mean() * 12, "t_post_pub": _t(post), "n_post_pub": len(post),
        "post_pub_change_pct": (post.mean() / ins.mean() - 1) * 100,
        "sharpe_insample": ins.mean() / ins.std() * np.sqrt(12), "sharpe_post_pub": post.mean() / post.std() * np.sqrt(12),
    })
pdec = pd.DataFrame(prow)
out_p = DATA / "r3_factor_pub_decay.csv"
pdec.to_csv(out_p, index=False, float_format="%.6f")
write_meta(out_p, {"source": "computed from r3_ff_factors_monthly.parquet", "rows": len(pdec),
                   "note": "French's factor definitions are not identical to each paper's original variable "
                           "(e.g. RMW uses operating profitability, not Novy-Marx gross profitability; CMA != CGS total asset growth decile spread). "
                           "In-sample periods are the papers' reported sample periods; post_pub starts the month after journal publication.",
                   "caveats": ["means over short post-publication windows have large standard errors (t-stats reported)"]})

# ---------------------------------------------------------------- correlations
crow = []
for wname, (a, b) in windows.items():
    c = f.loc[a:b, ["mkt_rf", "hml", "rmw", "cma", "umd"]].corr()
    c.insert(0, "window", wname)
    crow.append(c.reset_index().rename(columns={"index": "factor"}))
corr = pd.concat(crow, ignore_index=True)
out_c = DATA / "r3_factor_corr.csv"
corr.to_csv(out_c, index=False, float_format="%.4f")
write_meta(out_c, {"source": "computed from r3_ff_factors_monthly.parquet", "rows": len(corr), "method": "Pearson on monthly returns"})

# ---------------------------------------------------------------- market horizon base rates (US total market, 1926+)
cpi = None
try:
    rc = requests.get("https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCNS", headers=UA, timeout=60)
    rc.raise_for_status()
    (CACHE / "fred_CPIAUCNS.csv").write_bytes(rc.content)
    cp = pd.read_csv(io.BytesIO(rc.content))
    cp.columns = ["date", "cpi"]
    cp["date"] = pd.to_datetime(cp["date"]) + pd.offsets.MonthEnd(0)
    cpi = cp.set_index("date")["cpi"].astype(float)
except Exception as e:  # noqa: BLE001
    print("CPI download failed:", e)
mkt_tot = (f["mkt_rf_ff3"] + f["rf_ff3"]).dropna()
rf_all = f["rf_ff3"].dropna()
infl = cpi.pct_change().reindex(mkt_tot.index) if cpi is not None else None
hrows = []
for yrs_ in [1, 3, 5, 10, 15, 20]:
    w = 12 * yrs_
    rm = rolling_compound(mkt_tot, w).dropna()
    rr = rolling_compound(rf_all, w).reindex(rm.index)
    row = {"horizon_years": yrs_, "window_months": w, "n_windows": len(rm), "first_window_end": str(rm.index[0].date()),
           "pct_nominal_pos": float((rm > 0).mean()), "pct_beat_tbills": float((rm > rr).mean()),
           "worst_cum_nominal": float(rm.min()), "median_ann_nominal": float(((1 + rm) ** (1 / yrs_) - 1).median())}
    if infl is not None:
        ri = rolling_compound(infl.dropna(), w).reindex(rm.index)
        ok = ri.notna()
        row.update({"pct_real_pos": float((rm[ok] > ri[ok]).mean()), "n_windows_real": int(ok.sum()),
                    "worst_cum_real": float(((1 + rm[ok]) / (1 + ri[ok]) - 1).min())})
    hrows.append(row)
hz = pd.DataFrame(hrows)
out_h = DATA / "r3_market_horizon_base_rates.csv"
hz.to_csv(out_h, index=False, float_format="%.4f")
write_meta(out_h, {"source_urls": [FRENCH_FTP + files["ff3"], "https://fred.stlouisfed.org/series/CPIAUCNS"],
                   "rows": len(hz), "sample": f"1926-07..{latest.date()} monthly, overlapping rolling windows",
                   "definition": "US value-weighted CRSP market total return (Mkt-RF + RF); real = relative to CPI-U NSA",
                   "caveats": ["Overlapping windows: effective independent observations ~ sample years / horizon "
                               "(e.g. only ~10 non-overlapping 10-year periods since 1926).",
                               "US market is a survivor (ex-post the most successful large market); "
                               "global evidence (e.g. Japan 1990-2020) shows longer losing spells."]})

# ---------------------------------------------------------------- markdown tables for the report
def pct(x, d=1):
    return "n/a" if pd.isna(x) else f"{x*100:.{d}f}%"


md = ["## Factor statistics (long-short, gross, all-cap; Kenneth French Data Library, CRSP vintage 202607)\n"]
for wname in list(windows) + ["long"]:
    sub = stats[stats.window == wname] if wname != "long" else stats[~stats.window.isin(list(windows))]
    md.append(f"\n### Window {wname if wname != 'long' else 'full history (1926/27..2026-07)'}\n")
    md.append("| Factor | Ann. mean | Vol | Sharpe | t-stat | Max DD (peak->trough) | % mo >0 | % roll-12m >0 | % roll-36m >0 | % cal. yrs >0 | Worst 12m |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in sub.iterrows():
        md.append(f"| {r.label} | {pct(r.ann_mean_arith)} | {pct(r.ann_vol)} | {r.sharpe_or_ir:.2f} | {r.t_stat:.2f} | "
                  f"{pct(r.max_drawdown)} ({r.mdd_peak[:7]}->{r.mdd_trough[:7]}) | {pct(r.pct_months_pos,0)} | "
                  f"{pct(r.pct_roll12_pos,0)} | {pct(r.pct_roll36_pos,0)} | {pct(r.pct_calyears_pos,0)} (n={r.n_calyears}) | {pct(r.worst_12m)} |")
md.append("\n### Publication-decay check on French factors\n")
md.append("| Factor / paper | In-sample mean (t) | Post-sample mean (t) | Post-publication mean (t), n months | Change vs in-sample |")
md.append("|---|---|---|---|---|")
for _, r in pdec.iterrows():
    md.append(f"| {r.paper_sample} | {pct(r.ann_mean_insample)} ({r.t_insample:.2f}) | {pct(r.ann_mean_post_sample)} ({r.t_post_sample:.2f}) | "
              f"{pct(r.ann_mean_post_pub)} ({r.t_post_pub:.2f}), {r.n_post_pub} | {r.post_pub_change_pct:+.0f}% |")
md.append("\n### Correlations\n")
for wname in windows:
    c = corr[corr.window == wname].set_index("factor").drop(columns="window")
    md.append(f"\n{wname}\n")
    md.append("| | " + " | ".join(c.columns) + " |")
    md.append("|---" * (len(c.columns) + 1) + "|")
    for i, r in c.iterrows():
        md.append(f"| {i} | " + " | ".join(f"{v:.2f}" for v in r.values) + " |")
md.append("\n### US total market: share of rolling windows with positive outcomes (1926-07..latest)\n")
md.append("| Horizon | # windows | P(nominal > 0) | P(beat T-bills) | P(real > 0) | Worst cumulative nominal | Worst cumulative real | Median annualized nominal |")
md.append("|---|---|---|---|---|---|---|---|")
for _, r in hz.iterrows():
    md.append(f"| {int(r.horizon_years)}y | {int(r.n_windows)} | {pct(r.pct_nominal_pos)} | {pct(r.pct_beat_tbills)} | "
              f"{pct(r.get('pct_real_pos', np.nan))} | {pct(r.worst_cum_nominal)} | {pct(r.get('worst_cum_real', np.nan))} | {pct(r.median_ann_nominal)} |")
md.append("\n### Validation checks\n")
for n_, ok, det in checks:
    md.append(f"- {'PASS' if ok else 'FAIL'}: {n_} ({det})")
(CACHE / "tables_factors.md").write_text("\n".join(md), encoding="utf-8")
print("\n".join(md))
print(f"\nchecks: {sum(ok for _, ok, _ in checks)}/{len(checks)} pass | built {utc_now()}")
