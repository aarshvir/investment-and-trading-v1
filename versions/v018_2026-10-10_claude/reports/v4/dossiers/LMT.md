# LMT — Lockheed Martin Corporation

**Recency gate:** most recent period incorporated: Q2 2026 (period ended 2026-06-28), 10-Q filed 2026-07-23, 8-K/EX-99.1 filed 2026-07-23. Checked EDGAR for subsequent filings to 2026-09-25: an 8-K dated 2026-08-28 (report date 2026-08-24; items 1.01/9.01 — plausibly the Ultra Maritime acquisition definitive agreement or related financing) and several Forms 4/144 were found but **not reviewed** in this pass (time-boxed session) — flagged as an open item. **[Corrected 2026-10-06: resolved by DVH4: the 8-K of 2026-08-28 (acc 0001193125-26-371750) is a new $2.25 billion 364-day revolving credit agreement replacing the 5 Dec 2025 facility, not the Ultra Maritime agreement; Ultra Maritime ($3.45 billion, announced 6 Jul 2026, cash plus additional financing, expected to close Q4 2026) is described in the Q2 10-Q, acc 0001628280-26-049411]** No toolkit scripts (`verify_data.py`/`lint_report.py`) were run this pass given a hard session time limit; every figure below carries an inline source/period/GAAP-vs-non-GAAP label as a substitute control.

## 1. Verdict
**INCLUDE-SMALL** (half weight) — thesis horizon 24–36 months. Record, fast-growing backlog (missile demand in particular) and disciplined capital return are real and primary-sourced, but they sit against **two consecutive fiscal years of large, disclosed program-execution charges across at least four distinct programs** — a genuine, repeated pattern, not a one-off, which the quant "earnings-surprise" signal likely overstates (§3). Confidence: medium.

## 2. Business
Lockheed Martin is the world's largest defense prime, organized in four segments: **Aeronautics** (F-35, F-16, F-22 sustainment, C-130J, classified programs — largest segment), **Missiles and Fire Control/MFC** (PAC-3, THAAD, HIMARS, JASSM, LRASM, PrSM — fastest-growing, highest-margin segment), **Rotary and Mission Systems/RMS** (Sikorsky helicopters: Black Hawk, Seahawk, CH-53K, plus naval/radar systems), and **Space** (national-security space, GPS III, NASA Orion/Artemis). Customers are predominantly the U.S. government (majority DoD) plus foreign military sales/allied exports, under long-duration cost-type and fixed-price-incentive contracts. *(Source: 8-K EX-99.1 releases, segment descriptions; SEC EDGAR CIK 0000936468.)*

## 3. Why the model likes it — durable or artefact?
b1 factor scores (2026-09-25): composite 0.922 (decile 10, live_rank 39), fam_Q 0.681, fam_V 0.728, fam_M 0.598, **fam_S (earnings surprise) 0.826**.
- fam_Q/fam_V look durable: raw ROE 71.7% (small equity base + buybacks), FCF-yield percentile 88%, EBIT/EV percentile 77%, accruals percentile 83% — consistent with the real, filed backlog and cash-generation data in §6.
- **fam_S is very likely partly an artefact, and this is the central data conflict for this name.** Recent quarters "beat" prior-year comps mechanically because the **prior-year quarters themselves were depressed by one-time-like classified/international-program charges** (Q4'24 and Q2'25 — see §6). E.g., Q2'26 EPS of $7.94 vs Q2'25's $1.46 is a real result, but the comparison base was a charge quarter, not a clean baseline — the y/y "surprise" overstates underlying demand acceleration. The genuinely durable positive is the **backlog** trend (§6), which is independent of this base-effect distortion. Flagged for the quant team: SUE construction may not adequately control for disclosed one-time items in choppy-earnings names.

