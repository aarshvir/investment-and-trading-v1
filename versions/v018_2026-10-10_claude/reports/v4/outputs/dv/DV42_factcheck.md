# DV42 verification: VICI, VLO, VLTO, VMC, VMRK, VRSK, VRT, VRTX, VST, VTR (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs; load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts) and each valuation recomputed against the program rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated ERP; FCF or dividends, SBC a cost, no interest-income double count). Full list: DV42_factcheck.json (81 facts).

**Totals:** 48 PASS, 8 MINOR, 21 FAIL, 4 UNVERIFIABLE. Corrections appended to 9 dossiers (all except VLO). Four verdict changes, all INCLUDE-SMALL -> WATCH.

| Ticker | Result | Key findings |
|---|---|---|
| VICI | 4 FAIL | Dividend is $0.45 not $0.4525; Q1'26 AFFO/share +4.5% (5.7% is aggregate); year-ago equity $27.02bn; bear/bull scenarios wrong (bear -0.4%, bull +12.9% at the stated 9.5x). Verdict unchanged; F34 scenarios updated. |
| VLO | clean | Quarterly table, margin per barrel, guidance quotes, balance sheet, buybacks, reverse DCF and scenarios replicate (ERP unstated: MINOR). |
| VLTO | 2 FAIL | Debt $3,379M not $3,593M (net debt/EBITDA 0.91x not 1.06x); FCF base adds back SBC (implied 3.8% not 3.0%). Verdict WATCH, in_line unchanged. |
| VMC | 2 FAIL, verdict change | 7.5% WACC and SBC add-back: corrected implied 10-year FCF growth ~11.5% vs 5-6% base (above, not below); false "different basis" note. **INCLUDE-SMALL -> WATCH.** |
| VMRK | 2 FAIL, verdict change | 7.5% cost of equity inconsistent with the Treasury: at 8.8% implied ~3.3% = base (in_line). Borderline. **INCLUDE-SMALL -> WATCH.** |
| VRSK | 1 FAIL | Reverse DCF adds back SBC and mixes levered FCF with EV; corrected 3.5-4.2% still far below 7-8% base. WATCH unchanged. |
| VRT | 3 FAIL | Backlog $15bn / book-to-bill 2.9x are Dec-2025 figures presented as current; net debt $228m contradicts the company's net-cash statement (net cash ~$171m); base path compounds to 13.2% not 11-12%. WATCH unchanged. |
| VRTX | 1 FAIL, verdict change | Reverse DCF adds back SBC ($689M) and double counts interest income: corrected implied 12.2-13.9% vs 10% base (above). **INCLUDE-SMALL -> WATCH.** |
| VST | 3 FAIL | FY26 guidance was initiated in Nov 2025, not Feb 2026; EV omits $2.48bn preferred (EV/EBITDA 9.5x); $1.5bn junior notes of 24 Sep 2026 omitted (pro forma ~3.1x). WATCH unchanged. |
| VTR | 3 FAIL, verdict change | Release dated 29 Jul (not 7 Aug) and now primary-verified; leverage 4.72x not 5.3x; 8.5% cost of equity: at 9.0% implied 6.4% vs 7% base (in_line). Borderline. **INCLUDE-SMALL -> WATCH.** |

Verdict changes: VMC, VRTX, VMRK, VTR from INCLUDE-SMALL to WATCH (F107, F58, F134, F94 summary JSONs updated: verdict, implied_vs_base, reconciliation text, confidence note). VMRK and VTR are borderline (they depend on a 4.5% ERP; at 4.0% implied growth would sit below base). Scenario-only change: VICI (F34).

Unverifiable from SEC documents (flagged, not failed): VRT sell-side consensus, one-day stock move, S&P 500 inclusion and Form 4 items; VLO Fisher Form 4 sales; VTR prior $3.0bn investment guidance and period-end share counts; VRT TTM FCF as per the quant snapshot (filings give ~$2.9bn).

Caveats: sell-side/market inputs (prices, caps, betas) were taken from the dossiers, not re-pulled. Cost-of-equity restatements use 5.17% plus beta x 4.5% ERP, with betas of 0.8-0.85 for REITs and industrials as an assumption stated in each correction.
