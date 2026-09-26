"""d3_extract.py - extract selected XBRL concepts from cached companyfacts JSON into a long table.

Output
  v4/data/d3_xbrl_facts.parquet   columns: cik, ticker, taxonomy, concept, unit, val, start, end, fy, fp, form,
                                  filed, frame, accn, requested (bool: concept in the requested list vs extra fallback)
  v4/data/d3_company_meta.csv     one row per CIK from the SEC submissions JSON (name, SIC, FYE, filer category, ...)
Per-CIK shards are cached in CACHE/facts_shards so re-runs only process new CIKs (use --rebuild to redo all).
"""
from __future__ import annotations

import sys

import pandas as pd

from d3_common import (ALL_CONCEPTS, CF_DIR, DATA, FACT_SHARDS, REQUESTED_CONCEPTS, SUB_DIR, cik10,
                       read_gz_json, utcnow_iso, write_meta)

WANTED = {}
for c in ALL_CONCEPTS:
    tax, name = (c.split(":", 1) if ":" in c else ("us-gaap", c))
    WANTED[(tax, name)] = c in REQUESTED_CONCEPTS

SCHEMA_COLS = ["cik", "taxonomy", "concept", "unit", "val", "start", "end", "fy", "fp", "form", "filed", "frame",
               "accn", "requested"]


def extract_one(cik: int) -> pd.DataFrame:
    p = CF_DIR / f"CIK{cik10(cik)}.json.gz"
    j = read_gz_json(p)
    rows = []
    facts = j.get("facts", {})
    for (tax, name), req in WANTED.items():
        node = facts.get(tax, {}).get(name)
        if not node:
            continue
        for unit, xs in node.get("units", {}).items():
            for x in xs:
                rows.append((cik, tax, name, unit, x.get("val"), x.get("start"), x.get("end"), x.get("fy"), x.get("fp"),
                             x.get("form"), x.get("filed"), x.get("frame"), x.get("accn"), req))
    df = pd.DataFrame(rows, columns=SCHEMA_COLS)
    if len(df):
        df["val"] = pd.to_numeric(df["val"], errors="coerce").astype("float64")
        for c in ("start", "end", "filed"):
            df[c] = pd.to_datetime(df[c], errors="coerce")
        df["fy"] = pd.to_numeric(df["fy"], errors="coerce").astype("Int16")
        df["cik"] = df["cik"].astype("int64")
    return df


def company_meta(cik: int) -> dict:
    p = SUB_DIR / f"CIK{cik10(cik)}.json.gz"
    if not p.exists():
        return {"cik": cik}
    j = read_gz_json(p)
    fn = j.get("formerNames") or []
    return {"cik": cik, "sec_name": j.get("name"), "sic": j.get("sic"), "sic_description": j.get("sicDescription"),
            "entity_type": j.get("entityType"), "category": j.get("category"), "fiscal_year_end": j.get("fiscalYearEnd"),
            "state_of_incorporation": j.get("stateOfIncorporation"), "sec_tickers": ";".join(j.get("tickers") or []),
            "sec_exchanges": ";".join([e or "" for e in (j.get("exchanges") or [])]),
            "former_names": " | ".join(f"{x.get('name')} ({str(x.get('from'))[:10]}..{str(x.get('to'))[:10]})" for x in fn)}