## 4. Last 8 quarters (GAAP unless labeled; $ in billions except EPS/margin)
| Quarter | Net sales | Segment op. profit (non-GAAP)¹ | GAAP diluted EPS | OCF | FCF (non-GAAP)¹ |
|---|---|---|---|---|---|
| Q3'24 | $17.1B | n/a this pass | $6.80 | $2.4B | $2.1B |
| Q4'24 / FY24 | $18.6B / $71.0B | $6,083M reported / **$7,893M adjusted** (ex $2.0B classified charges) | $2.22 (incl. $5.45 classified-charge impact) / **FY $22.31 reported vs $27.99 adjusted** | $1.0B (after $990M pension contrib.) | $441M |
| Q1'25 | $18.0B | n/a | $7.28 | $1.4B | $955M |
| Q2'25 | $18.2B | $571M (incl. **$1.6B program losses + $169M other charges**) | $1.46 (incl. $5.83/sh combined charge impact) | $201M | **$(150)M** |
| Q3'25 | $18.6B | n/a | $6.95 | $3.7B | $3.3B |
| Q4'25 / FY25 | $20.3B / — | — | $5.80 / **FY $21.49** (incl. $1.63/sh pension-settlement charge in Q4) | $3.2B (after $860M pension contrib.) | $2.8B |
| Q1'26 | $18.0B | $1,823M | $6.44 (down YoY on F-16/C-130 unfavorable adjustments + working-capital timing) | $220M | **$(291)M** |
| Q2'26 | $20.1B | $2,162M (vs $571M Q2'25 — easy comp) | $7.94 | $3.2B | $2.9B |

¹ "Business segment operating profit" and "Free cash flow" are non-GAAP measures the company itself so labels in every release; reconciliations are in the source press releases. Segment detail, Q2'26 vs Q2'25 (both GAAP-segment, $M): Aeronautics sales $8,112/$7,420 (margin 9.4% vs op. **loss** $(98)M i.e. −1.3%), MFC sales $4,101/$3,433 (margin 14.5% vs 14.0%), RMS sales $4,354/$3,995 (margin 10.0% vs op. **loss** $(172)M i.e. −4.3%), Space sales $3,496/$3,307 (margin 10.6% vs 10.9%). *(Source: 8-K EX-99.1 for each quarter cited; CIK 0000936468.)*

## 5. Guidance track record (initial + every update; last 4 in bold)
| Release | Sales | Segment op. profit¹ | Diluted EPS | FCF¹ |
|---|---|---|---|---|
| Q3'24 update (2024-10-22) | ~$71,250M (vs Jul $70,500–71,500M, maintained) | ~$7,475M (vs $7,350–7,500M, maintained/high end) | ~$26.65 (vs $26.10–26.60, **raised**) | ~$6,200M (vs $6,000–6,300M, maintained) — premised on F-35 Lots 18–19 funding arriving in Q4'24 |
| FY24 actual vs guide | $71,043M (in line) | $6,083M reported / $7,893M adjusted (adj. ≈ high end of guide) | $22.31 reported / **$27.99 adjusted** (adj. beat the $26.65 update) | $5,287M reported / $6,122M adjusted (adj. within guide) |
| FY25 initial (2025-01-28) | $73,750–74,750M | $8,100–8,200M | $27.00–27.30 | $6,600–6,800M |
| Q1'25 (2025-04-22) | unchanged | unchanged | unchanged | unchanged — **maintained** |
| Q2'25 (2025-07-22) | unchanged $73,750–74,750M | **$6,600–6,700M — cut from $8,100–8,200M (~$1.5B)** | **$21.70–22.00 — cut from $27.00–27.30 (~$5.35/sh)** | unchanged $6,600–6,800M (mgmt explicitly held sales/OCF/capex/FCF/buyback guidance flat despite the profit-line cut) |
| **Q3'25 (2025-10-21)** | $74,250–74,750M (raised from $73,750–74,750M) | $6,675–6,725M (raised from $6,600–6,700M) | $22.15–22.35 (raised from $21.70–22.00) | ~$6,600M (trimmed to low end of $6,600–6,800M; flagged govt-shutdown and pension-conversion-charge risk in advance) |
| **Q4'25/FY25 actual + FY26 initial (2026-01-29)** | FY25 actual $20.3B Q4 / EPS $21.49 FY (~in line with Q3'25 guide once the $1.63 non-operational pension charge is excluded: $21.49+$1.63=$23.12 > $22.15–22.35 guide — beat) | FY26: $8,425–8,675M | FY26: $29.35–30.25 | FY26: $6,500–6,800M |
| **Q1'26 (2026-04-23)** | $77,500–80,000M — **reaffirmed unchanged** despite a weak Q1 (negative FCF) | $8,425–8,675M reaffirmed | $29.35–30.25 reaffirmed | $6,500–6,800M reaffirmed |
| **Q2'26 (2026-07-23)** | $79,750–81,750M (raised from $77,500–80,000M) | $8,500–8,700M (raised from $8,425–8,675M) | $29.95–30.65 (raised from $29.35–30.25) | $7,000–7,200M (raised from $6,500–6,800M; capex guide *lowered* to $2,000–2,400M from $2,500–2,800M) — excludes pending Ultra Maritime acquisition |

