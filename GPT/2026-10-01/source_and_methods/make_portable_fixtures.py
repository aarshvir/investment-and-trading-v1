"""One-time extraction of SHA-traced CSV fixtures from immutable archived inputs.

Requires the original Python 3.11 research runtime with pyarrow. The resulting
gzip CSVs are read by tests using the standard bundled Python 3.12 runtime.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / "fixtures"
PANEL = ROOT / "v4/data/b1_panel.parquet"
SPLITS = ROOT / "v4/data/d2_splits.parquet"
PRICES = ROOT / "v4/data/d2_adjclose.parquet"
WEIGHTS = ROOT / "v4/outputs/lead_portfolio_build.json"
COLS = ["month_end", "entity", "series", "shares_out", "shares_out_date",
        "split_factor_after", "mktcap_split_fix", "in_universe", "composite"]


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    panel = pd.read_parquet(PANEL, columns=COLS)
    splits = pd.read_parquet(SPLITS)
    weights = json.loads(WEIGHTS.read_text(encoding="utf-8"))["weights"]
    tickers = [k for k, v in weights.items() if float(v) > 0]
    returns = pd.read_parquet(PRICES)[tickers].pct_change().loc["2023-09-25":"2026-09-25"].dropna(how="any")
    panel.to_csv(OUT / "b1_panel_selected.csv.gz", index=False,
                 compression={"method": "gzip", "mtime": 0})
    splits.to_csv(OUT / "d2_splits.csv.gz", index=False,
                 compression={"method": "gzip", "mtime": 0})
    returns.rename_axis("date").to_csv(OUT / "lead_20_returns.csv.gz", index=True,
                                       compression={"method": "gzip", "mtime": 0}, float_format="%.17g")
    manifest = {
        "provenance": "Derived once from archived v011-era source bytes; not fresh market data or a live quote",
        "source_sha256": {"b1_panel.parquet": sha(PANEL), "d2_splits.parquet": sha(SPLITS),
                          "d2_adjclose.parquet": sha(PRICES), "lead_portfolio_build.json": sha(WEIGHTS)},
        "fixture_sha256": {p.name: sha(p) for p in sorted(OUT.glob("*.csv.gz"))},
        "rows": {"panel": len(panel), "splits": len(splits), "returns": len(returns)},
        "returns_tickers": tickers,
        "cutoff": "2026-09-25 US close; returns diagnostic window 2023-09-25..2026-09-25",
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
