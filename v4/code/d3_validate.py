"""d3_validate.py - validation of the D3 PIT fundamentals.

(a) FY revenue / net income vs legacy Yahoo statements (PROJECT/equity_project/fund_all.pkl): 25 named large caps
    (tolerance 1%) + the same test on every legacy ticker (broad check). XBRL value = as-first-reported OR latest
    restated annual value (both reported).
(b) Coverage by month: share of that month's S&P 500 constituents (fja snapshots; Wikipedia for 2026-09) with
    non-missing rev_ttm, ni_ttm, assets, equity, ocf_ttm, eps history (>=8 quarters) and sue.
(c) Restatement spot-check (AAPL FY2009 10-K vs 10-K/A) + automatic scan for other restatements.
(d) PIT leakage tests: max_filed_used <= month_end on every row; truncation test (recompute features from facts
    filed <= t only and compare with the panel); perturbation test (facts filed after t multiplied by 1000).
(e) Extras: split detection vs D2 Yahoo splits; month-over-month scale glitches.
Outputs: v4/outputs/d3_validation.json, d3_validation_fy_compare.csv, d3_coverage_monthly.csv
"""
from __future__ import annotations

import json
import random
from multiprocessing import Pool

import numpy as np
import pandas as pd

from d3_common import CACHE, DATA, LEGACY, OUT, PANEL_FORMS, month_ends, utcnow_iso

NAMED = ["AAPL", "MSFT", "JPM", "XOM", "JNJ", "WMT", "PG", "NVDA", "HD", "UNH", "KO", "PEP", "CSCO", "INTC", "ORCL",
         "BAC", "CVX", "MRK", "PFE", "ABT", "MCD", "NKE", "CAT", "HON", "V"]


def _facts_for(cik, facts, chains, first_filed):
    parts = [facts[cik]]
    cur, seen = cik, {cik}
    while cur in chains and chains[cur] in facts and chains[cur] not in seen:
        p = chains[cur]
        parts.append(facts[p][facts[p]["filed"] < first_filed[cur]])
        seen.add(p)
        cur = p
    return pd.concat(parts, ignore_index=True)


def annual_versions(args):
    """Run the engine; record for every annual period (350-380d) of revenue / NI the first-reported and latest value."""
    ticker, cik, fc = args
    from d3_pit_core import CompanyEngine, FLOW_SPECS, YMIN, YMAX
    eng = CompanyEngine(fc)
    rec = {}
    for i, E in enumerate(eng.events):
        eng.apply(E)
        for name, pool in (("rev", eng.rev_pool()), ("ni", eng.merged_dur(FLOW_SPECS["ni"]))):
            for (s, e), (v, f) in pool.items():
                if YMIN <= e - s <= YMAX:
                    k = (name, e)
                    if k not in rec:
                        rec[k] = {"first": v, "first_filed": f, "latest": v, "latest_filed": f}
                    elif f >= rec[k]["latest_filed"]:
                        rec[k]["latest"], rec[k]["latest_filed"] = v, f
    out = []
    for (name, e), d in rec.items():
        out.append({"ticker": ticker, "cik": cik, "item": name, "fy_end": pd.Timestamp("1970-01-01") + pd.Timedelta(days=e),
                    **{k: (v if "filed" not in k else pd.Timestamp("1970-01-01") + pd.Timedelta(days=v)) for k, v in d.items()}})
    return out


