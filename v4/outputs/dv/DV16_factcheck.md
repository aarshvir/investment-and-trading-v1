# DV16 verification: EW, EXE, EXPD, EXPE, EXR, F, FANG, FAST, FCX, FDS (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs (dossier_precheck_all500, xbrl_crosstie_all500, quarter_label_check_all500); load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts, later 8-Ks) and the valuation method recomputed against the program rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated ERP; FCF, or dividends for REITs; SBC a cost). Full list: DV16_factcheck.json (92 facts).

**Totals:** 56 PASS, 11 MINOR, 17 FAIL, 8 UNVERIFIABLE. Corrections appended to 7 dossiers (EW, EXE, EXPD, EXR, FANG, FAST, FDS). EXPE and F had no new FAIL (their earlier DVH4/DVH5 corrections replicate) and FCX only a MINOR date update, so those three received no DV16 section.

| Ticker | Result | Key findings |
|---|---|---|
| EW | 1 FAIL (valuation) | 8.0% WACC not tied to 5.17%; H1 FCF annualised (Q1 OCF only $44m) and SBC not deducted; TTM FCF after SBC $1,266m gives implied ~15.5% (not 12.5%) vs 9-10% base. Segment growth quoted in constant currency unlabelled; short-term investments ($1.35bn) omitted from net cash. WATCH unchanged. |
| EXE | 3 FAIL | Q4 "adjusted net income" cells are adjusted FCF; stale share count (239.2m vs 231.5m, market cap $20.1bn); Twin Eagle financing omits $500m 5.65% notes issued 17 Sep and ~0.5x leverage is pre-deal (~0.74x pro forma). Reverse DCF replicates (-1.6%), 'below' holds on FY25/TTM bases but flips to +2.8% on Q2 run-rate. INCLUDE-SMALL unchanged. |
| EXPD | 1 FAIL (valuation) | Quarterly data, guidance statements and cash flows all replicate; 8.93% cost of equity untied to 5.17%: implied 17.3% (not 14.2%), $130 revisit level becomes ~$117. WATCH unchanged. |
| EXPE | clean (post-DVH4) | DVH4 corrections independently replicate (results table, guidance raised once, $280m minority-investment gain, TTM FCF $4,459m, restated DCF -5.8% to +1.0%); only minor notes (net cash includes merchant float, ERP 4.14% vs 4.5%). INCLUDE-SMALL unchanged. |
| EXR | 4 FAIL, verdict change | "Raised for a second straight quarter" is false (raised once; Q1 unchanged); Ke 7.5-8.0% untied: at 9.2-9.67% implied Core FFO growth +3.1% to +4.1% = base, so implied below -> in_line; Core FFO share base wrong (221.0m not 211.2m); scenario returns recompute to -0.3/+8.5/+13.5%; unopened 24 Aug 8-K is CEO retirement. **INCLUDE-SMALL -> WATCH.** |
| F | clean (post-DVH5) | Quarterly table, guidance, balance sheet (note: the 10-Q prints Dec-25 before Jun-26), FCF reconciliation and DVH5 restated DCF (4.3% on $3.9bn) all replicate; 2 Oct F-150 supplier 8-K confirmed. INCLUDE-SMALL unchanged. |
| FANG | 3 FAIL | Total debt fell ~$1.9bn, not $2.7bn (current maturities doubled to $1.5bn); buyback figures wrong (Q1 $548m incl. $514m related-party, Q2 $141m) and Stephens-related repurchase/board stepdown omitted; no reverse DCF was run (recomputed: ~0-5% on normalised FCF, 'in_line' stands). INCLUDE-SMALL unchanged. |
| FAST | 1 FAIL (valuation) | All financials, guidance and cash-flow figures replicate; 9% rate untied (ERP 3.8%): implied ~18.8%; the $42 revisit level is a scenario-return price, a 9% DCF base case is worth ~$24-27. WATCH unchanged. |
| FCX | clean (1 MINOR) | Table, guidance trail, net debt scope, MOU terms and reverse DCF (31%/25%, $50/$73/$76) replicate on the program's 5.17% + ERP; 2 Oct operational-update 8-K confirms Q3 earnings on 27 Oct (dossier estimated ~22 Oct). WATCH unchanged. |
| FDS | 4 FAIL | Results table carried wrong-column values (Q3 FY24-Q2 FY25 revenue/EPS, Q3 FY25 adjusted EPS $4.27 not $4.05, Q1/Q2 FY26 GAAP and adjusted EPS); FY25 net income $597.0m not ~$561m; WACC 8.5% untied and levered FCF vs EV (restated implied ~1.6-3.3%, still below base). Post-cutoff: FY26 results issued 30 Sep (adjusted beat, GAAP EPS missed; FY27 organic ASV guide 5.0-6.5%). INCLUDE-SMALL unchanged. |

Verdict changes: **EXR INCLUDE-SMALL -> WATCH** (F113_summary.json updated: verdict, implied_vs_base in_line, reconciliation, scenario_returns_3y, thesis line, adverse facts, confidence).

Valuation changes without a verdict change: none in the F-summaries (EW, EXPD, FAST implied growth restated upward but 'above' unchanged; EXE and FDS restated, direction unchanged; FANG recomputed, 'in_line' stands).

Unverifiable from SEC documents (flagged, not failed): EW competitor share and trial timelines; EXPE Muse/AI-agent news, Vrbo suit and street targets; EXPD Form 4 count and V1 peer inputs; EXR net debt/EBITDA estimate; F Ford Pro 879,000 subscriptions; FANG WTI price, breakeven and Iran commentary; FAST Form 4 pattern and consensus targets; FCX short interest and Street data.

Note on programme discount rates: DVH4/FCX used ERP 4.14% with Blume beta; DV15 and this run used 4.5%. Every conclusion above is robust to either ERP (e.g. EXR at 4.14% x beta 0.9 gives Ke ~8.9% and implied growth ~2.6%, still within the 2-4% base).
