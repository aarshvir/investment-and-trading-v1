"""Reproduce the bounded stock-only model weights and dated quote bridge.

This is a research snapshot, not an order generator or return optimizer.
"""

import csv
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRICE_FILE = ROOT / "MARKET_RECONCILIATION.csv"

ROWS = [
    ("MSFT", "Information Technology", 8),
    ("AMP", "Financials", 6),
    ("NVDA", "Information Technology", 4),
    ("ADP", "Industrials", 6),
    ("TJX", "Consumer Discretionary", 6),
    ("RSG", "Industrials", 5),
    ("MA", "Financials", 5),
    ("MCK", "Health Care", 6),
    ("STE", "Health Care", 5),
    ("BALL", "Materials", 4),
    ("DOV", "Industrials", 5),
    ("BR", "Industrials", 4),
    ("AXP", "Financials", 5),
    ("USB", "Financials", 4),
    ("CRH", "Materials", 5),
    ("PTC", "Information Technology", 4),
    ("VEEV", "Health Care", 4),
    ("GDDY", "Information Technology", 4),
    ("ALLE", "Industrials", 5),
    ("HIG", "Financials", 5),
]

assert len(ROWS) == 20
assert len({t for t, _, _ in ROWS}) == 20
assert sum(w for _, _, w in ROWS) == 100
assert max(w for _, _, w in ROWS) == 8

with PRICE_FILE.open(newline="", encoding="utf-8") as f:
    prices = {r["ticker"]: r for r in csv.DictReader(f)}

sectors = defaultdict(int)
records = []
for ticker, sector, weight in ROWS:
    quote = prices[ticker]
    assert quote["date_et"] == "2026-09-30"
    assert quote["currency"] == "USD"
    assert quote["quote_status"] == "two_public_feeds_agree_within_0.1pct"
    assert float(quote["relative_close_gap_pct"]) < 0.1
    sectors[sector] += weight
    records.append(
        {
            "ticker": ticker,
            "sector": sector,
            "weight_pct": weight,
            "target_dollars_50000": 500 * weight,
            "target_dollars_100000": 1000 * weight,
            "reference_date_et": quote["date_et"],
            "reference_yahoo_close_usd": float(quote["yahoo_regular_close"]),
            "cboe_late_trade_usd": float(quote["cboe_close"]),
            "quote_gap_pct": float(quote["relative_close_gap_pct"]),
            "yahoo_raw_sha256": quote["yahoo_raw_sha256"],
            "cboe_raw_sha256": quote["cboe_raw_sha256"],
        }
    )

assert all(w <= 25 for w in sectors.values())
expected = {
    "Financials": 25,
    "Industrials": 25,
    "Information Technology": 20,
    "Health Care": 15,
    "Materials": 9,
    "Consumer Discretionary": 6,
}
assert dict(sectors) == expected

sector_shocks = {
    "Financials": -45,
    "Industrials": -40,
    "Information Technology": -50,
    "Health Care": -30,
    "Materials": -50,
    "Consumer Discretionary": -45,
}
shock_return = sum(sectors[s] * shock / 100 for s, shock in sector_shocks.items())
assert round(shock_return, 2) == -42.95

result = {
    "status": "provisional_stock_only_model_not_executable_orders",
    "parents": [
        "v011_2026-09-27_claude",
        "v012_2026-09-27_codex",
        "v013_2026-10-01_codex",
    ],
    "quote_date_et": "2026-09-30",
    "strategic_cash_pct": 0,
    "index_etf_pct": 0,
    "bond_treasury_pct": 0,
    "individual_stocks_pct": 100,
    "sector_weights_pct": dict(sectors),
    "hypothetical_sector_shock_pct": sector_shocks,
    "hypothetical_portfolio_shock_pct": shock_return,
    "shock_interpretation": "deterministic illustrative scenario; no probability or maximum-loss claim",
    "records": records,
}
(HERE / "stock_only_slate.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(f"Validated {len(records)} tickers, {sum(r['weight_pct'] for r in records)}% stocks")
