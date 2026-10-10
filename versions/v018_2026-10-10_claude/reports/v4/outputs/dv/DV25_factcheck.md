# DV25 fact-check (as of 2026-10-10)

Scope: KLAC, KMB, KMI, KO, KR, KVUE, L, LDOS, LEN, LHX. 77 facts: FAIL 6, MINOR 12, PASS 56, UNVERIFIABLE 3. Dossier corrections appended: KLAC, KVUE, LEN, LDOS (4 files); F28_summary.json (KLAC) and F164_summary.json (LEN) updated. No verdict changes; one implied_vs_base restatement (LEN below to above).

## FAILs

- **KLAC** - Net debt approx $1.25bn (also EV $246.49bn) -> $5,887.4m - $4,902.4m = $985m; EV about $246.2bn (Minor; no effect on verdict. Correction appended.)
- **KLAC** - Dividend raised to $2.30/share annualised (17th consecutive increase); new $7bn buyback; $2.29bn FY26 repurchases -> Quarterly dividend level raised to $2.30 per share PRE-split ($0.23 post-split, $0.92 a year); 17th consecutive increase and $7bn authorisation confirmed; FY26 repurchases $2,289.8m (Annualised/quarterly confusion; correction appended.)
- **KVUE** - "Three consecutive quarters of positive organic growth after four negative ones" -> Negative organic growth only in Q1 2025 (-1.2%), Q2 2025 (-4.2%), Q3 2025 (-4.4%); Q4 2024 was +1.7% (Three negative quarters, not four; correction appended. No verdict effect.)
- **LDOS** - Residual sentences repeating superseded claims: "four consecutive" raises (bull 1, section 5), "high-single-digit EPS growth" (bull 2), "2.4 -> Three raises plus one initial guide; guide midpoint +3.0%; 2.2x from 1.5x; base about 4% (Propagation misses; inline markers added. Verdict, scenarios and F25 summary unchanged.)
- **LEN** - "three straight full-year delivery-target cuts" -> Targets: ~85,000 (Dec 2025) to 82-83k (Jun 2026) to 80-81k (Sep 2026) = two cuts (Correction appended; F164 summary already said two cuts.)
- **LEN** - Reverse DCF on FY26 EPS $4.95 (10%, 3%, 10 yrs): implied 4.6% vs base 5.7%, implied_vs_base = below -> 4.63% reproduces, but EPS is treated as distributable cash. TTM FCF ~$717M gives ~11%; P/B-ROE needs a sustained ROE ~9.4% (10% Ke) vs ~5.5% FY26E and ~7% base. Restated to "above" (Method error (earnings treated as cash). implied_vs_base below to above; verdict WATCH unchanged; F164 updated.)

## Other notes

- KMB, KMI, KO, KR, KVUE, L, LHX: every quoted guidance string, period label, debt/cash figure and scenario return checked against the primary filing; no FAIL except KVUE (organic-growth streak). Mechanical-check leads (KLAC stale XBRL, KMB Kenvue net income, KMI debt tag and 2025 budget, KO derived TTM, L CNA scope, LDOS) resolved as false positives or already-labelled scope differences.
- Method (rule e): in KMB, KMI, KO, KR, KVUE, L, LHX and KLAC the discount rate is not stated as the 5.17% Treasury plus an equity risk premium (implied premiums 2.3-4.8 points) and FCF does not deduct SBC in KLAC, KMB, KR, KVUE. Recomputed sensitivities are in the JSON; none flips an implied_vs_base call. LEN is the only method FAIL (EPS used as cash).
- LDOS: DVH5 (2026-10-06) corrections independently re-verified; five residual sentences that repeated superseded claims were marked.
