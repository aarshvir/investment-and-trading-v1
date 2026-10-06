# DA16 Fact-Check — Latest-Quarter Figures (ADP, CAH, BR, PPG, PGR, AXP, HBAN)

**As of:** 2026-09-27 | **Scope:** Verify each dossier's latest reported quarter (revenue, GAAP net income,
diluted EPS GAAP/adjusted, period label) against SEC EDGAR primary sources (8-K Ex-99.1 earnings releases,
10-Q/10-K, XBRL companyfacts), and confirm the prior-year comparative was not swapped into the "latest
quarter" cell. This is a data-quality audit, not an investment conclusion.

## Summary of status counts

| Status | Count |
|---|---|
| PASS | 21 |
| MINOR | 1 |
| FAIL | 1 |
| UNVERIFIABLE | 4 |
| **Total facts checked** | **27** |

## The one FAIL

**ADP — Q4 FY26 net income cell is wrong (the exact bug the loop-8 audit was looking for).**

- **Dossier location:** `dossiers/ADP.md` §4, table row "Q4 FY26 (Jun-26)", Net income column, which reads
  `~$1,013–1,062M range (qtr)`.
- **Source:** ADP 8-K Ex-99.1, Q4/FY2026 earnings release, filed 2026-07-29, accession
  0000008670-26-000025; cross-checked against SEC XBRL companyfacts (CIK 0000008670): FY26 full-year net
  earnings $4,413.5M minus 9-month YTD (Jul-25–Mar-26) net earnings $3,434.9M.
- **Correct value:** **Q4 FY26 GAAP net earnings = $978.6M** (+7% YoY vs $910.6M in Q4 FY25) — stated
  verbatim in ADP's own release ("Net earnings increased 7% to $1.0 billion").
- **What happened:** the "$1,013–1,062M" range shown for Q4 FY26 is not a real figure — it is the Q1 FY26
  ($1,013.0M) and Q2 FY26 ($1,062.0M) net-income values, already shown two rows above in the same table,
  re-pasted into the Q4 cell instead of the correct $978.6M. The FY26 full-year total ($4,413.5M) and the
  Q4 diluted EPS figures ($2.45 GAAP / $2.64 adjusted) in the same row are both correct and are internally
  consistent with the corrected $978.6M quarterly figure (978.6 + 1,013.0 + 1,062.0 + 1,359.8 = $4,413.4M).
  Verdict impact: none (the dossier's INCLUDE thesis does not rest on this specific cell), but the row should
  be corrected.

## Everything else checked out

- **CAH:** Q4 FY26 revenue ($63.7bn, +6%) and diluted EPS ($1.70, +70%) match the 8-K exactly; Q3 FY26 EPS
  decline (-20% to $1.69, tied to the $184M Navista/ION goodwill impairment) confirmed verbatim; FY26 net
  income total ($1,714M) confirmed. No quarterly net-income column exists in this dossier to mis-swap.
- **BR:** the dossier's "derived" Q4 FY26 figures (10-K annual total minus 10-Q nine-month YTD, since
  Broadridge doesn't report a discrete Q4 income statement) are arithmetically exact: net income $398.1M,
  matching FY26 total $1,124.3M minus 9-month YTD $726.2M to the dollar. Revenue and EPS also confirmed.
- **PPG:** Q2 2026 net sales ($4,495M, +7%) and GAAP/adjusted EPS ($1.96 / $2.23) match the 8-K exactly.
  Gap (not an error): the dossier never states a quarterly net-income figure for PPG; primary-source net
  income was actually **$439M, down 2% YoY** despite revenue growth — worth adding to the dossier's
  earnings-quality section, but not a mis-stated fact since none was asserted.
- **PGR:** Q2 2026 net premiums earned ($21,573M), net income ($3,311M) and diluted EPS ($5.67) all match
  XBRL exactly; the four-quarter sequence (3Q25→2Q26) is correctly ordered with no shift.
- **AXP:** Q2 2026 revenue ($19.637bn), net income ($3.110bn) and diluted EPS ($4.53) match XBRL exactly; the
  Q2 2025 comparator used for YoY math is independently confirmed correct.
- **HBAN:** Q2 2026 net income ($727M) and diluted EPS ($0.33 GAAP / $0.39 adjusted) match the 8-K's own
  five-quarter summary table exactly, as does the full run of four prior quarters shown for comparison. Gap
  (not an error): the dossier states no single revenue figure for HBAN's latest quarter, so there's nothing
  to verify there.

## Period labels / non-calendar fiscal years

All seven dossiers correctly identify their most recent reported quarter and, where relevant, flag a
non-calendar fiscal year end (ADP, CAH, BR all FYE 30-Jun; PPG, PGR, AXP, HBAN all calendar-year). No
period-label or fiscal-year mislabeling was found anywhere in this sweep.

## Method note

Companyconcept/companyfacts XBRL pulls for HBAN and PPG initially returned data only through Q1 2026 despite
later 10-Qs/8-Ks being on file (a caching/lag artifact of the SEC API, not a filing gap) — resolved by
pulling the primary 8-K Ex-99.1 exhibits directly for the affected quarters. All source values in the
accompanying JSON are cited to the specific accession number used.
