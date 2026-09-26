"""d1_cik_sector.py - write d1_cik_map.csv, d1_sic_to_sector.csv, d1_sector_map.csv (+ meta) and coverage stats.

SIC source: SEC submissions JSON (cached) of each mapped CIK (sic, sicDescription, fiscalYearEnd, tickers,
exchanges, formerNames). SIC->sector: d1_sic_sector_rules (a-priori ranges) + tuned 4-digit overrides derived here
from systematic mismatches vs current GICS (a SIC code is overridden only if >=2 current members carry it and
>=60% of them share one other GICS sector); before/after agreement is reported.
"""
import json
from collections import Counter

import pandas as pd

from d1_common import CACHE, DATA, get_submissions, write_meta
from d1_sic_sector_rules import CODE_OVERRIDES, RANGE_RULES, sic_to_sector

LAST = "2026-09-25"


def _ok(x):
    return isinstance(x, str) and bool(x.strip())


def sec_info(cik):
    d = get_submissions(int(cik))
    if not d:
        return {}
    return {"sec_name": d.get("name"), "sic": d.get("sic") or None, "sic_description": d.get("sicDescription"),
            "fiscal_year_end": d.get("fiscalYearEnd"), "sec_tickers": ",".join(d.get("tickers") or []),
            "sec_exchanges": ",".join(x for x in (d.get("exchanges") or []) if x),
            "former_names": "; ".join(f"{f.get('name')} ({(f.get('from') or '')[:10]}..{(f.get('to') or '')[:10]})"
                                      for f in d.get("formerNames", [])),
            "state_of_incorporation": d.get("stateOfIncorporation")}


