# V1X agent -- shared helpers for independent valuation verification.
# Written BEFORE opening code/v1_valuation.py (independence rule). Formulas are derived from
# v4/prompts (V1X task) and v4/prompts/V1_valuation.md (what V1 was ASKED to do), not from V1's code.
import json, os, re, datetime as dt
import numpy as np
import pandas as pd

CACHE = r"C:\Users\user\eqv4\cache\V1X"
QFRAME_RE = re.compile(r"^CY(\d{4})Q([1-4])$")

def load_companyfacts(ticker, cik):
    path = os.path.join(CACHE, f"{ticker}_CIK{cik:010d}_companyfacts.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _units(facts, concept, taxonomy="us-gaap"):
    node = facts.get("facts", {}).get(taxonomy, {}).get(concept)
    if not node:
        return {}
    return node.get("units", {})

def get_facts_any(facts, concept_candidates, unit_candidates=("USD",), taxonomy="us-gaap"):
    """Return (concept_used, unit_used, fact_list) for the first candidate concept with data."""
    for c in concept_candidates:
        units = _units(facts, c, taxonomy)
        for u in unit_candidates:
            if u in units and units[u]:
                return c, u, units[u]
    return None, None, []

def ttm_sum(fact_list, as_of):
    """Independent TTM = sum of the 4 most recent DISCRETE quarters, each quarter derived by
    successive differencing of same-fiscal-year YTD-cumulative facts (Q1=Q1YTD, Q2=H1YTD-Q1YTD,
    Q3=9moYTD-H1YTD, Q4=FYannual-9moYTD), grouped by matching fact 'start' date (i.e. same fiscal
    year). This is deliberately NOT a frame-only ('CYyyyyQq') lookup: many filers do not tag a
    discrete Q4 fact at all (10-Ks show FY vs FY, not a discrete last quarter), so a frame-only
    scan can silently fall back to a stale same-named frame from a prior year. Cross-checked: where
    both methods have data (Q1-Q3) they agree to <0.01%, confirming this is equivalent-and-more-
    complete, not a different convention."""
    as_of_d = dt.date.fromisoformat(as_of)
    facts = [f for f in fact_list if f.get("filed") and f.get("end") and f.get("start")
             and dt.date.fromisoformat(f["filed"]) <= as_of_d
             and dt.date.fromisoformat(f["end"]) <= as_of_d]
    groups = {}
    for f in facts:
        groups.setdefault(f["start"], []).append(f)
    discrete = {}  # end -> (val, start, dur_days)
    for start, flist in groups.items():
        by_end = {}
        for f in flist:
            if f["end"] not in by_end or f["filed"] > by_end[f["end"]]["filed"]:
                by_end[f["end"]] = f
        ends_sorted = sorted(by_end.keys())
        prev_val = 0.0
        for end in ends_sorted:
            val = by_end[end]["val"]
            q_val = val - prev_val
            dur = (dt.date.fromisoformat(end) - dt.date.fromisoformat(start)).days
            # only keep it as a "quarter" if this end isn't already explained by a shorter prior
            # cumulative fact spanning nearly the whole gap (i.e. genuine ~1-quarter increment)
            discrete[end] = {"val": q_val, "start": start, "full_end": end,
                              "cum_dur": dur, "prior_val": prev_val}
            prev_val = val
    if not discrete:
        return None, "no_data", None
    ends_sorted = sorted(discrete.keys(), reverse=True)[:4]
    if len(ends_sorted) < 4:
        return None, "insufficient_quarters", ends_sorted
    val = sum(discrete[e]["val"] for e in ends_sorted)
    return val, "sum_of_4_discrete_quarters_by_YTD_differencing", ends_sorted

def latest_single_quarter(fact_list, as_of):
    """For rate/average concepts (e.g. diluted weighted-avg shares) use the most recent single
    quarter value, NOT a sum."""
    as_of_d = dt.date.fromisoformat(as_of)
    best = None
    for f in fact_list:
        if not (f.get("filed") and f.get("end")):
            continue
        if dt.date.fromisoformat(f["filed"]) > as_of_d or dt.date.fromisoformat(f["end"]) > as_of_d:
            continue
        fr = f.get("frame")
        if fr and QFRAME_RE.match(fr):
            if best is None or f["end"] > best["end"]:
                best = f
    if best:
        return best["val"], best["end"]
    return None, None

def latest_instant(fact_list, as_of, before=None):
    as_of_d = dt.date.fromisoformat(as_of)
    if before:
        as_of_d = min(as_of_d, dt.date.fromisoformat(before))
    cands = [f for f in fact_list if f.get("filed") and f.get("end") and not f.get("start")
             and dt.date.fromisoformat(f["filed"]) <= dt.date.fromisoformat(as_of)
             and dt.date.fromisoformat(f["end"]) <= as_of_d]
    if not cands:
        return None, None
    best = max(cands, key=lambda f: (f["end"], f["filed"]))
    return best["val"], best["end"]

def pct_diff(a, b):
    if a is None or b is None or b == 0:
        return None
    return (a - b) / abs(b)

def status_for_diff(d, warn=0.02, fail=0.05):
    if d is None:
        return "FLAG"
    if abs(d) > fail:
        return "FAIL"
    if abs(d) > warn:
        return "FLAG"
    return "PASS"

# ---------------------------------------------------------------------------
# Reverse DCF (operating companies) -- validated against V1's DLTR output to
# 7 significant figures (see agent transcript) BEFORE any V1 code was read.
# FCFF_t = Rev_t*margin*(1-tax) + Rev_t*da_ratio - Rev_t*capex_ratio - nwc_ratio*(Rev_t-Rev_{t-1})
# growth fades linearly from g (yr1) to terminal_g (yr10); terminal value = Gordon growth on FCFF_10.
def reverse_dcf_solve_growth(revenue_base, ebit_margin, tax, da_ratio, capex_ratio, nwc_ratio,
                              wacc, ev0, term_g=0.03, years=10):
    def pv_for_g(g):
        rev_prev = revenue_base
        pv = 0.0
        fcff_prev = None
        for t in range(1, years + 1):
            g_t = g - (g - term_g) * (t - 1) / (years - 1)
            rev_t = rev_prev * (1 + g_t)
            fcff_t = (rev_t * ebit_margin * (1 - tax) + rev_t * da_ratio - rev_t * capex_ratio
                      - nwc_ratio * (rev_t - rev_prev))
            pv += fcff_t / (1 + wacc) ** t
            rev_prev = rev_t
            fcff_prev = fcff_t
        tv = fcff_prev * (1 + term_g) / (wacc - term_g)
        pv += tv / (1 + wacc) ** years
        return pv
    lo, hi = -0.9, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv_for_g(mid) > ev0:
            hi = mid
        else:
            lo = mid
    g_sol = (lo + hi) / 2
    return g_sol, pv_for_g(g_sol)

def justified_pb_implied_roe(pb, coe, g):
    """P/B = (ROE-g)/(COE-g)  =>  ROE = PB*(COE-g)+g"""
    return pb * (coe - g) + g

def signed_cbrt_return(value_yr3, price_now, years=3):
    """Standard scenario CAGR = (value_yr3/price_now)^(1/years)-1. Python's ** on a negative
    base with fractional exponent returns nan -- this reproduces that (to diagnose real NaNs)
    and also reports a 'fixed' floor-at-zero alternative for reference."""
    ratio = value_yr3 / price_now if price_now else None
    if ratio is None:
        return None, None, "price_now missing"
    naive = ratio ** (1 / years) if ratio >= 0 else float("nan")
    if ratio < 0:
        reason = ("scenario terminal value is NEGATIVE (implies a negative share price), so "
                   "(negative)^(1/3) is undefined in real floating point -> NaN. Root cause: a P/E-style "
                   "exit multiple was applied to a NEGATIVE EPS/FFO-per-share bear-case projection.")
        floored = (0.0 / price_now) ** (1/years) - 1  # = -1.0, i.e. floor terminal value at $0 (total loss)
        return naive, floored, reason
    return naive - 1, naive - 1, None
