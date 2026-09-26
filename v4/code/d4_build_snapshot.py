"""d4_build_snapshot.py - build v4/data/d4_live_snapshot.parquet (one row per S&P 500 constituent) from the cached
Yahoo pulls (CACHE/yahoo/*.pkl), including the NTM calendarization.

NTM calendarization rule (documented in d4_report.md):
  FY0 = the current *unreported* fiscal year = the period Yahoo labels '0y' in earningsTrend. Its end date is taken
        from the raw earningsTrend 'endDate' of period '0y' (primary; this is exactly the period the eps_fy0 consensus
        refers to). Cross-check: info.nextFiscalYearEnd (= info.lastFiscalYearEnd + 1y, i.e. end of the fiscal year
        after the last *reported* one) must agree within 20 days, and info.mostRecentQuarter must lie in
        (lastFiscalYearEnd, FY0_end]. Disagreements are flagged (fy_check != 'ok').
        Fallback if endDate missing: nextFiscalYearEnd.
  f   = fraction of FY0 remaining at 2026-09-25 = clip((FY0_end - 2026-09-25) / (FY1_end - FY0_end), 0, 1)
        (FY1_end from '+1y' endDate; 365.25 days if missing). f = 0 when FY0 has ended but is not yet reported.
  EPS_NTM = f * EPS_FY0 + (1 - f) * EPS_FY1       (EPS_FY0/FY1 = earnings_estimate '0y'/'+1y' avg)
  REV_NTM = f * REV_FY0 + (1 - f) * REV_FY1
  Diagnostic 'quarter-aware' NTM: (EPS_FY0 - reported EPS of FY0 quarters already reported) + EPS_FY1 * q_rep/4,
        where FY0 quarters come from earnings_history (quarter end > lastFiscalYearEnd + 20d). Not the primary.
"""
from __future__ import annotations

import datetime as dt
import math
import pickle
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import ASOF, CACHE, DATA, utc_now_iso, write_meta  # noqa: E402

NY = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
YCACHE = CACHE / "yahoo"
ASOF_TS = pd.Timestamp(ASOF)

INFO_FIELDS = ["regularMarketPrice", "currentPrice", "regularMarketPreviousClose", "regularMarketTime",
               "marketCap", "nonDilutedMarketCap", "sharesOutstanding", "impliedSharesOutstanding", "floatShares",
               "enterpriseValue", "totalDebt", "totalCash", "ebitda", "freeCashflow", "operatingCashflow",
               "totalRevenue", "netIncomeToCommon", "trailingEps", "forwardEps", "trailingPE", "forwardPE",
               "epsCurrentYear", "priceEpsCurrentYear", "epsForward", "epsTrailingTwelveMonths",
               "dividendRate", "dividendYield", "trailingAnnualDividendRate", "trailingAnnualDividendYield",
               "payoutRatio", "beta", "bookValue", "priceToBook", "returnOnEquity", "profitMargins",
               "revenueGrowth", "earningsGrowth", "numberOfAnalystOpinions", "recommendationMean",
               "recommendationKey", "targetMeanPrice", "targetHighPrice", "targetLowPrice", "targetMedianPrice",
               "currency", "financialCurrency", "quoteType", "exchange", "fullExchangeName", "longName",
               "shortName", "displayName", "prevName", "nameChangeDate", "sector", "industry", "country",
               "earningsTimestamp", "earningsTimestampStart", "earningsTimestampEnd", "isEarningsDateEstimate",
               "exDividendDate", "lastSplitDate", "lastSplitFactor", "marketState", "sharesShort",
               "heldPercentInsiders", "heldPercentInstitutions", "fullTimeEmployees", "ipoExpectedDate"]


def ep_date(x):
    """Yahoo fiscal-date epochs are midnight-UTC of the calendar date."""
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return pd.NaT
    try:
        return pd.Timestamp(dt.datetime.fromtimestamp(int(x), tz=UTC).date())
    except (ValueError, OverflowError, OSError, TypeError):
        return pd.NaT


def ep_ny(x):
    if x is None:
        return pd.NaT
    try:
        return pd.Timestamp(dt.datetime.fromtimestamp(int(x), tz=UTC).astimezone(NY))
    except (ValueError, OverflowError, OSError, TypeError):
        return pd.NaT


def g(df, row, col):
    try:
        if df is None or not isinstance(df, pd.DataFrame) or row not in df.index or col not in df.columns:
            return np.nan
        v = df.loc[row, col]
        return float(v) if v is not None and not (isinstance(v, float) and math.isnan(v)) else np.nan
    except (TypeError, ValueError):
        return np.nan


