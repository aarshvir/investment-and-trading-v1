# State Street Corporation (STT) — Diligence Dossier (Agent F93, standard depth)

**1. Verdict: INCLUDE-SMALL (half weight), 12–36 month horizon.** A structurally improving, fee-heavy custody/asset-servicing
franchise with a genuine 2026 inflection in guidance, but roughly half the current NTM valuation is already paid for
that inflection and net-interest income is rate-cycle dependent — size for the reservation, not the story.

**2. Business in plain English.** State Street is a global custodian bank: it safekeeps, administers, and reports on
securities for institutional investors ($57.9tn assets under custody/administration, consolidated, State Street Q2 2026
10-Q, filed 2026-07-30), and runs the State Street Global Advisors (SSGA) asset-management arm ($6.3tn AUM, consolidated,
same source) which includes the SPY ETF franchise. It earns servicing/management fees, FX-trading spreads, securities-
finance income, and net interest income on its deposit/investment book. Competitive position: one of three global
scale custodians (with BNY, JPMorgan), with switching costs from deep operational integration.

**3. Why the model likes it / durability.** b1_live_scores.csv (composite decile 4/10, quintile 3/5, mom_12_1 in the
top decile, sue [earnings surprise] percentile 0.83) — momentum and earnings-surprise driven, not a classic value or
quality screen hit. That is at least partly durable: the Q2 2026 beat was broad-based (fee revenue +17% YoY, NII +18%
YoY, both consolidated income statement, STT Q2 2026 10-Q, filed 2026-07-30) and guidance was raised on both lines, not
a one-off trading quarter. Risk: a large share of the acceleration is NII, which is capital-markets- and rate-path-
dependent, and FX-trading revenue (+25.7% YoY, consolidated) is inherently volatile quarter to quarter.

**4. Last several quarters (consolidated income statement, GAAP; source: STT Q2 2026 10-Q filed 2026-07-30, Q3/Q2 2025
10-Qs, FY2025 10-K filed 2026-02-19).**

| Qtr (consolidated) | Total revenue | YoY | Net income | Diluted EPS | YoY EPS |
|---|---|---|---|---|---|
| Q2 2025 | $3,448m | — | $693m | $2.17 | — |
| Q3 2025 | $3,545m (Q3 total = $10,277m 9mo − $6,732m 6mo) | — | $861m | $2.78 | — |
| FY2025 | $13,944m | — | $2,945m | $9.40 | — |
| Q1 2026 | $3,796m | — | $764m | $2.49 | +14.7% vs Q1'25 est. **[Corrected 2026-10-08: Q1-25 diluted EPS was $2.04 (Q1-26 release), so Q1-26 EPS growth is +22%]** |
| Q2 2026 | $4,048m | **+17.4%** | $1,084m | $3.65 | **+68.2%** |

GAAP throughout; State Street also reports a non-GAAP "operating basis" EPS in its press release that excludes
notable items — this dossier uses GAAP unless labelled otherwise. 1H 2026 revenue $7,844m vs 1H 2025 $6,732m (+16.5%);
1H 2026 diluted EPS $6.14 vs $4.21 (+45.8%). Diluted share count fell from 290.5m (Q2'25) to 281.1m (Q2'26), ~3.2%
buyback-driven reduction, consistent with the EPS growth outrunning net-income growth in some quarters.

**5. Guidance track record (FY2026, consolidated; source: Q2 2026 earnings materials, and searched secondary
coverage of the 2026-07-23 earnings call — Investing.com and Motley Fool transcripts, cross-checked against the two
independent summaries; primary press release not re-opened in this pass, flagged as a limitation).** Per the Q2 2026
release, full-year fee-revenue growth guidance was raised to **12–13%** from a prior **7–9%**; NII growth guidance
raised to **14–15%** from **8–10%**; expense growth guidance raised to **~8%** from **5–6%** (higher revenue-linked
comp and AI/tech investment); management guided to ~500bps of positive operating leverage and a ~32% pre-tax margin.
This is a genuine raise versus the prior range, not an assumed one — but it was **not independently re-verified against
the primary earnings-release PDF/8-K exhibit** in this pass; treat the exact percentages as secondary-sourced pending
that check.

