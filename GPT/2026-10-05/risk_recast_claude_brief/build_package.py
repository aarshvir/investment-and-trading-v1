"""Build a self-contained, immutable-ready handoff package for this dated brief."""

from pathlib import Path
import hashlib
import json
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACKAGE = HERE / "RISK_RECAST_CLAUDE_CODE_2026-10-05.zip"
SOURCES = {
    "GPT/2026-10-05/risk_recast_claude_brief/CLAUDE_CODE_BRIEF.md": HERE / "CLAUDE_CODE_BRIEF.md",
    "GPT/2026-10-05/risk_recast_claude_brief/RELEASE_NOTES.md": HERE / "RELEASE_NOTES.md",
    "GPT/2026-10-05/risk_recast_claude_brief/build_package.py": HERE / "build_package.py",
    "review/weekly/2026-10-05_CLAUDE_CODE_RISK_RECAST_BRIEF.md": HERE / "CLAUDE_CODE_BRIEF.md",
    "parent_completed/v015_package.zip": ROOT / "versions/v015_2026-10-04_codex/package.zip",
    "parent_completed/v011_RELEASE_NOTES.md": ROOT / "versions/v011_2026-09-27_claude/RELEASE_NOTES.md",
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    missing = [str(path) for path in SOURCES.values() if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing required source files: {missing}")
    payloads = {name: path.read_bytes() for name, path in SOURCES.items()}
    manifest = {
        "status": "handoff_only_no_new_portfolio_weights",
        "data_cutoff": "2026-10-02 US close; v015 issuer events through 2026-10-04 14:10 UTC",
        "sources": [
            {"name": name, "bytes": len(data), "sha256": sha256(data)}
            for name, data in sorted(payloads.items())
        ],
    }
    payloads["GPT/2026-10-05/risk_recast_claude_brief/PACKAGE_MANIFEST.json"] = (
        json.dumps(manifest, indent=2) + "\n"
    ).encode("utf-8")
    with zipfile.ZipFile(PACKAGE, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for name, data in sorted(payloads.items()):
            archive.writestr(name, data)
    with zipfile.ZipFile(PACKAGE) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(payloads)
    (HERE / "PACKAGE_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"package": str(PACKAGE), "bytes": PACKAGE.stat().st_size,
                      "sha256": sha256(PACKAGE.read_bytes()), "files": len(payloads)}))


if __name__ == "__main__":
    main()
