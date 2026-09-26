"""d1_sec_ref.py - SEC reference data helpers for D1: ticker->CIK tables, cik-lookup name index, submissions
summaries (with older filing pages fetched only when needed), name normalisation.
"""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache

import pandas as pd

from d1_common import CACHE, get_submissions, get_submissions_page

LEGAL = {"INC", "INCORPORATED", "CORP", "CORPORATION", "CO", "COMPANY", "COS", "COMPANIES", "LTD", "LIMITED",
         "PLC", "LLC", "LP", "NV", "SA", "AG", "THE", "HLDGS", "SE", "CLASS", "CL", "SERIES"}
GENERIC = {"HOLDINGS", "HOLDING", "GROUP", "INTERNATIONAL", "ENTERPRISES", "TRUST", "BANCORP", "BANCORPORATION",
           "INDUSTRIES", "COMMUNICATIONS", "TECHNOLOGIES", "TECHNOLOGY", "SYSTEMS", "FINANCIAL", "SERVICES"}
ABBR = {"INTL": "INTERNATIONAL", "INT'L": "INTERNATIONAL", "LABS": "LABORATORIES", "MGMT": "MANAGEMENT",
        "SVCS": "SERVICES", "SVC": "SERVICE", "TECH": "TECHNOLOGIES", "PHARM": "PHARMACEUTICALS",
        "PHARMS": "PHARMACEUTICALS", "COMM": "COMMUNICATIONS", "COMMS": "COMMUNICATIONS", "NATL": "NATIONAL",
        "AMER": "AMERICAN", "MFG": "MANUFACTURING", "BANCSHARES": "BANCSHARES", "HLDG": "HOLDING",
        "RES": "RESOURCES", "PETE": "PETROLEUM", "ELEC": "ELECTRIC", "TEL": "TELEPHONE", "SYS": "SYSTEMS",
        "PROD": "PRODUCTS", "PRODS": "PRODUCTS", "INDS": "INDUSTRIES", "FINL": "FINANCIAL", "GRP": "GROUP",
        "CTRS": "CENTERS", "ENTMT": "ENTERTAINMENT", "BK": "BANK", "CORP.": "CORP", "N.V.": "NV", "S.A.": "SA",
        "GENL": "GENERAL", "GEN": "GENERAL", "RLTY": "REALTY", "PPTYS": "PROPERTIES", "PPTY": "PROPERTY",
        "MTG": "MORTGAGE", "DEPT": "DEPARTMENT", "STRS": "STORES", "BROS": "BROTHERS", "CHEM": "CHEMICAL",
        "INSUR": "INSURANCE", "INS": "INSURANCE", "LAB": "LABORATORIES", "SVC": "SERVICE", "MGT": "MANAGEMENT",
        "ASSN": "ASSOCIATION", "ASSOC": "ASSOCIATES", "INVT": "INVESTMENT", "DEV": "DEVELOPMENT",
        "EQUIP": "EQUIPMENT", "MED": "MEDICAL", "HLTH": "HEALTH", "UTD": "UNITED", "AMERN": "AMERICAN",
        "NATIONL": "NATIONAL", "PWR": "POWER", "GP": "GROUP", "SEMICONDUCTR": "SEMICONDUCTOR"}
US_STATES = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
             "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
             "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"}
FUZZY_DROP = {"NEW", "OLD", "DEL", "AND", "OF"} | US_STATES


def _tokens(name: str) -> list[str]:
    s = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode("ascii").upper()
    s = re.sub(r"\((THE|CLASS [A-Z]|CL [A-Z]|SERIES [A-Z])\)", " ", s)
    s = re.sub(r"\b(CLASS|CL|SERIES) [A-Z]\b", " ", s)
    s = re.sub(r"\((PRED|SUCC|OLD|NEW)\)", " ", s)
    s = re.sub(r"/[A-Z]{2,4}/", " ", s)          # SEC state tags like /DE/ /NEW/
    s = re.sub(r"\s/[A-Z]{2,5}/?(?=\s|$)", " ", s)  # trailing state tags like ' /DE'
    s = re.sub(r"/[A-Z]{2,5}/?$", " ", s)            # glued trailing tags like 'HCA INC/TN'
    s = s.replace("&", " AND ").replace("+", " AND ")
    s = s.replace("'", "").replace("’", "")
    s = re.sub(r"[^A-Z0-9 ]", " ", s)
    toks = [ABBR.get(t, t) for t in s.split()]
    return toks


