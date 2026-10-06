"""Build a complete GPT-only research ZIP with publisher-friendly report copies."""
import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PACKAGE = HERE / "GPT_Investment_Release_2026-10-01.zip"
MANIFEST = HERE / "PACKAGE_MANIFEST.json"

files = sorted(p for p in HERE.rglob("*") if p.is_file()
               and p not in (PACKAGE, MANIFEST)
               and "__pycache__" not in p.parts and p.suffix != ".pyc")
entries = []
for p in files:
    rel = p.relative_to(HERE).as_posix()
    entries.append({"file": rel, "bytes": p.stat().st_size,
                    "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
MANIFEST.write_text(json.dumps({
    "prepared_utc": datetime.now(timezone.utc).isoformat(),
    "author": "Codex", "parents": ["v012_2026-09-27_codex", "v011_2026-09-27_claude"],
    "data_cutoff": "2026-09-30 completed US session; issuer/SEC event checks through 2026-09-30 20:30 UTC",
    "file_count_excluding_this_manifest": len(entries),
    "files": entries,
}, indent=2), encoding="utf-8")
with zipfile.ZipFile(PACKAGE, "w", zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
    for p in files + [MANIFEST]:
        rel = p.relative_to(HERE).as_posix()
        z.write(p, f"GPT/2026-10-01/{rel}")
        # Shared publisher makes easy-to-open copies for reports. These ZIP
        # entries are aliases of the GPT files, not edits to the review tree.
        if p.suffix.lower() in (".md", ".csv", ".json") and "raw_market" not in p.parts and p.stat().st_size < 5_000_000:
            z.write(p, f"review/weekly/2026-10-01/{rel}")
with zipfile.ZipFile(PACKAGE) as z:
    bad = z.testzip()
    if bad:
        raise RuntimeError(f"ZIP integrity failure: {bad}")
print(json.dumps({"package": str(PACKAGE.relative_to(ROOT)).replace("\\", "/"),
                  "bytes": PACKAGE.stat().st_size, "unique_source_files": len(entries)+1,
                  "sha256": hashlib.sha256(PACKAGE.read_bytes()).hexdigest()}))
