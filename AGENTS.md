# Shared investment research workspace

Read `RESEARCH_VERSIONING.md`, `LATEST_HANDOFF.md` and `versions/catalog.json` before starting substantive research or publication. The user explicitly requires Claude and Codex to build on prior work while retaining every version and report.

- Published releases under `versions/vNNN_*` are immutable. Never overwrite, rename or delete one. Publish corrections as a new version with a change log.
- Existing v3 source files, historical packages and Claude's `v4/` work are preserved. Do not edit another active workstream's files. Coordinate through the shared handoff and release catalog; inherited claims still require validation.
- Before changing the current report/model/dashboard, ensure its delivered state has a complete versioned archive. Keep current convenience paths, but publish a new numbered release for every delivered revision, weekly report or material correction.
- Read the latest completed releases from both authors. Record the exact parent IDs, what was adopted, changed or rejected, and the evidence. A higher version number means newer publication, not proven superiority or automatic investment approval.
- Use `tools/publish_research_release.py` to reserve the next version, snapshot the complete package, record hashes and update the shared index. Never modify immutable release files to make old links point to new findings.
- Keep data cutoff, preparation time, author, release status and validation scope explicit. Drafts and competing analyses must not silently replace completed decisions. No trading or external publication is authorized by these versioning rules.