def check_a(facts, chains, first_filed, univ):
    leg = pd.read_pickle(LEGACY / "fund_all.pkl")
    t2c = {}
    for r in univ.itertuples():
        for t in str(r.tickers_all).split(";"):
            t2c.setdefault(t, int(r.cik))
    jobs = [(t, t2c[t], _facts_for(t2c[t], facts, chains, first_filed)) for t in leg if t in t2c and t2c[t] in facts]
    with Pool(12) as pool:
        res = pool.map(annual_versions, jobs, chunksize=4)
    xb = pd.DataFrame([r for rr in res for r in rr])
    rows = []
    for t, d in leg.items():
        inc = d["inc"]
        for item, yname in (("rev", "Total Revenue"), ("ni", "Net Income")):
            if yname not in inc.index:
                continue
            for c in inc.columns:
                yv = inc.loc[yname, c]
                if pd.isna(yv) or yv == 0:
                    continue
                x = xb[(xb.ticker == t) & (xb.item == item)] if len(xb) else xb
                x = x[(x.fy_end - pd.Timestamp(c)).abs().dt.days <= 7] if len(x) else x
                row = {"ticker": t, "item": item, "fy_end_yahoo": pd.Timestamp(c).date(), "yahoo": float(yv)}
                if len(x):
                    x = x.iloc[0]
                    row.update({"xbrl_first": x["first"], "first_filed": x["first_filed"].date(), "xbrl_latest": x["latest"],
                                "latest_filed": x["latest_filed"].date()})
                    rf, rl = abs(x["first"] / yv - 1), abs(x["latest"] / yv - 1)
                    row.update({"rel_err_first": rf, "rel_err_latest": rl, "match_1pct": bool(min(rf, rl) <= 0.01),
                                "match_5pct": bool(min(rf, rl) <= 0.05)})
                else:
                    row.update({"match_1pct": False, "match_5pct": False, "missing_xbrl": True})
                rows.append(row)
    cmp_ = pd.DataFrame(rows)
    cmp_["named25"] = cmp_["ticker"].isin(NAMED)
    cmp_.to_csv(OUT / "d3_validation_fy_compare.csv", index=False)
    summ = {}
    for scope, df in (("named25", cmp_[cmp_.named25]), ("all_legacy", cmp_)):
        for item in ("rev", "ni"):
            d = df[df.item == item]
            summ[f"{scope}_{item}"] = {"n": int(len(d)), "pass_1pct": int(d.match_1pct.sum()),
                                       "pass_rate_1pct": round(float(d.match_1pct.mean()), 4),
                                       "pass_rate_5pct": round(float(d.match_5pct.mean()), 4),
                                       "missing_xbrl": int(d.get("missing_xbrl", pd.Series(dtype=bool)).fillna(False).sum())}
    fails = cmp_[cmp_.named25 & ~cmp_.match_1pct].copy()
    return summ, fails


