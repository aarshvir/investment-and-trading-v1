"""b1_common.py - shared paths, calendar, statistics helpers for the B1 point-in-time backtest engine.

Owner: agent B1. Read-only use of other agents' data files (v4/data/d1_*, d2_*, d3_*, r3_*).
"""
from __future__ import annotations

import datetime as dt
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments")
V4 = PROJECT / "v4"
DATA = V4 / "data"
OUT = V4 / "outputs"
CODE = V4 / "code"
LEGACY = PROJECT / "equity_project"
CACHE = Path(r"C:\Users\user\eqv4\cache\b1")
CACHE.mkdir(parents=True, exist_ok=True)

LIVE_DATE = pd.Timestamp("2026-09-25")
# Headline window starts 2012-01 (lead instruction 2026-09-26 after D3: TTM coverage 66% in 2010, 91% in 2011,
# >=96.7% from 2012; SUE >=89.6% from 2012). 2010-11 is reported only as an exploratory extension.
FIRST_FORMATION = pd.Timestamp("2011-12-30")   # first signal month-end -> first return month 2012-01
EXPLORATORY_FIRST_FORMATION = pd.Timestamp("2009-12-31")
WINSOR_Q = (0.01, 0.99)     # per-month cross-sectional winsorisation of fundamental ratio metrics before ranking
LAST_RETURN_ME = pd.Timestamp("2026-08-31")    # last complete return month
COST_BPS = 10.0

PENDING_DEAL_EXCLUDE = ["WBD", "KVUE", "TECH", "AES", "NSC", "D"]   # D4 report: pending takeover targets

# ---------------------------------------------------------------- pre-registered metric definitions
# (name, family, higher_is_better, financial_missing)
METRICS = [
    ("gp_a", "Q", True, True),
    ("roe", "Q", True, False),
    ("ocf_a", "Q", True, False),
    ("accruals", "Q", False, True),
    ("leverage", "Q", False, True),
    ("asset_growth", "Q", False, False),
    ("net_issuance", "Q", False, False),
    ("ep", "V", True, False),
    ("fcfp", "V", True, False),
    ("ebit_ev", "V", True, True),
    ("bp", "V", True, False),
    ("mom_12_1", "M", True, False),
    ("sue", "S", True, False),
]
FAMILIES = ["Q", "V", "M", "S"]
FAMILY_METRICS = {f: [m for m, fam, _, _ in METRICS if fam == f] for f in FAMILIES}
MIN_SECTOR_N = 5            # pool sectors with < 5 names
FAMILY_MIN_SHARE = 0.5      # >= 50% of the family's metrics present
COMPOSITE_MIN_FAMILIES = 3  # require >= 3 of 4 families


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_meta(path: Path, meta: dict):
    path = Path(path)
    mp = path.with_name(path.name.rsplit(".", 1)[0] + ".meta.json")
    meta = dict(meta)
    meta.setdefault("agent", "b1")
    meta["written_utc"] = utcnow()
    mp.write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")


def month_end_days(days: pd.DatetimeIndex) -> pd.DatetimeIndex:
    """last trading day of each calendar month present in `days`"""
    s = pd.Series(days, index=days)
    me = s.groupby(days.to_period("M")).max()
    return pd.DatetimeIndex(me.values)


# ---------------------------------------------------------------- statistics
def max_drawdown(r: pd.Series) -> float:
    w = (1 + r.fillna(0)).cumprod()
    w = pd.concat([pd.Series([1.0]), w.reset_index(drop=True)])
    return float((w / w.cummax() - 1).min())


def cagr(r: pd.Series, periods: int = 12) -> float:
    r = r.dropna()
    if len(r) == 0:
        return float("nan")
    return float((1 + r).prod() ** (periods / len(r)) - 1)


def nw_mean_test(x, lags: int = 3) -> dict:
    """Newey-West (Bartlett) t-stat of the mean of x; returns mean, se, t, 95% CI (monthly units)"""
    x = np.asarray(pd.Series(x).dropna(), dtype=float)
    n = len(x)
    if n < 5:
        return {"n": n, "mean": float("nan"), "se": float("nan"), "t": float("nan"), "ci95": [float("nan")] * 2}
    mu = x.mean()
    e = x - mu
    s = e @ e / n
    for l in range(1, lags + 1):
        s += 2 * (1 - l / (lags + 1)) * (e[l:] @ e[:-l]) / n
    se = math.sqrt(s / n)
    return {"n": n, "mean": float(mu), "se": float(se), "t": float(mu / se) if se > 0 else float("nan"),
            "ci95": [float(mu - 1.96 * se), float(mu + 1.96 * se)]}


