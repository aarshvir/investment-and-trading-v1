"""
b2_tests.py -- unit tests for b2_risk.py. Stdlib unittest only (no pytest in the pinned env).

Run:  PYTHONPATH='C:\\Users\\user\\eqv4\\pylib' python b2_tests.py -v
"""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import b2_risk as b2


class TestMaxDrawdown(unittest.TestCase):
    def test_zero_vol_series_has_zero_drawdown(self):
        wealth = pd.Series([1.0] * 50)
        self.assertEqual(b2.max_drawdown(wealth), 0.0)

    def test_known_drawdown(self):
        wealth = [1.0, 1.1, 0.99, 0.88, 0.95, 1.2]  # trough 0.88 vs peak 1.1 -> -0.2
        self.assertAlmostEqual(b2.max_drawdown(wealth), 0.88 / 1.1 - 1, places=9)

    def test_monotonic_up_has_zero_drawdown(self):
        wealth = np.cumprod(1 + np.full(100, 0.001))
        self.assertEqual(b2.max_drawdown(wealth), 0.0)


class TestRecentring(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(0)
        self.returns = pd.Series(rng.normal(0.0003, 0.01, 1000),
                                  index=pd.bdate_range("2015-01-02", periods=1000))

    def test_geometric_recentre_hits_target_exactly(self):
        target = 0.08
        adj = b2.recentre_to_geometric_drift(self.returns, target)
        geo_annual = np.exp(np.log1p(adj).mean() * b2.TRADING_DAYS_YEAR) - 1
        self.assertAlmostEqual(geo_annual, target, places=9)

    def test_geometric_recentre_negative_target(self):
        target = -0.05
        adj = b2.recentre_to_geometric_drift(self.returns, target)
        geo_annual = np.exp(np.log1p(adj).mean() * b2.TRADING_DAYS_YEAR) - 1
        self.assertAlmostEqual(geo_annual, target, places=9)

    def test_arithmetic_recentre_hits_target_exactly(self):
        target = 0.10
        adj = b2.recentre_arithmetic(self.returns, target)
        arith_annual = adj.mean() * b2.TRADING_DAYS_YEAR
        self.assertAlmostEqual(arith_annual, target, places=9)


class TestLedoitWolf(unittest.TestCase):
    def test_shrinkage_bounds_and_psd(self):
        rng = np.random.default_rng(1)
        X = rng.normal(0, 0.01, size=(300, 6))
        cov, delta = b2.ledoit_wolf_shrinkage(X)
        self.assertTrue(0.0 <= delta <= 1.0)
        self.assertTrue(np.allclose(cov, cov.T))
        eigvals = np.linalg.eigvalsh(cov)
        self.assertTrue((eigvals >= -1e-10).all())

    def test_shrinkage_toward_identity_reduces_offdiag(self):
        rng = np.random.default_rng(2)
        # small T relative to N -> sample covariance is noisy -> shrinkage should be nontrivial
        X = rng.normal(0, 0.01, size=(15, 10))
        cov, delta = b2.ledoit_wolf_shrinkage(X)
        self.assertGreater(delta, 0.0)


class TestPortfolioDailyPath(unittest.TestCase):
    def setUp(self):
        self.dates = pd.bdate_range("2021-01-04", periods=200)
        rng = np.random.default_rng(3)
        self.a_ret = rng.normal(0.0003, 0.01, size=len(self.dates))
        self.a_ret[0] = 0.0
        a_price = 100 * np.concatenate([[1.0], np.cumprod(1 + self.a_ret[1:])])
        self.prices = pd.DataFrame({"A": a_price}, index=self.dates)

    def test_weights_must_sum_to_one(self):
        with self.assertRaises(ValueError):
            b2.portfolio_daily_path({"A": 0.5, "B": 0.6}, self.dates[0], self.dates[-1],
                                     prices=self.prices.assign(B=self.prices["A"]))

    def test_unknown_ticker_raises(self):
        with self.assertRaises(KeyError):
            b2.portfolio_daily_path({"ZZZ": 1.0}, self.dates[0], self.dates[-1], prices=self.prices)

    def test_single_asset_matches_underlying_return(self):
        path = b2.portfolio_daily_path({"A": 1.0}, self.dates[0], self.dates[-1],
                                        rebalance="M", missing="exclude", prices=self.prices)
        expected = self.prices["A"].pct_change().dropna()
        pd.testing.assert_series_equal(path.daily_return, expected, check_names=False,
                                        check_freq=False, atol=1e-10)
        self.assertAlmostEqual(path.wealth.iloc[-1],
                                self.prices["A"].iloc[-1] / self.prices["A"].iloc[0], places=8)

    def test_exclude_renormalises_and_reports_missing_share(self):
        # B has no price at all for the first 60 obs (pre-IPO), then trades.
        b_ret = np.random.default_rng(4).normal(0.0005, 0.012, size=len(self.dates))
        b_price = np.full(len(self.dates), np.nan)
        b_price[60] = 50.0
        for i in range(61, len(self.dates)):
            b_price[i] = b_price[i - 1] * (1 + b_ret[i])
        prices = self.prices.assign(B=b_price)
        path = b2.portfolio_daily_path({"A": 0.5, "B": 0.5}, self.dates[0], self.dates[-1],
                                        rebalance="M", missing="exclude", prices=prices)
        self.assertFalse(path.wealth.isna().any())
        self.assertAlmostEqual(path.missing_share.iloc[0], 0.5, places=9)
        self.assertAlmostEqual(path.missing_share.iloc[-1], 0.0, places=9)
        self.assertTrue(((path.missing_share == 0.0) | (path.missing_share == 0.5)).all())

    def test_proxy_fill_scales_by_beta(self):
        # D is absent at the rebalance boundary (day 0) so its return is proxy-filled for the
        # whole (rebalance='none') period; over its later real-data segment D_ret = 2*A_ret
        # exactly, so the estimated beta should be ~2.0 and the very first synthetic day should
        # equal 1.5 * A's return (0.5*A + 0.5*2*A) exactly (no drift yet on day 1).
        n = len(self.dates)
        d_price = np.full(n, np.nan)
        d_price[100] = 50.0
        for i in range(101, n):
            d_price[i] = d_price[i - 1] * (1 + 2 * self.a_ret[i])
        prices = self.prices.assign(D=d_price)
        path = b2.portfolio_daily_path({"A": 0.5, "D": 0.5}, self.dates[0], self.dates[-1],
                                        rebalance="none", missing="proxy", proxies={"D": "A"},
                                        prices=prices)
        expected_day1 = 1.5 * self.a_ret[1]
        self.assertAlmostEqual(path.daily_return.iloc[0], expected_day1, places=9)
        self.assertAlmostEqual(path.synthetic_share.iloc[0], 0.5, places=9)
        self.assertAlmostEqual(path.missing_share.iloc[0], 0.0, places=9)

    def test_cash_fill_zero_rate_replicates_zero_fill(self):
        # B entirely missing over the whole (rebalance='none') window -> filled at a constant 0%.
        # Closed-form check for a never-rebalanced buy-and-hold: since B's slice never changes
        # value (0% every day), final wealth = 0.5*(A_end/A_start) + 0.5*1.0 exactly, independent
        # of the day-by-day weight drift inside the window (which the naive "0.5*A_t every day"
        # formula ignores -- that was the bug in an earlier version of this test).
        b_price = np.full(len(self.dates), np.nan)
        prices = self.prices.assign(B=b_price)
        path = b2.portfolio_daily_path({"A": 0.5, "B": 0.5}, self.dates[0], self.dates[49],
                                        rebalance="none", missing="cash", cash_annual=0.0,
                                        prices=prices)
        self.assertAlmostEqual(path.daily_return.iloc[0], 0.5 * self.a_ret[1], places=9)
        self.assertTrue((path.synthetic_share == 0.5).all())
        self.assertTrue((path.missing_share == 0.0).all())
        expected_final_wealth = 0.5 * (self.prices["A"].iloc[49] / self.prices["A"].iloc[0]) + 0.5 * 1.0
        self.assertAlmostEqual(path.wealth.iloc[-1], expected_final_wealth, places=8)


class TestStationaryBootstrap(unittest.TestCase):
    def test_indices_within_range(self):
        rng = np.random.default_rng(6)
        idx = b2._stationary_bootstrap_index_matrix(T=100, n_paths=50, horizon_days=40,
                                                     mean_block=10, rng=rng)
        self.assertEqual(idx.shape, (50, 40))
        self.assertTrue((idx >= 0).all() and (idx < 100).all())


class TestSimulateOutcomes(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(7)
        self.low_vol = pd.Series(rng.normal(0.0002, 0.005, 2000),
                                  index=pd.bdate_range("2010-01-04", periods=2000))

    def test_bootstrap_median_hits_recentred_target_within_tolerance(self):
        target = 0.08
        out = b2.simulate_outcomes(self.low_vol, drift_annual=target, horizons=[1], n=5000,
                                    mean_block=21, seed=11)
        median_ann = out["horizons"]["1y"]["annualized_return_pct"]["p50"]
        self.assertAlmostEqual(median_ann, target, delta=0.02)

    def test_self_vs_self_beat_probability_is_zero(self):
        out = b2.simulate_outcomes(self.low_vol, drift_annual=0.06, horizons=[1], n=1000, seed=3,
                                    benchmark_returns=self.low_vol, benchmark_drift_annual=0.06)
        self.assertEqual(out["horizons"]["1y"]["p_beat_benchmark"], 0.0)

    def test_no_recentre_when_drift_none(self):
        out_none = b2.simulate_outcomes(self.low_vol, drift_annual=None, horizons=[1], n=500, seed=1)
        self.assertIsNone(out_none["drift_annual"])

    def test_drawdown_probabilities_are_monotonic_in_threshold(self):
        out = b2.simulate_outcomes(self.low_vol, drift_annual=0.06, horizons=[5], n=4000,
                                    mean_block=21, seed=9)
        p = out["horizons"]["5y"]["p_drawdown_worse_than"]
        self.assertGreaterEqual(p["-10%"], p["-15%"])
        self.assertGreaterEqual(p["-15%"], p["-20%"])
        self.assertGreaterEqual(p["-20%"], p["-30%"])


class TestAllocationScenarios(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(8)
        self.eq = pd.Series(rng.normal(0.0003, 0.009, 1500),
                             index=pd.bdate_range("2012-01-02", periods=1500))

    def test_full_equity_mix_matches_simulate_outcomes_directly(self):
        alloc = b2.allocation_scenarios(self.eq, reserve_yield=0.04, mixes=[1.0], horizons=[1],
                                         n=2000, mean_block=21, seed=7)
        direct = b2.simulate_outcomes(self.eq, drift_annual=None, horizons=[1], n=2000,
                                       mean_block=21, seed=7)
        self.assertEqual(alloc["100/0"]["horizons"]["1y"]["p_total_return_gt_0"],
                          direct["horizons"]["1y"]["p_total_return_gt_0"])
        self.assertEqual(alloc["100/0"]["horizons"]["1y"]["annualized_return_pct"],
                          direct["horizons"]["1y"]["annualized_return_pct"])

    def test_more_cash_reduces_drawdown_risk(self):
        alloc = b2.allocation_scenarios(self.eq, reserve_yield=0.04, mixes=[1.0, 0.5],
                                         horizons=[5], n=3000, mean_block=21, seed=13)
        p100 = alloc["100/0"]["horizons"]["5y"]["p_drawdown_worse_than"]["-20%"]
        p50 = alloc["50/50"]["horizons"]["5y"]["p_drawdown_worse_than"]["-20%"]
        self.assertGreaterEqual(p100, p50)


class TestEmpiricalDrawdownFrequency(unittest.TestCase):
    def test_detects_a_known_drawdown(self):
        # Flat, then a clean -25% drop, then flat -- within a 1y window this must register.
        n = 400
        prices = np.concatenate([np.full(50, 100.0), np.linspace(100, 75, 30), np.full(320, 75.0)])
        s = pd.Series(prices, index=pd.bdate_range("2019-01-02", periods=n))
        out = b2.empirical_drawdown_frequency(s, horizons_years=[1], thresholds=[-0.20])
        self.assertGreater(out["1y"]["p_worse_than_20pct"], 0.0)

    def test_flat_series_has_zero_frequency(self):
        s = pd.Series(100.0, index=pd.bdate_range("2019-01-02", periods=400))
        out = b2.empirical_drawdown_frequency(s, horizons_years=[1], thresholds=[-0.15, -0.20])
        self.assertEqual(out["1y"]["p_worse_than_15pct"], 0.0)
        self.assertEqual(out["1y"]["p_worse_than_20pct"], 0.0)


class TestRealDataSmoke(unittest.TestCase):
    """Light integration checks against the actual D2/D1 outputs this module is built for."""

    def test_load_prices_and_sector_map(self):
        try:
            prices = b2.load_prices()
        except FileNotFoundError:
            self.skipTest("D2 price panel not present in this environment")
            return
        self.assertIn("SPY", prices.columns)
        self.assertIn("ABNB", prices.columns)
        abnb_first = prices["ABNB"].dropna().index[0]
        self.assertEqual(str(abnb_first.date()), "2020-12-10")
        sectors = b2.load_sector_map()
        self.assertEqual(sectors.get("MSFT"), "Information Technology")

    def test_stress_windows_search_locates_2025_tariff_shock(self):
        try:
            prices = b2.load_prices()
        except FileNotFoundError:
            self.skipTest("D2 price panel not present in this environment")
            return
        peak, trough, dd = b2.find_drawdown_window(prices["SPY"], "2025-01-01", "2025-06-30")
        self.assertLess(dd, -0.05)
        self.assertLess(peak, trough)


if __name__ == "__main__":
    unittest.main(verbosity=2)
