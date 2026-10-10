# DV31 verification: NTAP, NTRS, NUE, NVDA, NVR, NWS, NXPI, O, ODFL, OKE (as of 2026-10-08)

Method: every dossier read to the end plus the three mechanical-check outputs; load-bearing facts rechecked against SEC EDGAR (8-K Ex-99.1 releases, 10-Q/10-K text, companyfacts XBRL) and every reverse DCF recomputed under the program rule (10-year Treasury 5.17% plus ERP 4.14% with the V1 Blume-adjusted 5-year weekly beta; FCF with stock compensation as a cost; dividends for REITs). Full list: DV31_factcheck.json (74 facts).

**Totals:** 42 PASS, 13 MINOR, 17 FAIL, 2 UNVERIFIABLE. Correction sections appended to 8 dossiers (NTAP, NUE, NVDA, NVR, NWS, NXPI, O, ODFL); NTRS and OKE had no FAIL.

| Ticker | Result | Key findings |
|---|---|---|
| NTAP | 1 FAIL | Q1 FY27 is a 14-week quarter in a 53-week fiscal year: +29.9% YoY is about +20.6% like-for-like; V1 TTM base and the FY27 guide carry the extra week. All numbers and both guidance ranges otherwise verbatim. Verdict WATCH unchanged. |
| NTRS | clean | 56 table cells, notable items, capital ratios, balance sheet and scenario arithmetic all reproduce. Only note: 9.5% cost of equity untied to 5.17% (program convention 9.66%). |
| NUE | 2 FAIL | Total debt is $7,099M and net debt $4,407M (dossier used the long-term portion only: $6.389B / $3.91B). Reported steel-mills price is $1,145/ton, so the "$800/ton in 2026" claim and the $800 kill threshold are wrong. Q3 EPS range not in the 8-K. Verdict unchanged. |
| NVDA | 4 FAIL, verdict change | Debt jump is a $25.0B notes issue in June 2026 (not unexplained, not Hugging Face, which was announced 2 Sep); omitted $105B OpenAI/SB Energy guarantees and $366B commitments; reverse DCF used WACC 9.5% and added back SBC: implied growth is about 22% (not 15.4%). **INCLUDE-SMALL -> WATCH.** |
| NVR | 3 FAIL | Three 2025 rows are 2024 data: true YoY revenue -21.7%/-10.5%, EPS -28.5%/-22.6% (not -41.8%/-30.4%). The "$1.09bn debt" is not the NVRM facility ($150M, undrawn); it equals cash. Orders and backlog (+9% units) have turned, which is the dossier's own condition for revisiting WATCH (lead for re-rank). |
| NWS | 3 FAIL | FCF is $811M (company), not $1,045M; market cap $16.0B not $17.1B; REA minorities take 23% of earnings. Implied growth about 4.8% (not 2.3%), still below the 6-8% base. Verdict unchanged. |
| NXPI | 2 FAIL | TTM FCF is $2,807M (not $3.56B) and the 11.8% WACC used beta 1.82 (program convention about 9.4%): implied 9.1-11.4%, "in line" borderline. Debt ladder wrong (nothing due in rest of 2026). Verdict unchanged. |
| O | 2 FAIL | Fitch assigned (not reaffirmed) an A rating. AFFO-Gordon method replaced by dividend basis: implied growth about 1.8-2.3% (not 0-0.5%), still below the roughly 4% guide. Verdict unchanged. |
| ODFL | clean (4 MINOR) | Leftover wrong FCF figures in the text, debt about $20M not zero, 2026 capex plan about $380M omitted, 450bp is YoY not sequential, normalised implied growth about 16.5% not about 20%. WATCH unchanged. |
| OKE | clean | Table, all three guidance quotes, debt, cash flow and the reverse DCF reproduce; Class B terms stated slightly loosely (15% of consolidated CFFO, 20% above 4.5x leverage, 7.01%). |

**Verdict changes:** NVDA INCLUDE-SMALL -> WATCH (F17_summary.json updated: verdict, valuation_view_vs_v1, kill criterion 5, key adverse fact 5, data conflicts, confidence).

**Other summary JSON edits (changed fields only, no verdict change):** F77 (NTAP), F45 (NUE), F99 (NVR key adverse facts, kill criteria, data conflicts), F89 (NWS valuation), F30 (NXPI valuation, data conflicts), F114 (O valuation), F81 (ODFL valuation, data conflicts).

**Leads:** NVR WATCH premise ("no confirmed trough") is contradicted by orders and backlog; consider re-rank to INCLUDE-SMALL. NXPI valuation is fair-to-full rather than comfortably in line.
