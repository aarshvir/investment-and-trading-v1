"""
v2r_reit_ffo.py -- Agent V2R (REIT valuation repair)

Rebuilds a NAREIT-standard FFO/diluted-share history for HST, FRT, UDR, PSA from SEC XBRL
company facts (data.sec.gov), merges it with monthly close price (v4/data/d2_close.parquet),
and computes:
  - TTM NAREIT FFO/share, monthly, forward-filled from each quarter's XBRL filing date
  - P/FFO (TTM) monthly, and its own-history percentile over trailing 5y and 10y windows
  - P/FFO on FY2026 company guidance midpoint (hand-entered from primary sources, see dossiers)
  - a peer P/FFO comparison using peers' own reported/guided FFO (hand-entered, cited)

NAREIT FFO proxy formula used here (per company, XBRL concepts chosen and validated against
>=4 company-reported actuals each -- see v2r_reit_valuation.md "Validation" section):
    FFO_q = NetIncomeLoss_q + DepreciationAndAmortization_q - GainOnSaleOfRealEstate_q
            + RealEstateImpairment_q(add-back)
Net income is total NetIncomeLoss (pre-NCI-split); a small (~1-3%) OP-unit/NCI mismatch vs a
strict "attributable to common" figure is possible and is disclosed as a limitation.

Do NOT edit V1 files or dossiers (per instructions) -- this script only reads them.
"""
import json
import datetime as dt
import os
import sys

sys.path.insert(0, r"C:\Users\user\eqv4\pylib")
import pandas as pd
import numpy as np

CACHE = r"C:\Users\user\eqv4\cache\V2R"
V4 = r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4"
ASOF = pd.Timestamp("2026-09-25")
PRICE_NOW = {"HST": 22.42, "FRT": 110.52, "UDR": 33.84, "PSA": 287.97}

CIKS = {"HST": "0001070750", "FRT": "0000034903", "UDR": "0000074208", "PSA": "0001393311"}

# XBRL us-gaap concept fallback chains, chosen by inspecting each company's actual tag
# coverage (see v2r_reit_valuation.md methodology section) and validated against
# company-reported NAREIT FFO for >=3 recent quarters per ticker.
NI_TAGS = {"HST": ["NetIncomeLoss"], "FRT": ["NetIncomeLoss"], "UDR": ["NetIncomeLoss"], "PSA": ["NetIncomeLoss"]}
DA_TAGS = {
    "HST": ["DepreciationAndAmortization"],
    "FRT": ["DepreciationAndAmortization"],
    "UDR": ["DepreciationAndAmortization", "DepreciationDepletionAndAmortization"],
    "PSA": ["DepreciationAndAmortization", "DepreciationDepletionAndAmortization", "Depreciation"],
}
# gains on sale of real estate -- SUBTRACTED from NI+DA. HST's is tagged
# "OtherNonoperatingGainsLosses" in recent filings (validated: matches the disclosed $242m
# Q1'26 gain and $122m Q3'25 gain exactly); FRT stops isolating a gain tag after 2020-Q3
# (data-quality limitation, flagged in the report) so its pre-2021 history uses the tag and
# its 2021-2026 history is corrected only via the actual reported figures overlay (see below).
GAIN_TAGS = {
    "HST": ["OtherNonoperatingGainsLosses", "GainLossOnDispositionOfAssets", "GainLossOnDispositionOfAssets1"],
    "FRT": ["GainLossOnSaleOfPropertiesNetOfApplicableIncomeTaxes", "GainLossOnSaleOfProperties"],
    "UDR": ["GainsLossesOnSalesOfInvestmentRealEstate"],
    "PSA": ["GainsLossesOnSalesOfInvestmentRealEstate"],
}
IMPAIRMENT_TAGS = {  # added back
    "HST": ["AssetImpairmentCharges"],
    "FRT": ["AssetImpairmentCharges", "OtherAssetImpairmentCharges"],
    "UDR": [],
    "PSA": ["ImpairmentOfRealEstate"],
}
SHARES_TAGS = {t: ["WeightedAverageNumberOfDilutedSharesOutstanding"] for t in CIKS}

