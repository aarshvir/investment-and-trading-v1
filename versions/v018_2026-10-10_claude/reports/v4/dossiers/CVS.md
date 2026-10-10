# CVS Health Corporation (CVS) — Diligence Dossier

**Agent:** F15 (replaces F9, which hung before writing anything — this is a fresh review) | **As of:** 2026-09-25 close | **Price:** $89.13

## 1. Verdict

**INCLUDE-SMALL** (half weight) — thesis horizon **24–36 months**.

CVS is a genuine, multi-quarter operational turnaround (Aetna medical costs improving, Medicare Advantage star ratings recovered sharply, guidance raised in three of the last four releases) trading at a statistically cheap multiple (10.6x NTM P/E, 8.8th percentile of its own 14-year history). The reservation: ~3.7x net debt/EBITDA, $85.5bn of goodwill (≈75% of market cap), a still-negative-outlook credit profile at two of three rating agencies, and an unresolved post-2028 PBM cost-plus mandate mean the full re-rating to a ~17x historical-average multiple that the V1 model's base case assumes is not assured on this timeline. Size accordingly.

## 2. Business in plain English

CVS Health is a diversified health-care conglomerate with three engines: **Aetna** (health insurance, including a large Medicare Advantage book), **Health Services** (CVS Caremark, the pharmacy-benefit manager that negotiates drug prices and rebates for employers/insurers, plus Oak Street Health primary-care clinics and Signify Health home assessments), and **Pharmacy & Consumer Wellness** (roughly 9,000 retail pharmacies). It makes money on insurance premiums net of medical claims, PBM spread/rebate economics and dispensing fees, and retail pharmacy margins. Its competitive position is scale: it is one of only three vertically integrated payer-PBM-pharmacy platforms in the US (with UnitedHealth/Optum and Cigna/Express Scripts), which matters because federal PBM reform is now reshaping how all three get paid.

## 3. Why the model likes it

B1 quant data (`v4/data/b1_live_scores.csv`, live_rank 25) and V1 valuation both flag CVS as statistically cheap on NTM P/E versus its own history. This is **not** primarily a momentum or quality signal — the 12-month price move (+28.5% per the underlying momentum factor) is a recovery off a depressed 2024–2025 base, and the "cheapness" is a scar from two years of Medicare Advantage cost misses, guidance cuts and a leadership change, not a hidden gem the market missed. The durability question is whether the 2026 operational improvement (below) is real and sustained, or a cyclical bounce that fades once easy comparisons roll off. The evidence in hard numbers (section 5) leans toward real, but recent.

## 4. Last several quarters of results

Full 8-quarter detail was not independently rebuilt within this review's time box (aggregator income-statement/cash-flow API was rate-limited by the shared data vendor throughout this session); the quarters below are sourced directly from CVS's own earnings releases and 10-Q/10-K filings (sources 2–6).

| Period | Revenue | Op. income | GAAP diluted EPS | Adjusted diluted EPS | Aetna MBR |
|---|---|---|---|---|---|
| Q3 2024 | n/a | n/a | n/a | n/a | 95.2% |
| FY2024 | n/a | n/a | n/a | n/a | 92.5% |
| Q2 2025 | $98,915M | n/a | n/a | $1.81 | 89.9% |
| Q3 2025 | n/a | n/a | GAAP diluted **loss** $(3.13) | $1.60 | 92.8% |
| Q4 2025 | n/a | n/a | n/a | n/a | 94.8% |
| **FY2025 (actual)** | ~$400bn+ (mgmt target language; exact total not isolated) | n/a | **$1.39** | **$6.75** | **91.2%** (vs 92.5% FY2024) |
| Q1 2026 | ≈$100,426M (derived: H1–Q2) | ≈$4,680M (derived: H1–Q2) | n/a (not isolated) | n/a (not isolated) | n/a |
| Q2 2026 | **$106,096M** (+7.3% YoY) | **$4,703M** (vs $2,381M Q2-25) | **$2.31** (vs $0.80 Q2-25) | **$2.58** (vs $1.81 Q2-25, +42.5%) | **87.4%** (−250bps YoY) |

