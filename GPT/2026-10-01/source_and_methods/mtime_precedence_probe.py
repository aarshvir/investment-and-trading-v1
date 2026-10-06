"""Read-only inventory of verdict precedence inputs in the archived lead builder."""
from __future__ import annotations

import glob
import hashlib
import json
import os
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BUILDER = ROOT / "v4/code/lead_build_portfolio.py"
VIEWS = ROOT / "v4/code/lead_views.py"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unpack(path):
    try:
        d = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return []
    items = d.items() if isinstance(d, dict) else []
    if isinstance(d, dict) and "ticker" in d and "verdict" in d:
        items = [(d["ticker"], d)]
    for key in ("tickers", "companies", "results", "summaries"):
        if isinstance(d, dict) and isinstance(d.get(key), dict):
            items = d[key].items()
        elif isinstance(d, dict) and isinstance(d.get(key), list):
            items = [(x.get("ticker"), x) for x in d[key] if isinstance(x, dict)]
    if isinstance(d, list):
        items = [(x.get("ticker"), x) for x in d if isinstance(x, dict)]
    return [(str(t).upper(), str(v["verdict"]).upper()) for t, v in items
            if isinstance(v, dict) and "verdict" in v and t]


def main():
    patterns = [str(ROOT / "v4/outputs/f*_summary.json"),
                r"C:\Users\user\eqv4\cache\f*\*\summary.json"]
    paths = sorted(set(sum((glob.glob(x) for x in patterns), [])), key=os.path.getmtime)
    rows = defaultdict(list)
    for path in paths:
        t = datetime.fromtimestamp(os.path.getmtime(path), timezone.utc).isoformat()
        for ticker, verdict in unpack(path):
            rows[ticker].append({"verdict": verdict, "path": path, "mtime_utc": t, "sha256": sha(Path(path))})
    duplicated = {k: v for k, v in rows.items() if len(v) > 1}
    conflict = {k: v for k, v in duplicated.items() if len({x["verdict"] for x in v}) > 1}
    output = {
        "scope": "Inventory of currently reachable summary inputs; filesystem timestamps can change on copy or restore",
        "builder_sha256": sha(BUILDER),
        "views_sha256": sha(VIEWS),
        "summary_files": len(paths),
        "tickers_with_verdict": len(rows),
        "tickers_with_multiple_verdict_records": len(duplicated),
        "tickers_with_conflicting_verdict_text": len(conflict),
        "conflicts": conflict,
    }
    (OUT / "mtime_precedence_probe.json").write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in output.items() if k != "conflicts"}, indent=2))
    print("conflict tickers:", sorted(conflict))


if __name__ == "__main__":
    main()
