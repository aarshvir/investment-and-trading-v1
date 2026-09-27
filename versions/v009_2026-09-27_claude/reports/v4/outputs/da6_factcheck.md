# DA6 — Adversarial data audit: dossier facts (current-holdings coverage completion)

**As of:** 2026-09-26 · **Scope:** the 7 current-holding dossiers no independent checker had yet verified: **BR, CMCSA, BKNG, DG, NOW, BX, EG**. 4 load-bearing facts per dossier = **28 facts checked**. Facts were deliberately chosen to be the ones most likely to be wrong — adjusted-vs-GAAP splits, fiscal-period/date labels, guidance deltas, and deal/litigation status as of 2026-09-25 — rather than a random sample. **Method:** primary sources only — SEC EDGAR 8-K Ex-99.1 earnings releases, 10-Q/10-K text and legal-opinion exhibits, fetched directly from `www.sec.gov`/`data.sec.gov` and cited by accession number below; one fact (a DOL/OSHA settlement figure) was cross-checked against the official settlement-agreement PDF published on dol.gov, a primary government legal document, because the underlying fact is a regulatory settlement rather than an SEC-filed item.

## Top-line result

**28 facts checked: 23 PASS, 1 CONFIRMED (a previously-flagged known issue, now resolved with an exact accession number), 1 MINOR, 2 FAIL, 1 UNVERIFIABLE.** Strict pass rate (PASS + CONFIRMED) = 24/28 = **85.7%** (89.3% counting the MINOR as acceptable). This is a somewhat lower clean-pass rate than DA5 found in its own batch (96.9% on core facts) — driven by two real, quotable, load-bearing misses (BR's CQG deal-size claim, DG's litigation-timeline claim), not by any pattern of GAAP/adjusted mislabeling, which continues to check out cleanly across all seven names.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | BR | FY2026 revenue $7,477m; diluted EPS $9.60 = Adjusted EPS $9.60 (unusual convergence) | 8-K Ex-99.1, accn 0001383312-26-000022 | PASS |
| 2 | BR | CQG acquisition completed "1 May 2026"; deal size "not disclosed" | 8-K Ex-99.1, accn 0001383312-26-000013 (Subsequent Event note) | **FAIL** |
| 3 | BR | Dividend +12% to $4.36; "14th double-digit increase in 15 years" | Same accn 0001383312-26-000022 | PASS |
| 4 | BR | FY2027 initial guide: 6–8% recurring-rev growth / 8–12% adj. EPS growth | Same accn 0001383312-26-000022 | PASS |
| 5 | CMCSA | 29-Jun-2026: NBCUniversal+Sky spin-off; Comcast retains up to 19.9% for up to 1 year | 8-K Ex-99.1, accn 0000950103-26-009591 | PASS |
| 6 | CMCSA | Q2'26 Peacock first-ever profitable quarter, $189m EBITDA, 48m subs | 8-K Ex-99.1, accn 0001628280-26-049274 | PASS |
| 7 | CMCSA | Q2'26 GAAP EPS $0.99 (NI −68% yoy); Adjusted EPS $1.04, −16.7% yoy | Same accn 0001628280-26-049274 | PASS |
| 8 | CMCSA | Versant separation completed 2-Jan-2026 | Same accn 0001628280-26-049274 | PASS |
| 9 | BKNG | 25-for-1 forward split effective 2-Apr-2026; split-adjusted trading from 6-Apr-2026 | 8-K, accn 0000950157-26-000465 | PASS |
| 10 | BKNG | Q2'26 GAAP EPS $2.53 (+131%); Adjusted EPS $2.54 (+15%) | 8-K Ex-99.1, accn 0001075531-26-000036 | PASS |
| 11 | BKNG | FY2026 guide: Adjusted EPS growth "low-to-mid teens" | Same accn 0001075531-26-000036 | PASS |
| 12 | BKNG | Stockholders' deficit −$10,783m at Q2'26 | 10-Q, accn 0001075531-26-000037 | PASS |
| 13 | DG | Q2 FY26 diluted EPS $2.48 (+33.3%); 6th straight quarter of positive all-category comps | 8-K Ex-99, accn 0001104659-26-101918 | PASS |
| 14 | DG | FY26 EPS guide raised to $7.80–$8.00 (from $7.20–$7.45), incl. ~$0.25 tariff-refund benefit | Same accn 0001104659-26-101918 | PASS |
| 15 | DG | Washtenaw securities suit: dismissed w/o prejudice "2026-06-23"; motion for leave to amend pending as of Aug-2025 | 10-Q, accn 0001104659-26-101932 (Legal Proceedings) | **FAIL** |
| 16 | NOW | [Flagged issue] Moveworks $2.85bn deal "signed but under DOJ 2nd request, not closed" | 8-K, accn 0001373715-25-000329, Ex-5.1 | **CONFIRMED — closed 2025-12-15** |
| 17 | NOW | Q2 FY26 subscription guide raised to $15,760–15,780m (22.5%); margins held 31.5%/35% | 8-K Ex-99.1, accn 0001373715-26-000072 | PASS |
| 18 | NOW | Q2 FY26 total revenue $3,987m (+24%); cRPO $13.20bn (+21%) | Same accn 0001373715-26-000072 | PASS |
| 19 | NOW | [Self-flagged data gap] DOJ/Army-CIO investigation still open, company cooperating | 10-Q, accn 0001373715-26-000076 (Legal Proceedings) | PASS (gap closed) |
| 20 | BX | Q2'26 DE $1.52/sh; FRE $1.43/sh; GAAP NI attributable ~$1.2bn | 8-K Ex-99.1, accn 0001193125-26-313250 | PASS |
| 21 | BX | Q2'26 dividend raised to $1.29/share | Same accn 0001193125-26-313250 | PASS |
| 22 | BX | Fee-earning AUM $961.6bn at Jun-26 (+8% yoy) | Same accn 0001193125-26-313250 | PASS |
| 23 | BX | Standalone LT debt $11.5bn (Dec-24)→$13.3bn (Jun-26); payout ratio ~85% of DE | 10-Q accn 0001193125-26-340208 / 8-K arithmetic check | UNVERIFIABLE |
| 24 | EG | Q3'25 $478m reserve charge, +12.4pts, 103.4% combined ratio; $1.2bn Longtail Re ADC eff. 1-Oct-25 | 8-K Ex-99.1, accn 0001095073-25-000077 | PASS |
| 25 | EG | Q2'26 combined ratio 92.0%; $33m YTD favorable development | 8-K Ex-99.1, accn 0001095073-26-000029 | PASS |
| 26 | EG | Q2'26 net premiums written −26.3% yoy | Same accn 0001095073-26-000029 | PASS |
| 27 | EG | Book value/share $398.83 (Jun-26) vs "$379.70" (Dec-25) | Same accn 0001095073-26-000029 | MINOR |
| 28 | DG | OSHA corporate-wide settlement "$12 million," July 2024 | DOL/OSHRC settlement agreement PDF (dol.gov), 24-1174-NAT | PASS |

