# Stocks-only risk challenge — 1 October 2026

**Status:** bounded independent research input, not a completed release or an order. **Exact completed parents read:** `v011_2026-09-27_claude`, `v012_2026-09-27_codex`, and `v013_2026-10-01_codex`. **Historical-price cutoff:** 30 September 2026 US completed session, while the covariance comparison ends 25 September to align with v011. The user has now specified **individual stocks only**; no Treasury, cash or ETF appears in the target weights below. SPY appears solely as an historical comparator and a sensitivity proxy for companies that did not trade in older crises.

## Decision judgment

The proposed 20-name, 100%-stock slate is investable in *form* but is not compatible with a 15–20% maximum tolerated drawdown if that earlier number was meant as a hard limit. Replaying current names through old crises produces a **−53.06% peak-to-trough GFC fall**, **−38.74% COVID fall**, and **−21.82% 2022 fall**. A cross-sector defensive candidate that substitutes PG, PEP and PEG for HIG, AMP and USB improves each of six archived crisis *episode* outcomes and lowers recent measured covariance risk, yet still shows roughly **−44%, −36% and −21%** worst falls in those three episodes. These are diagnostics from today's survivors, not forecast loss floors or odds.

The alternative should be a **candidate for fundamental re-underwriting, not an automatic buy**. The frozen v011 process called PG, PEP and PEG eligible but `INCLUDE-SMALL`; its scenario estimates are uncalibrated and their current owner cash, debt, valuation, growth and next catalysts must be checked before funding. The risk test alone cannot justify an expensive defensive stock.

## Exact weights and concentration

The input slate supplied by the portfolio lead is MSFT8, AMP6, NVDA4, ADP6, TJX6, RSG5, MA5, MCK6, STE5, BALL4, DOV5, BR4, AXP5, USB4, CRH5, PTC4, VEEV4, GDDY4, ALLE5, HIG5 (percent, total 100). The **defensive challenger keeps every other weight**, changing `HIG5 → PG5`, `AMP6 → PEP6`, and `USB4 → PEG4`. It has 20 individual stocks and sums to exactly 100%; the comparison is a substitution, not a 21st–23rd addition.

| Concentration | Input slate | Defensive challenger | Frozen v011 |
|---|---:|---:|---:|
| Largest name / top five | 8% / 32% | 8% / 32% | 8.32% / 32.92% |
| Effective name count from weight HHI | 19.23 | 19.23 | 18.87 |
| Financials / Industrials / Technology | 25% / 25% / 20% | 10% / 25% / 20% | 25% / 21.71% / 6.75% |
| Consumer staples / Utilities | 0% / 0% | 11% / 4% | 0% / 8.32% |
| Number of represented GICS sectors | 6 | 8 | 7 |

The input slate's 50% Financials-plus-Industrials position is an economic concentration despite 20 tickers and 19.23 effective names by weight. The challenger reduces that share to 35%; it still has a 25% industrial sector position and lacks Energy, Communication Services and Real Estate. Sector labels follow the archived v011 classification. Relative to the archived S&P proxy sectors, the input slate is approximately +12 percentage points Financials, +17 Industrials and −14 Technology; that active exposure may dominate stock-specific thesis quality.

## Six archived shocks at current weights

Yahoo daily adjusted prices were retrieved for all 20 target tickers, all 20 v011 names, the five tested defensive names, and SPY. Prices were identity-checked for ticker/USD and raw responses SHA-256 hashed. The same deterministic procedure buys today's named survivors at each episode start, rebalances to target weights at each new calendar quarter, and records total-return-adjusted end value and worst intra-episode drawdown. A name without quotes at both episode endpoints is **omitted with remaining weights renormalized**; GDDY, VEEV and ALLE together are 13% of both input/challenger weights in 2007 and 2011. The separate `missing_as_spy_sensitivity` preserves that 13% with a market proxy; it is not a recommended ETF allocation. Gross adjusted prices omit the actual investor's dividend withholding, dealing/FX fees and tax.

