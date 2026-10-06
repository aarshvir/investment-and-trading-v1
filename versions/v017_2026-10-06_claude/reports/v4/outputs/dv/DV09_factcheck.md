# DV09 verification: CI, CIEN, CINF, CL, CLX, CME, CMG, CMI, CMS, CNC (as of 2026-10-06)

Method: every dossier read to the end plus the three mechanical-check outputs (dossier_precheck_all500, xbrl_crosstie_all500, quarter_label_check_all500); load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts) and the valuation method recomputed against the program rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated ERP; FCF or dividends, SBC a cost). Full list: DV09_factcheck.json (73 facts).

**Totals:** 40 PASS, 8 MINOR, 20 FAIL, 5 UNVERIFIABLE. Corrections appended to 6 dossiers (CIEN, CL, CME, CMG, CMI, CMS); CI, CINF, CLX and CNC had no FAIL.

| Ticker | Result | Key findings |
|---|---|---|
| CI | clean | All figures, guidance quotes, balance sheet and reverse DCF replicate (post-cutoff 30 Sep 8-K reaffirms guidance and adds a 10-14% EPS growth target). |
| CIEN | 3 FAIL | Q4 FY25 revenue is $1,352.0m (not ~1,290); growth sequence 24-31-36-37% is wrong (20.3, 33.1, 39.5, 37.0); reverse DCF adds back SBC and the rate is untied to 5.17%: implied CAGR restated from 21-23% to ~25-30% (still above base). Verdict WATCH unchanged. |
| CINF | clean | Table, ratios, portfolio and V1 P/B-ROE method verified; quarter-label flag is a false positive (820 is net income). |
| CL | 4 FAIL, verdict change | Q1/Q2 growth rates wrong (true +8.4%, +4.9%); margin fall is restructuring charges, not tariffs; omitted Q4-25 (1.8% margin, net loss) means kill criteria 1 and 4 are already met; debt is falling, not rising. **INCLUDE-SMALL -> WATCH.** |
| CLX | clean | Guidance trail, balance sheet and reverse DCF verified; crosstie debt flags compare against Jun-2025. |
| CME | 4 FAIL | 2025 table rows are 2024 data; all four YoY growth rates wrong (true Q1-26 +14.5%, Q2-26 +0.8%); debt $3,424m not $3,868m; buybacks $1.24bn in H1 are not modest. Verdict unchanged. |
| CMG | 3 FAIL, implied_vs_base change | Q1 2025 comp was -0.4%; TTM FCF $1,569m not $1,116m; lease-liability EV double count and 8.5% rate: implied growth 8-9% (not 12.9%) so implied_vs_base above -> in_line. Verdict label WATCH kept, lead to re-rank. |
| CMI | 3 FAIL | Charge $458M/$3.28 is full-year (Q4 $218M/$1.54); guidance raised twice not three times; net debt $3.77bn (0.7x) not $3.16bn; kill criterion 1 already met at Q2-26. Verdict WATCH unchanged. |
| CMS | 3 FAIL | Q3-25 guidance was raised (not maintained), FY26 raised once not twice; securitization debt is only $525M and leverage is ~6.2x not 4.6x; TTM OCF $2.15bn not $2.77bn. Verdict INCLUDE-SMALL unchanged. |
| CNC | clean | Eight-quarter table, quote-by-quote guidance trail, debt/parent-cash scope and reverse DCF verified (only wording: two raises in 2026, not three). |

Verdict changes: CL INCLUDE-SMALL -> WATCH (F101_summary.json updated). Valuation change without verdict change: CMG implied_vs_base above -> in_line (F112_summary.json). Summary JSONs also edited for CIEN (F95), CME (F99), CMI and CMS (F40); only changed fields.

Unverifiable from SEC documents (flagged, not failed): CME antitrust and Kalshi/CFTC litigation, CMG Salmonella suit and 2024 class action, CMS Moody's outlook and Q2 EPS bridge, CMI Form 4 pattern, CINF sell-side revisions.
