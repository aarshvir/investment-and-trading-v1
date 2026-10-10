# DV01 verification, 9 Oct 2026

Scope: A, AAPL, ABBV, ABNB, ABT, ACGL, ACN, ADBE, ADI, ADM. Research only; not personal advice. Full table: `DV01_factcheck.json` (127 facts: 70 PASS, 24 MINOR, 31 FAIL, 2 UNVERIFIABLE).

Run history: an earlier DV01 attempt on 6 Oct 2026 finished A through ACN (correction sections dated 2026-10-06) and stopped before ADBE, ADI and ADM and before writing these files. This run verified ADBE, ADI and ADM from scratch (corrections dated 2026-10-09), then assembled the full 10-company record from the saved fact files.

Valuation re-tests used the programme parameters: 10-year Treasury 5.17% (25 Sep 2026), equity risk premium 4.14% for the three companies done in this run (4.5% in the earlier seven, as recorded in their sections), Blume-adjusted five-year weekly beta vs SPY, ten years of constant growth then 3.0% terminal, free cash flow burdened for stock-based compensation.

| Ticker | Result | Corrections written |
|---|---|---|
| A | Reverse DCF used WACC 8.5% with no stated ERP and added back SBC; restated about 16% vs base 8% | Dossier (6 Oct). Implied still above; WATCH unchanged |
| AAPL | Net-cash capital structure misdescribed (net cash about $62B); guidance claim mislabelled; DCF method; SBC and EV | Dossier + F17 summary. **INCLUDE-SMALL -> WATCH** |
| ABBV | Stale leverage and missed Apogee close ($10.9B) and $10B notes; FCF overstated ($19.7B vs $18.2B); DCF method | Dossier + F51 summary. **INCLUDE-SMALL -> WATCH** |
| ABNB | Net cash $9.6B, not $12B; share-count and Spain-fine wording | Dossier (second independent pass DVH4 also on file). Verdict unchanged |
| ABT | Q4'24 and Q4'25 table rows wrong; risk-free 4.2% in DCF | Dossier + F38 summary. Verdict unchanged |
| ACGL | Earnings DCF replaced with P/B-ROE for an insurer; implied ROE 11.4-12.3% vs 15.3% | Dossier (section records the F96 position). Verdict unchanged |
| ACN | Net cash and event scan wrong; b1 percentiles misquoted; method fine, implied below base | Dossier + F61 summary. Verdict unchanged |
| ADBE | Semrush ($1.87B, closed 28 Apr 2026) omitted and inside the guide raise; third senior departure omitted; price-reaction claim wrong; DCF at 8.5-10% with SBC added back (restated implied about -0.4%/yr vs base 8-10%) | Dossier + F26 summary (scenarios added). Verdict unchanged |
| ADI | Empower ($1.5B) and Alif ($1.35B) acquisitions and $3.0B notes omitted ("debt being paid down" false); dividend per share wrong; SBC tag exists; four gross-margin cells wrong; beta 1.21 not low, restated implied about 17.5%/yr vs base 9-11% | Dossier + F26 summary. **INCLUDE-SMALL -> WATCH** |
| ADM | Quarterly table, guidance, balance sheet, litigation all verify; omitted $275M negative MTM in Q1; cost of equity 8.5% vs programme 7.68% turns implied_vs_base from above to in line | Dossier + F119 summary. WATCH unchanged |

Verdict changes: AAPL, ABBV and ADI move INCLUDE-SMALL -> WATCH, each because the restated implied growth is above the base case, which fails the INCLUDE/INCLUDE-SMALL rule. ADM's implied_vs_base moves above -> in_line without a verdict change.

Open items: Street-consensus figures (ADBE Q4 guide vs consensus, ADI Street estimates) and press-sourced amounts (ADBE DOJ settlement split) are not in primary sources and are marked MINOR or UNVERIFIABLE. The ABBV dossier references a 5 Oct 2026 8-K (post cut-off) already noted in its correction section.
