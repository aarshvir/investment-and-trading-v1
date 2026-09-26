"""d4_fetch_sec.py - SEC EDGAR pulls for D4 validation and corporate-event flags.

1. XBRL frames (calendar-aligned annual facts, one row per filer):
     https://data.sec.gov/api/xbrl/frames/us-gaap/<Concept>/USD/CY2025.json
   Concepts: Revenues, RevenueFromContractWithCustomerExcludingAssessedTax, NetIncomeLoss (required)
             + RevenueFromContractWithCustomerIncludingAssessedTax, RevenuesNetOfInterestExpense, ProfitLoss,
               NetIncomeLossAvailableToCommonStockholdersBasic (extras to diagnose gaps)
2. Submissions JSON per CIK (recent filings index: form, filingDate, items) for corporate-event flags:
     https://data.sec.gov/submissions/CIK##########.json

Etiquette: UA per CONVENTIONS.md, gzip, <=2 requests/second, backoff on 429/5xx, raw JSON cached in CACHE/sec/.
"""
from __future__ import annotations

import gzip
import json
import sys
import time
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import CACHE, DATA, UA_SEC, RateLimiter, utc_now_iso  # noqa: E402

SC = CACHE / "sec"
(SC / "frames").mkdir(parents=True, exist_ok=True)
(SC / "submissions").mkdir(parents=True, exist_ok=True)
S = requests.Session()
S.headers.update({"User-Agent": UA_SEC, "Accept-Encoding": "gzip, deflate"})
LIM = RateLimiter(2.0)

CONCEPTS = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "NetIncomeLoss",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "RevenuesNetOfInterestExpense", "ProfitLoss",
            "NetIncomeLossAvailableToCommonStockholdersBasic"]


def get_json(url, tries=5):
    for i in range(tries):
        LIM.wait()
        try:
            r = S.get(url, timeout=60)
        except requests.RequestException as e:
            print("net err", url, e)
            time.sleep(2 ** i)
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code == 404:
            return {"_status": 404}
        print("http", r.status_code, url)
        time.sleep(2 ** i * 2)
    return None


def main():
    log = {"start_utc": utc_now_iso(), "frames": {}, "submissions": {}}
    for c in CONCEPTS:
        fp = SC / "frames" / f"{c}_CY2025.json.gz"
        if fp.exists():
            continue
        url = f"https://data.sec.gov/api/xbrl/frames/us-gaap/{c}/USD/CY2025.json"
        d = get_json(url)
        if d is None:
            log["frames"][c] = "FAILED"
            continue
        d["_retrieved_utc"] = utc_now_iso()
        d["_url"] = url
        with gzip.open(fp, "wt", encoding="utf-8") as f:
            json.dump(d, f)
        log["frames"][c] = len(d.get("data", []))
        print("frame", c, log["frames"][c])

    u = pd.read_csv(DATA / "d4_universe.csv")
    ciks = sorted(set(int(x) for x in u["cik"].dropna()))
    n_new = 0
    for cik in ciks:
        fp = SC / "submissions" / f"CIK{cik:010d}.json.gz"
        if fp.exists():
            continue
        url = f"https://data.sec.gov/submissions/CIK{cik:010d}.json"
        d = get_json(url)
        if d is None:
            log["submissions"][cik] = "FAILED"
            continue
        d["_retrieved_utc"] = utc_now_iso()
        with gzip.open(fp, "wt", encoding="utf-8") as f:
            json.dump(d, f)
        n_new += 1
        if n_new % 50 == 0:
            print("submissions", n_new, flush=True)
    log["end_utc"] = utc_now_iso()
    (SC / f"fetch_log_{int(time.time())}.json").write_text(json.dumps(log, indent=1, default=str))
    print("done", n_new, "new submissions; failures:",
          [k for k, v in log["submissions"].items() if v == "FAILED"])


if __name__ == "__main__":
    main()
