"""d3_lineage.py - discover predecessor CIKs (holding-company reorganisations, re-domiciliations, accounting
predecessors) for companies whose XBRL history starts late, using the SEC XBRL *frames* API.

Method: a successor's first filings contain comparative-period facts (prior-year net income, prior year-end assets)
that were ALSO reported by its predecessor under a different CIK. For each late-starting CIK we take its earliest
framed facts (NetIncomeLoss, Assets, StockholdersEquity), query
  https://data.sec.gov/api/xbrl/frames/us-gaap/{concept}/USD/{frame}.json
and look for other CIKs reporting the identical value (|diff| <= 0.1%) in >= 2 different concept/frame pairs.
Confirmed predecessors are downloaded (companyfacts + submissions) and the search recurses (e.g. AVGO -> Broadcom Ltd ->
Avago). The PIT engine then *enriches* the successor's state with predecessor facts filed before the successor's first
periodic filing (successor rows still start at its own first filing, so no row is attributed to the wrong entity).

Output: v4/data/d3_lineage.csv (successor_cik, predecessor_cik, names, n_matches, evidence, dates)
"""
from __future__ import annotations

import json
from collections import defaultdict

import pandas as pd

from d3_common import (CACHE, CF_DIR, DATA, PANEL_FORMS, cik10, http_get, read_gz_json, utcnow_iso, write_meta)
import d3_pull

FRAMES_DIR = CACHE / "frames"
FRAMES_DIR.mkdir(parents=True, exist_ok=True)
CONCEPTS = [("NetIncomeLoss", False), ("Assets", True), ("StockholdersEquity", True)]


def get_frame(concept, frame):
    p = FRAMES_DIR / f"{concept}_{frame}.json"
    if p.exists():
        return json.loads(p.read_text())
    url = f"https://data.sec.gov/api/xbrl/frames/us-gaap/{concept}/USD/{frame}.json"
    r = http_get(url, sec=True)
    j = r.json() if r.status_code == 200 else {"data": []}
    p.write_text(json.dumps(j))
    return j


def first_periodic_filed(j):
    best = None
    for tax in j.get("facts", {}).values():
        for node in tax.values():
            for xs in node.get("units", {}).values():
                for x in xs:
                    if x.get("form") in PANEL_FORMS and x.get("filed"):
                        if best is None or x["filed"] < best:
                            best = x["filed"]
    return best


def last_periodic_filed(j):
    best = None
    for tax in j.get("facts", {}).values():
        for node in tax.values():
            for xs in node.get("units", {}).values():
                for x in xs:
                    if x.get("form") in PANEL_FORMS and x.get("filed"):
                        if best is None or x["filed"] > best:
                            best = x["filed"]
    return best


def candidate_frames(j, max_per_concept=2):
    out = []
    ug = j.get("facts", {}).get("us-gaap", {})
    for concept, instant in CONCEPTS:
        xs = ug.get(concept, {}).get("units", {}).get("USD", [])
        xs = [x for x in xs if x.get("frame") and x.get("form") in PANEL_FORMS and x.get("val") not in (None, 0)]
        if not instant:
            xs = [x for x in xs if x.get("start")]
        xs.sort(key=lambda x: x["end"])
        seen = set()
        for x in xs:
            if x["frame"] in seen:
                continue
            seen.add(x["frame"])
            out.append((concept, x["frame"], float(x["val"])))
            if len(seen) >= max_per_concept:
                break
    return out


CONFIRM_INSTANT = ["LiabilitiesAndStockholdersEquity", "CashAndCashEquivalentsAtCarryingValue", "Liabilities",
                   "StockholdersEquity", "Assets"]
CONFIRM_DURATION = ["NetIncomeLoss", "Revenues", "OperatingIncomeLoss", "NetCashProvidedByUsedInOperatingActivities",
                    "IncomeTaxExpenseBenefit"]


def _own_value(j, concept, frame):
    xs = j.get("facts", {}).get("us-gaap", {}).get(concept, {}).get("units", {}).get("USD", [])
    for x in xs:
        if x.get("frame") == frame and x.get("form") in PANEL_FORMS and x.get("val") not in (None, 0):
            return float(x["val"])
    return None


def _eq(a, b):
    # identical reported values (successor comparatives == predecessor originals); tolerance only for float noise
    return abs(a - b) <= max(0.5, 1e-7 * abs(a))


