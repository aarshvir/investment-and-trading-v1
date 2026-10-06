"""Lock a prospective 90-name quote/forecast register without inventing coverage."""
import csv
import hashlib
import json
import math
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
V011 = ROOT / "versions/v011_2026-09-27_claude/package.zip"
with zipfile.ZipFile(V011) as z:
    raw = z.read("v4/outputs/lead_portfolio_build.json")
    parent = json.loads(raw)
candidates = {x["t"]: x for x in parent["candidates"]}
selected = set(parent["selected"])
quotes = list(csv.DictReader((HERE / "MARKET_RECONCILIATION.csv").open(newline="", encoding="utf-8")))
repriced = json.loads((HERE / "SCENARIO_REPRICE.json").read_text(encoding="utf-8"))
modeled = {x["ticker"]: x for x in repriced["results"]}
now = datetime.now(timezone.utc).isoformat()
rows = []
for q in quotes:
    ticker = q["ticker"]
    c = candidates.get(ticker)
    m = modeled.get(ticker)
    case = next((x for x in m["cases"] if x["case"] == "base"), None) if m else None
    old_base = c.get("base") if c else None
    old_base = old_base if isinstance(old_base, (int, float)) and math.isfinite(old_base) else None
    rows.append({
        "locked_utc": now, "asof_price_session_et": "2026-09-30", "ticker": ticker,
        "price_usd": q["yahoo_regular_close"], "price_identity": q["quote_status"],
        "price_raw_sha256": q["yahoo_raw_sha256"], "corroborating_raw_sha256": q["cboe_raw_sha256"],
        "v011_in_candidate_file": bool(c), "v011_selected_shadow": ticker in selected,
        "v011_original_rank": c.get("rank") if c else None,
        "v011_eligible_at_sep25": c.get("eligible") if c else None,
        "v011_base_scenario_archived_not_comparable": old_base,
        "v012_standardized_model": bool(m),
        "v012_bear_irr_repriced": next((x["irr_after_30pct_withholding_25bp_entry_exit_at_sep30"] for x in m["cases"] if x["case"] == "bear"), None) if m else None,
        "v012_base_irr_repriced": case["irr_after_30pct_withholding_25bp_entry_exit_at_sep30"] if case else None,
        "v012_bull_irr_repriced": next((x["irr_after_30pct_withholding_25bp_entry_exit_at_sep30"] for x in m["cases"] if x["case"] == "bull"), None) if m else None,
        "scenario_asof": "v012 prior assumptions; no September 30 forecast refresh" if m else "no cross-name comparable forecast",
        "new_money_decision": "WAIT_REUNDERWRITE" if ticker in ("AMP", "PAYX") else ("WAIT_PRICE_OR_EVIDENCE" if m else ("INDEX_EXPOSURE_ONLY" if ticker == "SPY" else "RESEARCH_ONLY")),
        "decision_reason": ("Published buy ceiling suspended: base return depends on exit P/E recovery and a modest miss erases the 12% hurdle" if ticker in ("AMP", "PAYX") else ("Existing limit or decision-critical evidence gate remains; this is not a funded allocation" if m else ("Benchmark proxy for the 25% broad index sleeve, not necessarily the chosen fund" if ticker == "SPY" else "A quote and archived scenario do not establish a validated after-cost expected return"))),
        "benchmark": "SPY dated close; index planning return is an assumption, not an alpha estimate",
        "next_measurement": "2026-10-30, 2026-12-29, 2027-09-30 completed sessions, adjusted for corporate actions and dividends",
    })
path = HERE / "PREDICTION_LEDGER.csv"
with path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(rows[0]))
    w.writeheader(); w.writerows(rows)
(HERE / "PREDICTION_LEDGER_MANIFEST.json").write_text(json.dumps({
    "locked_utc": now, "ledger_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    "v011_package_sha256": hashlib.sha256(V011.read_bytes()).hexdigest(),
    "v011_candidate_member_sha256": hashlib.sha256(raw).hexdigest(),
    "v012_model_sha256": repriced["source_model_sha256"],
    "count": len(rows), "standardized_inherited_scenarios": sum(bool(r["v012_standardized_model"]) for r in rows),
    "rule": "Historical forecasts and decisions remain frozen. Fill actual outcomes only in a future separately versioned file; never overwrite this snapshot.",
}, indent=2), encoding="utf-8")
assert len(rows) == 90
print(json.dumps({"rows": len(rows), "v011_selected": sum(r["v011_selected_shadow"] for r in rows), "v012_models": sum(r["v012_standardized_model"] for r in rows)}))
