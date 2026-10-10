# DVH5 verification, 6 Oct 2026

Scope: PCG, F, LDOS, FIS. Research only; not personal advice. Full table: `DVH5_factcheck.json` (55 facts: 34 PASS, 9 FAIL, 4 UNVERIFIABLE, 8 MINOR).

Sources: SEC EDGAR 10-Q, 10-K, 8-K Ex-99 releases and XBRL company facts (accessions in each fact). Price, d4 snapshot values and call-transcript statements are labelled; they are not on EDGAR.

| Ticker | Result |
|---|---|
| PCG | Quarterly figures, guidance quotes, debt (mechanical flags are false positives), liquidity and wildfire items pass. **FAIL:** reverse DCF starts from core EPS $1.65 and an untied 9.5% Ke; from a GAAP-adjusted $1.43 the price implies 5.6-7.6% vs base 7%. **implied_vs_base: below -> in line.** |
| F | Every quarter, guidance quote, balance-sheet line and 8-K fact passes. **FAIL:** adjusted FCF excludes about $2.15B (FY25) / $2.67B (H1 26) of pension, restructuring and "other, net" cash and SBC; strict basis implies 4.3%/yr (11% on $2.4B) vs base 4%. **implied_vs_base: below -> in line.** TTM loss is $7.4B; special items $17.4B total. New 2 Oct 8-K: F-150 supplier issue, within guide. |
| LDOS | **FAILS:** leverage 2.2x (from 1.5x), not 2.45x (from 2.0x); the SEC FCPA red flag is not in the 10-K or 10-Q, which disclose a live DOJ Antitrust criminal grand jury probe; Analogic JV (41.5% retained, closed 5 Oct 2026) omitted; TTM OCF $2,300M not $1,147M and FY26 EPS guide is +3%, not +7% (base scenario +12.4% -> about +9.2%); wrong period for the Q4 revenue decline. Implied still below base. |
| FIS | Quarterly EPS, three guidance steps, debt ($21.2bn incl. $4.2bn short-term borrowings; the XBRL flag is a false positive) and balance sheet pass. **FAIL (no direction change):** levered FCF set against EV with SBC added back; unlevered implied growth about 1.5%, not 2.6-2.7%. Debt rose 62%, not "doubled". |

Verdict changes: none (all four stay INCLUDE-SMALL). implied_vs_base changed for PCG and F (below -> in line). Summary files updated: `F124_summary.json` (PCG), `F137_summary.json` (F), `F25_summary.json` (LDOS), `F34_summary.json` (FIS, reconciliation text). Each dossier has inline corrections and a `## Correction (verification DVH5, 2026-10-06)` section.

Limits: earnings dates, 3.5x FIS gross leverage, insider and Form 4 items, and the 4 Aug 2026 PCG 8-K substance were not verified. Reverse-DCF recomputations use the dossiers' own discount rates and terminal growth; SES revenue for LDOS is not disclosed in the filings read.
