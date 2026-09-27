# SLB (SLB Limited, formerly Schlumberger) — Diligence Dossier (Agent F105, wave 6)

## 1. Verdict
**WATCH** — not INCLUDE despite a triage read of "reasonable 17x NTM multiple." Overturns the triage's implicit
comfort: revenue is growing (+5% YoY Q2 2026, guided to accelerate into Q4), but **GAAP net income and diluted
EPS fell 22–30% YoY in Q2 2026** even as revenue rose — a genuine earnings-quality divergence the triage's
one-line thesis did not surface (it flagged only "momentum already +78%... near-term expectations are high" as
the risk). Condition to move to INCLUDE: two consecutive quarters where adjusted EPS growth turns positive YoY
and the GAAP-vs-adjusted gap (charges/credits) narrows, confirming the margin pressure is genuinely transitory.
Thesis horizon if upgraded: 12–24 months (oilfield services is cyclical; do not treat as a long secular hold
without re-underwriting each year).

## 2. Business in plain English
SLB is the largest global oilfield-services company: it sells the technology, equipment, digital software (its
"Lumi" AI/digital platform) and personnel that oil & gas companies use to find, drill, complete and produce wells,
plus a growing new-energy/CCUS and data-center-power business. Unlike US shale-focused peers, SLB's revenue mix
skews international and offshore, which the triage correctly identified as a differentiator in the current
international-upcycle narrative.

## 3. Why the model likes it / durability
b1 factor data: composite decile **1 of 10** (bottom decile), live_rank 448 of ~500, quintile 1 — the **weakest**
quant score of this agent's three names, despite the triage's qualitative "quality 4, growth 3." Digging into the
family scores: Quality actually screens well (pct_gp_a 90%, i.e. gross-profit/assets in the top decile), but
**Value (pct_ep 23%, pct_fcfp 38%, and a raw book/price factor of −1.61, a clear outlier vs peers) and Momentum
(pct_mom_12_1 73%, i.e. already-run-up) drag the composite to the bottom.** This is a genuine, quantifiable
**data conflict** between the qualitative triage (which read the 17x multiple as "reasonable") and the systematic
factor model (which reads SLB as expensive on value factors after a large trailing run-up) — flagged explicitly
per the addendum's data_conflicts requirement. The negative book/price outlier is likely driven by SLB's large
buyback program shrinking book equity relative to price; not independently re-derived this pass (**data gap**).

