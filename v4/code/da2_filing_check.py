"""da2_filing_check.py - filing-document truth test: fetch real SEC filing statement pages (R.htm, the
SEC-rendered financial statements from the filer's own inline XBRL) for sampled companies and compare
to d3_xbrl_facts / d3_pit_monthly. Writes v4/audit/da2_supporting/filing_truth_test.csv.
"""
from __future__ import annotations
import sys, re, io, json, traceback
sys.path.insert(0, r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\code")
import da2_common as c
import numpy as np
import pandas as pd

SUP = c.AUDIT / "da2_supporting"
SUP.mkdir(parents=True, exist_ok=True)

facts = pd.read_parquet(c.DATA / "d3_xbrl_facts.parquet")
pit = pd.read_parquet(c.DATA / "d3_pit_monthly.parquet")
cmeta = pd.read_csv(c.DATA / "d3_company_meta.csv")
sample = pd.read_csv(SUP / "sample32.csv")

METRIC_PATTERNS = {
    "revenue": [r"^total revenues?$", r"^total net (sales|revenues?)$", r"^net (sales|revenues?)$",
                r"^total interest and.*income$", r"^net revenue$", r"^total revenue, net$"],
    "operating_income": [r"^(income|earnings) from operations$", r"^operating income", r"^total operating income"],
    "net_income_common": [r"net (income|earnings).*attributable to.*(common|shareholders|stockholders)",
                           r"^net (income|earnings) attributable to", r"^net (income|loss)$", r"^net earnings$"],
    "eps_diluted": [r"diluted$", r"^diluted$", r"net.*per share.*diluted", r"^earnings per share,? diluted"],
    "ocf": [r"net cash (provided by|from).*operating activities"],
    "capex": [r"purchases? of property", r"payments? (for|to acquire) property", r"capital expenditures?",
              r"additions to property"],
    "cash_sti": [r"^cash and cash equivalents$", r"^cash, cash equivalents"],
    "shares_out": [r"entity common stock, shares outstanding"],
}
NEG_HINT = ["basic"]  # rows containing these are lower priority for eps_diluted if 'diluted' absent


def fetch_reports(cik, accn):
    base = c.filing_base(cik, accn)
    b = c.sec_get(base + "FilingSummary.xml")
    txt = b.decode("utf-8", "ignore")
    reports = re.findall(r"<Report[^>]*>.*?</Report>", txt, re.S)
    out = []
    for r in reports:
        html = re.search(r"<HtmlFileName>(.*?)</HtmlFileName>", r)
        short = re.search(r"<ShortName>(.*?)</ShortName>", r)
        menu = re.search(r"<MenuCategory>(.*?)</MenuCategory>", r)
        if html and short:
            out.append((html.group(1), short.group(1), menu.group(1) if menu else ""))
    return base, out


def get_rows(base, htmlfile):
    b = c.sec_get(base + htmlfile)
    txt = b.decode("utf-8", "ignore")
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", txt, re.S)
    rows = []
    for r in trs:
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)
        clean = [re.sub("<[^<]+?>", "", cell).replace("&#160;", " ").replace("&nbsp;", " ").replace("&#xA0;", " ").strip() for cell in cells]
        clean = [x for x in clean if x != ""]
        if clean:
            rows.append(clean)
    return rows


NUM_RE = re.compile(r"^\(?\$?\s*-?[\d,]+\.?\d*\)?%?$")


def first_number(cells):
    for cell in cells:
        cc = cell.strip()
        if cc in ("$", "-", "&#8212;", "\u2014"):
            continue
        if NUM_RE.match(cc):
            neg = cc.startswith("(")
            cc2 = re.sub(r"[\$,()%]", "", cc)
            try:
                v = float(cc2)
                return -v if neg else v
            except ValueError:
                continue
    return None


