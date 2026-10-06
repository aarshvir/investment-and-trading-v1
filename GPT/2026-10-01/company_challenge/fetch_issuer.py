"""Archive issuer disclosures that may not appear in SEC submissions."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw_issuer"
RAW.mkdir(exist_ok=True)
SOURCES = {
    "AMP_2026-09-29_buyback": "https://ir.ameriprise.com/news/news-details/2026/Ameriprise-Financial-Announces-Additional-5-5-Billion-Share-Repurchase-Authorization/default.aspx",
    "MSFT_2026-09-15_dividend": "https://news.microsoft.com/source/2026/09/15/microsoft-announces-quarterly-dividend-increase-7/",
    "ADP_2026-08-05_dividend": "https://investors.adp.com/news/news-details/2026/ADP-Declares-Regular-Quarterly-Dividend-a7157c3eb/default.aspx",
    "NVDA_2026-09-30_CoreWeave": "https://blogs.nvidia.com/blog/coreweave-agentic-ai-vera-rubin/",
    "LH_2026-09-30_calendar": "https://www.sec.gov/Archives/edgar/data/920148/000092014826000207/lh-20260930.htm",
}
rows = []
for label, url in SOURCES.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Investment Research Audit contact institutional.research@example.com"})
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read()
        path = RAW / (label + ".html")
        path.write_bytes(raw)
        rows.append({"label": label, "url": url, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw), "path": str(path.relative_to(ROOT))})
        print(label, len(raw))
    except Exception as exc:
        rows.append({"label": label, "url": url, "error": str(exc)})
        print(label, "ERROR", exc)
(ROOT / "issuer_manifest.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
