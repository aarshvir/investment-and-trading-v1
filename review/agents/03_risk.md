# Independent risk, portfolio construction and probability audit

**Decision:** The supplied portfolio is not implementation-ready. Its advertised construction constraints are infeasible for the selected universe; delivered weights break those constraints; the five-year probability is a conditional simulation result rather than calibrated investor confidence; and its own reconstructed drawdown exceeds the user's 15–20% tolerance.

This audit reproduces supplied data, not authenticates market history. Source provenance and current quotes need separate validation. No new allocation is recommended here.

## Reproduction and evidence

Read-only source files: `source_bundle/equity_project/conv_port.py`, `opt.py`, `bt10.py`, `backtest3.py`, `conv_port.json`, `port2.json`, and inspected pandas pickles. Pickle opcode/global review was completed before loading; only pandas/numpy reconstruction globals and `builtins.slice` were found in the four files used. A restricted unpickler additionally rejects unexpected globals.

Reproduction script: `review/data/risk_audit.py`. Outputs: `risk_audit.json`, `risk_sensitivity.csv`, `risk_pickle_opcodes.txt` in that directory. Run the script from workspace root with the bundled Python. These artifacts contain exact weights, constraints, missing history, reproducible sensitivity outputs and seeds. Stock portfolio original one-year and five-year simulation statistics reproduce exactly, including 71.92% one-year probability of profit, 86.855% five-year probability, and 27.68% probability of doubling over five years. Delivered weights match after rounding (maximum difference 0.00475 percentage points).

## 1. Portfolio constraints fail, and cannot all be met

`conv_port.py:9–14` clips individual weights and sector totals, then renormalizes to 100%. Renormalization pushes weights back over caps. Fifty iterations cannot repair an infeasible constraint set.

| Constraint | Stated | Actual exact calculation |
|---|---:|---:|
| RL single stock | ≤10% | 10.6325% |
| ABNB single stock | ≤10% | 10.6325% |
| Financials | ≤25% | 26.2450% |
| Industrials | ≤25% | 26.2450% |
| Information Technology | ≤25% | 26.2450% |
| Consumer Discretionary | ≤25% | 21.2650% |

The basket contains four sectors. Full investment with each ≤25% requires exactly 25% per sector. Consumer Discretionary contains only RL and ABNB, which can supply at most 20% under the 10% stock cap. Thus the maximum feasible investment is **95%**, with three sectors at 25% and Consumer Discretionary at 20%. A feasible construction requires at least 5% unallocated/cash weight, an eligible additional sector/name, or an explicitly revised cap. This algebra does not depend on solver choice.

V2 has separate implementation defects. `opt.py:27–28` accepts `r.x` without checking optimizer success, removes positions ≤2%, and renormalizes. `opt.py:49` again removes small weights and renormalizes; `opt.py:63–65` trims the final portfolio to 20 positions and renormalizes without rechecking constraints.

Auditing saved V2 weights shows:

- Guardian modeled volatility 14.293% versus 14% cap (original unrounded report:14.294%); AIZ10.35% versus10%; BIIB7.24% versus its7% confidence-dependent cap. Three subindustries exceed12%: Asset Management12.42%, Biotechnology12.41%, Industrial Conglomerates12.42%.
- Recommended Information Technology30.42% versus30%; Asset Management12.41% versus12%.
- Balanced, Hurdle and Stretch saved weights passed these stock/sector/subindustry checks at tolerance0.01 percentage point. Rounded weight sums differ from100% by up to0.02 percentage point; this is immaterial compared with the larger violations.

**Repair:** feasibility-check the eligible set first; check solver status and every constraint independently; never prune and normalize after the final solve. If small positions must be removed, fix their weights at zero, rerun the constrained solve, and validate again. Persist solver status, residuals, covariance date and unrounded weights. Official [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html) explicitly provides `success` and `message`; the supplied code ignores both. A full optimizer rerun was not completed because this machine's application-control policy blocked a SciPy binary; reported violations are independently calculated directly from delivered weights and covariance inputs, not inferred from an attempted solve.

