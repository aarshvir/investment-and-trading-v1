# PNC — The PNC Financial Services Group, Inc.

## 1. Verdict

**INCLUDE-SMALL** (half weight). Thesis horizon: 12–36 months. Reservation: the current quarter's headline growth (GAAP diluted EPS +25% YoY) is flattered by the still-completing FirstBank acquisition and by a large, mostly-offset one-time Visa Class B-2 exchange gain; CET1 has fallen from 10.5% to 9.9% over the past year as the deal was funded, and the durable, ex-one-off earnings-power level needs another 1–2 quarters of clean prints (post-integration, which converted June 22, 2026) before the growth rate can be trusted at face value.

## 2. Business in plain English

PNC is a super-regional US bank holding company — commercial and retail banking, corporate/institutional banking, and asset management — that earns money on the spread between what it pays depositors and what it earns on loans and securities (net interest income), plus fees (capital markets, treasury management, card, wealth). It just closed and integrated an acquisition of FirstBank (Colorado/Arizona, ~780,000 customers, ~95 branches), announced September 2025 for implied consideration of $4.1bn and closed January 5, 2026, materially expanding PNC's Western US retail footprint. Note for the record: the prior triage's one-line thesis ("completed acquisition integration (BBVA USA)") refers to a 2021 deal, not the current one; the acquisition actually driving 2026 results and the current capital-ratio trend is FirstBank, not BBVA USA. This is flagged in the summary JSON's `data_conflicts`.

## 3. Why the model likes it — durable or artefact?

From `b1_live_scores.csv`: PNC's composite is driven almost entirely by **Value** (fam_V 0.771) and **Earnings momentum** (fam_S 0.676), with weak **Quality** (fam_Q 0.051 — the lowest of the three names in this batch, largely because bank balance-sheet items don't map cleanly onto the model's generic Q factors: gp_a and several other Q components are NaN/not meaningful for a depository, per the banks sector playbook's explicit warning that most generic quality ratios are undefined for banks) and a strong **Momentum** score (fam_M 0.711, mom_12_1 ≈ +23%). Composite rank 163/~500 (decile 7) — the best-ranked of the three names in this batch, though still outside the model's live top-30/top-70 cutoffs used for sleeve eligibility elsewhere in this program. The earnings-momentum score is durable in the sense that it is tracking real, filed EPS beats (Section 4); the low "Quality" score is largely a **model-fit artefact** for this sector rather than a genuine quality problem, and should be read in light of the sector-specific metrics in Section 6 instead.

## 4. Last six quarters of results (SEC filings; GAAP unless noted)

Source: quarterly earnings-release exhibits (8-K Ex-99.1), each a primary SEC filing, cross-checked against SEC XBRL where available.

| Period | Revenue ($M) | NII ($M) | Noninterest income ($M) | Net income ($M) | Diluted EPS (GAAP) | Diluted EPS (adjusted, non-GAAP) |
|---|---|---|---|---|---|---|
| Q1 2025 | 5,452 | 3,476 | 1,976 | 1,499 | 3.51 | 3.51 |
| Q2 2025 | 5,661 | 3,555 | 2,106 | 1,643 | 3.85 | 3.85 |
| Q3 2025 | 5,915 | 3,648 | 2,267 | 1,822 | 4.35 | 4.35 |
| Q4 2025 | 6,071 | 3,731 | 2,340 | 2,033 | 4.88 | 4.88 |
| Q1 2026 | 6,165 | 3,961 | 2,204 | 1,772 | 4.13 | 4.32 |
| Q2 2026 | 6,875 | 4,107 | 2,768 | 2,055 | 4.81 | 4.85 |

