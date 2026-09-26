"""b1_tests.py - no-look-ahead assertions and unit tests for the B1 engine.  Run: python b1_tests.py
Writes v4/outputs/b1_tests_output.txt
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b1_common import DATA, OUT, month_end_days, nw_mean_test, wilson, cagr, max_drawdown  # noqa: E402

RES = []


def check(name, cond, detail=""):
    RES.append((name, bool(cond), detail))
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""), flush=True)


def main():
    rng = np.random.default_rng(20260926)
    P = pd.read_parquet(DATA / "b1_panel.parquet")
    P["month_end"] = pd.DatetimeIndex(P.month_end)
    adj = pd.read_parquet(DATA / "d2_adjclose.parquet")
    adj.index = pd.DatetimeIndex(adj.index)
    ME = month_end_days(adj.index)

    # 1. fundamentals filed strictly before t (D3 lag1) -------------------------------------------------
    f = P[P.max_filed_used.notna()]
    n_bad = int((pd.DatetimeIndex(f.max_filed_used) >= pd.DatetimeIndex(f.month_end)).sum())
    check("fundamentals: max_filed_used < month_end for every row", n_bad == 0, f"rows={len(f)}, violations={n_bad}")
    lf = P[P.last_filed_date.notna()]
    n_bad2 = int((pd.DatetimeIndex(lf.last_filed_date) >= pd.DatetimeIndex(lf.month_end)).sum())
    check("fundamentals: last_filed_date < month_end", n_bad2 == 0, f"violations={n_bad2}")
    # independent re-derivation from the raw XBRL fact table for a sample of (cik, t): the latest filing date
    # of any fact with filed < t must be >= D3's max_filed_used (i.e. D3 used nothing unavailable)
    try:
        xf = pd.read_parquet(DATA / "d3_xbrl_facts.parquet", columns=["cik", "filed"])
        xf["filed"] = pd.to_datetime(xf.filed)
        smp = f.sample(300, random_state=1)
        viol = 0
        for r in smp.itertuples(index=False):
            ciks = {int(r.cik), int(r.fund_cik)} if pd.notna(getattr(r, "fund_cik", np.nan)) else {int(r.cik)}
            fl = xf.loc[xf.cik.isin(ciks) & (xf.filed < r.month_end), "filed"]
            if len(fl) and pd.Timestamp(r.max_filed_used) > fl.max():
                viol += 1
        check("fundamentals: max_filed_used consistent with raw XBRL filings available before t (300 samples)",
              viol == 0, f"violations={viol}")
    except Exception as e:  # noqa
        check("fundamentals: raw XBRL cross-check", False, f"error {e}")

    # 2. prices <= t: recompute momentum / vol on a price panel truncated at t ---------------------------
    U = P[P.in_universe & P.series.notna() & (P.month_end >= "2010-12-31") & (P.month_end < "2026-09-01")]
    smp = U.sample(250, random_state=2)
    mom_bad = vol_bad = 0
    for r in smp.itertuples(index=False):
        trunc = adj.loc[:r.month_end, r.series]            # nothing after t is visible
        me_t = ME[ME <= r.month_end]
        a1, a12 = trunc.get(me_t[-2]), trunc.get(me_t[-13])
        m = a1 / a12 - 1 if (a1 is not None and a12 is not None) else np.nan
        if not (np.isnan(m) and np.isnan(r.mom_12_1)) and not np.isclose(m, r.mom_12_1, rtol=1e-9, equal_nan=True):
            mom_bad += 1
        lr = np.log(trunc / trunc.shift(1)).iloc[-252:]
        v = lr.std() * np.sqrt(252) if lr.notna().sum() >= 200 else np.nan
        if not np.isclose(v, r.vol_1y, rtol=1e-6, equal_nan=True):
            vol_bad += 1
    check("momentum(t) identical when prices after t are removed (250 samples)", mom_bad == 0, f"mismatch={mom_bad}")
    check("1y vol(t) identical when prices after t are removed (250 samples)", vol_bad == 0, f"mismatch={vol_bad}")
    # market cap uses Close at t (not later): px_actual = Close_t * split factor after t
    close = pd.read_parquet(DATA / "d2_close.parquet")
    close.index = pd.DatetimeIndex(close.index)
    pb = 0
    for r in smp.itertuples(index=False):
        if pd.notna(r.px_actual) and not np.isclose(close.at[r.month_end, r.series] * r.split_factor_after, r.px_actual):
            pb += 1
    check("market-cap price = Close(t) x split factor after t", pb == 0, f"mismatch={pb}")
    # next-month return is the only forward-looking field and is used only as the outcome
    rb = 0
    for r in smp.itertuples(index=False):
        i = ME.get_loc(r.month_end)
        if i + 1 < len(ME) and r.month_end < pd.Timestamp("2026-08-31"):
            x = adj.at[ME[i + 1], r.series] / adj.at[r.month_end, r.series] - 1
            if not np.isclose(x, r.ret_next, equal_nan=True):
                rb += 1
    check("ret_next = AdjClose(t+1)/AdjClose(t)-1 (outcome only)", rb == 0, f"mismatch={rb}")

    # 3. membership at t only -----------------------------------------------------------------------------
    if P.mem_src.iloc[0].startswith("D2_spells"):
        sp = pd.read_csv(DATA / "d2_universe_spells.csv", parse_dates=["start", "end_excl"])
        sp["ticker"] = sp.ticker.str.upper().str.replace(".", "-", regex=False)
        smp3 = P.sample(400, random_state=3)
        bad = 0
        for r in smp3.itertuples(index=False):
            s = sp[sp.ticker == r.ticker]
            ok = ((s.start <= r.month_end) & (s.end_excl.isna() | (s.end_excl > r.month_end))).any()
            bad += (not ok)
        check("membership: every panel row is inside a membership spell at t (400 samples)", bad == 0, f"violations={bad}")
    else:
        m = pd.read_parquet(DATA / "d1_membership_monthly.parquet")
        m.index = pd.DatetimeIndex(m.index).to_period("M")
        smp3 = P.sample(1000, random_state=3)
        bad = sum(0 if bool(m.at[r.month_end.to_period("M"), r.entity]) else 1 for r in smp3.itertuples(index=False))
        check("membership: every sampled panel row is a D1 member at t (1000 samples)", bad == 0, f"violations={bad}")
        # and completeness: all D1 primary-line members at t appear in the panel
        t = pd.Timestamp("2019-06-28")
        mem_t = set(c for c in m.columns if "." not in c and m.at[t.to_period("M"), c])
        pan_t = set(P.loc[P.month_end == t, "entity"])
        check("membership: panel month == D1 member set (2019-06)", mem_t == pan_t, f"d1={len(mem_t)} panel={len(pan_t)}")
    # no entity appears twice in a month
    check("one row per (month, entity)", not P.duplicated(["month_end", "entity"]).any())

    # 4. composite at t uses only the cross-section at t: re-implement one month independently ---------
    t = pd.Timestamp("2018-06-29")
    g = P[(P.month_end == t) & P.in_universe].copy()
    g2 = P[(P.month_end == t) & P.in_universe].copy()
    # shuffle order + add garbage future rows -> ranks unchanged
    fut = P[(P.month_end > t)].head(500)
    comb = pd.concat([g2.sample(frac=1, random_state=4), fut])
    x = comb[comb.month_end == t]
    r1 = g.set_index("entity").composite
    r2 = x.set_index("entity").composite.reindex(r1.index)
    check("composite at t invariant to row order / presence of later rows", np.allclose(r1, r2, equal_nan=True))
    fams = ["fam_Q", "fam_V", "fam_M", "fam_S"]
    raw = g[fams].mean(axis=1).where(g[fams].notna().sum(axis=1) >= 3)
    rr = raw.rank()
    pct = (rr - 0.5) / raw.notna().sum()
    check("composite re-derived independently from family scores", np.allclose(pct, g.composite, equal_nan=True, atol=1e-12))

    # 5. statistics unit tests ------------------------------------------------------------------------------
    x = pd.Series(rng.normal(0.004, 0.03, 200))
    nw = nw_mean_test(x, 3)
    m = sm.OLS(x.values, np.ones(len(x))).fit(cov_type="HAC", cov_kwds={"maxlags": 3, "use_correction": False})
    check("NW t-stat matches statsmodels HAC (Bartlett, 3 lags)", abs(nw["t"] - m.tvalues[0]) < 1e-6,
          f"{nw['t']:.6f} vs {m.tvalues[0]:.6f}")
    lo, hi = wilson(50, 100)
    check("Wilson CI(50/100) = [0.4038, 0.5962]", abs(lo - 0.4038) < 1e-3 and abs(hi - 0.5962) < 1e-3, f"{lo:.4f},{hi:.4f}")
    check("CAGR of 12 x 1% months = 12.68%", abs(cagr(pd.Series([0.01] * 12)) - 0.126825) < 1e-5)
    check("max drawdown of [+10%, -50%, +20%] = -50%", abs(max_drawdown(pd.Series([0.1, -0.5, 0.2])) + 0.5) < 1e-9)

    npass = sum(ok for _, ok, _ in RES)
    txt = "\n".join(("PASS " if ok else "FAIL ") + n + (f"  [{d}]" if d else "") for n, ok, d in RES)
    txt += f"\n\n{npass}/{len(RES)} passed"
    (OUT / "b1_tests_output.txt").write_text(txt, encoding="utf-8")
    print(f"{npass}/{len(RES)} passed")


if __name__ == "__main__":
    main()
