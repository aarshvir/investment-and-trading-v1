# DV44 verification: WMB, WMT, WRB, WSM, WST, WTW, WY, WYNN, XEL, XOM (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs; load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts XBRL) and each valuation recomputed against the program rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated premium; FCF or dividends; SBC a cost; no interest-income double count; P/B-ROE for insurers; ten-year growth then 3% terminal). The EDGAR submissions lists show no 8-K, 10-Q or 10-K after 24 Sep 2026 for these companies (the WY 24 Sep investor presentation is already in the dossier; ExxonMobil Holdings' 25 Sep 8-K is a note-related Item 8.01). Full list: DV44_factcheck.json (75 facts).

**Totals:** 53 PASS, 6 MINOR, 14 FAIL, 2 UNVERIFIABLE. Corrections appended to 8 dossiers (all except WMB and WY). One verdict change: XEL INCLUDE-SMALL -> WATCH. Two implied-vs-base changes without a verdict change: XOM in_line -> above; WYNN (none stated) -> in_line.

| Ticker | Result | Key findings |
|---|---|---|
| WMB | clean | Q2 table, all four guidance quotations, consolidated debt and 3.67x leverage, reverse DCF (10.3% at 8.5%) and scenarios replicate. Trailing AFFO/share is $5.15 not $5.16 (MINOR); risk premium unstated (MINOR). |
| WMT | 1 FAIL | Reverse DCF base ($14B OCF-capex) adds back $3.6B of stock compensation; with SBC as a cost implied growth is 27.9% at 8% (22.3% shown). Still above; WATCH unchanged. Everything else (quarters, guidance table, $57.2B debt, $2.9B tariff refunds) verified. |
| WRB | 2 FAIL | "Operating income below net income in three of four quarters" is wrong (Q2'26 operating $497.1M is above net $452.3M). P/E-Gordon reverse DCF treats EPS as cash with a 4.2% risk-free rate; on P/B-ROE implied growth is 1.4-5.6% vs 5-8% base, so still below. INCLUDE-SMALL unchanged. BVPS $26.50 (MINOR). |
| WSM | 1 FAIL | Interest income double-counted in the reverse DCF (+0.6 point to implied growth, immaterial); 12.35% not 12.5% at 8.9%. Quarters, tariff refund items, guidance and balance sheet verified. WATCH unchanged. |
| WST | 1 FAIL | Normalised FCF base adds back stock compensation; implied growth 17.9% at 9% (17.1% shown), base value $222 a share ($234). Still above; WATCH unchanged. Guidance, cash-flow mislabel, TTM FCF verified. |
| WTW | 1 FAIL | Re-verified DVH1's corrections (all hold, including its FCF reverse DCF 0.7%). New: "total debt $4.76bn (Sep 2025)" compares noncurrent-only; total was $5.31bn, so the rise is +23% not +37%. INCLUDE unchanged. |
| WY | clean | Quarterly table, segment-guidance trail including the 24 Sep Wood Products cut, 5.0x leverage table, TTM FCF $22M, reverse DCF (20%) and scenarios replicate. Q2 "$71M after tax" gain is pre-tax (MINOR). |
| WYNN | 3 FAIL | Q1/Q2 2026 revenue overstated by about $3M; Q2 buyback ($75.0M, $326.1M authorization left) omitted; no valuation existed ("cheap" rested on a Street target). FCF reverse DCF implies about 5% a year vs delivered 4-8%: in_line, fair not cheap. INCLUDE-SMALL unchanged, no margin of safety; scenarios have no stated basis. |
| XEL | 2 FAIL, verdict change | Reverse dividend model used D1 $2.05 (declared dividend is $2.37, $0.5925 a quarter), a perpetual 5-6.6% growth rate, and a "6-8% EPS/dividend" objective (dividend guide is 4-6%). On the program method the price needs 8.8% dividend growth at 8.5% vs 4-6% guided: above. **INCLUDE-SMALL -> WATCH** (marginal at the lowest discount rate). F50 updated. |
| XOM | 3 FAIL | Q1'25 EPS is $1.76 not $1.78; the 4.4% perpetual-growth model mixes EV with levered FCF, adds per-share buyback accretion to firm-level growth and calls a 3% volume CAGR mid-single-digit; program method gives 6.9-9.4% vs base 3-5%: above. Scenario base restated to +8.4%. Verdict WATCH unchanged; F59 updated. |

Summary files changed: F154 (WMT, text), F116 (WRB, text), F130 (WST, text), F35 (WYNN: implied_vs_base in_line, dossier_view fair, text), F50 (XEL: verdict WATCH, implied above, text), F59 (XOM: implied above, base scenario 0.084, text).

Limits: market prices, share counts and consensus data were taken from the dossiers, not independently verified; betas and risk premiums are stated assumptions; oil-price narrative in XOM is from secondary sources.