def fnum(v):
    try:
        if v is None:
            return np.nan
        v = float(v)
        return v if math.isfinite(v) else np.nan
    except (TypeError, ValueError):
        return np.nan


def safe_div(a, b):
    a, b = fnum(a), fnum(b)
    if np.isnan(a) or np.isnan(b) or b == 0:
        return np.nan
    return a / b


# Documented fiscal-calendar exceptions (verified 2026-09-25 against SEC primary sources).
FY0_OVERRIDES = {
    # ticker: (fy0_end to use, evidence)
    "HONA": ("2026-12-31", "SEC submissions fiscalYearEnd=1231 for Honeywell Aerospace Inc. (https://data.sec.gov/"
                           "submissions/CIK0002089271.json); Yahoo 0y endDate 2027-01-31 disagrees with the calendar FY and"
                           " with info.nextFiscalYearEnd 2026-12-31; spin-off stub periods make FY0 consensus unreliable"),
}
FYE_CHANGE_NOTES = {
    "AMCR": "FYE changed Jun-30 -> Dec-31 (8-K Item 5.03 filed 2026-05-06: https://www.sec.gov/Archives/edgar/data/1748790/"
            "000110465926055873/tm2613113d1_8k.htm); transition period 2026-07-01..2026-12-31; Yahoo 0y=Dec-2026 is a"
            " 12-month calendar-2026 consensus; info.nextFiscalYearEnd (2027-06-30) and SEC fiscalYearEnd (0630) are stale",
    "FDX": "FYE changed May-31 -> Dec-31 effective 2026-06-01 (8-K Item 2.02 filed 2026-07-21: https://www.sec.gov/Archives/"
           "edgar/data/1048911/000104891126000108/fdx-20260721.htm); 7-month transition period 2026-06-01..2026-12-31;"
           " Yahoo 0y=Dec-2026 (calendar-2026 consensus); info.nextFiscalYearEnd (2027-05-31) and SEC fiscalYearEnd stale",
    "FDXF": "FedEx Freight spun off 2026-06-01; FYE May-31 (10-K for FY ended 2026-05-31 filed 2026-08-05); Yahoo 0y still"
            " labels the already-reported FY2026 (endDate 2026-05-31) -> f=0, NTM = FY ending 2027-05-31",
}


def trend_end(raw, period):
    for it in raw or []:
        if it.get("period") == period and it.get("endDate"):
            return pd.Timestamp(it["endDate"])
    return pd.NaT


