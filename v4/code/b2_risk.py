"""
b2_risk.py -- Agent B2: risk engine (drawdowns, stress tests, probability of outcomes).

Reusable, documented, unit-tested module. See v4/prompts/B2_risk_engine.md for the spec and
v4/outputs/b2_report.md for results and how to call this on a new portfolio.

Design principles (see v4/CONVENTIONS.md):
  - Missing is MISSING: portfolio_daily_path never silently zero-fills a name with no price.
    Every probability this module reports is conditional on an explicitly stated scenario.
  - No sklearn is available in the pinned environment, so Ledoit-Wolf shrinkage is implemented
    analytically (Ledoit & Wolf 2004, shrinkage toward a scaled-identity target).

Public API
----------
load_prices() -> DataFrame                          D2 adjusted (total-return) daily closes
load_sector_map() -> dict[ticker -> GICS sector]
load_flagged_ticks() -> (bad_ticks_df, confirmed_errors_df)
max_drawdown(wealth) -> float
recentre_to_geometric_drift(returns, target_annual) -> Series      (log-space, geometric)
recentre_arithmetic(returns, target_annual_arithmetic) -> Series   (simple-return shift)
ledoit_wolf_shrinkage(X) -> (cov, shrinkage_intensity)
portfolio_daily_path(weights, start, end, rebalance, proxies, missing, ...) -> PortfolioPath
risk_summary(weights, ...) -> dict
stress_tests(weights, ...) -> dict
simulate_outcomes(source, drift_annual, ...) -> dict
allocation_scenarios(equity_sleeve_returns, reserve_yield, mixes, ...) -> dict
empirical_drawdown_frequency(price_series, horizons_years, thresholds) -> dict
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252

V4_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = V4_DIR / "data"
OUTPUTS_DIR = V4_DIR / "outputs"


# ---------------------------------------------------------------------------
# 1. Data loading
# ---------------------------------------------------------------------------

def load_prices(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Load D2's adjusted (dividend/split total-return) daily closes.

    Returns a DataFrame indexed by NYSE trading day (datetime64), columns = Yahoo-style tickers.
    Close-to-close simple returns computed from this panel are total returns (see d2_report.md
    Sec.1). Missing cells are genuine NaN (pre-listing / post-delisting / no data) -- never filled
    here; callers decide how to handle gaps via `portfolio_daily_path`'s `missing` argument.
    """
    data_dir = Path(data_dir) if data_dir else DATA_DIR
    df = pd.read_parquet(data_dir / "d2_adjclose.parquet")
    df.index = pd.to_datetime(df.index)
    return df.sort_index()


def load_sector_map(data_dir: Optional[Path] = None) -> Dict[str, str]:
    """ticker -> GICS sector, from D1's current-constituent table (current sector only; no PIT
    sector history is used here since this module is about risk, not point-in-time backtesting)."""
    data_dir = Path(data_dir) if data_dir else DATA_DIR
    fp = data_dir / "d1_current_constituents.csv"
    if not fp.exists():
        return {}
    df = pd.read_csv(fp)
    return dict(zip(df["ticker_yahoo"], df["gics_sector"]))


