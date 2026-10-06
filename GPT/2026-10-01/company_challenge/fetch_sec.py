"""Archive SEC filing-index evidence for the bounded October 1 company audit."""

from __future__ import annotations

import hashlib
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw_sec"
RAW.mkdir(parents=True, exist_ok=True)
CIKS = {
    "AMP": 820027,
    "PAYX": 723531,
    "MSFT": 789019,
    "NVDA": 1045810,
    "ADP": 8670,
    "TJX": 109198,
    "RSG": 1060391,
    "LH": 920148,
}
HEADERS = {"User-Agent": "Investment Research Audit contact institutional.research@example.com"}


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


rows = []
for ticker, cik in CIKS.items():
    url = f"https://data.sec.gov/submissions/CIK{cik:010d}.json"
    data = fetch(url)
    filename = RAW / f"{ticker}_submissions.json"
    filename.write_bytes(data)
    payload = json.loads(data)
    recent = payload["filings"]["recent"]
    columns = ["form", "filingDate", "reportDate", "acceptanceDateTime", "accessionNumber", "primaryDocument"]
    records = [dict(zip(columns, values)) for values in zip(*(recent[k] for k in columns))]
    material = [
        record for record in records
        if "2026-09-25" <= record["filingDate"] <= "2026-10-01"
        and record["form"] in {"8-K", "10-Q", "10-K", "10-Q/A", "10-K/A", "424B2"}
    ]
    trailing = [
        record for record in records
        if record["form"] in {"8-K", "10-Q", "10-K"}
        and record["filingDate"] <= "2026-10-01"
    ][:7]
    rows.append({
        "ticker": ticker,
        "cik": cik,
        "url": url,
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "filings_since_sep25": material,
        "last_seven_material_filings": trailing,
    })
    time.sleep(0.2)

(ROOT / "sec_recent_index.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
for row in rows:
    print(row["ticker"], len(row["filings_since_sep25"]), row["filings_since_sep25"])