**6. Earnings quality & balance sheet (all consolidated, State Street Corporation; source: Q2 2026 10-Q, filed
2026-07-30).** Consolidated stockholders' equity $28,268m (Jun-2026) vs $27,307m (Jun-2025) vs $27,841m (Dec-2025). Cash and due
from banks $4,290m (Jun-2026) vs $4,433m (Dec-2025) — a small, non-representative slice of a bank's balance sheet;
State Street's real liquidity buffer sits in its investment securities portfolio and Fed/interbank placements, not
disclosed here. **Do not use "net cash provided by operating activities" as a cash-generation metric for a custody
bank** — it swings from −$14.5bn (1H 2026) to +$11.9bn (FY2025) purely from trading/deposit-book timing, not
operating distress; this is a known limitation of applying industrial-company FCF logic to banks (flagged explicitly
per program lessons). Consolidated bank capital ratios (CET1, leverage ratio) were **not pulled in this pass** — a gap; State Street's
own release typically discloses these and they matter more than any cash-flow figure for a bank's dividend/buyback
capacity. **Data gap, flagged, not filled with a guess.**

**7. Valuation vs V1.** No row exists for STT in `v4/outputs/v1_valuation_table.csv` — **v1_verdict: null**, no
systematic reconciliation possible this wave. b1_live_scores.csv (as of 2026-09-25 composite date, but px_actual
$181.34 dated 2026-07-30, i.e. stale by ~2 months) shows mktcap ~$49.8bn. Own reverse-DCF (Section 8) below.

**8. Reverse DCF (own work, simplified 2-stage; treat as directional, not the formal V1 model).** Base: TTM diluted
EPS ≈ FY2025 $9.40 − 1H2025 $4.21 + 1H2026 $6.14 = **$11.33**. At a 25-Sep-2026 close (not independently re-pulled in
this pass; using the b1 stale July mark of $181 as a lower bound and noting the "69% rally" cited in Q04 triage as the
likely driver toward a higher current price), a 16–18x trailing multiple on that TTM EPS implies **~$181–204**. If
current price is materially above $204 (plausible given a 69% YTD rally cited in triage), the market is pricing
continued double-digit EPS growth for several years — i.e. the priced-in growth is **at or above** a reasonable base
case (mid-single-digit-to-low-teens EPS CAGR for a mature custodian bank once the 2026 guidance-raise cycle
normalizes). **valuation_view_vs_v1.implied_vs_base = "in_line"** is the honest call only if price sits near the
$181–204 band; if price has run further, it should be "above." This dossier could not re-confirm the exact 25-Sep-2026
close in this pass — **flagged limitation**, next agent/lead should re-price before finalizing weight. **[Corrected 2026-10-08: method replaced: bank valuation should be P/TBV-ROTCE, not a trailing P/E band; corrected view is in_line (borderline), implied ROTCE about 24.5% - see Correction section]**

**9. Bull case.** (i) Fee-revenue and NII guidance both raised meaningfully in one quarter — real operating leverage,
not just a beat. (ii) Record AUM/AUC scale ($6.3tn / $57.9tn) reinforces switching-cost moat. (iii) Consistent buybacks
shrinking the share count (290.5m→281.1m diluted YoY) on top of EPS growth.

**Bear case.** (i) NII guidance is rate-cycle and balance-sheet-mix dependent; a dovish Fed pivot or securities-book
repricing could reverse the raise quickly. (ii) FX-trading and securities-finance revenue are volatile line items that
drove a chunk of the beat and may not repeat. (iii) Valuation has already re-rated hard (per triage's cited 69%
rally); most of the "surprise" may now be priced.

**9b. Kill criteria (measurable).**
1. Fee revenue growth (consolidated, YoY) falls below 6% for two consecutive quarters (below even the pre-raise low end).
2. NII growth (consolidated, YoY) turns negative for one quarter.
3. Expense growth (consolidated) exceeds revenue growth for two consecutive quarters (negative operating leverage).
4. Diluted share count stops declining sequentially for two consecutive quarters (buyback pace materially cut).
5. Any consolidated-bank CET1/Tier-1 capital ratio breach or regulatory capital action (not verified this pass; monitor upon next filing).

**10. Catalysts & calendar.** Next quarterly release: expected mid/late-October 2026 (Q3 2026; not confirmed against
an 8-K date in this pass — **flagged, verify before trade**). No pending M&A or lock-ups identified in the 8-K list
reviewed (filings through 2026-09-14, an item 8.01/other 8-K not read in detail — **limitation**).

**11. Red-flag scan.** No auditor change, restatement, or going-concern language identified from the filing index
reviewed (10-K/10-Q/8-K list through Sep-2026). No SEC/DOJ investigation or short-seller report found in this pass's
web search. Not exhaustive — Form 4 insider-selling pattern and litigation footnotes were **not read** this pass
(time-boxed); flagged as an open item for the next reviewer.

