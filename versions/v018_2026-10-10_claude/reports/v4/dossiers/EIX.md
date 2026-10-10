# EIX — Edison International (parent of Southern California Edison)

*Most recent period incorporated: Q2 2026 10-Q (period ended 2026-06-30, filed 2026-07-30). Checked SEC EDGAR filing index for events to 2026-09-25 (no 10-Q/10-K filed after 2026-07-30 as of that date; next scheduled filing is Q3 2026, due around late October) and checked news coverage (Bloomberg via Claims Journal, Courthouse News, Bloomberg Law, CalMatters, Utility Dive) through 2026-09-23. Two EIX 8-K exhibit folders on SEC EDGAR (the Q2 2026 earnings-release exhibits) returned repeated server errors during this research session and could not be opened directly **[Corrected 2026-10-08: wrong: the Q2 2026 Ex-99.1 text release is available, acc 0000827052-26-000058; see Correction section]**; the 10-Q itself, which contains the material financial and legal disclosure, was fully accessible and is the primary source below.*

*Basis: **consolidated** GAAP (Edison International, the parent holding company, together with its regulated utility subsidiary Southern California Edison, "SCE"), USD millions except per-share. Non-GAAP "core" EPS, where referenced, is labeled explicitly and is the company's own definition.*

## 1. Verdict

**WATCH.** Re-assess after Q3 2026 earnings (2026-10-27) and any outcome from a possible year-end special legislative session. One-sentence reason: EIX is statistically cheap (P/B ~1.2x, EV/EBITDA ~7.3x, both below typical regulated-utility ranges) with an intact rate-base growth story (~7% CAGR to a $67.9bn rate base by 2030), but it carries a **currently unquantifiable** wildfire liability — the company's own words are "unable to reasonably estimate a range of losses" for the Eaton Fire — with a statutory shareholder cap ($4.3bn) that can be voided two separate ways, a bellwether trial in January 2027, and a wildfire-liability legislative reform that just failed (triggering a 23% single-day stock decline around 2026-08-31/09-01). This is a case where the range of outcomes is genuinely dominated by a binary legal/regulatory question that neither this analyst nor the company can resolve today — a reason to wait for the next catalyst, not to size a position now.

## 2. Business in plain English

Edison International is the holding company for Southern California Edison, a regulated electric utility serving roughly 15 million people across a 50,000-square-mile service territory in central, coastal and Southern California (excluding the City of Los Angeles, served by LADWP). SCE earns a regulator-approved return on its "rate base" (approved capital investment in poles, wires, substations and grid-hardening equipment) set by the California Public Utilities Commission (CPUC) through periodic General Rate Cases — revenue and profit are a function of approved capital spending and the allowed return, not of a competitive product market. Competitive position is that of a monopoly franchise utility; the business risk is almost entirely regulatory, political and — as this dossier documents — wildfire-liability risk, not commercial risk.

## 3. Why the model likes it — and whether that's durable

Preliminary quant rank **24 of 503** (composite 0.757; Q 0.728, **V 0.942** — very high value/cheapness score, M 0.602 — weak, roughly flat 12-1-month momentum of +3.0%). The Value score is genuinely earned: sourced multiples (below, via `valuation.py`) confirm EIX trades below typical regulated-utility bands on P/B and EV/EBITDA. **This is not obviously a value trap nor obviously a bargain — it is a real, quantifiable discount for a real, currently unquantifiable risk**, and the two need to be held apart rather than netted into one score.

**Important, quantified limitation of the momentum input**: EIX stock fell ~23% in a single day around 2026-08-31/09-01 (its largest one-day decline in over 25 years, per CEO Pedro Pizarro) when a legislative wildfire-liability reform bill (SB 492) died without a vote at the end of the California legislative session. The "12-1 month" momentum factor construction **excludes the most recent month** — so, depending on the exact calendar-month cutoff used, this shock may sit substantially or entirely **outside** the window the M score measures. The model's weak-but-not-alarming M=0.602 should not be read as having priced in this event; the spot price and P/E multiples used elsewhere in the model (as of 2026-09-25) do reflect it, but the momentum *signal specifically* is a poor guide to how fresh and severe this repricing was. **Flag this explicitly as a data conflict/model blind spot**, not a reason for comfort.