## 2. Missing history understates risk, especially in the COVID replay

The daily file covers2015-09-25 through2026-09-24. The probability engine uses121 observations labelled2016-09-30 through2026-09-30. September2026 is a partial month labelled as month end, not evidence of future price observations.

ABNB first appears2020-12-10 and has **52 missing monthly returns of121**, all replaced with0 by `conv_port.py:15`. During the 2020 crash, a10.63% ABNB allocation is effectively zero-return cash. The result cannot be described as an observed replay of that14-stock portfolio. `opt.py:30,37–38` uses the same zero-fill design.

Illustrative sensitivity, using the same supplied data and expected returns:

| Missing-history treatment | Months | Stock volatility | Stock5yr profit probability | 50/50 blend5yr profit probability |
|---|---:|---:|---:|---:|
| Original zero filling |121|18.93%|86.86%|89.85%|
| Index-return proxy before listing |121|19.60%|85.66%|89.19%|
| Common actual-return history from2021 |69|19.28%|87.95%|91.34%|

The proxy is a sensitivity, not fabricated ABNB history. Restricting to common history also removes COVID; the seemingly better probability does not validate it. Production research should preserve missingness, distinguish IPO/delisting/data failures, use a documented economically appropriate proxy only for explicit stress assumptions, and disclose the actual common sample. Long-horizon inference needs a longer independent market history spanning more regimes.

## 3. “90% over five years” does not survive reasonable specification changes

`conv_port.py:18` forcibly recenters monthly returns to `(1+E)^(1/12)-1`. Thus the forecast is primarily conditional on the assumed drift. It is not a direct historical success rate, not evidence of forecast calibration, and not a probability of meeting the user's loss tolerance. The code's drift mapping targets a monthly arithmetic mean; it does not make E the expected geometric CAGR. Volatility drag and block dependence affect compound outcomes.

Independent20,000-path rerun, fixed3-month circular blocks, seed5, original missing-data treatment, 50% stocks/50% index:

| Assumed annual return input | Simulated chance of nominal profit after5years | Five-year5th-percentile cumulative return |
|---:|---:|---:|
|0%|43.5%|−47.7%|
|2%|55.2%|−42.2%|
|4%|66.1%|−36.3%|
|6%|75.3%|−29.8%|
|8%|82.7%|−22.9%|
|10%|88.2%|−15.4%|
|10.68% original blend assumption|89.8%|−12.7%|
|12%|92.6%|−7.3%|

These rows are **model sensitivity, not alternative forecasts**. The delivered blend90.125% and our89.845% differ modestly with random seed/implementation and rounded weights; the stock probabilities reproduce exactly. At90% with20,000 paths the Monte Carlo standard error is approximately0.21 percentage point, giving roughly±0.42 percentage point95% simulation error. This excludes the much larger uncertainty in expected returns, sampling period, future regimes and model choice.

