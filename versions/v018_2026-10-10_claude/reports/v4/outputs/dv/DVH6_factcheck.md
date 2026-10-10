# DVH6 verification, 6 Oct 2026

Scope: FDX, AMCR, VZ, OMC, CPAY, BRO, PYPL, KKR. Research only; not personal advice. Full table: `DVH6_factcheck.json` (101 facts: 42 PASS, 15 MINOR, 29 FAIL, 15 UNVERIFIABLE). All eight dossiers carry a `## Correction (verification DVH6, 2026-10-06)` section plus inline `[Corrected ...]` tags; the matching F*_summary.json entries were updated (F66 FDX, F72 AMCR, F128 VZ, F35 OMC, F41 CPAY, F40 BRO, F114 PYPL, F111 KKR).

Sources: 10-K/10-Q, 8-K Ex-99.1 releases and XBRL companyfacts from EDGAR; valuation basis = Ke 5.17% (10-year Treasury, 25 Sep 2026) + Blume-adjusted d4 snapshot beta x 4.14% ERP, ten years then 3.0%, equity basis, FCF after SBC.

| Ticker | Result |
|---|---|
| FDX | **FAIL:** Q3 FY24 row is the prior-year column (Q3 FY23); "three raises" was two; debt growth mixes bases; post-spin balance sheet stale (July 2026 ~$4.9bn note repurchase, Sept 2026 new notes, InPost, Supply Chain sale, 19.9% Freight stake); single Federal Express segment replaced by two segments; valuation mixes pre-spin FCF/EPS with a post-spin price, 7.5% rate untied, SBC not deducted. implied_vs_base stays below. |
| AMCR | Auditor change omitted (PwC Switzerland to PwC US, 8-K 4.01); valuation used WACC against EV with levered FCF and no SBC; on programme basis implied growth +0.3% (reported) so "below" holds on both bases. |
| VZ | "three consecutive raises" was two; $625M cash payment in the BT joint venture omitted; DCF rate 8.5%, no SBC deduction; implied growth about -1.0% to -6.2%, still below base. |
| OMC | Net debt/leverage wrongly called undisclosed ($2.2bn at YE25, 0.6x pro forma; $6.7bn at 30 Jun 2026); "$3.5bn" buyback is a 2026 target ($3.0bn done in H1); margin basis mix; valuation was a P/E heuristic, programme reverse DCF supports cheap. |
| CPAY | Derived Q4 2024 and Q4 2025 rows wrong; guidance midpoint raise $0.65 not $0.45; $100.9m FTC charge is the same case (proposed consent order), not a separate matter; kill criterion 5 arithmetic (81.6% already above 50%); SBC not deducted (implied 1.9-6.1%). |
| BRO | Q4 2025 organic revenue was -2.8% (omitted), so growth turned negative a quarter earlier than stated; Q4 adjusted EPS $0.93 not $0.89; EPS down in 4 of 5 quarters; levered FCF at a WACC against EV, SBC not deducted. |
| PYPL | CEO since 1 Mar 2026 not 2025; a $0.14 quarterly dividend exists; active-account kill criterion already met (Q1 and Q2 both -0.04% QoQ); SBC not deducted and stale share count; scenario returns not reproducible (restated -9.4% / +8.4% / +17.3%). |
| KKR | "$4.68bn new capital" is FRE per adjusted share (actual $133bn LTM); DCF rate 9.0% untied (11.50% on programme basis) and ANI not net of SBC: **implied_vs_base below -> in line**; scenarios restated (-4% / +10% / +22%). |

Verdict changes: none (all stay INCLUDE-SMALL). Implied-vs-base changed for KKR (below -> in line), and the lead should reconsider KKR (valuation no longer supports INCLUDE-SMALL on its own).

Limits: Freight carve-out FCF (FDX), OMC FCF base (secondary consensus), AMCR/OMC leverage estimates and KKR SBC after-tax figure are my estimates and labelled so in the dossiers; press-sourced items (litigation, insider sales, earnings dates, KKR 10-K quote, BRO deal terms) were left UNVERIFIABLE. The token budget was exceeded modestly.
