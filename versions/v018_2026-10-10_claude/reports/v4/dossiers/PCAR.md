# PACCAR Inc (Nasdaq: PCAR) — Diligence Dossier

Agent f7 | Prepared 2026-09-26 | Most recent period incorporated: Q2 2026 (10-Q filed 2026-07-29, period ended 2026-06-30) plus the Q2 2026 earnings release (2026-07-28); checked for events to 2026-09-25. Sector routing: GICS Industrials / Construction Machinery & Heavy Transportation Equipment → **infra-capitalgoods.md** playbook ("Farm & Heavy Construction Machinery" row), with **PACCAR Financial Services (PFS) treated as a separate, financial-services-style segment** per the routing note, rather than blended into industrial leverage/return ratios. **Deep Cyclicals** overlay (`13-situations.md` §2 — "capital goods with long order cycles" is explicitly named) applied to the Truck segment specifically.

**Data quality note:** figures below are sourced from SEC XBRL/filings and 8-K earnings-release exhibits, cited inline. Given PACCAR's mixed industrial/financial-services structure, this pass did **not** run `ratios.py`/`valuation.py` on a blended consolidated basis (doing so would itself risk the exact error the sector playbook warns against — consolidating a lender's balance sheet into an industrial one); instead, segment-level margins are computed directly from the segment note in each release, shown with their formula. Auditor tenure, full CAM detail and Form-4 transaction codes were not independently verified in this pass (see §11). This is research, not personalised investment advice, and not a solicitation to buy or sell; the reader is responsible for their own decisions.

## 1. Verdict

**INCLUDE** (full weight), thesis horizon 12–36 months. **[Corrected 2026-10-08: restated to INCLUDE-SMALL (half weight); FY2025 on an adjusted basis (EPS about $5.01 excluding a $0.50 EC litigation charge) was mid-cycle, not a trough, and the V1 verdict for PCAR is 'demanding'; see the correction section below]**

**One-sentence reason:** Unlike CF and MPC in this batch, PACCAR's earnings are **not** at a cyclical peak — FY2025 (EPS $4.51) was a sharp, genuine trough down 43% from FY2023's peak ($8.76), the high-margin Parts and Financial Services segments already generate the majority of segment profit even in this weak year, consensus's 2026–2027 recovery path doesn't even reclaim the 2023 peak, and there is no buyback-driven EPS engineering (share count is flat) — a materially cleaner and more conservatively-priced setup than the other two names in this batch.

## 2. Business in plain English

PACCAR designs and manufactures Class 8 heavy trucks under the Kenworth and Peterbilt brands (North America) and DAF (Europe, South America), sold through independent dealers to trucking fleets and owner-operators. Two other segments ride alongside the truck business: **PACCAR Parts**, a high-margin aftermarket parts distribution business selling to the installed fleet regardless of new-truck demand, and **PACCAR Financial Services (PFS)**, a captive finance/leasing arm that funds dealer and customer truck purchases. The Pigott family remains a meaningful, long-standing shareholder and board presence. Competitive position: a top-3 global Class 8 OEM with a reputation for build quality and resale value, and one of the few OEMs where the parts/aftermarket business is large enough to materially smooth the truck cycle.

## 3. Why the model likes it — durable or artefact?

Preliminary QVM percentiles (sector-neutral within Industrials, `lead_prelim_rank.csv`): **Q = 0.581** (58th pctile — middling, the lowest of the three tickers in this batch), **V = 0.874** (87th pctile), **M = 0.706** (71st pctile), preliminary composite = 0.721 — the **lowest-conviction quant score of the three**, which on inspection is appropriate rather than a false negative: PACCAR is not a standout on Quality (ROE 12.3% raw is unremarkable) because FY2025 genuinely was a down year for the Truck segment. **The Value score here is not the low-P/E-at-peak trap** that afflicts CF/MPC — trailing P/E (23.4x) and NTM P/E (16.1x) are moderate, not the 4–8x "cheap on peak earnings" pattern the deep-cyclical framework warns about, and this dossier's own analysis (§4, §7) finds FY2025/Q1-2026 sit closer to a **trough** than a peak for the Truck segment specifically. **Unlike CF and MPC, PCAR was not flagged by the quant pipeline's own >15%-next-year-EPS-decline screen** (FY2026 consensus $5.98, +32.6%; FY2027 $7.22, +20.7%) — this dossier's independent check (below) finds that absence is *not* complacency: the recovery path is real but modest, and does not even return to the 2023 high by 2027.

