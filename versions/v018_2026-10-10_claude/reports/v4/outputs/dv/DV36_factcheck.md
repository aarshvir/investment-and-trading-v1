# DV36 fact-check (2026-10-09)

Scope: RL, ROK, ROL, ROP, ROST, RTX, RVTY, SBAC, SBUX, SCHW. 106 facts checked against SEC EDGAR (10-Q/10-K, 8-K Ex-99.1, companyfacts): 59 PASS, 15 MINOR, 21 FAIL, 11 UNVERIFIABLE. Correction sections appended to all 10 dossiers.

## Verdict change
- **RL: INCLUDE (full weight) -> WATCH.** The dossier contained no valuation test. On the program basis (UST 5.17% + Blume beta 1.236 x ERP 4.14% = Ke 10.29%; FY26 FCF $746M after $408M capex, $635M after SBC; equity $21.3B) the price implies 14.7%/yr 10-year FCF growth (12.6% before SBC) against 10-13% supported by the FY27 guide (revenue +5-6% cc, margin +60-80bp). Also FCF yield is 3.5%, not 4.1-5.8%; Q1 FY26 adjusted EPS is $3.77, not 3.62. f4_summary.json updated (verdict, valuation_view_vs_v1).

## implied_vs_base changes without a verdict change
- **SBAC in_line -> above (WATCH kept).** The 7.3% WACC was not built from the 5.17% Treasury; rebuilt WACC 7.55% gives implied 4.6% vs base 3.5% and a base value of about $142 vs price $166.15. Also Q2'26 net income is $198.8M (not 196.5) and Q3'25 $236.8M (not 240.4). F153 updated.
- **SCHW below -> in_line (INCLUDE-SMALL kept).** Earnings-growth DCF at 10.5% (4.2% risk-free) replaced by P/TCE-ROTCE: 6.8x tangible common equity requires about 41% sustained ROTCE vs 41% H1 and 44% Q2 actual (49% at the dossier beta). TTM EPS is $5.49 (Q4'25 $1.32), P/E 18.0x. Adjusted Tier 1 leverage (with AOCI) is already 6.8%, below the 7.5% kill criterion; guidance figures are not in the 8-K. F47 updated.

## Restated valuation, label unchanged
- **ROK** (WATCH, above): price was stale ($434.15 not $415.62); untied 8.3% WACC replaced; implied about 16% vs 9-10% stated (base 5-7%). F92 updated.
- **ROP** (INCLUDE-SMALL, below): "earnings yield minus WACC" is not a DCF; FCF-based implied is 0.4%/yr vs 2.3% stated, base 7-9%. Net debt/EBITDA is 3.36x incl. $718M current debt (not 3.1x), within 0.15x of the 3.5x kill criterion. F98 updated.
- **ROST** (WATCH, above): levered FCF set against EV and SBC not deducted; implied 9.7-10.7% vs 8.4-9.3%. F118 updated.
- **RVTY** (WATCH, above): 9% rate below program Ke 9.56%, SBC not deducted; implied 11.4-12.4% vs 10.1%. F148 updated.
- **SBUX** (WATCH, above): adjusted net income used as FCF and an untied 7.8% WACC; program basis about 12% vs 13-14% stated (does not reproduce at 7.8%). Omitted 24 Sep 2026 8-K (about 250 NA closures, about $300M charges, FY26 openings cut to about 440 from 600-650). GAAP>non-GAAP EPS confirmed as a $536.3M divestiture gain. F92 updated.
- **ROL** (WATCH, in_line): rate ties (8.58%); deducting SBC gives 6.9% vs 5-7% base (upper edge). TTM net income $531.7M (not 525.5); CFO effective 15 Jun (not 1 Jul), internal promotion. F71 updated.

## Findings, no valuation change
- **RTX** (INCLUDE-SMALL, in_line): DVH3 (6 Oct) corrections re-derived and confirmed (guidance verbatim including the FCF raise, debt, dividend, restated DCF). New: 8-K of 15 Sep 2026, Pratt & Whitney president Shane Eddy steps down 1 Jan 2027 (successor Jill Albertelli), not mentioned. F105 updated.

## Method notes
Rate: 10y UST 5.17% (25 Sep 2026) + Blume beta (0.67 x raw snapshot beta + 0.33) x ERP 4.14%; ten years then 3.0% terminal; equity-basis flows compared with equity value, EV-basis with EV; SBC deducted; banks on P/TCE-ROTCE. 25 Sep 2026 prices from v4/data/d2_adjclose.parquet. Detailed rows, sources and accession numbers are in DV36_factcheck.json.
