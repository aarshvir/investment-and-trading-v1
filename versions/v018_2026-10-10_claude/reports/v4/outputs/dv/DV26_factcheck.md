# DV26 fact-check (2026-10-08)

Scope: LII, LIN, LITE, LLY, LMT, LNT, LOW, LRCX, LULU, LUV. 49 facts checked against SEC EDGAR (8-K Ex-99.1, 10-Q, 10-K, companyfacts): 27 PASS, 9 MINOR, 12 FAIL, 1 UNVERIFIABLE. Corrections appended to 7 dossiers (LII, LIN, LITE, LLY, LNT, LOW, LRCX); LMT (already corrected by DVH4), LULU and LUV had no FAIL.

## Verdict changes
None. No verdict, implied_vs_base call or scenario changed. Summary files touched (text only): F24_summary.json (LLY kill criterion 4 baseline), F103_summary.json (LNT kill criterion 3 baseline and reconciliation text).

## FAILs by ticker
- **LLY** debt omitted $7,050M of current debt: total debt $54.9bn, net debt about $46.0bn, net debt / TTM net income 1.72x (not 1.46x), only 0.03x below the 1.75x kill threshold. Debt is capex-linked and disclosed, so INCLUDE-SMALL stands, with almost no headroom.
- **LNT** debt/equity 1.61x on total debt of $12.1bn (not 1.41x on noncurrent debt); total debt flat on year-end, not "reduced". Reverse DDM used a stale 4.2% risk-free rate; restated implied dividend growth 4.5-5.1% vs 5.5-6.5% base, "below" narrower. Hyperscaler MW/GW/capex-plan claims are not in the primary documents.
- **LII** revenue guide was raised at Q1 (29 Apr), reaffirmed at Q2; FY25 net income is $805.8M (not ~$789M); WACC 8.5% too low (restated implied ~5.4-6.6% vs 7-9% base, still "below").
- **LIN** two guidance raises, not three (the Feb range was the initial guide; Q1 exhibit now opened and verified); WACC 7.5% too low (restated implied 12.6-14.4%, "above" unchanged).
- **LITE** revenue landed inside, not at or above the top of, the guided range in all three quarters (EPS did beat the top).
- **LOW** guidance was trimmed once (19 Aug), not twice; reverse DCF paired EV with levered FCF at 8.0%: consistent bases give about 0-1%, strengthening "below".
- **LRCX** FQ3 guide was $5.70B +/- $0.3B set on 28 Jan 2026 (not ~$5.73B); FQ4 beat vs midpoint is +1.85% revenue and +$0.17 EPS (not +1.1% / +$0.14).

## Clean or minor only
- **LMT** Q2 2026 results, guidance row, backlog and the DVH4 corrections all tie. Open item for the lead: the register says implied_vs_base "in_line" while the programme-basis re-derivation (implied -4.7%/yr, or -0.6% to +2.2% at Ke 8.5%, vs delivered +2.9%) points to "below"; the dossier states no base growth rate so it is left unchanged.
- **LULU** every release figure and guidance quote ties; reverse DCF rate 8.5% vs 8.9% and SBC add-back are minor (restated -3.6% vs +3% base).
- **LUV** every release figure, guidance quote, debt/liquidity figure and TTM OCF ties; Q2 2025 adjusted EPS is company-reported ($0.43), not a calculation.

## Method notes
Rate check: 10y UST 5.17% + Blume beta x ERP 4.14% (V1 convention), or the dossier's own ERP where stated. Reverse DCFs re-solved over 10 years with the dossier's terminal growth, SBC treated as a cost, levered FCF paired with equity value and unlevered FCF with EV. Cache: C:\Users\user\eqv4\cache\DV26. Details, sources and accession numbers are in DV26_factcheck.json.
