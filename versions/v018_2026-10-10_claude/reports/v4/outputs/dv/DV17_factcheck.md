# DV17 verification: FDX, FDXF, FE, FERG, FFIV, FICO, FIS, FISV, FITB, FIX (as of 2026-10-10)

Method: every dossier read to the end (including earlier DVH5/DVH6 corrections) plus the three mechanical-check outputs; load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts); valuation method recomputed against the programme rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated ERP; FCF after SBC; interest not double-counted; P/TBV-ROTCE for banks). Full list: DV17_factcheck.json (86 facts).

**Totals:** 64 PASS, 7 MINOR, 10 FAIL, 5 UNVERIFIABLE. Corrections appended to 7 dossiers (FDX, FE, FERG, FFIV, FICO, FITB, FIX). **No verdict changes.**

| Ticker | Result | Key findings |
|---|---|---|
| FDX | 1 FAIL | Total debt omits $745m short-term borrowings (DVH6's $24.97bn too): $25.71bn, net debt $12.40bn (pre-spin). Mechanical flags are period-mismatch false positives. INCLUDE-SMALL unchanged. |
| FDXF | 1 MINOR | All results, guidance, debt, covenant verified. 9% rate not tied to 5.17% in text but equals WACC 8.9% at Ke 10.3%; implied 9.5% replicates; above base. WATCH unchanged. |
| FE | 2 FAIL, 1 UNVERIFIABLE | Net debt omits $1,376m short-term borrowings ($28.9bn; 5.3x on d4 EBITDA, 0.17x from the 5.5x kill line); d4 EBITDA $5.42bn not reproducible (filings give ~$4.0bn); Feb-2026 guidance was affirmed, not initial; Q4-25 loss is the $275m Ohio restitution, not pension MTM. Reverse DCF replicates. INCLUDE-SMALL unchanged. |
| FERG | 1 FAIL, 1 MINOR | Valuation: rate untied to 5.17%, post-interest FCF against EV, SBC not deducted; equity-basis implied 7.8%-9.6% vs base 7-7.5% (still above). Wrong debt-table column ($4,150m vs $4,925m). WATCH unchanged. |
| FFIV | 1 FAIL, 1 MINOR | Raise at midpoint is +$2.27, not +$2.71. 9% rate slightly low; implied 14.3-15.7%. WATCH unchanged. |
| FICO | 2 FAIL | SBC (~$174m TTM) added back in the reverse DCF: FCF after SBC $787m gives implied 8.4% (not 5.7%) and base value $614 (not $750); at $598 implied 3.5% (not 0.8%). WATCH unchanged; summary JSON updated. |
| FIS | 1 MINOR, 2 UNVERIFIABLE | DVH5 corrections replicate. Stated WACC blend does not reproduce 8.5% (gives 6.1%); across 7-9.5% implied growth is 0-2.5%, far below base. Leverage 3.5x and settlement are transcript/secondary. INCLUDE-SMALL unchanged. |
| FISV | all PASS | Results, guidance cut, debt, cash flow, departures verified; reverse DCF method consistent (Ke 11%, FCF after SBC). WATCH unchanged. |
| FITB | 2 FAIL, 1 MINOR | 15.6% is reported ROTCE, not adjusted (adjusted 19.0% incl. AOCI, 16.3% excl.); implied growth is 2.8%-4.4%, not 5-6%; value range $41-64 still brackets $52.10, so in_line and INCLUDE-SMALL stand. Q1 CET1 later restated 9.96% to 9.89%. |
| FIX | 1 FAIL, 1 MINOR | Bear case exit value uses FY26 EPS: $864+dividends gives -19.2%/yr, not -21.5%. Base/bull reproduce. WATCH unchanged; F60_summary.json bear return updated. |

Summary files updated (only changed fields): F44 (FITB reconciliation), F60 (FIX bear return, scenario_basis), F66 (FDX data_conflicts), F75 (FE kill criterion 2, data_conflicts, key_adverse_facts), F126 (FICO implied growth, base value, reconciliation), F142 (FERG reconciliation). F34, F124, F162, F169 unchanged (no field affected).

Open items for the lead: FE EBITDA definition (vendor $5.42bn vs filing-based ~$4.0bn) and kill criterion 2; FDX/FE short-term borrowings omission is a pattern worth a mechanical check across all dossiers (debt = current maturities + long-term + short-term borrowings/commercial paper).
