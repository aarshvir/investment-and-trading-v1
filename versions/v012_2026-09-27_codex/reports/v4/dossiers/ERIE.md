# ERIE — Erie Indemnity Company — Diligence Dossier (F97, Wave 6)

## 1. Verdict
**INCLUDE-SMALL** (half weight) — an exceptional, asset-light, no-debt, ~25%-fee management-services franchise on the Erie Insurance Exchange, fairly priced (not cheap) on a reverse-DCF sense-check, with a real and **currently escalating** legal challenge to the management-fee model itself as the named reservation. Thesis horizon: 24–36 months, contingent on litigation resolution.

## 2. Business in plain English
Erie Indemnity does not underwrite insurance risk itself. It is the attorney-in-fact that manages Erie Insurance Exchange (a policyholder-owned reciprocal) — issuing policies, handling renewals and administration — in exchange for a management fee capped at 25% of the Exchange's direct and affiliated assumed written premium (set by Pennsylvania insurance regulation). Because it carries none of the underwriting/reserve risk, its earnings are a clean, high-margin call option on the Exchange's premium growth.

## 3. Why the model likes it / is it durable?
Quant flags: `financial=True` (financial-sector classification), extraordinary ROE percentile (0.98) and gp/assets percentile (0.84), but **no composite score** is computed (`coverage_flag = insufficient_families_no_composite` in b1_live_scores.csv — momentum/value families have too few comparable inputs for this business model). This is durable in the sense that the fee-cap-on-premium-growth model has compounded for a century, but the Q05 triage's own red flag — the Stephenson subscriber suit over the management fee — is not an artefact; it is a direct legal challenge to the durability of the moat itself, and (see §11) it escalated materially since the triage was written.

## 4. Last two quarters (GAAP, consolidated; source: 10-Q filed 2026-07-30, period 2026-06-30)
| ($000s) | Q2 2026 | Q2 2025 | Δ | H1 2026 | H1 2025 | Δ |
|---|---|---|---|---|---|---|
| Operating income (fee ops) | $204,123 | $199,173 | +2.5% | $370,910 | $350,549 | +5.8% |
| Net investment income | $22,553 | $19,600 | +15.1% | $44,672 | $39,136 | +14.1% |
| Income before taxes | $228,077 | $220,747 | +3.3% | $418,403 | $395,493 | +5.8% |
| Net income | $180,294 | $174,685 | +3.2% | $330,768 | $313,102 | +5.6% |
| Diluted EPS | $3.45 | $3.34 | +3.3% | $6.32 | $5.99 | +5.5% |

Q1 2026 diluted EPS was $2.87 (H1 $6.32 − Q2 $3.45). Management-fee revenue (policy issuance/renewal) grew +4.7% YoY in Q2 2026 and +4.5% YoY in H1 2026 — steady, not accelerating or decelerating materially (earnings release, EX-99.1, filed 2026-07-30). Commission expense rose faster than fee revenue in Q2 (+$44.7M) due to higher agent incentive compensation, a margin item worth watching but not yet a trend break (operating income still grew 2.5–5.8%).

## 5. Guidance track record
Erie Indemnity does not issue formal EPS/revenue guidance (confirmed: no numeric outlook found in the Q2 2026 release). Fee revenue growth is mechanically tied to the Exchange's direct/affiliated written premium growth, which the release attributes qualitatively to "growth in direct and affiliated assumed written premium" — no specific premium-growth figure was disclosed in the exhibit reviewed.

