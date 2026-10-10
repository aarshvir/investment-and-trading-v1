# DV24 verification: JCI, JKHY, JNJ, JPM, KDP, KEY, KEYS, KHC, KIM, KKR (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs; load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts) and each valuation recomputed against the program rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated ERP of 4.14%; FCF or dividends, SBC a cost; P/TBV-ROTCE for banks). Beta values used in recomputations are assumptions (flagged in the facts). Full list: DV24_factcheck.json (78 facts).

**Totals:** 49 PASS, 10 MINOR, 17 FAIL, 2 UNVERIFIABLE. Corrections appended to 8 dossiers (JCI, JKHY, JNJ, JPM, KEY, KEYS, KHC, KKR); KDP and KIM had no FAIL.

| Ticker | Result | Key findings |
|---|---|---|
| JCI | 1 FAIL, implied_vs_base change | Operating figures and guidance trail (adj EPS ~4.55 -> 4.70 -> 4.85 -> 5.05) verified; TTM FCF $3.17B confirmed. Reverse DCF used an untied 8% WACC and no SBC deduction: at cost of equity ~9.6% implied growth is ~11-12%, above the 8-10% base: implied_vs_base below -> above. Verdict INCLUDE-SMALL label kept, but the name loses lead eligibility. |
| JKHY | 3 FAIL, implied_vs_base change | FCF omitted $188M of capitalized/purchased software (FCF ~$507M, 101% of NI, not $695M/138%); reverse DCF arithmetic not reproducible (own inputs give g 0.9%, not 3.0-3.3%); cash was $12.1M at 30 Jun 2026, so kill criterion 4 (cash < $15M) is already met. Restated implied 5.9-6.6%: above -> in_line. Verdict unchanged. |
| JNJ | 6 FAIL | Q2'25 comparator wrong ($23.743B, so +6.6% not +5.5%); FCF yield 6.4% is really 2.6%; current debt $11.7B omitted (net debt/EBITDA ~0.8x not 0.5x); talc facts updated from the 10-Q (76,000 plaintiffs, $3.7B reserve, plaintiffs withdrew experts); "2:1 stock split" unsupported. Implied stays above base (wider). Verdict unchanged. |
| JPM | 1 FAIL | All figures tie. Valued on P/E and an unsourced ROE, not P/TBV-ROTCE: P/TBV 3.03x needs ~21% sustained ROTCE (average of last five quarters ex one-offs): implied_vs_base below -> in_line. |
| KDP | clean | Results, segments, verbatim guidance trail, debt and litigation all verified; reverse DCF reproduces (method presentation gaps only). |
| KEY | 1 FAIL | Reverse DCF used rf 4.2% (not 5.17%) and an EPS/exit-multiple method; P/TBV 1.51x implies ROTCE ~12-14% vs 12.9% now and a stated >15% target, so in_line stands. NII "eight" rising quarters is nine. |
| KEYS | 3 FAIL | Net cash is ~$0.1B (a $700M current debt portion was omitted), not $0.8B; TTM revenue $6,582M not $6,682M; reverse DCF restated to ~15-18% (from 13%), further above base. Guidance gap closed: serial large beats. WATCH unchanged. |
| KHC | 1 FAIL | Adjusted EPS fell 6.5% in Q1-26 and 20.2% in Q4-25, not "13-19% every quarter"; all other figures tie. WATCH unchanged. |
| KIM | clean | Results, verbatim guidance, consolidated balance sheet, covenants and AFFO-based reverse DCF verified. |
| KKR | 1 FAIL (residual) | Prior DVH6 corrections independently confirmed; two stale sentences (s1, s8 bull 3) still carried the superseded "~3% implied" conclusion and are now tagged. |

Verdict changes: none. Valuation (implied_vs_base) changes without a verdict change: JCI below -> above (F87_summary.json), JKHY above -> in_line (F102_summary.json), JPM below -> in_line (F80_summary.json).

Unverifiable from SEC documents: JPM's four media-reported class actions and its NII/expense outlook (given on the call), KIM's preferred tender detail.
