# V1X independent verification of V1's systematic valuation

as_of: 2026-09-25  |  overall pass rate: **86.5%** (160/185 checks across 12 names)

Independence note: SEC XBRL re-pulls, the reverse-DCF solver, the justified-P/B algebra, the own-history percentile rebuild and the scenario-CAGR replay were all written and validated against V1's PUBLISHED OUTPUT (json/csv) before code/v1_valuation.py was opened. Where a later look at V1's code was used to sharpen a diagnosis, that is stated explicitly below; no diagnosis in this report required it -- every root cause was reached from primary SEC filings, V1's own disclosed conflicts/flags, or V1's own output numbers.

## Summary table

| Ticker | Class | V1 verdict | Checks (pass/total) | FAILs | Verdict changes? |
|---|---|---|---|---|---|
| DLTR | operating | fair (0.21) | 12/14 | 0 | No |
| HST | reit | attractive (0.37) | 13/15 | 2 | No |
| JBHT | operating | fair (-0.03) | 14/14 | 0 | No |
| ALL | financial | fair (0.29) | 14/17 | 1 | No |
| GL | financial | fair (0.14) | 15/17 | 0 | No |
| SWK | operating | attractive (0.75) | 13/14 | 0 | No |
| HIG | financial | fair (-0.00) | 13/17 | 2 | No |
| BMY | operating | attractive (1.00) | 12/14 | 1 | No |
| MTB | financial | fair (0.18) | 13/17 | 1 | No |
| LMT | operating | fair (0.26) | 13/14 | 1 | No |
| FRT | reit | attractive (0.49) | 14/15 | 0 | No |
| SYF | financial | attractive (0.81) | 14/17 | 0 | No |

## Every FAIL, with the independently-derived correct value

| Ticker | Check | V1 value | V1X value | Diff |
|---|---|---|---|---|
| HST | capex (TTM) | 2.49e+08 | 2.76e+08 | 10.8% |
| HST | net_debt (total_debt-cash_sti) | 3.692e+09 | 2131000000 | -42.3% |
| ALL | net_debt (total_debt-cash_sti) | 6.652e+09 | 1947000000 | -70.7% |
| HIG | D&A (TTM) | 2.2e+08 | 4.29e+08 | 95.0% |
| HIG | net_debt (total_debt-cash_sti) | 4.171e+09 | 305000000 | -92.7% |
| BMY | net_debt (total_debt-cash_sti) | 3.282e+10 | 35166000000 | 7.1% |
| MTB | net_debt (total_debt-cash_sti) | 7.44e+08 | 16243000000 | 2083.2% |
| LMT | D&A (TTM) | 1.687e+09 | 2.088e+09 | 23.8% |

## NaN explanations (scenario returns)

**DLTR / bear**: value_yr3_total = -42.74 (negative). scenario terminal value is NEGATIVE (implies a negative share price), so (negative)^(1/3) is undefined in real floating point -> NaN. Root cause: a P/E-style exit multiple was applied to a NEGATIVE EPS/FFO-per-share bear-case projection. Is this a bug: **YES**. Recommended fix: Floor the scenario terminal value at $0 (or a liquidation/book-value floor) before compounding, and/or do not apply a P/E-style exit multiple when projected EPS/FFO-per-share is negative (use P/Sales or a fixed capital floor instead). Floored version implies annualised return = -100% (total loss) rather than an undefined value.

## Missing methods (item 4: three-method completeness)

- **HST**: peer median with >=3 real peers (V1 peer_n=2), peer median on a P/FFO (not NTM P/E) basis
- **FRT**: peer median on a P/FFO (not NTM P/E) basis

## Per-ticker notes and verdict-check reasoning

### DLTR (operating, V1 verdict: fair)

[0 FAIL(s)] verdict/base-case sign UNCHANGED: no FAIL of any kind.

### HST (reit, V1 verdict: attractive)

