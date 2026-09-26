"""r3_pit_beat_rates.py - Agent R3: point-in-time (PIT) share of S&P 500 members that beat the S&P 500 TR index.

Reads (read-only) agent D2's files: v4/data/d2_universe_spells.csv (membership spells reconstructed from fja05680 +
Wikipedia; D1 owns authoritative membership), d2_ret_monthly.parquet (Yahoo Adj Close monthly returns incl. ^SP500TR),
d2_coverage.csv (reuse_suspect flags).
Method: for each start year Y (members on Y-01-01) and horizon H in {1,3,5} years, compound each member's monthly total
returns Jan Y .. Dec Y+H-1 (buy-and-hold the stock whether or not it stays in the index). If the series ends early
(delisting/acquisition) the proceeds are assumed held in cash (0%) thereafter. Members with no Yahoo data for the first
month are MISSING (mostly acquired/bankrupt names Yahoo no longer serves) -> we report coverage and bounds:
  lower bound = all missing names lost to the index; upper bound = all missing names beat it.
Tickers flagged reuse_suspect by D2 (symbol now points to a different company) are excluded and counted as missing.
Output: v4/data/r3_pit_beat_rates.csv (+meta), CACHE/r3/tables_pit.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from r3_french_lib import CACHE, DATA, utc_now, write_meta  # noqa: E402

spells = pd.read_csv(DATA / "d2_universe_spells.csv", parse_dates=["start", "end_excl"])
R = pd.read_parquet(DATA / "d2_ret_monthly.parquet")
cov = pd.read_csv(DATA / "d2_coverage.csv")
reuse = set(cov.loc[cov["reuse_suspect"] == True, "ticker"])  # noqa: E712
bench = R["^SP500TR"]
d2_mtimes = {p: pd.Timestamp((DATA / p).stat().st_mtime, unit="s").isoformat() for p in
             ("d2_universe_spells.csv", "d2_ret_monthly.parquet", "d2_coverage.csv")}


def members_on(d: pd.Timestamp) -> list[str]:
    m = spells[(spells["start"] <= d) & (spells["end_excl"].isna() | (spells["end_excl"] > d))]
    return sorted(m["ticker"].unique())


rows = []
last_month = R.index.max()
for H in (1, 3, 5):
    for Y in range(2001, 2027):
        start = pd.Timestamp(f"{Y}-01-01")
        months = R.loc[f"{Y}-01-01":f"{Y + H - 1}-12-31"].index
        partial = bool(months.max() < pd.Timestamp(f"{Y + H - 1}-12-01")) if len(months) else True
        if len(months) == 0 or (partial and H > 1):
            continue
        if partial and len(months) < 6:
            continue
        mem = members_on(start)
        b = float((1 + bench.loc[months]).prod() - 1)
        n_mem, n_reuse, n_missing, n_partial = len(mem), 0, 0, 0
        rets = []
        for t in mem:
            if t in reuse:
                n_reuse += 1
                continue
            if t not in R.columns:
                n_missing += 1
                continue
            s = R.loc[months, t]
            if pd.isna(s.iloc[0]):
                n_missing += 1
                continue
            valid = s.notna().values
            last_valid = np.where(valid)[0].max()
            if (~valid[: last_valid + 1]).any():  # interior gap -> treat as missing
                n_missing += 1
                continue
            if last_valid < len(s) - 1:
                n_partial += 1
            rets.append(float((1 + s.iloc[: last_valid + 1]).prod() - 1))
        rets = np.array(rets)
        n_cov = len(rets)
        beat = float((rets > b).mean()) if n_cov else np.nan
        n_beat = int((rets > b).sum())
        n_unknown = n_mem - n_cov
        rows.append({
            "horizon_years": H, "start_year": Y, "months": len(months), "end_month": str(months.max().date()),
            "partial_period": bool(partial), "n_members_start": n_mem, "n_covered": n_cov, "n_missing_no_data": n_missing,
            "n_reuse_excluded": n_reuse, "coverage": n_cov / n_mem, "n_delisted_midway_cash": n_partial,
            "SP500TR_return": b, "pct_beat_covered": beat,
            "pct_beat_lower_bound": n_beat / n_mem, "pct_beat_upper_bound": (n_beat + n_unknown) / n_mem,
            "pct_positive_covered": float((rets > 0).mean()) if n_cov else np.nan,
            "median_member_return": float(np.median(rets)) if n_cov else np.nan,
            "EW_mean_member_return": float(np.mean(rets)) if n_cov else np.nan,
        })
T = pd.DataFrame(rows)
out = DATA / "r3_pit_beat_rates.csv"
T.to_csv(out, index=False, float_format="%.4f")
write_meta(out, {
    "description": "Share of S&P 500 members (point-in-time, on Jan 1 of start year) whose buy-and-hold total return beat ^SP500TR over 1/3/5 years",
    "inputs_read_only": {k: {"path": str(DATA / k), "mtime": v} for k, v in d2_mtimes.items()},
    "rows": len(T), "columns": list(T.columns),
    "caveats": ["Membership reconstructed by D2 from fja05680 GitHub + Wikipedia (not S&P's official file); D1 owns authoritative membership.",
                "Missing names (no Yahoo data) are disproportionately acquired or bankrupt companies; bounds reported. Coverage is lower in early years.",
                "Yahoo Adj Close is dividend-adjusted as of retrieval; delisting returns are not captured (cash assumed after the last full month).",
                "Beat-rate by count (equal-weight), not cap-weight; the index is cap-weighted, so beat-rates < 50% are expected when mega-caps lead.",
                "2026 row is a partial year (Jan-Aug)."],
})

def pct(x, d=0):
    return "n/a" if pd.isna(x) else f"{x*100:.{d}f}%"

md = ["## Point-in-time S&P 500 members beating the S&P 500 TR (D2 membership + Yahoo returns)\n",
      "| Horizon | Start year | Members | Coverage | S&P 500 TR | % beat (covered) | Bounds (all missing lose / win) | % positive | Median member |",
      "|---|---|---|---|---|---|---|---|---|"]
for _, r in T.iterrows():
    yr = f"{r.start_year}" + (" (Jan-Aug)" if r.partial_period else "")
    md.append(f"| {r.horizon_years}y | {yr} | {r.n_members_start} | {pct(r.coverage)} | {pct(r.SP500TR_return,1)} | {pct(r.pct_beat_covered)} | "
              f"{pct(r.pct_beat_lower_bound)}-{pct(r.pct_beat_upper_bound)} | {pct(r.pct_positive_covered)} | {pct(r.median_member_return,1)} |")
summ = (T[~T.partial_period].groupby("horizon_years")
        .agg(n_periods=("start_year", "size"), avg_beat_covered=("pct_beat_covered", "mean"), median_beat=("pct_beat_covered", "median"),
             min_beat=("pct_beat_covered", "min"), max_beat=("pct_beat_covered", "max"), avg_lower=("pct_beat_lower_bound", "mean"),
             avg_upper=("pct_beat_upper_bound", "mean"), avg_cov=("coverage", "mean"), avg_pos=("pct_positive_covered", "mean")))
md.append("\n### Averages across start years (complete periods only)\n")
md.append("| Horizon | # start years | Avg % beat (covered) | Median | Min-Max | Avg bounds | Avg coverage | Avg % positive |")
md.append("|---|---|---|---|---|---|---|---|")
for h, r in summ.iterrows():
    md.append(f"| {h}y | {int(r.n_periods)} | {pct(r.avg_beat_covered,1)} | {pct(r.median_beat,1)} | {pct(r.min_beat)}-{pct(r.max_beat)} | "
              f"{pct(r.avg_lower)}-{pct(r.avg_upper)} | {pct(r.avg_cov)} | {pct(r.avg_pos)} |")
(CACHE / "tables_pit.md").write_text("\n".join(md), encoding="utf-8")
summ.to_csv(CACHE / "pit_summary.csv")
print("\n".join(md))
print("built", utc_now())
