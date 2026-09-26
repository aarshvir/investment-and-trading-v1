"""d1_wiki_snapshots.py - month-end snapshots of Wikipedia 'List of S&P 500 companies' (page history).

For every calendar month from 2005-09 to 2026-09 we take the LAST revision saved in that month and parse the
constituents table (ticker, security name, GICS sector/sub-industry, CIK when present). This gives an
independent, time-stamped (editor-maintained) view of membership plus names/CIKs for companies that have since
left the index. Raw HTML is cached gzipped under CACHE/wiki_revs/.

Output (cache): CACHE/wiki_snapshots.parquet  (rev_month, revid, rev_ts, ticker, name, gics_sector,
                                               gics_sub_industry, cik, date_added_raw, n_rows_in_table)
                CACHE/wiki_revisions_monthly.csv
"""
import gzip
import io
import json
import re
import sys

import pandas as pd

from d1_common import CACHE, GEN_SESSION, GEN_LIMITER, utcnow_iso

API = "https://en.wikipedia.org/w/api.php"
REV_DIR = CACHE / "wiki_revs"
REV_DIR.mkdir(parents=True, exist_ok=True)


def list_revisions() -> pd.DataFrame:
    p = CACHE / "wiki_list_revisions.json"
    if p.exists():
        revs = json.loads(p.read_text())
    else:
        revs, cont = [], {}
        while True:
            params = dict(action="query", prop="revisions", titles="List_of_S&P_500_companies", rvlimit=500,
                          rvdir="newer", rvprop="ids|timestamp|size", format="json")
            params.update(cont)
            GEN_LIMITER.wait()
            d = GEN_SESSION.get(API, params=params, timeout=60).json()
            revs += list(d["query"]["pages"].values())[0]["revisions"]
            if "continue" in d:
                cont = d["continue"]
            else:
                break
        p.write_text(json.dumps(revs))
    df = pd.DataFrame(revs)
    df["ts"] = pd.to_datetime(df["timestamp"], utc=True)
    df["month"] = df["ts"].dt.strftime("%Y-%m")
    return df


def fetch_rev_html(revid: int) -> str:
    dest = REV_DIR / f"{revid}.html.gz"
    if dest.exists():
        return gzip.decompress(dest.read_bytes()).decode("utf-8")
    for attempt in range(5):
        GEN_LIMITER.wait()
        try:
            r = GEN_SESSION.get(API, params=dict(action="parse", oldid=revid, prop="text", format="json",
                                                 formatversion=2), timeout=120)
            if r.status_code == 200:
                d = r.json()
                html = d["parse"]["text"]
                dest.write_bytes(gzip.compress(html.encode("utf-8")))
                return html
        except Exception as e:  # retry
            print("retry", revid, e, file=sys.stderr)
    raise RuntimeError(f"failed revid {revid}")


def _norm_col(c) -> str:
    if isinstance(c, tuple):
        c = " ".join(str(x) for x in c)
    return re.sub(r"\s+", " ", str(c)).strip().lower()


def parse_constituents(html: str) -> pd.DataFrame | None:
    """Find the constituents table: the one with a ticker/symbol column and >= 300 rows."""
    try:
        tables = pd.read_html(io.StringIO(html), flavor="lxml")
    except (ValueError, ImportError):
        return None
    best = None
    for t in tables:
        if len(t) < 300:
            continue
        cols = [_norm_col(c) for c in t.columns]
        tick_idx = next((i for i, c in enumerate(cols) if c in ("symbol", "ticker symbol", "ticker") or
                         c.startswith("ticker") or c.startswith("symbol")), None)
        if tick_idx is None:
            continue
        name_idx = next((i for i, c in enumerate(cols) if c in ("security", "company", "company name", "name")
                         or c.startswith("security") or c.startswith("company")), None)
        sec_idx = next((i for i, c in enumerate(cols) if "gics sector" in c or c == "sector"), None)
        sub_idx = next((i for i, c in enumerate(cols) if "sub-industry" in c or "sub industry" in c
                        or "subindustry" in c), None)
        cik_idx = next((i for i, c in enumerate(cols) if c == "cik" or c.startswith("cik")), None)
        add_idx = next((i for i, c in enumerate(cols) if "added" in c), None)
        out = pd.DataFrame({
            "ticker": t.iloc[:, tick_idx].astype(str),
            "name": t.iloc[:, name_idx].astype(str) if name_idx is not None else None,
            "gics_sector": t.iloc[:, sec_idx].astype(str) if sec_idx is not None else None,
            "gics_sub_industry": t.iloc[:, sub_idx].astype(str) if sub_idx is not None else None,
            "cik": t.iloc[:, cik_idx].astype(str) if cik_idx is not None else None,
            "date_added_raw": t.iloc[:, add_idx].astype(str) if add_idx is not None else None,
        })
        if best is None or len(out) > len(best):
            best = out
    return best


def main():
    revs = list_revisions()
    monthly = revs.sort_values("ts").groupby("month").tail(1).reset_index(drop=True)
    monthly.to_csv(CACHE / "wiki_revisions_monthly.csv", index=False)
    frames = []
    for i, r in monthly.iterrows():
        html = fetch_rev_html(int(r.revid))
        t = parse_constituents(html)
        if t is None or len(t) == 0:
            print(f"{r.month} rev {r.revid}: no constituents table")
            continue
        t.insert(0, "rev_ts", r.timestamp)
        t.insert(0, "revid", int(r.revid))
        t.insert(0, "rev_month", r.month)
        t["n_rows_in_table"] = len(t)
        frames.append(t)
        if i % 12 == 0:
            print(f"{r.month} rev {r.revid}: {len(t)} rows; cols name={t['name'].notna().all()} "
                  f"cik={t['cik'].notna().any()} sector={t['gics_sector'].notna().any()}", flush=True)
    snaps = pd.concat(frames, ignore_index=True)
    for c in snaps.columns:
        if snaps[c].dtype == object:
            snaps[c] = snaps[c].astype("string")
    snaps.to_parquet(CACHE / "wiki_snapshots.parquet", index=False)
    (CACHE / "wiki_snapshots.meta.json").write_text(json.dumps({
        "source": "https://en.wikipedia.org/w/api.php?action=parse&oldid=<revid> (List_of_S%26P_500_companies)",
        "retrieved_utc": utcnow_iso(), "months": int(snaps.rev_month.nunique()), "rows": int(len(snaps))}, indent=2))
    print("done", snaps.shape, snaps.rev_month.min(), snaps.rev_month.max())


if __name__ == "__main__":
    main()
