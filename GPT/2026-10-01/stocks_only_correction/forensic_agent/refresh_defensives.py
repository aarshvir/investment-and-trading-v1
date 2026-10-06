"""Fetch dated public daily bars for a bounded PG/PEP/PEG comparison."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

import requests


def main() -> None:
    outdir = Path(__file__).parent
    rows = []
    for ticker in ("PG", "PEP", "PEG"):
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=5d&interval=1d"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=25)
        raw = response.content
        (outdir / f"yahoo_{ticker}.json").write_bytes(raw)
        result = response.json()["chart"]["result"][0]
        closes = result["indicators"]["quote"][0]["close"]
        bars = []
        for stamp, close in zip(result["timestamp"], closes):
            bars.append({"date_et": dt.datetime.fromtimestamp(stamp, dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=-4))).date().isoformat(), "close": close})
        rows.append({"ticker": ticker, "url": url, "status": response.status_code,
                     "retrieved_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                     "currency": result["meta"].get("currency"), "symbol": result["meta"].get("symbol"),
                     "bars": bars, "raw_sha256": hashlib.sha256(raw).hexdigest()})
    (outdir / "defensive_quotes.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row["ticker"], [x for x in row["bars"] if x["date_et"] == "2026-09-30"])

    cboe_rows = []
    for ticker in ("PG", "PEP", "PEG"):
        url = f"https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/{ticker}.json"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"}, timeout=25)
        raw = response.content
        (outdir / f"cboe_{ticker}.json").write_bytes(raw)
        cboe_rows.append({"ticker": ticker, "url": url, "status": response.status_code,
                          "retrieved_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                          "raw_sha256": hashlib.sha256(raw).hexdigest(),
                          "data": response.json().get("data") if response.ok else None})
    (outdir / "defensive_cboe_quotes.json").write_text(json.dumps(cboe_rows, indent=2) + "\n", encoding="utf-8")
    for row in cboe_rows:
        data = row["data"] or {}
        print("CBOE", row["ticker"], row["status"], data.get("last_trade_price"), data.get("last_trade_time"))


if __name__ == "__main__":
    main()
