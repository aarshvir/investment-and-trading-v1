"""Archive bounded SEC primary filings, with immutable bytes and SHA-256 ledger."""

from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.request
from pathlib import Path

from lxml import html

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw_sec"
INDEX = json.loads((ROOT / "sec_recent_index.json").read_text(encoding="utf-8"))
HEADERS = {"User-Agent": "Investment Research Audit contact institutional.research@example.com"}
WANTED = {
    "AMP": {"10-Q", "8-K"},
    "PAYX": {"10-Q", "8-K"},
    "MSFT": {"10-K", "8-K"},
    "NVDA": {"10-Q", "8-K"},
    "ADP": {"10-K", "8-K"},
    "TJX": {"10-Q", "8-K"},
    "RSG": {"10-Q", "8-K"},
    "LH": {"10-Q", "8-K"},
}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=45) as response:
        return response.read()


out = []
for company in INDEX:
    ticker, cik = company["ticker"], company["cik"]
    most_recent_per_form = {}
    for record in company["last_seven_material_filings"]:
        form = record["form"]
        if form in WANTED[ticker] and form not in most_recent_per_form:
            most_recent_per_form[form] = record
    if ticker == "LH":
        # The 30 September 8-K is decision-critical and must be included.
        most_recent_per_form["8-K"] = company["filings_since_sep25"][0]
    for form, record in most_recent_per_form.items():
        accession_plain = record["accessionNumber"].replace("-", "")
        name = record["primaryDocument"]
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_plain}/{name}"
        try:
            raw = fetch(url)
            stem = f"{ticker}_{record['filingDate']}_{form.replace('-', '')}_{name}"
            dest = RAW / stem
            dest.write_bytes(raw)
            text = html.fromstring(raw).text_content()
            text = re.sub(r"\s+", " ", text)
            (RAW / (stem + ".txt")).write_text(text, encoding="utf-8")
            out.append({
                "ticker": ticker,
                "form": form,
                "filing_date": record["filingDate"],
                "report_date": record["reportDate"],
                "acceptance_utc": record["acceptanceDateTime"],
                "accession": record["accessionNumber"],
                "url": url,
                "local_raw": str(dest.relative_to(ROOT)),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "text_characters": len(text),
            })
            print(ticker, form, record["filingDate"], len(raw))
        except Exception as exc:
            out.append({"ticker": ticker, "form": form, "url": url, "error": str(exc)})
            print(ticker, form, str(exc))
        time.sleep(0.3)

(ROOT / "filing_manifest.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