*(Source: 8-K EX-99.1 "Financial Outlook" tables, each release cited.)*

## 6. Earnings quality & balance sheet — classified/program charge history (critical section)
This is the central adverse-fact set for LMT, all company-disclosed and GAAP (segment operating profit and FCF are labeled non-GAAP by the company; classified-program losses hit **both** GAAP and non-GAAP segment operating profit):
- **FY2024 (Q4):** $1.7B pretax Q4 / $2.0B pretax FY ($1.3B/$5.45 per sh and $1.5B/$6.16 per sh after-tax). Aeronautics classified fixed-price-incentive program: $410M Q4 / $555M FY cumulative loss (design/integration/test issues; "may have to record additional losses"). MFC classified cost-reimbursable-plus-fixed-price-options program: additional $1.3B Q4 / $1.4B FY — company "now believe[s] it is probable that all options will be exercised" at a loss.
- **Q2 2025:** $1.6B pretax program losses + $169M other charges (~$5.83/sh combined). The **same** Aeronautics classified program: additional $950M reach-forward loss (issues "continued into 2025" with "greater impact...than previously estimated" — i.e., a chronic, not resolved, problem). RMS/Sikorsky international helicopter programs: CMHP (Canada Maritime Helicopter Program) $570M loss, TUHP $95M loss (programs being renegotiated with customers). Other: $66M fixed-asset write-off from losing the NGAD fighter down-select, $103M IRS uncertain-tax-position charge. Cash from ops fell to $201M and **FCF went negative $(150)M** — yet management explicitly held sales/OCF/capex/FCF/buyback guidance unchanged, characterizing the charges as non-cash-guidance-relevant.
- **Q4 2025:** $479M pension-settlement charge ($377M/$1.63 per sh after-tax) on a $943M pension risk-transfer to insurers — non-operational, de-risking, one-time.
- **Q1 2026 (smaller, same pattern, MD&A disclosure not press-release-headlined):** $125M unfavorable F-16 profit adjustment (production performance/development delays), $55M unfavorable C-130 adjustment ("diminishing manufacturing source integration challenges and associated delivery delays"), further Sikorsky (CH-53K/Seahawk/Black Hawk) unfavorable adjustments. **C-130J deliveries collapsed from 21 units (FY24) to 2 units (FY25).**
- **Net effect:** roughly $4.25B of disclosed pretax charges across FY2024–2025 touching Aeronautics (classified), MFC (classified), RMS/Sikorsky (three separate helicopter lines), F-16 and C-130J — a broad, recurring execution-risk pattern, not an isolated event. **[Corrected 2026-10-06: the $4.25B includes the $479M non-operational pension settlement; program and other operating charges total about $3.8B]** It cannot be ruled out from public filings that the still-active classified Aeronautics contract produces further reach-forward losses.
- **Backlog** (total, $B): Sep'24 165.7 → Dec'24 176.0 → Dec'25 193.6 → **Jun'26 230.4** (+31% in two quarters). By segment, MFC backlog **nearly doubled**: Dec'25 $46.7B → Jun'26 $87.9B, on multi-year missile-production framework agreements (Patriot/THAAD/PrSM, aiming for "3–4x current production rates" per Q1'26 commentary). Aeronautics backlog, by contrast, has **declined for two straight periods**: Dec'24 $62.8B → Dec'25 $59.4B → Jun'26 $54.4B.
- **F-35 deliveries:** FY24 110 (depressed by delayed Lot 18–19 funding) → FY25 191 (catch-up) → H1'26 51 vs H1'25 97 (**-47% YoY**) — a sharp deceleration to monitor.
- **Capital deployment:** FY25 dividends $3.1B (Q4 $799M); buybacks $3.0B/6.6M shares (Q4 $750M/1.6M shares); total buyback authorization raised to $10.3B (Oct 2024). Dividend raised for **23 consecutive years** (2024: +5%). FAS/CAS non-cash pension adjustment (reconciles segment to consolidated GAAP operating profit) ~$1,125M (2025) growing to ~$1,365M (2026 guide) — a real but non-cash tailwind to consolidated GAAP earnings, worth excluding when judging segment-level execution. **[Corrected 2026-10-06: Lockheed made no share repurchases in H1 2026 (cash flow statement: nil vs $1,250M in H1 2025; Q2 10-Q Item 2)]**
- **Budget risk (explicit, company-disclosed):** FY2025 guidance was conditioned on the "full year Continuing Appropriations and Extensions Act of 2025" (a CR, not a full-year budget) and excluded tariffs, the NGAD decision and executive orders; Q3'25 guidance excluded "potential impacts of government shutdown." FY2026 guidance excludes the pending Ultra Maritime acquisition. *(Source: 8-K EX-99.1 releases, "Earnings Impacts of Classified Program Losses," "Program Losses and Other Charges," "Backlog," "Aircraft Deliveries" tables, each quarter cited.)*

## 7. Valuation snapshot (per `v4/outputs/v1_valuation_table.csv`, 2026-09-25)
NTM P/E **16.16x** vs own-history percentile 31.1% (cheaper than usual) vs peer median 18.81x (**~14% discount to peers**, plausible given two years of charge-driven GAAP EPS volatility). Reverse-DCF implied growth **−5.15%** vs delivered-5y growth +2.88% vs consensus FY1 growth +5.61% — the price implies *less* growth than even LMT's own modest recent trend, consistent with an undemanding, not expensive, valuation (not independently re-derived this pass) **[Corrected 2026-10-06: DVH4 re-derived on the programme basis (Ke 6.82%, equity value $119.9bn, FCF after SBC $8.39bn TTM): implied growth -4.7%/yr, or -2.1%/yr on the FY26 FCF guide, so V1's -5.15% reproduces]**. WACC/CoE 7.05%. Scenario 3y annualized: bear −10.8% / base +4.1% / bull +28.8%. Street flag: "within Street 12m target range" (no red flag). SBC-adjusted FCF yield 7.0%. Verdict: **fair**, score 0.26 — meaningfully lower conviction than a typical "attractive" name, consistent with the charge history above.