def build_row(rec: dict, uni_row: pd.Series) -> dict:
    tk = rec["ticker"]
    info = rec.get("info") or {}
    # HTTP 404 on a quoteSummary module = Yahoo has no such module for the ticker -> treat as NO_DATA, not an error
    errs = {k: ("NO_DATA(404): " + str(v) if ("HTTP Error 404" in str(v) and not str(v).startswith("NO_DATA")) else str(v))
            for k, v in (rec.get("errors") or {}).items()}
    rec = {**rec, "errors": errs}
    r = {"ticker": tk, "ticker_orig": uni_row["ticker_orig"], "name_wiki": uni_row["name"],
         "gics_sector": uni_row["gics_sector"], "gics_sub_industry": uni_row["gics_sub_industry"],
         "cik": uni_row["cik"], "retrieved_utc_start": rec.get("t_start_utc"),
         "retrieved_utc_end": rec.get("t_end_utc"),
         "fetch_errors": ";".join(f"{k}" for k, v in errs.items() if not v.startswith("NO_DATA")),
         "fetch_nodata": ";".join(f"{k}" for k, v in errs.items() if v.startswith("NO_DATA"))}
    for f in INFO_FIELDS:
        v = info.get(f)
        r["y_" + f] = v if (v is None or isinstance(v, (int, float, str, bool))) else str(v)
    # --- price & timestamps
    price = fnum(info.get("regularMarketPrice"))
    if np.isnan(price):
        price = fnum(info.get("currentPrice"))
    r["price"] = price
    rmt = info.get("regularMarketTime")
    rmt_ny = ep_ny(rmt) if isinstance(rmt, (int, float)) else pd.NaT
    r["regularMarketTime_utc"] = (rmt_ny.tz_convert(UTC).strftime("%Y-%m-%dT%H:%M:%SZ") if pd.notna(rmt_ny) else None)
    r["regularMarketDate_ny"] = rmt_ny.date().isoformat() if pd.notna(rmt_ny) else None
    for f in ["marketCap", "sharesOutstanding", "impliedSharesOutstanding", "enterpriseValue", "totalDebt",
              "totalCash", "ebitda", "freeCashflow", "operatingCashflow", "trailingEps", "forwardEps", "trailingPE",
              "forwardPE", "dividendRate", "trailingAnnualDividendYield", "beta", "totalRevenue",
              "epsCurrentYear", "priceEpsCurrentYear"]:
        r[f] = fnum(info.get(f))
    r["lastFiscalYearEnd"] = ep_date(info.get("lastFiscalYearEnd"))
    r["nextFiscalYearEnd"] = ep_date(info.get("nextFiscalYearEnd"))
    r["mostRecentQuarter"] = ep_date(info.get("mostRecentQuarter"))

    # --- estimates
    ee, re_, et, ev = rec.get("earnings_estimate"), rec.get("revenue_estimate"), rec.get("eps_trend"), rec.get("eps_revisions")
    for p, lab in [("0q", "q0"), ("+1q", "q1"), ("0y", "fy0"), ("+1y", "fy1")]:
        r[f"eps_{lab}"] = g(ee, p, "avg")
        r[f"eps_{lab}_low"] = g(ee, p, "low")
        r[f"eps_{lab}_high"] = g(ee, p, "high")
        r[f"eps_{lab}_n"] = g(ee, p, "numberOfAnalysts")
        r[f"eps_{lab}_yago"] = g(ee, p, "yearAgoEps")
        r[f"eps_{lab}_growth"] = g(ee, p, "growth")
        r[f"rev_{lab}"] = g(re_, p, "avg")
        r[f"rev_{lab}_low"] = g(re_, p, "low")
        r[f"rev_{lab}_high"] = g(re_, p, "high")
        r[f"rev_{lab}_n"] = g(re_, p, "numberOfAnalysts")
        r[f"rev_{lab}_yago"] = g(re_, p, "yearAgoRevenue")
        r[f"rev_{lab}_growth"] = g(re_, p, "growth")
        for c in ["current", "7daysAgo", "30daysAgo", "60daysAgo", "90daysAgo"]:
            r[f"eps_trend_{lab}_{c}"] = g(et, p, c)
        for c, lab2 in [("upLast7days", "up7"), ("upLast30days", "up30"), ("downLast7Days", "down7"),
                        ("downLast30days", "down30")]:
            r[f"eps_rev_{lab}_{lab2}"] = g(ev, p, c)
    raw = rec.get("earnings_trend_raw") or []
    r["q0_end"] = trend_end(raw, "0q")
    r["q1_end"] = trend_end(raw, "+1q")
    r["fy0_end_trend"] = trend_end(raw, "0y")
    r["fy1_end_trend"] = trend_end(raw, "+1y")
    r["eps_currency"] = (ee["currency"].iloc[0] if isinstance(ee, pd.DataFrame) and "currency" in ee.columns and len(ee) else None)

    # revisions (%): trend now vs 30d / 90d ago
    for lab in ["fy0", "fy1"]:
        now, d30, d90 = r[f"eps_trend_{lab}_current"], r[f"eps_trend_{lab}_30daysAgo"], r[f"eps_trend_{lab}_90daysAgo"]
        r[f"eps_{lab}_rev30_pct"] = (now / d30 - 1) if (d30 and not np.isnan(d30) and d30 > 0 and not np.isnan(now)) else np.nan
        r[f"eps_{lab}_rev90_pct"] = (now / d90 - 1) if (d90 and not np.isnan(d90) and d90 > 0 and not np.isnan(now)) else np.nan

    # --- fiscal calendar / NTM
    fy0_end = r["fy0_end_trend"] if pd.notna(r["fy0_end_trend"]) else r["nextFiscalYearEnd"]
    r["fy0_end_source"] = "earningsTrend.0y.endDate" if pd.notna(r["fy0_end_trend"]) else ("info.nextFiscalYearEnd" if pd.notna(r["nextFiscalYearEnd"]) else None)
    r["fy0_note"] = FYE_CHANGE_NOTES.get(tk)
    if tk in FY0_OVERRIDES:
        fy0_end = pd.Timestamp(FY0_OVERRIDES[tk][0])
        r["fy0_end_source"] = "manual_override(SEC evidence)"
        r["fy0_note"] = FY0_OVERRIDES[tk][1]
    fy1_end = r["fy1_end_trend"]
    r["fy0_end"] = fy0_end
    fylen = (fy1_end - fy0_end).days if (pd.notna(fy1_end) and pd.notna(fy0_end)) else 365.25
    if not fylen or fylen < 300 or fylen > 400:
        fylen = 365.25
    if pd.notna(fy0_end):
        rem = (fy0_end - ASOF_TS).days
        r["fy0_days_remaining"] = rem
        r["f_fy0_remaining"] = float(min(1.0, max(0.0, rem / fylen)))
        r["fy0_ended_unreported"] = bool(rem < 0)
        r["fye_month"] = int(fy0_end.month)
    else:
        r["fy0_days_remaining"] = np.nan
        r["f_fy0_remaining"] = np.nan
        r["fy0_ended_unreported"] = None
        r["fye_month"] = (int(r["lastFiscalYearEnd"].month) if pd.notna(r["lastFiscalYearEnd"]) else np.nan)
    # consistency checks among fiscal dates
    chk = []
    if pd.notna(r["fy0_end_trend"]) and pd.notna(r["nextFiscalYearEnd"]):
        d = abs((r["fy0_end_trend"] - r["nextFiscalYearEnd"]).days)
        r["fy0_end_diff_days"] = d
        if d > 20:
            chk.append(f"trend0y_vs_nextFYE_{d}d")
    else:
        r["fy0_end_diff_days"] = np.nan
        chk.append("missing_fy_dates")
    if pd.notna(r["mostRecentQuarter"]) and pd.notna(r["lastFiscalYearEnd"]) and pd.notna(fy0_end):
        if r["mostRecentQuarter"] < r["lastFiscalYearEnd"] - pd.Timedelta(days=5):
            chk.append("MRQ_before_LFY")
        if r["mostRecentQuarter"] > fy0_end + pd.Timedelta(days=10):
            chk.append("MRQ_after_FY0end")
    if pd.notna(r["lastFiscalYearEnd"]) and r["lastFiscalYearEnd"] > ASOF_TS:
        chk.append("LFY_in_future")
    if tk in FYE_CHANGE_NOTES:
        chk = [("documented_FYE_change_or_spin" if c.startswith("trend0y_vs_nextFYE") else c) for c in chk]
    if tk in FY0_OVERRIDES:
        chk = [("override_applied" if c.startswith("trend0y_vs_nextFYE") else c) for c in chk]
    r["fy_check"] = "ok" if not chk else ";".join(chk)
    q_rep = np.nan
    if pd.notna(r["mostRecentQuarter"]) and pd.notna(r["lastFiscalYearEnd"]):
        q_rep = int(round((r["mostRecentQuarter"] - r["lastFiscalYearEnd"]).days / 91.3))
    r["fy0_quarters_reported_mrq"] = q_rep

    f = r["f_fy0_remaining"]
    e0, e1 = r["eps_fy0"], r["eps_fy1"]
    s0, s1 = r["rev_fy0"], r["rev_fy1"]
    if not np.isnan(f) and not np.isnan(e1) and (not np.isnan(e0) or f == 0):
        r["eps_ntm"] = (f * e0 if f > 0 else 0.0) + (1 - f) * e1
        r["ntm_basis"] = "FY1_only(FY0 ended, unreported)" if f == 0 else "f*FY0+(1-f)*FY1"
    else:
        r["eps_ntm"] = np.nan
        r["ntm_basis"] = "missing_estimates" if (np.isnan(e0) or np.isnan(e1)) else "missing_fy_dates"
    if not np.isnan(f) and not np.isnan(s1) and (not np.isnan(s0) or f == 0):
        r["rev_ntm"] = (f * s0 if f > 0 else 0.0) + (1 - f) * s1
    else:
        r["rev_ntm"] = np.nan

    # quarter-aware diagnostic NTM
    eh = rec.get("earnings_history")
    ytd, nq = np.nan, 0
    if isinstance(eh, pd.DataFrame) and len(eh) and pd.notna(r["lastFiscalYearEnd"]) and "epsActual" in eh.columns:
        idx = pd.to_datetime(eh.index)
        m = (idx > r["lastFiscalYearEnd"] + pd.Timedelta(days=20)) & (idx <= ASOF_TS)
        vals = pd.to_numeric(eh.loc[m, "epsActual"], errors="coerce")
        nq = int(vals.notna().sum())
        ytd = float(vals.sum()) if nq > 0 else 0.0
    r["fy0_quarters_reported_eh"] = nq
    r["eps_fy0_ytd_reported"] = ytd
    if not np.isnan(e0) and not np.isnan(e1) and not np.isnan(ytd) and not np.isnan(f):
        if f == 0:
            r["eps_ntm_qaware"] = e1
        else:
            r["eps_ntm_qaware"] = (e0 - ytd) + e1 * nq / 4.0
    else:
        r["eps_ntm_qaware"] = np.nan
    # internal-consistency check of the consensus: remaining FY0 EPS (FY0 - YTD reported) should equal the sum of the
    # remaining quarterly estimates when 1 or 2 quarters remain (0q[/+1q] are then exactly the remaining quarters)
    rem_q = 4 - nq
    est_rem = r["eps_q0"] if rem_q == 1 else (r["eps_q0"] + r["eps_q1"] if rem_q == 2 else np.nan)
    r["fy0_remaining_quarters"] = rem_q
    r["fy0_rem_vs_qsum"] = ((e0 - ytd) / est_rem - 1) if (not np.isnan(est_rem) and est_rem > 0 and not np.isnan(e0) and not np.isnan(ytd)) else np.nan
    # quarterly-sum NTM variant: remaining FY0 quarters from the explicit 0q/+1q rows (avoids the 0y annual row)
    if not np.isnan(f) and f == 0 and not np.isnan(e1):
        r["eps_ntm_qsum"] = e1
    elif not np.isnan(est_rem) and not np.isnan(e1):
        r["eps_ntm_qsum"] = est_rem + e1 * nq / 4.0
    else:
        r["eps_ntm_qsum"] = np.nan
    # internal consistency of Yahoo's consensus rows
    r["fy1_yago_vs_fy0"] = (r["eps_fy1_yago"] / e0 - 1) if (not np.isnan(e0) and e0 != 0 and not np.isnan(r["eps_fy1_yago"])) else np.nan
    r["fy1_n_ratio"] = (r["eps_fy1_n"] / r["eps_fy0_n"]) if (r["eps_fy0_n"] and not np.isnan(r["eps_fy0_n"]) and not np.isnan(r["eps_fy1_n"])) else np.nan
    r["info_epsCY_vs_fy0"] = (r["epsCurrentYear"] / e0 - 1) if (not np.isnan(e0) and e0 != 0 and not np.isnan(r["epsCurrentYear"])) else np.nan

    # valuation multiples
    def pe(p, e):
        return p / e if (not np.isnan(p) and not np.isnan(e) and e > 0) else np.nan
    r["pe_ntm"] = pe(price, r["eps_ntm"])
    r["pe_ntm_qaware"] = pe(price, r["eps_ntm_qaware"])
    r["pe_fy0"] = pe(price, e0)
    r["pe_fy1"] = pe(price, e1)
    r["pe_ntm_reason"] = (None if not np.isnan(r["pe_ntm"]) else
                         ("NTM EPS <= 0" if (not np.isnan(r["eps_ntm"]) and r["eps_ntm"] <= 0) else r["ntm_basis"]))
    r["ev_sales_ntm"] = safe_div(r["enterpriseValue"], r["rev_ntm"])
    r["ps_ntm"] = safe_div(r["marketCap"], r["rev_ntm"])
    r["fcf_yield"] = safe_div(r["freeCashflow"], r["marketCap"])
    r["eps_growth_ntm_vs_ttm"] = (r["eps_ntm"] / r["trailingEps"] - 1) if (r["trailingEps"] and r["trailingEps"] > 0 and not np.isnan(r["eps_ntm"])) else np.nan

    # which horizon does Yahoo forwardEps / forwardPE use?
    fe = r["forwardEps"]
    def rel(a, b):
        return abs(a / b - 1) if (not np.isnan(a) and not np.isnan(b) and b != 0) else np.nan
    r0, r1 = rel(fe, e0), rel(fe, e1)
    r["fwdEps_rel_fy0"], r["fwdEps_rel_fy1"] = r0, r1
    if np.isnan(fe):
        hz = "missing_forwardEps"
    elif not np.isnan(r1) and r1 <= 0.005:
        hz = "FY1(+1y)"
    elif not np.isnan(r0) and r0 <= 0.005:
        hz = "FY0(0y)"
    elif not np.isnan(r1) and not np.isnan(r0):
        hz = ("~FY1(+1y)" if r1 < r0 else "~FY0(0y)") + (">3%off" if min(r0, r1) > 0.03 else "")
    else:
        hz = "undetermined"
    r["yahoo_fwd_horizon"] = hz
    r["forwardPE_recalc"] = pe(price, fe)
    r["forwardPE_consistency"] = rel(r["forwardPE"], r["forwardPE_recalc"])
    r["fwdPE_over_peNTM"] = safe_div(r["forwardPE"], r["pe_ntm"])
    r["fwdPE_vs_peNTM_gt10pct"] = (bool(abs(r["fwdPE_over_peNTM"] - 1) > 0.10) if not np.isnan(r["fwdPE_over_peNTM"]) else None)
    r["pe_ntm_qsum"] = pe(price, r["eps_ntm_qsum"])

    # --- NTM data-quality grade (flags are listed; 'unreliable' = at least one major issue)
    major, minor = [], []
    if np.isnan(r["eps_ntm"]):
        major.append("ntm_missing")
    elif r["eps_ntm"] <= 0:
        major.append("ntm_eps_nonpositive")
    if "REIT" in str(uni_row["gics_sub_industry"]):
        major.append("reit_eps_not_ffo")
    v = r["fy0_rem_vs_qsum"]
    if not np.isnan(v) and abs(v) > 0.05:
        (major if abs(v) > 0.25 else minor).append(f"fy0_vs_quarterly_rows_{v:+.0%}")
    v = r["fy1_yago_vs_fy0"]
    if not np.isnan(v) and abs(v) > 0.02:
        (major if abs(v) > 0.10 else minor).append(f"fy1_row_yearAgo_ne_fy0_{v:+.0%}")
    if (not np.isnan(r["fy1_n_ratio"]) and r["fy1_n_ratio"] < 0.5) or (not np.isnan(r["eps_fy1_n"]) and r["eps_fy1_n"] < 3):
        minor.append("fy1_thin_coverage")
    v = r["info_epsCY_vs_fy0"]
    if not np.isnan(v) and abs(v) > 0.03:
        minor.append(f"info_epsCurrentYear_vs_trend_{v:+.0%}")
    if not np.isnan(r["eps_ntm"]) and r["eps_ntm"] > 0 and not np.isnan(r["eps_ntm_qaware"]):
        v = r["eps_ntm_qaware"] / r["eps_ntm"] - 1
        if abs(v) > 0.10:
            minor.append(f"ntm_timeweighted_vs_quarteraware_{v:+.0%}")
    if not np.isnan(e0) and not np.isnan(e1) and e0 > 0 and e1 < 0.85 * e0:
        minor.append("fy1_below_fy0_by_15pct+")
    lo1, hi1 = r["eps_fy1_low"], r["eps_fy1_high"]
    if not np.isnan(e1) and e1 != 0 and not np.isnan(lo1) and not np.isnan(hi1) and (hi1 - lo1) / abs(e1) > 1.0:
        minor.append("fy1_dispersion_extreme")
    if rec.get("estimates_from_sibling"):
        minor.append(f"estimates_from_sibling_{rec.get('estimates_from_sibling')}")
    if r["fy_check"] != "ok":
        minor.append("fiscal_date_check_" + r["fy_check"])
    r["ntm_flags"] = ";".join(major + minor)
    r["ntm_quality"] = "unreliable" if major else ("caution" if minor else "ok")

    # --- earnings surprises: last 8 reported quarters (earnings_dates), fallback earnings_history
    ed = rec.get("earnings_dates")
    beats = misses = nrep = 0
    avg_s = np.nan
    src = None
    if isinstance(ed, pd.DataFrame) and len(ed) and "Reported EPS" in ed.columns:
        e2 = ed.copy()
        e2.index = pd.to_datetime(e2.index, utc=True)
        e2 = e2[(e2["Reported EPS"].notna()) & (e2.index <= pd.Timestamp("2026-09-26", tz="UTC"))].sort_index(ascending=False)
        e2 = e2[~e2.index.duplicated()].head(8)
        if len(e2):
            s = pd.to_numeric(e2.get("Surprise(%)"), errors="coerce")
            if s.isna().all():
                s = (e2["Reported EPS"] / e2["EPS Estimate"] - 1) * 100
            beats, misses, nrep = int((s > 0).sum()), int((s < 0).sum()), int(s.notna().sum())
            avg_s = float(s.mean()) if nrep else np.nan
            src = "earnings_dates"
            r["last_report_date"] = e2.index.max().tz_convert(NY).date().isoformat()
    if src is None and isinstance(eh, pd.DataFrame) and len(eh) and "surprisePercent" in eh.columns:
        s = pd.to_numeric(eh["surprisePercent"], errors="coerce") * 100
        beats, misses, nrep = int((s > 0).sum()), int((s < 0).sum()), int(s.notna().sum())
        avg_s = float(s.mean()) if nrep else np.nan
        src = "earnings_history(4q)"
    r["beats_last8"], r["misses_last8"], r["n_reported_last8"], r["avg_surprise_pct_last8"] = beats, misses, nrep, avg_s
    r["surprise_source"] = src
    r.setdefault("last_report_date", None)

    # --- analyst targets / recommendations
    apt = rec.get("analyst_price_targets") or {}
    r["target_mean"], r["target_high"], r["target_low"], r["target_median"] = (fnum(apt.get(k)) for k in ["mean", "high", "low", "median"])
    r["n_analysts_targets"] = fnum(info.get("numberOfAnalystOpinions"))
    r["rec_mean"] = fnum(info.get("recommendationMean"))
    r["rec_key"] = info.get("recommendationKey")
    rs = rec.get("recommendations_summary")
    if isinstance(rs, pd.DataFrame) and len(rs) and "period" in rs.columns:
        row0 = rs[rs["period"] == "0m"]
        if len(row0):
            row0 = row0.iloc[0]
            cnt = [fnum(row0.get(c)) for c in ["strongBuy", "buy", "hold", "sell", "strongSell"]]
            n = np.nansum(cnt)
            r["rec_n_0m"] = n
            r["rec_strongbuy_buy_share"] = (cnt[0] + cnt[1]) / n if n else np.nan
            r["rec_mean_calc_0m"] = (sum((i + 1) * c for i, c in enumerate(cnt)) / n) if n else np.nan
    for k in ["rec_n_0m", "rec_strongbuy_buy_share", "rec_mean_calc_0m"]:
        r.setdefault(k, np.nan)

    # --- upgrades / downgrades in the 90 days to 2026-09-25 (inclusive)
    ud = rec.get("upgrades_downgrades")
    lo, hi = ASOF_TS - pd.Timedelta(days=90), ASOF_TS + pd.Timedelta(days=1)
    if isinstance(ud, pd.DataFrame) and len(ud):
        idx = pd.to_datetime(ud.index)
        w = ud[(idx > lo) & (idx < hi)]
        act = w.get("Action")
        pta = w.get("priceTargetAction")
        r["ud_ups_90d"] = int((act == "up").sum()) if act is not None else 0
        r["ud_downs_90d"] = int((act == "down").sum()) if act is not None else 0
        r["ud_inits_90d"] = int((act == "init").sum()) if act is not None else 0
        r["ud_actions_90d"] = int(len(w))
        r["pt_raises_90d"] = int((pta == "Raises").sum()) if pta is not None else 0
        r["pt_lowers_90d"] = int((pta == "Lowers").sum()) if pta is not None else 0
        r["ud_last_date"] = idx.max().date().isoformat()
    else:
        for k in ["ud_ups_90d", "ud_downs_90d", "ud_inits_90d", "ud_actions_90d", "pt_raises_90d", "pt_lowers_90d"]:
            r[k] = 0 if rec.get("errors", {}).get("upgrades_downgrades", "").startswith("NO_DATA") else np.nan
        r["ud_last_date"] = None

    # --- next earnings date (raw epochs -> New York date); compare to yfinance calendar (local-tz conversion)
    cr = rec.get("calendar_raw") or {}
    try:
        ce = cr["quoteSummary"]["result"][0]["calendarEvents"]
    except (KeyError, IndexError, TypeError):
        ce = {}
    earn = (ce.get("earnings") or {})
    eds = sorted(ep_ny(x) for x in (earn.get("earningsDate") or []) if x)
    fut = [d for d in eds if d.date() >= ASOF]
    r["next_earnings_date"] = fut[0].date().isoformat() if fut else None
    r["next_earnings_is_estimate"] = earn.get("isEarningsDateEstimate")
    r["earnings_dates_raw_all_past"] = bool(eds and not fut)
    cal = rec.get("calendar") or {}
    cal_ed = cal.get("Earnings Date") or []
    r["yf_calendar_earnings_date"] = cal_ed[0].isoformat() if cal_ed else None
    r["yf_calendar_tz_shift"] = bool(cal_ed and eds and cal_ed[0] != eds[0].date())
    r["days_to_next_earnings"] = ((pd.Timestamp(r["next_earnings_date"]) - ASOF_TS).days if r["next_earnings_date"] else np.nan)
    return r


