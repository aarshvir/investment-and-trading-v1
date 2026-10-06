from pathlib import Path
P=Path('review/ready')
(P/'README.md').write_text('''# Current investment decision pack

Reviewed 27 September 2026, Dubai. Start with the [weekly memo](INVESTMENT_DECISION_MEMO.md), [PDF](Investment_Decision_Memo.pdf), or first four tabs of the [dashboard](../Investment_Review.html).

- AMP: conditional new-money BUY at or below $500, up to 2% of capital.
- PAYX: conditional starter BUY at or below $101.80, up to 2%; demonstrated cash recovery required before a subsequent ADD.
- MSFT $500, NVDA $215, ALLE $145 and HIG $120 remain conditional funded levels. All are above their limits at the September 25 close. HIG also needs settlement/capital reconciliation.
- Initial target 19% equity /81% reserve; maximum 25% equity /75% reserve. A constructed 18% tail loss is not a guaranteed maximum.

## Current and historical material

The [dated weekly review](../weekly/2026-09-27/WEEKLY_REVIEW.md) and [34-name journal](../weekly/2026-09-27/ACTION_TABLE.csv) record decisions, changes, exact scope and disagreements with Claude v011. Three audit reports and hashed raw evidence are in that weekly folder. All 29 dashboard tabs remain.

The current model, workbook and 42 scenarios use September 25 stock prices. Company model refresh JSON records unchanged operating assumptions and new event conditions. The five detailed company memoranda are September 26 baseline underwriting; their older price references are historical. Current consolidated prices and weekly decisions govern. WEEKLY_POLICY_V2 remains effective September 26 and was reviewed unchanged September 27.

## Reproduction

From the workspace root, use the configured Python runtime to run, in order:

1. review/ready/build_decision_pack.py — reads company assumptions and weekly_override.json; builds model/workbook/CSVs.
2. review/weekly/2026-09-27/build_weekly_report.py — builds the dated journal, company refresh and current memo from frozen audited inputs.
3. review/ready/build_pdf.py
4. review/ready/publish_dashboard.py — rebuilds the archive and four current tabs together.
5. review/ready/audit_consolidated_financials.py — arithmetic, workbook caches and cost gates.

Do not run the old publish_decision_pack.py for the current weekly memo. One-time patch helpers in the weekly folder document construction history and are not refresh commands. Editable workbook scenario inputs feed both Scenarios and After costs formulas; editing Excel does not change published decisions or JSON. Regenerate and re-audit before a new publication.

Every delivered change requires a new immutable shared release via tools/publish_research_release.py after reading AGENTS.md and RESEARCH_VERSIONING.md. The preserved baseline ZIP and prior v005 release protect the previous state. No trades, daily monitoring, account performance, calibrated profit probabilities or complete consensus history are implied.
''',encoding='utf-8')
f=P/'publish_decision_pack.py';s=f.read_text(encoding='utf-8');s=s.replace("P=Path(__file__).resolve().parent", "P=Path(__file__).resolve().parent\nif (P/'weekly_override.json').exists():\n    raise SystemExit('A weekly release is active. Use the dated build_weekly_report.py in README.md; this historical publisher would overwrite newer decisions.')",1);f.write_text(s,encoding='utf-8')
print('Updated current navigation and guarded obsolete publisher.')
