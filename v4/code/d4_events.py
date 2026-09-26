"""d4_events.py - best-effort corporate-event flags for all S&P 500 constituents (as of 2026-09-25).

Method (documented in d4_report.md):
 1. SEC EDGAR submissions index (primary source; filings.recent, filings dated <= 2026-09-25):
    - SC 14D9 (/A) in 365d  -> the company is the SUBJECT of a tender offer (only targets file 14D-9)  [target, strong]
    - PREM14A/DEFM14A/PREM14C/DEFM14C in 365d -> merger proxy / information statement: a shareholder vote on a
      merger (usually the target; can be the acquirer in a large stock deal, or a reorganisation)       [target, medium]
    - SC TO-T (/A) in 365d WITHOUT SC 14D9 -> the company is the BIDDER in a tender offer             [acquirer]
    - S-4 (/A) in 365d -> registers shares for a stock deal (usually the acquirer)                     [acquirer]
    - 425 count in 365d -> communications about a business combination (acquirer or target)          [context]
    - 8-K item 2.01 in 180d -> completed acquisition OR disposition                                    [completed deal]
    - 25-NSE / 25 are NOT used as signals: they are routinely filed when debt securities are delisted.
 2. Yahoo Finance headlines (latest-news + press-release tabs, <=30 each, published <= 365d before as-of):
    company role is inferred from the position of the company name relative to the deal verb:
      '<Company> to acquire / agrees to acquire / enters into agreement to acquire ...'   -> acquirer
      '... to acquire <Company>' (name within 3 words after the verb, not possessive, not followed by
      stake/assets/business/unit/division/interest/portfolio) or '<Company> to be acquired/taken private' -> target
      '<Company> completes/closes acquisition|merger|sale|divestiture|separation|spin-off' -> completed deal
      '<Company> ... spin-off|spinoff|separation|split into' -> spin-off / separation
    Company name = cleaned Wikipedia security name (first two distinctive words) or the ticker in parentheses.
 3. Flags keep the evidence strings (form+date, [date] headline). Best-effort; false positives/negatives likely.

Output: v4/data/d4_corporate_events.csv (+ .meta.json)
"""
from __future__ import annotations

import gzip
import json
import pickle
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import ASOF, CACHE, DATA, utc_now_iso, write_meta  # noqa: E402

SUB = CACHE / "sec" / "submissions"
YC = CACHE / "yahoo"
AS = pd.Timestamp(ASOF)

SUFFIX = r"\b(inc|incorporated|corp|corporation|company|co|plc|ltd|limited|holdings?|group|the|class [a-c]|n\.v\.|nv|s\.a\.|sa|ag|lp|llc|trust)\b\.?"
DEAL_VERB = r"(?:to acquire|agrees? to acquire|agreed to acquire|agreement to acquire|intent to acquire|agrees? to buy|agreed to buy|to take private|to merge with|to combine with|in talks to acquire|nears deal (?:to|for)|bid to acquire|proposal to acquire|proposes to acquire)"
ASSET_WORDS = r"(?:stakes?|assets?|business(?:es)?|units?|divisions?|interests?|portfolio|segment|operations|brands?|plants?|facilit(?:y|ies)|fields?|blocks?|funds?|subsidiar(?:y|ies)|insurance company|company of)"
DEBT_TENDER = re.compile(r"\b(?:notes|debt securities|senior notes|debentures|tender offers? to purchase|offers? to purchase for cash)\b", re.I)


def name_phrases(name: str, ticker: str):
    n = re.sub(r"\(.*?\)", " ", str(name))
    n = re.sub(SUFFIX, " ", n, flags=re.I)
    n = re.sub(r"[,]", " ", n)
    words = [w for w in n.split() if w]
    phrases = set()
    if words:
        phrases.add(" ".join(words[:2]).lower() if len(words) >= 2 and len(words[0]) <= 3 else words[0].lower())
        if len(words) >= 2:
            phrases.add(" ".join(words[:2]).lower())
    phrases = {p for p in phrases if len(p) >= 3}
    phrases.add(f"({ticker.lower()})")
    phrases.add(f"({ticker.lower().replace('-', '.')})")
    return phrases


