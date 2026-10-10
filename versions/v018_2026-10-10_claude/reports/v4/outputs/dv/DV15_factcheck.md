# DV15 verification: EMR, EOG, EQIX, EQT, ERIE, ES, ESS, ETN, ETR, EVRG (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs (dossier_precheck_all500, xbrl_crosstie_all500, quarter_label_check_all500); load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q text, companyfacts) and the valuation method recomputed against the program rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated ERP; FCF, or dividends for utilities and REITs; SBC a cost). Full list: DV15_factcheck.json (97 facts).

**Totals:** 45 PASS, 19 MINOR, 24 FAIL, 9 UNVERIFIABLE. Corrections appended to 7 dossiers (EMR, EQIX, EQT, ERIE, ES, ESS, ETR); EOG, ETN and EVRG had no FAIL.

| Ticker | Result | Key findings |
|---|---|---|
| EMR | 5 FAIL, valuation change | Debt stock is $13.1bn (short-term $5.6bn + long-term $7.5bn), not the 10-K $8.92bn; TTM FCF $3.46bn not $3.71bn; EV arithmetic wrong; WACC untied to 5.17% and SBC not deducted: implied growth ~11.7-13% vs base 8-9%, so implied_vs_base in_line -> above. FY26 guidance never quoted ($7.26 is NTM, guide ~$6.55). WATCH unchanged. |
| EOG | clean | Already corrected by DVH4; quarterly table, debt/cash, TTM OCF/capex/SBC and Ke 7.29% replicate; guidance and antitrust case not in SEC documents. |
| EQIX | 3 FAIL | Reverse DCF used rf 4.2%, added back SBC and ignored growth capex: restated implied ~10.7% vs base ~10% (in line, not "below"); recurring capex is ~3% of revenue not 1.6%; "four consecutive raises" is three raises plus one initiation. INCLUDE-SMALL unchanged. |
| EQT | 2 FAIL | Q4 2024 EPS $0.69 not ~0.74; MVP deal was against ConEdison, not a Blackstone related party (related-party flag withdrawn); hedge percentage stale (kill criterion 4 already at trigger). Implied-below-base holds on every variant. INCLUDE-SMALL unchanged. |
| ERIE | 2 FAIL | Class A dividend yield 2.6% not 2.3%; dividend-only Gordon is wrong for a 41% payout: on TTM FCF ($553m) implied growth ~3.2% vs 4.5-5.5% delivered, so in_line -> below. INCLUDE-SMALL unchanged. |
| ES | 3 FAIL | TTM FCF ~$0.30bn not $0.81bn; justified-P/B arithmetic solves to 4.78% not 3.7% (and 7.4-7.9% at the 5.17% Treasury); utility dividend basis gives ~3.4% vs 5-7% guide: implied below base. INCLUDE-SMALL unchanged; missing scenario_returns_3y added. |
| ESS | 4 FAIL, verdict change | Q2 Total FFO ($3.32 vs Core $4.08) was hit by legal settlements the dossier missed ("no litigation"); debt omits $345m of lines of credit; Ke untied to 5.17%; stated scenario returns (2/9/15%) recompute to 0/6.3/10.7% from its own assumptions. **INCLUDE-SMALL -> WATCH.** |
| ETN | clean | Sales, EPS, five guidance releases, balance sheet, TTM FCF, EBITDA inputs, reverse DCF (12.2%) and scenario arithmetic all replicate; only note is the 8.0-9.0% rate band is not stated as Treasury plus ERP. |
| ETR | 4 FAIL, verdict change | Dossier's own "implied growth 9-10%" exceeds the 8% guided CAGR but was read as the "low end"; no DCF was run. Programme dividend basis gives ~12%: above base. FCF is -$2.5bn, debt +$4.2bn in H1, $2.175bn equity raise and 5% share growth omitted. **INCLUDE-SMALL -> WATCH.** |
| EVRG | clean | Guidance trail (five releases), debt lines ($16,498.0m), equity, cash, interest, 2,600 MW and the program-rate reverse DCF all verified; the exact fade structure of the DCF is not reproducible from the text (conclusion "above" holds under every variant). |

Verdict changes: ESS INCLUDE-SMALL -> WATCH (F113_summary.json updated); ETR INCLUDE-SMALL -> WATCH (F84_summary.json updated).

Valuation changes without a verdict change: EMR implied_vs_base in_line -> above (F101); EQIX below -> in_line, dossier_view cheap -> fair (F32); ERIE in_line -> below (F97); ES implied_vs_base set to below, data_conflicts and scenario_returns_3y added (F33).

Unverifiable from SEC documents (flagged, not failed): EOG antitrust case and breakeven claims; EQIX management call quote and $41.5m settlement; ETN Form 4 pattern and investor-page targets; ETR pipeline (7-12 GW), $57bn capex, NRC findings and the $101 price; EVRG vendor short-interest and Form 4 count; ES FY2024 $524m offshore-wind charge.
