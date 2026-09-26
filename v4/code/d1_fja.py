"""d1_fja.py - parse fja05680/sp500 membership files into security 'spells' (point-in-time).

Design (see d1_report.md):
* 1996-01-02 .. 2019-01-11 : ORIGINAL file 'S&P 500 Historical Components & Changes.csv' (Clenow / Norgate
  symbols). Keys are Norgate symbols: securities still listed in 2019 carry their 2019 ticker (e.g. BKNG for
  Priceline since 2009); delisted securities carry '<last ticker>-YYYYMM' (delisting month). This keeps two
  different companies that shared a ticker apart (e.g. BAC vs BAC-199809 = NationsBank vs old BankAmerica).
  The '(Updated)' file strips the suffix and de-duplicates, which silently DROPS one of the two companies
  (e.g. Tyco 'JCI' vs Johnson Controls 'JCI-201609', 1996-2016) -> we do not use it pre-2019.
* Artifact duplicates in the original file: for 10 companies delisted in 2018 (AET, CA, COL, ESRX, SCG, ANDV,
  EVHC, PX, GGP, XL) the file lists BOTH the stale plain symbol and the suffixed symbol for the same company.
  Rule: a plain key K is an artifact duplicate of K-YYYYMM when K is absent on the last original date, both
  overlap, and K-YYYYMM outlives K. The plain key's dates are merged into the suffixed key.
* 2019-01-12 .. 2026-08-18: '(Updated)' file (fja manual updates from Wikipedia; at-the-time tickers; ticker
  renames appear as add+remove on the same date).
* Known fix: Linde plc (LIN) missing in the original file after Praxair (PX-201810) left on 2018-10-31; fja's
  Updated file adds it only from 2018-11-06. We start LIN on 2018-10-31 (PX's removal date).
Membership semantics: a key is a member on row date d if listed in the row for d (row date = first trading day
the listed composition is effective). Spell end = first row date on which the key is absent (exclusive).
"""
import json
import re
from collections import defaultdict

import pandas as pd

from d1_common import CACHE

FJA = CACHE / "fja"
OG_FILE = FJA / "S&P 500 Historical Components & Changes.csv"
UP_FILE = FJA / "S&P 500 Historical Components & Changes (Updated).csv"
SUFFIX_RE = re.compile(r"-(\d{6})$")

# (key, drop rows dated before this date (None = drop all rows), evidence)
SEAM_DUPLICATES = [
    ("CPRI", "2018-09-19",
     "Michael Kors/Capri listed twice: stale 'KORS' 2013-11-13..2018-09-18 and refreshed 'CPRI' from the 2016-01-04 "
     "seam; Wikipedia lists a single KORS line (count 505 vs fja 506). Same company (SEC CIK 1530721)."),
    ("CCEP", None,
     "Coca-Cola Enterprises listed twice 2016-01-04..2016-05-31: 'CCE' and seam symbol 'CCEP' (successor Coca-Cola "
     "European Partners); both leave on 2016-05-31 (Wikipedia: AJG replaced CCE). Wikipedia shows one line."),
]


def strip_suffix(k: str) -> str:
    return SUFFIX_RE.sub("", k)


def read_rows(path) -> list[tuple[str, set]]:
    df = pd.read_csv(path)
    return [(d, set(x.strip() for x in t.split(",") if x.strip())) for d, t in zip(df["date"], df["tickers"])]