def universe_all(with_lineage: bool = True) -> pd.DataFrame:
    """D3 universe = current + fja-historical (d3_universe.csv) + D1 extras + lineage predecessors (d3_lineage.csv)."""
    u = pd.read_csv(DATA / "d3_universe.csv")
    extra = DATA / "d3_universe_extra_d1.csv"
    if extra.exists():
        e = pd.read_csv(extra)
        u = pd.concat([u, e[~e["cik"].isin(u["cik"])]], ignore_index=True)
    lin_p = DATA / "d3_lineage.csv"
    if with_lineage and lin_p.exists():
        lin = pd.read_csv(lin_p)
        if "co_registrant" in lin:
            lin = lin[~lin["co_registrant"].astype(bool)]
        # keep only PRIMARY predecessors (same rule as d3_build_pit.lineage_chains: most matches, then earliest filer)
        lin = lin.sort_values(["n_matches", "predecessor_first_filed"], ascending=[False, True])
        lin = lin.drop_duplicates("successor_cik", keep="first")
        t_of = dict(zip(u["cik"].astype(int), u["ticker"]))
        add = []
        # walk chains so that deeper predecessors inherit the ticker of the ultimate successor in the universe
        import re
        tok = lambda s: set(re.findall(r"[a-z]{3,}", str(s).lower())) - {"inc", "corp", "corporation", "company", "ltd",
                                                                         "plc", "holdings", "group", "the", "limited"}
        succ_of = {}
        # label a predecessor with the successor whose name is most similar (e.g. Dow Chemical -> Dow Inc., not DuPont)
        for pc, g in lin.groupby("predecessor_cik"):
            pn = tok(g["predecessor_name"].iloc[0])
            best = max(g.itertuples(), key=lambda r: (len(pn & tok(r.successor_name)) / max(1, len(pn | tok(r.successor_name))),
                                                      r.n_matches))
            succ_of[int(pc)] = int(best.successor_cik)
        for pc in succ_of:
            if pc in t_of:
                continue
            s, seen = succ_of[pc], set()
            while s not in t_of and s in succ_of and s not in seen:
                seen.add(s)
                s = succ_of[s]
            add.append({"cik": pc, "ticker": t_of.get(s), "tickers_all": t_of.get(s), "source": "lineage_predecessor",
                        "lineage_successor_cik": succ_of[pc], "in_wiki_current": False, "in_fja_since2009": False,
                        "name": lin.loc[lin.predecessor_cik == pc, "predecessor_name"].iloc[0]})
        if add:
            u = pd.concat([u, pd.DataFrame(add)], ignore_index=True)
    return u


def main(rebuild: bool = False):
    u = universe_all()
    ciks = [int(c) for c in u["cik"] if (CF_DIR / f"CIK{cik10(int(c))}.json.gz").exists()]
    t2 = dict(zip(u["cik"].astype(int), u["ticker"]))
    n_new = 0
    for i, c in enumerate(ciks):
        shard = FACT_SHARDS / f"{c}.parquet"
        if shard.exists() and not rebuild:
            continue
        df = extract_one(c)
        df.to_parquet(shard, index=False)
        n_new += 1
        if n_new % 100 == 0:
            print(f"[extract] {n_new} new shards", flush=True)
    print(f"[extract] new shards: {n_new}; assembling {len(ciks)} CIKs", flush=True)
    parts = []
    for c in ciks:
        df = pd.read_parquet(FACT_SHARDS / f"{c}.parquet")
        if len(df):
            parts.append(df)
    facts = pd.concat(parts, ignore_index=True)
    facts.insert(1, "ticker", facts["cik"].map(t2).astype("string"))
    for c in ("taxonomy", "concept", "unit", "fp", "form"):
        facts[c] = facts[c].astype("category")
    facts["frame"] = facts["frame"].astype("string")
    facts["accn"] = facts["accn"].astype("string")
    out = DATA / "d3_xbrl_facts.parquet"
    facts.to_parquet(out, index=False, compression="zstd")
    meta = pd.DataFrame([company_meta(c) for c in ciks])
    meta["ticker"] = meta["cik"].map(t2)
    meta.to_csv(DATA / "d3_company_meta.csv", index=False)
    cov = facts.groupby("concept", observed=True)["cik"].nunique().sort_values(ascending=False)
    write_meta(out, {
        "source_urls": ["https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json"],
        "retrieval": "see C:/Users/user/eqv4/cache/d3/pull_status.csv (per-CIK retrieval UTC)",
        "rows": int(len(facts)), "columns": list(facts.columns), "n_ciks": int(facts["cik"].nunique()),
        "n_concepts": int(facts["concept"].nunique()),
        "ciks_per_concept": {k: int(v) for k, v in cov.items()},
        "filed_range": [str(facts["filed"].min().date()), str(facts["filed"].max().date())],
        "notes": ["All units kept (USD, USD/shares, shares, other currencies if any).",
                  "fy/fp/form/filed describe the FILING that reported the fact (not the fact's own period); use start/end.",
                  "Same period appears once per filing that reported it (original + later comparatives/restatements).",
                  "Non-dimensional facts only (SEC companyfacts API). Multi-class dei share counts are absent.",
                  "requested=False rows are extra fallback concepts added by D3 (documented in d3_report.md)."],
    })
    write_meta(DATA / "d3_company_meta.csv", {
        "source_urls": ["https://data.sec.gov/submissions/CIK##########.json"], "rows": int(len(meta)),
        "columns": list(meta.columns)})
    print(f"[extract] facts rows={len(facts):,} ciks={facts['cik'].nunique()} -> {out}", flush=True)
    return facts


if __name__ == "__main__":
    main(rebuild="--rebuild" in sys.argv)