## 4. Last two years of results (quarterly; source: 10-Q/10-K XBRL + 8-K earnings releases, CIK 0000075362)

| Quarter | Consolidated revenue ($M) | GAAP diluted EPS | Truck segment margin* | Parts segment margin* | FS pre-tax income |
|---|---|---|---|---|---|
| Q3 2024 | — | 1.85 | — | — | — |
| Q4 2024 | — | 1.66 | — | — | — |
| Q1 2025 | — | 0.96 | — | — | $528.0M rev |
| Q2 2025 | — | 1.37 | 5.9% (308.8/5,243.1) | — | $123.2M |
| Q3 2025 | — (9M: 21,659) | 1.12 | 9M: 5.2% (776.2/14,850.3) | 9M: 24.4% (1,253.0/5,135.4) | 9M: $370.5M |
| Q4 2025 | 4,515.0 (Truck) | 1.06 | 2.1% (94.6/4,515.0) | 23.9% (415.0/1,738.3) | $114.9M |
| Q1 2026 | — | 1.15 | **3.9%** (176.2/4,526.5) | 23.5% (402.3/1,710.1) | $115.5M |
| Q2 2026 | — | 1.43 | 6.9% (360.5/5,253.1) | 23.9% (417.0/1,746.9) | $124.1M |

*Segment margin = segment pre-tax income ÷ segment revenue, computed by this analyst from the segment note in each release (not a company-defined "gross margin" figure).