def check_b(panel, univ, first_filed, last_filed, chains):
    mem = pd.read_parquet(CACHE / "membership_monthly.parquet")
    tmap = pd.read_csv(DATA / "d3_ticker_cik_map.csv")
    t2c = {t: c for t, c in zip(tmap["ticker"], tmap["cik"]) if pd.notna(c)}
    # extra CIKs registered via d3_pull --ciks-from (e.g. D1 map): use their tickers for still-unmapped tickers
    ex = DATA / "d3_universe_extra_d1.csv"
    if ex.exists():
        e = pd.read_csv(ex)
        for tks, c in zip(e["tickers_all"].astype(str), e["cik"]):
            for t in tks.split(";"):
                t = t.strip().upper().replace(".", "-")
                if t and t != "NAN" and t not in t2c:
                    t2c[t] = int(c)
    # lineage-aware, date-validated resolution of (ticker, month) -> CIK
    rev_chain = chains
    key = panel.set_index(["month_end", "cik"])
    cols = {"rev_ttm": "rev_ttm", "ni_ttm": "ni_ttm", "assets": "assets", "equity": "equity", "ocf_ttm": "ocf_ttm"}
    mem["cik0"] = mem["ticker"].map(t2c)
    res = []
    for (t, tk, c0) in zip(mem["month_end"], mem["ticker"], mem["cik0"]):
        if pd.isna(c0):
            res.append((None, "unmapped"))
            continue
        c = int(c0)
        # walk back the lineage while t precedes the current entity's first periodic filing
        while c in rev_chain and c in first_filed and t < first_filed[c] and rev_chain[c] in first_filed:
            c = rev_chain[c]
        ff, lf = first_filed.get(c), last_filed.get(c)
        if ff is None:
            res.append((None, "no_xbrl"))
        elif t < ff - pd.Timedelta(days=900) or t > lf + pd.Timedelta(days=400):
            res.append((None, "mapping_invalid_for_date"))   # ticker re-use / company not filing at t
        else:
            res.append((c, "mapped"))
    mem["cik"] = [r[0] for r in res]
    mem["map_status"] = [r[1] for r in res]
    # lineage walk-back conflicts: two tickers resolving to the same CIK in the same month (e.g. DD and DOW both walking
    # back to Dow Chemical) -> keep the ticker that labels that CIK in the panel, the other becomes unmapped
    lab = panel.drop_duplicates("cik").set_index("cik")["ticker"].to_dict()
    mm_ = mem[mem["cik"].notna()]
    n0 = mm_.groupby(["month_end", "cik"])["cik0"].transform("nunique")   # different starting CIKs (not share classes)
    dup = mm_.index[n0 > 1]
    bad = [i for i in dup if lab.get(int(mem.at[i, "cik"])) != mem.at[i, "ticker"]]
    mem.loc[bad, "cik"] = None
    mem.loc[bad, "map_status"] = "lineage_conflict"
    m = mem.merge(panel[["month_end", "cik"] + list(cols) + ["n_eps_q", "sue"]], on=["month_end", "cik"], how="left")
    m["eps_hist8"] = m["n_eps_q"].fillna(0) >= 8
    feats = list(cols) + ["eps_hist8", "sue"]
    for f in feats:
        m[f + "_ok"] = m[f].notna() if f != "eps_hist8" else m[f]
    g = m.groupby("month_end")
    cov = pd.DataFrame({"n_constituents": g.size(), "n_mapped": g["map_status"].apply(lambda s: (s == "mapped").sum())})
    for f in feats:
        cov[f"pct_{f}"] = g[f + "_ok"].mean()
    mm = m[m.map_status == "mapped"]
    gm = mm.groupby("month_end")
    for f in feats:
        cov[f"pct_mapped_{f}"] = gm[f + "_ok"].mean()
    cov = cov.reset_index()
    cov.to_csv(OUT / "d3_coverage_monthly.csv", index=False)
    cov["year"] = pd.to_datetime(cov["month_end"]).dt.year
    by_year = cov.groupby("year").mean(numeric_only=True).round(4)
    unm = m[m.map_status != "mapped"].groupby("ticker").agg(months=("month_end", "size"), status=("map_status", "first"),
                                                           last=("month_end", "max")).sort_values("months", ascending=False)
    return cov, by_year, unm


def check_c(panel, facts, univ):
    out = {}
    aapl = 320193
    p = panel[(panel.cik == aapl) & (panel.month_end.between("2009-09-01", "2010-03-31"))][
        ["month_end", "rev_ttm", "rev_ttm_end", "rev_ttm_src", "last_filed_date", "last_form"]]
    f = facts[aapl]
    f = f[(f.concept.astype(str).isin(["SalesRevenueNet", "Revenues"])) & (f.end == "2009-09-26") &
          (f.start == "2008-09-28")][["concept", "val", "form", "filed", "accn"]].sort_values("filed")
    out["aapl_fy2009_versions"] = f.astype(str).to_dict("records")
    out["aapl_panel"] = p.astype(str).to_dict("records")
    orig = f.iloc[0]
    rest = f[f.val != orig.val]
    ok = True
    if len(rest):
        rd = rest.iloc[0].filed
        before = p[(p.month_end >= orig.filed) & (p.month_end < rd) & (p.rev_ttm_end == "2009-09-26")]
        after = p[(p.month_end >= rd) & (p.rev_ttm_end == "2009-09-26")]
        ok = bool(len(before) and (before.rev_ttm == orig.val).all() and len(after) and (after.rev_ttm == rest.iloc[0].val).all())
        out["aapl_check"] = {"original": float(orig.val), "original_filed": str(orig.filed.date()), "original_form": orig.form,
                             "restated": float(rest.iloc[0].val), "restated_filed": str(rd.date()),
                             "restated_form": rest.iloc[0].form, "months_using_original": [str(x.date()) for x in before.month_end],
                             "months_using_restated": [str(x.date()) for x in after.month_end], "pass": ok}
    # automatic scan: annual NetIncomeLoss / Revenues periods restated by >2% in a later 10-K/A or comparative
    allf = pd.concat([v for v in facts.values()], ignore_index=True)
    a = allf[allf.concept.astype(str).isin(["NetIncomeLoss", "Revenues"]) & allf.start.notna()]
    a = a[((a.end - a.start).dt.days.between(350, 380)) & a.form.astype(str).isin(PANEL_FORMS)]
    g = a.sort_values("filed").groupby(["cik", "concept", "start", "end"], observed=True)["val"].agg(["first", "last", "count"])
    g = g[(g["count"] > 1) & ((g["last"] / g["first"] - 1).abs() > 0.02)]
    out["n_restated_annual_periods_scan"] = int(len(g))
    out["n_companies_with_restated_annual"] = int(g.index.get_level_values(0).nunique())
    return out, ok


