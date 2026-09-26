"""d3_build_pit.py - build the point-in-time monthly fundamental panel from d3_xbrl_facts.parquet.

Outputs (v4/data):
  d3_pit_monthly.parquet        month_end x CIK features, facts with filed <= month_end   (as specified)
  d3_pit_monthly_lag1.parquet   same, facts with filed <  month_end (= filed + 1 trading day <= t; CONVENTIONS backtest rule)
  d3_eps_quarterly_pit.parquet  long table: month_end, cik, q (0..12), period_end, split-adjusted diluted EPS, filed, derived
Per-CIK shards: C:/Users/user/eqv4/cache/d3/pit_shards (re-runs only build missing CIKs; --rebuild to redo all).

Lineage: a successor CIK's state is enriched with its predecessor chain's facts filed before the successor's first
periodic filing (d3_lineage.csv). Successor rows start at its own first filing; predecessor rows stop when the
successor starts filing, so each lineage has one active row per month.
"""
from __future__ import annotations

import sys
import time
from multiprocessing import Pool

import numpy as np
import pandas as pd

from d3_common import DATA, PANEL_FORMS, PIT_SHARDS, month_ends, utcnow_iso, write_meta

MONTH_ENDS = month_ends()


def lineage_chains():
    p = DATA / "d3_lineage.csv"
    if not p.exists():
        return {}, {}
    lin = pd.read_csv(p)
    if "co_registrant" in lin:
        lin = lin[~lin["co_registrant"].astype(bool)]
    lin = lin.sort_values(["n_matches", "predecessor_first_filed"], ascending=[False, True])
    prim = {}
    for r in lin.itertuples():
        prim.setdefault(int(r.successor_cik), int(r.predecessor_cik))
    succ = {}
    for s, pcik in prim.items():
        succ.setdefault(pcik, []).append(s)
    return prim, succ


def build_one(args):
    cik, ticker, fc, chain, is_fin, row_start, row_end, rebuild = args
    from d3_pit_core import CompanyEngine, to_monthly
    out_main = PIT_SHARDS / f"{cik}.parquet"
    if out_main.exists() and not rebuild:
        return cik, "cached", 0
    t0 = time.time()
    parts = [fc]
    for pcik, pfc, cutoff in chain:
        parts.append(pfc[pfc["filed"] < cutoff])
    allf = pd.concat(parts, ignore_index=True) if len(parts) > 1 else fc
    eng = CompanyEngine(allf, is_financial_sic=is_fin)
    states, eps_states = eng.run()
    # restrict rows to [row_start, row_end)
    keep = [i for i, (E, _) in enumerate(states)]
    me = [t for t in MONTH_ENDS if (row_start is None or t >= row_start) and (row_end is None or t < row_end)]
    panel, eps = to_monthly(states, eps_states, me, cik, ticker, strict=False)
    lag1, _ = to_monthly(states, eps_states, me, cik, ticker, strict=True)
    for df in (panel, lag1):
        if len(df):
            df["lineage_ciks"] = ";".join([str(cik)] + [str(p) for p, _, _ in chain]) if chain else str(cik)
            df["n_splits_detected"] = len(eng.splits)
    panel.to_parquet(out_main, index=False)
    lag1.to_parquet(PIT_SHARDS / f"{cik}_lag1.parquet", index=False)
    eps.to_parquet(PIT_SHARDS / f"{cik}_eps.parquet", index=False)
    return cik, f"{len(panel)} rows {time.time() - t0:.1f}s", len(panel)


def main(rebuild: bool = False, only=None, workers: int = 12):
    import d3_extract
    u = d3_extract.universe_all()
    facts = pd.read_parquet(DATA / "d3_xbrl_facts.parquet",
                            columns=["cik", "concept", "unit", "val", "start", "end", "filed", "form", "accn"])
    facts = facts[facts["form"].astype(str).isin(PANEL_FORMS)]
    groups = {int(k): g for k, g in facts.groupby("cik", sort=False)}
    first_filed = {c: g["filed"].min() for c, g in groups.items()}
    meta = pd.read_csv(DATA / "d3_company_meta.csv")
    sic = dict(zip(meta["cik"].astype(int), pd.to_numeric(meta["sic"], errors="coerce")))
    prim, succ = lineage_chains()

    jobs = []
    for r in u.drop_duplicates("cik").itertuples():
        cik = int(r.cik)
        if cik not in groups or (only and cik not in only):
            continue
        chain, cur, seen = [], cik, {cik}
        while cur in prim and prim[cur] in groups and prim[cur] not in seen:
            pcik = prim[cur]
            chain.append((pcik, groups[pcik], first_filed[cur]))
            seen.add(pcik)
            cur = pcik
        s = sic.get(cik)
        is_fin = bool(s is not None and not np.isnan(s) and 6000 <= s <= 6499)
        row_start = first_filed[cik] if chain else None   # successor rows start at its OWN first periodic filing
        row_end = None
        if cik in succ:   # predecessor: stop rows when its (earliest) successor starts filing
            ss = [first_filed[x] for x in succ[cik] if x in first_filed]
            if ss:
                row_end = min(ss)
        tk = r.ticker if isinstance(r.ticker, str) else None
        jobs.append((cik, tk, groups[cik], chain, is_fin, row_start, row_end, rebuild))
    print(f"[build] {len(jobs)} CIKs ({sum(1 for j in jobs if j[3])} with predecessor chains)", flush=True)
    t0 = time.time()
    with Pool(workers) as pool:
        for i, (cik, msg, n) in enumerate(pool.imap_unordered(build_one, jobs, chunksize=2)):
            if (i + 1) % 100 == 0:
                print(f"[build] {i + 1}/{len(jobs)} {time.time() - t0:.0f}s", flush=True)
    assemble([j[0] for j in jobs], u)


