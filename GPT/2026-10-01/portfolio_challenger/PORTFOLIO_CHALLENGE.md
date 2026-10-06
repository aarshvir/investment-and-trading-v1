# Independent portfolio construction challenge — 1 October 2026

**Status:** independent research input to the new GPT release, not a trade instruction or a new completed release. **Exact completed parents examined:** `v011_2026-09-27_claude` and `v012_2026-09-27_codex`. **Data cutoff for the numerical tests below:** US close 25 September 2026; the attached 1 October audit was evaluated as a methodological proposal. No 1 October executable quote, actual holding, tax status or confirmed account return is represented here. The calculations read the **immutable v011 package**, since the active `v4/code/lead_build_portfolio.py` has already diverged from that publication.

## Investment judgment

The attached audit identifies the right next problem: after broad research coverage, selection and valuation quality matter more than another large batch of dossiers. Its proposed optimizer cannot safely consume the current raw return column. The 214 eligible v011 names contain 210 finite numeric “base” scenarios, but the scenarios mix analyst and systematic methods, and several of the highest values assume very large multiple expansion that their own dossiers question. Optimizing these values would reward the most optimistic model, not necessarily the strongest business.

The current **15–20% tolerable drawdown** and the completed v012 **25% maximum equity** policy still govern the actionable new-money model. Calling a 70–100% equity portfolio “moderate” does not reconcile it with that loss tolerance. The risk budget may be reconsidered with the owner, but a change requires an explicit new mandate and corresponding stress, liquidity and tax analysis. No v011 holding should be adopted solely because it was selected from 214 eligible companies.

## What the published numbers establish

| Diagnostic | Reproduced result | Decision implication |
|---|---:|---|
| v011 eligible names / holdings | 214 / 20 | Coverage is broad; selecting the marginal name matters. |
| Eligible names with a finite numeric base scenario | 210 / 214 | Four lack even the value required by a return optimizer; the 210 remaining values are not necessarily comparable or calibrated. |
| Selected v011 holdings with a V1 systematic valuation record | 1 / 20 (LVS) | The portfolio's 13.04% weighted base figure mostly combines dossier estimates, not one uniform model. It is a scenario average, not an expected CAGR. |
| Reasonable analyst-priority orderings tested | 3 / 3 selected the same 20 | The audit's “only six robust names” claim needs qualification. |
| Orderings that substitute the original quant rank | 9 and 6 names overlap | This demonstrates a material method choice, but the quant ranking itself has no demonstrated alpha. |
| Largest v011 holding / sector | WEC 8.32% / Financials 25.00% | The stock sleeve's 10% name and 25% sector ceilings are close/binding; economic confidence needs to justify WEC's size. |

The five ordering results are recorded in `v4/outputs/lead_j_sensitivity.json` inside the immutable package. The first three vary conviction, margin of safety and base-return order yet reproduce exactly the same list. The last two insert model rank and retain nine and six names. The six-name intersection is a useful sensitivity warning, but it does **not** mean 14 names change under small perturbations of the actual analyst rules. Likewise, the original point-in-time factor backtest's lack of demonstrated alpha cannot be turned into validation for the analyst portfolio or the model-rank alternative.

## Return dependence on re-rating

The following holds each V1 base-case year-three EPS and cumulative dividends fixed, replaces the assumed exit P/E with the 25 September NTM P/E, then compounds the endpoint value over three years. It is a **sensitivity**, not a revised forecast; it inherits any EPS/share-count mistakes, ignores dividend timing, taxes, dealing costs and corporate restructuring, and compares an NTM current multiple with a year-three exit period.

| Candidate | V1 base return | Today's NTM P/E → V1 exit P/E | Return with flat P/E | Underwriting implication |
|---|---:|---:|---:|---|
| CMCSA | 62.14%/yr | 6.16× → 17.17× | 18.17%/yr | Own dossier calls 62% dependent on a pending separation and rejects the magnitude. |
| BKNG | 39.34%/yr | 13.83× → 30.10× | 7.98%/yr | Own dossier explicitly rejects 39% as a credible base case. |
| LVS, an actual v011 holding | 37.47%/yr | 11.47× → 23.50× | 9.81%/yr | The apparently exceptional base return needs a more defensible exit valuation and Macau/Singapore capital-spend bridge. |