def find_predecessors(cik: int):
    p = CF_DIR / f"CIK{cik10(cik)}.json.gz"
    j = read_gz_json(p)
    frames = candidate_frames(j)
    hits = defaultdict(list)
    hit_frames = defaultdict(set)
    names = {}
    for concept, frame, val in frames:
        fr = get_frame(concept, frame)
        for d in fr.get("data", []):
            c2 = int(d["cik"])
            if c2 == cik:
                continue
            v2 = float(d["val"])
            if _eq(val, v2) and abs(val) >= 1e6:
                hits[c2].append(f"{concept}:{frame}={val:.0f}")
                hit_frames[c2].add(frame)
                names[c2] = d.get("entityName")
    # confirmation pass for single-concept candidates: same frame(s), additional concepts
    for c2 in [c for c, ev in hits.items() if len({e.split(':')[0] for e in ev}) < 2]:
        for frame in sorted(hit_frames[c2]):
            confirm = CONFIRM_INSTANT if frame.endswith("I") else CONFIRM_DURATION
            for concept in confirm:
                if any(e.startswith(concept + ":" + frame) for e in hits[c2]):
                    continue
                own = _own_value(j, concept, frame)
                if own is None:
                    continue
                for d in get_frame(concept, frame).get("data", []):
                    if int(d["cik"]) == c2 and _eq(own, float(d["val"])):
                        hits[c2].append(f"{concept}:{frame}={own:.0f}")
    out = []
    for c2, ev in hits.items():
        n_concepts = len({e.split(":")[0] for e in ev})
        if len(ev) >= 2 and n_concepts >= 2:
            out.append({"predecessor_cik": c2, "predecessor_name": names.get(c2), "n_matches": len(ev),
                        "evidence": "; ".join(ev)})
    return out, frames


def main(min_first_filed="2011-10-01"):
    import d3_extract
    u = d3_extract.universe_all()
    rows = []
    todo = [int(c) for c in u["cik"]]
    checked = set()
    depth = {c: 0 for c in todo}
    while todo:
        cik = todo.pop(0)
        if cik in checked:
            continue
        checked.add(cik)
        p = CF_DIR / f"CIK{cik10(cik)}.json.gz"
        if not p.exists():
            continue
        j = read_gz_json(p)
        ff = first_periodic_filed(j)
        if ff is None or ff < min_first_filed:
            continue
        preds, frames = find_predecessors(cik)
        for pr in preds:
            pc = pr["predecessor_cik"]
            d3_pull.download([pc])
            pj_path = CF_DIR / f"CIK{cik10(pc)}.json.gz"
            pj = read_gz_json(pj_path) if pj_path.exists() else {}
            pf, pl = first_periodic_filed(pj), last_periodic_filed(pj)
            # a predecessor must have started filing before the successor
            if pf is None or pf >= ff:
                continue
            rows.append({"successor_cik": cik, "successor_name": j.get("entityName"), "successor_first_filed": ff,
                         **pr, "predecessor_first_filed": pf, "predecessor_last_filed": pl, "depth": depth.get(cik, 0)})
            if pc not in checked and depth.get(cik, 0) < 2:
                depth[pc] = depth.get(cik, 0) + 1
                todo.append(pc)
        print(f"[lineage] {cik} {j.get('entityName')} first={ff} frames={len(frames)} preds={[r['predecessor_cik'] for r in preds]}",
              flush=True)
    lin = pd.DataFrame(rows)
    if len(lin):   # parallel co-registrants (e.g. Broadcom Ltd / Broadcom Cayman L.P.) are not successions
        lin["co_registrant"] = (pd.to_datetime(lin["successor_first_filed"]) -
                                pd.to_datetime(lin["predecessor_first_filed"])).dt.days < 90
    out = DATA / "d3_lineage.csv"
    lin.to_csv(out, index=False)
    write_meta(out, {"source_urls": ["https://data.sec.gov/api/xbrl/frames/us-gaap/{concept}/USD/{frame}.json",
                                     "https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json"],
                     "retrieval_utc": utcnow_iso(), "rows": len(lin),
                     "method": "identical comparative values (NetIncomeLoss/Assets/StockholdersEquity frames, >=2 matches "
                               "across >=2 concepts, |diff|<=0.1%) between a late-starting CIK and an earlier filer",
                     "use": "PIT engine enriches successor state with predecessor facts filed before successor's first "
                            "periodic filing; successor rows start at its own first filing."})
    print(lin.to_string() if len(lin) else "no lineage found")
    return lin


if __name__ == "__main__":
    main()