def wilson(k, n, z: float = 1.96):
    if n is None or n <= 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (float(c - h), float(c + h))


def rolling_excess_positive(r: pd.Series, b: pd.Series, window: int) -> dict:
    df = pd.concat([r, b], axis=1).dropna()
    if len(df) < window:
        return {"n_windows": 0, "share_positive": float("nan")}
    lr = np.log1p(df.iloc[:, 0]).rolling(window).sum()
    lb = np.log1p(df.iloc[:, 1]).rolling(window).sum()
    d = (np.expm1(lr) - np.expm1(lb)).dropna()
    return {"n_windows": int(len(d)), "share_positive": float((d > 0).mean()),
            "median_excess": float(d.median()), "p10_excess": float(d.quantile(0.1)),
            "p90_excess": float(d.quantile(0.9))}


def perf_block(r: pd.Series, rf: pd.Series | None = None) -> dict:
    r = r.dropna()
    out = {"n_months": int(len(r)), "start": str(r.index.min().date()) if len(r) else None,
           "end": str(r.index.max().date()) if len(r) else None,
           "cagr": cagr(r), "vol": float(r.std(ddof=1) * math.sqrt(12)), "mdd_monthly": max_drawdown(r)}
    if rf is not None:
        ex = (r - rf.reindex(r.index)).dropna()
        out["sharpe"] = float(ex.mean() * 12 / (r.std(ddof=1) * math.sqrt(12))) if len(ex) else float("nan")
    return out


def relative_block(r: pd.Series, b: pd.Series, nw_lags: int = 3) -> dict:
    df = pd.concat([r.rename("r"), b.rename("b")], axis=1).dropna()
    ex = df.r - df.b
    te = float(ex.std(ddof=1) * math.sqrt(12))
    nw = nw_mean_test(ex, nw_lags)
    out = {"n_months": int(len(df)), "cagr_strategy": cagr(df.r), "cagr_benchmark": cagr(df.b),
           "excess_cagr": cagr(df.r) - cagr(df.b), "mean_monthly_excess": float(ex.mean()),
           "ann_mean_excess": float(ex.mean() * 12), "tracking_error": te,
           "information_ratio": float(ex.mean() * 12 / te) if te > 0 else float("nan"),
           "nw_t": nw["t"], "nw_se_monthly": nw["se"],
           "ci95_ann_mean_excess": [nw["ci95"][0] * 12, nw["ci95"][1] * 12],
           "share_months_beating": float((ex > 0).mean())}
    for w in (12, 36, 60):
        out[f"rolling_{w}m"] = rolling_excess_positive(df.r, df.b, w)
    return out


def calendar_year_table(rets: dict[str, pd.Series]) -> pd.DataFrame:
    df = pd.DataFrame(rets)
    return (1 + df).groupby(df.index.year).prod() - 1


def subperiods(r: pd.Series, b: pd.Series, periods=(("2010-2014", "2010", "2014"), ("2015-2019", "2015", "2019"),
                                                     ("2020-2026", "2020", "2026"))) -> dict:
    out = {}
    for name, a, z in periods:
        rr = r.loc[a:z]
        bb = b.loc[a:z]
        df = pd.concat([rr, bb], axis=1).dropna()
        if len(df) < 6:
            continue
        out[name] = {"cagr": cagr(df.iloc[:, 0]), "bench_cagr": cagr(df.iloc[:, 1]),
                     "excess_cagr": cagr(df.iloc[:, 0]) - cagr(df.iloc[:, 1]),
                     "nw_t": nw_mean_test(df.iloc[:, 0] - df.iloc[:, 1])["t"], "n": int(len(df))}
    return out


def to_jsonable(o):
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if (o is None or not np.isfinite(o)) else round(float(o), 6)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (pd.Timestamp, dt.date)):
        return str(o.date()) if isinstance(o, pd.Timestamp) else str(o)
    if isinstance(o, pd.DataFrame):
        return to_jsonable(o.reset_index().to_dict(orient="records"))
    if isinstance(o, pd.Series):
        return to_jsonable(o.to_dict())
    return o
