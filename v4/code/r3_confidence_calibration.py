"""r3_confidence_calibration.py - Agent R3, task 5: what can "90% confident" mean? Closed-form calibration tables.

Block A  P(portfolio beats benchmark over T years) for expected active return alpha and tracking error TE, assuming
         iid normal annual active returns:  P = Phi(alpha*sqrt(T)/TE)  (arithmetic approximation).
Block B  Years needed for (i) 90% probability of outperformance, T90 = (1.2816*TE/alpha)^2, and (ii) a t-stat of 2 or 3
         to *detect* the skill statistically, T = (t*TE/alpha)^2.
Block C  Hit rate of a single top-quantile pick: score s and next-period return r are bivariate normal with correlation IC.
         P(r beats the index | s in top q) where the index sits at the p-th percentile of the stock-return cross-section
         (base rate of a random stock beating the index = 1-p, e.g. 0.45-0.50). Computed by numerical integration.
Output: v4/data/r3_confidence_calibration.csv (+meta), CACHE/r3/tables_calibration.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import integrate, stats

sys.path.insert(0, str(Path(__file__).parent))
from r3_french_lib import CACHE, DATA, utc_now, write_meta  # noqa: E402

N = stats.norm
rows = []
# ---- Block A/B
for alpha in (0.005, 0.01, 0.015, 0.02, 0.03):
    for te in (0.03, 0.05, 0.07, 0.09):
        ir = alpha / te
        r = {"block": "A_B", "alpha": alpha, "TE": te, "IR": ir}
        for T in (1, 3, 5, 10, 20):
            r[f"P_outperform_{T}y"] = float(N.cdf(ir * np.sqrt(T)))
        r["years_for_90pct"] = float((N.ppf(0.90) / ir) ** 2)
        r["years_for_t2"] = float((2 / ir) ** 2)
        r["years_for_t3"] = float((3 / ir) ** 2)
        rows.append(r)

# ---- Block C
def p_beat_given_top(ic: float, top_q: float, base_beat: float) -> float:
    """P(r > c | s > z_{1-top_q}); r,s std bivariate normal corr ic; c chosen so P(r > c) = base_beat."""
    c = N.ppf(1 - base_beat)
    z = N.ppf(1 - top_q)
    f = lambda s: N.pdf(s) * N.sf((c - ic * s) / np.sqrt(1 - ic ** 2))  # noqa: E731
    val, _ = integrate.quad(f, z, np.inf)
    return val / top_q


for ic in (0.0, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20):
    for top_q in (0.05, 0.10, 0.20):
        for base in (0.45, 0.50):
            rows.append({"block": "C", "IC": ic, "top_quantile": top_q, "base_rate_random_stock_beats_index": base,
                         "P_pick_beats_index": p_beat_given_top(ic, top_q, base)})
# IC needed for a 90% single-pick hit rate (top decile, base 0.475)
lo, hi = 0.0, 0.999
for _ in range(60):
    mid = (lo + hi) / 2
    if p_beat_given_top(mid, 0.10, 0.475) < 0.90:
        lo = mid
    else:
        hi = mid
ic_needed = hi
rows.append({"block": "C_needed", "top_quantile": 0.10, "base_rate_random_stock_beats_index": 0.475, "IC_needed_for_90pct_hit": ic_needed})

# ---- Block D: Harvey & Liu (2015, JPM "Backtesting") multiple-testing haircut, independent-tests (Sidak) version:
#      t = SR*sqrt(T); p_S two-sided; p_M = 1-(1-p_S)^N; SR_adj = Phi^-1(1-p_M/2)/sqrt(T); haircut = 1 - SR_adj/SR
for sr in (0.3, 0.5, 0.75, 1.0):
    for yrs in (10, 20, 60):
        t_ = sr * np.sqrt(yrs)
        p_s = 2 * N.sf(t_)
        r = {"block": "D", "SR_backtest": sr, "years": yrs, "t_single": t_}
        for n_tests in (10, 100, 316):
            p_m = -np.expm1(n_tests * np.log1p(-p_s))
            sr_adj = N.isf(p_m / 2) / np.sqrt(yrs) if p_m < 1 else 0.0
            r[f"haircut_N{n_tests}"] = float(1 - max(sr_adj, 0) / sr)
        rows.append(r)

T = pd.DataFrame(rows)
out = DATA / "r3_confidence_calibration.csv"
T.to_csv(out, index=False, float_format="%.4f")
write_meta(out, {"description": __doc__.strip().splitlines()[0], "rows": len(T), "columns": list(T.columns),
                 "assumptions": ["normal iid annual active returns (Block A/B); bivariate normal score/return with correlation = IC (Block C)",
                                 "fat tails, regime shifts and alpha decay make real-world probabilities LOWER than these idealized numbers"],
                 "context": "Typical cross-sectional monthly IC of good published signals ~0.02-0.06 (practitioner rule of thumb; see report)."})

def pct(x, d=0):
    return f"{x*100:.{d}f}%"

A = T[T.block == "A_B"]
md = ["## Calibration: probability of beating the benchmark (normal approx.)\n",
      "| Expected alpha | TE | IR | P(beat) 1y | 3y | 5y | 10y | 20y | Years for 90% | Years for t=2 | Years for t=3 |",
      "|---|---|---|---|---|---|---|---|---|---|---|"]
for _, r in A.iterrows():
    md.append(f"| {pct(r.alpha,1)} | {pct(r.TE)} | {r.IR:.2f} | {pct(r.P_outperform_1y)} | {pct(r.P_outperform_3y)} | {pct(r.P_outperform_5y)} | "
              f"{pct(r.P_outperform_10y)} | {pct(r.P_outperform_20y)} | {r.years_for_90pct:.0f} | {r.years_for_t2:.0f} | {r.years_for_t3:.0f} |")
Cb = T[T.block == "C"]
md.append("\n## Single-stock pick: P(top-quantile pick beats the index) vs signal IC\n")
md.append("| IC | Top 5% (base 45%) | Top 10% (base 45%) | Top 20% (base 45%) | Top 5% (base 50%) | Top 10% (base 50%) | Top 20% (base 50%) |")
md.append("|---|---|---|---|---|---|---|")
for ic in sorted(Cb.IC.unique()):
    g = Cb[Cb.IC == ic]
    vals = [g[(g.top_quantile == q) & (g.base_rate_random_stock_beats_index == b)].P_pick_beats_index.iloc[0] for b in (0.45, 0.50) for q in (0.05, 0.10, 0.20)]
    md.append(f"| {ic:.2f} | " + " | ".join(pct(v, 1) for v in vals) + " |")
md.append(f"\nIC needed for a 90% hit rate on a top-decile pick (base rate 47.5%): {ic_needed:.2f}\n")
D = T[T.block == "D"]
md.append("\n## Multiple-testing haircut to a backtested Sharpe ratio (Harvey & Liu 2015 independent-tests version)\n")
md.append("| Backtest SR | Years | t (single test) | Haircut if best of 10 | best of 100 | best of 316 |")
md.append("|---|---|---|---|---|---|")
for _, r in D.iterrows():
    md.append(f"| {r.SR_backtest:.2f} | {int(r.years)} | {r.t_single:.2f} | {pct(r.haircut_N10)} | {pct(r.haircut_N100)} | {pct(r.haircut_N316)} |")
(CACHE / "tables_calibration.md").write_text("\n".join(md), encoding="utf-8")
print("\n".join(md))
print("built", utc_now())
