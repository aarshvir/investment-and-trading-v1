# DV27 verification: LYB, LYV, MAA, MAR, MAS, MCD, MCHP, MCO, MDLZ, MDT (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs; load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts); each reverse DCF replicated and then recomputed on the program rule (10-year Treasury 5.17% on 25 Sep 2026 plus ERP 4.14% on a Blume-adjusted beta, free cash flow with SBC deducted, levered cash flow against equity value). Full list: DV27_factcheck.json (68 facts).

**Totals:** 41 PASS, 3 MINOR, 22 FAIL, 2 UNVERIFIABLE. Corrections appended to 9 dossiers (all except MAA). One verdict change: MCO INCLUDE-SMALL -> WATCH.

| Ticker | Result | Key findings |
|---|---|---|
| LYB | 2 FAIL | Reverse DCF arithmetic (3.5% should be 2.8%) and SBC added back: implied 4.2% vs base 3.0%, in_line -> above. Interest double-counted in the normalised FCF (minor). WATCH unchanged. |
| LYV | 1 FAIL | Reverse DCF adds back SBC, excludes growth capex, 9% rate below program ~9.65%: implied 19.5-23% (50% after growth capex) vs base 10%. Still above. WATCH unchanged. |
| MAA | clean | All figures, guidance rows, balance sheet and the 8.5% rate (5.17% + 0.81 x 4.14%) replicate. INCLUDE-SMALL unchanged. |
| MAR | 1 FAIL | Cost of equity 8.5% below program ~9.6%: implied 11-12% vs base 7%. Still above. WATCH unchanged. |
| MAS | 4 FAIL | Tariff refund is INCLUDED in adjusted EPS (dossier said excluded); adjusted margin ex-refund fell 70bps, not +410bps; Q2 balance sheet ignored (LTD $3,245M, not flat $2,945M); H1 OCF $417M vs $148M omitted, so the dossier's own TTM-OCF upgrade trigger is met. WATCH kept; upgrade review due. |
| MCD | 4 FAIL | Total debt $39.9B (no current portion) not $40.7B; leverage 2.6x not 2.8x (D&A $2.2B); TTM NI $8,787M; reverse DCF mixes levered FCF with EV. Still below base. INCLUDE-SMALL unchanged. |
| MCHP | 2 FAIL | Reverse DCF was EPS-based with SBC added back and stale 4.2% rf: FCF-based implied 14-24% vs 12.5%; $246.9M dividends are common only. WATCH unchanged. |
| MCO | 2 FAIL, verdict change | Q2 release cut FCF guidance (dossier said no cuts); 20x terminal multiple embeds ~5.8% perpetual growth: restated implied 14-15% vs base 12-13%, in_line -> above. INCLUDE-SMALL -> WATCH. |
| MDLZ | 3 FAIL | FY25 FCF $3.2B (not $3.5B) and no 2026 FCF guide cut; leverage 3.2-3.4x from the 30 Jun 10-Q (not 3.8x); EV-vs-levered-FCF mismatch: implied ~6.8% vs base 5-6%. WATCH unchanged. |
| MDT | 3 FAIL | Q1 FY27 +13.7% includes a 53rd fiscal week (~$570M, ~6.6 points; FY27 guidance includes it); FY26 non-GAAP EPS $5.53 below the reiterated $5.62-5.66; EPS-based DCF restated on FCF: implied 3-5% vs base 6-8%, in_line -> below. INCLUDE-SMALL unchanged. |

Summary files changed (only the affected fields): F141 (LYB), F139 (LYV), F138 (MAR), F36 (MCD), F76 (MCHP, MDT), F54 (MCO verdict and valuation fields), F104 (MDLZ wording). F156 (MAA) and F13 (MAS) unchanged. Scenario returns were not recomputed; they rest on EPS and multiples rather than the DCF.