## 2. The FAILs, in full

### 2a. BR — CQG deal size claimed "undisclosed"; it isn't (#2)

**Claim in dossier (BR.md §6 and §11):** *"CQG (futures/options execution and market connectivity) completed 1 May 2026; deal size not disclosed, explicitly stated by the company as not expected to be material to results."* / *"CQG acquisition: financial terms undisclosed by the company... the lack of disclosed purchase price is itself noted for completeness."*

**What the primary source actually says:** Broadridge's own Q3 FY2026 8-K Ex-99.1 (accession 0001383312-26-000013, filed 2026-04-30), in its "Subsequent Event" note: *"On April 30, 2026, the Company completed the acquisition of CQG, Inc. ('CQG')... The total purchase price was approximately $173 million plus additional contingent consideration."*

This contradicts the dossier on two points: (1) the completion date is April 30, 2026 per the company's own SEC filing, not May 1, 2026 as stated in the dossier (a one-day slip, likely inherited from a press-release dateline rather than the primary filing); and (2) the purchase price *was* disclosed — approximately $173 million plus contingent consideration — directly contradicting the dossier's repeated, explicit claim (made twice, once as a standalone red-flag item) that the price was never given.

**Correct value:** CQG acquisition completed **April 30, 2026**; total purchase price **≈$173 million plus additional contingent consideration**, per Broadridge's own 8-K.

**Exact dossier lines to fix:** BR.md §6, "M&A" bullet ("CQG... completed 1 May 2026; deal size not disclosed...") and §11, "CQG acquisition" bullet ("financial terms undisclosed by the company...").

### 2b. DG — shareholder-suit timeline is a year stale, and understates where the case actually stands (#15)

**Claim in dossier (DG.md §11, §9 kill criterion 5, §10 catalysts):** the *Washtenaw County* securities suit was "dismissed... without prejudice on **2026-06-23**; lead plaintiffs filed a motion for leave to amend on 2025-08-25... Status as of this dossier: dismissed but not fully resolved — monitor," with a listed forward catalyst of "any ruling on the pending motion for leave to amend."

