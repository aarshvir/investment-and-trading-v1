"""Path/size inventory for scope transparency; does not read or rewrite other workstreams."""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "REPOSITORY_INVENTORY.json"
rows = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    if ".git" in rel.parts or path == OUT:
        continue
    stat = path.stat()
    rows.append({"path": rel.as_posix(), "bytes": stat.st_size})
rows.sort(key=lambda x: x["path"])
counts, sizes = Counter(), Counter()
for row in rows:
    group = row["path"].split("/")[0]
    counts[group] += 1
    sizes[group] += row["bytes"]
OUT.write_text(json.dumps({
    "prepared_utc": datetime.now(timezone.utc).isoformat(),
    "purpose": "Inventory only; no claim that every file received semantic due diligence. Active workstreams may change after this capture.",
    "total_files_excluding_git": len(rows),
    "total_bytes_excluding_git": sum(x["bytes"] for x in rows),
    "top_level": {k: {"files": counts[k], "bytes": sizes[k]} for k in sorted(counts)},
    "files": rows,
}, indent=2), encoding="utf-8")
print(json.dumps({"files": len(rows), "GiB": round(sum(x["bytes"] for x in rows)/2**30, 2)}))