**YoY, Q2 2026 vs Q2 2025 (per the Q2 2026 earnings release, 8-K Ex-99.1, filed 2026-07-15):** revenue +21%, NII +16%, net income +25%, GAAP diluted EPS +25% ($3.85→$4.81), adjusted diluted EPS +26% ($3.85→$4.85). Per that same release, growth is a blend of (a) the FirstBank acquisition (added since Jan 5, 2026, full quarter benefit from Q2), (b) organic commercial loan growth (average loans +4% QoQ, +12.3bn, per the release), and (c) a one-time $448M gain on the Visa Class B-2/B-3 exchange (per the release's significant-items table), substantially offset by a $140M PNC Foundation contribution, a $139M securities repositioning loss, and $121M of integration costs (all per the same table) — net effect of integration costs plus 2Q26 significant items was **−$0.04/share** (per the release), already excluded from the $4.85 adjusted figure. This is a genuinely strong quarter per the primary filing, but a meaningful share of the YoY delta is inorganic (M&A) rather than same-store growth, and should not be extrapolated at face value.

## 5. Guidance track record

PNC, like most large banks, does not give full-year EPS guidance; it gives qualitative next-quarter/near-term color. From the Q2 2026 release (2026-07-15): "Share repurchase activity in the third quarter of 2026 is expected to approximate second quarter of 2026 share repurchase levels" ($0.6bn) — the only explicit forward-looking quantitative statement identified. No formal guidance was raised, cut, or maintained in the sense the base template asks about, because none is issued; this is stated explicitly rather than left implicit, per the addendum's instruction not to count "no guidance" as a pass or a fail.

## 6. Earnings quality & balance sheet (bank-specific metrics per the banks sector playbook)

- **NIM:** 2.96% (Q2 2026) vs 2.80% (Q2 2025), +16bps YoY — genuine spread expansion, not a one-off.
- **Efficiency ratio:** 60% (Q2 2026) vs 60% (Q2 2025) — flat; the playbook's "42–50% good, 50–60% build-out" bands suggest PNC sits at the upper end of the acceptable range, consistent with ongoing FirstBank integration spend still in the expense base.
- **Credit quality:** net loan charge-offs $226M / 0.25% annualized to average loans (Q2 2026) — well inside the playbook's 0.3–0.6% "normal cycle" band, in fact below it; total nonperforming loans $2.0bn, **down** 10% QoQ; delinquencies $1.4bn, down 8% QoQ; allowance for credit losses/total loans 1.48%, down from 1.62% a year ago (partly organic, partly FirstBank's acquired book carrying its own day-one mark). No evidence of asset-quality deterioration in the two most recent quarters — the opposite, in fact.
- **Capital:** CET1 ratio 9.9% (Q2 2026) vs 10.5% (Q2 2025) and 10.1% (Q1 2026) — a genuine, disclosed decline, driven by funding the FirstBank acquisition and continued buybacks ($0.6bn in Q2 2026 alone) even as the ratio fell. Still comfortably above regulatory minimums, but the trend (down 60bps in one quarter) **[Corrected 2026-10-08: CET1 fell 20bps in the quarter (10.1% to 9.9%); 60bps is the year-on-year fall (10.5% to 9.9%)]** is the single metric most worth watching next quarter.
- **Funding:** average deposits $457.0bn, roughly stable QoQ; noninterest-bearing deposit share grew; rate paid on interest-bearing deposits declined 5bps QoQ — a mildly favorable funding-cost trend.
- **M&A financing:** FirstBank was announced 2025-09-08 for "implied consideration of $4.1 billion" (quoted from the Q3 2025 earnings release); the cash/stock consideration split was not further quantified in the documents pulled for this pass — flagged as a gap; see the original 2025-09-08 8-K for full deal terms if this needs tightening before any capital-allocation decision.
- **Share count:** average diluted shares outstanding rose from 397M (Q2 2025) to 403M (Q2 2026), i.e., net issuance (likely FirstBank-related) outweighed buybacks over the year despite the $0.6–0.7bn/quarter repurchase pace.

## 7. Valuation — V1 reconciliation and reverse DCF

**No V1 row exists for PNC** in `v4/outputs/v1_valuation_table.csv` or `v1_valuation.json` (checked; ticker absent from both). `v1_verdict` is therefore `null`.

**Snapshot (d4_live_snapshot.parquet, as of 2026-09-25 close, price $225.64):** trailing P/E 12.43x, NTM P/E 10.53x, P/B 1.55x, P/TBV 2.03x, ROE (trailing) 12.6%, beta 0.889, analyst mean target $276.58 (20 analysts, "buy" consensus) — an implied 22.6% upside to mean target, matching the triage note.