def find_pos(tl: str, phrases):
    best = None
    for p in phrases:
        for m in re.finditer(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", tl):
            if best is None or m.start() < best[0]:
                best = (m.start(), m.end())
    return best


def classify(title: str, phrases):
    tl = title.lower()
    if DEBT_TENDER.search(tl):
        return set()
    pos = find_pos(tl, phrases)
    if pos is None:
        return set()
    roles = set()
    s, e = pos
    head_words = len(tl[:s].split())
    after = tl[e:]
    # acquirer: company named in the first 4 words and a deal verb follows within 8 words
    m = re.search(DEAL_VERB, after)
    if head_words <= 4 and m and len(after[:m.start()].split()) <= 8 and not re.match(r"\s*(?:'s|’s)", after):
        roles.add("acquirer")
    if head_words <= 4 and re.search(r"\b(?:to be acquired|agrees? to be acquired|to be taken private|to be bought|to sell itself|explores? (?:a )?sale|accepts? .{0,40}(?:offer|bid))\b", after[:80]):
        roles.add("target")
    # target: deal verb shortly before the company name, company not possessive, not an asset sale
    for vm in re.finditer(DEAL_VERB, tl[:s]):
        gap = tl[vm.end():s].split()
        if len(gap) <= 1 and not re.search(r"\bfrom\s*$", tl[:s]) and not re.match(r"\s*(?:'s|’s)", after) and not re.match(r"\s*(?:\w+\s+){0,2}" + ASSET_WORDS + r"\b", after):
            roles.add("target")
    if head_words <= 4 and re.search(r"\b(?:complet(?:es|ed)|clos(?:es|ed)|finaliz(?:es|ed))\b.{0,40}\b(?:acquisition|merger|purchase|sale|divestiture|separation|spin-?off|combination)\b", after[:120]):
        roles.add("completed")
    if re.search(r"\b(?:spin[- ]?off|spins? off|spinoff|separation of|to separate|separate into|split into|split up|break[- ]?up)\b", tl):
        roles.add("spinoff")
    return roles


def sec_flags(cik):
    fp = SUB / f"CIK{int(cik):010d}.json.gz"
    out = {"sec_14d9_365d": "", "sec_merger_proxy_365d": "", "sec_tender_bidder_365d": "", "sec_s4_365d": "",
           "sec_425_365d_n": 0, "sec_8k_201_180d": "", "sec_submissions_ok": False, "sec_recent_oldest": None}
    if not fp.exists():
        return out
    j = json.load(gzip.open(fp, "rt", encoding="utf-8"))
    rc = j["filings"]["recent"]
    df = pd.DataFrame({k: rc[k] for k in ["form", "filingDate", "items"]})
    df["filingDate"] = pd.to_datetime(df["filingDate"])
    df = df[df["filingDate"] <= AS]
    out["sec_submissions_ok"] = True
    out["sec_recent_oldest"] = str(df["filingDate"].min().date()) if len(df) else None

    def lst(mask, cap=260):
        x = df[mask].drop_duplicates(["form", "filingDate"])
        return "; ".join(f"{f} {d.date()}" for f, d in zip(x["form"], x["filingDate"]))[:cap]
    w365 = df["filingDate"] > AS - pd.Timedelta(days=365)
    w180 = df["filingDate"] > AS - pd.Timedelta(days=180)
    f = df["form"]
    out["sec_14d9_365d"] = lst(w365 & f.isin(["SC 14D9", "SC 14D9/A"]))
    out["sec_merger_proxy_365d"] = lst(w365 & f.isin(["PREM14A", "DEFM14A", "PREM14C", "DEFM14C", "DEFM14A/A", "PREM14A/A"]))
    if not out["sec_14d9_365d"]:
        out["sec_tender_bidder_365d"] = lst(w365 & f.isin(["SC TO-T", "SC TO-T/A"]))
    out["sec_s4_365d"] = lst(w365 & f.isin(["S-4", "S-4/A", "F-4"]))
    out["sec_425_365d_n"] = int((w365 & (f == "425")).sum())
    is8k = f.isin(["8-K", "8-K/A"])
    out["sec_8k_201_180d"] = lst(w180 & is8k & df["items"].fillna("").str.contains(r"2\.01"))
    return out


def news_flags(tk, name):
    fp = YC / f"{tk}.pkl"
    out = {"hl_target": "", "hl_acquirer": "", "hl_completed": "", "hl_spinoff": "", "n_headlines": 0}
    if not fp.exists():
        return out
    rec = pickle.load(open(fp, "rb"))
    items = (rec.get("press_releases") or []) + (rec.get("news") or [])
    out["n_headlines"] = len(items)
    phrases = name_phrases(name, tk)
    seen = set()
    for it in items:
        t = (it.get("title") or "").replace(" ", " ")
        if not t or t in seen:
            continue
        seen.add(t)
        pdt = str(it.get("pubDate") or "")[:10]
        if pdt and (pdt < str((AS - pd.Timedelta(days=365)).date()) or pdt > str((AS + pd.Timedelta(days=1)).date())):
            continue
        for role in classify(t, phrases):
            col = "hl_" + role
            if len(out[col]) < 450:
                out[col] += (" | " if out[col] else "") + f"[{pdt}] {t}"
    return out


def main():
    u = pd.read_csv(DATA / "d4_universe.csv")
    rows = []
    for _, r in u.iterrows():
        row = {"ticker": r["ticker"], "name": r["name"], "cik": r["cik"], "gics_sector": r["gics_sector"],
               "date_added_to_index": r["date_added"]}
        row.update(sec_flags(r["cik"]))
        row.update(news_flags(r["ticker"], r["name"]))
        tgt = []
        if row["sec_14d9_365d"]:
            tgt.append("SEC-14D9(strong)")
        if row["sec_merger_proxy_365d"]:
            tgt.append("SEC-merger-proxy(medium)")
        if row["hl_target"]:
            tgt.append("headline")
        row["evt_being_acquired"] = "+".join(tgt)
        acq = []
        if row["sec_tender_bidder_365d"]:
            acq.append("SEC-tender-bidder")
        if row["sec_s4_365d"]:
            acq.append("SEC-S-4")
        if row["hl_acquirer"]:
            acq.append("headline")
        row["evt_acquirer_pending_or_recent"] = "+".join(acq)
        comp = []
        if row["sec_8k_201_180d"]:
            comp.append("SEC-8-K-2.01")
        if row["hl_completed"]:
            comp.append("headline")
        row["evt_recent_completed_deal"] = "+".join(comp)
        row["evt_spinoff_separation"] = "headline" if row["hl_spinoff"] else ""
        rows.append(row)
    d = pd.DataFrame(rows)
    out = DATA / "d4_corporate_events.csv"
    d.to_csv(out, index=False)
    summ = {c: int((d[c] != "").sum()) for c in ["evt_being_acquired", "evt_acquirer_pending_or_recent",
                                                "evt_recent_completed_deal", "evt_spinoff_separation"]}
    summ["being_acquired_sec_14d9"] = int(d["sec_14d9_365d"].ne("").sum())
    summ["being_acquired_merger_proxy"] = int(d["sec_merger_proxy_365d"].ne("").sum())
    summ["companies_with_425_filings"] = int((d["sec_425_365d_n"] > 0).sum())
    write_meta(out, {"description": "best-effort corporate-event flags (SEC submissions forms + Yahoo headlines)",
                     "source_urls": ["https://data.sec.gov/submissions/CIK##########.json",
                                     "Yahoo Finance news + press-release tabs via yfinance get_news()"],
                     "retrieval_utc": utc_now_iso(), "rows": int(len(d)), "columns": list(d.columns),
                     "flag_counts": summ, "as_of": ASOF.isoformat(),
                     "caveats": ["Headline heuristics; SEC 8-K 2.01 covers acquisitions AND dispositions.",
                                 "Merger proxies can be filed by acquirers (large stock deals) or for reorganisations.",
                                 "SEC 'recent' block = latest ~1000 filings per filer (sec_recent_oldest shows coverage).",
                                 "Yahoo news tabs cover only the latest ~30 headlines each, so older deals can be missed."]})
    print(summ)


if __name__ == "__main__":
    main()