def load_flagged_ticks(data_dir: Optional[Path] = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """D2's flagged >50% daily moves and cross-source-contradicted values, for disclosure only.
    Returns (bad_ticks_df, confirmed_errors_df); both empty DataFrames if files are absent."""
    data_dir = Path(data_dir) if data_dir else DATA_DIR
    bt_fp, ce_fp = data_dir / "d2_bad_ticks.csv", data_dir / "d2_confirmed_errors.csv"
    bt = pd.read_csv(bt_fp, parse_dates=["date"]) if bt_fp.exists() else pd.DataFrame()
    ce = pd.read_csv(ce_fp, parse_dates=["date"]) if ce_fp.exists() else pd.DataFrame()
    return bt, ce


def flagged_ticks_for(tickers: Sequence[str], data_dir: Optional[Path] = None) -> dict:
    """Convenience: which of `tickers` have any D2 bad-tick / confirmed-error flags, for a report
    disclosure line. Does not modify or exclude any data."""
    bt, ce = load_flagged_ticks(data_dir)
    out = {}
    for t in tickers:
        hits_bt = bt[bt["ticker"] == t] if len(bt) else bt
        hits_ce = ce[ce["ticker"] == t] if len(ce) else ce
        if len(hits_bt) or len(hits_ce):
            out[t] = dict(bad_ticks=len(hits_bt), confirmed_errors=len(hits_ce))
    return out


# ---------------------------------------------------------------------------
# 2. Small numeric helpers
# ---------------------------------------------------------------------------

def max_drawdown(wealth: Union[pd.Series, np.ndarray, Sequence[float]]) -> float:
    """Worst peak-to-trough fractional decline of a wealth/price path. A constant (zero-return)
    series has max_drawdown == 0.0 exactly."""
    arr = np.asarray(wealth, dtype=float)
    if arr.size == 0:
        return float("nan")
    running_max = np.maximum.accumulate(arr)
    dd = arr / running_max - 1.0
    return float(dd.min())


def recentre_to_geometric_drift(returns: pd.Series, target_annual: float) -> pd.Series:
    """Shift daily returns so the series' OWN compounded (geometric) annual growth rate equals
    `target_annual`, preserving the shape/vol/autocorrelation of the historical series (a location
    shift applied additively in log-return space):

        shift   = ln(1 + target_annual) / 252  -  mean(ln(1 + r_hist))
        r_adj_t = exp( ln(1 + r_t) + shift ) - 1

    By construction, exp(252 * mean(ln(1+r_adj))) - 1 == target_annual (exactly, up to float
    error) on the recentred pool itself; a stationary bootstrap drawn FROM that recentred pool
    will have a sample geometric mean that is close to, but not exactly, the target (sampling
    variance from resampling + block structure), which is expected and reported, not hidden.
    """
    r = pd.Series(returns).dropna()
    log_r = np.log1p(r.to_numpy())
    mu_hist = log_r.mean()
    mu_target = math.log1p(target_annual) / TRADING_DAYS_YEAR
    shift = mu_target - mu_hist
    adjusted = np.expm1(log_r + shift)
    return pd.Series(adjusted, index=r.index)


def recentre_arithmetic(returns: pd.Series, target_annual_arithmetic: float) -> pd.Series:
    """Simple additive shift of daily SIMPLE returns so their arithmetic mean equals
    target_annual_arithmetic / 252. Used only by `allocation_scenarios`, which is specified as
    'arithmetic only' -- deliberately NOT the geometric/log-space method above."""
    r = pd.Series(returns).dropna()
    shift = target_annual_arithmetic / TRADING_DAYS_YEAR - r.mean()
    return r + shift


def ledoit_wolf_shrinkage(X: np.ndarray) -> Tuple[np.ndarray, float]:
    """Analytic Ledoit-Wolf (2004, 'A well-conditioned estimator for large-dimensional covariance
    matrices') shrinkage of the sample covariance toward a scaled-identity target F = mu*I,
    mu = trace(S)/N. No sklearn dependency (not installed in this environment); this is the same
    estimator sklearn.covariance.ledoit_wolf implements (Chen et al. 2010 formulation).

    X: (T, N) array of demeaned-or-not daily returns (T obs, N assets); demeaning is done here.
    Returns (shrunk_covariance (N,N), shrinkage_intensity in [0,1]).
    """
    X = np.asarray(X, dtype=float)
    X = X - X.mean(axis=0, keepdims=True)
    T, N = X.shape
    if T < 2 or N < 1:
        raise ValueError("need at least 2 observations and 1 asset for shrinkage")
    S = (X.T @ X) / T
    mu = np.trace(S) / N
    F = mu * np.eye(N)
    diff = S - F
    d2 = float(np.sum(diff * diff))
    outer = np.einsum("ti,tj->tij", X, X)          # T x N x N, each x_t x_t'
    dev = outer - S[None, :, :]
    b_bar2 = float(np.mean(np.sum(dev * dev, axis=(1, 2))))
    b2 = min(b_bar2, d2)
    delta = 0.0 if d2 <= 0 else b2 / d2
    delta = float(min(max(delta, 0.0), 1.0))
    shrunk = delta * F + (1 - delta) * S
    return shrunk, delta


# ---------------------------------------------------------------------------
# 3. Portfolio daily wealth path (rebalancing + explicit missing-history handling)
# ---------------------------------------------------------------------------

@dataclass
class PortfolioPath:
    wealth: pd.Series            # starts at 1.0 on the first date, compounds daily
    daily_return: pd.Series
    missing_share: pd.Series     # target weight genuinely excluded that day (never zero-filled)
    synthetic_share: pd.Series   # target weight covered by a disclosed proxy/cash fill that day
    meta: dict

    def summary(self) -> dict:
        n_years = (self.wealth.index[-1] - self.wealth.index[0]).days / 365.25
        end_wealth = float(self.wealth.iloc[-1])
        cagr = float(end_wealth ** (1 / n_years) - 1) if n_years > 0 else float("nan")
        return dict(
            start=str(self.wealth.index[0].date()), end=str(self.wealth.index[-1].date()),
            n_days=int(len(self.wealth)), total_return=end_wealth - 1.0, cagr=cagr,
            max_drawdown=max_drawdown(self.wealth),
            missing_weight_share_mean=float(self.missing_share.mean()),
            missing_weight_share_max=float(self.missing_share.max()),
            synthetic_weight_share_mean=float(self.synthetic_share.mean()),
            **self.meta,
        )


def _period_boundaries(dates: pd.DatetimeIndex, rebalance: str) -> List[pd.Timestamp]:
    """Rebalance reference dates: the first date, plus each month-/quarter-end trading day
    present in `dates` (excluding the very last date, which needs no further rebalance)."""
    if rebalance == "none":
        return [dates[0]]
    if rebalance not in ("M", "Q"):
        raise ValueError("rebalance must be one of 'M', 'Q', 'none'")
    periods = dates.to_period(rebalance)
    df = pd.DataFrame({"date": dates, "period": periods})
    period_ends = df.groupby("period")["date"].max()
    boundaries = sorted(set(period_ends.tolist()) | {dates[0]})
    boundaries = [b for b in boundaries if b < dates[-1]]
    if dates[0] not in boundaries:
        boundaries = [dates[0]] + boundaries
    return sorted(set(boundaries))


def portfolio_daily_path(
    weights: Dict[str, float],
    start,
    end,
    rebalance: str = "M",
    proxies: Optional[Dict[str, str]] = None,
    missing: str = "exclude",
    cash_annual: float = 0.0,
    prices: Optional[pd.DataFrame] = None,
) -> PortfolioPath:
    """Daily wealth path of a portfolio built from D2 adjusted closes, with explicit, disclosed
    handling of names that lack a price at a given rebalance date.

    weights   : {ticker: target weight}, must sum to 1.0 (tol 1e-6).
    rebalance : 'M' | 'Q' | 'none'. Target weights are (re-)applied, renormalised per `missing`,
                at the first date and at every subsequent month-/quarter-end; between rebalances
                weights drift with cumulative returns (buy-and-hold within the period). A name
                already held that stops trading mid-period (delisting) is frozen at 0% return
                from its last valid price until the next rebalance re-evaluates availability.
    missing   : how to treat a name with NO price at a rebalance date (evaluated ONCE per period,
                at that period's start date -- never mid-period):
        'exclude' - drop the name for that whole period and renormalise the remaining target
                    weights so they sum to 1; the dropped weight is reported daily in
                    `missing_share` (never zero-filled or treated as cash).
        'proxy'   - for names in `proxies` ({ticker: proxy_ticker}), fill the whole period with
                    the proxy's daily return scaled by the name's historical beta to that proxy
                    (OLS slope, no intercept, estimated over their full common overlap in the
                    price panel; beta=1.0 if overlap < 60 days). Flagged as `synthetic_share`.
                    Names not listed in `proxies` fall back to 'exclude'.
        'cash'    - fill with a constant daily return implied by `cash_annual` (0.0 replicates a
                    naive "zero-fill"). Only intended as a disclosed sensitivity run (matches
                    CONVENTIONS: "never silently zero-fill" -- this makes the assumption explicit
                    and visible in `synthetic_share` / `meta['missing_mode']` instead).
    prices    : optional pre-loaded panel (else `load_prices()`).

    Returns PortfolioPath(wealth, daily_return, missing_share, synthetic_share, meta).
    """
    if missing not in ("exclude", "proxy", "cash"):
        raise ValueError("missing must be 'exclude', 'proxy' or 'cash'")
    wsum = sum(weights.values())
    if not math.isclose(wsum, 1.0, abs_tol=1e-6):
        raise ValueError(f"weights must sum to 1.0 (got {wsum:.6f})")

    prices = load_prices() if prices is None else prices
    tickers = list(weights.keys())
    absent = [t for t in tickers if t not in prices.columns]
    if absent:
        raise KeyError(f"tickers missing from price panel: {absent}")

    px = prices.loc[pd.Timestamp(start):pd.Timestamp(end), tickers]
    if len(px) < 2:
        raise ValueError("need at least 2 trading days between start and end")
    rets_real = px.pct_change()
    dates = px.index
    proxies = proxies or {}

    proxy_ret: Dict[str, pd.Series] = {}
    proxy_beta: Dict[str, float] = {}
    for tgt, prx in proxies.items():
        if prx not in prices.columns:
            continue
        both = prices[[tgt, prx]].pct_change().dropna()
        if len(both) >= 60:
            # np.cov defaults to ddof=1; np.var must match or the ratio picks up a spurious
            # N/(N-1) factor (caught by b2_tests.test_proxy_fill_scales_by_beta).
            var_p = float(np.var(both[prx].to_numpy(), ddof=1))
            beta = float(np.cov(both[tgt], both[prx])[0, 1] / var_p) if var_p > 0 else 1.0
        else:
            beta = 1.0
        proxy_beta[tgt] = beta
        proxy_ret[tgt] = prices[prx].pct_change() * beta

    w0 = pd.Series(weights, dtype=float)
    boundaries = _period_boundaries(dates, rebalance)
    cash_daily = (1 + cash_annual) ** (1 / TRADING_DAYS_YEAR) - 1

    out_dates: List[pd.Timestamp] = []
    out_wealth: List[float] = []
    out_ret: List[float] = []
    out_missing: List[float] = []
    out_synth: List[float] = []
    any_frozen_delist = False

    cur_wealth = 1.0
    for bi, b_start in enumerate(boundaries):
        b_end = boundaries[bi + 1] if bi + 1 < len(boundaries) else dates[-1]
        period_dates = dates[(dates > b_start) & (dates <= b_end)]
        if len(period_dates) == 0:
            continue

        price_at_b = px.loc[b_start]
        has_price = price_at_b.notna()
        valid = has_price.copy()
        synthetic = pd.Series(False, index=tickers)
        period_rets = pd.DataFrame(index=period_dates, columns=tickers, dtype=float)

        for t in tickers:
            if has_price[t]:
                col = rets_real.loc[period_dates, t]
                if col.isna().any():
                    any_frozen_delist = True
                period_rets[t] = col.fillna(0.0)
            elif missing == "proxy" and t in proxy_ret:
                period_rets[t] = proxy_ret[t].reindex(period_dates).fillna(0.0)
                valid[t] = True
                synthetic[t] = True
            elif missing == "cash":
                period_rets[t] = cash_daily
                valid[t] = True
                synthetic[t] = True
            else:
                period_rets[t] = 0.0  # weight will be 0 below; value is inert

        w_target = w0.where(valid, 0.0)
        vsum = float(w_target.sum())
        if vsum <= 0:
            raise RuntimeError(f"no valid/proxyable names at rebalance {b_start.date()}")
        w_target = w_target / vsum
        missing_share = float(w0[~valid].sum())
        synthetic_share = float(w0[synthetic].sum())

        w_run = w_target.to_numpy()
        R = period_rets.to_numpy()
        for i in range(R.shape[0]):
            r_d = R[i]
            r_p = float(np.dot(w_run, r_d))
            cur_wealth *= (1 + r_p)
            out_dates.append(period_dates[i])
            out_wealth.append(cur_wealth)
            out_ret.append(r_p)
            out_missing.append(missing_share)
            out_synth.append(synthetic_share)
            grown = w_run * (1 + r_d)
            denom = 1 + r_p
            w_run = grown / denom if denom != 0 else w_target.to_numpy()

    idx = pd.DatetimeIndex(out_dates)
    meta = dict(
        rebalance=rebalance, missing_mode=missing, proxies=dict(proxies),
        cash_annual=cash_annual, tickers=tickers, n_names=len(tickers),
        any_frozen_delisting=any_frozen_delist,
    )
    return PortfolioPath(
        wealth=pd.Series(out_wealth, index=idx, name="wealth"),
        daily_return=pd.Series(out_ret, index=idx, name="return"),
        missing_share=pd.Series(out_missing, index=idx, name="missing_share"),
        synthetic_share=pd.Series(out_synth, index=idx, name="synthetic_share"),
        meta=meta,
    )


# ---------------------------------------------------------------------------
# 4. Risk summary
# ---------------------------------------------------------------------------

def risk_summary(
    weights: Dict[str, float],
    prices: Optional[pd.DataFrame] = None,
    asof=None,
    sector_map: Optional[Dict[str, str]] = None,
    windows: Sequence[int] = (3, 5),
    benchmark: str = "SPY",
) -> dict:
    """Ex-ante risk summary using ONLY days where every held name + benchmark has a real price
    (so pre-listing gaps do not enter the covariance estimate; disclosed as `n_days`/`start`).

    Per window (years, trailing from `asof`, default = latest date in the panel):
      vol_annual (Ledoit-Wolf shrunk), shrinkage_intensity, beta_vs_benchmark, tracking_error,
      risk_contribution_pct by name and by GICS sector (sum to 1), effective number of bets
      (1/sum(w^2) and 1/sum(risk_contribution^2)), average pairwise correlation, top-3 PC share
      of variance (correlation-matrix PCA).
    """
    prices = load_prices() if prices is None else prices
    sector_map = load_sector_map() if sector_map is None else sector_map
    asof_ts = pd.Timestamp(asof) if asof is not None else prices.index[-1]
    tickers = list(weights.keys())
    w = np.array([weights[t] for t in tickers], dtype=float)
    if not math.isclose(w.sum(), 1.0, abs_tol=1e-6):
        raise ValueError(f"weights must sum to 1.0 (got {w.sum():.6f})")
    all_needed = list(dict.fromkeys(tickers + [benchmark]))

    result: dict = {"asof": str(asof_ts.date()), "benchmark": benchmark, "windows": {}}
    for yrs in windows:
        w_start = asof_ts - pd.DateOffset(years=yrs)
        sub = prices.loc[w_start:asof_ts, all_needed].dropna(how="any")
        rets = sub.pct_change().iloc[1:]
        if len(rets) < 20:
            result["windows"][f"{yrs}y"] = {"error": "insufficient overlapping history"}
            continue

        X = rets[tickers].to_numpy()
        cov_shrunk, delta = ledoit_wolf_shrinkage(X)
        port_var_daily = float(w @ cov_shrunk @ w)
        vol_annual = math.sqrt(max(port_var_daily, 0.0) * TRADING_DAYS_YEAR)
        # Raw (unshrunk) sample-covariance vol, for comparison: a handful of assets with fat-tailed
        # (large single-day, e.g. earnings) returns can push delta to its 1.0 ceiling, which
        # shrinks ALL cross-correlation to zero -- flattering for a concentrated stock portfolio
        # and worth disclosing rather than hiding behind a single "risk model" number.
        cov_raw = np.atleast_2d(np.cov(X, rowvar=False, ddof=0))  # np.cov collapses to 0-d for N=1
        vol_annual_unshrunk = math.sqrt(max(float(w @ cov_raw @ w), 0.0) * TRADING_DAYS_YEAR)

        port_ret = X @ w
        bench_ret = rets[benchmark].to_numpy()
        var_b = float(np.var(bench_ret, ddof=1))  # match np.cov's default ddof=1
        beta = float(np.cov(port_ret, bench_ret)[0, 1] / var_b) if var_b > 0 else float("nan")
        te_annual = float(np.std(port_ret - bench_ret, ddof=1) * math.sqrt(TRADING_DAYS_YEAR))

        sigma_p = math.sqrt(port_var_daily)
        if sigma_p > 0:
            mctr = (cov_shrunk @ w) / sigma_p
            pctr = (w * mctr) / sigma_p
        else:
            pctr = np.zeros_like(w)
        risk_by_name = dict(zip(tickers, pctr.tolist()))
        risk_by_sector: Dict[str, float] = {}
        for t, pc in zip(tickers, pctr):
            sec = sector_map.get(t, "Unknown")
            risk_by_sector[sec] = risk_by_sector.get(sec, 0.0) + float(pc)

        enb_weight = float(1.0 / np.sum(w ** 2))
        enb_risk = float(1.0 / np.sum(pctr ** 2)) if np.any(pctr) else float("nan")

        corr = rets[tickers].corr().to_numpy()
        iu = np.triu_indices_from(corr, k=1)
        avg_pairwise_corr = float(np.mean(corr[iu])) if len(iu[0]) else float("nan")

        eigvals = np.clip(np.linalg.eigvalsh(corr)[::-1], 0, None)
        top3_share = float(np.sum(eigvals[:3]) / np.sum(eigvals)) if np.sum(eigvals) > 0 else float("nan")

        result["windows"][f"{yrs}y"] = dict(
            n_days=int(len(rets)), start=str(rets.index[0].date()), end=str(rets.index[-1].date()),
            vol_annual=vol_annual, vol_annual_unshrunk=vol_annual_unshrunk,
            shrinkage_intensity=delta, beta_vs_benchmark=beta,
            tracking_error_annual=te_annual,
            risk_contribution_pct_by_name=risk_by_name,
            risk_contribution_pct_by_sector=risk_by_sector,
            effective_bets_weight=enb_weight, effective_bets_risk=enb_risk,
            avg_pairwise_correlation=avg_pairwise_corr, top3_pc_share_of_variance=top3_share,
        )
    return result


# ---------------------------------------------------------------------------
# 5. Stress tests
# ---------------------------------------------------------------------------

STRESS_WINDOWS_FIXED = {
    "GFC_2007_2009": ("2007-10-09", "2009-03-09"),
    "Q4_2018": ("2018-09-20", "2018-12-24"),
    "COVID_2020": ("2020-02-19", "2020-03-23"),
    "Bear_2022": ("2022-01-03", "2022-10-12"),
}
# Searched, not hard-coded: exact SPY peak/trough located within these bracket windows.
STRESS_WINDOWS_SEARCH = {
    "US_downgrade_Eurozone_2011": ("2011-07-01", "2011-10-31"),
    "China_deval_selloff_2015_2016": ("2015-07-01", "2016-02-29"),
    "Tariff_shock_2025": ("2025-01-01", "2025-06-30"),
}


def find_drawdown_window(series: pd.Series, search_start, search_end) -> Tuple[pd.Timestamp, pd.Timestamp, float]:
    """Exact peak date, trough date and drawdown of the worst decline inside [search_start,
    search_end], found by scanning for the running-maximum-relative minimum (standard drawdown
    definition), not assumed."""
    s = series.loc[pd.Timestamp(search_start):pd.Timestamp(search_end)].dropna()
    if len(s) < 2:
        raise ValueError("not enough data in search window")
    running_max = s.cummax()
    dd = s / running_max - 1
    trough = dd.idxmin()
    peak = s.loc[:trough].idxmax()
    return peak, trough, float(dd.loc[trough])


def stress_tests(
    weights: Dict[str, float],
    prices: Optional[pd.DataFrame] = None,
    missing: str = "exclude",
    proxies: Optional[Dict[str, str]] = None,
    cash_annual: float = 0.0,
    benchmark: str = "SPY",
) -> dict:
    """Daily-data replays of named historical crises (buy-and-hold from the window's start
    weights -- rebalance='none' -- so the result is the portfolio's actual peak-to-trough
    experience, not a rebalanced approximation). Reports the SPY result and the weight share
    covered by real vs proxy/cash data in each window."""
    prices = load_prices() if prices is None else prices
    spy = prices[benchmark]

    windows: Dict[str, Tuple[pd.Timestamp, pd.Timestamp]] = {}
    for name, (s, e) in STRESS_WINDOWS_FIXED.items():
        windows[name] = (pd.Timestamp(s), pd.Timestamp(e))
    found_dates = {}
    for name, (s, e) in STRESS_WINDOWS_SEARCH.items():
        peak, trough, dd = find_drawdown_window(spy, s, e)
        windows[name] = (peak, trough)
        found_dates[name] = dict(peak=str(peak.date()), trough=str(trough.date()), spy_drawdown=dd)

    out = {}
    for name, (w_start, w_end) in windows.items():
        path = portfolio_daily_path(
            weights, w_start, w_end, rebalance="none", missing=missing,
            proxies=proxies, cash_annual=cash_annual, prices=prices,
        )
        port_ret = float(path.wealth.iloc[-1] - 1.0)
        spy_ret = float(spy.loc[w_end] / spy.loc[w_start] - 1.0)
        entry = dict(
            start=str(w_start.date()), end=str(w_end.date()),
            portfolio_return=port_ret, portfolio_max_drawdown=max_drawdown(pd.concat([pd.Series([1.0]), path.wealth])),
            spy_return=spy_ret,
            missing_weight_share_avg=float(path.missing_share.mean()),
            synthetic_weight_share_avg=float(path.synthetic_share.mean()),
        )
        if name in found_dates:
            entry["window_located_by_search"] = found_dates[name]
        out[name] = entry
    return out


# ---------------------------------------------------------------------------
# 6. Stationary bootstrap simulation of outcomes
# ---------------------------------------------------------------------------

def _stationary_bootstrap_index_matrix(T: int, n_paths: int, horizon_days: int, mean_block: float, rng) -> np.ndarray:
    """Politis & Romano (1994) stationary bootstrap index draws, vectorised across paths.
    At each step, restart at a fresh uniform index with probability 1/mean_block, else continue
    (cyclically) from the previous index -- giving geometric(mean=mean_block) block lengths while
    keeping every source day equally likely to start a block (stationarity)."""
    p = 1.0 / mean_block
    idx = rng.integers(0, T, size=n_paths).astype(np.int32)
    out = np.empty((n_paths, horizon_days), dtype=np.int32)
    out[:, 0] = idx
    for t in range(1, horizon_days):
        restart = rng.random(n_paths) < p
        fresh = rng.integers(0, T, size=n_paths).astype(np.int32)
        idx = np.where(restart, fresh, (idx + 1) % T).astype(np.int32)
        out[:, t] = idx
    return out


def _path_stats(path_r: np.ndarray, horizon_years: float) -> dict:
    wealth = np.cumprod(1 + path_r, axis=1, dtype=np.float64)
    total_ret = wealth[:, -1] - 1.0
    ann_ret = np.sign(1 + total_ret) * np.abs(1 + total_ret) ** (1 / horizon_years) - 1.0
    running_max = np.maximum.accumulate(wealth, axis=1)
    dd = wealth / running_max - 1.0
    worst_dd = dd.min(axis=1)
    pct = lambda a, q: float(np.percentile(a, q))
    return dict(
        p_total_return_gt_0=float(np.mean(total_ret > 0)),
        total_return_pct=dict(p5=pct(total_ret, 5), p25=pct(total_ret, 25), p50=pct(total_ret, 50),
                               p75=pct(total_ret, 75), p95=pct(total_ret, 95)),
        annualized_return_pct=dict(p5=pct(ann_ret, 5), p25=pct(ann_ret, 25), p50=pct(ann_ret, 50),
                                    p75=pct(ann_ret, 75), p95=pct(ann_ret, 95)),
        p_drawdown_worse_than={
            "-10%": float(np.mean(worst_dd < -0.10)), "-15%": float(np.mean(worst_dd < -0.15)),
            "-20%": float(np.mean(worst_dd < -0.20)), "-30%": float(np.mean(worst_dd < -0.30)),
        },
        expected_worst_drawdown=float(worst_dd.mean()),
        median_worst_drawdown=float(np.median(worst_dd)),
    ), total_ret


def simulate_outcomes(
    source: Union[Dict[str, float], pd.Series],
    drift_annual: Optional[float],
    horizons: Sequence[float] = (1, 3, 5),
    n: int = 20000,
    method: str = "stationary_bootstrap",
    mean_block: float = 21,
    seed: int = 42,
    benchmark_returns: Optional[pd.Series] = None,
    benchmark_drift_annual: Optional[float] = None,
    start=None, end=None, rebalance: str = "M", missing: str = "proxy",
    proxies: Optional[Dict[str, str]] = None, prices: Optional[pd.DataFrame] = None,
) -> dict:
    """Politis-Romano stationary bootstrap of daily returns, recentred to `drift_annual` as a
    GEOMETRIC (compound) annual growth target (see recentre_to_geometric_drift for the exact
    conversion; pass drift_annual=None to bootstrap the raw historical series unrecentred).

    source: either a {ticker: weight} dict (built into a return series via portfolio_daily_path,
      using the LONGEST available history and `missing`/`proxies` to handle gaps -- default
      missing='proxy' so B2's disclosed proxy sensitivities feed the bootstrap pool, falling back
      to 'exclude' for any name not in `proxies`), or a ready-made pd.Series of daily returns.

    benchmark_returns: if given, bootstrapped JOINTLY with `source` (same resampled day-indices,
      drawn from the common overlap of both series) so co-movement is preserved, enabling
      P(source total return > benchmark total return) per horizon. benchmark_drift_annual
      defaults to `drift_annual` (i.e. same scenario applied to both legs).

    Returns dict with pool diagnostics and, per horizon (as 'Ny'): P(total return>0), P(beat
    benchmark) if applicable, percentiles (5/25/50/75/95) of total AND annualised return,
    P(max drawdown worse than -10/-15/-20/-30%), expected & median worst drawdown.
    """
    if method != "stationary_bootstrap":
        raise NotImplementedError("only method='stationary_bootstrap' is implemented")

    prices_df = load_prices() if prices is None else prices
    diagnostics: dict = {}
    if isinstance(source, dict):
        # "longest available history" = from the earliest date ANY held name has a price, not
        # necessarily the whole panel's start (e.g. RSP alone only goes back to 2003-05-01).
        s0 = start or min(prices_df[t].dropna().index[0] for t in source if t in prices_df.columns)
        e0 = end or prices_df.index[-1]
        path = portfolio_daily_path(source, s0, e0, rebalance=rebalance, missing=missing,
                                     proxies=proxies, prices=prices_df)
        raw_returns = path.daily_return
        diagnostics = dict(
            pool_missing_share_mean=float(path.missing_share.mean()),
            pool_synthetic_share_mean=float(path.synthetic_share.mean()),
            missing_mode=missing, proxies=dict(proxies or {}),
        )
    else:
        raw_returns = pd.Series(source).dropna()

    if benchmark_returns is not None:
        bench = pd.Series(benchmark_returns).dropna()
        common_idx = raw_returns.index.intersection(bench.index)
        raw_returns = raw_returns.loc[common_idx]
        bench = bench.loc[common_idx]
        bd = drift_annual if benchmark_drift_annual is None else benchmark_drift_annual
        adj_bench = bench if bd is None else recentre_to_geometric_drift(bench, bd)
        adj_bench = adj_bench.reindex(common_idx)
    else:
        adj_bench = None

    adj_returns = raw_returns if drift_annual is None else recentre_to_geometric_drift(raw_returns, drift_annual)

    rng = np.random.default_rng(seed)
    T = len(adj_returns)
    if T < 30:
        raise ValueError(f"return pool too short for bootstrap ({T} obs)")
    r_arr = adj_returns.to_numpy(dtype=np.float64).astype(np.float32)
    b_arr = adj_bench.to_numpy(dtype=np.float64).astype(np.float32) if adj_bench is not None else None

    out = dict(
        drift_annual=drift_annual, mean_block=mean_block, n_paths=n, seed=seed,
        pool_days=T, pool_start=str(adj_returns.index[0].date()), pool_end=str(adj_returns.index[-1].date()),
        diagnostics=diagnostics, horizons={},
    )
    for yrs in horizons:
        H = int(round(yrs * TRADING_DAYS_YEAR))
        idx_mat = _stationary_bootstrap_index_matrix(T, n, H, mean_block, rng)
        path_r = r_arr[idx_mat]
        stats, total_ret = _path_stats(path_r, yrs)
        if b_arr is not None:
            path_b = b_arr[idx_mat]
            _, total_ret_b = _path_stats(path_b, yrs)
            stats["p_beat_benchmark"] = float(np.mean(total_ret > total_ret_b))
        out["horizons"][f"{yrs}y"] = stats
        del idx_mat, path_r
    return out


def block_length_sensitivity(
    source: Union[Dict[str, float], pd.Series], drift_annual: Optional[float],
    horizons: Sequence[float] = (1, 3, 5), n: int = 20000, seed: int = 42,
    mean_blocks: Sequence[float] = (5, 21, 63), **kwargs,
) -> dict:
    """Runs simulate_outcomes at each of `mean_blocks` and returns all of them side by side --
    "report it, do not cherry-pick" (B2 spec Sec.4)."""
    return {f"block_{int(b)}": simulate_outcomes(source, drift_annual, horizons=horizons, n=n,
                                                  mean_block=b, seed=seed, **kwargs)
            for b in mean_blocks}


# ---------------------------------------------------------------------------
# 7. Allocation (equity sleeve / cash reserve) scenarios
# ---------------------------------------------------------------------------

def allocation_scenarios(
    equity_sleeve_returns: pd.Series,
    reserve_yield: float,
    mixes: Sequence[float] = (1.0, 0.8, 0.7, 0.6, 0.5),
    horizons: Sequence[float] = (1, 3, 5),
    n: int = 20000,
    mean_block: float = 21,
    seed: int = 42,
) -> dict:
    """Scenario analysis (NOT advice) for mixes of an equity sleeve vs a constant cash/T-bill
    reserve. Blending is ARITHMETIC (simple daily returns: e*r_equity + (1-e)*r_cash) per the B2
    spec ('arithmetic only'), deliberately not the geometric log-space recentring used elsewhere
    in this module. `equity_sleeve_returns` should already carry whatever scenario drift the
    caller wants (e.g. built with `recentre_to_geometric_drift` against an R1 Bear/Base/Bull
    geometric target, or `recentre_arithmetic` against R1's arithmetic-equivalent column) --
    this function does not recentre it again.

    Returns {'{equity%}/{reserve%}': simulate_outcomes(...) output} for each mix in `mixes`,
    giving the same drawdown-probability / P(profit) / return-percentile statistics.
    """
    reserve_daily = (1 + reserve_yield) ** (1 / TRADING_DAYS_YEAR) - 1
    eq = pd.Series(equity_sleeve_returns).dropna()
    results = {}
    for e in mixes:
        blended = e * eq + (1 - e) * reserve_daily
        sim = simulate_outcomes(blended, drift_annual=None, horizons=horizons, n=n,
                                 mean_block=mean_block, seed=seed)
        results[f"{round(e*100)}/{round((1-e)*100)}"] = sim
    return results


# ---------------------------------------------------------------------------
# 8. Empirical drawdown base rate (sanity check for the bootstrap)
# ---------------------------------------------------------------------------

def empirical_drawdown_frequency(
    price_series: pd.Series, horizons_years: Sequence[float] = (1, 3, 5),
    thresholds: Sequence[float] = (-0.15, -0.20),
) -> dict:
    """Overlapping-window empirical base rate, computed directly from actual daily history (no
    resampling): for every possible start day, what fraction of the following `horizon` years had
    a max drawdown worse than each threshold? Windows overlap heavily (consecutive start days
    share almost all their data), so this is NOT `n_windows` independent observations -- roughly
    `len(series)/horizon_days` independent non-overlapping stretches are available, given
    alongside as `n_independent_approx`. A sanity check for the bootstrap, not a replacement."""
    s = price_series.dropna()
    arr = s.to_numpy(dtype=float)
    out = {}
    for yrs in horizons_years:
        H = int(round(yrs * TRADING_DAYS_YEAR))
        if len(arr) <= H:
            continue
        windows = np.lib.stride_tricks.sliding_window_view(arr, H + 1)  # (n_windows, H+1)
        running_max = np.maximum.accumulate(windows, axis=1)
        worst = (windows / running_max - 1).min(axis=1)
        entry = dict(n_windows=int(len(worst)), n_independent_approx=int(len(arr) / H))
        for t in thresholds:
            entry[f"p_worse_than_{abs(int(round(t*100)))}pct"] = float(np.mean(worst < t))
        out[f"{yrs}y"] = entry
    return out