The Q3 2025 GAAP loss was driven by a **$5.7bn non-cash goodwill impairment** against the Health Care Delivery (Oak Street Health) reporting unit — excluded from adjusted EPS (source 8). The consistent thread across every quarter with an MBR data point is **sequential improvement**: 95.2% → 92.5% (FY) → 89.9% → 92.8% → 94.8% (Q4, seasonally the highest) → 91.2% (FY) → 87.4%. Segment revenue in Q2 2026: Health Care Benefits $37.5bn, Health Services $51.8bn, Pharmacy & Consumer Wellness $33.8bn (source 2).

## 5. Guidance track record (last 4 releases, verbatim ranges)

| Release | FY adjusted EPS guidance | vs prior range | FY operating cash flow guidance | vs prior |
|---|---|---|---|---|
| Q3 2025 (Oct-29-25) | **$6.55–$6.65** (FY25) | **Raised** from $6.30–$6.40 | — | — |
| Dec-2025 Investor Day | 2026 preview: **$7.00–$7.20**; long-term "mid-teens Adjusted EPS CAGR through 2028" | Confirmed 2025 OCF $7.5–$8.0bn; teased 2026 OCF "at least $10.0bn" | teased ≥$10.0bn | preview, not official guide |
| Q4/FY2025 (Feb-10-26) | **$7.00–$7.20** (FY26 initial) | New year, first official guide | **≥$9.0bn** | **Cut** from the Investor Day's ≥$10.0bn tease two months earlier |
| Q1 2026 (May-06-26) | **$7.30–$7.50** (implied prior range referenced in Q2 release) | Raised from $7.00–$7.20 | ≥$9.5bn (implied) | Raised |
| Q2 2026 (Aug-05-26) | **$7.90–$8.10** | **Raised** from $7.30–$7.50 | **≥$11.5bn** | **Raised** from ≥$9.5bn |

FY2025 actual adjusted EPS ($6.75) beat even the raised Q3-25 range ($6.55–$6.65). Net: adjusted EPS guidance has been raised in three of the last four releases and beaten once; the one blemish is that **initial FY2026 cash-flow guidance was quietly cut versus the December Investor Day preview** before being raised twice thereafter — a nuance the headline "guidance raised" would miss if the prior range weren't checked (source 5, 6, 7).

## 6. Earnings quality & balance sheet

- **FCF conversion:** TTM OCF $14.78bn vs TTM NI $4.89bn (D3/V1 basis) — FCF conversion is distorted by the Q3-25 non-cash impairment depressing NI; on a cleaner H1-2026 basis, OCF $10.6bn vs NI $5.92bn is a more normal ~1.8x. **[Corrected 2026-10-06: cash taxes paid were only $37M in H1 2026 against $863M in H1 2025 (XBRL IncomeTaxesPaidNet), so TTM OCF of $14.78bn is flattered by about $1bn of tax timing; the FY2026 OCF guide of 'at least $11.5 billion' (verbatim, 8-K ex-99.1 acc. 0000064803-26-000097) implies a weak H2 and is the right base. FCF after SBC on the guide is about $7.8bn, not $11.0bn]**
- **GAAP vs adjusted gap:** material and explained — Q3 2025's entire GAAP-vs-adjusted gap was the $5.7bn goodwill charge plus Oak Street asset write-downs; Q2 2026's gap ($2.31 GAAP vs $2.58 adjusted) is smaller and more typical (acquisition-amortization/integration-cost add-backs).
- **Goodwill:** **$85,478M**, unchanged Dec-2025 to Jun-2026 (10-Q, source 4) — no further impairment through Q2 2026, but this is ~75% of the $114.7bn market cap and the Health Care Delivery unit (which triggered the 2025 charge) has not disclosed remaining headroom.
- **Leverage:** Net debt $47.45bn (D3/V1, latest 10-Q); TTM EBIT+D&A ≈ $12.81bn ⇒ **net debt/EBITDA ≈ 3.7x** (GAAP-TTM approximation, not the company's own covenant-defined adjusted EBITDA, which would likely be somewhat lower). **[Corrected 2026-10-06: wrong basis. TTM EBIT of $8,288M includes the $5,725M Q3-2025 goodwill impairment (XBRL GoodwillImpairmentLoss, 10-K FY2025). Ex-impairment EBIT is $14,013M, EBITDA about $18.5bn and net debt/EBITDA about 2.6x, not 3.7x. Source: 10-Q acc. 0000064803-26-000098 and 10-K acc. 0000064803-26-000010]** Credit ratings: **BBB (S&P, negative outlook), BBB (Fitch, negative outlook), Baa3 (Moody's, stable)** — two of three agencies carry a negative outlook (source 9).
- **Buybacks/dividends:** $0 buybacks in FY2025 (vs $3.02bn in FY2024) — capital preserved during the cost crisis; resumed modestly in H1 2026 (~$146M net). Dividends paid $1.725bn in H1 2026.
- **Recent M&A/financing:** No new acquisitions; **Omnicare LLC** (a legacy long-term-care pharmacy subsidiary) filed **Chapter 11** on 2025-09-22 with $110M DIP financing to resolve litigation and industry-wide LTC-pharmacy financial pressure — a contained, disclosed legacy liability, not a going-concern issue for the parent (source 10).
- **Share count:** ~1,287M diluted (D3/V1); buybacks paused then modestly resumed as above.
- **Governance:** CEO David Joyner was also named Board **Chair** effective 2026-01-01 (combined role — a minor governance flag); John Gallina (ex-Elevance Health CFO) added to the Board/Audit Committee 2026-03-19 (source 11, 12).

