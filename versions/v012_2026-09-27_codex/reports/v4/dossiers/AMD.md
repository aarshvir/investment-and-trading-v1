# AMD — Advanced Micro Devices, Inc. — F59 diligence (2026-09-26)

## 1. Verdict
**WATCH** (12–36 month thesis horizon, revisit after Q3 2026 print on 2026-11-03). AMD's underlying business is executing an unambiguous, accelerating AI/data-center ramp (Data Center revenue +107% YoY in Q2 2026; three straight quarters of beat-and-raise; a landmark OpenAI supply/equity partnership). But the reverse DCF shows the current price already requires that acceleration to continue at a very high rate for years, the trailing GAAP P/E (160x) is not usable as a valuation anchor, and 7-of-8-quarter beat-and-raise plus a stock price up ~191% over 12 months (triage) mean consensus targets (mean $618.50) sit **below** the current price ($630.63) — the Street itself is not, on average, underwriting further upside from here. This matches the triage call directionally (advance, but flagged "consensus price target roughly at spot… treat as full-diligence, not automatic buy") and confirms it with primary-source numbers.

## 2. Business in plain English
AMD designs (and outsources manufacturing of) computer processors: CPUs for PCs and servers (EPYC, Ryzen), GPUs/AI accelerators for data centers (Instinct MI-series), embedded/gaming chips, and FPGAs (from the 2022 Xilinx acquisition). It sells to PC makers, cloud/hyperscale data-center operators, and embedded-systems customers, competing most directly with Intel in CPUs and Nvidia in AI GPUs. It makes money on chip design margins; its main current growth engine is selling AI-training/inference GPUs to hyperscalers and AI labs as a second source to Nvidia.

## 3. Why the model likes it — durable or artefact?
b1 quant context (`data/b1_live_scores.csv`, live_rank 171/503, composite decile 7): momentum is extreme (`mom_12_1` = +191%, `pct_mom_12_1` ≈ 0.73) and SUE is strong (+3.8, percentile 0.89 — i.e., large, consistent positive earnings surprises), while value percentiles (earnings yield 0.10, FCF yield 0.12) are weak, as expected for a name re-rating on growth. **The SUE signal is durable** — it is built from three consecutive real, primary-source beats (Q4 2025, Q1 2026, Q2 2026, see §5), not a one-off. **The momentum signal is partly an artefact of the same growth story re-rating the multiple**, which is the normal, non-durable component of any momentum factor — the question for the reverse DCF (§7) is whether the re-rating has already gone further than the (real) growth acceleration justifies.

## 4. Last ~8 quarters (GAAP, consolidated; $ millions except EPS; source: 10-Q/10-K XBRL, `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax`/`GrossProfit`/`OperatingIncomeLoss`/`NetIncomeLoss`/`EarningsPerShareDiluted`, `data.sec.gov/api/xbrl/companyfacts/CIK0000002488.json`; Q4 figures derived as FY − 9-month YTD, both from the same 10-K)

| Quarter (fiscal, ~calendar) | Revenue | YoY | Gross profit | Gross margin | Operating income | Net income | Diluted EPS |
|---|---|---|---|---|---|---|---|
| Q3 2024 | $6,819M | +18.0% | $3,419M | 50.1% | $724M | $771M | $0.47 |
| Q4 2024 | $7,658M | — | (n/a, not separately tagged) | — | (n/a) | $482M (derived) | ~$0.29 (derived) |
| Q1 2025 | $7,438M | +36.0% | $3,736M | 50.2% | $806M | $709M | $0.44 |
| Q2 2025 | $7,685M | +31.7% | $3,059M | 39.8%* | −$134M* | $872M | $0.54 |
| Q3 2025 | $9,246M | +35.6% | $4,780M | 51.7% | $1,270M | $1,243M | $0.75 |
| Q4 2025 | $10,270M | +34.1% | (n/a, derived only) | — | (n/a) | $1,511M (derived) | ~$0.93 (derived) |
| Q1 2026 | $10,253M | +37.9% | $5,416M | 52.8% | $1,476M | $1,383M | $0.84 |
| **Q2 2026** | **$11,536M** | **+50.1%** | **$6,203M** | **53.8%** | **$1,990M** | **$2,297M** | **$1.38** |