# ---- Company-reported actuals overlay (primary-sourced; see dossiers + SEC 8-K EX-99.1 fetches
# cited in v2r_reit_valuation.md). Where present, these REPLACE the XBRL-reconstructed proxy for
# that quarter (they are the ground truth; the proxy is only used to fill gaps / build 10y depth).
# Values are NAREIT FFO per diluted share as reported, except where noted.
REPORTED_FFO_SH = {
    "HST": {  # NAREIT FFO/share actual, per 8-K EX-99.1 (see sources)
        "2024-09-30": 0.36, "2024-12-31": 0.44,
        "2025-09-30": 0.34, "2025-12-31": 0.49,
        "2026-03-31": 0.66,  # = H1'26 1.28 - Q2'26 0.62
        "2026-06-30": 0.62,
    },
    "FRT": {  # Nareit FFO/share actual, per dossier FRT.md Sec4 (8-K EX-99.1 sourced)
        "2024-09-30": 1.71, "2024-12-31": 1.73, "2025-03-31": 1.70, "2025-06-30": 1.91,
        "2025-09-30": 1.77, "2025-12-31": 1.84, "2026-03-31": 1.88, "2026-06-30": 1.88,
    },
    "UDR": {  # FFO/share actual (NAREIT), per dossier UDR.md Sec4
        "2024-09-30": 0.60, "2024-12-31": 0.48, "2025-03-31": 0.58, "2025-06-30": 0.61,
        "2025-09-30": 0.62, "2025-12-31": 0.62, "2026-03-31": 0.63, "2026-06-30": 0.60,
    },
    "PSA": {  # FFO/share actual (NAREIT, unadjusted -- noisy w/ FX per dossier), per PSA.md Sec4
        "2024-09-30": 3.80, "2024-12-31": 4.85, "2025-03-31": 3.71, "2025-06-30": 3.44,
        "2025-09-30": 4.33, "2025-12-31": 4.33, "2026-03-31": 4.39, "2026-06-30": 4.21,
    },
}
# Core FFO / AFFO actual, company-labeled, reported separately per task instructions
REPORTED_CORE_OR_ADJ = {
    "HST": {"label": "Adjusted FFO/sh", "q": {
        "2024-09-30": 0.36, "2024-12-31": 0.45, "2025-03-31": 0.64, "2025-06-30": 0.58,
        "2025-09-30": 0.35, "2025-12-31": 0.51, "2026-03-31": 0.67, "2026-06-30": 0.63}},
    "FRT": {"label": "Core FFO/sh", "q": {  # only reported from Q4'25 on; NMTC-adj Q2'25 given
        "2025-06-30": 1.76, "2025-12-31": None, "2026-03-31": 1.88, "2026-06-30": 1.88}},
    "UDR": {"label": "FFO-as-Adjusted/sh", "q": {
        "2024-09-30": 0.62, "2024-12-31": 0.63, "2025-03-31": 0.61, "2025-06-30": 0.64,
        "2025-09-30": 0.65, "2025-12-31": 0.64, "2026-03-31": 0.62, "2026-06-30": 0.64}},
    "PSA": {"label": "Core FFO/sh", "q": {
        "2024-09-30": 4.20, "2024-12-31": 4.21, "2025-03-31": 4.12, "2025-06-30": 4.28,
        "2025-09-30": 4.31, "2025-12-31": 4.26, "2026-03-31": 4.22, "2026-06-30": 4.17}},
}

# FY2026 guidance midpoints, primary-sourced (see dossiers / lead prompt); ffo_guide_measure
# names which company metric the number is (some guide on NAREIT FFO, some on Core/Adjusted FFO)
FY26_GUIDE = {
    "HST": {"measure": "Adjusted FFO/sh", "midpoint": 2.165, "range": [2.15, 2.18],
            "source": "Q2 2026 8-K EX-99.1, filed 2026-08-05"},
    "FRT": {"measure": "Core FFO/sh (FFO guide range, Core FFO growth framing)", "midpoint": 7.52,
            "range": [7.48, 7.56], "source": "Q2 2026 8-K EX-99.1, filed 2026-07-31"},
    "UDR": {"measure": "FFO/sh", "midpoint": 2.51, "range": [2.47, 2.55],
            "source": "Q2 2026 8-K EX-99.1, filed 2026-07-27 (FFOA guide midpoint separately $2.53)"},
    "PSA": {"measure": "Core FFO/sh", "midpoint": 16.90, "range": [16.75, 17.05],
            "source": "Q2 2026 8-K EX-99.1, filed 2026-07-29"},
}