## 4. Last two years of results

Figures are consolidated GAAP unless labeled "core" (company non-GAAP). **Data-quality caveat**: EIX's XBRL duration facts for Q4 2024 and Q4 2025 were not separately available in the point-in-time extract used and were not re-derived from FY-minus-9-months this pass — two of the requested eight quarters are therefore `not available` rather than estimated.

| Quarter | Revenue ($m) | Net income ($m) | Diluted EPS |
|---|---|---|---|
| Q3 2024 | n/a¹ | n/a¹ | n/a¹ |
| Q4 2024 | not available² | not available² | not available² |
| Q1 2025 | 3,811 | 1,436 | **$3.72** |
| Q2 2025 | 4,543 | 343 | $0.89 |
| Q3 2025 | 5,750 | 832 | $2.16 |
| Q4 2025 | not available² | not available² | not available² | **[Corrected 2026-10-08: derivable: revenue $5,213m, net income $1,848m, diluted EPS $4.78 (FY2025 less 9M)]**
| Q1 2026 | 4,103 | 531 | $1.37 |
| Q2 2026 | 4,348 | 534 | $1.38 |

¹ Q3 2024 XBRL revenue tag pulled a value inconsistent with the surrounding series in this extraction pass and was excluded rather than reported with low confidence. ² see caveat above.

**The single most important line in this table is Q1 2025 — the quarter the Eaton Fire ignited (2025-01-07/08) — showing the *highest* net income and EPS ($3.73 per the Q1 2025 earnings release; $3.72 in the XBRL extract, rounding) of the eight quarters, not a large charge.** This is a genuine, adversarial finding this dossier ran to ground rather than left unexplained: per the Q1 2025 earnings release's own non-GAAP reconciliation (8-K Ex-99.1, filed 2025-04-29), **$908 million after-tax ($2.36/share) of "non-core" items** were recorded that quarter (core EPS was a much more pedestrian $1.37, core earnings $528m) — and the dominant piece, per the release's own footnote, is **not Eaton Fire-related at all**: it is a **$1,341 million pre-tax ($966m after-tax) regulatory-recovery gain tied to the TKM Settlement Agreement**, which in Q1 2025 authorized cost recovery (through customer rates) of previously-expensed 2017/2018 Thomas/Koenigstein/Montecito wildfire and mudslide claim costs — a much older litigation matter (§11) whose settlement approval happened to land in the same quarter the Eaton Fire ignited, creating a one-time, non-cash, GAAP-only income spike unrelated to Eaton. Two smaller items (small Eaton-related insurance/legal net items, and $36m of routine Wildfire Insurance Fund contribution amortization) round out the reconciliation. The **operating** picture that quarter (core EPS $1.37, up from $1.13 a year earlier) was unremarkable and driven mainly by a TKM-related interest-expense benefit, not the fire. This is exactly why core (non-GAAP) EPS, clearly labeled, is the more useful run-rate metric for this name, and why this dossier treats the GAAP EPS series as noisy. By contrast, the two most recent quarters (Q1–Q2 2026) show the *Eaton* Fire's **net pre-tax P&L impact was specifically $0** in both the quarter and the six months (see §6) — gross claims are being offset dollar-for-dollar by an equal expected Wildfire Fund recovery, a different and more benign mechanic than the headline word "wildfire liability" alone would suggest — **provided that recovery is ultimately allowed** (§9).

## 5. Guidance track record

**Sourcing caveat**: both of EIX's Q2 2026 8-K exhibits turned out, on retrieval, to be **image-based slide decks** (a "Business Update Presentation" and an "Earnings Teleconference" deck — confirmed by opening the filings' own document index, accessions 0000827052-26-000058 and -000061), not text press releases, so the guidance table could not be grepped from a primary text source the way it was for the other two companies in this batch **[Corrected 2026-10-08: wrong: Ex-99.1 is a text press release stating the guidance verbatim]**. The figures below are therefore **secondary-sourced** (multiple independent contemporaneous news reports of the 2026-07-30 earnings call — Seeking Alpha and BigGo Finance both report the same numbers) and are flagged `aggregator-sourced, cross-corroborated but not independently verified against the primary exhibit` rather than stated with full primary-source confidence:

- **FY2026 core (non-GAAP) EPS guidance: $5.90–$6.20, REAFFIRMED (not raised or cut) at the Q2 2026 release** — unchanged from prior guidance per these reports.
- Q2 2026 **core** EPS reported at **$1.54**, up 59% YoY from $0.97 in Q2 2025 — versus the **GAAP** diluted EPS of $1.38 this dossier verified directly from the 10-Q (§4) for the same quarter. The ~$0.16/share GAAP-vs-core gap is real and should be labeled every time either figure is used; this dossier could not independently confirm the exact reconciling items (likely wildfire-related items excluded from "core") from a primary source this pass.
- Long-term target reaffirmed at the same release: **5–7% core EPS growth**, attributed by management to the 2025 GRC authorization and lower interest expense tied to Woolsey Fire cost recovery.

A **reaffirmed** (not raised or cut) guide, at a modest premium to the 12-month-trailing run-rate implied by Q1+Q2 2026 core EPS, is a genuinely neutral-to-mildly-positive signal on the pure operating business — but it says nothing about the Eaton Fire liability question, which sits outside "core" EPS by construction. **Only one data point was obtained this pass (Q2 2026); the full 4-release track record (Q3 2025 through Q2 2026) recommended by the standard template was not completed** given the image-exhibit obstacle and time constraints — a follow-up item for the lead.

## 6. Earnings quality & balance sheet

- **Eaton Fire accounting mechanics (the central earnings-quality issue for this name)**: self-insurance recoveries were **exhausted as of 2026-02-11**. Above a $1.0bn retention, SCE is reimbursed from the AB1054/SB254 Wildfire Fund's "Initial Account," confirmed by the fund administrator as covering the Eaton Fire as a "covered wildfire." For the six months ended 2026-06-30, SCE recorded **$511m of gross Eaton Fire wildfire-related claims, fully offset by an equal $511m expected Wildfire Fund recovery — a $0 net pre-tax P&L impact**. The statewide fund is reported to have **~$21bn of claims-paying capacity** available for the Eaton Fire. This offset accounting is the reason GAAP earnings have not (yet) shown a large, sustained Eaton Fire charge — but it depends entirely on that recovery being realized (§9).
- **The company states plainly it cannot size the total exposure**: *"While SCE recorded losses related to settlements that have been entered into related to the Eaton Fire, Edison International and SCE are currently unable to reasonably estimate a range of losses that may be incurred in connection with the Eaton Fire."* (10-Q, Note 12). This is as close to an explicit "we cannot bound this liability" statement as a filing makes, and is the single fact this whole dossier turns on.
- **Leverage** (utility-appropriate reading, not generic D/E): FY2025 total debt (short + long-term, per internal pipeline cross-check) ≈ $43.3bn against equity of $17.3bn — an equity multiplier of ~5.4x, which the utilities-power.md playbook says is normal-to-expected for a regulated network financed against contracted/regulated cash flows, not a red flag on its own. Edison International Parent's own credit-facility covenant caps consolidated debt/total-capitalization at 0.70:1; **actual at 2026-06-30 was 0.66:1 — inside the covenant, with limited headroom**, per the 10-Q MD&A.
- **Credit ratings, updated for the most recent event**: S&P **BBB- with negative outlook** (downgraded 2025-10-21, citing Wildfire Fund concerns); Moody's **Baa2 stable** (reaffirmed after SB 254 passed, Sept 2025 — not re-confirmed after the more recent SB 492 failure); Fitch **BBB, outlook cut to negative from stable** in early September 2026, explicitly "citing the stalled reform push" (SB 492's failure). **Two of three agencies now carry a negative outlook**; all three sit at the lower end of investment grade, and management itself frames a further downgrade to junk as a real, customer-cost-relevant risk.
- **Preferred stock**: EIX redeemed all Series A Preferred Stock and repurchased some Series B in Q1 2026 ($414m + $4m); Series B preferred remains outstanding and can restrict common dividends under its terms.
- **Financing/equity**: multiple capital-markets shelf offerings (424B2/424B5 filings) in March 2025, February 2026 and April/May 2026 — **type and size were not individually confirmed this pass** (`not available`), a real gap given "equity issuance needs" was specifically flagged as a diligence priority for this name. What **is** confirmed, from a 2026-09-23 CEO interview (Bloomberg via Claims Journal): management's current public claim is that the **$38–41bn capital plan requires no new common equity issuance through 2030**, funded instead by cash flow and capital-markets debt. Treat this as **management's own claim, not an audited fact** — it is inherently contingent on the Eaton Fire liability not exceeding what is already funded/capped, which is precisely the unresolved question in §9.

