"""d1_snaplink.py - direct linking of fja membership keys to Wikipedia month-end snapshot rows (2007-03..2026-09).

For every calendar month m we compare fja membership at the calendar month-end with the Wikipedia list as it stood
then (last revision saved on/before the month-end). Direct rule: tickers compared after removing punctuation
('BRK.B' = 'BRKB' = 'BRK-B'). When two fja keys share the stripped ticker (e.g. plain 'AGN' = Actavis/Allergan plc
and 'AGN-201503' = Allergan Inc), the suffixed key wins while m <= its delisting month, because the suffix marks the
company that actually traded under that ticker until then. Remaining unmatched keys/rows are paired later by
d1_identity.py (co-occurrence + name/ticker gating).
Outputs (cache): snaplink_month.parquet (month, key, wiki_ticker, wiki_name, wiki_cik, wiki_sector, link)
                 snaplink_wiki_unmatched.parquet (month, wiki_ticker, tk, wiki_name, wiki_cik, wiki_sector)
"""
import re
from collections import defaultdict

import pandas as pd

from d1_common import CACHE

SUFFIX_RE = re.compile(r"-(\d{6})$")
LAST_DATA_DATE = "2026-09-25"


def tkey(t: str) -> str:
    """punctuation-insensitive ticker key"""
    return re.sub(r"[^A-Z0-9]", "", str(t).strip().upper())


def load_snapshots() -> tuple[pd.DataFrame, dict]:
    sn = pd.read_parquet(CACHE / "wiki_snapshots.parquet")
    sn["ticker"] = (sn["ticker"].astype(str).str.replace("\xa0", " ").str.split(":").str[-1].str.strip()
                    .str.upper())
    sn["tk"] = sn["ticker"].map(tkey)
    sn["cikn"] = pd.to_numeric(sn["cik"], errors="coerce").astype("Int64")
    months = [str(p) for p in pd.period_range("2007-03", "2026-09", freq="M")]
    avail = sorted(sn["rev_month"].unique())
    asof, j = {}, 0
    for m in months:
        while j + 1 < len(avail) and avail[j + 1] <= m:
            j += 1
        asof[m] = avail[j] if avail[j] <= m else None
    return sn, asof


def month_end(m: str) -> str:
    d = pd.Period(m, freq="M").to_timestamp(how="end").strftime("%Y-%m-%d")
    return min(d, LAST_DATA_DATE)


def members_at(sp: pd.DataFrame, d: str) -> list[str]:
    e = sp["end"].fillna("9999-12-31")
    return sp.loc[(sp["start"] <= d) & (e > d), "key"].tolist()


def build():
    sp = pd.read_parquet(CACHE / "fja_spells.parquet")
    sn, asof = load_snapshots()
    by_rev = {m: df for m, df in sn.groupby("rev_month")}
    rows, wiki_unmatched = [], []
    for m in asof:
        keys = members_at(sp, month_end(m))
        snap = by_rev[asof[m]]
        by_t = defaultdict(list)
        for k in keys:
            by_t[tkey(SUFFIX_RE.sub("", k))].append(k)
        matched = set()
        ym = int(m.replace("-", ""))
        for _, r in snap.iterrows():
            cands = [k for k in by_t.get(r.tk, []) if k not in matched]
            chosen = None
            if len(cands) == 1:
                chosen = cands[0]
            elif len(cands) > 1:
                suff = [k for k in cands if SUFFIX_RE.search(k) and int(SUFFIX_RE.search(k).group(1)) >= ym]
                chosen = (sorted(suff, key=lambda k: SUFFIX_RE.search(k).group(1))[0] if suff
                          else next((k for k in cands if not SUFFIX_RE.search(k)), cands[0]))
            if chosen:
                matched.add(chosen)
                rows.append((m, chosen, r.ticker, r["name"], r.cikn, r.gics_sector, "ticker"))
            else:
                wiki_unmatched.append((m, r.ticker, r.tk, r["name"], r.cikn, r.gics_sector))
        for k in keys:
            if k not in matched:
                rows.append((m, k, None, None, pd.NA, None, "unmatched"))
    L = pd.DataFrame(rows, columns=["month", "key", "wiki_ticker", "wiki_name", "wiki_cik", "wiki_sector", "link"])
    W = pd.DataFrame(wiki_unmatched, columns=["month", "wiki_ticker", "tk", "wiki_name", "wiki_cik", "wiki_sector"])
    L["wiki_cik"] = L["wiki_cik"].astype("Int64")
    W["wiki_cik"] = W["wiki_cik"].astype("Int64")
    for df in (L, W):
        for c in df.columns:
            if df[c].dtype == object:
                df[c] = df[c].astype("string")
    return L, W


def main():
    L, W = build()
    L.to_parquet(CACHE / "snaplink_month.parquet", index=False)
    W.to_parquet(CACHE / "snaplink_wiki_unmatched.parquet", index=False)
    print(L.link.value_counts().to_dict(), "wiki unmatched rows:", len(W))


if __name__ == "__main__":
    main()