## 7. Valuation snapshot — explicit reconciliation with V1

**V1 says:** verdict **attractive** (score 0.94/1.0), NTM P/E 10.61x (8.8th percentile of 171-month own history), base case **+35.9%/yr** over 3 years (bear −5.4%/yr, bull +67.5%/yr), driven by a WACC of 6.64% and an assumed re-rating of the exit multiple from ~10.6x to **17.46x** plus EPS growing from $8.40 (NTM) to $12.37 (yr-3). V1 flags "base 3-yr value exceeds Street 12m high target" ($148 high target vs V1's $216 base-case yr-3 value) — its own built-in sanity check.

**My view: I agree directionally (cheap, worth owning) but I am more cautious on the magnitude/pace than V1's base case, so I mark this "cheap" but not fully "consistent" at face value** — the exit-multiple assumption (17.46x, back near CVS's pre-2024-crisis average) is the specific input I'd challenge. It presumes the market fully forgives the leverage (3.7x net debt/EBITDA), the $85.5bn goodwill overhang and the still-unresolved post-2028 Caremark cost-plus mandate (FTC-Caremark settlement, source 13) within three years. A more conservative 13–15x exit multiple — still a meaningful re-rating from today's 10.6x — would still support a solidly positive (low-to-mid-teens %/yr) return without assuming a full return to the old regime. **[Corrected 2026-10-06: the arithmetic does not tie. On V1's own EPS path ($8.40 to $12.37) a 13-15x exit gives about +24% to +29% a year, not low-to-mid-teens. The return is low-teens only if EPS growth is haircut: at 9% a year (between Street FY27 +6% and the management mid-teens target) and a flat 10.6x multiple the base is +11.4% a year]** Peer set (CI, CVS, DVA, LH, DGX; median 10.8x NTM P/E) shows CVS trading roughly in line with sector peers today, so the re-rating case rests on CVS *and the sector* re-rating together, not CVS closing a standalone discount.

## 8. Bull case / bear case

**Bull:**
1. Aetna MBR has improved for five straight comparable quarters (95.2%→87.4% YoY at Q2-26) and 2026 Medicare Advantage star ratings recovered to 81%+ members in 4-star plans (from a much weaker 2024–2025 base), locking in 2027 quality-bonus payments (source 14).
2. Adjusted EPS guidance raised in 3 of the last 4 releases; FY2025 actual beat the last raised range.
3. The July-2026 FTC-Caremark settlement resolves a multi-year antitrust overhang with a bounded, phased-in remedy (cost-plus option starts 2028) rather than an open-ended liability (source 13).

**Bear:**
1. Two of three rating agencies carry a negative outlook on CVS's BBB/Baa3 credit, at ~3.7x leverage, against $85.5bn of goodwill that has already required one $5.7bn write-down (source 8, 9).
2. PBM reform structurally caps Caremark's rebate-based economics from 2028; the near-term settlement relief could still be a medium-term margin headwind once cost-plus reimbursement is mandatory.
3. Director Larry Robbins (Glenview Capital) sold **$317M** of CVS stock on 2026-05-19 — the single largest disclosed insider transaction in the review period (source 15). **[Corrected 2026-10-06: Mr Robbins left the Board effective 13 Aug 2026 (8-K Item 5.02, acc. 0001193125-26-354096, filed 17 Aug), so he is a former director; the sale by a departing activist is a supply overhang, not an insider-confidence signal]**

## 9. Key risks & kill criteria (measurable)

1. Aetna Medical Benefit Ratio rises above **92% for two consecutive quarters** (vs 87.4% in Q2 2026).
2. Net debt/EBITDA rises above **4.0x** **[Corrected 2026-10-06: on the corrected ex-impairment basis the ratio is about 2.6x, so a 4.0x line is 1.4x away; restated criterion: net debt/(GAAP EBIT ex-impairments + D&A) above 3.5x]**, or a **second** rating agency downgrades CVS below BBB-/Baa3.
3. A **further goodwill impairment** is taken against the Health Care Delivery (Oak Street) reporting unit, following the $5.7bn Q3-2025 charge.
4. FY adjusted EPS guidance is **cut** from a prior range (breaking the pattern of raises through Q3-2025–Q2-2026).
5. 2027 Medicare Advantage star ratings (expected ~October 2026) show a **material reversal** from the 81%/63% (4-star/4.5-star) share achieved for 2026.

## 10. Catalysts & calendar

- **Next earnings:** ~2026-10-28 (Q3 2026, per D4 live snapshot).
- **2027 CMS Star Ratings release:** expected early October 2026 — likely lands at or just after this review's information cutoff (2026-09-25); check immediately on release.
- CMS 2027 Medicare Advantage/Part D rate notice (typically finalized ~April, already public by this cutoff — not separately verified in this review).
- Ongoing FTC-Caremark settlement implementation milestones through the 2028 cost-plus option start date.

## 11. Red-flag scan

- **Litigation:** Omnicare Chapter 11 (2025-09-22, contained); FTC-Caremark antitrust settlement (2026-07-14, resolved via settlement, not litigated to judgment); 10-Q XBRL references ongoing "U.S. ex rel. Bassan et al. v. Omnicare" and "In re CVS Health Shareholder Derivative Litigation" (named but substance not independently reviewed within this time box — flagged for follow-up).
- **Auditor:** Ernst & Young ratified for 2026 at the May-2026 annual meeting; no auditor change or qualification found.
- **Goodwill impairment:** $5.7bn taken Q3 2025 (disclosed, not hidden) — see section 6.
- **Insider selling:** Director Larry Robbins sold $317M (2026-05-19); other Form 4 activity in the period was routine tax-withholding on RSU vesting (CAO James Clark, Amy Compton-Phillips) — not a broad-based executive selling pattern.
- **Credit outlook:** Negative from S&P and Fitch (source 9) — a real, disclosed rating-agency concern, not a data conflict.
- **Governance:** Combined Chair/CEO role adopted January 2026 (minor).
- No restatements, no going-concern language, and no material-weakness disclosure were identified in the filings reviewed.

## 12. Data basis, recency and disclaimer

**Most recent period incorporated:** Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-05 (accession 0000064803-26-000098), plus the FY2025 Form 10-K filed 2026-02-10 and all 8-K earnings releases through Q2 2026. All figures are on a **consolidated** basis (CVS Health Corporation and subsidiaries); no standalone/parent-only figures are used anywhere in this dossier. **Events checked to:** 2026-09-25 (confirmed no company 8-K filed between 2026-08-17 and cutoff other than routine items). **GAAP vs adjusted:** every EPS figure above is labelled GAAP or Adjusted as reported by the company; V1's valuation model uses D3 GAAP TTM inputs (EBIT, NI, OCF, capex) as documented in `v1_valuation.json`. **This dossier is research only; not investment advice, and not a recommendation to buy or sell any security.**

## Sources

1. SEC EDGAR CIK 0000064803 filing index — https://data.sec.gov/submissions/CIK0000064803.json
2. CVS Q2 2026 earnings release (8-K ex-99.1, filed 2026-08-05) — https://www.sec.gov/Archives/edgar/data/64803/000006480326000097/cvs_ex99x1q2-26.htm
3. CVS Form 10-Q Q2 2026 (filed 2026-08-05) — https://www.sec.gov/Archives/edgar/data/64803/000006480326000098/cvs-20260630.htm
4. Same 10-Q, goodwill/debt/dividend extract (as above)
5. CVS Q3 2025 earnings release (8-K ex-99.1, filed 2025-10-29) — https://www.sec.gov/Archives/edgar/data/64803/000006480325000036/cvs_ex99x1q3-25.htm
6. CVS Q4/FY2025 earnings release (8-K ex-99.1, filed 2026-02-10) — https://www.sec.gov/Archives/edgar/data/64803/000006480326000009/cvs_ex99x1q4-25.htm
7. CVS December 2025 Investor Day release (8-K ex-99.1, filed 2025-12-09) — https://www.sec.gov/Archives/edgar/data/64803/000006480325000082/cvs_ex99x1investorday2025.htm
8. Healthcare Dive, "CVS hikes 2025 guidance despite goodwill impairment charge on healthcare delivery" (Oct 2025) — https://www.healthcaredive.com/news/cvs-hikes-adjusted-earnings-guidance-goodwill-impairment-oak-street-q3-2025/804104/ ; Home Health Care News, "CVS To Close 16 Oak Street Locations" — https://homehealthcarenews.com/2025/10/cvs-to-close-16-oak-street-locations-temper-growth-trajectory/
9. S&P Global Ratings / cbonds credit-rating summaries (BBB/Baa3/BBB, negative/negative/stable outlooks) — https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3235109 ; https://cbonds.com/news/3412627/
10. CVS 8-K, Omnicare Chapter 11 filing (2025-09-22) — https://www.sec.gov/Archives/edgar/data/64803/000119312525211349/d57621dex991.htm
11. CVS 8-K, Joyner named Chair (2025-11-20) — https://www.sec.gov/Archives/edgar/data/64803/000119312525289805/d172430dex991.htm
12. CVS 8-K, Gallina board appointment (2026-03-19) — https://www.sec.gov/Archives/edgar/data/64803/000006480326000017/cvs-20260318.htm; 8-K annual-meeting results (2026-05-18) — https://www.sec.gov/Archives/edgar/data/64803/000006480326000082/cvs-20260514.htm
13. FTC press release, "FTC Secures Major Settlement with Caremark" (2026-07-14) — https://www.ftc.gov/news-events/news/press-releases/2026/07/ftc-secures-major-settlement-caremark-resolving-antitrust-case-against-second-drug-middleman
14. Aetna/CVS press release, "Aetna achieves over 81% of Medicare Advantage members in 4-Star plans... for 2026" — https://www.prnewswire.com/news-releases/aetna-achieves-over-81-of-medicare-advantage-members-in-4-star-plans-and-over-63-in-4-5-star-plans-for-2026--302580277.html ; Becker's Payer Issues — https://www.beckerspayer.com/payer/medicare-advantage/cms-posts-2026-medicare-advantage-star-ratings-8-notes/
15. MarketScreener, "CVS Health Insider Sold Shares Worth $317,471,136" (Larry Robbins, 2026-05-19) — https://www.marketscreener.com/news/cvs-health-insider-sold-shares-worth-317-471-136-according-to-a-recent-sec-filing-ce7f5adfd98efe24
16. V1 systematic valuation model — `v4/outputs/v1_valuation.json`, `v4/outputs/v1_valuation_table.csv` (as of 2026-09-25)
17. B1 quant factor scores — `v4/data/b1_live_scores.csv` (as of 2026-09-25); D4 live snapshot (analyst targets, beta, next-earnings date) — `v4/data/d4_live_snapshot.parquet`

## Re-assessment (RA11, 2026-10-06)

**Scope and result.** Recency check on EDGAR (submissions API, CIK 0000064803, pulled 2026-10-06): the only filing after the 5 Aug 2026 10-Q/8-K is the 17 Aug 8-K (Items 5.02, 7.01, 9.01; acc. 0001193125-26-354096: Teresa Heitsenrether joins the Board effective 18 Nov 2026; Larry Robbins left the Board on 13 Aug 2026), a 13G/A (13 Aug) and a 13F (6 Aug). No 8-K, 13D or S-4 after 25 Sep. The 2027 Medicare Advantage Star Ratings were not found in a primary source as of 2026-10-06 (kill criterion 5 untested). Verdict INCLUDE-SMALL is **unchanged**; implied-vs-base is **below**; three dossier statements are corrected (leverage basis, the 13-15x arithmetic, Robbins status) and the cash-flow base is restated.

**Inputs.** Macro inputs (primary): 10-year Treasury 5.17% on 25 Sep 2026 (FRED DGS10; 5.24%, 5.26%, 5.29%, 5.24%, 5.28% on 28 Sep to 2 Oct, not used); Fed target range raised to 3.75-4.00% on 16 Sep 2026. Cost of equity = 5.17% + Blume-adjusted 5-year weekly beta (V1 file) x 4.14% ERP (programme V1 parameters); a 9.0% stress rate is shown because the V1 betas for DG, DVA and CVS (0.57-0.66) are low. Reverse DCF is at equity level: free cash flow = operating cash flow minus capex minus stock-based compensation (SBC is a cost, not added back), market capitalisation = price x latest cover-page shares, 10 years of constant growth then 3.0% terminal growth. CVS: price $89.13, 1,278.97M shares (cover, 29 Jul 2026), market cap $113.99bn; Blume beta 0.66, Ke 7.91% (V1 file).

**Cash-flow base (replaces TTM FCF of $11.0bn).** FY2026 OCF guide 'at least $11.5 billion' less TTM capex $3.02bn less TTM SBC $0.72bn = $7.76bn (6.8% yield on market cap). TTM interest expense is $3.10bn (already inside OCF). Net debt $47.45bn at 30 Jun 2026 (debt $61.4bn less cash $11.3bn less short-term investments $2.6bn; consolidated, CVS Health Corporation). Cash-tax timing: H1 2026 cash taxes $37M vs $863M; the stress case deducts a further $1.0bn.

**Reverse DCF (implied 10-year FCF growth).** Central FCF $7.76bn: -1.5% at Ke 7.91%, -0.1% at 8.5%, +0.9% at 9.0%, +2.0% at 9.5%. Stress FCF $6.76bn: +0.2% / +1.6% / +2.8% / +3.8%. Evidence-based base case 5.5% a year (EPS +9% for three years, +4% afterwards; Street FY27 EPS $8.53 is only +6% on FY26 $8.04, and management's 'mid-teens' target is the upper bound). **Implied vs base: BELOW (cushion 3-5 points). Direction unchanged; V1's -6.4% capitalised an EBIT depressed by the $5.7bn impairment and was too low.**

**Scenarios, 3-year annualised from $89.13 (replaces V1 -5.4% / +35.9% / +67.5%; V1 arithmetic reproduced: $12.37 x 17.46 gives +36.0%).** Dividends $2.66 a year held flat. Bear: EPS falls to $6.00 (medical cost relapse; below FY25 adjusted $6.75), 9.0x: **-11.4%**. Base: EPS +9% a year to $10.88, flat 10.6x (peer median 10.8x): **+11.4%**. Bull: EPS +13.8% a year (management path, $12.37), 14.0x: **+26.7%**. The base return exceeds Ke (7.9-9.0%) by 2.4-3.5 points; V1's +35.9% depended on a re-rating to 17.5x that the dossier itself said was not assured.

**Other checks.** (1) Guidance quoted verbatim from the 5 Aug release: GAAP diluted EPS guidance range to $6.84 to $7.04 from $6.24 to $6.44; Adjusted EPS guidance range to $7.90 to $8.10 from $7.30 to $7.50; cash flow from operations guidance to at least $11.5 billion from at least $9.5 billion. On GAAP guidance the P/E is about 12.8x, not 10.6x. (2) Aetna MBR 87.4% (Q2) and 86.0% (H1) include $1.2bn of favourable prior-year reserve development in H1 2026 (release text); part of the improvement is reserve-driven. (3) Goodwill $85,478M unchanged; Aetna medical membership 26.0M. (4) Corrected leverage 2.6x (inline correction). Verdict reason: the margin of safety survives the corrected method (FCF yield of 6.8% after SBC and interest against an implied growth near zero) and no kill criterion has fired, but half weight stays because the Star Ratings, the Q3 print (about 28 Oct) and the 2028 Caremark cost-plus change are unresolved.