## 8. Bull case / Bear case
**Bull:** (1) Backlog at an all-time high ($230.4B, +31% in two quarters), with MFC backlog nearly doubling on funded, multi-year missile-production framework agreements against a structurally elevated global missile-defense demand backdrop. (2) The FY24/Q2'25 charge quarters appear to be flowing through (reach-forward-loss accounting front-loads the full remaining loss), and post-charge quarters (Q3'25 EPS $6.95, Q4'25 $5.80, Q2'26 $7.94; OCF/FCF rebounding to $2.8–3.7B/quarter) show real recovery, with guidance raised twice in 2026. (3) Capital-return discipline intact through the charge-heavy period: 23 consecutive years of dividend growth, $3.0B FY25 buybacks against a $10.3B authorization, FY26 FCF guide raised to $7.0–7.2B. **[Corrected 2026-10-06: no shares were repurchased in H1 2026 (10-Q), so 'discipline intact' applies to FY25 only; a $3.45bn acquisition to be funded with cash and new financing is pending]**

**Bear:** (1) The charge pattern spans **two consecutive fiscal years and at least four programs/business units** (Aeronautics classified ×2, MFC classified, RMS/Sikorsky ×2, plus newly disclosed F-16/C-130J issues) — a genuine, recurring pattern of cost-estimation and execution risk, and by definition classified-program specifics cannot be independently verified from public filings. (2) F-35 delivery cadence decelerated sharply in H1 2026 (-47% YoY) exactly as Aeronautics segment backlog has declined for two straight periods — the largest, historically most stable program may be plateauing in volume terms. (3) A single quarter (Q2 2025) saw ~$1.5B of segment-operating-profit guidance and ~$5.35/sh of EPS guidance cut at once — a scale of in-year revision that is a fair challenge to how much program-level visibility management has when it first frames annual guidance.