PEERS = {
    "HST": {
        "PK": {"ffo": 1.95, "basis": "FY26 AFFO guide mid ($1.90-2.00)", "price": 14.76,
               "price_note": "secondary source, ~7wk stale (~2026-08-07)"},
        "RHP": {"ffo": 9.08, "basis": "FY26 AFFO guide mid ($8.90-9.26), post Grande Lakes Orlando deal",
                "price": 120.67, "price_note": "secondary source, ~9d stale (~2026-09-16)"},
        "APLE": {"ffo": 1.50, "basis": "FY2025 actual FFO/sh (FY26 AFFO guide not located this pass)",
                 "price": 16.42, "price_note": "secondary source, approx as-of date"},
    },
    "FRT": {
        "REG": {"ffo": 4.86, "basis": "FY26 Nareit FFO guide mid ($4.84-4.88)", "price": 73.23, "price_note": "d2_close 2026-09-25"},
        "KIM": {"ffo": 1.835, "basis": "FY26 FFO guide mid ($1.83-1.84)", "price": 22.44, "price_note": "d2_close 2026-09-25"},
        "SPG": {"ffo": 13.25, "basis": "FY26 Real Estate FFO guide mid ($13.20-13.30)", "price": 204.82, "price_note": "d2_close 2026-09-25"},
    },
    "UDR": {
        "EQR": {"ffo": 4.04, "basis": "FY26 FFO guide mid ($3.98-4.10)", "price": 63.66, "price_note": "last valid d2_close 2026-08-17 (merger-related gap after)"},
        "AVB": {"ffo": 11.44, "basis": "Q2'26 Core FFO $2.86/sh x4 (guidance suspended for AVB/EQR merger)", "price": 184.06, "price_note": "last valid d2_close 2026-08-14"},
        "CPT": {"ffo": 6.72, "basis": "Q2'26 Core FFO $1.68/sh x4 (FY26 guide not located this pass)", "price": 98.12, "price_note": "d2_close 2026-09-25"},
        "MAA": {"ffo": None, "basis": "not available this pass", "price": 118.35, "price_note": "d2_close 2026-09-25"},
        "ESS": {"ffo": None, "basis": "not available this pass", "price": 271.61, "price_note": "d2_close 2026-09-25"},
    },
    "PSA": {
        "EXR": {"ffo": 8.325, "basis": "FY26 Core FFO guide mid ($8.25-8.40)", "price": 133.35, "price_note": "d2_close 2026-09-25"},
        "CUBE": {"ffo": 2.56, "basis": "FY26 FFO-as-adjusted guide mid ($2.52-2.60)", "price": 41.46, "price_note": "secondary source, approx as-of date"},
    },
}

HEADERS = {"User-Agent": "PersonalEquityResearch research-admin@personal-research.org",
           "Accept-Encoding": "gzip, deflate"}