**Reverse DCF (excess-return / justified-P/B model, own build, per the banks sector playbook's `Justified P/B = (ROE − g)/(COE − g)`):** CAPM cost of equity (rf 4.2%, ERP 5%, PNC beta 0.889 → COE ≈ 8.6%) **[Corrected 2026-10-08: rf was stale; with the 5.17% 10-year Treasury COE is about 9.6% and implied growth is 2.4%-4.4% on P/TBV; see Correction section]**. Using book-value P/B (1.55x) against a normalized ROE band of 13–16%, implied sustainable growth is roughly **0% to +1%**; using tangible-book P/TBV (2.03x) against a normalized ROTCE band of 15–17% (i.e., below the current, one-off-flattered 17.9% headline print), implied growth is roughly **0.5% to 2.5%**. Both are comfortably below any reasonable estimate of PNC's actual medium-term EPS growth capacity (high-single to low-double-digit, per Section 4's trend and consensus). **Reconciliation: the current price does not appear to be pricing in aggressive growth on either a book or tangible-book basis** — consistent with "cheap versus its own demonstrated earnings power," satisfying the wave-2 valuation gate, though this reverse-engineering is more sensitive than the utility dividend model to the ROE/ROTCE normalization choice (the headline 17.9% Q2 ROTCE is itself inflated by the net one-time items discussed in Section 4, so a normalized mid-teens ROTCE was used deliberately rather than the headline number).

**Dossier view: cheap-to-fair.**

**3-year scenario returns (own build, annualized; method: dividend yield (~3.0%) **[Corrected 2026-10-08: quarterly dividend is now $2.00, a 3.58% yield; scenarios are about 0.6pt a year too low]** + EPS CAGR + amortized P/B re-rating over 3 years, entry P/B 1.55x per d4 snapshot):** Bear (credit cycle turns, EPS CAGR ~2%, P/B compresses to ~1.30x) ≈ **-1%/yr**. Base (EPS CAGR ~8%, blending organic growth, FirstBank synergy realization and buybacks, P/B stable) ≈ **+11%/yr**. Bull (EPS CAGR ~13% on faster integration synergies and continued NIM expansion, P/B re-rates to ~1.75x) ≈ **+20%/yr**. These are the analyst's own scenario construction, not a formal Monte Carlo or DCF output, and are disclosed as such.

## 8. Bull case / bear case

**Bull (3 points):**
1. Credit quality is improving, not deteriorating, even as the bank digests a large acquisition: NPLs down 10% QoQ, delinquencies down 8% QoQ, NCOs at 0.25% annualized — well inside a healthy through-cycle band.
2. NIM has expanded 16bps YoY in a period when many regional banks have struggled to grow spread, driven by disciplined deposit pricing (rate paid on interest-bearing deposits falling) and noninterest-bearing deposit growth.
3. FirstBank customer/system conversion is complete (as of June 22, 2026) — the highest-execution-risk phase of the acquisition is behind the company, and reported results should get progressively cleaner (fewer integration-cost deductions) from here.

**Bear (3 points):**
1. CET1 fell 60bps in a single quarter (10.1%→9.9%) **[Corrected 2026-10-08: 20bps in the quarter; 60bps over the year]** while the company kept buying back stock ($0.6bn) — a capital-allocation choice that leaves less cushion if credit conditions turn or if regulators push for higher buffers.
2. A meaningful share of the headline EPS growth is not organic: the FirstBank acquisition's full-quarter benefit plus a net-favorable mix of one-time items (Visa gain net of Foundation contribution, securities loss, and integration costs) inflate the YoY comparison; the market may already be pricing in a run-rate the bank has not yet demonstrated on a clean quarter.
3. Efficiency ratio is stuck at 60%, at the high end of the playbook's "acceptable" band, and won't improve until FirstBank integration costs fully roll off — a multi-quarter, not immediate, catalyst.

## 9. Key risks & kill criteria (measurable) — thesis-invalidation triggers / what would change our mind

1. Net charge-offs rise above 0.60% annualized of average loans for two consecutive quarters (vs 0.25% currently).
2. CET1 ratio falls below 9.5% (vs 9.9% currently) without a stated, credible path back above 10% within two quarters.
3. NIM compresses below 2.70% (vs 2.96% currently) for two consecutive quarters.
4. Efficiency ratio remains above 62% for three or more consecutive quarters after FirstBank integration costs were guided to roll off (i.e., expected cost synergies fail to materialize).
5. Nonperforming loans increase more than 25% quarter-over-quarter for two consecutive quarters (a reversal of the current improving trend).

## 10. Catalysts & calendar

- Next earnings release: estimated mid-October 2026 (Q3 2026), based on the 2025-10-15 filing date for the prior-year equivalent release — not yet confirmed by a company announcement.
- Full roll-off of FirstBank integration costs (management has not given an explicit end-quarter in the documents reviewed; worth confirming on the Q3 2026 call).
- CET1 trajectory over the next 1–2 quarters — the single number most likely to move the thesis either way.

## 11. Red-flag scan

No auditor change, restatement, going-concern language, or SEC/DOJ investigation was identified in the 10-K/10-Q/8-K filing index reviewed for 2024–2026. The most recent non-earnings 8-K (2026-07-21, Item 8.01/9.01) was a routine $2bn senior-notes issuance. The Visa Class B-3 derivative fair-value adjustment (−$85M in Q2 2026, "driven by the extension of anticipated litigation resolution timing") reflects PNC's exposure to the industry-wide Visa covered-litigation escrow structure — a known, disclosed, sector-wide item, not PNC-specific litigation risk, but worth tracking because the timing extension itself signals the underlying litigation is not yet resolved. **Correction to prior triage:** the triage's one-line thesis cites "completed acquisition integration (BBVA USA)" — that 2021 deal is not the relevant current event; the FirstBank acquisition (announced 2025-09-08, closed 2026-01-05, systems converted 2026-06-22) is what is actually driving 2026 results and the CET1 decline. This is recorded as a data conflict in the summary JSON. Insider Form 4 pattern and short-interest were not reviewed in this pass (time-boxed; flagged as a gap).

## 12. Data Quality Note — data basis, recency and disclaimer

Most recent period incorporated: Q2 2026 (10-Q filed 2026-08-05; earnings release 8-K Ex-99.1 filed 2026-07-15). Checked for events to 2026-09-25 via the SEC EDGAR filing index (most recent 8-K reviewed: 2026-07-21, routine debt issuance). GAAP vs adjusted labelling: all GAAP figures are explicitly labelled; "adjusted" (non-GAAP) EPS and ROTCE figures are labelled as such per company disclosure. Figures are presented on a consolidated basis throughout. This is research, not personalized investment advice.

## 13. Sources

1. SEC EDGAR, PNC submissions index — https://data.sec.gov/submissions/CIK0000713676.json (retrieved 2026-09-26)
2. PNC Q2 2026 earnings release, 8-K Ex-99.1, filed 2026-07-15 — https://www.sec.gov/Archives/edgar/data/713676/000162828026048244/q22026financialhighlightsa.htm
3. PNC Q1 2026 earnings release, 8-K Ex-99.1, filed 2026-04-15 — https://www.sec.gov/Archives/edgar/data/713676/000071367626000026/q12026financialhighlightsa.htm
4. PNC Q3 2025 earnings release, 8-K Ex-99.1, filed 2025-10-15 (FirstBank deal announcement terms) — https://www.sec.gov/Archives/edgar/data/713676/000071367625000126/q32025financialhighlightsa.htm
5. PNC 8-K, senior notes issuance, filed 2026-07-21 — https://www.sec.gov/Archives/edgar/data/713676/000162828026048994/pnc-20260716.htm
6. v4/data/b1_live_scores.csv and v4/data/d4_live_snapshot.parquet (project data, as-of dates per file)
7. v4/outputs/Q04_triage.json (prior triage note for PNC)

## Correction (verification DV34, 2026-10-08)

1. CET1 change (s6 Capital, s8 bear 1). Wrong text: "CET1 fell 60bps in a single quarter (10.1%→9.9%)" and "down 60bps in one quarter". Correct: CET1 was 10.1% at 31 Mar 2026 and 9.9% at 30 Jun 2026, a 20bps quarterly fall; 60bps (10.5% to 9.9%) is the year-on-year fall (8-K Ex-99.1 accession 0001628280-26-048244). The F46 summary JSON already says 20bp in the quarter.
2. Valuation method (s7). Wrong text: risk-free 4.2% giving cost of equity about 8.6% and implied growth "0% to +1%" (P/B 1.55x, ROE 13-16%) and "+0.5% to +2.5%" (P/TBV 2.03x, ROTCE 15-17%). Correct: the 10-year Treasury was 5.17% on 25 Sep 2026, so COE = 5.17% + 0.889 x 5% = 9.6%. With implied g = (P/B x COE - ROE)/(P/B - 1): P/B 1.55x gives +3.4% (ROE 13%), +0.7% (14.5%), -2.0% (16%); P/TBV 2.03x gives +4.4% (ROTCE 15%), +3.4% (16%), +2.4% (17%). (Even at the original 8.6% COE the P/B result was +0.6% at ROE 13% and -4.9% at 16%, so "0% to +1%" held only at the low end.) Inputs: book value $145.52 and TBV $111.09 per share (8-K -048244), price $225.64, beta 0.889 (d4). Implied growth is still below the dossier's own high-single-digit EPS base, so implied vs base remains "below" and the cheap-to-fair view stands, but the cushion is about 2.4%-4.4% priced in, not 0%-2.5%.
3. Dividend yield in the 3-year scenarios (s7). Wrong text: dividend yield about 3.0%. Correct: PNC raised the quarterly dividend 30 cents (18%) to $2.00 (8-K -048244); $8.00 a year is 3.58% of $225.64 (d4). Scenario returns are about 0.6pt a year too low: bear about -0.4%, base about +11.6%, bull about +20.6%.
4. Data gap closed (s6 M&A financing). The FirstBank consideration was about 13.9 million PNC shares plus $1.2 billion in cash, implying a transaction value of $4.1 billion (8-K accession 0000713676-25-000062); closed 5 Jan 2026 (accession 0000713676-26-000003).

Verdict: unchanged (INCLUDE-SMALL). F46_summary.json: PNC scenario_returns_3y and the valuation reconciliation text were updated to the restated values; implied_vs_base ("below") is unchanged.
