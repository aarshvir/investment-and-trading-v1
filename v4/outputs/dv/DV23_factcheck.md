# DV23 verification: IQV, IR, IRM, ISRG, IT, ITW, IVZ, J, JBHT, JBL (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs; load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases and presentations, 10-Q text, companyfacts). Valuation re-tested on the programme basis: 10-year Treasury 5.17% (25 Sep 2026) + Blume-adjusted d4 beta x ERP 4.14%, ten years then 3.0% terminal, equity basis, free cash flow after SBC (dividends for the REIT). Full list: DV23_factcheck.json (71 facts).

**Totals:** 47 PASS, 8 MINOR, 15 FAIL, 1 UNVERIFIABLE. Corrections appended to 7 dossiers (IQV, IR, IRM, ISRG, ITW, JBHT, JBL); IT, IVZ and J had no FAIL.

| Ticker | Result | Key findings |
|---|---|---|
| IQV | 1 FAIL | Reverse DCF used Ke 8.5%; programme Ke 9.83% gives implied 8.8% (not 5.8%) vs 6.5% base. implied_vs_base in_line -> above; WATCH unchanged. All results, guidance quotes and the 3.59x leverage verified. |
| IR | 1 FAIL | 11.7% was a fade-start growth rate compared with an average base; SBC not deducted; Ke 9%. Restated average about 9.2% vs 8% base: above stands. WATCH unchanged. |
| IRM | 3 FAIL | Claimed no guidance exhibit: the 5 Aug 2026 8-K carries the presentation (FY26 guide raised on every line). EBITDA was estimated low (TTM about $2.80bn, EV/EBITDA 18.0x, not 19.6x). "7.5% cost of capital, 13-15% EBITDA growth" was never computed; dividend-basis at Ke 9.88% implies 13.3% a year: above stands. WATCH unchanged. |
| ISRG | 3 FAIL, verdict change | Guidance was raised at Q1 and Q2 (not "maintained"). Reverse DCF at WACC 8.5%, FCF before SBC ($0.83bn TTM), terminal 3.5%, EV netted for cash while FCF holds interest income: restated at Ke 10.6% on FCF after SBC, implied about 23% a year vs 11-13% base. INCLUDE-SMALL -> WATCH. |
| IT | clean | All results, balance sheet and retention verified; guidance is not on EDGAR (verified to the call transcript). Rate 9% vs 9.18%: immaterial. |
| ITW | 1 FAIL | Rate 8.5% and SBC: restated implied 9.9% (was 7.6%) vs 7.0% base; above stands, price near bull case. WATCH unchanged. |
| IVZ | clean | Q2-26 results, parent debt, preferred and flows verified; V1 rate 10.36% vs 10.99% programme (implied 3.5% vs 6.7% base: below holds). |
| J | clean | Fiscal Q3-26 (26 Jun 2026) labels and four guidance quotes verified; Ke 9% vs 8.42%: implied 5.8%, below base holds. |
| JBHT | 4 FAIL, verdict change | "Capex" cut of 64% is net investing outflow (gross additions -51%); "gross debt $1,227.7M" matches no balance sheet ($1,145.3M at 30 Jun 2026); SBC gap fillable; reverse DCF 6% not reproducible (7.9% at Ke 10.11% on FCF after SBC). Own central value is 31% below the price: INCLUDE-SMALL -> WATCH (lead sleeve had already excluded JBHT). |
| JBL | 2 FAIL | Price used was the 24 Sep close ($310.69; 25 Sep is $316.74). Reverse DCF added net debt to market value against after-interest FCF, untied WACC, no SBC: restated 12.2% (9.8% on FY26 FCF) vs 11% base: in_line holds. Post-cutoff 30 Sep 2026 FQ4 release (core EPS $4.40 vs $3.80-4.20 guide; FY27 core EPS outlook $17.55) checked; no kill criterion triggered. |

**Verdict changes:** ISRG INCLUDE-SMALL -> WATCH (F53_summary.json updated); JBHT INCLUDE-SMALL -> WATCH (f6_summary.json updated). Valuation-text updates without verdict change: IQV (implied_vs_base above), IR, IRM, ITW, JBL.