## 9. Key risks & kill criteria
1. Any newly disclosed reach-forward/classified-program charge exceeding ~$300M pretax in a single quarter.
2. Aeronautics segment backlog falling below the 2026-06-30 level of $54.4B at the next 10-Q (a third consecutive decline).
3. Full-year 2026 F-35 deliveries pacing materially below the ~150–155 unit run-rate implied by FY2025's 191 (e.g., under ~100–110 units through Q3 2026).
4. A guidance **cut** (not reaffirmation) to FY2026 sales, segment operating profit, or FCF at either of the next two earnings releases.
5. A continuing resolution or government shutdown lasting beyond one quarter that management explicitly attributes a revenue/cash shortfall to.

## 10. Catalysts & calendar
Q3 2026 earnings expected on/about 2026-10-20 (unconfirmed estimate from historical mid-to-late-October pattern). Pending Ultra Maritime acquisition (announced, excluded from FY26 guidance) — closing/financing terms are a near-term catalyst; the 2026-08-28 8-K (items 1.01/9.01) likely relates to this and was **not reviewed** this pass. **[Corrected 2026-10-06: the 8-K is a $2.25 billion 364-day revolver renewal (acc 0001193125-26-371750); the Ultra Maritime agreement dates from 6 Jul 2026]** FY2027 budget/appropriations process (CR vs. full-year enactment) is a recurring Q1-timed macro risk. Further pension risk-transfer transactions have been flagged by management as recurring optionality.

## 11. Red-flag scan
Two consecutive fiscal years of large classified/international-program losses across ≥4 programs (§6) is the dominant, already-disclosed red flag — not a future risk but a present, repeated pattern. C-130J deliveries collapsed 21→2 units on disclosed supply-chain ("diminishing manufacturing sources") issues. No auditor change, restatement, going-concern language, or SEC/DOJ investigation was identified in sources reviewed, but a full FY2025 10-K critical-audit-matters, related-party, and Form 4 insider-pattern review was **not completed** this pass (time-boxed) — flagged as a coverage gap, not a clean bill. Whether FY2025 actually delivered the reaffirmed cash-flow guidance was not independently recomputed from the FY total column this pass — a to-do for the audit agent.

