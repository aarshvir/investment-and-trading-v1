# DV10 verification: CNP, COF, COHR, COIN, COO, COP, COST, CPAY, CPRT, CPT (as of 2026-10-09)

Method: every dossier read to the end plus the three mechanical-check outputs (dossier_precheck_all500, xbrl_crosstie_all500, quarter_label_check_all500); load-bearing facts rechecked against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K text, Form 4 XML, companyfacts) and the valuation method recomputed against the programme rule (10-year Treasury 5.17% on 25 Sep 2026 plus a stated ERP; FCF or dividends, SBC a cost, interest income not double-counted). Full list: DV10_factcheck.json (93 facts).

**Totals:** 57 PASS, 13 MINOR, 16 FAIL, 7 UNVERIFIABLE. Corrections appended to 6 dossiers (CNP, COF, COHR, COO, CPAY, CPRT); COIN, COP, COST and CPT had no FAIL (minor notes only, no edit).

| Ticker | Result | Key findings |
|---|---|---|
| CNP | 4 FAIL | Q2'26 revenue is $2,152m (not ~2,110); dividend input to the Gordon model should be $0.96 (not $0.855) and r=8.5% is not tied to the 5.17% Treasury (implied growth 5.9% at 8.5%, 7.6% at 10.2%); pending $2.62bn Ohio gas sale to National Fuel (closed 1 Oct) omitted from M&A; 14 Sep 2026 cybersecurity 8-K missing from red-flag scan. Verdict INCLUDE-SMALL unchanged but rate-sensitive. |
| COF | 3 FAIL | FY2024 revenue is $39.1bn (53.4 is FY2025); "Q1 2025 22.5" is H1 (Q1 = $10.0bn); Brex acquisition (7 Apr 2026, ~$4.5bn) omitted and is part of the CET1 decline. P/TBV ~2.0x vs P/B 1.09x noted. Verdict WATCH unchanged. |
| COHR | 5 FAIL, verdict change | Q3 FY26 revenue was inside (not above) guidance; NVIDIA's $2bn equity purchase (Mar 2026) and $825m of short-term investments omitted from net debt and financing risk; reverse DCF added back SBC and used EPS as cash: recomputed implied revenue CAGR ~22% (19.5-26%) vs ~20% base = above. **INCLUDE-SMALL -> WATCH** (borderline). |
| COIN | clean | Eight-quarter table, quote-by-quote guidance, balance sheet, buybacks and reverse DCF replicate (mechanical cash flag is a false positive). Minor: stated F0 components do not reproduce $0.9bn (a lower F0 only strengthens "above"); director-affiliated 10b5-1 sale plan not noted. |
| COO | 1 FAIL | Reverse DCF FCF added back SBC: implied growth 7.3% (not 5.6%) vs 6.0% base, so implied_vs_base in_line -> above. Verdict WATCH unchanged; all guidance quotes, quarters and debt tie. |
| COP | clean | Quarters, four guidance quotes, balance sheet, Kirkuk/noncore deals and V1 row tie. Minor: levered FCF vs EV and SBC not deducted roughly offset. |
| COST | clean | FY26/Q4 statements, balance sheet, 10-Q debt schedule and reverse DCF (18.3%/14.0%/22.0%) reproduce exactly; minor: Q4 "ticket +5.9% adjusted" is the unadjusted ticket (adjusted +3.3%). |
| CPAY | 1 FAIL | Re-checked the DVH6 corrections (all stand). CEO Form 4 sales are 213,860 shares / ~$88.5m (dossier captured only the 25 Aug leg, $49m); organic growth is 10% (at the kill threshold), reported acceleration is acquisition-driven. Verdict unchanged. |
| CPRT | 2 FAIL | "Cash data conflict" does not exist ($1.91bn cash + $2.58bn HTM = $4.49bn); reverse DCF double-counts interest income on $4.5bn cash and adds back SBC: implied 5.5-6.2% vs 3-4% base = above (not in_line). FY26 FCF actually rose 2.9% as capex fell 41%. Verdict WATCH unchanged. |
| CPT | clean | Quarterly table, four guidance rows, California sale, debt, leverage and AFFO reverse DCF (2.3%/3.3%/1.2%) all reproduce. |

Verdict changes: COHR INCLUDE-SMALL -> WATCH (F95_summary.json updated: verdict, implied_vs_base, reconciliation). Valuation-only changes: COO implied_vs_base in_line -> above (F120_summary.json), CPRT in_line -> above (F36_summary.json); CNP reconciliation text updated for corrected implied growth (F109_summary.json). Only changed fields edited.

Unverifiable from SEC documents (flagged, not failed): CNP FFO/debt and net debt/EBITDA (secondary sources) and 2026 convertible settlement outcome; COP price strip level; COST Q1 membership-income comparison; COIN Underwood ruling detail; CPT Q1 charge/share-repurchase detail; COO segment organic percentages.
