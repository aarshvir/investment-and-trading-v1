"""Read-only comparison of archived B1 split-basis choices against a causal median.

This is a diagnostic, not a replacement backtest. The original parquet and code are
read only; output is written next to this script.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PANEL = ROOT / "v4/data/b1_panel.parquet"
SPLITS = ROOT / "v4/data/d2_splits.parquet"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    cols = ["month_end", "entity", "series", "shares_out", "shares_out_date",
            "split_factor_after", "mktcap_split_fix", "px_actual", "mktcap", "sector",
            "in_universe", "composite", "ep", "fcfp", "bp", "ebit_ev"]
    p = pd.read_parquet(PANEL, columns=cols).sort_values(["entity", "month_end"], kind="stable")
    s = pd.read_parquet(SPLITS)
    s["date"] = pd.to_datetime(s["date"])
    groups = {k: v.sort_values("date") for k, v in s.groupby("ticker")}
    n = len(p)
    mult_b = np.ones(n)
    amb = np.zeros(n, dtype=bool)
    for k, (series, sh_date, asof) in enumerate(zip(p["series"], p["shares_out_date"], p["month_end"])):
        if pd.isna(series) or pd.isna(sh_date) or series not in groups:
            continue
        g = groups[series]
        hit = g[(g.date > pd.Timestamp(sh_date)) & (g.date <= asof)]
        if len(hit):
            amb[k] = True
            mult_b[k] = float(hit.split_ratio.prod())
    sh_a = p.shares_out * p.split_factor_after
    sh_b = p.shares_out * mult_b * p.split_factor_after
    ref_source = sh_a.where(~amb)
    grp = p.entity
    legacy = ref_source.groupby(grp).transform(lambda x: x.rolling(13, center=True, min_periods=1).median())
    legacy = legacy.groupby(grp).transform(lambda x: x.ffill().bfill())
    causal = ref_source.groupby(grp).transform(lambda x: x.rolling(13, min_periods=1).median())
    causal = causal.groupby(grp).ffill()
    use_old = amb & (np.log(sh_b / legacy).abs() < np.log(sh_a / legacy).abs())
    use_new = amb & (np.log(sh_b / causal).abs() < np.log(sh_a / causal).abs())
    old_saved = p.mktcap_split_fix.fillna(False).astype(bool).to_numpy()
    change = amb & (use_old != use_new)
    direct_cap_old = p.px_actual * p.shares_out * np.where(use_old, mult_b, 1.0)
    direct_cap_new = p.px_actual * p.shares_out * np.where(use_new, mult_b, 1.0)
    cap_ratio = direct_cap_new / direct_cap_old
    changed = p.loc[change, ["month_end", "entity", "series", "sector", "shares_out", "px_actual",
                             "mktcap", "in_universe", "composite", "ep", "fcfp", "bp", "ebit_ev"]].copy()
    changed["legacy_fix"] = use_old[change]
    changed["causal_fix"] = use_new[change]
    changed["split_ratio"] = mult_b[change]
    changed["cap_ratio_new_over_old"] = cap_ratio[change]
    changed.to_csv(OUT / "causal_share_changed_rows.csv", index=False)
    result = {
        "scope": "Diagnostic of split-basis decision only, not complete B1 rerun or CAGR delta",
        "inputs_sha256": {str(PANEL.relative_to(ROOT)): sha(PANEL), str(SPLITS.relative_to(ROOT)): sha(SPLITS)},
        "panel_rows": n,
        "ambiguous_split_rows": int(amb.sum()),
        "saved_fix_rows": int(old_saved.sum()),
        "reproduced_legacy_fix_rows": int(use_old.sum()),
        "saved_vs_reproduced_disagreements": int((old_saved != use_old).sum()),
        "causal_fix_rows": int(use_new.sum()),
        "legacy_vs_causal_changed_rows": int(change.sum()),
        "changed_rows_in_headline_2012_2026_period": int((change & (p.month_end >= "2011-12-01") & (p.month_end <= "2026-08-31")).sum()),
        "changed_rows_in_headline_period_scored_universe": int((change & (p.month_end >= "2011-12-01") & (p.month_end <= "2026-08-31") & p.in_universe.fillna(False) & p.composite.notna()).sum()),
        "changed_rows_with_saved_nonmissing_market_cap": int((change & p.mktcap.notna()).sum()),
        "causal_reference_missing_ambiguous_rows": int((amb & causal.isna()).sum()),
        "changed_by_year": changed.month_end.dt.year.value_counts().sort_index().to_dict(),
        "changed_by_series": changed.series.value_counts().to_dict(),
        "changed_cap_ratio_min": float(cap_ratio[change].min()) if change.any() else None,
        "changed_cap_ratio_max": float(cap_ratio[change].max()) if change.any() else None,
    }
    (OUT / "causal_share_probe.json").write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
