"""Read-only diagnostic for the archived B2 covariance shrinkage scaling."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "v4/code"))
import b2_risk as b2  # noqa: E402

OUT = Path(__file__).resolve().parent
BUILD = ROOT / "v4/outputs/lead_portfolio_build.json"
PRICE = ROOT / "v4/data/d2_adjclose.parquet"
SOURCE = ROOT / "v4/code/b2_risk.py"


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    weights = json.loads(BUILD.read_text(encoding="utf-8"))["weights"]
    weights = {k: float(v) for k, v in weights.items() if float(v) > 0}
    total = sum(weights.values())
    weights = {k: v / total for k, v in weights.items()}
    prices = b2.load_prices()
    returns = prices[list(weights)].pct_change().loc["2023-09-25":"2026-09-25"].dropna(how="any")
    X = returns.to_numpy(dtype=float)
    old_cov, old_delta = b2.ledoit_wolf_shrinkage(X)
    X = X - X.mean(axis=0, keepdims=True)
    t, n = X.shape
    sample = X.T @ X / t
    mu = np.trace(sample) / n
    target = mu * np.eye(n)
    d2 = float(np.sum((sample - target) ** 2))
    # Variance of sample covariance is E[||x x' - S||^2] / T. The
    # archived function uses the expectation without the final /T.
    deviations = np.einsum("ti,tj->tij", X, X) - sample[None, :, :]
    b_bar2 = float(np.mean(np.sum(deviations ** 2, axis=(1, 2))))
    corrected_delta = min(1.0, b_bar2 / t / d2) if d2 > 0 else 0.0
    corrected_cov = corrected_delta * target + (1 - corrected_delta) * sample
    w = np.array([weights[k] for k in returns.columns])
    annual = lambda cov: float(np.sqrt(max(w @ cov @ w, 0) * 252))
    result = {
        "scope": "Scaling diagnostic for existing B2 scaled-identity estimator, not an independently certified Ledoit-Wolf implementation",
        "input_sha256": {str(x.relative_to(ROOT)): sha(x) for x in (BUILD, PRICE, SOURCE)},
        "window": f"{returns.index[0].date()}..{returns.index[-1].date()}",
        "observations": t,
        "names": n,
        "archived_delta": old_delta,
        "variance_sum_divisor_required": t,
        "diagnostic_corrected_delta": corrected_delta,
        "archived_annual_vol": annual(old_cov),
        "diagnostic_corrected_annual_vol": annual(corrected_cov),
        "sample_annual_vol": annual(sample),
    }
    (OUT / "shrinkage_probe.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
