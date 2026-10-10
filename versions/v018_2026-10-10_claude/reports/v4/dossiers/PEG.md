# PEG — Public Service Enterprise Group Incorporated

## 1. Verdict

**INCLUDE-SMALL** (half weight). Thesis horizon: 12–36 months. Reservation: GAAP EPS is volatile and currently declining because of Nuclear Decommissioning Trust (NDT) mark-to-market swings, so the headline GAAP trend understates the growth story that management's non-GAAP operating-earnings guidance describes; and the nuclear/data-center upside that the triage cited as an extra lever is still an option, not yet a signed cash flow. Reaffirmed 2026 non-GAAP operating-EPS guidance and reasonable relative valuation support the core rate-base thesis, but the GAAP/non-GAAP gap and rising leverage funding a large capex program earn the half-weight treatment.

## 2. Business in plain English

PSEG's main asset is PSE&G, New Jersey's largest regulated electric and gas transmission-and-distribution utility, which earns a state-regulator-approved return on its wired network. Alongside it, PSEG Power/PSEG Nuclear owns and operates New Jersey's nuclear fleet (Salem/Hope Creek, with NRC licenses extended into the 2050s–2060s per the company's Q1 2026 materials cited in the prior triage), selling power into the PJM wholesale market and increasingly discussing long-term contracts with data-center developers who want firm, carbon-free electricity. PSEG Long Island and smaller competitive/transmission units round out the portfolio. Revenue and profit are overwhelmingly a function of (a) the regulator-approved rate base at PSE&G and (b) nuclear output and wholesale/hedge prices, not of retail competition.

## 3. Why the model likes it — durable or artefact?

