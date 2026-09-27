# AMZN — Amazon.com, Inc.

## 1. Verdict
**WATCH.** Horizon 12–36 months. AWS is genuinely re-accelerating (37% YoY, an 18-quarter high) with a $496bn backlog growing triple-digit — the strongest "real demand, not just capex" signal in this batch — but it is being funded by capex so large ($220bn 2026 guide) that trailing free cash flow has turned negative on one commonly used measure, leverage has risen sharply, and the model's own quality factor score is the weakest of the four names reviewed. The 25-Sep-2026 close ($249.67) implies a 10-year revenue CAGR of ~14.9% versus an evidence-based base case of ~10.9%.

## 2. Business in plain English
Amazon runs the largest US e-commerce marketplace (retail, third-party seller fees, advertising) and, through AWS, the largest cloud infrastructure business in the world, renting compute, storage and — increasingly — AI model access (Bedrock) and custom AI chips (Trainium) to enterprises. It makes money on razor-thin retail/logistics margins subsidized in large part by AWS's much higher-margin cloud and advertising businesses.

## 3. Why the model likes it — durability check
b1 composite **0.563** (decile 6, quintile 3, live_rank 218 — the model was neutral-to-mildly-positive, well outside its own top-30). The composite is carried entirely by **Momentum** (fam_M 0.754) and especially **Earnings momentum** (fam_S 0.991, the highest of any family score in this batch) — Amazon has beaten EPS estimates in all of the last 8 quarters with an average surprise of +50%. But **Quality (fam_Q 0.136) is by far the weakest score of the four companies** in this program, reflecting the capex-driven balance-sheet and cash-flow deterioration described in §6 below (heavy asset growth, rising leverage, and — depending on the measure — negative free cash flow are all *negative* inputs to the quality family). This is not an artefact: it is a real, current, disclosed condition of the business, not a modeling quirk.

## 4. Last two years of results (quarterly highlights, $bn GAAP)
| Quarter | Total revenue | YoY | AWS revenue | AWS YoY | AWS op. margin | Consol. op. margin |
|---|---:|---:|---:|---:|---:|---:|
| Q2 2026 | $200.6 | +20% | $42.2 | **+36.7%** (fastest in 18 qtrs) | 39% (+650bps YoY; +520bps ex-derivative gains) | 14% (+2pp YoY) |

AWS added **$4.6bn of sequential revenue** in Q2 2026 — about 80% more than its largest previous quarterly increase — and is now a **$169bn annualized run-rate** business [Investing.com transcript; TechTimes]. **AWS backlog: $496bn, growing triple-digit YoY**; a separate **$225bn+ of Trainium revenue commitments** is disclosed on top of that backlog [TechTimes, 2026-07-31; valueaddvc]. AWS AI services and custom-chip revenue each independently crossed **$25bn annualized run-rate**, both growing triple-digit YoY; Bedrock customer spend grew 170% QoQ in Q1 2026, with Bedrock processing more tokens that quarter than in all prior years combined [multiple sources, 2026 Q1/Q2 earnings coverage]. TTM revenue (d4): $775.7bn. NTM consensus EPS $11.13 (d4); trailing EPS $12.42.

## 5. Guidance track record
2026 capex guidance was raised from ~$200bn to **~$220bn** at the Q2 2026 call, explicitly attributed to higher memory costs, not to weaker-than-planned demand. Management (CEO Andy Jassy) stated Amazon **still won't have enough capacity to meet 2026 demand, and expects the same to be true in 2027** [Fortune, 2026-07-30] — a demand-constrained framing, which is bullish for revenue durability but confirms the capex burden will not ease soon.

