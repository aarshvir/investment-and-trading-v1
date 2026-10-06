"""Build a reproducible, bounded validation record for methodology_v2."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from methodology_v2 import causal_share_basis_repair, scaled_identity_shrinkage_v2


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
FIXTURES = OUT / "fixtures"
FILES = {
    "panel": ROOT / "v4/data/b1_panel.parquet",
    "splits": ROOT / "v4/data/d2_splits.parquet",
    "prices": ROOT / "v4/data/d2_adjclose.parquet",
    "weights": ROOT / "v4/outputs/lead_portfolio_build.json",
    "module": OUT / "methodology_v2.py",
}


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    manifest = json.loads((FIXTURES / "manifest.json").read_text(encoding="utf-8"))
    for name, expected in manifest["fixture_sha256"].items():
        if sha(FIXTURES / name) != expected:
            raise ValueError(f"portable fixture hash mismatch: {name}")
    if sha(FILES["panel"]) != manifest["source_sha256"]["b1_panel.parquet"]:
        raise ValueError("archived panel source hash mismatch")
    if sha(FILES["splits"]) != manifest["source_sha256"]["d2_splits.parquet"]:
        raise ValueError("archived split source hash mismatch")
    p = pd.read_csv(FIXTURES / "b1_panel_selected.csv.gz",
                    parse_dates=["month_end", "shares_out_date"])
    s = pd.read_csv(FIXTURES / "d2_splits.csv.gz", parse_dates=["date"])
    original = p.mktcap_split_fix.fillna(False).astype(bool).to_numpy()
    repaired = causal_share_basis_repair(p, s)
    repaired_no_date_gate = causal_share_basis_repair(p, s, reject_future_share_dates=False)
    new = repaired.split_adjustment_applied.to_numpy()
    no_date = repaired_no_date_gate.split_adjustment_applied.to_numpy()
    headline = ((p.month_end >= "2011-12-01") & (p.month_end <= "2026-08-31")
                & p.in_universe.fillna(False) & p.composite.notna()).to_numpy()
    weights = json.loads(FILES["weights"].read_text(encoding="utf-8"))["weights"]
    weights = {k: float(v) for k, v in weights.items() if float(v) > 0}
    ret = pd.read_csv(FIXTURES / "lead_20_returns.csv.gz", index_col="date", parse_dates=["date"])[list(weights)]
    cov, intensity = scaled_identity_shrinkage_v2(ret.to_numpy())
    w = np.array([weights[k] for k in ret.columns]); w /= w.sum()
    sample = np.cov(ret.to_numpy(), rowvar=False, ddof=0)
    result = {
        "scope": "Primitive-level validation only; full B1 factor-rank/return backtest and production portfolio optimizer were not rerun",
        "source_sha256": {k: sha(v) for k, v in FILES.items()},
        "fixture_sha256": manifest["fixture_sha256"],
        "causal_share": {
            "panel_rows": len(p),
            "ambiguous_rows_with_strict_date_gate": int(repaired.split_ambiguous.sum()),
            "future_share_date_rows_rejected": int(repaired.future_share_date.sum()),
            "original_split_fixes": int(original.sum()),
            "causal_split_fixes_without_date_gate": int(no_date.sum()),
            "split_decisions_changed_without_date_gate": int((original != no_date).sum()),
            "strict_causal_split_fixes": int(new.sum()),
            "strict_decisions_changed_from_original": int((original != new).sum()),
            "strict_changed_in_headline_scored_universe": int(((original != new) & headline).sum()),
            "note": "Future-dated share records are separately nullified; counts of changed split flags do not count every affected valuation metric",
        },
        "scaled_identity_covariance": {
            "observations": len(ret), "names": ret.shape[1],
            "window": f"{ret.index[0].date()}..{ret.index[-1].date()}",
            "corrected_shrinkage_intensity": intensity,
            "corrected_annual_vol": float(np.sqrt(w @ cov @ w * 252)),
            "sample_annual_vol_ddof0": float(np.sqrt(w @ sample @ w * 252)),
            "minimum_eigenvalue": float(np.linalg.eigvalsh(cov).min()),
        },
    }
    (OUT / "methodology_v2_validation.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