def recompute_row(args):
    cik, fc, t, strict = args
    from d3_pit_core import CompanyEngine, to_monthly
    tt = pd.Timestamp(t)
    fc2 = fc[(fc.filed < tt) if strict else (fc.filed <= tt)]
    if fc2.empty:
        return cik, t, None
    eng = CompanyEngine(fc2)
    st, es = eng.run()
    p, _ = to_monthly(st, es, [tt], cik, None, strict=strict)
    return cik, t, (p.iloc[0].to_dict() if len(p) else None)


def perturb_row(args):
    cik, fc, t = args
    from d3_pit_core import CompanyEngine, to_monthly
    tt = pd.Timestamp(t)
    fc2 = fc.copy()
    fut = fc2.filed > tt
    fc2.loc[fut, "val"] = fc2.loc[fut, "val"] * 1000.0 + 7.0
    eng = CompanyEngine(fc2)
    st, es = eng.run()
    p, _ = to_monthly(st, es, [tt], cik, None)
    return cik, t, (p.iloc[0].to_dict() if len(p) else None)


FEATS_CMP = ["rev_ttm", "gp_ttm", "opinc_ttm", "ni_ttm", "ocf_ttm", "capex_ttm", "assets", "assets_1y_ago", "equity",
             "liabilities", "cash_sti", "total_debt", "shares_out", "shares_1y_ago", "eps_q0", "eps_q4", "sue"]


def _same(a, b):
    if pd.isna(a) and pd.isna(b):
        return True
    if pd.isna(a) or pd.isna(b):
        return False
    return abs(a - b) <= 1e-9 * max(1.0, abs(a), abs(b))


def check_d(panel, facts, chains, first_filed, n_cos=40, n_dates=5, seed=7):
    out = {"rows": int(len(panel)),
           "rows_max_filed_used_after_t": int((panel["max_filed_used"] > panel["month_end"]).sum()),
           "rows_last_filed_after_t": int((panel["last_filed_date"] > panel["month_end"]).sum())}
    rnd = random.Random(seed)
    # only CIKs without lineage enrichment (panel rows depend on predecessor facts otherwise)
    ciks = sorted(set(panel.cik) - set(chains))
    sample = rnd.sample(ciks, min(n_cos, len(ciks)))
    jobs, pj = [], []
    for c in sample:
        mes = sorted(panel.loc[panel.cik == c, "month_end"])
        for t in rnd.sample(mes, min(n_dates, len(mes))):
            jobs.append((c, facts[c], t, False))
            pj.append((c, facts[c], t))
    with Pool(12) as pool:
        trunc = pool.map(recompute_row, jobs, chunksize=2)
        pert = pool.map(perturb_row, pj, chunksize=2)
    key = panel.set_index(["cik", "month_end"])
    n_cmp = n_bad = 0
    bad = []
    for label, res in (("truncation", trunc), ("perturbation", pert)):
        for c, t, row in res:
            ref = key.loc[(c, t)]
            for f in FEATS_CMP:
                n_cmp += 1
                if row is None or not _same(ref[f], row[f]):
                    n_bad += 1
                    bad.append((label, int(c), str(pd.Timestamp(t).date()), f, ref[f], None if row is None else row[f]))
    out.update({"n_company_dates_tested": len(jobs), "n_feature_comparisons": n_cmp, "n_mismatches": n_bad,
                "mismatch_examples": [list(map(str, b)) for b in bad[:20]]})
    return out


