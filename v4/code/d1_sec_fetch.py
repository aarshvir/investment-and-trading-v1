"""d1_sec_fetch.py - prefetch SEC submissions JSON for a set of CIKs (cached in CACHE/submissions, <=3.5 req/s).

Usage: python d1_sec_fetch.py [ciks.txt]   (default: all CIKs referenced by Wikipedia tables + SEC ticker matches
                                          of fja plain keys + CACHE/extra_ciks.txt if present)
"""
import json
import sys

import pandas as pd

from d1_common import CACHE, SUBM_CACHE, get_submissions


def default_ciks() -> set[int]:
    ciks = set()
    sn = pd.read_parquet(CACHE / "wiki_snapshots.parquet")
    ciks |= set(pd.to_numeric(sn["cik"], errors="coerce").dropna().astype(int))
    cur = pd.read_parquet(CACHE / "wiki_current.parquet")
    ciks |= set(cur["cik"].dropna().astype(int))
    sp = pd.read_parquet(CACHE / "fja_spells.parquet")
    d = json.loads((CACHE / "company_tickers_exchange.json").read_text())
    ct = pd.DataFrame(d["data"], columns=d["fields"])
    ct["tn"] = ct["ticker"].str.upper().str.replace(".", "-", regex=False)
    tn = set(sp["ticker"].str.replace(".", "-", regex=False))
    ciks |= set(ct.loc[ct["tn"].isin(tn), "cik"].astype(int))
    extra = CACHE / "extra_ciks.txt"
    if extra.exists():
        ciks |= {int(x) for x in extra.read_text().split() if x.strip().isdigit()}
    return ciks


def main():
    if len(sys.argv) > 1:
        ciks = {int(x) for x in open(sys.argv[1]).read().split() if x.strip().isdigit()}
    else:
        ciks = default_ciks()
    todo = [c for c in sorted(ciks) if not (SUBM_CACHE / f"CIK{c:010d}.json").exists()]
    print(f"{len(ciks)} CIKs, {len(todo)} to fetch", flush=True)
    # 4 worker threads share one rate limiter (<= 3.5 request starts per second in total)
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def one(c):
        try:
            get_submissions(c)
            return None
        except Exception as e:  # keep going
            return f"ERR {c} {e}"

    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(one, c) for c in todo]
        for i, f in enumerate(as_completed(futs)):
            msg = f.result()
            if msg:
                print(msg, flush=True)
            if i % 100 == 0:
                print("progress", i, flush=True)
    print("done")


if __name__ == "__main__":
    main()
