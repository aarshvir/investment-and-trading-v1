# DV21 verification, 8 Oct 2026

Scope: HPE, HPQ, HRL, HSIC, HSY, HUBB, HUM, HWM, IBKR, IBM. Research only; not personal advice. Full table: `DV21_factcheck.json` (80 facts: 47 PASS, 14 MINOR, 19 FAIL, 0 UNVERIFIABLE).

Valuation re-tests used the programme parameters: 10-year Treasury 5.17% (25 Sep 2026), equity risk premium 4.14%, Blume-adjusted beta (raw beta from `d4_live_snapshot`), ten years of constant growth then 3.0% terminal, equity basis with stock-based compensation deducted. For insurers and brokers a P/B-ROE cross-check was added.

| Ticker | Result | Corrections written |
|---|---|---|
| HPE | All quarterly figures and revenue/EPS guidance pass; FY26 FCF guide was raised to at least $3.75bn at Q3, not reaffirmed at $3.5bn; net debt/EBITDA is ~2.3x on GAAP EBITDA (not 2.0x); reverse DCF used 8.8% Ke, EPS as cash and no SBC | Dossier + F75. Implied restated 9.6% -> 10.9-14.2% vs base ~13%: **below -> in line**; verdict INCLUDE-SMALL unchanged |
| HPQ | All figures, guidance quotes, balance sheet pass (crosstie flag is a false positive); reverse DCF did not deduct SBC | Dossier + F143. Implied -0.1% -> +3.4% (+0.9% at 3% terminal) vs base -1.5%: still above; WATCH unchanged |
| HRL | All pass; reverse DCF did not deduct SBC (minor) | Dossier + F163. Implied -1.7% -> -1.2% (-2.7% at 3% terminal): still below base; INCLUDE-SMALL unchanged |
| HSIC | Guidance narrative says "raised twice" (one raise, one reaffirmation); short-term borrowings "roughly doubled" (+12%); reverse DCF mixed after-interest FCF with an EV, omitted $906M redeemable NCI and SBC | Dossier + F68. Implied 3.8% -> 4.4-5.1%: narrowly below base; INCLUDE-SMALL unchanged |
| HSY | H1 adjusted EPS +28.4% called "at the high end" of a +32.5-35% guide (H2 must grow 37-42%); guide midpoint stale; reverse DCF used EV/7% WACC on after-interest FCF without SBC | Dossier + F68. Implied 1.25% -> -1.6% to +2.6%: still below base; INCLUDE-SMALL unchanged |
| HUBB | **Missed the $3.0bn NSI acquisition (announced 4 May, closed 9 Jun 2026)**; used the 31 Mar balance sheet (net debt ~$1.5bn vs $4,874M at 30 Jun); leverage 3.26x TTM adjusted EBITDA (triage's 3.4x corroborated); GAAP EPS guide was lowered, not raised; FCF conversion used 33.6M instead of 53.1M shares (61%, not 75-80%) | Dossier + F85. Own kill criterion 1 (net debt above $2.5B) fired. **INCLUDE-SMALL -> WATCH** |
| HUM | All pass; benefit-ratio column mixes insurance and consolidated bases; Ke 9.5% vs programme 8.6% | Dossier + F160. Implied 14.6% -> 12.1% vs base ~9%; P/B-ROE needs ~16.9% ROE: still above; WATCH unchanged |
| HWM | All eight quarters, guidance rows, balance sheet and 1.4x leverage pass; Ke 9.0% vs programme 9.8% | Dossier + F146. Implied 17.5% -> 19.6% vs base 11%: still above; WATCH unchanged |
| IBKR | Operating figures pass; public stake in IBG LLC is 26.5% (not ~15-16%); net interest is 55.7% of revenue (not 40-50%); reverse DCF treated EPS as cash (14% payout) at 9% Ke and 4% terminal; scenario returns not reproducible | Dossier + F86. Implied 10.8% -> 15.5% (EPS as cash) to 20-23% (with retention) vs base 12-15%: **below -> above**; scenarios -8/+10/+24% -> -14.4/+4.7/+17.3%. **INCLUDE-SMALL -> WATCH** |
| IBM | All pass (reverse DCF reproduces within rounding at the programme Ke of 8.5%); one minor cash-measure inconsistency in net debt | None |

Verdict changes: HUBB INCLUDE-SMALL -> WATCH (own kill criterion fired after a debt-funded acquisition the dossier missed); IBKR INCLUDE-SMALL -> WATCH (valuation premise reverses once Ke, terminal growth and retention are corrected). HPE implied_vs_base changes from below to in line with the verdict unchanged. Both verdict changes rest on judgement thresholds the owner may wish to review: HUBB at 3.26x reported / ~2.9x pro forma leverage, IBKR at the retention assumption (ROE 20-30%); even the most favourable method (EPS as cash) leaves IBKR's implied growth at the top of its base range.

Notes: Hubbell's Q2 2026 10-Q is still not in SEC companyfacts on 8 Oct 2026, so its June balance sheet comes from the Ex-99.1 release. Original dossier text was never deleted; each corrected sentence carries an inline `[Corrected 2026-10-08: ...]` tag and each corrected dossier ends with a `## Correction (verification DV21, 2026-10-08)` section.