| Historical episode | Input 20 end return | Defensive challenger end return | Frozen v011 rerun on same Yahoo feed | SPY same feed |
|---|---:|---:|---:|---:|
| 2007–09 GFC | −52.37% | **−41.81%** | −47.59% | −55.19% |
| 2011 downgrade/euro crisis | −20.74% | **−16.25%** | −17.76% | −18.37% |
| 2015–16 China sell-off | −11.73% | **−7.37%** | −10.38% | −13.02% |
| Q4 2018 rate scare | −21.49% | **−18.03%** | −18.55% | −19.35% |
| 2020 COVID | −38.74% | **−35.51%** | −37.77% | −33.72% |
| 2022 inflation bear | −21.23% | **−20.80%** | −17.33% | −24.50% |

Worst **within-episode** path declines for input/challenger respectively are GFC **−53.06%/−44.08%**, COVID **−38.74%/−35.51%**, and 2022 **−21.82%/−21.03%**. If the missing GFC 13% is filled with a historical SPY *proxy* instead of renormalizing, input/challenger episode returns are **−52.74%/−43.70%**, leaving the conclusion unchanged. The v011 rerun differs from its immutable published episode figures by at most **0.34 percentage point** across six episodes, a useful replication check but not an independent fundamental audit. At $50,000, a −44.08% mark-to-market fall is about **$22,040**; at $100,000 about **$44,080**. The path can be worse in a different future crisis.

The substitutions were a small, disclosed challenge set, **not** a search across all eligible companies. Single replacements show mixed results: HIG5→PG5 improves GFC from −52.37% to −46.56% and COVID to −37.51% but worsens 2022 from −21.23% to −21.94%; AMP6→PEP6 improves GFC to −48.78%, COVID to −37.16% and 2022 to −20.63%. Two swaps HIG/AMP→PG/PEP give −42.64% GFC, −35.92% COVID, −21.35% 2022. The third USB→PEG improves those to −41.81%, −35.51%, −20.80%. Such in-sample gains can disappear because correlations, macro drivers, business economics and entry valuations change.

## Recent covariance and what it cannot say

From **753 common adjusted-price daily returns, 25 September 2023–25 September 2026**, input/defensive/v011 portfolios have sample annualized volatility **14.33%/12.99%/13.56%** and beta to SPY **0.739/0.645/0.593**. The challenger's lower 12.99% recent volatility, lower mean pairwise correlation (0.226 vs input 0.270) and lower GFC replay make it a better **risk candidate** than the input slate. Its tracking error to SPY rises marginally from 9.65% to 10.05%; active risk is not eliminated. V011 beta was low (0.593) but its GFC decline still reached roughly 47%; beta is not a crisis-loss ceiling. The replacement names were selected with knowledge of past market stress and do not establish a future hedge.

The archived v011 20-name base-scenario average (13.04%) is **not a calibrated expected portfolio CAGR**. The current 20-name slate likewise has no uniform, after-tax, no-rerating owner-return estimate for all members. Frozen v011 scenario values for HIG, AMP, USB, PG, PEP and PEG are not comparable enough to plug into an optimizer, and v013 showed AMP's stronger 13.20% case falls to 7.77% under flat current normalized P/E. No probability of gain/outperformance or estimated alpha is claimed here. A risk-adjusted final decision requires the fresh company cash/valuation audit to test whether PG/PEP/PEG deserve their current purchase prices and what, if any, stocks replace HIG/AMP/USB. Do not swap simply because their historical prices look defensive.

These limitations are consistent with the [SEC's statement that diversification cannot guarantee protection in a market decline](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments). In a stock-only account, position sizing, balance-sheet quality and sector diversity can lower specific risks, but a historical replay does not make 15–20% a credible maximum loss.

**Reproducibility:** [`stress_test.py`](stress_test.py) and [`stress_diagnostics.json`](stress_diagnostics.json) reproduce the input slate and frozen v011 crisis comparison; [`defensive_swap_test.py`](defensive_swap_test.py) and [`defensive_swap_diagnostics.json`](defensive_swap_diagnostics.json) reproduce predeclared sector swaps and SPY-missing sensitivity; [`risk_profile.py`](risk_profile.py) and [`covariance_diagnostics.json`](covariance_diagnostics.json) derive recent covariance. Each raw Yahoo response is stored under [`raw_yahoo/`](raw_yahoo/) and SHA-256 logged in the diagnostics. The complete v011 source ZIP hash is included in `stress_diagnostics.json`. None of these files revises immutable parents or another workstream.