## 4. Last several quarters of results (USD millions except EPS)
Source: XBRL company facts, `https://data.sec.gov/api/xbrl/companyfacts/CIK0000087347.json`; FY2025 10-K (accession 0001193125-26-021017, filed
2026-01-23); Q1 2026 10-Q (accession 0001193125-26-190101, filed 2026-04-29); Q2 2026 10-Q (accession 0001193125-26-322595, filed 2026-07-29); Q2 2026 earnings release
(https://investorcenter.slb.com/news-releases/news-release-details/slb-announces-second-quarter-2026-results).

| Quarter | Revenue | YoY growth | Net income (GAAP) | YoY | Diluted EPS (GAAP) | YoY |
|---|---|---|---|---|---|---|
| Q1 2025 | 8,490 | — | 797 | — | 0.58 | — |
| Q2 2025 | 8,546 | — | 1,014 | — | 0.74 | — |
| Q3 2025 | 8,928* | — | 739* | — | 0.50 | — |
| FY2025 (annual) | 35,708 | — | 3,374 | — | 2.35 | — |
| Q1 2026 | 8,721 | +2.7% | 752 | **−5.6%** | 0.50 | **−13.8%** |
| Q2 2026 | 8,972† | **+5.0%** | 786 | **−22.5%** | 0.52 | **−29.7%** |

\* Q3 2025 figures derived (9-month cumulative minus H1 2025), consistent with the FY2025 10-K total.
† Q2 2026 revenue/NI independently confirmed by SLB's own press release: "Revenue of $8.97 billion increased 3%
sequentially and 5% year on year... Net income attributable to SLB of $786 million increased 5% sequentially and
decreased 22% year on year... GAAP EPS of $0.52 increased 4% sequentially but decreased 30% year on year" — this
cross-check matches the XBRL-derived figures above.
**Adjusted EPS also fell YoY**, just by less: SLB's own release states adjusted EPS of $0.55 "decreased 26% year
on year" — so this is **not purely a GAAP-vs-adjusted charges/credits story**; underlying (adjusted) profitability
genuinely compressed even as revenue grew. Adjusted EBITDA of $1.90B was also down 7% YoY in Q2 2026 despite the
revenue growth. This margin/profitability divergence from revenue growth is the central red flag of this dossier.

## 5. Guidance track record
- **Q2 2026 release (24 Jul 2026):** SLB guided to **sequential revenue growth in Q3 2026** and **revenue above
  $10B in Q4 2026** (vs. $8.97B in Q2 2026 — a large sequential step-up implied for Q4). No explicit prior-quarter
  numeric guidance range was identified to compare this against in the sources reviewed (SLB tends to guide
  qualitatively/directionally rather than with tight numeric EPS ranges) — **flagged: guidance-track-record
  comparison is qualitative only this pass, a data gap versus the addendum's "raised/maintained/cut vs prior
  range" requirement.**

## 6. Earnings quality & balance sheet
- **FCF (TTM):** OCF (FY2025 6,489 − H1 2025 1,802 + H1 2026 1,846) = **6,533M**; capex (FY2025 1,694 − H1 2025
  769 + H1 2026 802) = **1,727M**; **TTM FCF ≈ $4,806M**. TTM net income (FY2025 3,374 − H1 2025 1,811 + H1 2026
  1,538) = **$3,101M** → **FCF/NI ≈ 155%** — high conversion in absolute terms, but note NI itself is the metric
  that is falling YoY (§4), so a high conversion ratio on a shrinking NI base is not, by itself, reassuring.
- **Balance sheet (consolidated, Q2 2026 10-Q accession 0001193125-26-322595, period end 2026-06-30):** consolidated cash & restricted cash
  (incl. disposal group) $2,743M; consolidated long-term debt (noncurrent) $11,140M (up from $9,670M at Q1
  2026 — **a ~$1.47B increase in one quarter**, likely new issuance; not independently tied to a specific note in
  the sources reviewed this pass — **data gap, flagged for the fact-check pass**); current portion of consolidated
  long-term debt not separately identified in this extraction (XBRL tag `LongTermDebtCurrent` last populated in
  2016 filings, suggesting SLB now uses a different/combined tag — **data gap**). Consolidated stockholders'
  equity $26,074M. Using consolidated noncurrent debt only, **consolidated net debt ≈ $8.4B**, close to the $8.2B
  consolidated net-debt figure SLB itself disclosed for Q1 2026 (Simply Wall St summary of the 10-Q) — reasonably
  consistent.
- **Capital returns:** SLB targets **>$4B returned to shareholders in 2026** (dividends + buybacks), including at
  least $2.4B of buybacks; cumulative buybacks under the $10B program reached ~$6.3B as of Q1 2026-end. Dividend
  raised 3.5% in Jan 2026 (to $0.295/share quarterly, effective the April 2026 payment). This is an aggressive
  capital-return program **being maintained even as GAAP/adjusted EPS fall YoY** — worth flagging: continuing a
  large buyback while per-share earnings power is under pressure is not inherently wrong (buybacks below
  intrinsic value are accretive) but raises the bar for confirming the margin pressure is transitory before
  crediting the buyback as value-accretive rather than merely EPS-supportive.
- **Capex:** full-year 2026 guided at ≈$2.5B.

## 7. Valuation snapshot & reconciliation with V1
**No V1 row exists for SLB** in `v4/outputs/v1_valuation_table.csv`/`v1_valuation.json` — `v1_verdict: null`.
- Price used: **$51.43** (25 Sep 2026 close, per web search).
- **NTM P/E:** on trailing-four-quarter GAAP EPS (0.50+0.52+0.50+0.74, using the last four reported quarters
  Q3'25–Q2'26 = 2.26) → 22.8x trailing; on an annualized Q2 2026 adjusted run-rate ($0.55 × 4 = $2.20) → 23.4x.
  Both are **meaningfully higher than the triage's cited "17x NTM multiple"** — the triage's 17x appears to have
  used a forward EPS estimate assuming margin recovery into H2 2026 (consistent with SLB's own Q4 >$10B revenue
  guide), which has **not yet been confirmed** by Q3 2026 results (due ~16 Oct 2026) at the time of this dossier.
  This is the key reconciliation point flagged for the valuation agent: **the 17x figure the triage relied on is
  a forward/hoped-for number, not a trailing one, and the trailing multiple (~23x) is notably richer** given the
  YoY EPS decline.
- **FCF yield:** TTM FCF/share ≈ $4,806M / ~1,506M diluted shares = $3.19/share ÷ $51.43 = **6.2%** — the highest
  FCF yield of this agent's three names, a genuine value support even given the EPS concerns.
- **Reverse DCF (this agent's own model):** two-stage DCF, FCF0 = $3.19/share, WACC 9.0% (labelled — higher than
  RMD/RTX given oilfield-services cyclicality/energy-price sensitivity), 10-year explicit + 3% terminal growth.
  Implied 10-year FCF growth to justify $51.43: **≈ 2.2%/year**. This is a **low bar** relative to SLB's own
  Q4 2026 revenue guide (implying a >10% sequential jump from Q2), so **on a pure FCF-yield/reverse-DCF view the
  stock screens cheap-to-fair**, consistent with the triage. **The disagreement is not about the DCF-implied
  growth bar (which is genuinely low and achievable if the Q4 revenue guide holds) but about earnings quality and
  trajectory (§4/§6) and the quant model's value-factor read (§3)** — the reason for WATCH rather than INCLUDE is
  that per-share profitability has been moving the wrong direction for two consecutive quarters even as revenue
  grows, and this dossier prioritizes resolving that before crediting the FCF-yield support.

## 8. Bull case / bear case
**Bull (3):**
1. Q4 2026 revenue guide (>$10B, up from $8.97B in Q2) delivers, confirming the international/offshore upcycle
   this triage identified is accelerating, not decelerating.
2. High FCF yield (6.2%) and an aggressive, ongoing buyback (>$2.4B targeted in 2026 alone) support per-share
   value even if reported net income stays choppy.
3. Digital/AI-enabled service technology (the differentiator the triage cited) supports structurally higher
   margins over a multi-year horizon versus the equipment-only oilfield-services peers.

**Bear (3):**
1. GAAP and adjusted EPS both fell YoY in Q1 and Q2 2026 despite revenue growth — if this is margin pressure from
   pricing, mix, or cost inflation rather than a one-off charge, the "cheap on forward multiple" read is wrong and
   the trailing ~23x multiple is the more honest one.
2. Momentum is already extended (+78% over 12 months per the triage's own red flag) — a lot of the international-
   upcycle good news is arguably already in the price, and the quant model's bottom-decile composite (driven by
   value factors) agrees.
3. Long-term-debt jumped ~$1.5B in a single quarter (Q1→Q2 2026) while buybacks continue at pace — a capital-
   allocation combination (rising debt + large buybacks + falling EPS) worth monitoring for balance-sheet
   discipline if the commodity cycle turns.

## 9. Key risks & kill criteria (measurable)
1. Q4 2026 revenue does not reach the guided >$10B (i.e., sequential growth from Q2's $8.97B stalls) — direct
   test of the bull thesis and the Q3/Q4 guide.
2. Adjusted EPS YoY growth stays negative for a third consecutive quarter (Q1 2026 −13.8% GAAP/-unclear adj., Q2
   2026 −29.7% GAAP / −26% adjusted) at the Q3 2026 report (due ~16 Oct 2026).
3. Consolidated net debt/EBITDA (using TTM EBITDA proxy) rises materially from the ~1.7x implied by $8.4B
   consolidated net debt / ~$4.9B TTM adjusted-EBITDA run-rate (4 × $1.90B — a rough proxy, not independently tied
   to a disclosed TTM EBITDA figure — **flagged as an approximation**) — watch for a level above 2.5x.
4. Buyback pace is cut below the $2.4B full-year-2026 target, which would signal management itself losing
   confidence in free cash flow generation.
5. Brent/WTI oil price sustains below $60/bbl for two consecutive quarters, historically the level at which
   E&P capex (SLB's revenue driver) gets cut (qualitative macro trigger, not company-specific — include as a
   monitorable macro kill switch given the sector's oil-price sensitivity).

## 10. Catalysts & calendar
- Next earnings: **Q3 2026, ~16 October 2026** (per search results; confirm on investorcenter.slb.com nearer the
  date) — the key near-term test of both the Q4 revenue guide and whether EPS growth turns positive.
- Q4 2026 results (Jan 2027) — the guided ">$10B revenue" quarter.

## 11. Red-flag scan
- **Earnings-quality divergence** (§4/§6): revenue growth with declining GAAP and adjusted net income/EPS for two
  consecutive quarters — the central finding of this dossier, not previously surfaced in the triage.
- **Consolidated long-term debt increase** of ~$1.47B in a single quarter (Q1→Q2 2026) — not independently tied to
  a specific new note/issuance in the sources reviewed this pass; **data gap, flagged for the fact-check pass.**
- No auditor change, restatement, or going-concern language identified in the FY2025 10-K review this pass.
- No SEC/DOJ investigation or material litigation identified in the sources checked this pass (SLB, as a large
  multinational oilfield-services company, carries ordinary-course litigation and sanctions-exposure risk given
  historical operations in various jurisdictions; **not independently re-verified this pass — data gap**).
- Insider Form 4 pattern not reviewed this pass — **data gap**.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q (accession 0001193125-26-322595, period end 2026-06-30, filed 2026-07-29) and the 24 Jul 2026
earnings release. Events checked to 2026-09-25. Figures in §4/§6 are GAAP unless marked "adjusted"; SLB's own
"charges and credits" reconciliation (adjusted EPS $0.55 vs GAAP $0.52 in Q2 2026) is cited from the company
release, not independently re-derived from the 10-Q footnotes this pass. **Research only, not personalized investment advice.**

## 13. Sources
1. SEC EDGAR XBRL company facts, CIK 0000087347: https://data.sec.gov/api/xbrl/companyfacts/CIK0000087347.json (retrieved 2026-09-27)
2. SLB FY2025 10-K (accession 0001193125-26-021017, filed 2026-01-23): https://www.sec.gov/Archives/edgar/data/87347/000119312526021017/slb-20251231.htm
3. SLB Q1 2026 10-Q (accession 0001193125-26-190101, filed 2026-04-29): https://www.sec.gov/Archives/edgar/data/0000087347/000119312526190101/slb-20260331.htm
4. SLB Q2 2026 10-Q (accession 0001193125-26-322595, filed 2026-07-29): https://www.sec.gov/Archives/edgar/data/0000087347/000119312526322595/slb-20260630.htm
5. SLB Announces Second-Quarter 2026 Results: https://investorcenter.slb.com/news-releases/news-release-details/slb-announces-second-quarter-2026-results
6. SLB Announces First-Quarter 2026 Results: https://investorcenter.slb.com/news-releases/news-release-details/slb-announces-first-quarter-2026-results
7. Simply Wall St, "How SLB's Q2 2026 Revenue Guidance, Buybacks, And Dividend Have Changed Its Investment Story": https://simplywall.st/stocks/us/energy/nyse-slb/slb/news/how-slbs-slb-q2-2026-revenue-guidance-buybacks-and-dividend
8. Simply Wall St, "SLB Affirms Dividend And Buyback, Is It Still Below Fair Value?": https://simplywall.st/stocks/us/energy/nyse-slb/slb/news/slb-slb-affirms-dividend-and-buyback-is-it-still-below-fair
9. Q03_triage.json (v4/outputs) — prior-stage triage note on SLB
10. v4/data/b1_live_scores.csv — factor composite/decile context
11. Stock price 25 Sep 2026 close, web search aggregation (retrieved 2026-09-27)
