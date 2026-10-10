# DV38 fact-check (2026-10-08)

Scope: SRE, STLD, STT, STX, STZ, SW, SWKS, SYK, SYY, T. 66 facts checked against SEC EDGAR (10-Q/10-K, 8-K Ex-99.1, companyfacts): 44 PASS, 11 MINOR, 11 FAIL, 0 UNVERIFIABLE (a few sub-items marked in notes). Corrections appended to 7 dossiers (SRE, STLD, STT, STX, STZ, SW, SWKS); SYK, SYY and T had no FAIL.

## Verdict change
- **SRE: INCLUDE-SMALL -> WATCH.** The reverse-DCF used a stale 4.16% risk-free rate (10y Treasury is 5.17% on 25 Sep 2026) and treated NTM EPS as cash for a utility holdco with deeply negative FCF. On a dividend basis at Ke 8.0% the $77.93 price needs about 9.3%/yr dividend growth for 5 years (top of the 7-9% guide); implied_vs_base is above, so the INCLUDE-type test fails. F33 summary updated (verdict, valuation view, restated scenarios 0% / +7.6% / +13.4%).

## FAILs by ticker
- **SRE** valuation method (above). Minor: NCI composition claim unsupported.
- **STLD** second Columbus CASH line is guided to start producing qualification material before end-2026 (17 Sep 2026 release), not 2027; kill criterion 4 and F48 summary reworded. Verdict WATCH unchanged.
- **STT** Q1-26 EPS growth is +22% (Q1-25 EPS $2.04), not +14.7%; valuation used a trailing-P/E band instead of P/TBV-ROTCE. Corrected: TBV about $57.5/share, P/TBV 3.15x, implied ROTCE about 24.5% vs company mid-20s target; implied_vs_base in_line (borderline). Guidance figures verified in primary Ex-99.3. INCLUDE-SMALL kept.
- **STX** reverse-DCF WACC 9-10% inconsistent with 5.17% risk-free and beta 2.09; at about 12% the price needs 28-29%/yr FCF growth for 10 years (not 21-24%). WATCH reinforced; implied_vs_base above added to F31.
- **STZ** all quarterly fiscal labels one year too high (quarter to 31 May 2026 is Q1 FY2027, not FY2028) and the quarter to 28 Feb 2026 omitted; "long-term debt" trend hid that total debt is $10.53bn and barely moved (reclassification to current maturities). Amounts tie. INCLUDE-SMALL kept. Post-cutoff Q2 FY27 (6 Oct): guidance reaffirmed, depletions -0.6%.
- **SW** net debt omitted $931m current debt (net debt $13.49bn, 2.7x, EV $37.8bn); reverse-DCF divided levered FCF into EV. Corrected implied growth about 4.5% vs about 5% base: implied_vs_base above -> in_line. WATCH kept (guidance cut, margin compression, thin FCF conversion). F78 updated.
- **SWKS** reverse-DCF 9.5% rate too low for beta 1.5 (CAPM about 10.8%) and EPS used as the cash proxy; corrected implied about 10.6% vs 6.6% base, WATCH reinforced. Post-cutoff: Qorvo merger closed 5 Oct 2026.

## Clean
- **SYK** all load-bearing figures tie (Q2-26, guidance, debt incl. current maturities, TTM FCF, scenarios). Minor: TTM dividends mislabelled, reverse DCF pairs levered FCF with EV (corrected 4.3-4.6% vs 4.8%, conclusion unchanged). Post-cutoff: CEO succession announced 6 Oct 2026.
- **SYY** every figure and valuation step reproduces; mechanical crosstie flags were pro forma and JRD entity lines correctly labelled.
- **T** every figure ties to the Q2-26 release and 10-Q; scenario returns reproduce within 1 point. Post-period: about $8-9bn of new notes issued in August (pre-funding EchoStar), deal still unclosed per EDGAR.

## Method notes
Rate check used 10y UST 5.17% plus either the dossier's stated ERP or V1's 4.14% with Blume beta. Banks tested on P/TBV-ROTCE; utilities on dividends; SBC treated as a cost; levered FCF kept away from EV. Detailed rows, sources and accession numbers are in DV38_factcheck.json.