def norm1(name: str) -> str:
    """drop legal-form words + punctuation (task spec: drop Inc/Corp/Co/Ltd/&/punctuation)."""
    toks = [t for t in _tokens(name) if t not in LEGAL and t != "AND"]
    return " ".join(toks)


def norm2(name: str) -> str:
    toks = [t for t in norm1(name).split() if t not in GENERIC]
    return " ".join(toks) if toks else norm1(name)


def squash(name: str) -> str:
    return norm1(name).replace(" ", "")


def token_sim(a: str, b: str) -> float:
    ta, tb = set(norm1(a).split()), set(norm1(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


@lru_cache(maxsize=1)
def company_tickers() -> pd.DataFrame:
    d = json.loads((CACHE / "company_tickers_exchange.json").read_text())
    df = pd.DataFrame(d["data"], columns=d["fields"])
    df["ticker_norm"] = df["ticker"].str.upper().str.replace(".", "-", regex=False)
    return df


@lru_cache(maxsize=1)
def cik_lookup() -> pd.DataFrame:
    pq = CACHE / "cik_lookup.parquet"
    if pq.exists():
        return pd.read_parquet(pq)
    rows = []
    with open(CACHE / "cik-lookup-data.txt", encoding="latin-1") as f:
        for line in f:
            line = line.rstrip("\n")
            m = re.match(r"^(.*):(\d{10}):\s*$", line)
            if not m:
                continue
            nm = re.sub(r"\s+", " ", m.group(1)).strip()
            if not nm:
                continue
            rows.append((nm, int(m.group(2))))
    df = pd.DataFrame(rows, columns=["name", "cik"]).drop_duplicates()
    df["n1"] = df["name"].map(norm1)
    df["n2"] = df["name"].map(norm2)
    df["sq"] = df["n1"].str.replace(" ", "", regex=False)
    df.to_parquet(pq, index=False)
    return df


@lru_cache(maxsize=1)
def lookup_indexes():
    df = cik_lookup()
    idx = {}
    for col in ("n1", "n2", "sq"):
        idx[col] = df.groupby(col)["cik"].apply(lambda s: sorted(set(s))).to_dict()
    return idx


def _ftoks(name: str) -> list[str]:
    return [t for t in norm1(name).split() if t not in FUZZY_DROP]


@lru_cache(maxsize=1)
def fuzzy_index():
    """first-token -> list of (token tuple, cik, name) over the SEC cik-lookup names"""
    df = cik_lookup()
    idx = {}
    for nm, ck in zip(df["name"], df["cik"]):
        toks = tuple(_ftoks(nm))
        if not toks:
            continue
        idx.setdefault(toks[0], []).append((toks, int(ck), nm))
    return idx


def fuzzy_sim(qt: tuple, ct: tuple) -> float:
    a, b = set(qt), set(ct)
    if not a or not b:
        return 0.0
    if "".join(qt) == "".join(ct):
        return 1.0
    jac = len(a & b) / len(a | b)
    short, long_ = (a, b) if len(a) <= len(b) else (b, a)
    cont = len(short & long_) / len(short)
    distinctive = any(len(t) >= 4 and t not in GENERIC for t in short)
    return max(jac, 0.9 * cont if (cont == 1.0 and distinctive) else 0.0)


def fuzzy_candidates(name: str, top: int = 8, min_sim: float = 0.6) -> list[tuple[int, float, str]]:
    """(cik, sim, sec_name) for SEC names sharing the first significant token; best sim per CIK."""
    qt = tuple(_ftoks(name))
    if not qt:
        return []
    best = {}
    # SEC conformed names often invert personal names ('CLAIBORNE LIZ INC', 'MORGAN J P & CO', 'BARD C R INC'):
    # also look up rotations of the first one/two tokens.
    variants = [qt] + ([qt[1:] + qt[:1]] if len(qt) >= 2 else []) + ([qt[2:] + qt[:2]] if len(qt) >= 3 else [])
    for v in variants:
        pool = fuzzy_index().get(v[0], [])
        if len(v) >= 2 and len(pool) > 4000:
            pool = [p for p in pool if v[1] in p[0]]
        for toks, ck, nm in pool:
            s = fuzzy_sim(qt, toks)
            if s >= min_sim and s > best.get(ck, (0, ""))[0]:
                best[ck] = (s, nm)
    out = sorted(((ck, s, nm) for ck, (s, nm) in best.items()), key=lambda x: -x[1])
    return out[:top]


def name_candidates(name: str) -> dict[int, str]:
    """CIK candidates for a company name via exact normalised matches; returns {cik: match_level}."""
    idx = lookup_indexes()
    out = {}
    for col, fn in (("n1", norm1), ("sq", squash), ("n2", norm2)):
        key = fn(name)
        if not key:
            continue
        for c in idx[col].get(key, []):
            out.setdefault(c, col)
    return out


REPORT_FORMS = {"10-K", "10-K405", "10-KSB", "10-KT", "10-Q", "10-QSB", "20-F", "40-F", "10-K/A", "10-Q/A",
                "20-F/A", "40-F/A", "10-KSB40", "10-K405/A"}


def _filings_frame(block: dict) -> pd.DataFrame:
    if not block or "form" not in block:
        return pd.DataFrame(columns=["form", "filingDate", "reportDate"])
    return pd.DataFrame({"form": block.get("form", []), "filingDate": block.get("filingDate", []),
                         "reportDate": block.get("reportDate", [""] * len(block.get("form", [])))})


def submissions_summary(cik: int, need_from: str | None = None) -> dict | None:
    """Summary of a CIK's submissions. If need_from (YYYY-MM-DD) is earlier than the oldest 'recent' filing,
    older pages overlapping [need_from, ...] are fetched and included."""
    d = get_submissions(cik)
    if d is None:
        return None
    rec = _filings_frame(d.get("filings", {}).get("recent", {}))
    frames = [rec]
    files = d.get("filings", {}).get("files", []) or []
    oldest_recent = rec["filingDate"].min() if len(rec) else "9999-12-31"
    if need_from and files and need_from < oldest_recent:
        for fmeta in files:
            if fmeta.get("filingTo", "9999") >= need_from:
                pg = get_submissions_page(fmeta["name"])
                if pg:
                    frames.append(_filings_frame(pg))
    fl = pd.concat(frames, ignore_index=True)
    rep = fl[fl["form"].isin(REPORT_FORMS)]
    return {
        "cik": int(cik),
        "name": d.get("name"),
        "formerNames": d.get("formerNames", []),
        "tickers": d.get("tickers", []),
        "exchanges": d.get("exchanges", []),
        "sic": d.get("sic"),
        "sicDescription": d.get("sicDescription"),
        "fiscalYearEnd": d.get("fiscalYearEnd"),
        "stateOfIncorporation": d.get("stateOfIncorporation"),
        "entityType": d.get("entityType"),
        "n_filings_loaded": int(len(fl)),
        "has_older_pages": bool(files),
        "oldest_loaded": fl["filingDate"].min() if len(fl) else None,
        "report_dates": sorted(rep["filingDate"].tolist()),
        "first_report": rep["filingDate"].min() if len(rep) else None,
        "last_report": rep["filingDate"].max() if len(rep) else None,
        "last_filing": fl["filingDate"].max() if len(fl) else None,
    }


def filed_reports_between(summary: dict, start: str, end: str, slack_days: int = 400) -> int:
    """# of 10-K/10-Q/20-F/40-F filings within [start - slack, end + slack]."""
    if not summary:
        return 0
    s = (pd.Timestamp(start) - pd.Timedelta(days=slack_days)).strftime("%Y-%m-%d")
    e = (pd.Timestamp(end) + pd.Timedelta(days=slack_days)).strftime("%Y-%m-%d") if end else "9999-12-31"
    return sum(1 for x in summary["report_dates"] if s <= x <= e)


def all_names(summary: dict) -> list[str]:
    if not summary:
        return []
    return [summary["name"]] + [f.get("name") for f in summary.get("formerNames", []) if f.get("name")]
