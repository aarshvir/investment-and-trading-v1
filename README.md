# Investment and Trading v1

Private archive of the complete shared investment research workspace: Claude and Codex research, source bundles, datasets, dashboards, scripts, audit reports and versioned releases.

## Start here

- [Latest shared handoff](LATEST_HANDOFF.md)
- [Version library](versions/INDEX.md)
- [Version catalog](versions/catalog.json)
- [Version-preservation rules](RESEARCH_VERSIONING.md)
- [Codex decision pack](review/ready/README.md)
- [Claude research state](v4/STATE.md)

The research releases retain their existing numbers and authors. The repository name's “v1” denotes this GitHub archive; it does not reset the research history. Different releases may disagree. Read their dates, assumptions, source evidence and release notes before using their conclusions.

## Folder contents

| Folder | Contents |
|---|---|
| `equity_project/` | Original research, scripts and data |
| `source_bundle/` | Preserved original source bundle |
| `review/` | Codex audits, decisions, models, evidence and dashboard |
| `v4/` | Claude research, datasets, dossiers, audits, dashboard and release packages |
| `versions/` | Preserved numbered publications and shared version index |
| `tools/` | Publication and continuity tools |
| `.claude/` | Workspace launch configuration |

Root-level handoffs and ZIP archives are also included. Published releases are historical snapshots; do not overwrite them. New research should use a new numbered release and a new Git commit.

## Download the full workspace

Large archives, datasets, PDFs and workbooks use **Git LFS** at their original paths. To obtain the complete file contents, install Git LFS and clone:

```sh
git lfs install
git clone https://github.com/aarshvir/investment-and-trading-v1.git
cd investment-and-trading-v1
git lfs pull
```

A browser ZIP download may contain LFS pointers rather than all large-file contents; a Git LFS clone is the reliable full-workspace download. Original text bytes are preserved without automatic line-ending conversion so archived hashes remain meaningful.

Open the downloaded HTML dashboards locally. GitHub's file viewer shows HTML source and does not execute the interactive dashboards. The repository is private; no public website or GitHub Pages deployment is configured.

This is research and its audit trail. Uploading it does not validate every historical claim, change an investment recommendation or authorize trades. Credentials are excluded from version control.