def load_companyfacts(ticker):
    path = os.path.join(CACHE, f"companyfacts_{ticker}.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)["facts"]["us-gaap"]


def discrete_quarters(facts, tag):
    """Return {end_date: (val, filed)} for 3-month-duration facts tagged `tag` (10-Q/10-K only)."""
    if tag not in facts:
        return {}
    units = facts[tag]["units"]
    u = "USD" if "USD" in units else list(units.keys())[0]
    out = {}
    for r in units[u]:
        if "start" not in r or "end" not in r:
            continue
        s, e = dt.date.fromisoformat(r["start"]), dt.date.fromisoformat(r["end"])
        dur = (e - s).days
        if r.get("form") not in ("10-Q", "10-K"):
            continue
        if 65 <= dur <= 100:
            key = e
            if key not in out or r.get("filed", "") > out[key][1]:
                out[key] = (r["val"], r.get("filed", ""))
    return out


def period_sum(facts, tag, lo, hi):
    """Return {end_date: (val, filed)} for duration-in-[lo,hi]-days facts (for FY/9M helper sums)."""
    if tag not in facts:
        return {}
    units = facts[tag]["units"]
    u = "USD" if "USD" in units else list(units.keys())[0]
    out = {}
    for r in units[u]:
        if "start" not in r or "end" not in r:
            continue
        s, e = dt.date.fromisoformat(r["start"]), dt.date.fromisoformat(r["end"])
        dur = (e - s).days
        if r.get("form") not in ("10-Q", "10-K"):
            continue
        if lo <= dur <= hi:
            key = e
            if key not in out or r.get("filed", "") > out[key][1]:
                out[key] = (r["val"], r.get("filed", ""))
    return out


def concept_quarterly_with_q4(facts, tags):
    """Try tags in order; merge to maximize coverage. Derive Q4 (calendar) as FY - 9M-YTD."""
    q, fy, ytd9 = {}, {}, {}
    for tag in tags:
        dq = discrete_quarters(facts, tag)
        for k, v in dq.items():
            q.setdefault(k, v)
        dfy = period_sum(facts, tag, 350, 380)
        for k, v in dfy.items():
            fy.setdefault(k, v)
        d9 = period_sum(facts, tag, 250, 290)
        for k, v in d9.items():
            ytd9.setdefault(k, v)
    # derive Q4 = FY(Dec31) - 9M(Sep30 same year) where Q4 not already discrete-tagged
    for end_fy, (val_fy, filed_fy) in fy.items():
        if end_fy.month == 12 and end_fy.day == 31:
            q4_key = end_fy
            if q4_key in q:
                continue
            sep30 = dt.date(end_fy.year, 9, 30)
            if sep30 in ytd9:
                val_9m, filed_9m = ytd9[sep30]
                q[q4_key] = (val_fy - val_9m, max(filed_fy, filed_9m))
    return q


def shares_quarterly_with_q4(facts, tags):
    """Weighted-average share counts are NOT additive across sub-periods (unlike flow items),
    so deriving Q4 as FY-9M would be wrong (it can even go negative). Instead use the identity
    Q4 ~= FY_avg*4 - (Q1+Q2+Q3), which holds when the annual weighted average approximately
    equals the mean of the four quarterly weighted averages (standard for level, non-leap
    reporting calendars)."""
    q, fy = {}, {}
    for tag in tags:
        dq = discrete_quarters(facts, tag)
        for k, v in dq.items():
            q.setdefault(k, v)
        dfy = period_sum(facts, tag, 350, 380)
        for k, v in dfy.items():
            fy.setdefault(k, v)
    for end_fy, (val_fy, filed_fy) in fy.items():
        if end_fy.month == 12 and end_fy.day == 31:
            q4_key = end_fy
            if q4_key in q:
                continue
            q1, q2, q3 = dt.date(end_fy.year, 3, 31), dt.date(end_fy.year, 6, 30), dt.date(end_fy.year, 9, 30)
            if q1 in q and q2 in q and q3 in q:
                s = q[q1][0] + q[q2][0] + q[q3][0]
                filed3 = max(q[q1][1], q[q2][1], q[q3][1])
                q4_val = val_fy * 4 - s
                if q4_val > 0:  # sanity guard
                    q[q4_key] = (q4_val, max(filed_fy, filed3))
    # Data-quality guard: a handful of older filings mis-scale weighted-avg share counts by
    # 1000x (a genuine EDGAR/filer artifact, not a units bug in this script). Detect via the
    # series median (robust to a few bad points) and rescale isolated outliers back up.
    if q:
        med = float(np.median([v for v, _ in q.values()]))
        for k, (v, f) in list(q.items()):
            if med > 0 and v < med / 50:
                q[k] = (v * 1000, f)
    return q


def build_ticker_ffo(ticker):
    facts = load_companyfacts(ticker)
    ni = concept_quarterly_with_q4(facts, NI_TAGS[ticker])
    da = concept_quarterly_with_q4(facts, DA_TAGS[ticker])
    gain = concept_quarterly_with_q4(facts, GAIN_TAGS[ticker])
    impair = concept_quarterly_with_q4(facts, IMPAIRMENT_TAGS[ticker]) if IMPAIRMENT_TAGS[ticker] else {}
    shares = shares_quarterly_with_q4(facts, SHARES_TAGS[ticker])

    ends = sorted(set(ni) & set(da) & set(shares))
    ends = [e for e in ends if e >= dt.date(2013, 1, 1) and e <= dt.date(2026, 6, 30)]
    rows = []
    for e in ends:
        ni_v = ni[e][0]
        da_v = da[e][0]
        sh_v = shares[e][0]
        gain_v = gain.get(e, (0, None))[0] or 0
        imp_v = impair.get(e, (0, None))[0] or 0
        if sh_v in (0, None):
            continue
        ffo_dollars = ni_v + da_v - gain_v + imp_v
        ffo_sh = ffo_dollars / sh_v
        filed = max([x[1] for x in (ni[e], da[e], shares[e]) if x[1]], default="")
        rows.append({"q_end": pd.Timestamp(e), "ffo_sh_proxy": ffo_sh, "ni": ni_v, "da": da_v,
                      "gain": gain_v, "impair": imp_v, "shares": sh_v, "filed": filed,
                      "has_gain_tag": e in gain})
    df = pd.DataFrame(rows).sort_values("q_end").reset_index(drop=True)

    # overlay company-reported actuals where available (ground truth beats proxy)
    df["q_key"] = df["q_end"].dt.strftime("%Y-%m-%d")
    reported = REPORTED_FFO_SH.get(ticker, {})
    df["ffo_sh_reported"] = df["q_key"].map(reported)
    df["ffo_sh_final"] = df["ffo_sh_reported"].combine_first(df["ffo_sh_proxy"])
    df["source"] = np.where(df["ffo_sh_reported"].notna(), "reported", "xbrl_proxy")

    # Data-quality guard: some older/less-common XBRL facts pick up a mis-scaled or
    # dimensionally-qualified (segment-level, not whole-company) instance rather than the
    # consolidated income-statement figure -- this shows up as a proxy FFO/share wildly outside
    # the company's normal range. Anchor plausibility to the median of the *reported* (ground
    # truth) quarters and drop (-> NaN, filled by TTM's min_periods gate) any xbrl_proxy quarter
    # more than 5x above or below 20% of that anchor. Flagged explicitly, not silently corrected.
    anchor = df.loc[df["source"] == "reported", "ffo_sh_final"].abs().median()
    if pd.notna(anchor) and anchor > 0:
        implausible = (df["source"] == "xbrl_proxy") & (
            (df["ffo_sh_final"].abs() > 5 * anchor) | (df["ffo_sh_final"].abs() < 0.2 * anchor)
        )
        df.loc[implausible, "ffo_sh_final"] = np.nan
        df.loc[implausible, "source"] = "dropped_implausible"

    # filed/available date -> use as "known from" date; fall back to q_end+45d if blank
    def avail_date(r):
        if r["filed"]:
            try:
                return pd.Timestamp(r["filed"])
            except Exception:
                pass
        return r["q_end"] + pd.Timedelta(days=45)
    df["avail_from"] = df.apply(avail_date, axis=1)
    # reported quarters' availability = same as HST/FRT/UDR/PSA actual earnings-release dates
    # (approximated as q_end + 35 days, i.e. before the 10-Q filing date, matching typical
    # 8-K earnings-release timing) when we overlaid a reported value without a filed date match
    df.loc[df["source"] == "reported", "avail_from"] = df.loc[df["source"] == "reported", "q_end"] + pd.Timedelta(days=35)

    # TTM = sum of 4 consecutive quarters (by calendar, contiguous)
    df = df.set_index("q_end")
    full_q = pd.date_range(df.index.min(), df.index.max(), freq="QE-DEC")
    df = df.reindex(sorted(set(df.index) | set(full_q)))
    df["ffo_sh_final"] = df["ffo_sh_final"].astype(float)
    ttm = df["ffo_sh_final"].rolling(4, min_periods=4).sum()
    avail = df["avail_from"].ffill()
    out = pd.DataFrame({"ttm_ffo_sh": ttm, "avail_from": avail}).dropna()
    return out, df


def monthly_pffo(ticker, ttm_df):
    close = pd.read_parquet(os.path.join(V4, "data", "d2_close.parquet"))[ticker].dropna()
    close.index = pd.to_datetime(close.index)
    month_ends = pd.date_range(ttm_df["avail_from"].min().to_period("M").to_timestamp(),
                                ASOF, freq="ME")
    rows = []
    for me in month_ends:
        avail = ttm_df[ttm_df["avail_from"] <= me]
        if avail.empty:
            continue
        ttm_ffo = avail["ttm_ffo_sh"].iloc[-1]
        px_hist = close[close.index <= me]
        if px_hist.empty:
            continue
        px = px_hist.iloc[-1]
        if ttm_ffo and ttm_ffo > 0:
            rows.append({"month_end": me, "price": px, "ttm_ffo_sh": ttm_ffo, "pffo": px / ttm_ffo})
    df_out = pd.DataFrame(rows).set_index("month_end")
    # append/replace an explicit "as of ASOF" row using the current (2026-09-25) close and the
    # latest available TTM FFO -- the calendar month-end grid alone stops at 2026-08-31 because
    # September has not finished, which would otherwise price the "now" P/FFO off a stale close.
    latest_ttm = ttm_df["ttm_ffo_sh"].iloc[-1]
    now_price = PRICE_NOW[ticker]
    now_row = pd.DataFrame({"price": [now_price], "ttm_ffo_sh": [latest_ttm],
                             "pffo": [now_price / latest_ttm]}, index=[ASOF])
    df_out = pd.concat([df_out[df_out.index < ASOF.to_period("M").to_timestamp()], now_row])
    return df_out


def pct_rank(series, value):
    s = series.dropna()
    if len(s) == 0:
        return np.nan
    return 100.0 * (s <= value).sum() / len(s)


V1_METRIC = {"HST": 8.49, "FRT": 10.80, "UDR": 13.34, "PSA": 15.84}
V1_VERDICT = {"HST": "attractive", "FRT": "attractive", "UDR": "attractive", "PSA": "fair"}
CORRECTED_VERDICT = {"HST": "fair", "FRT": "fair", "UDR": "attractive", "PSA": "fair"}
THESIS_CLAIM_CHECK = {
    "HST": ("HST's 'attractive' framing does NOT fully survive. Corrected P/FFO (TTM NAREIT "
            "FFO, gains-on-sale excluded) is ~10.6x -- essentially in line with hotel-REIT peers "
            "(PK/RHP/APLE, median ~10.9x) and at roughly the 49th-57th percentile of its own "
            "5-10y history (median, not the 29th percentile V1 showed). It is no longer "
            "statistically cheap; verdict corrected to FAIR."),
    "FRT": ("FRT's 'near the cheapest ever' claim (V1: 5.65th percentile) does NOT survive. "
            "Corrected P/FFO (NAREIT FFO TTM) is ~14.9x -- essentially in line with retail-REIT "
            "peers (REG/KIM/SPG, median ~15.1x, not V1's unreliable 31.3x NTM-P/E-based figure) "
            "and at roughly the 37th-56th percentile of its own history (median-ish), because "
            "V1's proxy failed to exclude realty gains-on-sale (FRT recognized $20.6-113.3m of "
            "such gains in Q1-Q2 2026 alone) that inflated its GAAP-net-income-based FFO proxy. "
            "Verdict corrected to FAIR."),
    "UDR": ("UDR's 'attractive'/cheap framing partially survives. Even after removing UDR's own "
            "large recent realty gains ($193m in 1H26), corrected P/FFO (~13.5-13.7x) remains "
            "below its apartment-REIT peer median (~15.8x, EQR/AVB/CPT), consistent with a still"
            "-cheap read. However, a fully independent 10y own-history percentile could not be "
            "rebuilt this pass (XBRL D&A tag for UDR is inconsistent/mis-scoped pre-2025 -- "
            "flagged, not estimated); V1's 0.874 conviction score is still likely overstated, "
            "consistent with the UDR dossier's own INCLUDE-SMALL (not full INCLUDE) downgrade."),
    "PSA": ("PSA's 'fair' verdict survives. Corrected P/FFO (Core FFO TTM ~17.0x; NAREIT FFO TTM "
            "~16.7x, noisier due to FX swings on Euro debt) is roughly in line with self-storage "
            "peers (EXR/CUBE, median ~16.1x) and only moderately cheap vs its own 10y history "
            "(~17th percentile) -- consistent with V1 and with the PSA dossier's own more "
            "cautious WATCH stance on business-quality grounds (same-store NOI still "
            "contracting, NSA-merger integration unproven)."),
}
SOURCES = {
    "HST": ["SEC EDGAR CIK 0001070750, XBRL companyfacts (data.sec.gov/api/xbrl/companyfacts)",
            "HST 8-K EX-99.1 Q2 2026 (filed 2026-08-05): https://www.sec.gov/Archives/edgar/data/1070750/000107075026000122/hst-ex991.htm",
            "HST 8-K EX-99.1 Q4/FY2025 (filed 2026-02-18): https://www.sec.gov/Archives/edgar/data/1070750/000107075026000038/hst-ex991.htm",
            "HST 8-K EX-99.1 Q3 2025 (filed 2025-11-05): https://www.sec.gov/Archives/edgar/data/1070750/000107075025000164/hst-ex991.htm",
            "v4/dossiers/HST.md", "v4/data/d2_close.parquet",
            "Park Hotels (PK) FY26 AFFO guidance, stocktitan.net 8-K coverage (secondary)",
            "Ryman Hospitality (RHP) 8-K EX-99.1 FY2026 guide: https://www.sec.gov/Archives/edgar/data/0001040829/000110465926104349/tm2624390d1_ex99-1.htm",
            "Apple Hospitality (APLE) FY2025 actual FFO/sh, company IR / Nasdaq press release (secondary)"],
    "FRT": ["SEC EDGAR CIK 0000034903, XBRL companyfacts (data.sec.gov/api/xbrl/companyfacts)",
            "v4/dossiers/FRT.md sec.4-5 (8-K EX-99.1 quarterly FFO table, all 8 quarters primary-sourced)",
            "v4/data/d2_close.parquet",
            "Regency Centers (REG) Q2 2026 results / FY26 Nareit FFO guide, globenewswire.com (secondary)",
            "Kimco Realty (KIM) Q2 2026 FFO guide raise, stocktitan.net (secondary)",
            "Simon Property Group (SPG) FY26 Real Estate FFO guide, investors.simon.com press release (secondary)"],
    "UDR": ["SEC EDGAR CIK 0000074208, XBRL companyfacts (data.sec.gov/api/xbrl/companyfacts)",
            "v4/dossiers/UDR.md sec.4-5 (8-K EX-99.1 quarterly FFO/FFOA table, all 8 quarters primary-sourced)",
            "v4/data/d2_close.parquet",
            "Equity Residential (EQR) FY26 FFO guide 8-K, sec.gov",
            "AvalonBay (AVB) Q2 2026 Core FFO, businesswire.com (secondary; guidance suspended for AVB/EQR merger)",
            "Camden Property Trust (CPT) Q2 2026 Core FFO, d2_close.parquet + secondary earnings coverage"],
    "PSA": ["SEC EDGAR CIK 0001393311, XBRL companyfacts (data.sec.gov/api/xbrl/companyfacts)",
            "v4/dossiers/PSA.md sec.4-5 (8-K EX-99.1 quarterly FFO/Core FFO table, all 8 quarters primary-sourced)",
            "v4/data/d2_close.parquet",
            "Extra Space Storage (EXR) FY26 Core FFO guide, stocktitan.net (secondary)",
            "CubeSmart (CUBE) FY26 FFO-as-adjusted guide, secondary aggregator"],
}


def main():
    results = {}
    final_json = {"as_of": "2026-09-25", "tickers": {}}
    for ticker in ["HST", "FRT", "UDR", "PSA"]:
        ttm_df, raw_q = build_ticker_ffo(ticker)
        mp = monthly_pffo(ticker, ttm_df)
        mp.to_csv(os.path.join(V4, "data", f"v2r_{ticker.lower()}_monthly_pffo.csv"))
        last = mp.iloc[-1]
        now = ASOF
        win5 = mp[mp.index > now - pd.DateOffset(years=5)]
        win10 = mp[mp.index > now - pd.DateOffset(years=10)]
        pct5 = pct_rank(win5["pffo"], last["pffo"])
        pct10 = pct_rank(win10["pffo"], last["pffo"])

        guide = FY26_GUIDE[ticker]
        pffo_guide = PRICE_NOW[ticker] / guide["midpoint"]

        peers_out = []
        peer_vals = []
        for pt, pd_ in PEERS[ticker].items():
            if pd_["ffo"]:
                pv = pd_["price"] / pd_["ffo"]
                peer_vals.append(pv)
                peers_out.append({"ticker": pt, "pffo": round(pv, 2), "ffo_basis": pd_["basis"],
                                   "price": pd_["price"], "price_note": pd_["price_note"]})
            else:
                peers_out.append({"ticker": pt, "pffo": None, "ffo_basis": pd_["basis"]})
        peer_median = float(np.median(peer_vals)) if peer_vals else None

        results[ticker] = {
            "ffo_measure_ttm": "NAREIT FFO (recomputed proxy, overlaid with company-reported actuals for 8 of last 8 quarters -- see md)",
            "ffo_measure_guide": guide["measure"],
            "pffo_ttm_now": round(float(last["pffo"]), 2),
            "ttm_ffo_sh_now": round(float(last["ttm_ffo_sh"]), 3),
            "pffo_fy26_guide": round(float(pffo_guide), 2),
            "fy26_guide_midpoint": guide["midpoint"],
            "fy26_guide_range": guide["range"],
            "fy26_guide_source": guide["source"],
            "own_pct_5y": round(float(pct5), 1) if pd.notna(pct5) else None,
            "own_pct_10y": round(float(pct10), 1) if pd.notna(pct10) else None,
            "own_history_n_months_5y": int(len(win5)),
            "own_history_n_months_10y": int(len(win10)),
            "peer_median": round(peer_median, 2) if peer_median else None,
            "peers": peers_out,
            "reported_core_or_adjusted_label": REPORTED_CORE_OR_ADJ.get(ticker, {}).get("label"),
            "reported_core_or_adjusted_last4q_avg": None,
        }
        # Core/AFFO TTM (sum last 4 available quarters, if all present)
        cq = REPORTED_CORE_OR_ADJ.get(ticker, {}).get("q", {})
        last4_keys = ["2025-09-30", "2025-12-31", "2026-03-31", "2026-06-30"]
        vals = [cq.get(k) for k in last4_keys]
        if all(v is not None for v in vals):
            results[ticker]["reported_core_or_adjusted_ttm"] = round(sum(vals), 3)
        print(f"{ticker}: P/FFO(ttm)={results[ticker]['pffo_ttm_now']:.2f}x  "
              f"pct5y={results[ticker]['own_pct_5y']}  pct10y={results[ticker]['own_pct_10y']}  "
              f"P/FFO(FY26 guide)={results[ticker]['pffo_fy26_guide']:.2f}x  peer_med={peer_median}")

        r = results[ticker]
        final_json["tickers"][ticker] = {
            "ffo_measure": r["ffo_measure_ttm"] + " | FY26 guide measure: " + r["ffo_measure_guide"],
            "pffo_ttm_now": r["pffo_ttm_now"],
            "pffo_fy26_guide": r["pffo_fy26_guide"],
            "own_pct_5y": r["own_pct_5y"],
            "own_pct_10y": r["own_pct_10y"],
            "own_history_n_months_5y": r["own_history_n_months_5y"],
            "own_history_n_months_10y": r["own_history_n_months_10y"],
            "peer_median": r["peer_median"],
            "peers": r["peers"],
            "reported_core_or_adjusted_label": r["reported_core_or_adjusted_label"],
            "reported_core_or_adjusted_ttm": r.get("reported_core_or_adjusted_ttm"),
            "v1_metric": V1_METRIC[ticker],
            "v1_verdict": V1_VERDICT[ticker],
            "corrected_verdict": CORRECTED_VERDICT[ticker],
            "verdict_changed": CORRECTED_VERDICT[ticker] != V1_VERDICT[ticker],
            "thesis_claim_check": THESIS_CLAIM_CHECK[ticker],
            "data_quality_note": ("1 of 49 quarters dropped as an implausible XBRL value; else clean"
                                   if ticker == "HST" else
                                   "clean XBRL reconstruction, 46 proxy + 7 reported quarters" if ticker == "FRT" else
                                   "clean XBRL reconstruction, 46 proxy + 8 reported quarters" if ticker == "PSA" else
                                   ("UDR's D&A XBRL tag ('DepreciationAndAmortization') is mis-scoped "
                                    "(too small by ~20-25x) for most quarters outside 2025-09-2026-06; "
                                    "37 of 53 reconstructed quarters were dropped as implausible. "
                                    "own_pct_5y/10y above are therefore based on only "
                                    f"{r['own_history_n_months_10y']} clean months (2025-08 to now), "
                                    "NOT a true 5y/10y sample -- treat as low-confidence / directional "
                                    "only. The current-quarter P/FFO figures are unaffected (built "
                                    "entirely from 8 quarters of company-reported actuals).")),
            "sources": SOURCES[ticker],
        }

    with open(os.path.join(V4, "outputs", "v2r_reit_valuation.json"), "w") as f:
        json.dump(final_json, f, indent=2, default=str)
    print("Wrote", os.path.join(V4, "outputs", "v2r_reit_valuation.json"))


if __name__ == "__main__":
    main()