EST_KEYS = ["earnings_estimate", "revenue_estimate", "eps_trend", "eps_revisions", "earnings_trend_raw", "earnings_history"]


def has_est(rec):
    ee = rec.get("earnings_estimate")
    return isinstance(ee, pd.DataFrame) and len(ee) > 0


def main():
    u = pd.read_csv(DATA / "d4_universe.csv")
    recs, missing = {}, []
    for _, ur in u.iterrows():
        fp = YCACHE / f"{ur['ticker']}.pkl"
        if not fp.exists():
            missing.append(ur["ticker"])
            continue
        with open(fp, "rb") as f:
            recs[ur["ticker"]] = pickle.load(f)
    # Share-class siblings (same CIK, equal per-share economics, e.g. FOX/FOXA, NWS/NWSA, GOOG/GOOGL): if Yahoo has no
    # consensus for one class, borrow the sibling's consensus objects and FLAG it (column estimates_from_sibling).
    cik_of = dict(zip(u["ticker"], u["cik"]))
    for tk, rec in recs.items():
        rec["estimates_from_sibling"] = None
        if has_est(rec):
            continue
        sibs = [t for t in recs if t != tk and cik_of.get(t) == cik_of.get(tk) and has_est(recs[t])]
        if sibs:
            rec.update({k: recs[sibs[0]].get(k) for k in EST_KEYS})
            rec["estimates_from_sibling"] = sibs[0]
            rec["errors"] = {k: v for k, v in (rec.get("errors") or {}).items() if k not in EST_KEYS}
    rows = []
    for _, ur in u.iterrows():
        if ur["ticker"] in recs:
            row = build_row(recs[ur["ticker"]], ur)
            row["estimates_from_sibling"] = recs[ur["ticker"]].get("estimates_from_sibling")
            rows.append(row)
    df = pd.DataFrame(rows)
    # tidy dtypes for parquet
    for c in df.columns:
        if df[c].dtype == object:
            vals = df[c].dropna()
            if len(vals) and all(isinstance(v, (bool, np.bool_)) for v in vals):
                df[c] = df[c].astype("boolean")
            elif len(vals) and all(isinstance(v, (int, float, np.integer, np.floating)) and not isinstance(v, bool) for v in vals):
                df[c] = pd.to_numeric(df[c], errors="coerce")
            elif len(vals):
                df[c] = df[c].map(lambda v: None if v is None or (isinstance(v, float) and math.isnan(v)) else str(v))
    out = DATA / "d4_live_snapshot.parquet"
    df.to_parquet(out, index=False)
    t_start = df["retrieved_utc_start"].dropna().min()
    t_end = df["retrieved_utc_end"].dropna().max()
    write_meta(out, {
        "source": "Yahoo Finance via yfinance 1.7.0 (quoteSummary, v7 quote, fundamentals-timeseries, earnings calendar page)",
        "source_urls": ["https://query2.finance.yahoo.com/v10/finance/quoteSummary/<T>",
                        "https://query1.finance.yahoo.com/v7/finance/quote?symbols=<T>",
                        "https://finance.yahoo.com/calendar/earnings?symbol=<T>",
                        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"],
        "retrieval_utc_first": t_start, "retrieval_utc_last": t_end,
        "as_of_close": ASOF.isoformat(), "rows": int(len(df)), "columns_n": int(df.shape[1]),
        "missing_tickers": missing,
        "coverage": {c: int(df[c].notna().sum()) for c in ["price", "marketCap", "forwardEps", "eps_fy0", "eps_fy1",
                                                            "eps_ntm", "pe_ntm", "rev_ntm", "target_mean",
                                                            "next_earnings_date"]},
        "key_definitions": {
            "price": "info.regularMarketPrice (regular-session close 2026-09-25)",
            "eps_fy0/eps_fy1": "earnings_estimate avg for Yahoo periods '0y'/'+1y'",
            "fy0_end": "raw earningsTrend endDate of '0y' (fallback info.nextFiscalYearEnd)",
            "f_fy0_remaining": "clip((fy0_end-2026-09-25)/(fy1_end-fy0_end),0,1)",
            "eps_ntm": "f*eps_fy0+(1-f)*eps_fy1",
            "rev_ntm": "f*rev_fy0+(1-f)*rev_fy1",
            "yahoo_fwd_horizon": "which period Yahoo's forwardEps equals (0.5% tolerance)",
            "trailingAnnualDividendYield": "fraction (0.01 = 1%); NOTE y_dividendYield is in PERCENT units in yfinance 1.7",
            "ud_*_90d": "upgrades_downgrades rows with GradeDate in (2026-06-27, 2026-09-25]",
            "beats_last8": "count of Surprise(%)>0 over last 8 reported quarters (earnings_dates; fallback earnings_history 4q)",
            "next_earnings_date": "calendarEvents.earnings.earningsDate epoch converted in America/New_York",
        },
        "caveats": ["Yahoo consensus = vendor snapshot; basis (GAAP/adjusted) is vendor-defined and undocumented.",
                    "earningsTrend endDates are month-end normalized (e.g., NVDA FY ends last Sunday of Jan).",
                    "Missing values are NaN; see fetch_errors / fetch_nodata / pe_ntm_reason."],
    })
    print("rows", len(df), "cols", df.shape[1], "missing", missing)


if __name__ == "__main__":
    main()