## 7. Valuation snapshot

Per the utilities-power.md playbook, a mixed regulated/holdco entity should ideally be valued sum-of-the-parts on EV/RAB or P/B-against-earned-ROE; that full build was not completed this pass given time constraints, so the figures below (from `valuation.py`, FY2025 financials, price 2026-09-25) are trailing cross-checks, not the primary method:

| Metric | EIX | Typical regulated-utility range (playbook) |
|---|---|---|
| P/E (trailing GAAP) | 5.7x | **[Corrected 2026-10-08: FY2025 GAAP EPS $11.55 gives 4.6x; TTM about 5.4x]** not the primary lens (playbook: "corrupted by non-cash and timing items") |
| EV/EBITDA | **7.3x** | 9–13x for regulated networks — EIX trades at a **real discount** |
| P/B | **1.2x** | US regulated utilities historically 1.6–2.2x — also a **real discount** |
| Dividend yield | 6.7% | — elevated, market pricing real risk |
| FCF yield | -3.2% (FCF = CFO $6.0bn − capex $6.6bn) | **negative FCF during rate-base growth is a playbook-flagged growth signal, not distress**, provided it is funded on-plan |
| Scenario value (prob.-weighted) | **$55.50/share (+5.5% vs $52.65 price)** | Bear $36.40 (-30.9%, 30%) / Base $57.60 (+9.4%, 45%) / Bull $74.80 (+42.1%, 25%) — deliberately wide dispersion reflecting the binary liability question, not a growth assumption |

The discount to typical regulated-utility multiples is real and roughly proportionate to a genuine, unresolved risk — this dossier does not conclude the stock is mispriced in either direction.

## 8. Bull case and bear case

**Bull (3 points, evidence-based)**
1. Core regulated-utility earnings power is intact and growing: ~7% rate-base CAGR guided through 2030 to a $67.9bn rate base, under a General Rate Case that already runs through 2028 — a business-model tailwind unrelated to the wildfire litigation.
2. The existing AB1054/SB254 framework has already survived one legislative cycle (SB 254 passed and expanded the Wildfire Fund in September 2025); the Eaton Fire has been confirmed a "covered wildfire," the $1.0bn self-insurance retention is already exhausted (the worst of the *direct* P&L hit may be behind, not ahead), and management is publicly committed to no new equity dilution through 2030.
3. Valuation already reflects real stress (P/B 1.2x, EV/EBITDA 7.3x, both below typical regulated-network ranges) — the probability-weighted scenario value is modestly above the current price even before crediting any chance of a favorable prudency finding or a successful special legislative session.

