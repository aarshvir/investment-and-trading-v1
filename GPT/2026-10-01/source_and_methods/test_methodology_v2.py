"""Focused archived-input and unit tests for methodology_v2.

The compressed CSV fixtures are derived from SHA-pinned archived Parquet data,
so these tests require only pandas/numpy and standard-library gzip, not pyarrow.
All tests are read-only toward the existing repository and releases.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

from methodology_v2 import (
    AmbiguousVerdictError,
    InvalidResearchRecord,
    causal_share_basis_repair,
    effective_verdict,
    scaled_identity_shrinkage_v2,
)


ROOT = Path(__file__).resolve().parents[3]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
PANEL = ROOT / "v4/data/b1_panel.parquet"
SPLITS = ROOT / "v4/data/d2_splits.parquet"
PRICES = ROOT / "v4/data/d2_adjclose.parquet"
WEIGHTS = ROOT / "v4/outputs/lead_portfolio_build.json"
EXPECTED_SHA = {
    PANEL: "eb0056e204af219e4a87b171f45e137715b95c4bcd1202d38cfe24b570c29ff8",
    SPLITS: "f7555535ed89204c6762ab49f866c1ea59a7cef8ad7767d991ab9a419c5dea57",
    PRICES: "3da4932d998bf4a2aff1804cfd3778530dbbccca56446228bcd2f279dbaf028f",
    WEIGHTS: "e996d6f3a94a47f3c23c4f7a35a0874079f3d6452cf127eb935a4cac78e5c084",
}


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def sample_verdict(analysis_id="R1", revision=1, *, supersedes_id=None, status="APPROVED",
                   approved_at="2026-09-25T21:00:00Z", verdict="INCLUDE"):
    return {
        "analysis_id": analysis_id, "ticker": "FRT", "revision": revision,
        "verdict": verdict, "status": status, "approved_at_utc": approved_at,
        "market_cutoff_utc": "2026-09-25T20:00:00Z",
        "filing_cutoff_utc": "2026-09-25T20:00:00Z",
        "source_sha256": "a" * 64, "supersedes_id": supersedes_id,
    }


class MethodologyV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest = json.loads((FIXTURES / "manifest.json").read_text(encoding="utf-8"))
        for name, expected in manifest["fixture_sha256"].items():
            assert sha(FIXTURES / name) == expected, f"fixture has changed: {name}"
        for path, expected in EXPECTED_SHA.items():
            if not path.exists():
                raise unittest.SkipTest(f"archived input unavailable: {path}")
            assert sha(path) == expected, f"archived input has changed: {path}"

    def test_causal_share_repair_archived_scope(self):
        cols = ["month_end", "entity", "series", "shares_out", "shares_out_date",
                "split_factor_after", "mktcap_split_fix"]
        panel = pd.read_csv(FIXTURES / "b1_panel_selected.csv.gz",
                            parse_dates=["month_end", "shares_out_date"])[cols]
        splits = pd.read_csv(FIXTURES / "d2_splits.csv.gz", parse_dates=["date"])
        legacy_date_allowed = causal_share_basis_repair(panel, splits, reject_future_share_dates=False)
        old = panel.mktcap_split_fix.fillna(False).astype(bool).to_numpy()
        new = legacy_date_allowed.split_adjustment_applied.to_numpy()
        self.assertEqual(int(legacy_date_allowed.split_ambiguous.sum()), 590)
        self.assertEqual(int(new.sum()), 382)
        self.assertEqual(int((old != new).sum()), 90)
        self.assertEqual(int(legacy_date_allowed.future_share_date.sum()), 16)
        strict = causal_share_basis_repair(panel, splits)
        self.assertEqual(int(strict.future_share_date.sum()), 16)
        self.assertTrue(strict.loc[strict.future_share_date, "chosen_share_count"].isna().all())

    def test_causal_prefix_unchanged_by_future_input(self):
        dates = pd.to_datetime(["2020-01-31", "2020-02-28", "2020-03-31", "2020-04-30"])
        panel = pd.DataFrame({
            "month_end": dates, "entity": ["E"] * 4, "series": ["X"] * 4,
            "shares_out": [100., 60., 200., 1000.],
            "shares_out_date": [dates[0], dates[0], dates[2], dates[3]],
            "split_factor_after": [1., 1., 1., 1.],
        })
        splits = pd.DataFrame({"date": [dates[1]], "ticker": ["X"], "split_ratio": [2.]})
        early = causal_share_basis_repair(panel.iloc[:2], splits)
        full = causal_share_basis_repair(panel, splits)
        pd.testing.assert_frame_equal(early, full.iloc[:2].reset_index(drop=True))
        self.assertTrue(bool(full.loc[1, "split_adjustment_applied"]))

    def test_scaled_identity_archived_20_stock_window(self):
        weights = json.loads(WEIGHTS.read_text(encoding="utf-8"))["weights"]
        weights = {k: float(v) for k, v in weights.items() if float(v) > 0}
        returns = pd.read_csv(FIXTURES / "lead_20_returns.csv.gz", index_col="date", parse_dates=["date"])[list(weights)]
        self.assertEqual(len(returns), 754)
        cov, intensity = scaled_identity_shrinkage_v2(returns.to_numpy())
        w = np.array([weights[k] for k in returns.columns])
        w /= w.sum()
        vol = float(np.sqrt(w @ cov @ w * 252))
        self.assertAlmostEqual(intensity, 0.03758231685985554, places=10)
        self.assertAlmostEqual(vol, 0.1333503430544168, places=10)
        self.assertTrue(np.allclose(cov, cov.T, atol=1e-15))
        self.assertGreaterEqual(float(np.linalg.eigvalsh(cov).min()), -1e-14)

    def test_scaled_identity_input_and_scalar_case(self):
        cov, intensity = scaled_identity_shrinkage_v2(np.array([[0.0], [0.1], [-0.1]]))
        self.assertEqual(intensity, 0.0)
        self.assertEqual(cov.shape, (1, 1))
        with self.assertRaises(InvalidResearchRecord):
            scaled_identity_shrinkage_v2(np.array([[1., np.nan], [2., 3.]]))

    def test_verdict_precedence_is_explicit(self):
        first = sample_verdict()
        second = sample_verdict("R2", 2, supersedes_id="R1", verdict="INCLUDE-SMALL",
                                approved_at="2026-09-26T21:00:00Z")
        future = sample_verdict("R3", 3, supersedes_id="R2", verdict="WATCH",
                                approved_at="2026-10-02T21:00:00Z")
        self.assertEqual(effective_verdict([first, second, future], "frt", "2026-10-01T00:00:00Z")["analysis_id"], "R2")
        self.assertEqual(effective_verdict([first, second, future], "FRT", "2026-09-26T00:00:00Z")["analysis_id"], "R1")
        draft = sample_verdict("R4", 4, supersedes_id="R2", status="DRAFT",
                               approved_at="2026-09-30T21:00:00Z")
        self.assertEqual(effective_verdict([first, second, draft], "FRT", "2026-10-01T00:00:00Z")["analysis_id"], "R2")

    def test_verdict_parallel_branches_rejected(self):
        roots = [sample_verdict(), sample_verdict("R2", 2, verdict="WATCH")]
        with self.assertRaises(AmbiguousVerdictError):
            effective_verdict(roots, "FRT", "2026-10-01T00:00:00Z")
        bad = sample_verdict()
        bad["source_sha256"] = "not-a-hash"
        with self.assertRaises(InvalidResearchRecord):
            effective_verdict([bad], "FRT", "2026-10-01T00:00:00Z")


if __name__ == "__main__":
    unittest.main(verbosity=2)
