# DV40 verification, 8 Oct 2026

Scope: TRGP, TRMB, TROW, TSCO, TSLA, TSN, TT, TTWO, TXN, TXT. Research only; not personal advice. Full table: `DV40_factcheck.json` (100 facts: 64 PASS, 15 MINOR, 17 FAIL, 4 UNVERIFIABLE). Eight dossiers carry a `## Correction (verification DV40, 2026-10-08)` section plus inline `[Corrected ...]` tags (TRGP and TXT had no FAIL); the matching F*_summary.json entries were updated (F158 TRMB, F165 TSCO, F57 TT and TXN).

Sources: 10-K/10-Q, 8-K Ex-99.1 releases and XBRL companyfacts from EDGAR; valuation basis = Ke 5.17% (10-year Treasury, 25 Sep 2026) + Blume-adjusted d4 snapshot beta x 4.14% ERP, ten years then 3.0%, equity basis, FCF after SBC.

| Ticker | Result |
|---|---|
| TRGP | No FAIL. Quarters, four guidance quotations, debt $19,578M / 3.5x, equity, 2026E reconciliation all tie. Ke 8.5% matches programme 8.54%; implied 6.6% vs base 5% reproduces. MINOR: SBC (~$80M) not deducted; Speedway/Train 13 dates sit in earlier releases. WATCH stands. |
| TRMB | Valuation FAIL: 9% rate untied; programme Ke 10.31% with SBC gives 8.4-8.7% vs 9% base (was 3.2-6.2%), so implied_vs_base below -> in line. SBC TTM $155M not $170M. Post-cutoff $500M delayed-draw term loan (2 Oct). Guidance, debt, leverage verified. INCLUDE-SMALL kept. |
| TROW | Q4 2025 operating income cell still $538.8M (actual $471.0M, 24.4%); Q1 2025 YoY -0.6% should be +0.8%; reverse DCF 3.5% is 5.3% after SBC and at 10.64%; Q1 10-Q accession wrong. WATCH stands. |
| TSCO | Valuation FAIL: 9% rate vs programme 7.84% -> implied 4.8% (FY26E FCF), 6.8% (TTM $590M), 15% (reported FCF $307M) vs ~7% base: above -> in line. Omitted $500M notes (25 Aug). WATCH kept on comps/guidance. |
| TSLA | Reverse DCF at 9% on EV; programme Ke 11.65%, SBC deducted: implied 46-65% (cases $37/$86/$223, weighted ~$108 vs $170). Direction unchanged. SpaceX stake $3.0bn fair value; $20bn term-loan 8-K (29 Sep). WATCH stands. |
| TSN | Valuation FAIL (9% vs 7.57%, SBC): implied -3.3% / -1.8% vs +1.1%; still far below 6% base. Omitted $1.0bn notes (Aug). Guidance cut/raise history, debt, leverage verified. INCLUDE-SMALL stands. |
| TT | "Three raises" was two (initial 29 Jan, raised 30 Apr, 30 Jul); balance sheet stale and $4.615bn is total, not long-term, debt (30 Jun net debt $3.30bn, 0.77x); valuation at WACC 8% on EV: programme basis implied 11.8-14.4% vs 9-10% base. **INCLUDE-SMALL -> WATCH.** |
| TTWO | Debt called convertibles (actually senior notes; $600M 3.70% due 14 Apr 2027); "SBC $132.4M" is the deferral column (SBC $86.0M Q1, ~$430M FY27); risk-free 4.2% stale and SBC not deducted: implied 18.2% -> 30.7%. Net Bookings -3% YoY omitted. WATCH stands. |
| TXN | $14.052bn is total debt (not LTD), $1.149bn current maturity, $3.341bn short-term investments ignored (net debt $7.05bn, 0.74x); TTM FCF includes ~$1.2bn CHIPS Act proceeds while the annualised base excludes them; programme basis implied 12.6-20% vs 9-10% base. **INCLUDE-SMALL -> WATCH.** |
| TXT | No FAIL. Quarters, guidance, Manufacturing-group debt, MV-75 figures verified; Ke 9.03% matches the 9.0% used; EV-vs-FCF mixing and 2.5% terminal are conservative (equity-basis implied 4.8% vs ~9% base). INCLUDE-SMALL stands. |

Verdict changes: TT INCLUDE-SMALL -> WATCH; TXN INCLUDE-SMALL -> WATCH. Implied-vs-base changed for TRMB (below -> in line), TSCO (above -> in line), TT and TXN (in line -> above).

Limits: TROW is not in any F*_summary file; the derived all500_register.json was not edited. TSLA/TSN/TTWO F*_summary entries were left unchanged (verdict, implied_vs_base, scenarios unchanged). China MOFCOM exposure (TXN), earlier-release guidance quotes (TXT), Form-4 details and earnings dates were left UNVERIFIABLE or only partly checked. Programme-basis recomputations are my own and labelled as such in each dossier.
