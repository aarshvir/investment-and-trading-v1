# Research versioning and cross-model handoff

Effective 26 September 2026. User instruction: Claude and Codex should build on each other's work and always preserve successive versions and reports.

## Publication rules

1. Keep working folders separate. `v4/` is the existing Claude workstream; `review/` is the existing Codex workstream. Read both for context, without changing the other workstream's files or treating its conclusions as verified.
2. Completed publications use one shared increasing number, beginning with v005 to avoid colliding with existing v1–v4 names. The number identifies publication order. It does not assert that v005 incorporates unfinished v4 work.
3. Each release has its own directory: `versions/vNNN_YYYY-MM-DD_author/`. It contains the complete original ZIP, convenient report copies, release notes, author, explicit parent IDs, source cutoff, validation scope and SHA-256 hashes. Never overwrite a release. An error correction creates a new release.
4. A release must explain what changed, why, which earlier findings were accepted or rejected, effects on decisions/limits/weights, and unresolved disagreements. Preserve evidence for contrary views. AI agreement and numerical checks do not establish investment accuracy.
5. `versions/index.html`, `versions/INDEX.md`, `versions/catalog.json` and `LATEST_HANDOFF.md` are navigational records and may be updated. The catalog records the latest publication per author and the most recent completed publication. A newer release does not automatically override the investment policy: its notes must state whether it supersedes, supplements or challenges the prior recommendation.
6. Before updating convenience files such as `review/Investment_Review.html`, preserve the prior delivered package. After validation, publish the new package, then point readers to it. The first four current dashboard tabs may evolve; preserved historical tabs and release archives must remain available.
7. Every weekly review gets a new numbered release, including a no-trade report. Record a genuine data cutoff and a no-change explanation; never copy stale prices and label them fresh. Minor unpublished edits can remain drafts until a coherent version is ready.
8. Claude and Codex use the same handoff and release register. External chats require the user or an authorized integration to provide the files; this mechanism does not imply automatic chat-to-chat synchronization.

## Publishing

Create a complete ZIP with the reports, models, dashboard, source ledger and necessary supporting files. Keep it under the workspace. Create a release-notes Markdown file covering the changes and validation. Then run the publisher with:

```
python tools/publish_research_release.py --author Codex --package PATH_TO_PACKAGE.zip --notes PATH_TO_RELEASE_NOTES.md --summary "Describe the delivered change" --parents v005_2026-09-26_codex --data-cutoff "State the actual cutoff and exceptions"
```

Use `--author Claude` for a Claude release. The publisher reserves the next number under an exclusive lock, refuses to overwrite an existing release, copies the full package, extracts useful reports for easy reading, verifies archive hashes and updates the index. The complete ZIP is authoritative for full dashboard/source reconstruction. Convenient report copies are clearly identified and are not a substitute for the full archive.

The publication lock prevents cooperating local runs from choosing the same version. OneDrive is not a distributed transaction system: avoid simultaneous publishing from separate devices. If a run is interrupted, inspect the lock and incomplete release before recovery; never erase an existing completed release to retry.

## Existing history

- Original Claude v3: original handoff and bundle, preserved under their existing names.
- Initial Codex audit and deeper data audit: existing ZIPs retained and listed as historical references.
- Claude v4: observed working branch with its own state/conventions/dashboard. Its status is not inferred to be complete from the directory name.
- Codex v005: snapshot of the completed investment decision pack delivered before this versioning setup. Its investment findings did not use or certify Claude's unfinished v4 outputs.

No financial recommendation, allocation or entry limit changes merely because this versioning system was installed.
