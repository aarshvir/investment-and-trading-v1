"""b1x_common.py - shared utilities for agent B1X (independent replication of the primary backtest).

Independence note: this module reads DATA outputs of D1/D2/D3 (shared upstream inputs, same as B1 uses) and
the D1 *SIC->sector classification function* d1_sic_sector_rules.sic_to_sector (a deterministic lookup table,
not backtest/factor logic) so that both implementations are sector-neutral within the SAME sector definitions,
per the task spec ("sector-neutral percentiles within D1's SIC-derived sectors"). No b1_*.py file is imported
or read anywhere in this codebase.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

V4 = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4")
DATA = V4 / "data"
OUT = V4 / "outputs"
CODE = V4 / "code"

sys.path.insert(0, str(CODE))
from d1_sic_sector_rules import sic_to_sector  # noqa: E402  (D1 data-classification helper, not b1_*)

BACKTEST_START_MONTH = "2010-01"
BACKTEST_END_MONTH = "2026-08"
HEADLINE_START_MONTH = "2012-01"  # lead + d3_report.md: fundamental coverage >=~97% (mapped) only from 2012
LIVE_DATE = "2026-09-25"
ONE_WAY_COST_BPS = 10.0
BRK_B_CLASS_CONVERSION = 1500.0  # d3_report.md sec.5.6: BRK shares/EPS are Class-A equivalents


def month_end_index():
    """NYSE month-end trading days from d2_adjclose, restricted to calendar months [2010-01, 2026-08]."""
    idx = pd.read_parquet(DATA / "d2_adjclose.parquet", columns=["SPY"]).index
    per = idx.to_period("M")
    me = idx.to_series().groupby(per).max()
    keep = (me.index >= pd.Period(BACKTEST_START_MONTH, "M")) & (me.index <= pd.Period(BACKTEST_END_MONTH, "M"))
    me = me[keep]
    return pd.DatetimeIndex(sorted(me.values))


def sic_sector_map():
    """CIK -> (sic, sector, basis) from D3's company meta (SEC-sourced SIC), via D1's sector rule function."""
    cm = pd.read_csv(DATA / "d3_company_meta.csv", dtype={"cik": "int64"})
    cm["sector"], cm["sector_basis"] = zip(*cm["sic"].map(lambda s: sic_to_sector(s)))
    return cm.set_index("cik")[["sic", "sector", "sector_basis"]]


def membership_spells():
    """Temporary membership source per launch instructions: D1's own PIT files were not yet present at build
    time (polled; see b1x_report.md). Falls back to D2's labelled reconstruction (d2_universe_spells.csv)."""
    d1_files = [DATA / "d1_membership_monthly.parquet", DATA / "d1_cik_map.csv", DATA / "d1_sector_map.csv"]
    if all(p.exists() for p in d1_files):
        return "d1", d1_files
    sp = pd.read_csv(DATA / "d2_universe_spells.csv", parse_dates=["start", "end_excl"])
    return "d2_universe_spells_fallback", sp


def split_factor_after(splits: pd.DataFrame, tickers, month_ends):
    """cum_split_factor_after(ticker, t) = product of split_ratio for all splits with date > t (through the
    end of the data, 2026-09-25). d2_close is split-adjusted to the 2026-09-25 basis; D3 shares_out is on the
    as-of-t basis, so market_cap(t) = d2_close(t) * shares_out(t) * cum_split_factor_after(t)."""
    s = splits[splits["ticker"].isin(tickers)].copy()
    out = {}
    for tkr, g in s.groupby("ticker"):
        dates = g["date"].values
        ratios = g["split_ratio"].values
        order = np.argsort(dates)
        dates, ratios = dates[order], ratios[order]
        # cumulative product from the END backwards: factor_after(t) = prod(ratios[dates > t])
        rev_cum = np.cumprod(ratios[::-1])[::-1]
        # factor_after(t) uses splits strictly after t -> for a given month_end grid, searchsorted
        me = np.asarray(month_ends, dtype="datetime64[ns]")
        pos = np.searchsorted(dates, me, side="right")  # number of splits with date <= t
        n = len(dates)
        factor = np.where(pos < n, rev_cum[np.minimum(pos, n - 1)], 1.0)
        factor = np.where(pos == n, 1.0, factor)
        out[tkr] = pd.Series(factor, index=pd.DatetimeIndex(me))
    return out


def winsorize_by_month(df: pd.DataFrame, col: str, month_col: str = "month_end",
                        lo: float = 0.01, hi: float = 0.99) -> pd.Series:
    """Cross-sectional winsorisation at the 1st/99th percentile within each month (lead instruction, since
    D3 flags early-XBRL scale errors and TTM discontinuities at IPOs/spin-offs/reverse splits: d3_report.md
    checks (e))."""
    def _clip(s):
        lo_v, hi_v = s.quantile([lo, hi])
        return s.clip(lo_v, hi_v)
    return df.groupby(month_col)[col].transform(_clip)


def sector_neutral_percentile(df: pd.DataFrame, value_col: str, month_col: str, sector_col: str) -> pd.Series:
    """percentile rank in (0,1], ascending (higher value = higher percentile), within (month, sector)."""
    return df.groupby([month_col, sector_col])[value_col].rank(pct=True, method="average")


def cagr(monthly_returns: pd.Series) -> float:
    r = monthly_returns.dropna()
    if len(r) == 0:
        return np.nan
    total = (1 + r).prod()
    years = len(r) / 12.0
    return total ** (1 / years) - 1 if years > 0 else np.nan


def ann_vol(monthly_returns: pd.Series) -> float:
    r = monthly_returns.dropna()
    return r.std(ddof=1) * np.sqrt(12) if len(r) > 1 else np.nan


def max_drawdown(monthly_returns: pd.Series) -> float:
    r = monthly_returns.dropna()
    if len(r) == 0:
        return np.nan
    wealth = (1 + r).cumprod()
    peak = wealth.cummax()
    dd = wealth / peak - 1
    return dd.min()


def tstat_mean(x: pd.Series) -> float:
    x = x.dropna()
    if len(x) < 2:
        return np.nan
    return x.mean() / (x.std(ddof=1) / np.sqrt(len(x)))


def write_json(path: Path, obj):
    def default(o):
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return None if np.isnan(o) else float(o)
        if isinstance(o, (np.bool_,)):
            return bool(o)
        if isinstance(o, (pd.Timestamp,)):
            return o.strftime("%Y-%m-%d")
        raise TypeError(str(type(o)))
    path.write_text(json.dumps(obj, indent=2, default=default))