## 6. Earnings quality & balance sheet — the central issue for this name
- **Data conflict (flag per program instructions):** the v4 quant snapshot (`d4_live_snapshot.parquet`) shows trailing FCF of **+$3.2bn**, while independent Q2 2026 earnings coverage reports **TTM free cash flow of −$7.6bn**, a 142% YoY decline from +$18.2bn a year earlier [Barchart, Investing.com, 2026-07]. The gap is very likely a definitional difference (Yahoo's FCF field vs. Amazon's own operating-cash-flow-minus-capex-and-equipment-finance-leases definition, which explicitly moved negative per the company's own slides), but it is large enough (a ~$11bn swing) that it should not be taken at face value from either source without reconciling the exact capex/lease treatment — **treat AMZN's "FCF" as ambiguous pending reconciliation.**
- TTM cash capex reached **$173bn**, up from $107bn a year earlier; operating cash flow rose ~33% YoY over the same period — the FCF deterioration is a capex story, not an operating-cash story.
- **Long-term debt principal+interest reached $220.3bn as of 30-Jun-2026**, roughly doubling within six months; Amazon has stated it will "continue evaluating funding options," i.e., more debt issuance is plausible [AlphaQuery; company disclosures].
- Stock-based compensation: Q2 2026 $10.07bn (down 1.5% YoY — a rare instance of SBC *not* growing among these four names), Q1 2026 $4.03bn — treat as a real cost regardless of the recent flattening.

## 7. Valuation — reverse DCF (no V1 row exists for this ticker; valuation performed directly here)
**10-year reverse DCF:** 12.5% discount rate (higher than MSFT/GOOGL to reflect thinner margins and capex/leverage risk), 16% terminal consolidated operating margin (vs. today's 14%, allowing continued mix-shift toward AWS/advertising), 20% tax, ~10.79bn diluted shares (from market cap/price), 22x terminal P/E. The $249.67 close requires a **constant 10-year revenue CAGR of ~14.9%**.

**My base case:** AWS decelerating from 37% today toward the high-teens by year 3 as the $496bn backlog converts and the base compounds past $250bn+ annualized, blended with mid-single-digit-to-low-double-digit retail/advertising growth. Explicit path (18%/16%/13%/12%/11%/10%/9%/8%/7%/6%) gives a 10-year compound-equivalent of **~10.9%** and a base-case fair value of **~$176** — **~42% below** the current $249.67. **implied_vs_base: above.**

**3-year scenario returns (IRR from $249.67; Amazon pays no dividend, so all return is price appreciation):**
| Scenario | Yr3 revenue | Op. margin | P/E | Yr3 price | 3-yr IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $1,004.5bn | 12% | 16x | $143 | **−17.0%** |
| Base | $1,179.7bn | 16% | 22x | $308 | **+7.2%** |
| Bull | $1,340.4bn | 20% | 28x | $557 | **+30.6%** |

Of the four names, AMZN's base-case 3-year return (+7.2%) is the least unattractive on this framework — but the weak quality score and FCF ambiguity mean the margin-of-safety is genuinely lower than the headline valuation gap alone would suggest.

## 8. Bull case
1. AWS's re-acceleration to an 18-quarter-high growth rate, with a $496bn backlog (growing triple-digit) plus $225bn of separate Trainium commitments, is real, dated, disclosed demand — not a hopeful extrapolation.
2. AWS operating margin expanded 650bps YoY even while absorbing the AI capex ramp, showing the segment is not just growing but getting more profitable at the same time.
3. Retail/advertising margin improvement (consolidated op margin +2pp YoY) provides a second, independent earnings lever besides AWS.

## Bear case
1. Quality-factor deterioration is the worst of any name in this program (fam_Q 0.136) — real, current, and driven by the same capex program that bulls point to as the growth driver, i.e., growth and quality-erosion are two sides of the same coin right now.
2. FCF is ambiguous-to-negative on the most recent TTM data by at least one credible external measure, while long-term debt has roughly doubled in six months — a genuine, not hypothetical, capex burden.
3. A separate FTC monopoly-power lawsuit (marketplace/pricing practices) is scheduled for a **bench trial starting 9-Feb-2027** — later than earlier expected (originally Oct-2026) but a real, dated event risk to core retail-marketplace economics, distinct from and in addition to the $2.5bn Prime-enrollment settlement Amazon already paid [Bloomberg Law, MLex, 2026].

## 9. Key risks & kill criteria (thesis-invalidation triggers — signposts to watch)
1. AWS revenue growth decelerates below **28% YoY** for two consecutive quarters (would break the re-acceleration thesis).
2. TTM free cash flow (reconciled, company-reported basis) remains negative for **three consecutive quarters** after 2026 capex guidance is met (i.e., the negative FCF print becomes structural, not a temporary supercycle).
3. Long-term debt principal+interest exceeds **$300bn** without a corresponding step-up in AWS backlog.
4. 2026 capex guidance is raised a **third time** beyond $220bn.
5. FTC monopoly-power case survives Amazon's motion to dismiss and proceeds toward the Feb-2027 trial with a scope that includes structural remedies.

## 10. Catalysts & calendar
Next earnings: **2026-10-29** (per d4 snapshot). FTC v. Amazon monopoly-power bench trial: **9-Feb-2027** (quarterly status conferences precede it). No EU DMA-specific enforcement action against Amazon identified in this window beyond the general 2026 enforcement-plan framing (potential fines across Apple/Google/Meta/Amazon/Microsoft collectively exceeding €100bn, per Commission estimates, but no Amazon-specific decision dated).

## 11. Red-flag scan
No auditor changes, restatements or going-concern language identified. **Data conflict flagged in §6** (FCF: +$3.2bn per d4 vs. −$7.6bn TTM per external Q2 2026 coverage) — resolve before using either figure as an input to portfolio-level cash-flow assumptions. Separate, closed item: Amazon paid a **$2.5bn/$1.5bn-range FTC settlement** over unlawful Prime enrollment/cancellation practices (dates and exact amount vary by source; treat as resolved, not a live risk). No short-seller report identified in this window.

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q (quarter ended 30 June 2026, filed ~July/August 2026) and the Q2 2026 earnings release/call. Events checked to 2026-09-25 close. GAAP figures are labeled GAAP; the FCF conflict in §6 is explicitly unresolved and disclosed as such rather than silently picking one source. Research, not personalized investment advice; not a recommendation to buy or sell.

## 12. Sources
1. Amazon Q1 2026 10-Q — https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000014/amzn-20260331.htm
2. Amazon Q2 2026 10-Q — https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000026/amzn-20260630.htm
3. TechTimes — AWS backlog $496bn, capex raised to $220bn — https://www.techtimes.com/articles/322572/20260731/aws-backlog-hits-496b-amazon-raises-ai-spend-220b-capacity-runs-short.htm
4. Fortune — Jassy: "won't have enough capacity" — https://fortune.com/2026/07/30/andy-jassy-amazon-capex-demand-aws-pga-tour/
5. Investing.com — Q2 2026 earnings call transcript, AWS growth acceleration — https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442
6. Barchart — "Amazon's free cash flow and FCF margins tumble" — https://www.barchart.com/story/news/33814326/amazon-s-free-cash-flow-and-fcf-margins-tumble-is-amzn-overvalued
7. Investing.com — Q2 2026 slides, FCF turns negative — https://www.investing.com/news/company-news/amazon-q2-2026-slides-aws-surges-37-free-cash-flow-turns-negative-93CH-4826472
8. Bloomberg Law / MLex — FTC v. Amazon trial date Feb-2027 — https://news.bloomberglaw.com/antitrust/amazon-poised-for-late-2026-trial-in-ftc-monopoly-power-lawsuit ; https://www.mlex.com/mlex/articles/2349579/amazon-loses-bid-to-keep-october-2026-trial-date-for-us-ftc-antitrust-case
9. v4 data snapshot — `v4/data/d4_live_snapshot.parquet` (25-Sep-2026 close $249.67), `v4/data/b1_live_scores.csv` (factor scores)
