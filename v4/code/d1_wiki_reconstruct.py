"""d1_wiki_reconstruct.py - independent membership reconstruction by walking Wikipedia's change table backwards
from the current (2026-09-25) Wikipedia constituent list.

state_before(D) = state_after(D) - added(D) + removed(D), for change dates D in descending order.
Tickers are at-the-time tickers of each change row (punctuation-insensitive keys). Renames that are not
index events (e.g. FB->META) are NOT in the change table, so the walk carries current tickers backwards;
the comparison with fja (d1_reconcile.py) therefore happens in entity space.
Outputs (cache): wiki_recon_states.parquet (valid_from, valid_to, tk) - half-open [valid_from, valid_to)
                 wiki_recon_log.csv (anomalies: undo of an add whose ticker is absent, re-add of a present ticker)
"""
import pandas as pd

from d1_common import CACHE
from d1_snaplink import tkey

START_DATE = "2026-09-25"


def reconstruct():
    cur = pd.read_parquet(CACHE / "wiki_current.parquet")
    ch = pd.read_parquet(CACHE / "wiki_changes.parquet")
    state = set(cur["symbol"].map(tkey))
    intervals = []   # (valid_from, valid_to, tk)
    log = []
    upper = "9999-12-31"
    # the current list is valid from the latest change date onward
    dates = sorted(ch["date"].dropna().unique(), reverse=True)
    for D in dates:
        rows = ch[ch.date == D]
        for t in state:
            intervals.append((D, upper, t))
        upper = D
        adds = [tkey(x) for x in rows.add_ticker.dropna()]
        rems = [tkey(x) for x in rows.rem_ticker.dropna()]
        for a in adds:
            if a in state:
                state.discard(a)
            else:
                log.append({"date": D, "issue": "undo-add: ticker not in later state", "ticker": a,
                            "row_ids": ",".join(map(str, rows.row_id))})
        for r in rems:
            if r in state and r not in adds:
                log.append({"date": D, "issue": "undo-remove: ticker already in earlier state (reuse/error)",
                            "ticker": r, "row_ids": ",".join(map(str, rows.row_id))})
            state.add(r)
    for t in state:
        intervals.append(("1900-01-01", upper, t))
    iv = pd.DataFrame(intervals, columns=["valid_from", "valid_to", "tk"])
    # compress consecutive intervals per ticker
    iv = iv.sort_values(["tk", "valid_from"])
    out = []
    for t, g in iv.groupby("tk"):
        cs, ce = None, None
        for s, e in zip(g.valid_from, g.valid_to):
            if cs is None:
                cs, ce = s, e
            elif s == ce:
                ce = e
            else:
                out.append((cs, ce, t))
                cs, ce = s, e
        out.append((cs, ce, t))
    res = pd.DataFrame(out, columns=["valid_from", "valid_to", "tk"])
    return res, pd.DataFrame(log)


def members_at(res: pd.DataFrame, d: str) -> set:
    return set(res.loc[(res.valid_from <= d) & (res.valid_to > d), "tk"])


def main():
    res, log = reconstruct()
    res.to_parquet(CACHE / "wiki_recon_states.parquet", index=False)
    log.to_csv(CACHE / "wiki_recon_log.csv", index=False)
    for d in ["2026-09-25", "2020-01-02", "2015-01-02", "2010-01-04", "2005-01-03", "2000-01-03"]:
        print(d, len(members_at(res, d)))
    print("anomalies:", len(log))
    print(log.head(40).to_string())


if __name__ == "__main__":
    main()