def check_e(panel, univ):
    out = {}
    try:
        sp = pd.read_parquet(DATA / "d2_splits.parquet")
        sp = sp[(sp["date"] >= "2010-06-01") & (sp["date"] <= "2026-06-30")]
        nice = lambda r: any(abs(r / c - 1) < 0.01 for c in [2, 3, 4, 5, 6, 7, 8, 10, 15, 20, 1.5, 1.25, 4 / 3, 0.5, 0.2, 0.1,
                                                              1 / 3, 0.25, 1 / 15, 1 / 20, 1 / 8, 2.5])
        sp = sp[sp["split_ratio"].map(nice)]
        cur = univ[univ.in_wiki_current == True]
        t2c = dict(zip(cur["ticker"], cur["cik"].astype(int)))
        sp = sp[sp["ticker"].isin(t2c)]
        det = panel.groupby("cik")["n_splits_detected"].max()
        hits = 0
        for r in sp.itertuples():
            c = t2c[r.ticker]
            hits += int(det.get(c, 0) > 0)
        out["d2_nice_splits_2010_2026_current"] = int(len(sp))
        out["d2_splits_with_xbrl_detection_in_same_company"] = hits
    except Exception as e:  # D2 file may be absent
        out["d2_split_check_error"] = repr(e)
    p = panel.sort_values(["cik", "month_end"])
    r = p.groupby("cik")["rev_ttm"].pct_change(fill_method=None).abs()
    out["rev_ttm_mom_change_gt_10x"] = int((r > 9).sum())
    s = p.groupby("cik")["shares_out"].pct_change(fill_method=None).abs()
    out["shares_mom_change_gt_3x"] = int((s > 2).sum())
    return out


def main():
    import d3_extract
    from d3_build_pit import lineage_chains
    univ = d3_extract.universe_all()
    f = pd.read_parquet(DATA / "d3_xbrl_facts.parquet",
                        columns=["cik", "concept", "unit", "val", "start", "end", "filed", "form", "accn"])
    f = f[f["form"].astype(str).isin(PANEL_FORMS)]
    facts = {int(k): g for k, g in f.groupby("cik", sort=False)}
    first_filed = {c: g["filed"].min() for c, g in facts.items()}
    last_filed = {c: g["filed"].max() for c, g in facts.items()}
    chains, _ = lineage_chains()
    panel = pd.read_parquet(DATA / "d3_pit_monthly.parquet")
    res = {"run_utc": utcnow_iso()}
    print("[validate] (a) FY revenue / NI vs Yahoo ...", flush=True)
    res["a_fy_vs_yahoo"], fails = check_a(facts, chains, first_filed, univ)
    res["a_named25_failures"] = fails.astype(str).to_dict("records")
    print(json.dumps(res["a_fy_vs_yahoo"], indent=1), flush=True)
    print("[validate] (b) coverage ...", flush=True)
    cov, by_year, unm = check_b(panel, univ, first_filed, last_filed, chains)
    res["b_coverage_by_year"] = by_year.reset_index().to_dict("records")
    res["b_unmapped_top"] = unm.head(40).reset_index().astype(str).to_dict("records")
    print(by_year.to_string(), flush=True)
    print("[validate] (c) restatement ...", flush=True)
    res["c_restatement"], ok = check_c(panel, facts, univ)
    print(json.dumps(res["c_restatement"].get("aapl_check"), indent=1), flush=True)
    print("[validate] (d) PIT leakage ...", flush=True)
    res["d_pit_leakage"] = check_d(panel, facts, chains, first_filed)
    print(json.dumps({k: v for k, v in res["d_pit_leakage"].items() if k != "mismatch_examples"}), flush=True)
    res["e_extras"] = check_e(panel, univ)
    print(json.dumps(res["e_extras"]), flush=True)
    with open(OUT / "d3_validation.json", "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=str)


if __name__ == "__main__":
    main()
