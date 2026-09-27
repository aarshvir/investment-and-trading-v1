# DA15 Fact-Check — Loop-8 Must-Fix Targeted Sweep

**As of:** 2026-09-27
**Scope:** SO, MA, STE, USB, EXC, BALL, DOV — verify the dossier's latest-reported-quarter revenue, GAAP net income, diluted EPS (GAAP and adjusted where stated), period label/end date, and prior-year comparative against each company's latest 8-K Ex-99.1 earnings release / 10-Q on SEC EDGAR. Target defect pattern: a "latest quarter" net income figure that is actually the prior-year comparative column.

## Summary

| Status | Count |
|---|---|
| PASS | 12 |
| MINOR | 2 |
| FAIL | 0 |
| UNVERIFIABLE | 0 |
| **Total facts** | **14** |

**No instances of the loop-8 swap bug (prior-year quarter mislabeled as the latest quarter) were found in any of the seven dossiers.** All latest-quarter revenue, GAAP net income, and diluted EPS figures cross-checked to the cent/million against the primary-source earnings release or 10-Q. Fiscal-year labeling for STE (fiscal year ending 31-Mar) is correctly identified as Q1 FY2027, not miscast as a calendar quarter.

Two MINOR findings, both in EXC.md: the dossier's Q2 2026 revenue and net income cells are marked "n/a" pending a bulk-XBRL data lag, but the same Ex-99.1 release already cited by the dossier contains the exact figures ($5,967M revenue, $396M net income) — a completeness gap, not a wrong value.

## Facts by ticker

### SO
- Q2 2026 revenue $6.98bn, GAAP EPS $1.03 — **PASS** (8-K Ex-99.1, accession 0000092122-26-000056; source shows net income $1,174M as reported, EPS $1.03 vs $0.80 Q2 2025)
- Adjusted EPS $1.13 vs $0.92 — **PASS**

### MA
- 2Q26 net revenue $9,277M, op. income $5,587M, GAAP diluted EPS $4.97, net income ~$4.4bn — **PASS** (8-K Ex-99.1, accession 0001141391-26-000081)
- 2Q25 comparative ($8,133M revenue, $4.07 EPS, $3.7bn net income) correctly in its own row — **PASS**

### STE
- Q1 FY2027 (ended 2026-06-30) revenue $1,492.7m, GAAP diluted EPS $2.04, adjusted EPS $2.59 — **PASS** (8-K Ex-99.1, accession 0001628280-26-053412; net income $200.1M)
- Q1 FY2026 comparative ($1,391.1m revenue, $1.79 EPS, $177.4M net income) correctly in prior-year row — **PASS**

### USB
- Q2 2026 net revenue $7,712M, net income $2,177M, diluted EPS $1.35 — **PASS** (8-K Ex-99.1, accession 0000036104-26-000039)
- Q2 2025 comparative ($1,815M net income, $1.11 EPS) correctly in its own row — **PASS**

### EXC
- Q2 2026 GAAP diluted EPS $0.39, adjusted operating EPS $0.43 — **PASS** (8-K Ex-99.1, accession 0001109357-26-000077)
- Q2 2026 revenue/net income marked "n/a" in dossier — **MINOR**: source shows exact figures $5,967M revenue / $396M net income, available at write time; should be filled in.
- Q2 2025 comparative ($5,427M revenue, $391M net income, $0.39 EPS) correctly in its own row despite EPS coincidentally equal to Q2 2026 — **PASS**, confirms no swap.

### BALL
- Q2'26 net sales $4.00bn, GAAP diluted EPS $0.83, comparable EPS $1.03 — **PASS** (8-K Ex-99.1, accession 0001104659-26-090074)
- Q2'25 comparative ($3.34bn sales, $0.76 GAAP EPS, $0.90 comparable EPS) correctly in its own row — **PASS**

### DOV
- Q2 2026 revenue $2,190.0m, net income (GAAP, total) $312.2m, diluted EPS $2.30, adjusted EPS $2.74 — **PASS** (8-K Ex-99.1, accession 0000029905-26-000026; note: dossier correctly uses total "net earnings" $312,246K/$2.30, not the very similar "earnings from continuing operations" $312,545K/$2.31 — no swap, but a basis distinction worth flagging for future checks)
- Q1 2026 revenue $2,053.6m, net income $238.4m, diluted EPS $1.75 correctly in its own (earlier) column — **PASS**

## FAILs

None. No FAIL findings in this sweep.

## Notes
- Pre-existing DA11 Correction sections in STE.md (Healthcare segment revenue $1,048.3m not $1,051.4m) and BALL.md (FY2025 comparable EBITDA $2,041m not $2,044m) were reviewed; both are immaterial and unrelated to the latest-quarter figures checked here, and were left unedited per the do-not-edit-dossiers instruction.
- No dossier or other file was modified. Outputs written only to `v4\outputs\da15_factcheck.json` and `v4\outputs\da15_factcheck.md`.