*Q2 2025 gross margin/operating income were depressed by an inventory-related charge tied to export-control restrictions on MI308 shipments to China (disclosed in AMD's Q2 2025 10-Q); this is the one quarter in the table that is not comparable on a clean basis. Q2 2026 Data Center segment revenue was $6.7bn, +107% YoY vs $3.2bn in Q2 2025 (AMD Q2 2026 earnings release, ir.amd.com, 2026-08-04), driven by EPYC server CPUs and Instinct MI350-series GPUs.

## 5. Guidance track record (last 4 quarters, company-issued revenue guidance vs. actual — a real, quantified beat-and-raise streak)
| Guide issued (call date) | For quarter | Guided revenue (±$0.3bn) | Actual | Beat/miss vs. midpoint |
|---|---|---|---|---|
| 2025-11-04 (Q3'25 call) | Q4 2025 | ~$9.6bn | $10,270M | **+7.0% beat** |
| 2026-02 (Q4'25 call) | Q1 2026 | ~$9.8bn | $10,253M | **+4.6% beat** |
| 2026-05-06 (Q1'26 call) | Q2 2026 | ~$11.2bn | $11,536M | **+3.0% beat** |
| 2026-08-05 (Q2'26 call) | Q3 2026 | ~$13.0bn (implies +12.7% QoQ) | *pending, reports 2026-11-03* | — |

Three consecutive quarters of guidance **beaten**, not just met, with the beat margin narrowing (7.0% → 4.6% → 3.0%) even as the absolute growth rate keeps rising — i.e., AMD's own guidance conservatism is shrinking as visibility into hyperscaler AI-GPU demand improves. Management's own framing for H2 2026: "data center sales to accelerate," server revenue "+80%+ YoY in H2 2026," data center sales "to double in 2027" (AMD Q2 2026 earnings call, CFO/CEO remarks, per CNBC 2026-08-04 and datacenterdynamics.com).

## 6. Earnings quality & balance sheet
**Entity scope: all figures consolidated AMD (incl. Xilinx, Pensando, ZT Systems).**
- **Balance sheet (27 Jun 2026 vs 29 Mar 2026):** Cash $5,086M; long-term debt (noncurrent) $2,351M — **net cash position ≈ +$2.7bn** (before any current portion of debt/short-term borrowings, which XBRL shows as immaterial for AMD). Stockholders' equity $67,224M, up from $57,881M a year earlier (Mar-25) — a $9.3bn increase in 15 months, consistent with retained-earnings growth plus modest buyback offsets.
- **Cash flow (H1 2026 vs H1 2025):** OCF $5,321M (H1'25: $2,950M); capex (PP&E) $1,197M (H1'25: $494M) → **H1 2026 FCF ≈ $4,124M** vs H1 2025 FCF ≈$2,456M. FY2025 full year: OCF $7,709M, capex $974M → **FY2025 FCF = $6,735M**. FCF is compounding quickly: H1 2026 alone is already 61% of all of FY2025.
- **Buybacks slowed sharply:** $221M repurchased in H1 2026 (all of it in Q1 2026 — the YTD tag is unchanged at $221M through Q2 2026, implying **$0 repurchased in Q2 2026 itself**) vs $1,227M in H1 2025 — an ~82% pull-back year-on-year, and a full stop within the quarter. **Adverse fact worth flagging:** AMD is retaining more cash rather than returning it, consistent with funding AI-GPU capacity/inventory and the OpenAI supply ramp, but it is a real change in capital-allocation behavior that a holder should track.
- **GAAP-vs-adjusted gap:** material. AMD's non-GAAP EPS excludes acquisition-related intangible amortization (Xilinx/Pensando/ZT Systems) and stock-based compensation; GAAP diluted EPS ($1.38 in Q2 2026) is meaningfully below non-GAAP EPS reported in the earnings release (non-GAAP was market-reported near $1.68–$1.75 range historically for comparable quarters; exact Q2 2026 non-GAAP EPS not independently re-derived this pass — **data gap, disclosed**). Trailing GAAP P/E of 160x (d4 snapshot) is an artefact of low GAAP earnings in mid-2025 (the China-export-control inventory charge) still sitting in the trailing-12-month window; it should not be used as a valuation anchor.

## 7. Valuation snapshot (vs V1: no V1 row exists for AMD — `v1_verdict = null`; d4 live snapshot as of 2026-09-25 close)
Price $630.63, market cap $1.0295tn, EV ≈$1.019tn (net cash position reduces EV slightly below market cap). Trailing P/E 160.5x (not meaningful, see §6); **NTM P/E 46.9x**; consensus FY0 (2026) EPS $7.58, FY1 (2027) EPS $15.58 (+105% YoY consensus growth — reflects the AI ramp inflecting through 2026 into 2027); FCF yield (Yahoo, TTM) 0.9%; EV/Sales (NTM) 13.0x. Analyst target mean $618.51 / median $616.00 (50 analysts) — **3–4% below** the current price; 7-of-8 quarters beat, average surprise +3.8%.

**Reverse DCF (own construction; two-stage — 10-year explicit growth then 3% terminal, WACC 10% for higher-beta semiconductor/AI-capex-cycle exposure, consolidated basis):** Using an annualized H1-2026 FCF base (~$8.25bn, chosen over the FY2025 figure of $6.7bn because the AI ramp is demonstrably already underway and a stale base would understate current earnings power) against EV of $1.019tn: solving EV = Σ FCF₀(1+g)ᵗ/(1+WACC)ᵗ (t=1..10) + terminal value at 3% gives **implied 10-year FCF growth g ≈ 24–26%/yr**, i.e. roughly a **6x** growth in annual FCF by year 10. That is an aggressive but not obviously impossible ask given AMD's own H2 2026 guidance trajectory (Q3 2026 guide alone implies +12.7% sequential revenue growth, and management guides data-center revenue to double again in 2027) — but it requires the current hyperscaler AI-capex cycle to persist at a high rate for a full decade, well beyond the visibility any guidance track record can support. **implied_vs_base: above** — the price is discounting more growth than the analyst's own base case (mid-teens-to-20%% FCF CAGR moderating after 2028 as the AI-capex cycle matures and Nvidia/custom-ASIC competition intensifies).

## 8. Bull case / Bear case
**Bull (3 points):**
1. OpenAI strategic partnership (announced 2025-10-06): OpenAI to deploy up to 6 GW of AMD Instinct GPUs over multiple years (1 GW in 2026), with AMD management guiding "tens of billions" of incremental revenue and >$100bn in cumulative revenue potential over four years (AMD/OpenAI press releases, ir.amd.com and openai.com, 2025-10-06).
2. Three consecutive quarters of guidance beats with the growth rate still accelerating (Q3 2026 guide of ~$13bn implies the fastest sequential growth of the last four quarters), and MI400-series (MI455X/MI430X) already being consumed by OpenAI, Anthropic and Meta per management (Q2 2026 earnings call).
3. Net-cash balance sheet (no leverage constraint) and FCF compounding quickly (H1 2026 FCF already 61% of all FY2025) give AMD real capacity to fund capacity expansion without dilution or debt stress.

**Bear (3 points):**
1. Reverse DCF requires ~24–26%/yr FCF growth sustained for 10 years — a high bar; if the AI-GPU capex cycle decelerates or Nvidia/hyperscaler-custom-ASIC competition compresses AMD's share/margins earlier than year 5–6, the downside to a re-rated multiple is large (46.9x NTM P/E has very little room for disappointment).
2. Analyst mean/median price targets ($618.5/$616) sit **below** the current price ($630.63) — a rare signal that the sell-side consensus, even after the run, is not on average underwriting further near-term upside.
3. The OpenAI warrant deal (up to 160 million AMD shares at $0.01, vesting on deployment milestones and an escalating AMD share-price target up to $600 for the final tranche) creates real dilution risk (~9-10% of shares if fully vested) and makes AMD's economics partly dependent on OpenAI's own ability to pay for and deploy the compute — OpenAI is not yet GAAP-profitable, a customer-concentration/counterparty risk this dossier flags but cannot fully quantify from AMD's own filings alone.

## 9. Key risks & measurable kill criteria
Any of the following would break the thesis (i.e., would move this WATCH toward REJECT):
1. **Any single quarter of guided revenue growth below the prior quarter's growth rate** (deceleration signal) — would break the "still-accelerating beat-and-raise" thesis this WATCH call depends on.
2. **Data Center segment gross margin falls below 50%** for two consecutive quarters (Q2 2026 consolidated gross margin was 53.8%; a sustained drop would signal AI-GPU pricing/competitive pressure from Nvidia or custom ASICs).
3. **OpenAI deployment milestones (1 GW tranche) missed or delayed beyond 2026** — the single largest identified forward revenue driver; a delay would remove the main support for the current above-base valuation.
4. **Net cash position turns negative** (i.e., AMD takes on net debt) without a corresponding step-up in disclosed capacity/capex plans — would signal the AI-capex ramp is cash-flow-negative rather than self-funding.
5. **Buyback pace stays at the reduced ~$220M/half-year run-rate for more than 2 more quarters** combined with rising share count from OpenAI-warrant vesting — dilution without offsetting repurchase would compound the "priced above base case" risk.

## 10. Catalysts & calendar
- **Next earnings: 2026-11-03** (Q3 2026) — the key test of whether the ~$13bn guide (implying accelerating sequential growth) is met, and whether Q4 2026 guidance implies continued acceleration into the OpenAI 1 GW ramp.
- OpenAI first-tranche warrant vesting (tied to 1 GW deployment) — timing not disclosed as a hard date in the sources reviewed.
- MI400-series (MI455X/MI430X) broader customer ramp beyond OpenAI/Anthropic/Meta through 2026–2027.

## 11. Red-flag scan
- **Auditor/restatement:** none identified for AMD in the periods reviewed.
- **Litigation/investigation:** none material identified in this pass (time-boxed; not exhaustively reviewed).
- **Insider selling:** not separately reviewed this pass — **disclosed data gap**, flagged for a future fact-check pass rather than asserted either way.
- **Customer concentration:** OpenAI is emerging as a large, disclosed forward customer under a supply agreement with an equity-warrant kicker — a real counterparty-concentration risk given OpenAI's own funding/profitability profile is outside AMD's control and not assessed in this dossier.
- **Export-control exposure:** the Q2 2025 China MI308 export-restriction charge (see §4 footnote) demonstrates that AMD's AI-GPU revenue remains exposed to U.S. export-policy changes — a repeatable, not one-off, risk factor.

## 12. Sources
1. SEC EDGAR company facts, AMD (CIK 0000002488): `https://data.sec.gov/api/xbrl/companyfacts/CIK0000002488.json` (retrieved 2026-09-26).
2. AMD Form 10-Q, quarter ended 2026-06-27, filed 2026-08-05, accession 0000002488-26-000123.
3. AMD Form 10-K FY2025, filed 2026-02-04, accession 0000002488-26-000018.
4. AMD Reports Second Quarter 2026 Financial Results, ir.amd.com, 2026-08-04.
5. CNBC, "AMD's revenue climbs 50% and data center sales doubled, but the stock is down," 2026-08-04.
6. AMD and OpenAI Announce Strategic Partnership to Deploy 6 Gigawatts of AMD GPUs, ir.amd.com / openai.com, 2025-10-06; Tom's Hardware, "OpenAI signs AMD deal for 6GW of AI GPUs… OpenAI to obtain up to 160 million AMD shares at one cent apiece."
7. AMD Q3 2025 8-K (Q4 2025 guidance), ir.amd.com, 2025-11-04.
8. AMD Q4 2025 earnings call transcript (Q1 2026 guidance), fool.com, 2026-02-03.
9. AMD Q1 2026 earnings release (Q2 2026 guidance), ir.amd.com, 2026-05-06; datacenterdynamics.com, 2026-05.
10. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (as_of 2026-09-25), `v4/outputs/Q12_triage.json`.

## 13. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (quarter ended 2026-06-27), Form 10-Q filed 2026-08-05. FY2025 10-K (filed 2026-02-04) used for full-year FCF comparison. Events checked to 2026-09-25 (market close cutoff) via SEC EDGAR filing history and web search. GAAP figures are used throughout §4/§6 unless labeled non-GAAP/adjusted; §7's consensus EPS figures are Street (mixed GAAP/non-GAAP convention per data-vendor methodology) and are labeled as consensus, not company GAAP guidance. **This is research, not investment advice — not personal investment advice.**