def assemble(ciks, u):
    t0 = time.time()
    outs = {}
    for suffix, name in [("", "d3_pit_monthly"), ("_lag1", "d3_pit_monthly_lag1"), ("_eps", "d3_eps_quarterly_pit")]:
        parts = []
        for c in ciks:
            p = PIT_SHARDS / f"{c}{suffix}.parquet"
            if p.exists():
                df = pd.read_parquet(p)
                if len(df):
                    parts.append(df)
        df = pd.concat(parts, ignore_index=True)
        df = df.sort_values(["month_end", "cik"] + (["q"] if suffix == "_eps" else [])).reset_index(drop=True)
        if suffix != "_eps":
            src = dict(zip(u["cik"].astype(int), u["source"]))
            df["universe_source"] = df["cik"].map(src)
            for c in ("rev_ttm_src", "ebit_src", "liabilities_src", "debt_src", "shares_src", "last_form", "ticker",
                      "lineage_ciks", "universe_source"):
                if c in df:
                    df[c] = df[c].astype("string")
            # hard PIT assertion
            if suffix == "":
                assert (df["max_filed_used"].isna() | (df["max_filed_used"] <= df["month_end"])).all()
                assert (df["last_filed_date"] <= df["month_end"]).all()
            else:
                assert (df["max_filed_used"].isna() | (df["max_filed_used"] < df["month_end"])).all()
        out = DATA / f"{name}.parquet"
        df.to_parquet(out, index=False, compression="zstd")
        outs[name] = df
        print(f"[assemble] {name}: {len(df):,} rows x {df.shape[1]} cols ({time.time() - t0:.0f}s)", flush=True)
    p = outs["d3_pit_monthly"]
    feat_cov = {c: float(p[c].notna().mean()) for c in p.columns if p[c].dtype.kind in "fi"}
    common = {"source": "v4/data/d3_xbrl_facts.parquet (SEC XBRL companyfacts, https://data.sec.gov/api/xbrl/companyfacts/)",
              "built_utc": utcnow_iso(), "code": ["v4/code/d3_pit_core.py", "v4/code/d3_build_pit.py"],
              "month_ends": f"{MONTH_ENDS[0].date()}..{MONTH_ENDS[-1].date()} (last NYSE trading day; 2026-09 = 2026-09-25)"}
    write_meta(DATA / "d3_pit_monthly.parquet", {
        **common, "rows": len(p), "columns": list(p.columns), "n_ciks": int(p["cik"].nunique()),
        "pit_rule": "features at month_end t use only facts with filed <= t (latest version filed <= t per period)",
        "non_missing_share": feat_cov,
        "key_definitions": {
            "*_ttm": "sum of latest 4 consecutive fiscal quarters (quarters derived from 3M facts or YTD differences) "
                     "or latest annual (350-380 day) value if it ends at least as late",
            "rev_ttm": "per period: RevenuesNetOfInterestExpense > Revenues > RegulatedAndUnregulatedOperatingRevenue > "
                       "RevenueFromContract(Excl>Incl)AssessedTax(+RevenueNotFromContract) > SalesRevenueNet > Goods+Services; "
                       "candidate matching GrossProfit+COGS (or OperatingIncome+CostsAndExpenses) within 1.5% preferred; "
                       "banks: NII+noninterest income; REITs: + lease income",
            "shares_out": "dei:EntityCommonStockSharesOutstanding (fresh, plausible) > CommonStockSharesOutstanding > "
                          "weighted diluted; split-adjusted to the latest basis known at t",
            "sue": "(eps_q0-eps_q4)/std(eps_q(i)-eps_q(i+4), i=1..8, ddof=1); >=6 differences; split-adjusted",
            "staleness_days": "month_end - last_period_end",
        },
        "caveats": ["XBRL starts mid-2009 (large accelerated filers) / mid-2011 (all): TTM coverage builds up 2010-2012",
                    "IFRS 20-F filers not covered; banks/insurers lack gross profit / current assets (is_financial flag)",
                    "rows exist only for CIKs in d3 universe (current + fja historical mapped via SEC current tickers "
                    "+ lineage predecessors [+ D1 extras]) - delisted companies not in that map are absent",
                    "backtests should prefer d3_pit_monthly_lag1 (filed < t) per CONVENTIONS"]})
    write_meta(DATA / "d3_pit_monthly_lag1.parquet", {**common, "rows": len(outs["d3_pit_monthly_lag1"]),
               "columns": list(outs["d3_pit_monthly_lag1"].columns),
               "pit_rule": "features at month_end t use only facts with filed < t (i.e. filed + 1 trading day <= t)"})
    e = outs["d3_eps_quarterly_pit"]
    write_meta(DATA / "d3_eps_quarterly_pit.parquet", {**common, "rows": len(e), "columns": list(e.columns),
               "definition": "for each month_end t and CIK: latest 13 fiscal quarters (q=0 latest .. 12) of diluted EPS "
                             "known at t (filed <= t), aligned by period end (q_i ends ~i*91d before q0, +-20d), "
                             "split-adjusted to the share basis known at t; derived=True when from YTD differences "
                             "(e.g. Q4 = FY - 9M)"})


if __name__ == "__main__":
    main(rebuild="--rebuild" in sys.argv)