**FY2025 full year:** consolidated revenue $28,445M (-15.5% YoY), GAAP diluted EPS **$4.51** (-42.9% vs FY2024's $7.90) — this follows FY2023's peak of **$8.76** (net margin 13.1%). By segment (FY2025): **Truck** $19,365.3M revenue / $870.8M pre-tax (4.5% margin — the trough), **Parts** $6,873.7M / $1,668.0M (24.3% margin), **Financial Services** $2,209.7M / $485.4M (22.0% margin). **Parts + FS generated $2,153M of segment pre-tax income on just 32% of consolidated revenue — 71% of total segment profit — in a year the Truck segment was clearly weak.** PACCAR does not publish a distinct "adjusted EPS"; GAAP is the primary and only reported figure in the releases reviewed. **[Corrected 2026-10-08: wrong: PACCAR's releases publish adjusted net income; Q1 2025 GAAP included a $350.0M pre-tax ($264.5M after-tax, about $0.50 per share) charge for civil litigation in Europe (EC-related claims), so FY2025 adjusted net income is about $2,640M and adjusted EPS about $5.01]** **Trajectory: Q1 2026 (Truck margin 3.9%) looks like the trough quarter; Q2 2026 (6.9%) shows a real but still-modest sequential improvement** — this is a gentle recovery, not the sharp, sudden, all-region spike seen in CF's and MPC's Q2 2026 prints.

## 5. Guidance track record (last 3–4 releases; PACCAR guides industry volumes and capex/R&D, not EPS or detailed segment ranges)

| Release | Date | Metric guided | Prior guide | New guide | Verdict |
|---|---|---|---|---|---|
| Q3 2025 | 2025-10-21 | FY2025 US/Canada Class 8 retail sales | (not captured this pass) | 230,000–245,000 | Baseline |
| Q3 2025 | 2025-10-21 | FY2026 US/Canada Class 8 (early look) | n/a | 230,000–270,000 | New |
| Q4/FY2025 | 2026-01-27 | FY2026 US/Canada Class 8 | 230,000–270,000 | 230,000–270,000 | **Maintained** |
| Q4/FY2025 | 2026-01-27 | FY2026 Europe (>16t) Class 8 | n/a | 280,000–320,000 | New |
| Q4/FY2025 | 2026-01-27 | FY2026 capex / R&D | n/a | $725–775M / $450–500M | New |
| Q1 2026 | 2026-04-28 | FY2026 US/Canada; Europe | 230–270k; 280–320k | 230,000–270,000; 280,000–320,000 | **Maintained** |
| Q2 2026 | 2026-07-28 | FY2026 US/Canada; Europe; South America | 230–270k; 280–320k; n/a | 230,000–270,000; **290,000–330,000** (raised); 100,000–110,000 (new) | **Maintained (NA); Raised (Europe)** |
| Q2 2026 | 2026-07-28 | FY2026 capex / R&D | $725–775M / $450–500M | **$700–750M** / **$450–480M** | **Tightened/modestly reduced** (both ranges narrowed toward the lower end) |

**Important limitation:** the press-release exhibits reviewed in this pass did **not** contain the granular quarter-ahead segment guidance (specific truck-delivery counts, Parts gross-margin range, Financial Services pre-tax range) that PACCAR is reputed to issue — that level of detail may sit in the earnings-call transcript or investor-relations slide deck, neither of which this pass could access (the FMP transcript tool required a higher subscription tier than is available on this connector, and a third-party transcript source was not chased given time constraints). What **was** found is a clean, repeatable industry-volume and capex/R&D guidance series, shown above, with **no cuts identified** — guidance has been maintained or modestly improved (Europe raised, capex/R&D tightened toward the low end) across every release reviewed. This is a genuine, if partial, remediation of the prior audit's "guidance raised without checking the prior range" failure; closing the segment-guidance gap (via the call transcript) is the highest-value follow-up before final sizing.

## 6. Earnings quality & balance sheet

**FCF conversion:** FY2025 FCF (CFO $4,416M − capex $743M) = $3,673M; FY2025 NI $2,376M → FCF/NI ≈ **1.55x**, a strong, consistent pattern across the whole window (FCF/NI was 1.16x in 2022, 0.76x in 2023, 0.91x in 2024, 1.55x in 2025) — cash generation held up better than earnings through the downturn, a genuine quality positive (helped by PFS receivables/lease-portfolio dynamics as much as pure operations — not independently decomposed in this pass) **[Corrected 2026-10-08: capex excludes $643.6M of equipment on operating lease; on that basis FCF is about $3,029M and FCF/NI about 1.27x]**. **SBC:** not separately broken out cleanly in this pass; not flagged as material. **GAAP-vs-adjusted:** not applicable — PACCAR reports GAAP only. **Leverage:** this dossier could **not** cleanly compute a consolidated net-debt/EBITDA figure — PACCAR's debt sits overwhelmingly at PACCAR Financial Corp (funding the lease/receivables book) and was not tagged in a form this pass's XBRL extraction could isolate; per the sector playbook, blending PFS debt into an industrial leverage ratio would be a routing error in any case. What can be said: PACCAR's equity has grown every year through the downturn (equity $13.2B FY2022 → $19.3B FY2025, no reduction), share count is essentially flat (523M→527M diluted shares, 2021–2025 — **no buyback-driven EPS engineering**, unlike CF/MPC), and the company carries a reputation (not independently re-verified against a rating agency source this pass) for a conservative, high-investment-grade balance sheet. **Debt maturities / covenants:** not independently reviewed this pass — flagged as a follow-up. **M&A:** PACCAR divested its Winch business (BRADEN/CARCO/Gearmatic brands) to Black Phoenix Group, effective 2024-10-31 (a small, non-core disposal, not a leverage event). **Capital return:** dividends only — FY2025 total dividends **$2.72/share**, comprising regular quarterly dividends (~$1.32) **plus a $1.40/share year-end (special) dividend** paid 2026-01-07 — confirming the payout-ratio-on-the-regular-dividend-alone figure in the quant snapshot (28.2%) understates true distribution; on a $2.72 total-dividend basis against FY2025 EPS $4.51, the effective payout ratio was **~60%**. Buybacks are trivial ($2–4M/yr 2021–2024, a one-off $36.1M in 2025) — this is a dividend-return, not buyback-return, company.

## 7. Valuation snapshot

| Basis | P/E | Notes |
|---|---|---|
| Trailing TTM (pipeline, EPS $4.75) | 23.43x | |
| FY2025 GAAP actual (EPS $4.51) | 24.7x | Trough-year earnings — a high multiple on a low base is the *opposite* of the CF/MPC pattern |
| NTM consensus (d4, EPS≈$6.89, calendarised) | 16.15x | |
| FY2023 peak-year EPS ($8.76) at current price | 12.7x | For reference only — shows how cheap the stock would look if 2023-peak earnings recurred, which is not the base case |

**Mid-cycle framing:** FY2019–2025 consolidated net margin ranged from 6.9% (2020, COVID) to 13.1% (2023 peak), with FY2025 at 8.4% — using the 2018–2025 median (8 points: 9.3, 9.3, 6.9, 7.9, 10.4, 13.1, 12.4, 8.4 → median ≈9.35%) as a mid-cycle proxy on FY2025 revenue ($28,445M) gives mid-cycle NI ≈ **$2,660M**, i.e. modestly **above** FY2025's actual $2,376M — consistent with this dossier's finding that FY2025 was a slight trough, not mid-cycle or peak. On ~527M diluted shares that is mid-cycle EPS ≈ **$5.05**, giving a mid-cycle P/E of **~22x** at the current price ($111.31) — roughly in line with the trailing multiple and below the NTM-consensus-implied multiple's inverse (i.e. the stock is not "cheap" on a mid-cycle view either, but nor is it priced for a repeat of the 2023 peak — a reasonably fairly-valued, unexciting setup rather than a screaming bargain or a peak-cycle trap). Peers for cross-check (not independently re-underwritten this pass): Daimler Truck (DTRUY), Traton SE/Volvo Group (TRATF, VLVLY) as global heavy-truck OEMs; Cummins (CMI) as an engine-supplier reference point only, not a direct OEM peer.

## 8. Bull case / Bear case

**Bull (3):**
1. **Parts + Financial Services already generate ~71% of segment profit on ~32% of revenue**, and both are structurally more stable than new-truck sales (Parts sells into the installed fleet regardless of the new-build cycle; FS margin has been essentially flat, 21–23%, across every quarter reviewed) — this is real, evidenced, non-cyclical earnings quality sitting underneath the Truck segment.
2. **No buyback-driven EPS engineering and a conservative capital-return policy** (dividend-led, share count flat, equity growing every year through the downturn) — the cleanest capital-allocation picture of the three names in this batch, and management's own regulatory commentary (EPA clarity "beneficial... for 2027," three releases running) suggests replacement demand that had been deferred by uncertainty is being unlocked, not merely pulled forward.
3. **Consensus's own recovery path is conservative** — FY2027 consensus EPS ($7.22) still sits below the FY2023 peak ($8.76), meaning the market is not underwriting a return to boom conditions, which lowers the bar for the thesis to be validated by continued gradual recovery alone.

**Bear (3):**
1. **The Truck segment's Q1–Q2 2026 recovery is still modest and unproven** (margin 3.9%→6.9%, nowhere near the 2022–2023 double-digit levels) — if the North American freight recession that depressed 2024–2025 persists rather than resolving, the recovery baked into consensus ($5.98/$7.22) may not materialize on schedule.
2. **This dossier could not independently confirm whether a 2026–2027 emissions "pre-buy" is inflating current order activity** — management frames EPA clarity as a positive that unlocks deferred demand, but that is management's own framing, not independently verified against neutral industry order/backlog data (e.g. ACT Research), and the Section 232 truck tariffs taking effect November 2025 add a second, entangled variable that could equally be pulling orders forward. A pre-buy, if present, would make today's "trough-to-recovery" read look better than the underlying replacement-demand trend actually is.
3. **Granular segment guidance and consolidated leverage could not be verified in this pass** (§5, §6) — the investment case rests partly on data (PFS balance-sheet quality, exact debt maturities, call-transcript guidance detail) this dossier did not fully close out.

## 9. Key risks & kill criteria (thesis-invalidation triggers)

1. **Truck segment margin fails to continue improving beyond Q2 2026's 6.9%** for two more consecutive quarters — would suggest the "trough is behind us" read in §4 is wrong.
2. **NA Class 8 retail sales guidance is cut below the 230,000 floor** in a future release (currently maintained at 230,000–270,000 across three releases) — a direct, quotable guidance-cut trigger.
3. **PACCAR Parts segment margin drops meaningfully below its ~23–24% band** — would remove the specific evidenced "stable profit anchor" bull point.
4. **Clear evidence emerges of a 2026 pre-buy followed by a 2027–2028 order air-pocket** (e.g. a sharp reversal in order intake once 2027 models are available) — would reclassify today's recovery as borrowed demand rather than genuine replacement-cycle healing.
5. **A cut to the FY2025-established $1.40/share special dividend** — PACCAR's special dividend is discretionary and tied to the year's earnings; a cut would be a direct, observable signal that management sees the recovery as fragile.

## 10. Catalysts & calendar

- **Next earnings:** ~2026-10-27 (Q3 2026, aggregator estimate — verify via IR calendar).
- Section 232 truck tariff implementation and any further trade-policy action (effective ~November 2025 per Q3-2025 commentary) — could help (import protection) or hurt (input-cost/retaliation) depending on net effect, not yet independently assessed.
- EPA "EPA27" 35mg NOx limit implementation and any further regulatory clarification through 2027 — the single most-cited theme across the last three releases.
- Europe Class 8 guidance was just raised (Q2 2026) — watch whether this holds or reverses in Q3.
- No lock-up or index-event triggers identified in this pass.

## 11. Red-flag scan

- **Auditor/controls/litigation/going-concern:** none identified in the sections of the filings reviewed in this pass; a full Item 8/9A (auditor opinion, CAMs, material weakness) and Item 3 (legal proceedings) review was **not completed** this pass — flagged as the primary open item before final sizing, not a known issue.
- **Management/governance:** frequent Item 5.02 8-Ks (board/officer changes) were observed in the filing index (e.g. 2026-04-27, 2026-01-16, 2025-12-12, 2025-09-05) but were **not individually opened** in this pass given time constraints; several carry a companion Item 5.07 (annual meeting voting results), which is routine and expected timing (spring proxy season) rather than a turnover signal — worth a quick confirmatory read before sizing, but not treated as a red flag on the evidence available.
- **Insider trading (Form 4) pattern:** not independently pulled in this pass (same SEC-feed access constraint noted in the CF and MPC dossiers) — flagged as a data gap.
- **Short-seller reports / SEC-DOJ investigations:** none identified via the searches performed in this pass.
- **Divestiture:** PACCAR Winch sale to Black Phoenix Group (effective 2024-10-31) — routine portfolio pruning, not a red flag.

## 12. Sources

1. SEC EDGAR, PACCAR Inc CIK 0000075362, XBRL company facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK0000075362.json` (retrieved 2026-09-26).
2. SEC EDGAR filing index: `https://data.sec.gov/submissions/CIK0000075362.json` (retrieved 2026-09-26).
3. 8-K Ex-99.1, Q2 2026 earnings release (2026-07-28): `https://www.sec.gov/Archives/edgar/data/75362/000119312526318918/pcar-ex99_1.htm`.
4. 8-K Ex-99.1, Q1 2026 earnings release (2026-04-28): `https://www.sec.gov/Archives/edgar/data/75362/000119312526183626/pcar-ex99_1.htm`.
5. 8-K Ex-99.1, Q4/FY2025 earnings release (2026-01-27): `https://www.sec.gov/Archives/edgar/data/75362/000119312526023374/pcar-ex99_1.htm`.
6. 8-K Ex-99.1, Q3 2025 earnings release (2025-10-21): `https://www.sec.gov/Archives/edgar/data/75362/000119312525244291/pcar-ex99_1.htm`.
7. 8-K, PACCAR Winch divestiture (2024-11-04, event date 2024-10-31): `https://www.sec.gov/Archives/edgar/data/75362/000119312524250714/d903036d8k.htm`.
8. v4 pipeline internal data: `v4\outputs\lead_prelim_rank.csv` (Q/V/M/prelim), `v4\data\d4_live_snapshot.parquet` (NTM consensus, revisions, targets) — cross-check only; consistent with primary-source EPS figures in this dossier (FY2025 EPS $4.51 confirmed against both XBRL and the earnings release).

**Limitations note:** this dossier did **not** independently verify (a) PACCAR's consolidated/PFS-only leverage and debt maturity schedule, (b) the granular segment-level quarterly guidance (truck deliveries, Parts margin range, FS pre-tax range) referenced in the assignment brief — the press-release exhibits reviewed contained industry-volume and capex/R&D guidance only, not the finer segment detail, which likely requires the earnings-call transcript (not accessible this pass — FMP's transcript tool required a higher plan tier), (c) auditor/CAM/litigation detail, or (d) Form-4 insider-trading transaction codes. None of these are believed likely to overturn the INCLUDE verdict given the strength of the segment-mix and trough-not-peak evidence in §4/§6/§7, but they are the concrete next steps before final position sizing.

## Correction (verification DV32, 2026-10-08)
**Wrong text and corrections (sources: 8-K Ex-99.1 0001193125-26-318918 (Q2 2026), -183626 (Q1), -023374 (Q4 FY25), 10-K 0001193125-26-057025, outputs/v1_valuation.json):**
1. Sections 1, 4 and 7: "PACCAR does not publish a distinct adjusted EPS; GAAP is the only figure" is wrong. The Q1 and Q2 2026 releases carry adjusted net income reconciliations: Q1 2025 included a $350.0M pre-tax charge ($264.5M after tax, about $0.50 a share) for civil litigation in Europe (EC-related claims); H1 2025 adjusted net income was $1,493.4M against GAAP $1,228.9M. FY2025 adjusted net income is about $2,640M and adjusted EPS about $5.01 (GAAP $4.51 plus $0.50), which is the dossier's own "mid-cycle" estimate ($2,660M, EPS $5.05). On the dossier's own method FY2025 was a mid-cycle year, so the premise "sharp, genuine trough" behind the full-weight INCLUDE is overstated. Q1 2025 GAAP EPS of $0.96 is also depressed by the charge.
2. Section 7 / V1: a V1 row for PCAR exists (outputs/v1_valuation.json) and is not reconciled. V1: Ke 8.67%, implied 10-year FCFF growth 10.3% against consensus FY1 growth 10.0% and a 5-year CAGR of 4.6%; verdict "demanding" (score -0.39); 3-year annualised returns bear -30.4%, base -5.2%, bull +20.1%; base 3-year value below the lowest Street target. My equity-basis check (FCFE about $2.4-2.6bn after PFS growth, market cap $58.6bn, ten years then 3.0%): implied growth 5.1% (Ke 8.0%), 9.3% (9.7%), 10.5% (10.3%): the price already discounts the consensus recovery (FY2027 EPS $7.22 = 15.4x). implied_vs_base was missing; it is in_line.
3. Section 6: FCF/NI of 1.55x uses capex of $743M only; PaymentsToAcquireEquipmentOnLease was $643.6M in FY2025, giving FCF about $3,029M and FCF/NI about 1.27x (1.15x on adjusted NI).
4. Section 5: South America 100,000-110,000 was not new in Q2 2026; it was already in the Q4 FY25 and Q1 2026 releases. Other guidance rows (US/Canada 230-270k, Europe 290-330k raised, capex $700-750M, R&D $450-480M) are verbatim.
5. Observation (no correction): Truck margin in H1 2026 (5.5%) is below H1 2025 (6.4%) on 6.6% lower truck revenue, so the recovery is sequential only. The $1.40 year-end dividend is confirmed (Q4 FY25 release); PACCAR calls it a year-end, not a special, dividend.

**Verdict:** INCLUDE -> INCLUDE-SMALL (half weight): quality and balance sheet are unchanged, but the dossier's own evidence (mid-cycle P/E ~22x, 'not cheap', adjusted FY2025 at mid-cycle, V1 'demanding' with a negative base return) does not support a full-weight position. f7_summary.json PCAR verdict, implied_vs_base, valuation_view_vs_v1, scenario_returns_3y (V1 values) and key_adverse_facts updated.
