"""r3_french_lib.py - shared helpers for agent R3 (evidence base).

* download_french(name): fetch a Kenneth French Data Library CSV zip into CACHE (re-uses cache).
* parse_french_csv(path): split a French CSV into {section_title: DataFrame}; monthly sections are
  indexed by month-end Timestamp, annual sections by int year. Values are left in the file's units
  (percent for returns); -99.99 / -999 are converted to NaN.
* perf_stats(r): summary statistics for a monthly return (or active-return) series in DECIMAL units.
"""
from __future__ import annotations

import io
import json
import re
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import requests

PROJECT = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments")
V4 = PROJECT / "v4"
DATA = V4 / "data"
OUT = V4 / "outputs"
CACHE = Path(r"C:\Users\user\eqv4\cache\r3")
CACHE.mkdir(parents=True, exist_ok=True)
FRENCH_FTP = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"
FRENCH_HOME = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html"
UA = {"User-Agent": "PersonalEquityResearch research-admin@personal-research.org"}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def download_french(zip_name: str, refresh: bool = False) -> Path:
    """Download <zip_name> from the French FTP folder into CACHE; return path of the extracted CSV."""
    zpath = CACHE / zip_name
    if refresh or not zpath.exists():
        for attempt in range(4):
            try:
                resp = requests.get(FRENCH_FTP + zip_name, headers=UA, timeout=60)
                resp.raise_for_status()
                zpath.write_bytes(resp.content)
                break
            except Exception:  # noqa: BLE001 - retry with backoff
                if attempt == 3:
                    raise
                time.sleep(2 ** attempt)
        time.sleep(0.6)  # politeness
    with zipfile.ZipFile(zpath) as zf:
        member = [m for m in zf.namelist() if m.lower().endswith(".csv")][0]
        out = CACHE / "unz" / member
        out.parent.mkdir(exist_ok=True)
        out.write_bytes(zf.read(member))
    return out


def file_header(path: Path, n: int = 3) -> str:
    """First n non-empty lines (used to record the CRSP vintage in meta files)."""
    lines = [ln.strip() for ln in path.read_text(encoding="latin-1").splitlines() if ln.strip()]
    return " | ".join(lines[:n])


_ROW = re.compile(r"^\s*(\d{4}|\d{6})\s*,")


def parse_french_csv(path: Path) -> dict[str, pd.DataFrame]:
    """Parse every table in a French CSV. Section title = nearest non-empty non-data line above the header."""
    lines = path.read_text(encoding="latin-1").splitlines()
    sections: dict[str, pd.DataFrame] = {}
    i, last_text = 0, "UNTITLED"
    while i < len(lines):
        ln = lines[i]
        if ln.startswith(","):  # header row
            cols = [c.strip() for c in ln.split(",")[1:]]
            rows, idx = [], []
            j = i + 1
            while j < len(lines) and _ROW.match(lines[j]):
                parts = [p.strip() for p in lines[j].split(",")]
                idx.append(parts[0])
                rows.append([float(p) if p not in ("",) else np.nan for p in parts[1: len(cols) + 1]])
                j += 1
            if rows:
                df = pd.DataFrame(rows, columns=cols)
                df = df.mask(df.isin([-99.99, -999.0]))
                if len(idx[0]) == 6:
                    per = pd.PeriodIndex([f"{s[:4]}-{s[4:]}" for s in idx], freq="M")
                    df.index = per.to_timestamp(how="end").normalize()
                    df.index.name = "month_end"
                else:
                    df.index = pd.Index([int(s) for s in idx], name="year")
                title = last_text.strip()
                key, k = title, 2
                while key in sections:  # keep duplicate titles distinct
                    key = f"{title} #{k}"
                    k += 1
                sections[key] = df
            i = j
            continue
        if ln.strip() and not _ROW.match(ln):
            last_text = ln
        i += 1
    return sections


def get_section(sections: dict[str, pd.DataFrame], pattern: str) -> pd.DataFrame:
    hits = [k for k in sections if re.search(pattern, k, flags=re.I)]
    if not hits:
        raise KeyError(f"no section matching {pattern!r}; have {list(sections)}")
    return sections[hits[0]]


def rolling_compound(r: pd.Series, window: int) -> pd.Series:
    """Rolling compounded return over `window` months (NaN for incomplete windows)."""
    lr = np.log1p(r)
    return np.expm1(lr.rolling(window).sum())


def max_drawdown(r: pd.Series) -> tuple[float, str, str]:
    """Max drawdown of cumulative (1+r) wealth starting at 1.0; returns (mdd, peak_date, trough_date).
    peak_date = 'start' when the peak is the initial 1.0 (drawdown began in the first month)."""
    w = (1 + r).cumprod()
    peak = w.cummax().clip(lower=1.0)
    dd = w / peak - 1
    trough = dd.idxmin()
    pk_level = peak.loc[trough]
    if pk_level <= 1.0 + 1e-12:
        peak_date = "start"
    else:
        before = w.loc[:trough]
        peak_date = str(before[np.isclose(before, pk_level)].index[-1].date())
    return float(dd.min()), peak_date, str(pd.Timestamp(trough).date())


def perf_stats(r: pd.Series) -> dict:
    """r: monthly returns in decimals (long-short factor returns or active returns)."""
    r = r.dropna()
    n = len(r)
    mu, sd = r.mean(), r.std(ddof=1)
    r12, r36, r60 = rolling_compound(r, 12).dropna(), rolling_compound(r, 36).dropna(), rolling_compound(r, 60).dropna()
    cal = (1 + r).groupby(r.index.year).prod() - 1
    cal_counts = r.groupby(r.index.year).size()
    cal = cal[cal_counts == 12]
    mdd, pk, tr = max_drawdown(r)
    return {
        "start": str(r.index[0].date()), "end": str(r.index[-1].date()), "n_months": n,
        "ann_mean_arith": mu * 12,
        "ann_geo": float((1 + r).prod() ** (12 / n) - 1),
        "ann_vol": sd * np.sqrt(12),
        "sharpe_or_ir": (mu / sd) * np.sqrt(12) if sd > 0 else np.nan,
        "t_stat": mu / (sd / np.sqrt(n)) if sd > 0 else np.nan,
        "max_drawdown": mdd, "mdd_peak": pk, "mdd_trough": tr,
        "pct_months_pos": float((r > 0).mean()),
        "pct_roll12_pos": float((r12 > 0).mean()), "n_roll12": len(r12),
        "pct_roll36_pos": float((r36 > 0).mean()) if len(r36) else np.nan, "n_roll36": len(r36),
        "pct_roll60_pos": float((r60 > 0).mean()) if len(r60) else np.nan, "n_roll60": len(r60),
        "pct_calyears_pos": float((cal > 0).mean()) if len(cal) else np.nan, "n_calyears": len(cal),
        "worst_12m": float(r12.min()) if len(r12) else np.nan,
        "worst_36m": float(r36.min()) if len(r36) else np.nan,
    }


def write_meta(path: Path, meta: dict) -> Path:
    """Sidecar <stem>.meta.json next to the dataset (e.g. r3_ff_factors_monthly.meta.json)."""
    meta = {"agent": "r3", "dataset": Path(path).name, "built_utc": utc_now(), **meta}
    mpath = Path(path).parent / (Path(path).stem + ".meta.json")
    mpath.write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
    return mpath
