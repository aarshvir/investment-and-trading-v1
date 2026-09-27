# The Progressive Corporation (PGR) — Diligence Dossier

**Agent:** F23 | **As of:** 2026-09-25 close ($205.50) | **Depth:** Standard

## 1. Verdict
**INCLUDE** (12–36 month horizon). Best-in-class, transparently-disclosed (monthly!) auto insurer with a
combined ratio that has stayed comfortably under its own 96 target every month of the last year bar one
disclosed, non-recurring, regulatory item, at a valuation that does not require its current exceptional
returns to persist.

## 2. Business in plain English
Progressive is the largest direct/independent-agent personal auto insurer in the US, plus a growing
commercial-auto and property (home/renters) book. It underwrites, prices with granular telematics/data,
and invests the "float" between collecting premiums and paying claims. Its edge is pricing precision and
low-cost distribution (direct + agency), which lets it grow policies while keeping loss ratios low.

## 3. Why the model likes it — durable or artefact?
Triage (Q06, sourced to `data/triage_cards.csv`) correctly caught that the vendor data card's "NTM P/E 0.3x"
and "+4,978% EPS growth" fields are garbage and fell back to trailing P/E (10.3x) and 34.9% ROE (both per
`data/d4_live_snapshot.parquet`, 2026-09-25 snapshot). **Confirmed and extended**: d4's own
`pe_ntm`/`eps_ntm` fields for PGR are still corrupted in this run (pe_ntm=0.27, eps_ntm=$747.86, eps_fy1
implied +5,395% growth) — this is a live, reproducible data-quality defect in the pipeline, not a one-off,
and should not be used for PGR under any circumstance. Trailing P/E (10.3x, per d4) and the combined-ratio
data below are clean SEC-sourced primary numbers and are what the rest of this dossier relies on.

## 4. Last 4 quarters, GAAP (SEC 8-K Item 2.02 monthly/quarterly releases; PGR reports no non-GAAP EPS)

| Quarter | Net premiums earned ($M) | YoY | Net income ($M) | Diluted EPS | Combined ratio | YoY Δ pts |
|---|---|---|---|---|---|---|
| 3Q25 (Jul–Sep) | 20,849 | +14% | 2,615 | $4.45 | 89.5 | +0.5 |
| 4Q25 (Oct–Dec) | 21,093 | +10% | 2,951 | $5.02 | 88.0 | +0.1 |
| 1Q26 (Jan–Mar) | 20,968 | +8% | 2,818 | $4.80 | 86.4 | -2.1 |
| 2Q26 (Apr–Jun) | 21,573 | +6% | 3,311 | $5.67 | 87.3 | +1.1 |

Note: the *September 2025 single month* combined ratio spiked to 100.4 (from 93.4) — this drove headline
alarm in some data feeds, but the **quarterly** figure (89.5) shows it was almost fully absorbed within the
quarter. Cause, confirmed from the filing (see §6): a one-time $950M Florida "policyholder credit" accrual,
not a deterioration in underwriting. Premium growth is decelerating each quarter (+14%→+10%→+8%→+6% YoY, per the four quarterly earnings
releases cited in §12) as 2023–24's large rate increases lap; this is the main trend to monitor, not the
combined ratio. Policies in force (companywide, per the same releases): 38.08M (3Q25) → 38.62M (4Q25) →
39.57M (1Q26) → 40.09M (2Q26), +7% YoY, still growing across every product line.

## 5. Guidance track record
PGR gives no forward EPS/premium guidance (industry norm for the monthly-disclosure model it uses instead);
its one standing public target is a **combined ratio at or below 96** and a debt-to-total-capital ratio
**below 30%**, both self-imposed policy ceilings, not consensus estimates. Both have been met every period
reviewed (combined ratio 86.4–89.5 quarterly; debt/total-capital 17.5–19.6%, §6).

