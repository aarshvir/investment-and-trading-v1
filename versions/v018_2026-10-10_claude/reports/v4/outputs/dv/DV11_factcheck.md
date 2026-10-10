# DV11 fact-check (as of 2026-10-09)

Scope: CRL, CRM, CRWD, CSCO, CSGP, CSX, CTAS, CTSH, CTVA, CVNA. 66 facts checked against SEC filings: PASS 30, MINOR 15, FAIL 20, UNVERIFIABLE 1. All ten dossiers carry a `## Correction (verification DV11 ...)` section (eight from the 2026-10-06 pass, CTSH and CVNA added 2026-10-09). The 2026-10-06 pass for the first eight tickers was re-affirmed from their correction sections, with spot re-checks of CSCO debt, CRM debt, CTAS and CRWD SBC and CSGP cash against XBRL.

## Verdict changes
- CSGP: INCLUDE-SMALL -> WATCH (SBC treated as a cost moves implied growth to 11.5-17% vs a 10% base; Zonda cash outflow; July revenue cut). F41 summary updated.

## implied_vs_base changes
- CSGP in_line -> above. No other implied_vs_base call changed; CRL, CRWD, CSCO, CSX, CTAS and CVNA stay above (more strongly), CRM, CTSH and CTVA stay below.

## Main FAILs
CRL, CRM, CRWD, CSCO, CSX, CTAS, CTSH, CVNA: reverse-DCF discount rate not tied to the 5.17% Treasury plus a stated equity risk premium and/or SBC added back (the restated implied growth is higher in every case except CTSH, which is about 0.5 point less negative). CSCO: debt and FY25 comparatives. CSGP: FY2025 revenue, guidance chronology, debt description, missed Zonda purchase. CRM: operating margin and debt multiple. CTAS: organic-growth run. CTVA: 31 Dec 2025 net cash.

## CTSH and CVNA (checked 2026-10-09)
CTSH: all table cells, four guidance releases and the balance sheet reproduce; one method FAIL (SBC added back, rate unstated; implied -2.7% vs -3.2%, below base either way) and three MINOR items (Q1-26 margin cause is a Q1-25 property-sale gain, Syntel is a favorable $298M unrecorded judgment under appeal, Financial Services growth includes pass-through product sales). INCLUDE-SMALL stands.
CVNA: financial table, guidance, balance sheet, loan-sale, related-party and refinancing facts reproduce. One FAIL: r = 10% has no basis; with 5.17% + Blume beta 2.67 x 4.14% = 16.2% the price implies 34% a year (19.1% at a beta of 1) against a 19.5% base, and the base case is worth $23.6 a share rather than $63. WATCH stands; implied_vs_base stays above.

## Notes
Unverifiable items (consensus, price targets, earnings dates, short-seller and felony items) are listed per company in the JSON. The F-summary files were edited for CTSH (F127) and CVNA (F169) as text-only reconciliation notes.
