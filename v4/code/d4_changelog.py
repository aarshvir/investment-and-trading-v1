"""d4_changelog.py - change log: legacy v3 snapshot (equity_project/info.json + est_all.pkl, Yahoo as of 2026-09-24)
vs fresh D4 snapshot (Yahoo as of the 2026-09-25 close) for the 14 v3 portfolio names.

Fields: price, forwardEps, epsCurrentYear, eps FY0/FY1 consensus (eps_trend 'current'), target mean, # analysts,
recommendation mean, Yahoo forwardPE vs fresh NTM P/E. Estimate changes > 2% are flagged.
Output: v4/data/d4_changelog_v3.csv (+ .meta.json)
"""
from __future__ import annotations

import json
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import DATA, LEGACY, V3_PORTFOLIO, utc_now_iso, write_meta  # noqa: E402


def tr(df, per, col="current"):
    try:
        return float(df.loc[per, col])
    except (KeyError, TypeError, ValueError, AttributeError):
        return np.nan


def ch(a, b):
    return (b / a - 1) if (pd.notna(a) and pd.notna(b) and a != 0) else np.nan


def main():
    I = json.load(open(LEGACY / "info.json", encoding="utf-8"))
    E = pickle.load(open(LEGACY / "est_all.pkl", "rb"))
    s = pd.read_parquet(DATA / "d4_live_snapshot.parquet").set_index("ticker")
    rows = []
    for tk in V3_PORTFOLIO:
        li, le = I.get(tk, {}), E.get(tk, {})
        f = s.loc[tk] if tk in s.index else None
        ltr = le.get("trend") if isinstance(le, dict) else None
        r = {"ticker": tk,
             "legacy_regularMarketTime_utc": pd.to_datetime(li.get("regularMarketTime"), unit="s", utc=True).strftime("%Y-%m-%dT%H:%M:%SZ") if li.get("regularMarketTime") else None,
             "fresh_regularMarketTime_utc": f["regularMarketTime_utc"] if f is not None else None,
             "legacy_price": li.get("currentPrice"), "fresh_price": f["price"] if f is not None else np.nan,
             "legacy_forwardEps": li.get("forwardEps"), "fresh_forwardEps": f["forwardEps"] if f is not None else np.nan,
             "legacy_epsCurrentYear": li.get("epsCurrentYear"), "fresh_epsCurrentYear": f["epsCurrentYear"] if f is not None else np.nan,
             "legacy_trend_fy0": tr(ltr, "0y"), "fresh_trend_fy0": f["eps_trend_fy0_current"] if f is not None else np.nan,
             "legacy_trend_fy1": tr(ltr, "+1y"), "fresh_trend_fy1": f["eps_trend_fy1_current"] if f is not None else np.nan,
             "legacy_trend_q0": tr(ltr, "0q"), "fresh_trend_q0": f["eps_trend_q0_current"] if f is not None else np.nan,
             "fresh_trend_fy1_7dago": f["eps_trend_fy1_7daysAgo"] if f is not None else np.nan,
             "legacy_targetMean": li.get("targetMeanPrice"), "fresh_targetMean": f["target_mean"] if f is not None else np.nan,
             "legacy_nAnalysts": li.get("numberOfAnalystOpinions"), "fresh_nAnalysts": f["n_analysts_targets"] if f is not None else np.nan,
             "legacy_recMean": li.get("recommendationMean"), "fresh_recMean": f["rec_mean"] if f is not None else np.nan,
             "legacy_forwardPE": li.get("forwardPE"), "fresh_forwardPE": f["forwardPE"] if f is not None else np.nan,
             "fresh_pe_fy0": f["pe_fy0"] if f is not None else np.nan, "fresh_pe_ntm": f["pe_ntm"] if f is not None else np.nan,
             "fresh_pe_ntm_qaware": f["pe_ntm_qaware"] if f is not None else np.nan,
             "fresh_pe_fy1": f["pe_fy1"] if f is not None else np.nan,
             "fresh_fy0_end": str(f["fy0_end"])[:10] if f is not None else None,
             "fresh_f_fy0_remaining": f["f_fy0_remaining"] if f is not None else np.nan,
             "fresh_last_report_date": f["last_report_date"] if f is not None else None,
             "fresh_next_earnings_date": f["next_earnings_date"] if f is not None else None,
             "legacy_prevName": li.get("prevName"), "fresh_prevName": f["y_prevName"] if f is not None else None}
        for a, b, lab in [("legacy_price", "fresh_price", "chg_price"), ("legacy_forwardEps", "fresh_forwardEps", "chg_forwardEps"),
                          ("legacy_epsCurrentYear", "fresh_epsCurrentYear", "chg_epsCurrentYear"),
                          ("legacy_trend_fy0", "fresh_trend_fy0", "chg_eps_fy0"), ("legacy_trend_fy1", "fresh_trend_fy1", "chg_eps_fy1"),
                          ("legacy_targetMean", "fresh_targetMean", "chg_targetMean")]:
            r[lab] = ch(r[a], r[b])
        flags = [lab for lab in ["chg_forwardEps", "chg_epsCurrentYear", "chg_eps_fy0", "chg_eps_fy1"] if pd.notna(r[lab]) and abs(r[lab]) > 0.02]
        if pd.notna(r["chg_targetMean"]) and abs(r["chg_targetMean"]) > 0.02:
            flags.append("chg_targetMean")
        r["flags_gt2pct"] = ";".join(flags)
        r["pe_ntm_vs_legacy_fwdPE"] = ch(r["legacy_forwardPE"], r["fresh_pe_ntm"])
        rows.append(r)
    d = pd.DataFrame(rows)
    out = DATA / "d4_changelog_v3.csv"
    d.to_csv(out, index=False)
    write_meta(out, {"description": "legacy (2026-09-24) vs fresh (2026-09-25 close) Yahoo fields for 14 v3 names",
                     "inputs": ["equity_project/info.json", "equity_project/est_all.pkl", "v4/data/d4_live_snapshot.parquet"],
                     "retrieval_utc": utc_now_iso(), "rows": int(len(d)), "columns": list(d.columns),
                     "caveats": ["Legacy est_all 'trend' = yfinance eps_trend at legacy pull time (not stamped per ticker).",
                                 "Change flags use 2% threshold on consensus EPS/target fields."]})
    pd.set_option("display.width", 250)
    print(d[["ticker", "legacy_price", "fresh_price", "chg_price", "chg_forwardEps", "chg_eps_fy0", "chg_eps_fy1", "chg_targetMean", "flags_gt2pct"]].round(4).to_string())


if __name__ == "__main__":
    main()