These are archived September prices. The crucial finding is the large **method sensitivity**, not the precise flat-multiple return. In particular, calling LVS's 37.47% a central expected return would overstate the case unless the 23.50× exit multiple is independently supported. At its 3.84% sleeve weight, the difference between 37.47% and 9.81% alone changes a naïve weighted annual base average by about **1.06 percentage points** before any other correction. This weighted difference is a diagnostic, not a portfolio CAGR calculation.

WEC deserves a separate capital-intensive-utility test. Its archived dossier cites the 25 September $101.45 price, FY2026 guided EPS midpoint $5.56 and management's 7–8% long-run EPS growth range. **Its estimated $3.53 annual dividend is stale:** the issuer declared $0.9525 quarterly in 2026, or a $3.81 annual run rate. At **7.5% EPS growth for three years**, a flat $3.81 annual cash dividend and an 18.25× exit P/E (the price divided by that FY2026 EPS) produce about **11.01% gross cash-flow IRR**. A 15× exit yields **4.43%**, and a 13× exit about **−0.08%**. This is a mechanical valuation sensitivity with no tax, costs, dilution change or refreshed price. WEC's dossier “reverse DCF” discounts EPS using 7.5% cost of equity and 3.5% terminal growth even though the utility needs heavy capital spending and external equity/debt financing; earnings are not freely distributable owner cash. Its negative implied-growth result should not independently justify an 8.32% sleeve allocation. The issuer's [FY2025 results](https://investor.wecenergygroup.com/investors/news-releases/press-release-details/2026/WEC-Energy-Group-posts-2025-results/default.aspx) corroborate the EPS guidance and long-term range; its [2026 dividend declaration](https://investor.wecenergygroup.com/investors/news-releases/press-release-details/2026/WEC-Energy-Group-declares-quarterly-dividend-7ab72a82c/default.aspx) establishes the current cash dividend.

## Mandate and historical shock comparison

The table reproduces v011's **quarterly-rebalanced historical replay**, which applies today's holdings to old crises and assumes a constant 4% annual reserve return. It is a diagnostic of sensitivity to historic price paths, not a backtest of what the present manager could have bought then. GDDY and VEEV lacked 2007–09 share prices; 6.21% of the sleeve is filled with SPY in the mixed portfolios for that episode.

| Allocation tested in v011 | Equity share | GFC episode / worst point | COVID episode | 2022 episode | Fit with current mandate |
|---|---:|---:|---:|---:|---|
| S&P 500 proxy (SPY) | 100% | −55.19% | −33.72% | −24.50% | Relevant market comparison, but also outside the current loss tolerance. |
| v011 stock sleeve alone | 100% | −47.35% / sleeve maximum drawdown −47.70% | −37.43% | −17.34% | Fails the stated 15–20% tolerance in two episodes. |
| “Moderate” 55% index / 15% v011 sleeve / 30% reserve | 70% | −39.50% | −24.05% | −15.62% | Exceeds the stated tolerance in GFC and COVID. |
| 15% index / 10% v011 sleeve / 75% reserve | 25% | −12.04% / −12.70% | −8.53% | −3.48% | Historically inside tolerance for these episodes; not a future floor. |

The 10% v011 direct-stock sleeve is a **shadow comparison**, not an endorsed switch. It would place the largest single direct stock at **0.832%** of total capital and the largest direct sector at **2.50%**, under v012's 2% name and 5% direct-sector planning limits before index look-through. Actual issuer overlap, live entry prices, taxes and trading capacity must still be checked. The v012 starter model has only 4% direct exposure; moving to the full 10% requires funded, independently underwritten replacements.

Portfolio economics make the scope of stock selection clear: improving the direct sleeve's *true* annual return by 5 percentage points increases a 10%-direct whole portfolio's annual return by about **0.5 percentage point before costs**, assuming stable weights. A 1-point change in the return on a 75% reserve moves the whole portfolio by about **0.75 point**. These are allocation identities, not forecasts. They explain why reserve instrument, tax, fees and the equity budget deserve the same scrutiny as an exact top-20 stock order.

## Candidate decisions for the research queue

These classifications concern **further underwriting**, not personalized sales of unknown actual holdings or 1 October buy orders:

