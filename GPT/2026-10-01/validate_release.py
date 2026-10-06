"""Independent arithmetic, lineage, schema, and preservation gates for GPT release."""
import csv
import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
checks = []
def check(name, predicate, detail=""):
    result = bool(predicate)
    checks.append({"check": name, "pass": result, "detail": detail})
    if not result:
        raise AssertionError(name + ": " + detail)
def read(name): return json.loads((HERE / name).read_text(encoding="utf-8"))
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

catalog = json.loads((ROOT / "versions/catalog.json").read_text(encoding="utf-8"))
parents = read("PARENT_RELEASE_LINKS.json")
for p in parents["parents"]:
    path = ROOT / p["archive"]
    check("immutable parent hash " + p["id"], sha(path) == p["sha256_in_shared_catalog"])
    found = next((x for x in catalog["releases"] if x["id"] == p["id"]), None)
    check("catalog parent identity " + p["id"], found is not None and found["package_sha256"] == p["sha256_in_shared_catalog"])
check("user audit input hash", sha(HERE / "INPUT_CHATGPT_AUDIT.txt") == parents["user_audit_input"]["sha256"])

market = list(csv.DictReader((HERE / "MARKET_RECONCILIATION.csv").open(newline="", encoding="utf-8")))
ledger = list(csv.DictReader((HERE / "PREDICTION_LEDGER.csv").open(newline="", encoding="utf-8")))
shadow = list(csv.DictReader((HERE / "V011_SHADOW_REVIEW.csv").open(newline="", encoding="utf-8")))
check("market 90 unique", len(market) == 90 and len({x["ticker"] for x in market}) == 90)
check("ledger 90 same identities", len(ledger) == 90 and {x["ticker"] for x in ledger} == {x["ticker"] for x in market})
check("shadow 20 unique", len(shadow) == 20 and len({x["ticker"] for x in shadow}) == 20)
check("dual source 32", sum(x["cboe_close"] != "" for x in market) == 32)
check("all dual feed gaps below .1pct", max(float(x["relative_close_gap_pct"]) for x in market if x["relative_close_gap_pct"]) < .1)
check("all dates USD", all(x["date_et"] == "2026-09-30" and x["currency"] == "USD" for x in market))
check("no unmodeled numeric scenarios", sum(x["v012_standardized_model"] == "True" for x in ledger) == 14 and all(x["v012_base_irr_repriced"] == "" for x in ledger if x["v012_standardized_model"] != "True"))

scenarios = read("SCENARIO_REPRICE.json")
check("14 scenario cases", len(scenarios["results"]) == 14 and all({x["case"] for x in r["cases"]} == {"bear", "base", "bull"} for r in scenarios["results"]))
positions = {x["ticker"]: x for x in scenarios["results"]}
check("AMP/PAYX prices and wait decisions", math.isclose(positions["AMP"]["close_sep30"], 492.35) and math.isclose(positions["PAYX"]["close_sep30"], 98.5) and all(next(x for x in ledger if x["ticker"] == t)["new_money_decision"] == "WAIT_REUNDERWRITE" for t in ("AMP", "PAYX")))
alloc = read("PORTFOLIO_MAP.json")
selected = next(x for x in alloc["allocations"] if x["name"] == alloc["recommended_allocation_id"])
check("selected 25/0/75", selected["weights"]["index"] == .25 and selected["weights"]["direct"] == {} and selected["weights"]["reserve"] == .75)
check("selected risk arithmetic", math.isclose(selected["stress"]["severe_correlated_pct"], -13.25) and math.isclose(selected["stress"]["tail_constructed_pct"], -16.5))

method = read("source_and_methods/methodology_v2_validation.json")
check("method validation document", isinstance(method, dict) and len(method) > 0)
bundled = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe"
test_python = bundled if bundled.is_file() else Path(sys.executable)
test = subprocess.run([str(test_python), str(HERE / "source_and_methods/test_methodology_v2.py")], cwd=ROOT, capture_output=True, text=True)
check("method module tests", test.returncode == 0, test.stdout[-1500:] + test.stderr[-1500:])
report = {"status": "passed", "checks": checks, "note": "Arithmetic, lineage and bounded evidence gates; not a proof of forecast accuracy, future returns or maximum loss."}
(HERE / "VALIDATION.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps({"passed": len(checks), "method_test_output": (test.stdout + test.stderr)[-350:]}))