def find_metric(rows, patterns, avoid_basic_for_diluted=False):
    best = None
    for row in rows:
        label = row[0].lower().strip()
        for pat in patterns:
            if re.search(pat, label):
                if avoid_basic_for_diluted and "diluted" not in label and "basic" in label:
                    continue
                val = first_number(row[1:])
                if val is not None:
                    return val, row[0]
    return None, None


def get_statement_pages(base, reports, keywords):
    out = []
    for html, short, menu in reports:
        s = short.lower()
        if any(k in s for k in keywords):
            out.append((html, short))
    return out


def check_company(ticker, cik, accn, form, period_end, filed):
    base, reports = fetch_reports(cik, accn)
    result = {"ticker": ticker, "cik": cik, "accn": accn, "form": form, "period_end": str(period_end.date()), "filed": str(filed.date())}
    income_pages = get_statement_pages(base, reports, ["operations", "earnings", "income"])
    cf_pages = get_statement_pages(base, reports, ["cash flow"])
    bs_pages = get_statement_pages(base, reports, ["balance sheet", "financial position"])
    cover_pages = get_statement_pages(base, reports, ["cover"])
    income_pages = [p for p in income_pages if "comprehensive" not in p[1].lower()][:1] or income_pages[:1]
    cf_pages = cf_pages[:1]
    bs_pages = [p for p in bs_pages if "parenthetical" not in p[1].lower()][:1] or bs_pages[:1]
    cover_pages = cover_pages[:1]

    for label, pages, keys in [("income", income_pages, ["revenue", "operating_income", "net_income_common", "eps_diluted"]),
                                ("cf", cf_pages, ["ocf", "capex"]),
                                ("bs", bs_pages, ["cash_sti"]),
                                ("cover", cover_pages, ["shares_out"])]:
        if not pages:
            for k in keys:
                result[k] = None
                result[k + "_label"] = "NO_PAGE"
            continue
        try:
            rows = get_rows(base, pages[0][0])
        except Exception as e:
            for k in keys:
                result[k] = None
                result[k + "_label"] = f"FETCH_ERR:{e}"
            continue
        for k in keys:
            avoid = k == "eps_diluted"
            v, lbl = find_metric(rows, METRIC_PATTERNS[k], avoid_basic_for_diluted=avoid)
            result[k] = v
            result[k + "_label"] = lbl
    result["_income_page"] = income_pages[0][1] if income_pages else None
    result["_url"] = base
    return result


def pick_filings(cik, n_recent_q=1, want_10k=False):
    df = c.filings_table(cik)
    df["filingDate"] = pd.to_datetime(df["filingDate"])
    df["reportDate"] = pd.to_datetime(df["reportDate"])
    df = df.sort_values("filingDate")
    out = []
    q = df[df.form == "10-Q"].tail(n_recent_q)
    for _, r in q.iterrows():
        out.append(r)
    if want_10k:
        k = df[df.form == "10-K"].tail(1)
        for _, r in k.iterrows():
            out.append(r)
    return out


results = []
errors = []
for _, srow in sample.iterrows():
    ticker = srow.ticker
    cik = srow.cik
    if pd.isna(cik):
        errors.append((ticker, "no_cik"))
        continue
    cik = int(cik)
    want_10k = srow.group == "purposive"
    try:
        filings = pick_filings(cik, n_recent_q=1, want_10k=want_10k)
    except Exception as e:
        errors.append((ticker, f"filings_table_err:{e}"))
        continue
    for f in filings:
        try:
            res = check_company(ticker, cik, f.accessionNumber, f.form, f.reportDate, f.filingDate)
            results.append(res)
            print("OK", ticker, f.form, f.reportDate.date())
        except Exception as e:
            errors.append((ticker, f"{f.form} {f.reportDate.date()} err:{e}"))
            print("ERR", ticker, f.form, e)

res_df = pd.DataFrame(results)
res_df.to_csv(SUP / "filing_truth_test_raw.csv", index=False)
with open(SUP / "filing_truth_test_errors.json", "w") as fh:
    json.dump(errors, fh, indent=2, default=str)
print("done:", len(res_df), "filings checked;", len(errors), "errors")
