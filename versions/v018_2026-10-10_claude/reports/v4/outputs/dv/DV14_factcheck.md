# DV14 fact-check (as of 2026-10-08)

Scope: DXCM, EBAY, ECHO, ECL, ED, EFX, EIX, EL, ELV, EME. 104 facts checked against SEC filings (EDGAR companyfacts, 10-Q/10-K, 8-K Ex-99.1): PASS 59, MINOR 13, FAIL 19, UNVERIFIABLE 13. Nine of ten dossiers carry a `## Correction (verification DV14 ...)` section; ELV had no FAIL.

## Verdict changes
- DXCM: WATCH -> INCLUDE-SMALL. V1's 30.2% implied growth was P/E-based; on FCF after SBC at 9.67% the price implies ~10%/yr (consensus 10.9%, base 12-14%). Also: net cash $0.7bn, not net debt $0.5bn; Q1 26 revenue $1,191.9M, not ~$1.15bn. F84 updated.
- EME: INCLUDE-SMALL -> WATCH. Reverse Gordon treated EPS as cash at 9% (should be 10.3%); FCF-based needs 13.7-15.1%/yr. Q4 25 12.7% margin includes a $144.9M UK-sale gain (underlying 9.7%); RPO baseline stale ($17.14bn, +43.9%); "debt $548M" is leases. F43 updated.

## implied_vs_base only (verdicts unchanged)
- ECHO below -> in_line (present value vs future price; DBS emerged 1 Oct 2026). ED below -> in_line (cost of equity not tied to 5.17%). EFX below -> in_line (rf 4.2% and SBC; current debt $1,410M omitted, net debt/FCF 4.8x not 3.5x). F143, F119, F64 updated.

## Other FAILs
EBAY: adjusted EPS +41% should be +17%; D/E 144% not 163%; FY outlook ranges not in the release. ECL: Q4 25 revenue $4,196M not $5,916M; reverse DCF mixed EV and levered FCF at 8% WACC (corrected ~17%). EIX: Q2 8-K is a text release (guidance verified), Q4 25 derivable. EL: Q3 FY26 organic was +2%, not accelerating; reverse DCF ~10.0% not 11.7%. ELV: all PASS (rate sensitivity MINOR).

## Notes
Unverifiable items (consensus, rating actions, earnings dates, Form 4s) are listed per company in the JSON. Scenario restatements for DXCM and EME use stated assumptions (FCF growth and exit yield) and replace undocumented bases.