## 6. Earnings quality & balance sheet (consolidated; source: 10-Q R4/R8.htm, period 2026-06-30 vs. 2025-12-31)
- **Balance sheet is genuinely asset-light and unlevered:** Total assets $3,557.0M (Jun-26) vs. $3,355.5M (Dec-25); Total liabilities $1,089.9M (mostly commissions payable $457.2M and agent incentive compensation $116.6M — operating liabilities, not debt); **no funded debt/notes payable line exists on the balance sheet.** Total shareholders' equity $2,467.1M vs. $2,283.4M.
- **FCF conversion:** near-total — the fee model has minimal capex/working-capital drag; H1 2026 dividends paid $136.2M vs. H1 2025 $127.1M (+7.2%), funded comfortably from a $330.8M H1 net income (41% payout ratio).
- **ROE:** ~24.8% per the Q05 triage's characterization (not independently re-derived this cycle from a full DuPont breakdown — treat as approximately confirmed, not re-verified line-by-line, given time budget).
- **Related-party structure:** the entire revenue base depends on continued good relations with, and continued premium growth at, a separate legal entity (the Exchange) that ERIE does not own — a structural concentration that is unusual for an "asset-light compounder" framing and is the underlying vulnerability the Stephenson litigation targets.

## 7. Valuation snapshot & reverse DCF
- Price (2026-09-25 close): **$222.86**. TTM net income (FY2025 $559.335M − H1'25 $313.102M + H1'26 $330.768M) = $577.0M ÷ ~52.26M diluted shares (from Q2'26 NI/EPS) = **TTM EPS ≈ $11.04** ⇒ TTM P/E ≈ **20.2x** — matches the Q05 triage's "20.2x trailing" figure, a useful internal cross-check that passed.
- Annualized dividend (2×H1'26 paid ÷ ~52.3M shares) ≈ $5.21/share ⇒ dividend yield ≈ **2.3%**.
*(Basis note: the TTM build above combines FY2025 total net income $559.3M (10-K, filed 2026-02-23), less H1 2025 $313.1M and plus H1 2026 $330.8M — both from the same "Net income" line, consolidated, per the 10-Q Statements of Operations; these are prior-period components of an arithmetic roll-forward, not the same figure as the single-quarter Q2 2026 net income of $180.3M shown in §4.)*
- **Reverse DCF (dividend Gordon-growth sense-check):** at an assumed cost of equity r = 8.0% (assumption: asset-light fee business, low operating leverage risk but real legal-tail risk — analyst estimate, not a filed WACC), implied perpetual growth **g ≈ 8.0% − 2.3% = 5.7%**, which is **in line** with the ~5–6% fee/EPS growth actually delivered in H1 2026 (implied_vs_base = in_line). **The stock is fairly priced, not cheap** — there is little valuation cushion if the litigation outcome is adverse.
- No V1 systematic valuation row exists for ERIE in `v1_valuation_table.csv` (checked — absent); v1_verdict = null.

## 8. Bull / Bear
**Bull:** (1) the fee-cap model has survived multiple prior legal challenges (Beltz, Ritz, both dismissed) intact; (2) net investment income is growing faster than the fee book (+14–15% YoY) as invested assets compound; (3) zero funded debt gives total balance-sheet flexibility regardless of how litigation resolves.
**Bear:** (1) the Stephenson litigation (see §11) was just **amended and expanded** (June 2026) to challenge the fee for 2020-to-present, after Erie lost at the Third Circuit and the Supreme Court declined to hear its appeal — the tail risk is larger, not smaller, than when the triage was written; (2) commission/agent-incentive expense is growing faster than fee revenue in the latest quarter, a margin risk if it persists; (3) the entire economic model depends on a fee rate (25% cap) set by Pennsylvania insurance regulation, which is itself a political/regulatory tail risk independent of the litigation.

## 9. Kill criteria (measurable)
1. Any court order or settlement that reduces the effective management fee rate below the current ~25% cap, retroactively or prospectively.
2. Management-fee revenue growth (policy issuance + renewal + administrative) falls below 2% YoY for two consecutive quarters (vs. +4.5–4.7% in H1 2026).
3. Commission + non-commission cost of operations grows faster than management-fee revenue for three consecutive quarters (margin compression trend, vs. the mixed Q2 2026 picture).
4. A verdict or settlement in Stephenson (or the amended June 2026 complaint) that establishes actual damages or a refund obligation, of any size.
5. Dividend payout ratio (dividends paid/net income) rises above 60% without a corresponding acceleration in fee growth (vs. ~41% currently) — would signal management pulling forward cash return ahead of a known risk.

## 10. Catalysts & calendar
Next quarterly results: estimated ~2026-10-29 (based on FY2025 cadence: Q3 2025 10-Q filed 2025-10-30); not confirmed in filings reviewed. **Litigation calendar is the dominant near-term catalyst**: the Amended Complaint was filed 2026-06-11 in the Court of Common Pleas of Allegheny County; no trial date or briefing schedule was found in the 10-Q excerpt reviewed — a data gap worth a dedicated legal-docket check before initiating.

## 11. Red-flag scan (primary source, filing itself — not news summaries)
Full litigation history per the Q2 2026 10-Q, Legal Proceedings note (period 2026-06-30, filed 2026-07-30):
- Prior federal litigation (Erie Ins. Exch. v. Erie Indem. Co.) was preliminarily enjoined by the district court (Order, 2024-02-28) under the All Writs Act after the Supreme Court denied Indemnity's own cert petition on jurisdiction (2024-02-26).
- Plaintiffs appealed; the **Third Circuit issued its opinion on 2025-10-14**, concluding the district court "abused its discretion" in granting the injunction, and held the Stephenson plaintiffs were not precluded (by the earlier Ritz/Beltz dismissals) from challenging the management fee for 2019–2020.
- Indemnity's Petition for Reargument (en banc) was filed 2025-10-28 and **denied 2025-11-12**.
- Indemnity's Petition for Writ of Certiorari to SCOTUS was filed 2026-01-12 and **denied 2026-03-23**.
- Indemnity **voluntarily dismissed** the federal action on 2026-04-27.
- **An Amended Complaint was filed 2026-06-11** in the Court of Common Pleas of Allegheny County, adding two new plaintiffs (Rosemarie Perrotta, Rachel Stewart) and **expanding the challenged period to calendar years 2020-to-present** (previously just 2019–2020). Indemnity states it "intends to vigorously defend."
- This is a materially more current and more adverse picture than the Q05 triage's characterization ("3rd Circuit revived... SCOTUS declined to review, so the case proceeds") — the triage was accurate as of its own cutoff, but the case has since moved to state court and the plaintiffs' scope has **grown**, which this dossier surfaces as the key update.
- No auditor changes, no material weakness, no going-concern language, no restatement found in the Q2 2026 10-Q.

## 12. Sources
1. SEC EDGAR, Erie Indemnity 10-Q, period 2026-06-30, filed 2026-07-30, accession 0001628280-26-051079 (Statements of Financial Position R4.htm, Cash Flows R8.htm, Item 3/Legal Proceedings, full text — including the Stephenson litigation history quoted verbatim from the filing).
2. SEC EDGAR, Erie Indemnity 8-K Ex-99.1, "Erie Indemnity Reports Second Quarter 2026 Results," filed 2026-07-30, accession 0001628280-26-051071.
3. SEC EDGAR, XBRL company facts API, CIK0000922621, retrieved 2026-09-27.
4. `v4/data/b1_live_scores.csv` (price $222.86 as of 2026-09-25; `coverage_flag = insufficient_families_no_composite`); `v4/outputs/Q05_triage.json` (prior triage call and its Oct-2025-dated litigation summary, now superseded by §11); `v4/outputs/v1_valuation_table.csv` (checked — no ERIE row).

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period end 2026-06-30), 10-Q filed 2026-07-30. Checked for events to 2026-09-25 via the SEC submissions feed; no filing more recent than the Q2 2026 10-Q/8-K was found on record as of the pull date — no confirmed post-2026-06-11 update on the Amended Complaint's docket status (a dedicated Allegheny County court-docket check was out of scope this cycle; flagged as the single highest-priority follow-up). All figures are GAAP; ERIE does not report a non-GAAP adjusted EPS. Research, not personal investment advice.