def build():
    og = read_rows(OG_FILE)
    up = read_rows(UP_FILE)
    og_last_date, og_last = og[-1]
    diag = {"og_rows": len(og), "og_first": og[0][0], "og_last": og_last_date,
            "up_rows": len(up), "up_first": up[0][0], "up_last": up[-1][0]}

    # ---- artifact duplicate detection in original file
    first, last = {}, {}
    for d, s in og:
        for k in s:
            first.setdefault(k, d)
            last[k] = d
    artifacts = {}
    for k in list(first):
        m = SUFFIX_RE.search(k)
        if not m:
            continue
        plain = strip_suffix(k)
        if plain in first and plain not in og_last:
            overlap = first[k] <= last[plain] and first[plain] <= last[k]
            if overlap and last[k] >= last[plain]:
                artifacts[plain] = k
    diag["artifact_duplicates"] = artifacts

    rows = []  # (date, set of keys)
    for d, s in og:
        s2 = set(artifacts.get(k, k) for k in s)
        rows.append((d, s2))

    # ---- data-seam duplicates between two PLAIN symbols (same company listed twice 2016-01-04..2018-09-18).
    # The original file visibly concatenates data pulls: counts jump to 512-514 between 2016-01-04 and 2018-09-18
    # because stale and refreshed symbols coexist. Plain-vs-plain cases are not caught by the suffix rule:
    fixes = []
    for key, drop_before, why in SEAM_DUPLICATES:
        n = 0
        for i, (d, s) in enumerate(rows):
            if key in s and (drop_before is None or d < drop_before):
                s.discard(key)
                n += 1
        fixes.append({"key": key, "fix": f"drop rows before {drop_before or 'end (all rows)'} ({n} rows)",
                      "evidence": why})

    # ---- LIN fix (original file lacks Linde plc after 2018-10-31)
    for i, (d, s) in enumerate(rows):
        if "2018-10-31" <= d <= og_last_date and "LIN" not in s:
            s.add("LIN")
            if d == "2018-10-31":
                fixes.append({"key": "LIN", "fix": "add from 2018-10-31 (PX-201810 removal date) to 2019-01-11",
                              "evidence": "Praxair->Linde plc share exchange; og drops PX-201810 on 2018-10-31 but never "
                                          "adds LIN; fja Updated adds LIN from 2018-11-06; Wikipedia list shows LIN by 2018-11-27"})
    # ---- junction check vs Updated at og last date
    up_map = dict(up)
    j_og = set(strip_suffix(k) for k in rows[-1][1])
    j_up = up_map[og_last_date]
    diag["junction_og_minus_up"] = sorted(j_og - j_up)
    diag["junction_up_minus_og"] = sorted(j_up - j_og)

    # ---- append Updated rows after og last date
    for d, s in up:
        if d > og_last_date:
            rows.append((d, set(s)))

    # ---- extend with Wikipedia change-table events after fja's last date (fja ends 2026-08-18)
    ch = pd.read_parquet(CACHE / "wiki_changes.parquet")
    last_d, last_s = rows[-1]
    wiki_rows = []
    for d in sorted(x for x in ch["date"].dropna().unique() if x > last_d and x <= "2026-09-25"):
        g = ch[ch["date"] == d]
        s = set(rows[-1][1])
        for t in g["rem_ticker"].dropna():
            s.discard(str(t))
        for t in g["add_ticker"].dropna():
            s.add(str(t))
        rows.append((d, s))
        wiki_rows.append({"date": d, "added": sorted(g["add_ticker"].dropna()), "removed": sorted(g["rem_ticker"].dropna())})
    diag["wiki_extension"] = wiki_rows

    # ---- spells
    spells = []
    cur = {}
    dates = [d for d, _ in rows]
    for d, s in rows:
        for k in s:
            if k not in cur:
                cur[k] = d
        for k in list(cur):
            if k not in s:
                spells.append((k, cur.pop(k), d))
    for k, st in cur.items():
        spells.append((k, st, None))
    sp = pd.DataFrame(spells, columns=["key", "start", "end"]).sort_values(["key", "start"]).reset_index(drop=True)
    sp["spell_no"] = sp.groupby("key").cumcount() + 1
    sp["ticker"] = sp["key"].map(strip_suffix)
    sp["delist_ym"] = sp["key"].str.extract(r"-(\d{6})$", expand=False)
    up_last = up[-1][0]
    sp["src"] = sp.apply(lambda r: "fja_orig(norgate)" if r.start <= og_last_date else
                         ("fja_updated" if r.start <= up_last else "wikipedia_changes"), axis=1)
    sp["end_src"] = sp["end"].map(lambda e: None if e is None or (isinstance(e, float)) else
                                  ("fja_orig(norgate)" if e <= og_last_date else
                                   ("fja_updated" if e <= up_last else "wikipedia_changes")))
    counts = pd.DataFrame({"date": dates, "n": [len(s) for _, s in rows]})
    long = pd.DataFrame([(d, k) for d, s in rows for k in s], columns=["date", "key"])
    diag["n_keys"] = int(sp.key.nunique())
    diag["n_spells"] = int(len(sp))
    diag["fixes"] = fixes
    diag["count_min"] = int(counts.n.min())
    diag["count_max"] = int(counts.n.max())
    return sp, long, counts, diag


def main():
    sp, long, counts, diag = build()
    sp.to_parquet(CACHE / "fja_spells.parquet", index=False)
    long.to_parquet(CACHE / "fja_long.parquet", index=False)
    counts.to_parquet(CACHE / "fja_counts.parquet", index=False)
    (CACHE / "fja_diag.json").write_text(json.dumps(diag, indent=2))
    print(json.dumps({k: v for k, v in diag.items()}, indent=1)[:3000])
    counts["year"] = counts.date.str[:4]
    print(counts.groupby("year").n.agg(["min", "max"]).T.to_string())


if __name__ == "__main__":
    main()
