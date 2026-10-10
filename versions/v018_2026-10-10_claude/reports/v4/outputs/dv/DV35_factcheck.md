# DV35 fact-check (2026-10-08)

Scope: PSX, PWR, PYPL, Q, QCOM, RCL, RDDT, REG, REGN, RF. 62 facts checked against SEC EDGAR (10-Q/10-K, 8-K Ex-99.x, companyfacts): 28 PASS, 12 MINOR, 17 FAIL, 5 UNVERIFIABLE. Correction sections appended to 8 dossiers (PWR, PYPL, Q, RCL, RDDT, REG, REGN, RF); PSX and QCOM had no FAIL.

## Verdict change
- **RCL: INCLUDE-SMALL -> WATCH.** The reverse DCF used TTM adjusted net income as the cash flow and divided it into enterprise value (the stated 8.0% reproduces only that way). TTM free cash flow is -$416M. On free cash flow to equity (FY26E about $2.5-3.0B, equity value $65.0B, Ke 12.4% from the dossier's own beta 1.75) implied 10-year growth is about 13-15.5% (11.4% unlevered) against a 7% base: implied_vs_base above, which the program rule says disqualifies INCLUDE-SMALL. F21 summary updated; scenarios restated to about -23% / -5% / +6%. Also Q4 2024 GAAP EPS is $2.02, not $2.27.

## implied_vs_base changes without a verdict change
- **RDDT below -> in_line.** Net cash omitted $1.30B of marketable securities (cash plus securities $2.79B); FCF added back $338M stock compensation and counted about $93M interest income. Corrected implied growth about 22.6% vs 15.5%, within about 1.5 points of the dossier's own 24% base path. INCLUDE-SMALL kept. F20 updated.
- **REG below -> in_line.** FFO (levered) was set against EV with a 7.2% rate and no recurring capex; on TTM AFFO $728.8M and equity value at Ke 9.0-9.5% implied growth is 4.5-5.9% vs a 4-5% base. Guidance was raised once in 2026, not twice (Q1 reaffirmed); FY25 Core EPS was $4.41. INCLUDE-SMALL kept. F104 updated.
- **REGN below -> in_line (borderline).** FCF not charged for $987M stock compensation; cash and securities are $17.8B (net cash $15.8B), not unquantified; the GAAP/non-GAAP gap is stock compensation, a $176M manufacturing interruption charge and amortization, not securities marks; capex guide is $1.030-1.100B (the $985M figure is COCM). Corrected implied growth 8.3-9.2% vs a 6-8% base. INCLUDE-SMALL kept. F47 updated. Post-cutoff: Sanofi Sixth Amendment ($1.0B upfront, up to $7.0B milestones), 1 Oct 2026.

## FAILs and findings by ticker (verdict unchanged)
- **PWR** (WATCH): GAAP-to-adjusted gap is amortization ($1.03/sh) and stock compensation ($0.42/sh) add-backs, not equity-method marks; debt is $6,104.9M per the 10-Q (net debt/EBITDA 1.8x, not 2.0x); TTM EBIT is $2,036M (EV/EBIT 50x, not 47x). Guidance now verified verbatim in the primary release; FCF-based implied growth 20-25%/yr. F91 updated.
- **PYPL** (INCLUDE-SMALL): kill criterion 2 (non-GAAP operating margin contraction) is already met as written, three consecutive quarters (Q4'25 -9bp, Q1'26 -229bp, Q2'26 -248bp). DVH6 corrections confirmed; reverse DCF about -5.2% (or -4.5%, convention) vs far higher trajectory. DOJ item still unverified. F114 annotated.
- **Q** (WATCH): table row "Q4'24" is Q4 2025; reverse DCF set levered adjusted FCF against EV at an untied 9.5%; equity basis gives about 18-20% (14% unlevered) vs 10-12% base. New: PFAS indemnification $43M, new CFO from 1 Oct 2026. F78 updated.
- **RF** (WATCH): clean on numbers and valuation method; guidance deck cited with wrong accession and date (acc -000057, 7 Aug 2026); NII and NIE guides confirmed maintained.

## Clean
- **PSX** (WATCH): every figure ties (Q2'26 NI $3,847M, EPS $9.55, debt $20,565M, crack spread $41.63, Propel accrual $928M); reverse DCF reproduces exactly (market cap equals the bull PV). New: EVP Refining retiring 31 Dec 2026.
- **QCOM** (WATCH): every figure ties (Q3 FY26 revenue $9,947M, EPS $1.87 / $2.21, Q4 guide verbatim, debt $15,270M, net debt $6,966M); reverse DCF and scenario IRRs reproduce exactly; the 9.5% rate is untied to rf + beta x ERP (at 10.1% implied growth is about 16.3%, so the call is conservative).

## Method notes
Rate check used 10y UST 5.17% (25 Sep 2026) plus the dossier's stated or V1's ERP 4.14% with Blume beta. SBC treated as a cost, interest income kept out of EV-based flows, levered cash flows matched with equity value, REITs on AFFO, banks on P/B-ROE with a P/TBV-ROTCE cross-check. Detailed rows, sources and accession numbers are in DV35_factcheck.json.