## 12. Sources
1. SEC EDGAR CIK 0000936468, submissions JSON: https://data.sec.gov/submissions/CIK0000936468.json (retrieved 2026-09-26)
2. 8-K/EX-99.1 Q3'24 (2024-10-22): .../000093646824000107/ex991q32024.htm
3. 8-K/EX-99.1 Q4'24/FY24 (2025-01-28): .../000093646825000006/ex991q42024.htm
4. 8-K/EX-99.1 Q1'25 (2025-04-22): .../000093646825000031/ex991q12025.htm
5. 8-K/EX-99.1 Q2'25 (2025-07-22): .../000162828025035502/ex991q22025.htm
6. 8-K/EX-99.1 Q3'25 (2025-10-21): .../000162828025045582/ex991q32025.htm
7. 8-K/EX-99.1 Q4'25/FY25 (2026-01-29): .../000162828026003970/ex991q42025.htm
8. 8-K/EX-99.1 Q1'26 (2026-04-23): .../000162828026026683/ex991q12026.htm
9. 8-K/EX-99.1 Q2'26 (2026-07-23): .../000162828026049277/ex991q22026.htm
10. v4/data/b1_live_scores.csv (as_of 2026-09-25); v4/outputs/v1_valuation_table.csv, v1_valuation.json

## Data basis, recency and disclaimer

- Most recent reported period incorporated: Q2 2026 (quarter ended 2026-06-30) **[Corrected 2026-10-06: the quarter ended 2026-06-28]**, from the 10-Q and 8-K Exhibit 99.1 cited above; events checked through 2026-09-25 (US close).
- Reporting basis: consolidated US GAAP figures in USD millions unless explicitly labelled adjusted/operating (company non-GAAP) or per share.
- Research, not personalised investment advice; the author is not a licensed adviser.

## Correction (verification DVH4, 2026-10-06)

**Sources: Lockheed Martin (CIK 936468) 8-K Ex-99.1 releases acc 0001628280-26-049277 (Q2'26), -026683 (Q1'26), -003970 (Q4'25), 0001628280-25-045582 (Q3'25), -035502 (Q2'25), 0000936468-25-000031 / -000006 / 0000936468-24-000107; 10-Q acc 0001628280-26-049411; 8-K acc 0001193125-26-371750; XBRL company facts.**

Verified without change: every quarterly row and period label, the segment results, all eight guidance rows (verbatim), the FY24 and Q2'25 charge amounts and per-share impacts, backlog by segment, F-35 and C-130J deliveries.

1. **Capital return (FAIL).** Wrong: "capital-return discipline intact through the charge-heavy period" (bull case 3). Correct: the FY25 figures are right, but the Q2 10-Q and cash flow statement show no share repurchases in H1 2026 (H1 2025: $1,250M) and a $3.45bn acquisition (Ultra Maritime, signed 6 Jul 2026, cash plus additional financing, close expected Q4 2026) is pending.
2. **Unreviewed 8-K (FAIL, now resolved).** The 8-K of 2026-08-28 is a new $2.25 billion 364-day revolving credit agreement (24 Aug 2026), replacing the 5 Dec 2025 facility. It is not the Ultra Maritime agreement.
3. **Charge total (MINOR).** $4.25B includes the $479M non-operational pension settlement; program and operating charges are about $3.8B. A period label in the data-basis bullet (2026-06-30) should be 2026-06-28.
4. **Valuation re-derivation (programme basis).** Ke = 5.17% + 0.400 (Blume of raw 0.104) x 4.14% = 6.82%; equity value $119.9bn; TTM FCF $8,729M (FY25 6,908 - H1'25 805 + H1'26 2,626) less SBC $343M. Implied FCF growth for ten years then 3.0%: -4.7%/yr (-2.1% on the FY26 guide of $7.0-7.2bn; -0.6% to +2.2% at Ke 8.5%). V1's -5.15% reproduces. Implied growth is below delivered (+2.9%) and consensus (+5.6%) growth on every basis, but TTM FCF is flattered by H1'26 receipt timing and lower tax payments and the Ke rests on a near-zero beta. The dossier gives no implied_vs_base; the register shows "in_line" (from V1's +4.1% base return); the programme-basis test points to "below". Not restated here; left for the lead to reconcile.
5. Not verifiable on EDGAR: 23 years of dividend growth; the Q3 date (d4 estimate 2026-10-20).

**Verdict:** INCLUDE-SMALL unchanged; scenarios and implied_vs_base not changed. f11_summary.json LMT entry updated: key_adverse_facts[6], data_conflicts[1] and confidence reason (text only).