**Bear (3 points, evidence-based)**
1. **The company itself cannot bound the liability.** The 10-Q's own words — "unable to reasonably estimate a range of losses" — mean neither this analyst nor, on the record, the company can currently size the downside. A bellwether trial is set for January 2027, and "investigators have tied [the fire] to Edison equipment" per contemporaneous reporting, even though SCE's own filing language is more guarded ("likely associated").
2. **The $4.3bn shareholder liability cap can be voided two separate ways**: a CPUC finding of "conscious or willful disregard" (a high bar, but not a zero-probability one given SCE's own account of a de-energized line being associated with the ignition), **or** simple depletion of the statewide $21bn Wildfire Fund — a risk EIX does not fully control, since the fund is shared with PG&E and SDG&E's own wildfire liabilities. A recent, still-live legislative push (SB 492) to add further protections just failed, and Fitch has already moved to a negative outlook citing exactly that failure.
3. **Political/regulatory risk is acute and current, not theoretical**: the -23% single-day stock move on the SB 492 failure (versus PG&E's -18-26%, depending on source) shows the market treats this as a live, first-order risk, not a resolved historical event — and management's own CEO says a further downgrade to junk would raise customer costs by "hundreds of millions of dollars," implying the company itself views the credit-rating trajectory as fragile.

## 9. Key risks & kill criteria

1. CPUC issues (or signals it is likely to issue) a "conscious or willful disregard" prudency finding on the Eaton Fire — this would remove the $4.3bn cap entirely.
2. Credible signs the statewide $21bn Wildfire Fund is being materially depleted (by this fire, a new fire, or PG&E/SDG&E claims) before SCE's claims are resolved — the second, EIX-uncontrolled way the cap disappears.
3. Any additional Eaton-Fire-related GAAP charge that is **not** offset dollar-for-dollar by a Wildfire Fund recovery accrual (i.e., a break in the $0-net-impact pattern seen in H1 2026) — this would signal the recovery mechanism itself is becoming less certain.
4. A further credit-rating downgrade at any of the three agencies (S&P is already at the lowest investment-grade notch, BBB-, with a negative outlook — the next downgrade step is speculative grade).
5. Management reverses the "no new common equity through 2030" position — a concrete, checkable statement made on 2026-09-23 that would be a material negative surprise if walked back.
6. An adverse verdict or damaging evidentiary finding at the January 2027 bellwether trial.

## 10. Catalysts & calendar

Next earnings: **2026-10-27** (Q3 2026, 32 days from data cutoff). A possible **special California legislative session before year-end 2026** to revisit wildfire liability reform (CEO Pizarro: "a possibility," per the 2026-09-23 interview) — genuinely dated and binary. **Bellwether jury trial, January 2027** (first of what will likely be several, covering 8 plaintiffs). Ongoing: SCE's internal review of the fire's cause remains "complex and ongoing" per the 10-Q, so a company-side causation update could land at any time.

## 11. Red-flag scan

- **Felony liability**: the 10-Q explicitly discloses exposure to "felony liability with regards to the Eaton Fire," and states any resulting fines/penalties would **not** be recoverable from insurance, the Wildfire Fund, or rates (i.e., fully shareholder-borne). This is disclosed as a risk-factor-level exposure, not a confirmed charge — but it is a materially different (and more severe) category of risk than a civil damages exposure and should be tracked separately.
- **Going-concern language**: none found; the 10-Q and MD&A liquidity discussion assume continued access to capital markets, consistent with an investment-grade (if weak) rated entity.
- **Auditor changes / restatements / SEC-DOJ matters**: none identified this pass.
- **Insider selling pattern**: not pulled this pass (FMP insider-trading endpoints hit a session rate limit) — flagged `not available`, an open item for follow-up.
- **Litigation beyond Eaton**: the 10-Q separately discloses ongoing reserved exposure for 2017/2018 Wildfire/Mudslide Events (Thomas/Koenigstein/Montecito-era), including a still-unresolved CAL OES public-entity claim in the "TKM" litigation with a tolled statute of limitations — a smaller, longer-tail item layered on top of the much larger Eaton Fire exposure.

## 12. Sources

1. Edison International / SCE combined 10-Q, Q2 2026, filed 2026-07-30, accn 0000827052-26-000059 — https://www.sec.gov/Archives/edgar/data/827052/000082705226000059/eix-20260630.htm
2. SEC EDGAR filing index, CIK 0000827052, https://data.sec.gov/submissions/CIK0000827052.json (reviewed for filings 2025-01-01 to 2026-09-25)
3. SEC XBRL point-in-time extract, `v4\data\d3_xbrl_facts.parquet` (ticker EIX)
4. "Edison CEO Warns Wildfire Impasse Risks Higher Customer Bills," Bloomberg News via Claims Journal, 2026-09-23 — https://www.claimsjournal.com/news/national/2026/09/23/340299.htm
5. "Edison International downgraded to 'BBB-' by S&P on wildfire fund concerns," Investing.com, 2025-10-21 (secondary reporting of an S&P Global Ratings action; not independently re-verified on S&P's own site)
6. "Edison unlikely to escape liability in Eaton Fire lawsuit," Courthouse News Service, and Bloomberg Law coverage of the denied summary-judgment motion and the January 2027 bellwether trial date (2026)
7. "California wildfire liability bill dies without a vote," CalMatters, and "PG&E, Edison International Stocks Plunge on California Wildfire Bill," Bloomberg/24-7 Wall St, both ~2026-08-31/09-01, on the SB 492 failure and stock-price reaction
8. Internal preliminary quant ranking, `v4\outputs\lead_prelim_rank.csv`, and live snapshot, `v4\data\d4_live_snapshot.parquet`, both dated 2026-09-25 close — cross-check/navigation only, not source of record
9. `scripts/verify_data.py`, `scripts/ratios.py --sector utilities`, `scripts/valuation.py` output (finance-skills stock-analysis toolkit), run 2026-09-26 (intake JSON retained in `C:\Users\user\eqv4\cache\f5\EIX\`)

---
*Research only; not investment advice. Data-quality note: 17 of 18 headline datapoints checked traced to a primary or secondary-but-attributed source (`verify_data.py`, 94% Tier-1-3 coverage); the one aggregator-only figure (quant-model NTM P/E) is flagged wherever used. Material open items, disclosed rather than papered over: the Q2 2026 earnings-release guidance table (SEC server error, §5), exact terms of the 2025-2026 capital-markets issuances (§6), Q4 2024/Q4 2025 standalone quarterals (§4), the Q1 2025 EPS anomaly's precise driver (§4), and insider Form 4 pattern (§11). This dossier's ratios.py/valuation.py runs used a lower-precision balance-sheet input than the other two companies in this batch (see intake-file notes) given the time this name's qualitative legal/regulatory diligence required — a deliberate trade-off given the wildfire liability, not the balance sheet mechanics, is what actually decides this thesis.*

## Correction (verification DV14, 2026-10-08)

**Verdict unchanged: WATCH.**
1. Section 5 (guidance track record): the statement that EIX's Q2 2026 earnings exhibits were image-only slide decks, so guidance could only be taken from news, is wrong. Exhibit 99.1 of the 30 Jul 2026 8-K (acc 0000827052-26-000058, eix-2026x0730exx991.htm) is a full text earnings release. It states "Reaffirmed 2026 core EPS guidance of $5.90-$6.20" and "Continued confidence in delivering 5-7% core EPS growth from 2025-2030", and reports Q2 core earnings of $592m ($1.54 against $0.97) and GAAP EPS of $1.39 basic / $1.38 diluted. The numbers in the dossier were right; the sourcing caveat and the "only one data point" limitation do not stand. Equivalent text releases exist for the Q1 2026 (acc -41) and Q4 2025 (acc -10) 8-Ks, so the four-release track record can be completed from primary sources.
2. Section 4: the Q4 2025 row is derivable, not unavailable. FY2025 revenue $19,317m, net income $4,459m and diluted EPS $11.55 less the first three quarters give Q4 2025 revenue $5,213m, net income $1,848m, diluted EPS $4.78 (derived). This reinforces the dossier's warning that GAAP EPS is noisy.
3. Section 7: trailing GAAP P/E on FY2025 EPS of $11.55 is 4.6x (5.4x on TTM $9.69), not 5.7x; shareholders' equity at 31 Dec 2025 was $17,579m (not $17.3bn). Immaterial to the verdict.
4. Valuation method: the dossier uses price multiples and probability-weighted price scenarios without a discount rate or a cash-flow model, so the 5.17% Treasury test cannot be applied; the weighted value ($55.54) and scenario returns reproduce arithmetically. The binary Eaton Fire liability, not the multiple, drives WATCH, and the dossier's evidence supports it.
5. Verified unchanged: Eaton Fire $511m gross claims offset by $511m expected Wildfire Fund recovery (net $0); "unable to reasonably estimate a range of losses"; $4.3bn cap; ~$21bn fund capacity; felony-liability language; Parent covenant 0.70:1 with 0.66:1 actual; the 23.1% one-day fall on 31 Aug 2026 ($70.17 to $53.98).
