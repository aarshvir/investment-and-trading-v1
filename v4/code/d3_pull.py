"""d3_pull.py - download SEC XBRL companyfacts (+ submissions metadata) for the D3 universe, resumable.

Usage (Git Bash, from PROJECT):
  PYTHONPATH='C:\\Users\\user\\eqv4\\pylib' python v4/code/d3_pull.py                 # universe from d3_universe.csv
  PYTHONPATH=... python v4/code/d3_pull.py --ciks-from v4/data/d1_cik_map.csv         # + D1 CIKs (confidence high/medium),
                                                                                      #   downloads/extracts/builds ONLY missing CIKs,
                                                                                      #   then re-assembles the combined outputs
  options: --no-submissions  --download-only  --limit N

Raw JSON is stored gzipped in C:\\Users\\user\\eqv4\\cache\\d3\\{companyfacts,submissions}\\CIK##########.json.gz
SEC etiquette: User-Agent header, <= 3.3 req/s (convention max 4/s), backoff on 429/5xx/403.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import pandas as pd

from d3_common import (CF_DIR, SUB_DIR, CACHE, DATA, PROJECT, cik10, http_get, utcnow_iso, write_gz_bytes)

CF_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{}.json"
SUB_URL = "https://data.sec.gov/submissions/CIK{}.json"
STATUS = CACHE / "pull_status.csv"


def load_status() -> pd.DataFrame:
    if STATUS.exists():
        return pd.read_csv(STATUS, dtype={"cik": int})
    return pd.DataFrame(columns=["cik", "kind", "status", "bytes", "retrieved_utc"])


def download(ciks, kinds=("companyfacts", "submissions"), limit=None):
    st = load_status()
    done = set(zip(st["cik"].astype(int), st["kind"])) if len(st) else set()
    new_rows = []
    todo = []
    for c in ciks:
        for k in kinds:
            d = CF_DIR if k == "companyfacts" else SUB_DIR
            p = d / f"CIK{cik10(c)}.json.gz"
            if p.exists() and p.stat().st_size > 0:
                continue
            if (int(c), k) in done and (st[(st.cik == int(c)) & (st.kind == k)]["status"] == 404).any():
                continue   # known 404: no XBRL facts for this CIK
            todo.append((int(c), k, p))
    if limit:
        todo = todo[:limit]
    print(f"[pull] {len(todo)} downloads to do", flush=True)
    t0 = time.time()

    def one(job):
        c, k, p = job
        url = (CF_URL if k == "companyfacts" else SUB_URL).format(cik10(c))
        try:
            r = http_get(url, sec=True)
            if r.status_code == 200:
                write_gz_bytes(p, r.content)
            return {"cik": c, "kind": k, "status": r.status_code, "bytes": len(r.content), "retrieved_utc": utcnow_iso()}
        except Exception as e:  # keep going; record failure
            print(f"[pull] FAIL {c} {k}: {e}", flush=True)
            return {"cik": c, "kind": k, "status": -1, "bytes": 0, "retrieved_utc": utcnow_iso()}

    # 3 worker threads share ONE global rate limiter (<= 3.3 request starts per second in total)
    from concurrent.futures import ThreadPoolExecutor, as_completed
    with ThreadPoolExecutor(max_workers=3) as ex:
        futs = [ex.submit(one, j) for j in todo]
        for i, f in enumerate(as_completed(futs)):
            new_rows.append(f.result())
            if (i + 1) % 50 == 0:
                print(f"[pull] {i + 1}/{len(todo)} in {time.time() - t0:.0f}s", flush=True)
                _save_status(st, new_rows)
    _save_status(st, new_rows)
    return new_rows


def _save_status(st, new_rows):
    if not new_rows:
        return
    out = pd.concat([st, pd.DataFrame(new_rows)], ignore_index=True)
    out = out.drop_duplicates(subset=["cik", "kind"], keep="last")
    out.to_csv(STATUS, index=False)


def read_d1_map(path: Path) -> pd.DataFrame:
    """Read D1's CIK map flexibly: needs a 'cik' column; keeps confidence in {high, medium} if such a column exists."""
    df = pd.read_csv(path)
    cols = {c.lower(): c for c in df.columns}
    cik_col = cols.get("cik") or next((c for c in df.columns if "cik" in c.lower()), None)
    if cik_col is None:
        raise SystemExit(f"no CIK column in {path}: {list(df.columns)}")
    conf_col = next((c for c in df.columns if "confidence" in c.lower()), None)
    df = df[pd.to_numeric(df[cik_col], errors="coerce").notna()].copy()
    df["cik"] = pd.to_numeric(df[cik_col]).astype(int)
    if conf_col is not None:
        df = df[df[conf_col].astype(str).str.lower().str.strip().isin(["high", "medium"])]
    tick_col = next((c for c in df.columns if c.lower() in ("ticker", "symbol", "ticker_yahoo", "ticker_norm")), None)
    df["ticker_d1"] = df[tick_col].astype(str) if tick_col else None
    return df


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ciks-from", default=None, help="CSV with a cik column (e.g. v4/data/d1_cik_map.csv)")
    ap.add_argument("--no-submissions", action="store_true")
    ap.add_argument("--download-only", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--source-label", default="d1_cik_map", help="label stored in d3_universe_extra_d1.csv 'source'")
    args = ap.parse_args()

    univ = pd.read_csv(DATA / "d3_universe.csv")
    ciks = [int(c) for c in univ["cik"]]
    extra = []
    if args.ciks_from:
        p = Path(args.ciks_from)
        if not p.is_absolute():
            p = PROJECT / p
        if not p.exists():
            raise SystemExit(f"--ciks-from file not found: {p}")
        d1 = read_d1_map(p)
        extra = sorted(set(d1["cik"]) - set(ciks))
        print(f"[pull] D1 map: {d1['cik'].nunique()} CIKs with confidence high/medium; {len(extra)} not yet in D3 universe")
        # register extra CIKs (one row each) so that downstream steps include them
        add = (d1[d1["cik"].isin(extra)].sort_values("cik").groupby("cik").agg(
            ticker=("ticker_d1", lambda s: sorted(set(map(str, s)))[-1] if s.notna().any() else None),
            tickers_all=("ticker_d1", lambda s: ";".join(sorted(set(map(str, s.dropna()))))),
        ).reset_index())
        add["source"] = args.source_label
        add["in_wiki_current"] = False
        add["in_fja_since2009"] = False
        extra_path = DATA / "d3_universe_extra_d1.csv"
        if extra_path.exists():
            old = pd.read_csv(extra_path)
            add = pd.concat([old, add[~add["cik"].isin(old["cik"])]], ignore_index=True)
        add.to_csv(extra_path, index=False)
        ciks = ciks + extra

    kinds = ("companyfacts",) if args.no_submissions else ("companyfacts", "submissions")
    download(ciks, kinds=kinds, limit=args.limit)
    if args.download_only:
        return
    # extraction + PIT build (both incremental: per-CIK shards are reused, only missing CIKs are processed)
    import d3_extract
    import d3_build_pit
    d3_extract.main()
    d3_build_pit.main()


if __name__ == "__main__":
    sys.exit(main())