def main():
    I = pd.read_csv(DATA / "d1_membership_intervals.csv", dtype={"end_date": "string"})
    M = pd.read_parquet(DATA / "d1_membership_monthly.parquet")
    cur = pd.read_parquet(CACHE / "wiki_current.parquet")
    L = pd.read_parquet(CACHE / "id_link_month.parquet")
    O = pd.read_parquet(CACHE / "entity_rows.parquet")

    # ------------------------------------------------------------------ CIK map (one row per entity x CIK)
    rows = []
    for (eid, cik), g in I[I.cik.notna()].groupby(["entity_id", "cik"]):
        g = g.sort_values("start_date")
        tk = g["ticker_current_yahoo"].dropna()
        hist = ";".join(g["ticker_history"].dropna())
        last_t = hist.split(";")[-1].split(":")[0] if hist else g["ticker_at_time"].iloc[-1]
        info = sec_info(cik)
        conf = g["cik_confidence"].mode().iloc[0]
        rows.append({"entity_id": eid, "ticker_key": tk.iloc[-1] if len(tk) else str(last_t).replace(".", "-"),
                     "ticker_current_yahoo": tk.iloc[-1] if len(tk) else None,
                     "tickers_at_time": ",".join(dict.fromkeys(g["ticker_at_time"].astype(str))),
                     "cik": int(cik), "cik_valid_from": g["start_date"].min(),
                     "cik_valid_to": (None if g["end_date"].isna().any() else g["end_date"].max()),
                     "sec_name": info.get("sec_name"), "match_method": g["cik_method"].iloc[-1],
                     "confidence": conf, "cik_first_report": g["cik_first_report"].min(),
                     "cik_last_report": g["cik_last_report"].max(),
                     "notes": ("CIK filings start after membership start (predecessor registrant not mapped; "
                               "fundamentals before cik_first_report will be missing)"
                               if _ok(g["cik_first_report"].min()) and g["cik_first_report"].min() >
                               (pd.Timestamp(max(g["start_date"].min(), "1996-06-01")) + pd.Timedelta(days=400)).strftime("%Y-%m-%d")
                               else None),
                     **{k: info.get(k) for k in ["sic", "sic_description", "fiscal_year_end", "sec_tickers",
                                                 "sec_exchanges", "former_names", "state_of_incorporation"]}})
    # entities without CIK
    for eid, g in I[I.cik.isna()].groupby("entity_id"):
        rows.append({"entity_id": eid, "ticker_key": str(g["ticker_at_time"].iloc[-1]).replace(".", "-"),
                     "tickers_at_time": ",".join(dict.fromkeys(g["ticker_at_time"].astype(str))), "cik": None,
                     "cik_valid_from": g["start_date"].min(), "cik_valid_to": g["end_date"].max(),
                     "match_method": "none", "confidence": "none",
                     "notes": "no verified CIK (removed before 2000 or unresolved Norgate symbol)"})
    C = pd.DataFrame(rows)
    C["cik"] = C["cik"].astype("Int64")
    C = C.sort_values(["entity_id", "cik_valid_from"]).reset_index(drop=True)
    pc = DATA / "d1_cik_map.csv"
    C.to_csv(pc, index=False)

    # ------------------------------------------------------------------ coverage: member-months since 2000
    Ms = M[M.index >= "2000-01-01"]
    grid = [d.strftime("%Y-%m-%d") for d in Ms.index]
    conf_mm = Counter()
    for r in I.itertuples():
        e = r.end_date if _ok(r.end_date) else "9999-12-31"
        n = sum(1 for d in grid if r.start_date <= d < e)
        conf_mm[r.cik_confidence if _ok(r.cik_confidence) else "none"] += n
    tot = sum(conf_mm.values())
    cov = {k: round(100 * v / tot, 2) for k, v in conf_mm.items()}
    cov_hm = round(100 * (conf_mm["high"] + conf_mm["medium"]) / tot, 2)

    # ------------------------------------------------------------------ sectors
    ent = O.sort_values("start_date").groupby("entity_id").tail(1).set_index("entity_id")
    cur_by_t = cur.set_index("ticker_yahoo")
    rec = []
    for eid, r in ent.iterrows():
        latest_cik = int(eid[3:13]) if eid.startswith("CIK") else None
        info = sec_info(latest_cik) if latest_cik else {}
        tcy = r["ticker_current_yahoo"]
        g_sec = g_sub = None
        if r["is_current_member"] and _ok(tcy) and tcy in cur_by_t.index:
            g_sec, g_sub = cur_by_t.at[tcy, "gics_sector"], cur_by_t.at[tcy, "gics_sub_industry"]
        # last Wikipedia-observed GICS sector (2008+ snapshots)
        spells = []
        for s in O.loc[O.entity_id == eid, "spell_ids"]:
            spells += s.split(",")
        w = L[L.spell_id.isin(spells) & L.wiki_sector.notna()].sort_values("month")
        rec.append({"entity_id": eid, "ticker_key": tcy if _ok(tcy) else r["line_last_ticker"], "cik": latest_cik,
                    "name": r["name"], "sic": info.get("sic"), "sic_description": info.get("sic_description"),
                    "is_current_member": bool(r["is_current_member"]),
                    "gics_sector_current": g_sec, "gics_sub_industry_current": g_sub,
                    "gics_sector_wiki_last": w["wiki_sector"].iloc[-1] if len(w) else None,
                    "gics_wiki_last_month": w["month"].iloc[-1] if len(w) else None})
    SM = pd.DataFrame(rec)

    def apply(overrides):
        res = [sic_to_sector(s, overrides) for s in SM["sic"]]
        return [x[0] for x in res], [x[1] for x in res]

    SM["sic_sector_apriori"], _ = apply({k: v for k, v in CODE_OVERRIDES.items() if not v[1]})
    curm = SM[SM.gics_sector_current.notna() & SM.sic.notna()]
    agree_before = (curm["sic_sector_apriori"] == curm["gics_sector_current"]).mean()
    # tuning: systematic mismatches per SIC code among current members
    tuned = {}
    for sic, g in curm.groupby("sic"):
        if len(g) < 2:
            continue
        vc = g["gics_sector_current"].value_counts()
        top, share = vc.index[0], vc.iloc[0] / len(g)
        if share >= 0.6 and top != g["sic_sector_apriori"].iloc[0]:
            tuned[int(sic)] = (top, True, f"{vc.iloc[0]}/{len(g)} current members with SIC {sic} are GICS {top} "
                                          f"(a-priori: {g['sic_sector_apriori'].iloc[0]})")
    overrides = {k: v for k, v in CODE_OVERRIDES.items()}
    overrides.update(tuned)
    SM["sic_sector"], SM["sic_sector_basis"] = apply(overrides)
    curm = SM[SM.gics_sector_current.notna() & SM.sic.notna()]
    agree_after = (curm["sic_sector"] == curm["gics_sector_current"]).mean()
    # leave-one-out style honesty check: agreement on current members whose SIC code was NOT tuned
    untuned = curm[~curm["sic"].astype(int).isin(tuned.keys())]
    agree_untuned = (untuned["sic_sector"] == untuned["gics_sector_current"]).mean()
    # historical check vs last Wikipedia GICS (non-current entities, sector names normalised to post-2018 GICS)
    norm = {"Telecommunications Services": "Communication Services", "Telecommunication Services": "Communication Services",
            "Telecommunication": "Communication Services"}
    hist = SM[(~SM.is_current_member) & SM.gics_sector_wiki_last.notna() & SM.sic.notna()].copy()
    hist["g"] = hist["gics_sector_wiki_last"].replace(norm)
    agree_hist = (hist["sic_sector"] == hist["g"]).mean() if len(hist) else None
    SM["sic"] = pd.to_numeric(SM["sic"], errors="coerce").astype("Int64")
    SM["cik"] = SM["cik"].astype("Int64")
    ps = DATA / "d1_sector_map.csv"
    SM[["entity_id", "ticker_key", "cik", "name", "sic", "sic_description", "sic_sector", "sic_sector_basis",
        "is_current_member", "gics_sector_current", "gics_sub_industry_current", "gics_sector_wiki_last",
        "gics_wiki_last_month"]].to_csv(ps, index=False)

    # SIC -> sector table (all SIC codes seen + rule ranges)
    codes = sorted(set(int(x) for x in SM["sic"].dropna()))
    desc = SM.dropna(subset=["sic"]).groupby("sic")["sic_description"].first().to_dict()
    tab = []
    for c in codes:
        sec, basis = sic_to_sector(c, overrides)
        g = SM[SM.sic == c]
        gc = g[g.gics_sector_current.notna()]
        tab.append({"sic": c, "sic_description": desc.get(c), "sector": sec, "basis": basis,
                    "tuned": c in tuned, "n_entities": len(g), "n_current_members": len(gc),
                    "current_members_agree": int((gc["gics_sector_current"] == sec).sum()),
                    "current_gics_mix": "; ".join(f"{k}:{v}" for k, v in gc["gics_sector_current"].value_counts().items())})
    T = pd.DataFrame(tab)
    rules = pd.DataFrame([{"sic": f"{lo}-{hi}", "sic_description": note, "sector": sec, "basis": "range rule (a priori)",
                           "tuned": False} for lo, hi, sec, note in RANGE_RULES])
    pt = DATA / "d1_sic_to_sector.csv"
    pd.concat([T, rules], ignore_index=True).to_csv(pt, index=False)

    stats = {"cik_coverage_member_months_since_2000_pct_by_confidence": cov,
             "cik_coverage_high_or_medium_pct": cov_hm, "member_months_since_2000": tot,
             "sector_agreement_current_members_apriori": round(float(agree_before), 4),
             "sector_agreement_current_members_tuned": round(float(agree_after), 4),
             "sector_agreement_current_members_untuned_codes_only": round(float(agree_untuned), 4),
             "sector_agreement_historical_vs_last_wikipedia_gics": None if agree_hist is None else round(float(agree_hist), 4),
             "n_tuned_overrides": len(tuned), "tuned": {str(k): v[2] for k, v in tuned.items()},
             "n_current_members_with_sic": int(len(curm))}
    (CACHE / "d1_cik_sector_stats.json").write_text(json.dumps(stats, indent=2))
    src = ["https://data.sec.gov/submissions/CIK##########.json", "https://www.sec.gov/files/company_tickers_exchange.json",
           "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt", "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"]
    write_meta(pc, {"dataset": "entity x CIK map with validity dates, SEC name, SIC, FYE, tickers, former names",
                    "source_urls": src, "rows": int(len(C)), "columns": list(C.columns),
                    "coverage": stats, "confidence_definitions": {
                        "high": "filings verified in window AND (Wikipedia CIK column or SEC ticker table with name sim>=0.5, "
                                "or >=2 independent sources agree, or Wikipedia-name match >=0.8)",
                        "medium": "filings verified with weaker name agreement, or analyst name hypothesis confirmed by SEC "
                                  "name + 10-K/10-Q inside the window, or Norgate 2019 symbol = SEC ticker + filings, or "
                                  "Wikipedia CIK + name match without EDGAR periodic reports (banks)",
                        "low": "other", "none": "no candidate"}})
    write_meta(ps, {"dataset": "entity sector map: SEC SIC -> GICS-like sector (+ current GICS, last Wikipedia GICS)",
                    "source_urls": src, "rows": int(len(SM)), "stats": stats,
                    "caveats": ["SIC is from the entity's latest CIK (current SEC record), not point-in-time.",
                                "gics_sector_wiki_last uses the GICS structure of that date (pre-2016 no Real Estate, "
                                "pre-2018 Telecommunication Services)."]})
    write_meta(pt, {"dataset": "SIC -> 11-sector mapping table (rows with numeric sic = codes observed; rows with ranges = "
                               "a-priori rules)", "rows": int(len(T) + len(rules)), "n_tuned": len(tuned)})
    print(json.dumps(stats, indent=1)[:3000])


if __name__ == "__main__":
    main()