**What the primary source actually says:** DG's own Q2 FY2026 10-Q (accession 0001104659-26-101932, filed 2026-08-27 — the same filing the dossier cites as its data-cutoff document), Legal Proceedings note: the motion to dismiss the second amended complaint was granted without prejudice on **June 23, 2025** (one year earlier than the dossier's date). The court then **granted** the motion for leave to amend on **March 24, 2026**, and lead plaintiffs filed a **third** consolidated amended complaint; defendants moved to dismiss *that* complaint on April 21, 2026, and briefing was **completed May 29, 2026** — i.e., a fully-briefed motion to dismiss the third amended complaint is what is actually pending, not an open motion for leave to amend. The 10-Q also reveals this is legally two consolidated matters (Washtenaw County + a second case, *Edmonds*, voluntarily dismissed in Jan 2024) — the dossier names only Washtenaw County.

**Correct status (as of DG's own Q2 FY26 10-Q, filed 2026-08-27):** dismissal-without-prejudice date is **2025-06-23**, not 2026-06-23; the motion for leave to amend was granted **March 24, 2026**; a third amended complaint is now the operative pleading, with defendants' motion to dismiss it fully briefed as of **May 29, 2026** and awaiting ruling.

**Exact dossier lines to fix:** DG.md §11 red-flag scan, "Shareholder securities class action" bullet; §9 kill criterion 5 (references "the securities class action is reinstated" as a future trigger, when a third complaint already exists); §10 catalysts, "Any ruling on the pending motion for leave to amend the consolidated shareholder securities complaint" (stale — that motion was already ruled on; the live event is the ruling on the motion to dismiss the third complaint).

## 3. The flagged known issue — NOW / Moveworks, resolved (#16)

Per this audit's assignment, I confirmed the Loop-3 auditor's finding directly against ServiceNow's own SEC filing rather than secondary reporting. ServiceNow's 8-K filed **2025-12-15** (accession **0001373715-25-000329**), Exhibit 5.1 (Skadden legal opinion covering the resale of shares issued as merger consideration), states verbatim: *"the Shares were issued to the Selling Stockholders in connection with the closing of the Company's acquisition of Moveworks, Inc., a Delaware corporation..., **on December 15, 2025**, pursuant to the Agreement and Plan of Merger, dated as of March 9, 2025."* This is an unambiguous, primary-source confirmation of both the close date and the fact that it closed at all. NOW.md already carries a lead-added correction note dated 2026-09-26 reflecting this; that note's substance is accurate, and this audit supplies the requested accession number. No further dossier edit is needed beyond what the lead has already appended (per instructions, dossiers were not edited by this audit in any case).

## 4. The MINOR, in full — EG book-value comparison figure (#27)

EG.md §6 states book value per share "$398.83... vs $379.70 (Dec-25)." Everest's own Q2 2026 8-K Ex-99.1 states: *"Book value per share of $398.83 at June 30, 2026 versus $379.83 at December 31, 2025."* The current-quarter figure and the ex-URA(D) figure ($407.67) both match exactly; only the Dec-2025 comparison figure is off, by $0.13/share (0.03%) — immaterial to the P/B ratio (0.93x) or to the thesis, but not an exact match, and likely a transcription slip.

## 5. The UNVERIFIABLE, briefly (#23)

BX.md's standalone long-term-debt progression ($11.5bn Dec-24 → $13.3bn Jun-26) and its "~85% of DE" payout-ratio claim were not independently re-derived from the Dec-2024 and Jun-2026 10-Ks/10-Qs within this review's time-box. The payout-ratio claim is arithmetically consistent with two other, independently-confirmed primary figures in this same pass ($1.29 dividend / $1.52 DE-per-share = 84.9% ≈ "~85%"), so it is not flagged as wrong — only as not separately re-verified at the balance-sheet level.

## 6. One-line judgement on dossier reliability

Across BR, CMCSA, BKNG, DG, NOW, BX and EG, **every GAAP-vs-adjusted split, every guidance figure, and every quarterly headline number checked against its cited SEC exhibit matched exactly** — the pattern DA5 and earlier passes established continues to hold for the pure-arithmetic facts. The two real defects found this pass are both about **currency of a claim, not its arithmetic**: BR's dossier asserts a deal term (undisclosed price) that the company's own subsequent-event note contradicts outright, and DG's dossier describes litigation status using the filing's own historical narrative but mis-dates the key ruling by exactly one year and then stops one full amendment-and-motion cycle short of where the same cited 10-Q says the case actually stands as of 2026-08-27. Both are fixable with the exact source language quoted above. The NOW/Moveworks issue flagged for this audit is confirmed exactly as the Loop-3 auditor found it, with the primary-source accession number now on record.