**12. Sources.**
1. State Street Corp, 10-Q for Q2 2026 (period 2026-06-30), filed 2026-07-30, accession 0000093751-26-000397, SEC EDGAR.
2. State Street Corp, 10-Q for Q2 2025 (period 2025-06-30), filed 2025-07-31, accession 0000093751-25-000425 (via companyfacts XBRL), SEC EDGAR.
3. State Street Corp, 10-K FY2025, filed 2026-02-19, accession 0000093751-26-000124, SEC EDGAR.
4. SEC EDGAR companyfacts API, CIK0000093751, retrieved 2026-09-27.
5. Investing.com, "State Street Q2 2026 slides: record results drive guidance raise," and Motley Fool Q2 2026 earnings-call transcript (secondary; guidance percentages not independently re-verified against the primary release in this pass).
6. `v4/data/b1_live_scores.csv` (as_of 2026-09-25, px_actual dated 2026-07-30).
7. `v4/outputs/v1_valuation_table.csv` — no STT row found.

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period ended 2026-06-30), State Street 10-Q filed 2026-07-30. Events
checked to: guidance/news search run 2026-09-27 (session date), but the exact 25-Sep-2026 closing price and capital
ratios were **not independently re-confirmed** in this pass — flagged limitation, not filled with a guess. GAAP figures
used throughout unless labelled "operating basis" (non-GAAP, mentioned but not substituted). Research, not personal
investment advice.

## Correction (verification DV38, 2026-10-08)

**Verifier:** DV38. **Sources:** 8-K Ex-99.1 / Ex-99.3 acc 0000093751-26-000387 (Q2-26 release and presentation, 16 Jul 2026); Q1-26 release acc 0000093751-26-000184; 10-Q acc 0000093751-26-000397; companyfacts CIK 93751; d4 snapshot (market cap $49.8bn, 274.7m shares); 10-year Treasury 5.17%.

**1. Q1-26 EPS growth (FAIL).** Wrong: "+14.7% vs Q1'25 est." Correct: Q1-25 diluted EPS was $2.04 (Q1-26 release; also 1H25 $4.21 less Q2-25 $2.17), so $2.49 is +22%. Does not affect the verdict.

**2. Valuation method (FAIL) - conclusion survives.** Wrong: a trailing-P/E band (16-18x on TTM EPS $11.33 = $181-204) is not a valuation method for a bank, and no 25 Sep price was confirmed. Correct method (P/TBV-ROTCE): common equity $28,268m less preferred $3,559m = $24,709m; less goodwill $8,106m and intangibles $816m = tangible common equity about $15,787m = about $57.5 per share on 274.7m shares. At about $181.3 (d4 market cap / shares) P/TBV is about 3.15x. With Ke = 5.17% + Blume beta 1.28 x 4.14% = about 10.5% and g = 4%, the implied sustainable ROTCE = 3.15 x 6.5% + 4% = **about 24.5%**, versus FY25 19.6%, 1H26 22.8% ex-notables, Q2-26 25.5% and the company's medium-term target of "mid-20s" ROTCE (35% pre-tax margin). The price therefore needs the full medium-term target delivered with no margin of safety. On the raw beta of 1.42 (Ke 12.3%) it would read above. **implied_vs_base = in_line (borderline)**, dossier_view = fair, matching the F93 summary; INCLUDE-SMALL is retained. F93 summary scenarios (-5% / +9% / +18%) were re-derived (bear about -3.6%, base about +9.4%, bull about +19%) and kept; they are absent from this dossier's body.

**3. Gaps filled / minor.** (a) The guidance percentages that the dossier called secondary-sourced are verified in the primary Ex-99.3 slide 12: fee revenue +12-13% (prior 7-9%), NII +14-15% (prior 8-10%), expenses ~+8% (prior 5-6%), ~500bps operating leverage. (b) The Q2 release and call are dated 16 Jul 2026, not 23 Jul (the 23 Jul 8-K is an unrelated 8.01). (c) The "~32% pre-tax margin" is not a stated target; 2026 YTD ex-notables pre-tax margin is 31.7%. (d) Capital ratios (not pulled originally): CET1 10.8% (standardized), Tier 1 leverage 5.3%, LCR 107%, no breach. (e) 25 Sep 2026 close is still not independently confirmable (UNVERIFIABLE).

**Verified without change:** Q2-26 revenue $4,048m (+17.4%), NI $1,084m, EPS $3.65 (+68.2%; +44% ex-notables); Q3-25 $3,545m / $861m / $2.78; FY25 $13,944m / $2,945m / $9.40; 1H26 revenue $7,844m vs $6,732m; diluted shares 281.1m vs 290.5m; equity $28,268m; cash and due from banks $4,290m; AUC/A $57.9tn; AUM $6.3tn.