| Name/group | Research action | Evidence that would change an allocation |
|---|---|---|
| WEC | Challenge the largest v011 weight | Rebuild regulated cash available to owners after capex, debt and equity issuance; stress 15×/13× exits and rate decisions. |
| LVS | Challenge the v011 37.47% return claim | Reconcile Macau concession and Singapore expansion cash uses, terminal EPS and an exit multiple that does not simply double. |
| CMCSA, BKNG | Near-miss valuation work, no automatic promotion | Rebuild post-separation/post-regulatory owner cash and peer-adjusted multiples; use flat-multiple and contracting-multiple cases. |
| RSG, LH | Research alternatives only | Repair the cash-flow/discount-rate definitions and debt/reimbursement bridges already identified in v012. |
| AMP, PAYX | Preserve v012's conditional starter framework pending this week's fresh quote/event/accounting gates | Compare any replacement against their after-cost, after-withholding purchase ceilings and the direct 10% funding limit. |
| Remaining v011 holdings | Preserve as candidates | Produce comparable company-specific bear/base/bull cash flows, purchase prices and no-re-rating returns before pairwise replacement claims. |

No evidence here proves that any one of the 20 should be sold from an actual account, because actual positions and tax lots were not supplied. A price falling below a limit by itself does not clear the thesis and event gates.

## Feasible next construction method

1. **Freeze the mandate and comparison set.** Use v012's 15% index, up to 10% direct and at least 75% reserve as the current feasible set. Record 25% index/75% reserve, v012 current proposal and a constrained v011 shadow as immutable competitors. Revisit the cap only through an explicit policy revision with a new stress analysis.
2. **Normalize per-security economics.** Forecast operating drivers, share count, net debt/regulatory capital, distributable cash/dividends, and bear/base/bull terminal value at the same dated price and fiscal horizon. Keep reported, adjusted and normalized figures separate. Calculate after-withholding/cost returns and an explicit flat/contraction/expansion multiple bridge. For banks, insurers, REITs and utilities use sector-appropriate balance-sheet and distributable-cash mechanics.
3. **Represent estimation error.** Give each growth, margin, capital and exit-multiple input an evidence locator, vintage, range and owner. Distinguish management guidance from analyst judgment. Use historical forecast errors and prospective misses to shrink estimated alpha; do not assign arbitrary outcome probabilities or optimize uncalibrated point forecasts.
4. **Construct and challenge portfolios jointly.** First exclude candidates with missing decision-critical data. Compare feasible weights under name, sector, fund-overlap and liquidity limits. Show sensitivity to covariance estimator, expected-return shrinkage, terminal multiple, tax and costs. Evaluate historical replays plus forward correlated operating shocks; label replays as diagnostics. A mathematically computed frontier is useful only if its inputs are identified and its instability is shown.
5. **Learn prospectively.** Before each change, lock the dated scenario, price, source hashes, predicted return interval, rejection reason and benchmark. Report forecast errors, drawdowns, tax/cost drag and selection turnover at 30 days, 90 days and 12 months without rewriting old forecasts.

**Release implication:** This challenge supports the attached audit's call for comparable underwriting, no-multiple testing, forecast calibration and prospective shadow portfolios. It rejects using a raw 214-name optimizer, treating v011's weighted scenario average as an expected return, or widening the current equity allocation merely because the all-stock sleeve's three-year beta is 0.59. It does not itself change v012's AMP/PAYX ceilings or weights.

### Reproducibility and locators

- [`diagnostics.json`](diagnostics.json) and [`reproduce.py`](reproduce.py) derive the quantities above directly from the immutable `versions/v011_2026-09-27_claude/package.zip` entries `v4/outputs/lead_portfolio_build.json`, `lead_j_sensitivity.json`, `lead_risk_results.json`, and `v1_valuation.json`. The source ZIP's SHA-256 matches `versions/catalog.json`; each read member's SHA-256 is recorded in the diagnostics.
- Archived selection and sizing: `v4/code/lead_build_portfolio.py` lines 194–227 and `v4/code/lead_portfolio.py` lines 23–53 in that ZIP. The current working copy of `lead_build_portfolio.py` differs from the published one, so it was not used as v011 evidence.
- The underlying company caveats are archived in `v4/dossiers/CMCSA.md` §7, `BKNG.md` §7, `LVS.md` §7 and `WEC.md` §§5–7. The v012 mandate and disagreements are in its immutable release notes and `review/ready/WEEKLY_POLICY_V2.md` as archived in `versions/v012_2026-09-27_codex/package.zip`.