b1_live_scores.csv (as of the file's `as_of` date) shows PEG's factor pull is concentrated in **Quality** (fam_Q 0.900, top of its peer set) and **Value** (fam_V 0.811), with weak **Momentum** (fam_M 0.144) and weak **Earnings momentum** (fam_S 0.142, SUE −1.26 — the worst of the three names in this batch). Composite rank 263 of ~500 (decile 5), i.e., mid-pack overall and well outside the model's live top-30. Quant read: the Quality/Value signal is a genuinely durable feature of a regulated utility with high gross-profit/assets and a value-tilted starting multiple; the weak SUE/momentum readings line up with the GAAP EPS decline discussed below (Section 5) rather than being noise — this is a real, not artefactual, near-term earnings-momentum negative that the quant model is correctly picking up, even though the non-GAAP operating story is intact.

## 4. Last several quarters of results (SEC filings; GAAP unless noted)

Source: PEG 10-Q filings via SEC EDGAR XBRL (data.sec.gov/api/xbrl/companyfacts/CIK0000788784.json, retrieved 2026-09-26) and the Q2 2026 earnings release (8-K Ex-99.1, filed 2026-08-04, and the Q2 2025 equivalent filed 2025-08-05).

| Period | Revenue ($M, GAAP) | Net income ($M, GAAP) | Diluted EPS (GAAP) | Non-GAAP operating EPS |
|---|---|---|---|---|
| Q1 2025 | 3,222 | 589 | 1.18 | n/a (not pulled) |
| Q2 2025 | 2,805 | 585 | 1.17 | 0.77 |
| Q3 2025 | 3,226 (q. only 3,226; 9-mo 9,253) | 622 | 1.24 | n/a (not pulled) |
| FY2025 | 12,168 | 2,111 | 4.22 | ~4.06 (implied; see note) |
| Q1 2026 | 3,848 | 741 | 1.48 | n/a (not pulled) |
| Q2 2026 | 2,554 | 334 | 0.67 | 0.86 |
| H1 2026 | 6,402 | 1,075 | 2.15 | 2.41 |

Note on FY2025 non-GAAP: the Q2 2026 slide deck states 2026 operating-earnings guidance midpoint (~$4.34, i.e. $4.28–$4.40) "represents ~7% increase over 2025 results," which backs out to an implied FY2025 non-GAAP operating EPS of roughly $4.06 — this is a derived figure, not a directly quoted one, and should be confirmed against the Q4 2025 earnings release before being relied on precisely.

**GAAP vs non-GAAP gap, quantified and sourced:** Q2 2026 GAAP EPS fell 43% YoY ($1.17→$0.67) while non-GAAP operating EPS *rose* 12% YoY ($0.77→$0.86); H1 2026 GAAP EPS fell 9% YoY ($2.35→$2.15) while H1 non-GAAP operating EPS rose to $2.41. Both figures are quoted directly from the Q2 2026 and Q2 2025 earnings-release slide decks (Ex-99.1 to the respective 8-Ks). Management attributes the gap to NDT (nuclear trust) mark-to-market and other non-cash/infrequent items excluded from operating earnings — a standard, disclosed adjustment for utilities with large decommissioning trusts, but one that means a reader who tracks only headline (GAAP) EPS would wrongly conclude PSEG's earnings power is shrinking.

## 5. Guidance track record

- **Q2 2026 release (2026-08-04):** "PSEG maintained 2026 non-GAAP Operating Earnings guidance of $4.28–$4.40 per share" — reaffirmed, not raised or cut, versus the prior (Q1 2026 and FY2025-release) range. Long-term: "PSEG's outlook for long-term, non-GAAP Operating Earnings CAGR is 6%–8% through 2030," also reaffirmed.
- Company gives full-year non-GAAP operating-EPS guidance rather than quarterly guidance; no evidence in the pulled filings of a guidance cut in the last four releases. This corroborates the triage's "guided 6–8% EPS growth" claim with a primary source (contrary to the lead_v3_audit lesson about unverified "guidance raised" claims — here the correct characterization is **maintained**, not raised).

## 6. Earnings quality & balance sheet

- **FCF / cash conversion:** H1 2026 operating cash flow $1,821M vs capex (PaymentsToAcquirePropertyPlantAndEquipment) $1,459M → traditional FCF ≈ +$362M for the half; H1 2025 was OCF $1,527M vs capex $1,415M ≈ +$112M. Per the utilities sector playbook, positive traditional FCF at a growth utility is not obviously a virtue — it can indicate under-investment relative to rate-base growth — so this is presented as a fact, not a scored positive.
- **Leverage:** Long-term debt (noncurrent) rose from $18,964M (2024-12-31) to $22,741M (2026-06-30), +20% in six quarters, consistent with a large, rate-base-funding capex program (company states a **$24–28bn total capital program** in the Q2 2026 deck). Debt/EBITDA proxy using d4 snapshot figures: total debt $24,678M / EBITDA $4,463M ≈ 5.53x — this is a rough proxy, not a rating-agency FFO/Debt figure (which was not obtained in this pass — data gap, flagged).
- **SBC/one-offs:** Not separately quantified in this pass; flagged as a gap for a future update.
- **Recent financing:** $500M of 4.800% senior notes due 2031, completed 2026-06-03 (8-K Item 8.01, filed 2026-06-03) — routine debt issuance, no red flag.
- **Share count:** PSEG fully diluted average shares ~499M in Q2 2026 vs ~500M in Q2 2025 — essentially flat, no material dilution.
- **Dividend:** Indicated annual dividend raised by $0.16/share for 2026 — the company states this is the 15th consecutive annual increase (Q2 2026 deck). Current dividend rate ≈ $2.68/share (payout ≈ 62% of non-GAAP operating EPS guidance midpoint).

## 7. Valuation — V1 reconciliation and reverse DCF

**No V1 row exists for PEG** in `v4/outputs/v1_valuation_table.csv` or `v1_valuation.json` (checked; ticker absent from both). `v1_verdict` is therefore set to `null` — this dossier's valuation view is the analyst's own, not a reconciliation.

**Snapshot (d4_live_snapshot.parquet, as of 2026-09-25 close, price $67.02):** NTM P/E 14.34x, trailing P/E 16.67x, dividend yield 3.91–4.0%, EV $57.66B, beta 0.519, analyst mean target $85.31 (18 analysts, "buy" consensus) — an implied 27.3% upside to mean target, matching the triage note.

**Reverse DCF (two-stage dividend-discount, own build):** Using the current indicated dividend ($2.68), a CAPM cost of equity (rf 4.2%, ERP 5%, PEG beta 0.519 → COE ≈ 6.8%) and a 4% nominal terminal growth rate after 10 years, the price of $67.02 is consistent with roughly **-0.6% to +2%** annualized dividend/earnings growth over the next decade — sensitivity at COE 7.0%/7.5%/8.0% gives implied growth of 0.2%/1.9%/3.5% respectively (script `reverse_dcf.py`, cache/F46). **[Corrected 2026-10-08: rf 4.2% and 4% terminal growth are inconsistent with the 5.17% 10-year Treasury; at Ke 7.98% and 3% terminal the dividend model implies about 5.4% a year, not -0.6% to +2% (DV33)]** **This is well below management's guided 6–8% non-GAAP operating-earnings CAGR through 2030.** The reconciliation: the market is pricing PEG for materially less growth than the company itself is guiding to — consistent with "cheap versus guidance" rather than "priced for perfection." Caveat: this model is sensitive to the discount-rate assumption and to whether dividend growth tracks EPS growth 1:1; it is presented as a directional check, not a precise fair value.

**Dossier view: cheap-to-fair.** Consistent with the reverse-DCF check above (implied growth < base case), which satisfies the INCLUDE/INCLUDE-SMALL valuation gate in the wave-2 instructions.

**3-year scenario returns (own build, annualized; method: dividend yield + non-GAAP operating-EPS CAGR + amortized NTM P/E re-rating over 3 years, entry NTM P/E 14.34x per d4 snapshot):** Bear (EPS CAGR ~2%, multiple compresses to ~12.5x on a hostile NJ rate case or nuclear-subsidy setback, dividend held) ≈ **+1%/yr**. Base (EPS CAGR at the guided 6-8% midpoint ~7%, multiple stable) ≈ **+11%/yr**. Bull (EPS CAGR ~9% on nuclear-PPA upside, multiple re-rates to ~17x) ≈ **+19%/yr**. These are the analyst's own scenario construction, not a formal Monte Carlo or DCF output, and are disclosed as such.

## 8. Bull case / bear case

**Bull (3 points):**
1. Nuclear fleet (licenses extended into the mid-2050s to mid-2060s per prior triage research) is well positioned for direct data-center power-purchase agreements or uprates, which — if signed — would be incremental to the current 6–8% CAGR guidance and are not yet in the base plan.
2. PSE&G's regulated rate base grew ~7% in 2025 (per the Q2 2026 deck's "outlook driven by" bullet), and a $24–28bn multi-year capital program gives high revenue-growth visibility if the NJ BPU continues to approve recovery.
3. 15 consecutive years of dividend increases and a reaffirmed (not cut) long-term growth guide are evidence of a management team executing to plan.