## 6. Earnings quality & balance sheet
- **The Florida policyholder credit (the key adverse fact this diligence surfaced):** Florida law caps the
  three-calendar-year profit an auto insurer group can earn on Florida personal-auto business; if the cap is
  breached, the excess must be refunded to all Florida policyholders active at the measurement date. Because
  Progressive's Florida book has been *very* profitable, it accrued a **$950M policyholder credit expense**
  in September 2025 — its current estimate of the profit above the cap for the three years ending
  2025-12-31 — payable to ~2.7M Florida policyholders in early 2026 (10-Q, Note; confirmed in the Q3'25
  earnings release "Monthly Commentary"). This is disclosed, one-time, and a direct consequence of *too much*
  underwriting profit in one state, not a quality problem — but it establishes that very strong Florida
  profitability can recur and trigger further credits in future 3-year windows; I treat it as a real,
  measurable, state-specific tail risk (kill criterion #4 below), not noise to ignore.
- **Capital structure:** total capital (debt + equity) $42.7bn at 2026-06-30 vs $37.2bn at 2025-12-31, the
  increase mostly organic (H1'26 comprehensive income $5.2bn) plus a $1.5bn senior-notes issuance in 1Q26.
  Debt-to-total-capital 19.6% (2Q26), up from 17.5% (2Q25) but still well inside the firm's own <30% ceiling.
  No rating/credit-trigger covenants on existing debt (10-Q).
  Equity: $34.33bn (2Q26) vs $30.32bn (4Q25) vs $28.95bn (1Q25) — up sharply on retained earnings plus
  unrealized bond gains.
- **Litigation (10-Q, Legal Proceedings):** PGR and/or subsidiaries are defendants in multi-state class
  actions alleging improper valuation of total-loss vehicles via a "negotiation adjustment" — classes
  already certified in three states, similar suits pending in others. This is an industry-wide, recurring
  litigation category (not unique to PGR) but is open and not yet resolved company-wide.
- **ROE:** TTM net income (sum of the four quarters above) ≈$11.7bn on average equity ≈$32bn → **~36% TTM
  ROE**, matching the triage's 34.9% figure and confirming it, not overturning it.

## 7. Valuation
No V1 systematic valuation row exists for PGR (not in the 92-name V1 universe) — **v1_verdict: null**.
Book value per share ≈$58.9 (2Q26 equity $34.33bn ÷ 583.1M diluted shares) → **P/B ≈3.49x** at $205.50.
Reverse-engineered via justified-P/B (rf 5.17%, ERP 4.14%; PGR's own single-stock beta of 0.26 in the live
snapshot looks too low to be a reliable cost-of-equity input for a single insurer, so I instead use ~7.5%,
in line with where the V1 model places comparable P&C insurers TRV/ALL/CB, 7.6–7.8%; g=3%): the current
3.49x P/B requires a sustained **~18.7% ROE** in perpetuity. Delivered TTM ROE (~36%) and even a generously
conservative "reversion" scenario (a return to the more typical high-teens/low-20s ROE the personal-auto
hard-market cycle has produced historically) clear that bar comfortably. dossier_view: **cheap** — the
market is pricing in a large fade in profitability that the disclosed trend (combined ratio 86–90, premium
growth still positive though decelerating) does not yet support.

## 8. Bull case / Bear case
**Bull:** (1) combined ratio has stayed 86.4–89.5 every quarter for a year, ~7–10 points of cushion to the
96 target; (2) policies in force growing +7% YoY across every segment simultaneously (agency, direct,
special lines, property, commercial); (3) debt/total-capital of just 19.6% leaves headroom to the 30%
policy ceiling for further buybacks or bolt-on growth.
**Bear:** (1) premium growth has decelerated every quarter for a year (+14%→+6% YoY) as 2023–24 rate hikes
lap — if this continues past a normal "growth normalization" into an actual competitive rate war, combined
ratio could rise quickly, as the industry's 2021–22 experience showed is possible; (2) the Florida
profit-cap mechanism is a real, quantifiable, recurring state-regulatory risk that could reduce reported
profit again; (3) multi-state total-loss-valuation class actions (classes already certified in three
states) are an open, uncapped legal exposure.

## 9. Kill criteria
1. Quarterly GAAP combined ratio above 96 (the company's own ceiling) for two consecutive quarters.
2. Net premiums earned growth turns negative YoY for two consecutive quarters.
3. Companywide policies-in-force growth turns negative YoY.
4. A second state imposes a profit-cap policyholder-credit resulting in a single-quarter charge >$500M.
5. Debt-to-total-capital ratio exceeds the company's own 30% policy ceiling.

## 10. Catalysts & calendar
PGR reports monthly (typically mid-month for the prior month) and a fuller quarterly release the same day
as the third month of each quarter. Next quarterly release: ~2026-10-15 (Q3'26, estimated from the identical
prior-year filing date; not yet announced). Florida policyholder credits are expected to be paid out to
~2.7M policyholders in early 2026 per the company's own disclosure (a cash, not P&L, event by then).

## 11. Red-flag scan
No going-concern language, material weakness or restatement found in the reviewed 10-Q. Open items: the
Florida policyholder-credit mechanism (recurring risk, not resolved — it resets each 3-year window) and the
multi-state total-loss-valuation class actions (§6, §8). No auditor change noted.

## 12. Sources
1. SEC EDGAR submissions/companyfacts, CIK 0000080661 (data.sec.gov), retrieved 2026-09-26.
2. PGR 10-Q for the period ended 2026-06-30, filed 2026-08-03 (accession 0000080661-26-000308).
3. PGR "September Results" (Q3'25) earnings release, filed 2025-10-15 (accession 0000080661-25-000126).
4. PGR "December Results" (Q4/FY25) earnings release, filed 2026-01-28 (accession 0000080661-26-000071).
5. PGR "March Results" (Q1'26) earnings release, filed 2026-04-15 (accession 0000080661-26-000173).
6. PGR "June Results" (Q2'26) earnings release, filed 2026-07-15 (accession 0000080661-26-000262).
7. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (2026-09-25 snapshot); v4/outputs/Q06_triage.json.

## Data basis, recency and disclaimer
Most recent period incorporated: 10-Q for quarter ended 2026-06-30 (filed 2026-08-03) and the June 2026
monthly/quarterly earnings release (2026-07-15). Events checked to 2026-09-25. All figures above are GAAP;
PGR does not present a non-GAAP EPS. The d4 live-snapshot pe_ntm/eps_ntm fields for PGR are confirmed
corrupted and were not used anywhere in this valuation. This dossier covers the consolidated entity. Research, not personalised investment advice.