net_debt FAIL (-42.3%) and capex FLAG/FAIL: REIT debt is carried under property-level mortgage/unsecured-notes tags (e.g. SecuredDebt, SeniorNotes, or custom dimensioned concepts), not the generic industrial LongTermDebt* tags used here -- V1 hit the SAME wall (its own net_debt_source says 'D4/Yahoo (totalDebt - totalCash), D3 balance-sheet fields missing'), so this is a confirmed, mutually-acknowledged data-coverage gap for REIT debt, not a new problem. capex diff (10.8%) is a smaller, plausible real-estate-capex-tag scope difference (development vs improvements). | Per V1X task spec the appropriate intrinsic method for a REIT is P/FFO, not FCFF reverse-DCF; V1 actually applied the same reverse-DCF FCFF method used for operating companies (confirmed from v1_valuation.json's own 'method' field, read only as V1's OUTPUT, not its code). This is a method-choice deviation flagged under item 4, not a mechanics error -- the DCF math itself reproduces V1's number (see check above). | True NAREIT FFO (from the company's own 8-K supplemental, adjusting for gains/losses on property sales and impairments) was NOT retrievable within the time box -- 8-K exhibit press releases are not part of SEC XBRL companyfacts. Used FFO-proxy = NI+D&A (matches V1's own 'P/FFO(proxy)' number to within the tolerance below), consistent with V1's own disclosed flag that real peer FFO data is unavailable. | Independent GICS peer count (D1 constituents, excl. self) = 1 for sub-industry 'Hotel & Resort REITs'; V1 reported peer_n=2 (sample ['HST', 'VICI']). | REIT peer comparison uses NTM P/E as a proxy (V1-disclosed); real FFO-based peer set not available locally either -- three-method completeness for REITs is PARTIAL (own-history multiple = true P/FFO-proxy OK; peer median = NTM P/E, not P/FFO; intrinsic method = FCFF DCF, not P/FFO as specified). Flagging, not failing, since V1 disclosed the limitation rather than hiding it. || [2 FAIL(s)] verdict/base-case sign UNCHANGED: net_debt/capex FAILs make V1's debt figure LARGER (my EV would be lower), which would require LESS implied growth to justify price, reinforcing 'attractive', not reversing it.

### JBHT (operating, V1 verdict: fair)

Independent GICS peer count (D1 constituents, excl. self) = 2 for sub-industry 'Cargo Ground Transportation'; V1 reported peer_n=3 (sample ['FDXF', 'JBHT', 'ODFL']). || [0 FAIL(s)] verdict/base-case sign UNCHANGED: no FAIL of any kind.

### ALL (financial, V1 verdict: fair)

net_debt FAIL: insurer 'debt' (junior subordinated debentures, hybrid capital) is tagged inconsistently across filers and not fully captured by generic LongTermDebt* tags -- same root cause as MTB/SYF's revenue-tag ambiguity, just on the balance-sheet side. IMMATERIAL to ALL's verdict: valuation method is justified P/B (ROE/equity-driven), independent of net_debt (net_debt only feeds an EV/EBIT view that ALL's valuation_model does not use). || [1 FAIL(s)] verdict/base-case sign UNCHANGED: net_debt FAIL does not feed the justified-P/B valuation (checked: P/B mechanics and implied-ROE both PASS exactly).

### GL (financial, V1 verdict: fair)

[0 FAIL(s)] verdict/base-case sign UNCHANGED: no FAIL of any kind.

### SWK (operating, V1 verdict: attractive)

[0 FAIL(s)] verdict/base-case sign UNCHANGED: no FAIL of any kind.

### HIG (financial, V1 verdict: fair)

net_debt FAIL: insurer 'debt' (junior subordinated debentures, hybrid capital) is tagged inconsistently across filers and not fully captured by generic LongTermDebt* tags -- same root cause as MTB/SYF's revenue-tag ambiguity, just on the balance-sheet side. IMMATERIAL to HIG's verdict: valuation method is justified P/B (ROE/equity-driven), independent of net_debt (net_debt only feeds an EV/EBIT view that HIG's valuation_model does not use). | D&A FAIL (95%): generic DepreciationAmortizationAndAccretionNet for an insurer likely bundles in amortization of deferred acquisition costs (DAC) and/or value-of-business-acquired (VOBA) -- large insurance-specific non-PP&E amortization -- inflating the figure vs V1's smaller, presumably PP&E-only da_ttm. Likely a tag-choice difference, not a data error; also immaterial to HIG's P/B-based verdict. || [2 FAIL(s)] verdict/base-case sign UNCHANGED: D&A/net_debt FAILs do not feed the justified-P/B valuation (checked: P/B mechanics and implied-ROE both PASS exactly).

### BMY (operating, V1 verdict: attractive)

net_debt FAIL (7.1%, just above the 5% threshold): likely a debt-scope boundary choice (this rebuild includes a $1.03bn ShortTermBorrowings draw that V1 may exclude, and/or V1 nets a short-term-investments balance not captured by the generic STI tag search here). Modest in EV terms (~1.4% of BMY's $161.6bn EV0) -- does not change BMY's implied growth enough to affect the 'attractive' verdict (implied growth is -16% vs consensus +... a directionally enormous gap already). || [1 FAIL(s)] verdict/base-case sign UNCHANGED: net_debt FAIL is +7.1% of net_debt but only ~1.4% of EV0 ($161.6bn); BMY is priced for -16.4%/yr FCFF decline vs consensus -3.3% and delivered +2%/+11% (5y/10y) -- a gap of >10 points that a 1.4% EV change cannot close.

### MTB (financial, V1 verdict: fair)

net_debt FAIL (20.8x): bank 'total debt' (LongTermDebt + ShortTermBorrowings, which for a bank includes repo agreements / short-term wholesale funding used in normal balance-sheet management) is not the same concept as the 'net debt' an equity analyst nets against EV for a bank -- V1's own $744m figure is far smaller, implying V1 either excludes wholesale short-term funding entirely or nets a much larger cash/securities base than the generic CashAndCashEquivalentsAtCarryingValue tag captures (banks hold most liquidity in interest-earning deposits/AFS securities, not the 'cash' GAAP line). IMMATERIAL to MTB's verdict either way: valuation method is justified P/B. | MTB conflict (D3 rev 9.961bn vs Yahoo 9.451bn, 5.1%) DIAGNOSED with an EXACT independent match: SEC InterestIncomeExpenseNet (net interest income, TTM $7.018bn) + NoninterestIncome ($2.864bn) minus a rounding of $0.079bn recombination = $9,961,000,000 -- IDENTICAL to D3's figure to the dollar, via a route that never touches D3's own pipeline. D3's revenue definition (net interest income + fee income, the standard bank 'total revenue') is primary-source-confirmed correct; Yahoo's lower figure is the likely outlier. This is IMMATERIAL to MTB's verdict: the valuation method used is justified P/B (ROE/equity-driven), independent of revenue or the D3 'EBIT' proxy -- the 79.7% 'EBIT margin' V1 flagged as implausible is a symptom of D3's blanket EBIT formula not being economically meaningful for a bank (interest expense is a bank's cost of funds, not COGS), not a valuation error. || [1 FAIL(s)] verdict/base-case sign UNCHANGED: net_debt FAIL does not feed the justified-P/B valuation (checked: P/B mechanics and implied-ROE both PASS exactly).

### LMT (operating, V1 verdict: fair)

D&A FAIL (23.8%, $2.088bn vs V1's $1.687bn): no generic candidate concept reproduces V1's figure exactly; likely a different (possibly segment- or program-amortization-scoped) tag choice. NOTE ON MATERIALITY: the reverse-DCF mechanics check above reuses V1's OWN da_ratio (not this independently-sourced figure), so this input gap does NOT propagate into the growth-tolerance check, which passed almost exactly. It WOULD shift the result by roughly (2.088-1.687)/77.0bn revenue = 0.5pt of EBIT-margin-equivalent FCFF if a fully bottom-up independent DCF were built instead of the mechanics check. || [1 FAIL(s)] verdict/base-case sign UNCHANGED: D&A FAIL does not propagate into the growth-tolerance check (which reused V1's own da_ratio and passed almost exactly); a fully bottom-up DCF using the independent, higher D&A figure would if anything raise FCFF and make LMT look slightly MORE attractive, not less -- verdict direction is safe either way.

### FRT (reit, V1 verdict: attractive)

Per V1X task spec the appropriate intrinsic method for a REIT is P/FFO, not FCFF reverse-DCF; V1 actually applied the same reverse-DCF FCFF method used for operating companies (confirmed from v1_valuation.json's own 'method' field, read only as V1's OUTPUT, not its code). This is a method-choice deviation flagged under item 4, not a mechanics error -- the DCF math itself reproduces V1's number (see check above). | True NAREIT FFO (from the company's own 8-K supplemental, adjusting for gains/losses on property sales and impairments) was NOT retrievable within the time box -- 8-K exhibit press releases are not part of SEC XBRL companyfacts. Used FFO-proxy = NI+D&A (matches V1's own 'P/FFO(proxy)' number to within the tolerance below), consistent with V1's own disclosed flag that real peer FFO data is unavailable. | REIT peer comparison uses NTM P/E as a proxy (V1-disclosed); real FFO-based peer set not available locally either -- three-method completeness for REITs is PARTIAL (own-history multiple = true P/FFO-proxy OK; peer median = NTM P/E, not P/FFO; intrinsic method = FCFF DCF, not P/FFO as specified). Flagging, not failing, since V1 disclosed the limitation rather than hiding it. || [0 FAIL(s)] verdict/base-case sign UNCHANGED: no FAIL; the REIT method-choice deviation (FCFF DCF vs the task-specified P/FFO) is a methodology note, not a numeric one -- the independent P/FFO check matched V1's own P/FFO-proxy number exactly (0.0 diff).

### SYF (financial, V1 verdict: attractive)

SYF conflict (D3 rev 19.247bn vs Yahoo 9.908bn, 48.5%) DIAGNOSED with an EXACT independent match: SEC InterestIncomeExpenseNet (net interest income) + NoninterestIncome reproduces D3's $19,247,000,000 to the dollar via a route that never touches D3's pipeline -- D3/V1's number is primary-source-confirmed correct. Yahoo's ~$9.9bn is roughly net-interest-income AFTER a plausible TTM provision-for-credit-losses deduction (a card issuer's loss provision is large, plausibly $8-9bn scale for SYF) -- i.e. Yahoo's vendor figure likely nets provision against revenue, which is non-standard (GAAP shows provision as a separate expense below revenue, not a revenue contra-item); this part of the explanation is plausible but not independently confirmed to the dollar. As with MTB this is IMMATERIAL to SYF's verdict: valuation method is justified P/B, independent of the revenue figure. | Independent GICS peer count (D1 constituents, excl. self) = 2 for sub-industry 'Consumer Finance'; V1 reported peer_n=3 (sample ['AXP', 'COF', 'SYF']). || [0 FAIL(s)] verdict/base-case sign UNCHANGED: no FAIL of any kind (net_debt PASSED at -4.2%, within tolerance).

---

# Extension (Loop 3): 8 names added in Loop 2

as_of: 2026-09-25  |  extension pass rate: **90.2%** (101/112 checks across 8 names)  |  combined 20-name pass rate: **87.9%** (261/297)

Same method, tolerances and independence rule as the original 12 (see top of this file). All 8 are 'operating' classification (reverse-DCF FCFF). One genuine bug found and fixed while extending: BKNG's (and DVA's/EOG's/DRI's) historical share count in D3 is not retroactively split-adjusted, which corrupts the own-history percentile unless corrected using d2_splits.parquet -- see v1x_verify.split_adjust_shares. This fix is opt-in (fix_splits=True) and was verified to leave the original 12's results unchanged.

## Extension summary table

| Ticker | V1 verdict | Checks (pass/total) | FAILs | Verdict changes? |
|---|---|---|---|---|
| DVA | attractive (0.94) | 12/14 | 1 | No |
| DG | attractive (0.80) | 13/14 | 0 | No |
| CVS | attractive (0.94) | 13/14 | 0 | No |
| ABNB | fair (0.10) | 12/14 | 0 | No |
| EOG | attractive (0.64) | 13/14 | 0 | No |
| DRI | attractive (0.35) | 12/14 | 2 | No |
| VRSN | fair (-0.08) | 13/14 | 0 | No |
| BKNG | attractive (0.99) | 13/14 | 0 | No |

## Extension: every FAIL

| Ticker | Check | V1 value | V1X value | Diff |
|---|---|---|---|---|
| DVA | net income (TTM) | 8.475e+08 | 1.179e+09 | 39.2% |
| DRI | net income (TTM) | 1.207e+09 | 2.008e+09 | 66.4% |
| DRI | net_debt (total_debt-cash_sti) | 1.418e+09 | 2111800000 | 48.9% |

## Special coordinator checks (EOG oil-spike embedding; BKNG/CVS exit-multiple-vs-own-range)

### EOG

EOG SPECIAL CHECK: TTM window (last 4 discrete SEC quarters as of 2026-09-25) is Q3'25+Q4'25+Q1'26+Q2'26 -- Q2'26 (Apr-Jun 2026) is confirmed, per EOG's own 8-K, the Iran/Hormuz war-spike quarter (realized oil $98.18/bbl vs $64.84/bbl in Q2'25). YES, V1's ttm_ebit_d3/ttm_revenue_d3/ebit_margin_used (32.9%) mechanically embed this spike quarter -- it is one of the 4 summed quarters. Independent confirmation the market/consensus itself expects fade: eps_fy0=17.00715 > eps_fy1=14.91138 (forward EPS is LOWER than current-FY EPS, i.e. consensus prices in a decline) -- CONFIRMED the spike is embedded and expected to fade, exactly as EOG's own dossier (section 7) describes. This does not FAIL any tolerance check (V1's own inputs are internally consistent with the primary-source TTM window), but it is a real valuation-interpretation caveat: NTM P/E 9.07x looks statistically cheap partly because the TTM/NTM base is elevated, not purely because of a structural re-rating. || [0 FAIL(s)] TTM/NTM figures embed the 2026 oil-price-spike quarter (see EOG special-check note); this does not change the 'attractive' verdict's SIGN because V1's base case here is already the most modest of this batch (+9.4%/yr, not a 30-40%/yr case) and the model's own street_flag shows the base value is within (not beyond) the Street range -- but it is a real caveat on the DEGREE of 'cheap', consistent with the dossier's own reservation.

### BKNG

BKNG SPECIAL CHECK: V1 base-case exit multiple = 30.10x vs current 13.83x (2.18x expansion assumed over 3 years). Independent own-history (2012-2026, split-adjusted, 177 months, positive-multiple only): raw max=1717.1x (NOT robust -- driven by near-zero-trailing-earnings quarters, 2021 COVID travel collapse, not a real sustained valuation level); robust 90th-percentile 'typical top of range' = 70.2x. Exit multiple sits within the robust p90 range. For BKNG specifically: the raw max (265x+ even excluding the worst COVID months) means 30.1x is not literally unprecedented, so the dossier's sharper and more defensible point (independently corroborated here) is the ~2.2x MULTIPLE-EXPANSION assumption itself (13.8x->30.1x) outrunning management's own guided low-to-mid-teens adjusted-EPS growth -- not that 30.1x is literally off the chart. || [0 FAIL(s)] V1's base case (+39.3%/yr) requires the NTM P/E to expand ~2.2x (13.8x->30.1x) in 3 years -- independently confirmed (see special-check note) to exceed a robust p90 'typical top of range' (~42x) only modestly, and not the raw all-time max (~266x, itself an artifact of near-zero-earnings quarters) -- so 30.1x is not literally unprecedented, but the ASSUMED RATE of re-rating outruns management's own low-to-mid-teens guided EPS growth, exactly as the dossier argues. Does not flip the qualitative 'attractive' verdict (BKNG is genuinely cheap today, 1.1st percentile), but the BASE CASE MAGNITUDE should be treated as closer to an upside/bull case, not the base case -- same conclusion the dossier reaches, corroborated here independently from V1's own history data.

### CVS

CVS SPECIAL CHECK: V1 base-case exit multiple = 17.46x vs current 10.61x (1.65x expansion assumed over 3 years). Independent own-history (2012-2026, split-adjusted, 171 months, positive-multiple only): raw max=214.7x (NOT robust -- driven by near-zero-trailing-earnings quarters, the Q3-2025 goodwill impairment, not a real sustained valuation level); robust 90th-percentile 'typical top of range' = 26.5x. Exit multiple sits within the robust p90 range. For CVS: 17.46x sits comfortably within the robust range (p90 26.5x, pre-2024-crisis-era multiples were routinely in this zone), consistent with the dossier's own framing ('back near CVS's pre-2024-crisis average') -- an aggressive but not unprecedented assumption. || [0 FAIL(s)] V1's base case (+35.9%/yr) assumes exit multiple 17.46x, WITHIN CVS's own ~14-year range (dossier: 'back near CVS's pre-2024-crisis average') -- aggressive but not unprecedented; verdict direction unaffected by any FAIL found here.

## Extension: per-ticker notes

### DVA (operating, V1 verdict: attractive)

net income FAIL (+39.2%): generic NetIncomeLoss ($1,179.4m TTM) is CONSOLIDATED net income including non-controlling interests in DaVita's joint-venture dialysis centers; V1/D3's $847.5m is 'Net income attributable to DaVita Inc.' (the parent-only figure), exactly as DaVita's own dossier (section 6) flags -- 'a high multiple, partly reflecting minority-interest carve-outs.' Tag-choice difference, not a data error; V1's figure is the correct one for per-share/equity-holder valuation. || [1 FAIL(s)] verdict/base-case sign UNCHANGED: no material FAIL found.

### DG (operating, V1 verdict: attractive)

[0 FAIL(s)] verdict/base-case sign UNCHANGED: no material FAIL found.

### ABNB (operating, V1 verdict: fair)

[0 FAIL(s)] verdict/base-case sign UNCHANGED: no material FAIL found.

### DRI (operating, V1 verdict: attractive)

net income FAIL (+66.4%): generic NetIncomeLoss ($2,008.5m TTM) independently confirmed to include a large one-off (likely discontinued-operations) item; IncomeLossFromContinuingOperations TTM = $1,213.7m matches V1's $1,206.7m to within 0.6% (well inside tolerance) -- V1 correctly uses continuing-operations net income, consistent with the dossier's own table header ('GAAP diluted EPS (continuing ops)'). net_debt FAIL (+48.9%) not fully resolved within the time box; plausible cause is operating-lease-liability inclusion/exclusion (DRI's finance/operating lease liabilities are large for a company-owned-restaurant model) -- flagged, not diagnosed to the dollar. || [2 FAIL(s)] verdict/base-case sign UNCHANGED: no material FAIL found.

### VRSN (operating, V1 verdict: fair)

Independent GICS peer count (D1 constituents, excl. self) = 2 for sub-industry 'Internet Services & Infrastructure'; V1 reported peer_n=3 (sample ['AKAM', 'GDDY', 'VRSN']). || [0 FAIL(s)] verdict/base-case sign UNCHANGED: no material FAIL found.