**Bear (3 points):**
1. GAAP earnings are genuinely volatile — Q2 2026 GAAP EPS fell 43% YoY on NDT mark-to-market losses — and a reader or algorithm that scores on trailing GAAP EPS (as some screens do) will misprice this stock; the SUE score in b1_live_scores.csv (−1.26, the weakest of this batch) reflects exactly that. **[Corrected 2026-10-08: the Q2 2026 GAAP decline came from a $258M pre-tax mark-to-market LOSS on power hedges, not NDT losses; NDT fund activity was a $153M pre-tax GAIN (DV33)]**
2. Long-term debt is growing faster than the regulated asset base can obviously absorb without a credit-metric check we did not complete in this pass (FFO/Debt not obtained); if a downgrade followed, PSEG's growth plan becomes more expensive to finance.
3. New Jersey's nuclear-subsidy and rate-recovery framework is a political variable; a hostile BPU decision on a future rate case or ZEC-style nuclear support renewal would directly cut the growth rate this thesis depends on.

## 9. Key risks & kill criteria (measurable) — thesis-invalidation triggers / what would change our mind

1. Non-GAAP operating-earnings guidance for FY2026 is formally cut below the current $4.28–$4.40/share range, or the long-term 6–8% CAGR guide (through 2030) is lowered.
2. NDT mark-to-market losses (or other excluded items) depress GAAP net income by more than 20% YoY in two consecutive quarters with no offsetting rise in non-GAAP operating EPS (i.e., the gap becomes a real earnings problem, not a technical MTM item).
3. Total debt/EBITDA (proxy) rises above 6.5x for two consecutive quarters (from ≈5.5x currently).
4. No signed data-center nuclear PPA, uprate agreement, or equivalent incremental-growth contract is announced within the next 12 months (removes the stated bull optionality without penalizing the base case).
5. A credit-rating agency (S&P/Moody's/Fitch) downgrades PSEG or PSE&G's senior unsecured rating, or moves the outlook to negative.

## 10. Catalysts & calendar

- Next earnings release: estimated early November 2026 (Q3 2026), based on the 2025-11-03 filing date for the prior-year equivalent release — not yet confirmed by a company announcement.
- NJ BPU rate-case and nuclear-subsidy/ZEC renewal proceedings (ongoing; specific dates not pulled in this pass).
- Any Q3/Q4 2026 announcement of a data-center bilateral power contract (the Utility Dive article cited in the prior triage flagged this as an emerging area).

## 11. Red-flag scan

No auditor change, restatement, going-concern language, SEC/DOJ investigation, or short-seller report was identified in the SEC EDGAR filing list (10-K/10-Q/8-K index) reviewed for 2024–2026. The two most recent non-earnings 8-Ks (2026-06-03 debt issuance, 2026-04-23 Item 5.07 annual-meeting vote results) are routine. The GAAP/non-GAAP EPS gap discussed in Sections 4–6 is a genuine earnings-quality complication (not a fraud flag) that must be read correctly, per the lead_v3_audit lesson on not mixing adjusted and GAAP numbers. Insider Form 4 pattern and short-interest were not reviewed in this pass (time-boxed; flagged as a gap).

## 12. Data Quality Note — data basis, recency and disclaimer

Most recent period incorporated: Q2 2026 (10-Q filed 2026-08-04; earnings release 8-K Ex-99.1 filed 2026-08-04). Checked for events to 2026-09-25 via the SEC EDGAR filing index (no 10-Q/10-K/8-K after 2026-08-04 flagged a change to guidance, credit rating, or litigation status as of this review). GAAP vs adjusted labelling: all GAAP figures are explicitly labelled; "non-GAAP operating earnings" figures are labelled as such per company disclosure and are management's own reconciliation, not an analyst adjustment. Figures are presented on a consolidated basis throughout. This is research, not personalized investment advice.

## 13. Sources

1. SEC EDGAR, PEG submissions index — https://data.sec.gov/submissions/CIK0000788784.json (retrieved 2026-09-26)
2. SEC EDGAR, PEG XBRL company facts — https://data.sec.gov/api/xbrl/companyfacts/CIK0000788784.json (retrieved 2026-09-26)
3. PEG Q2 2026 earnings release / slide deck, 8-K Ex-99.1, filed 2026-08-04 — https://www.sec.gov/Archives/edgar/data/788784/000119312526331660/d101695dex991.htm
4. PEG Q2 2025 earnings release / slide deck, 8-K Ex-99.1, filed 2025-08-05 — https://www.sec.gov/Archives/edgar/data/788784/000119312525173127/d206274dex991.htm
5. PEG 8-K, debt issuance, filed 2026-06-03 — https://www.sec.gov/Archives/edgar/data/788784/000119312526255562/d38824d8k.htm
6. v4/data/b1_live_scores.csv and v4/data/d4_live_snapshot.parquet (project data, as-of dates per file)
7. v4/outputs/Q15_triage.json (prior triage note for PEG)
8. Prior triage's own sources: utilitydive.com PSEG/PJM data-center article; investing.com PSEG Q1 2026 slides summary (not independently re-verified in this pass; carried forward as context, not as a primary figure source)
9. `reverse_dcf.py`, written for this dossier, cache C:\Users\user\eqv4\cache\F46\

## Correction (verification DV33, 2026-10-08)

Sources: 10-Q acc 0001193125-26-332943; 8-K Ex-99.1 accs 0001193125-26-331660 (Q2 2026) and -26-073678 (Q4 2025); XBRL companyfacts. Quarterly GAAP table, non-GAAP operating EPS (0.86, 0.77, 2.41), guidance ($4.28-$4.40, 6%-8% CAGR), $24-28bn capital program, dividend raise, long-term debt ($22,741M) all pass.

1. Driver of the Q2 GAAP decline (FAIL, moderate). Wrong text: "Q2 2026 GAAP EPS fell 43% YoY on NDT mark-to-market losses" (sections 4 and 8, kill criterion 2, F46 key_adverse_facts). Correct: the Q2 2026 reconciliation shows NDT fund activity was a pre-tax GAIN of $153M (Q2 2025: $108M gain); the swing is a pre-tax mark-to-market LOSS of $258M on power-hedge positions (Q2 2025: $190M gain). Operating EPS is unaffected. Verdict unchanged; read kill criterion 2 as "MTM and NDT items".
2. Reverse DCF (FAIL, method). Wrong text: rf 4.2%, ERP 5%, COE 6.8%, terminal growth 4%, implied -0.6% to +2%. The risk-free rate is not the 5.17% 10-year Treasury (25 Sep 2026) and the 4% terminal rate is above the programme's 3%. Recomputed on the dossier's own dividend basis (D0 $2.68, price $67.02): Ke 7.98% (5.17% + Blume-adjusted beta 0.678 x 4.14%), terminal 3% gives implied dividend growth of 5.4% a year (3.4% at Ke 7.25%, 6.7% at 8.5%). Versus the base of 7% (guided 6%-8%) implied is still below, but by 1.6 points, not "well below". implied_vs_base stays "below" (narrow); INCLUDE-SMALL unchanged. Scenario arithmetic (+1%, +11%, +19%) reproduces and was not re-based.
3. Minor: the FY2025 non-GAAP operating EPS "implied about $4.06" is stated as $4.05 in the Q4 2025 release. Total debt / EBITDA 5.5x uses Yahoo fields and is unverifiable from filings.

Verdict change: none. implied_vs_base unchanged ("below", narrower). `F46_summary.json` PEG entry updated (reconciliation text and the key_adverse_facts wording only).