Keeping the original10.68% return assumption but changing fixed block length to1/3/6/12/24months produces87.58%/89.85%/91.53%/91.83%/95.48%. Choosing the block size yielding a desired headline would be model selection bias. Long blocks here improve the headline because of this particular historical path; that is not proof of greater reliability. The implementation is a fixed-length circular block bootstrap, not the random-length stationary bootstrap introduced by [Politis and Romano](https://users.ssc.wisc.edu/~behansen/718/Politis%20Romano.pdf).

**Repair:** define expected return units, propagate estimation uncertainty, test multiple block lengths and market regimes, report outcomes net of realistic fees/taxes, and use walk-forward probability calibration where data permit. Publish ranges and assumptions rather than an apparently precise probability of success.20,000 paths resample a small dataset; they do not create20,000 independent historical years.

## 4. Drawdown reporting misses what the investor experiences

`conv_port.py:23,27` computes drawdown on month-end values. Its reported worst fall is26.18%. Reconstructing the daily wealth path while **rebalancing at each month end to the same supplied weights** produces a **36.15% drawdown** on the same sample, retaining the original pre-IPO cash treatment. A daily constant-weight proxy gives35.94%; the monthly-rebalanced daily path is the relevant like-for-like correction. Neither is an unbiased prospective backtest because today's winners/weights were selected using later information.

The reconstructed peak was2020-02-20 and trough2020-03-23. Reconstructed month-end wealth matches the original code's month-end series to maximum absolute numerical error7.5e-14, confirming the same calendar-month rebalancing convention. This is a present-day-holdings retrospective replay with pre-IPO zero-return cash, not an actual historical portfolio.

For$50,000/$100,000,36.15% corresponds to about$18,075/$36,151 drawdown. This is materially above the user's15–20% tolerance. Five-year final profit and intraperiod capital loss are different outcomes: a profitable final result can include a very large earlier drawdown.

Do not treat a stop loss as a guaranteed drawdown cap; gaps, liquidity and correlated selloffs can bypass an intended level.

## 5. Backtest claims need relabelling

- Replaying current holdings with current weights through history (`conv_port.py`, `opt.py`) is a retrospective stress illustration, not an investable strategy backtest.
- `bt10.py:3` starts from current-universe price histories, so delisted/removed constituents are absent. Its factor signals are lagged for the following month (`:17–21`), which helps avoid simple contemporaneous signal leakage, but does not remove universe survivorship.
- `backtest3.py:5,12–15,19–21` uses currently retrieved statements, period-end dates and a fixed90-day lag. It does not establish original filing/publication timestamps or vintage data before restatements. Calling it point-in-time is too strong. It tests only three annual periods, and the conviction-specific saved output has no selected names in2023,28 in2024,34 in2025.
- `bt_conv.json` gives mean selected-name returns10.34% versus universe14.47% in2024, and6.99% versus17.91% in2025. Profit hit rates64.29% versus61.30%, and55.88% versus57.58%, do not demonstrate an advantage. Nor can two cohorts prove the universal assertion that no individual stock can ever have90% profit probability. Correct wording: this process has not established such a calibrated probability.
- Comparing surviving-universe stock returns with a different benchmark return convention can contaminate apparent alpha. Verify adjusted-price/dividend handling and use an investable total-return benchmark consistently. A generic58% haircut cannot mathematically repair survivorship or vintage-data leakage.

## 6. Improved mandate for weekly buy/hold/sell review

Separate refresh cadence from investment horizon. Weekly review does not validate one-week predictions or require weekly trades. Each candidate needs an explicit thesis horizon, expected catalyst, valuation case, invalidation conditions and position risk; short-term trades need a separate tested execution model. A single long-only equity method cannot be assumed valid interchangeably over a day, week, month and year.

For the user's15–20% portfolio drawdown tolerance, perform deterministic allocation stress budgets before security ranking. If the non-equity sleeve were unchanged during stress, equity weight times equity shock equals portfolio loss:

| Equity shock assumption | Maximum equity weight for15% portfolio loss | Maximum for20% loss |
|---|---:|---:|
|−40%|37.5%|50%|
|−50%|30%|40%|

These are arithmetic scenarios, **not recommended weights, calibrated probabilities or guarantees**. Non-equity assets can also lose value; the investor's existing assets, cash needs, liabilities, expenses, taxes and correlations must enter the budget. The14-stock portfolio plus S&P500 remains100% equity, so the index blend does not create a protective reserve.

Weekly decision rules should default to HOLD when no material thesis, valuation, concentration or risk-budget change occurs. BUY requires verified fresh data, sufficient valuation support and available risk budget. TRIM/SELL requires an evidence-based thesis break, excess risk or a materially better risk-adjusted use of capital, while documenting transaction costs and tax effects. Store dated decisions and freeze the methodology before forward evaluation so repeated model adjustments cannot manufacture a reassuring score.
