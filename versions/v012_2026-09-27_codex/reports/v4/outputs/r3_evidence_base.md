# R3 Evidence Base — factor research, active-management base rates, stock-outcome base rates

**Agent:** R3 · **Built:** 2026-09-25T20:53:07Z · **Data cutoffs:** Kenneth French Data Library (CRSP vintage 202607, monthly through 2026-07);
SPIVA U.S. Year-End 2025 (pub. 2026-03-03) and Mid-Year 2026 (pub. 2026-09-17); Yahoo prices through 2026-09-25 (monthly analyses end 2026-08).
**Purpose:** give the pre-registered Q/V/M/S model an honest prior, and define what "confidence" can and cannot mean.
All long-short factor numbers are gross of costs, all-cap and value-weighted; numbers marked (biased) use survivorship-biased data and are upper bounds.

---

## 0. Answer first

1. **"90% confident" is a legitimate statement about diversified equity exposure over long horizons, not about beating the index.**
   - Since 1926 the US total market had a positive nominal return in **95.4%** of rolling 10-year windows and **99.5%** of 15-year windows.
   - In real terms the figures are 87.6% and 97.1%. At 1 year the market is positive only 75.5% of the time.
   - The US is the survivor case: across 39 developed markets, a diversified investor still had a **12%** chance of losing to inflation over 30 years (Anarkulova, Cederburg & O'Doherty 2022).
   - What is *not* attainable:
     - **A single stock:** it beats the market in about **44%** of stock-years and about **37%** of stock-decades (Bessembinder 2018). S&P 500 members beat the index in only **28% / 28% / 31%** of cases in 2023/2024/2025 (our point-in-time computation; S&P DJI reports 26% / 28% / 30%).
     - **A top-decile pick from a "very good" signal (IC 0.10)** gets to only **~57%**. A 90% single-stock hit rate would need IC ≈ **0.63**, versus the 0.05 "good" and 0.10 "very good" practitioner benchmarks.
     - **A 15–30 stock tilt:** at an IR of 0.14 (central case) to 0.4 (optimistic) it beats the S&P 500 over one year with only **56%–66%** probability, and over 10 years with **67%–90%**.
     - **Professional managers:** **86–93%** of US large-cap funds lagged the S&P 500 over 10–20 years (SPIVA YE2025).
2. **Realistic expectation for our 15–30 stock large-cap long-only Q+V+M+S tilt:**
   - **Central case:** gross alpha ≈ **+1%/yr** (plausible range 0 to +2%), before ~0.2–0.4%/yr trading costs.
   - **Tracking error** ≈ **6–9%**, so IR ≈ 0.1–0.3.
   - **Expect to lag the S&P 500 in ~40–45% of calendar years** and in ~20–40% of 5-year windows.
   - **The evidence behind this:**
     - Fama-French big-cap long-only mix, 1963–2026: **+1.9%** to **+2.3%/yr gross**, with TE 3.1%–4.3%, and negative in 26%–31% of years.
     - The same mix since 2010: only **+0.5%** to **+1.1%/yr** (t < 1).
     - Live large-cap factor ETFs, 2011/13/15–2026, net of fees, versus SPY: QUAL -0.5%; MTUM +1.0%; VLUE -0.7%; USMV -3.3%; LRGF -1.5%; GSLC -1.0% per year. An equal-weight QUAL+MTUM+VLUE mix returned +0.06%/yr.
3. **The long-short factors are real over the long run but have decayed.** Over 1963–2026 (all-cap, gross):
   - **Long-run premia:**
     - HML 3.6%/yr (t 2.8); RMW 3.1% (t 3.1).
     - CMA 3.0% (t 3.3); UMD 7.3% (t 4.0).
     - Equal-weight combo: **4.2%/yr, Sharpe 0.76**, positive in 79% of calendar years and 86% of 36-month windows.
   - **Since 2010:**
     - HML -0.4%, CMA 0.4%, RMW 2.2%, UMD 3.3%.
     - Combo 1.4%/yr (t 1.1).
   - **After publication:**
     - Our own check on French's data: value -57%, momentum -53%, profitability -15%, investment -108%.
     - This matches the McLean & Pontiff (2016) average of −58%.
4. **A large-cap long-only implementation captures only ~45–54%** of the all-cap long-short combo premium (1963–2026).
   - By factor, the capture is: value 67–74%, profitability 31–35%, investment 55–73% and momentum 35–45%.
5. **Haircut rule for any backtest we produce:**
   - Keep ≤ **40%** of in-sample alpha from published-factor backtests.
   - Multiply by ~**0.45** again if the backtest was long-short and all-cap.
   - Subtract costs.
   - Demand **t ≥ 3** (Harvey, Liu & Zhu 2016) before believing anything new. A 10-year backtest with Sharpe 0.5 has t ≈ 1.6, which is statistically empty once ≥10 variants were tried.
   - The v3 model tuned on 3 annual backtest points carries **no** statistical information.
6. **The legacy price file is badly biased.**
   - Equal-weighting today's S&P 500 members (`close10.pkl`) earned **18.1%/yr** over 2015-10-31..2026-08-31, versus **12.4%/yr** for the investable equal-weight S&P 500 (RSP). That is a survivorship/look-ahead bias of **≈5.7%/yr**.
   - Its stock closes are also dividend-adjusted while `^GSPC` is price-only. That inflates naive "beat the index" rates by 3–9 points.
   - v4 backtests must use point-in-time membership with delisting returns, and a total-return benchmark.
7. **Low volatility belongs as a constraint, not a return driver** (consistent with the pre-registration).
   - The large-cap low-variance and low-beta quintiles had active returns of -1.0% and -0.6%/yr versus their universe in 1963–2026, and -3.2% and -3.3%/yr since 2010.
   - Their beta-adjusted alpha was positive but insignificant (+1.3%, +1.4%; t ≈ 1.5).
8. **Evidence strength for the model's families:**
   - **Strongest for large caps:** momentum (in the long run) and profitability/quality.
   - **Value and investment:** strong over 1963–2026 but flat since 2010.
   - **Low accruals and net repurchases:** respectable large-cap evidence (+1.9% and +1.5%/yr long-only active, 1963–2026).
   - **Earnings-surprise drift (SUE/PEAD):** largely gone in large caps after ~2006 (Martineau 2022), so the S family deserves the weakest prior.

---

## 1. Literature — what is well replicated and what decayed

| # | Paper (journal, year) | Sample | Key quantitative finding | Known decay / caveats | DOI / URL | Status |
|---|---|---|---|---|---|---|
| 1 | **Returns to Buying Winners and Selling Losers** — Jegadeesh & Titman (JF 48(1):65-91, 1993) | NYSE/AMEX, 1965-1989 | 6-month/6-month relative-strength strategy earns ~12.0%/yr compounded (~1%/month); 12m/3m best at 1.31%/month; cumulative gain peaks ~9.5% at month 12 and partly reverses (~4% by month 36). | Persisted in the 1990s (JT 2001, JF 56(2)). Our data: UMD 9.9%/yr in JT's sample vs 4.7%/yr after publication (-53%). Crash-prone (see Daniel & Moskowitz). | https://doi.org/10.1111/j.1540-6261.1993.tb04702.x | VERIFIED-SUB; decay = our data |
| 2 | **Value and Momentum Everywhere** — Asness, Moskowitz & Pedersen (JF 68(3):929-985, 2013) | 8 markets/asset classes, 1972-2011 (US: ~724 liquid large caps) | Value and momentum premia in every asset class; value-momentum correlation about -0.6 within stock markets; global 50/50 value+momentum combination Sharpe 1.45. | Standalone Sharpe ratios slightly lower in 1992-2011 than 1972-1991; gross of costs; value then suffered its 2007-2020 drawdown. | https://doi.org/10.1111/jofi.12021 | VERIFIED-SUB |
| 3 | **Momentum Crashes** — Daniel & Moskowitz (JFE 122(2):221-247, 2016) | US 1927-2013 + international equities and other asset classes | Crashes happen in 'panic' states (after market falls, high volatility) when markets rebound: Mar-May 2009 losers +163% vs winners +8%; Jul-Aug 1932 losers +232% vs winners +32%. Dynamic weighting roughly doubles alpha and Sharpe. | Constant-volatility scaling is an alternative fix (Barroso & Santa-Clara 2015, JFE 116(1)). Our data: UMD -49% in Mar-May 2009; worst drawdown -78% (1932-39). | https://doi.org/10.1016/j.jfineco.2015.12.002 | VERIFIED-SUB; our data |
| 4 | **The Cross-Section of Expected Stock Returns** — Fama & French (JF 47(2):427-465, 1992) | NYSE/AMEX/NASDAQ nonfinancials, 1963-1990 | Beta has no reliable relation to average returns; B/M decile returns rise from 0.30% to 1.83%/month (spread 1.53%/month); size and B/M absorb E/P and leverage effects. | Our data: HML 5.1%/yr in FF's sample vs 2.2%/yr after publication (-57%). Fama & French (2021, RAPS 11(1):105-121): value premium much lower in the second half of 1963-2019, but too volatile to reject equal expected premia. | https://doi.org/10.1111/j.1540-6261.1992.tb04398.x | VERIFIED-SUB; decay = our data |
| 5 | **Common Risk Factors in the Returns on Stocks and Bonds** — Fama & French (JFE 33(1):3-56, 1993) | US 1963-07 to 1991-12 | Three-factor model; HML 0.40%/month (t 2.91), SMB 0.27%/month (t 1.73). | Size premium weak since (our data: SMB +2.2%/yr, t 1.7, 1963-2026; -0.8%/yr since 2010). | https://doi.org/10.1016/0304-405X(93)90023-5 | VERIFIED-SUB |
| 6 | **A Five-Factor Asset Pricing Model** — Fama & French (JFE 116(1):1-22, 2015) | US 1963-07 to 2013-12 | Adds profitability (RMW) and investment (CMA); explains 71-94% of the cross-section variance of expected returns for test portfolios; HML redundant in this sample; HML only 0.21%/month (t 1.69) among big stocks vs 0.53% among small. | Our data after publication (2015-05 to 2026-07): RMW 2.7%/yr (t 1.1; -15% vs in-sample), CMA -0.3%/yr (-108%). | https://doi.org/10.1016/j.jfineco.2014.10.010 | VERIFIED-SUB; decay = our data |
| 7 | **The Other Side of Value: The Gross Profitability Premium** — Novy-Marx (JFE 108(1):1-28, 2013) | US nonfinancials 1963-07 to 2010-12 | Gross profits/assets predicts returns about as well as B/M: value-weighted quintile spread 0.31%/month (t 2.49), FF3 alpha 0.52%/month (t 4.49); correlation with value -0.57, so combining improves both. | Large caps alone: 0.26%/month (t 1.88), but large-cap profitability+value earns 0.62%/month (Sharpe 0.74). French's RMW uses operating, not gross, profitability. | https://doi.org/10.1016/j.jfineco.2013.01.003 | VERIFIED-SUB |
| 8 | **Quality Minus Junk** — Asness, Frazzini & Pedersen (Review of Accounting Studies 24(1):34-112, 2019) | US 1957-2016; 24 countries 1989-2016 (54,616 stocks) | Quality (profitable, growing, safe, well-managed) earns significant risk-adjusted returns: US QMJ alphas 39-60 bp/month (t 5.4-10.0), global 51-61 bp; quality stocks trade at only moderately higher prices. | Raw top-minus-bottom decile spread only 42-52 bp/month (t ~2.5); much of the alpha comes from QMJ's low/negative beta. Authors are AQR-affiliated. | https://doi.org/10.1007/s11142-018-9470-2 | VERIFIED-SUB |
| 9 | **Asset Growth and the Cross-Section of Stock Returns** — Cooper, Gulen & Schill (JF 63(4):1609-1651, 2008) | US nonfinancials 1968-2003 | Low-minus-high total asset growth decile: ~20%/yr equal-weighted raw (~26% vs 6%), ~13%/yr value-weighted raw, ~8.4%/yr value-weighted risk-adjusted; effect holds among large caps. | Now embedded in CMA/q-factor investment. Our data: CMA 5.5%/yr in CGS's sample vs 0.6%/yr after 2008 (-90%); -0.7%/yr since 2015. | https://doi.org/10.1111/j.1540-6261.2008.01370.x | PARTLY (numbers from SSRN WP/secondary; JF abstract verified) |
| 10 | **Share Issuance and Cross-sectional Returns** — Pontiff & Woodgate (JF 63(2):921-945, 2008) | US, post-1970 (with an earlier comparison period) | Post-1970, net share issuance predicts returns (negatively) more significantly than size, B/M or momentum; no significant predictive power in the earlier period for most horizons. Chen & Zimmermann replication 0.58%/month (t 4.9). | Holds internationally (McLean, Pontiff & Watanabe 2009, JFE 94(1)). Our data: big-cap net repurchasers +1.5%/yr active 1963-2026, only +0.1%/yr since 2010. | https://doi.org/10.1111/j.1540-6261.2008.01335.x | VERIFIED-SUB (start of pre-1970 period unverified) |
| 11 | **Market Reactions to Tangible and Intangible Information** — Daniel & Titman (JF 61(4):1605-1643, 2006) | US | B/M predicts returns because it proxies for the 'intangible' (non-fundamental) part of past returns; a composite equity-issuance measure independently forecasts returns negatively. | Numeric results not checked by R3. | https://doi.org/10.1111/j.1540-6261.2006.00884.x | VERIFIED-SUB (abstract level) |
| 12 | **Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about Future Earnings?** — Sloan (The Accounting Review 71(3):289-315, 1996) | 40,679 NYSE/AMEX firm-years, 1962-1991 | Accruals are less persistent than cash flows, but prices act as if investors fixate on earnings; a low-minus-high accrual hedge earns 10.4% size-adjusted in year 1 (t 4.7), positive in 28 of 30 years. | Green, Hand & Soliman (2011, Mgmt Sci 57(5):797-816): the hedge return decayed until it was no longer reliably positive. Our data: big-cap low-accrual quintile +1.9%/yr active 1963-2026, +2.4%/yr since 2010 (t 1.6). | https://doi.org/10.2308/tar-9608042309 | VERIFIED-SUB |
| 13 | **Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?** — Bernard & Thomas (JAR 27 (Suppl.):1-36, 1989) | NYSE/AMEX quarterly announcements, 1974-1986 | Prices keep drifting in the direction of the earnings surprise for ~60 trading days: extreme SUE deciles about +/-2% each (~4% long-short per quarter, ~18% annualized). | Chordia, Goyal, Sadka, Sadka & Shivakumar (2009, FAJ 65(4)): drift 0.04%/month in the most liquid stocks vs 2.43% in the least, and costs absorb 70-100% of paper profits. | https://doi.org/10.2307/2491062 | SECONDARY for numbers (paper behind JSTOR) |
| 14 | **Rest in Peace Post-Earnings Announcement Drift** — Martineau (Critical Finance Review 11(3-4):613-646, 2022) | US, recent decades | Earnings surprises are now fully priced on the announcement day: the drift has been insignificant for large stocks since ~2006 and more recently for microcaps too. | Text-based surprises still show drift (Meursault, Liang, Routledge & Scanlon 2023, JFQA 58(6):2299-2326: 1-yr drift 8.0% text-based vs 4.6% classic SUE in 2010-2019, working-paper figures). | https://doi.org/10.1561/104.00000122 | VERIFIED-SUB |
| 15 | **Betting Against Beta** — Frazzini & Pedersen (JFE 111(1):1-25, 2014) | US 1926-2012 + 19 international markets, Treasuries, credit, futures | Long leveraged low-beta / short high-beta (BAB) has US Sharpe 0.78 and FF3 alpha 0.73%/month (t 7.4); the security market line is flatter than CAPM predicts in 18 of 19 markets. | Novy-Marx & Velikov (2022, JFE 143(1):80-106): BAB's construction effectively equal-weights and loads on tiny stocks; its return is explained by profitability/investment tilts. Our data: big-cap low-beta quintile -0.6%/yr raw active (beta 0.70), CAPM alpha +1.4%/yr (t 1.7), 1963-2026. | https://doi.org/10.1016/j.jfineco.2013.10.005 | VERIFIED-SUB; our data |
| 16 | **The Cross-Section of Volatility and Expected Returns** — Ang, Hodrick, Xing & Zhang (JF 61(1):259-299, 2006) | US 1963-07 to 2000-12 | Stocks with high idiosyncratic volatility (relative to FF3) earn very low returns: top-minus-bottom quintile -1.06%/month (value-weighted). | Bali & Cakici (2008, JFQA 43(1):29-58): not robust to weighting, breakpoints, data frequency and size/price/liquidity screens. Our data: big-cap low-variance quintile -1.0%/yr raw active (beta 0.66), CAPM alpha +1.3%/yr (t 1.4), 1963-2026. | https://doi.org/10.1111/j.1540-6261.2006.00836.x | VERIFIED-SUB; our data |
| 17 | **Does Academic Research Destroy Stock Return Predictability?** — McLean & Pontiff (JF 71(1):5-32, 2016) | 97 published cross-sectional return predictors | Predictor portfolio returns are 26% lower out-of-sample (upper bound on data mining) and 58% lower after publication; 32% is attributed to publication-informed trading; bigger declines for predictors with higher in-sample returns. | Implies keeping ~40% of in-sample premia for published signals. Our French check: -53% (momentum), -57% (value). | https://doi.org/10.1111/jofi.12365 | VERIFIED-R3 (Crossref abstract) |
| 18 | **...and the Cross-Section of Expected Returns** — Harvey, Liu & Zhu (RFS 29(1):5-68, 2016) | 316 factors from 313 papers | Once you account for how many factors have been tried, a newly proposed factor needs t > 3.0; most claimed research findings in financial economics are likely false. | Companion Harvey & Liu (2015, JPM 42(1):13-28): the Sharpe-ratio haircut is nonlinear; the 50% rule of thumb is too lenient below Sharpe 0.4 and too harsh above 1.0. | https://doi.org/10.1093/rfs/hhv059 | VERIFIED-SUB; HL(2015) VERIFIED-R3 |
| 19 | **Replicating Anomalies** — Hou, Xue & Zhang (RFS 33(5):2019-2133, 2020) | 452 anomalies, US | With microcaps mitigated (NYSE breakpoints, value-weighted returns), 65% fail |t| >= 1.96 (including 96% of the trading-frictions category) and 82% fail t >= 2.78; replicated anomalies are much smaller than originally reported. | Supports a large-cap, value-weighted implementation of only the robust families, with shrunken premia. | https://doi.org/10.1093/rfs/hhy131 | VERIFIED-R3 (Crossref abstract) |
| 20 | **Is There a Replication Crisis in Finance?** — Jensen, Kelly & Pedersen (JF 78(5):2465-2518, 2023) | 153 factors, 93 countries | With a Bayesian framework, most factors replicate (82.4% in the US), cluster into 13 themes, work out-of-sample internationally, and their evidence is strengthened (not weakened) by the large number of factors. | Average alpha 0.49%/month in-sample vs 0.26% after the original samples (-47%): decay, not disappearance. | https://doi.org/10.1111/jofi.13249 | VERIFIED-R3 (abstract); 82.4% and alpha figures VERIFIED-SUB |
| 21 | **Open Source Cross-Sectional Asset Pricing** — Chen & Zimmermann (Critical Finance Review 11(2):207-264, 2022) | 319 characteristics | 98% of the 161 clearly significant predictors reproduce with t > 1.96; reproduced vs original t-stats slope 0.88. | Reproduction is in-sample; it says nothing about post-publication returns. | https://doi.org/10.1561/104.00000112 | VERIFIED-SUB |
| 22 | **How Do Factor Premia Vary Over Time? A Century of Evidence** — Ilmanen, Israel, Lee, Moskowitz & Thapar (Journal of Investment Management 19(4), 2021) | Value, momentum, carry, defensive across 6 asset classes, ~1926-2020 | Pooled t-stats 5.1 (value) to >6.6 (defensive); multifactor Sharpe 1.46; out-of-sample Sharpe 49% below original-sample for value but only 18% lower for the multifactor combination; little evidence of arbitrage-driven decay. | AQR authors; the long-short, multi-asset setting differs from large-cap long-only equities. | https://doi.org/10.2139/ssrn.3400998 | VERIFIED-SUB (forthcoming draft) |
| 23 | **Is (Systematic) Value Investing Dead?** — Israel, Laursen & Richardson (JPM 47(2):38-62, 2021) | US equities, focus on the 2018-2020 value drawdown | Value's recent underperformance came mainly from a widening gap between prices and fundamentals (valuation spreads), not from value's fundamentals failing. | Decomposition numbers not checked. | https://doi.org/10.3905/jpm.2020.1.194 | VERIFIED-SUB (abstract level) |
| 24 | **Reports of Value's Death May Be Greatly Exaggerated** — Arnott, Harvey, Kalesnik & Linnainmaa (FAJ 77(1):44-67, 2021) | US, value 2007-2020 | HML fell ~55% from 2007 to mid-2020; the change in relative valuations explains the entire drawdown; capitalising intangibles improves value. | Our data: HML -57.8% peak-to-trough (2006-12 to 2020-09), then +68.5% from 2020-10 to 2022-12. | https://doi.org/10.1080/0015198X.2020.1842704 | VERIFIED-SUB; our data |
| 25 | **The Role of Shorting, Firm Size, and Time on Market Anomalies** — Israel & Moskowitz (JFE 108(2):275-301, 2013) | 86 years US + ~40 years international equities and asset classes | The long side supplies ~60% of value and ~half of momentum profits (almost all of size); the value premium falls with firm size and is weak among the largest stocks; momentum has no reliable size relation; variation over time looks like chance. | Consistent with our large-cap long-only capture of ~45-54% of the all-cap combo premium. | https://doi.org/10.1016/j.jfineco.2012.11.005 | VERIFIED-SUB |
| 26 | **When Equity Factors Drop Their Shorts** — Blitz, Baltussen & van Vliet (FAJ 76(4):73-99, 2020) | US and international equities | Both legs carry premia, but most added value comes from the long legs, and the shorts are largely subsumed by the longs, in large and small caps alike. | Magnitudes not checked. | https://doi.org/10.1080/0015198X.2020.1779560 | VERIFIED-SUB (abstract level) |
| 27 | **A Taxonomy of Anomalies and Their Trading Costs** — Novy-Marx & Velikov (RFS 29(1):104-147, 2016) | US anomalies | Most anomalies with <50% monthly turnover keep significant net spreads with cost mitigation (buy/hold spreads); few high-turnover ones do; size, value and profitability have the largest capacity. | Institutional live-trade costs are much lower (Frazzini, Israel & Moskowitz 2018 WP 'Trading Costs', SSRN 3229719); a small investor's costs sit between the two. | https://doi.org/10.1093/rfs/hhv063 | VERIFIED-SUB |
| 28 | **Long-Only Style Investing: Don't Just Mix, Integrate** — Fitzgibbons, Friedman, Pomorski & Serban (Journal of Investing 26(4):153-164, 2017) | Long-only style portfolios | Integrating styles in a single portfolio beats a mix of stand-alone style sleeves (higher return and IR) by avoiding stocks with offsetting exposures. | AQR authors. | https://www.aqr.com/Insights/Research/White-Papers/Long-Only-Style-Investing | VERIFIED-R3 (abstract via journal/AQR pages) |
| 29 | **Stocks for the Long Run? Evidence from a Broad Sample of Developed Markets** — Anarkulova, Cederburg & O'Doherty (JFE 143(1):409-433, 2022) | 39 developed markets, 1841-2019 (bootstrap) | A diversified investor with a 30-year horizon has a 12% chance of losing to inflation. | Counterweight to US-only 'stocks always win over 20 years' evidence. | https://doi.org/10.1016/j.jfineco.2021.06.040 | VERIFIED-R3 (abstract) |

**What this literature implies for us:**
- **Replication.** The core families replicate: value, momentum, profitability/quality, investment and issuance. Jensen, Kelly & Pedersen (2023) find most published factors replicate out of sample and internationally. Hou, Xue & Zhang (2020) find that 65% of 452 anomalies fail even with microcaps mitigated, and that the survivors are smaller than originally reported. Hence we use only the robust families, and shrink their premia.
- **Magnitude.** The *size* of the premia has fallen after publication (McLean & Pontiff 2016). Value had a historic 2007–2020 drawdown, steepest in 2017–2020 (Israel, Laursen & Richardson 2021; Arnott et al. 2021).
- **Where to expect them.** Premia are weaker in large caps (Israel & Moskowitz 2013) and after costs (Novy-Marx & Velikov 2016).
- **Implementation.** Integrating styles in one ranking beats mixing separate style sleeves (Fitzgibbons, Friedman, Pomorski & Serban 2017, *Journal of Investing* 26(4):153–164; [AQR](https://www.aqr.com/Insights/Research/White-Papers/Long-Only-Style-Investing)). That supports the pre-registered composite rank.

---

## 2. Long-sample factor evidence (Kenneth French Data Library; our computation)

Source files: [F-F_Research_Data_5_Factors_2x3](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip),
[F-F_Momentum_Factor](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip) and
[F-F_Research_Data_Factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip)
(CRSP vintage 202607, downloaded 2026-09-25 UTC). The data are in `v4/data/r3_ff_factors_monthly.parquet`.

**Conventions:**
- Returns are monthly and in decimals, compounded where stated.
- Sharpe = mean / vol, because the factors are zero-cost long-short portfolios.
- t = mean / (sd / √n).
- Rolling windows overlap, so their effective sample is small.

### 2.1 Long-short factors, 1963-07 → 2026-07
| Factor | Ann. mean | Vol | Sharpe | t-stat | Max drawdown (peak→trough) | % roll-12m > 0 | % roll-36m > 0 | % cal. yrs > 0 | Worst 12m |
|---|---|---|---|---|---|---|---|---|---|
| HML (value) | 3.6% | 10.3% | 0.35 | 2.77 | -57.8% (2006-12→2020-09) | 61% | 67% | 56% (n=62) | -35.2% |
| RMW (profitability) | 3.1% | 7.9% | 0.39 | 3.10 | -41.8% (1998-08→2000-02) | 68% | 79% | 68% (n=62) | -37.7% |
| CMA (conservative investment) | 3.0% | 7.2% | 0.41 | 3.27 | -27.6% (2022-12→2025-10) | 59% | 67% | 53% (n=62) | -16.1% |
| UMD (momentum) | 7.3% | 14.6% | 0.50 | 3.96 | -57.8% (2008-11→2009-09) | 75% | 85% | 71% (n=62) | -56.5% |
| EW combo HML+RMW+CMA+UMD | 4.2% | 5.6% | 0.76 | 6.00 | -21.8% (2008-11→2020-12) | 80% | 86% | 79% (n=62) | -17.7% |
| Mkt-RF (equity premium, ref.) | 7.2% | 15.5% | 0.47 | 3.70 | -55.8% (1968-11→1974-09) | 73% | 80% | 73% (n=62) | -45.8% |
| SMB (size, ref.) | 2.2% | 10.5% | 0.21 | 1.71 | -56.4% (1983-07→1999-03) | 53% | 52% | 52% (n=62) | -29.3% |

### 2.2 Since 2010-01
| Factor | Ann. mean | Vol | Sharpe | t-stat | Max drawdown (peak→trough) | % roll-12m > 0 | % roll-36m > 0 | % cal. yrs > 0 | Worst 12m |
|---|---|---|---|---|---|---|---|---|---|
| HML (value) | -0.4% | 11.2% | -0.03 | -0.13 | -53.4% (2010-04→2020-09) | 46% | 38% | 38% (n=16) | -35.2% |
| RMW (profitability) | 2.2% | 7.7% | 0.28 | 1.14 | -25.9% (2023-10→2026-06) | 66% | 80% | 62% (n=16) | -20.6% |
| CMA (conservative investment) | 0.4% | 7.4% | 0.06 | 0.23 | -27.6% (2022-12→2025-10) | 41% | 39% | 38% (n=16) | -16.1% |
| UMD (momentum) | 3.3% | 12.7% | 0.26 | 1.07 | -25.4% (2020-09→2021-03) | 65% | 72% | 56% (n=16) | -22.0% |
| EW combo HML+RMW+CMA+UMD | 1.4% | 5.2% | 0.27 | 1.08 | -16.7% (2016-12→2020-12) | 57% | 63% | 56% (n=16) | -10.9% |
| Mkt-RF (equity premium, ref.) | 13.0% | 14.9% | 0.87 | 3.55 | -25.3% (2021-12→2022-09) | 86% | 100% | 88% (n=16) | -21.0% |
| SMB (size, ref.) | -0.8% | 9.3% | -0.09 | -0.36 | -35.3% (2014-02→2025-07) | 35% | 27% | 25% (n=16) | -17.0% |

### 2.3 Since 2015-01
| Factor | Ann. mean | Vol | Sharpe | t-stat | Max drawdown (peak→trough) | % roll-12m > 0 | % roll-36m > 0 | % cal. yrs > 0 | Worst 12m |
|---|---|---|---|---|---|---|---|---|---|
| HML (value) | -0.3% | 12.8% | -0.02 | -0.07 | -51.4% (2016-12→2020-09) | 49% | 36% | 36% (n=11) | -35.2% |
| RMW (profitability) | 2.7% | 8.5% | 0.32 | 1.08 | -25.9% (2023-10→2026-06) | 72% | 88% | 73% (n=11) | -20.6% |
| CMA (conservative investment) | -0.7% | 8.3% | -0.09 | -0.29 | -27.6% (2022-12→2025-10) | 37% | 34% | 27% (n=11) | -16.1% |
| UMD (momentum) | 3.0% | 14.2% | 0.21 | 0.73 | -25.4% (2020-09→2021-03) | 59% | 60% | 45% (n=11) | -22.0% |
| EW combo HML+RMW+CMA+UMD | 1.2% | 5.8% | 0.20 | 0.69 | -16.7% (2016-12→2020-12) | 49% | 51% | 45% (n=11) | -10.9% |
| Mkt-RF (equity premium, ref.) | 12.0% | 15.5% | 0.77 | 2.62 | -25.3% (2021-12→2022-09) | 80% | 100% | 82% (n=11) | -21.0% |
| SMB (size, ref.) | -1.8% | 10.1% | -0.18 | -0.61 | -32.7% (2018-06→2025-07) | 31% | 27% | 18% (n=11) | -17.0% |

### 2.4 Full history (momentum and value from 1926/27)
| Series | Window | Ann. mean | Sharpe | t | Max drawdown | Worst 12m |
|---|---|---|---|---|---|---|
| HML (value, FF3 file) | 1926-07..2026-07 | 4.3% | 0.35 | 3.46 | -57.8% (2006-12→2020-09) | -39.7% |
| UMD (momentum) | 1927-01..2026-07 | 7.4% | 0.46 | 4.55 | -78.4% (1932-06→1939-09) | -75.7% |
| Mkt-RF (FF3 file) | 1926-07..2026-07 | 8.3% | 0.45 | 4.54 | -84.6% (1929-08→1932-06) | -66.2% |

**Reading the tables:**
- **Combining helps.** The equal-weight combo roughly halves volatility thanks to the low or negative correlations: value–momentum ≈ −0.2 to −0.3, and profitability is roughly uncorrelated with the others (see `r3_factor_corr.csv`).
- **But the combo can still be underwater for 12 years.** Its drawdown ran from 2008-11 to 2020-12: the 2009 momentum crash, then value's lost decade.
- **Momentum crashes are real.** UMD's peak-to-trough drawdown was -57.8% (2008-11→2009-09), including −49% in March–May 2009 alone. Its worst drawdown since 1927 is −78% (1932–39); see Daniel & Moskowitz (2016).
- **2026 so far (through July):** UMD +10.2%, HML +12.3%, CMA +7.2%, RMW −5.8%. RMW's drawdown from 2023-10 reached −25.9% in 2026-06.

### 2.5 Publication-decay check on French's own factors (McLean–Pontiff style)
| Factor (French definition) / original paper & sample | In-sample mean (t) | After sample end (t) | After publication (t), months | Change vs in-sample |
|---|---|---|---|---|
| Fama & French (1992, JF) value; sample 1963-07..1990-12 | 5.1% (3.02) | 2.4% (1.28) | 2.2% (1.12), 409 | -57% |
| Jegadeesh & Titman (1993, JF) momentum; sample 1965..1989 | 9.9% (4.01) | 5.5% (2.06) | 4.7% (1.63), 400 | -53% |
| Fama & French (2015, JFE) RMW; sample 1963-07..2013-12 | 3.2% (2.94) | 2.6% (1.08) | 2.7% (1.06), 135 | -15% |
| Fama & French (2015, JFE) CMA; sample 1963-07..2013-12 | 3.9% (3.99) | -0.8% (-0.35) | -0.3% (-0.13), 135 | -108% |
| Cooper, Gulen & Schill (2008, JF) asset growth; sample 1968..2003 | 5.5% (4.45) | -0.0% (-0.00) | 0.6% (0.33), 215 | -90% |

The French definitions are not identical to each paper's original variable; for example, RMW is operating profitability, not Novy-Marx's gross profitability. Post-publication windows are short, so their t-stats are low. The direction matches McLean & Pontiff: value and momentum kept roughly 45% of their in-sample premia, and investment kept roughly none.

### 2.6 How much does a LARGE-CAP LONG-ONLY tilt capture?

**Method:**
- **Portfolios.** We use French's size × characteristic portfolios, value-weighted within each portfolio.
  - "2x3" means big stocks (above the NYSE median market cap) in the top 30% of the characteristic.
  - "5x5" means the top NYSE size quintile and the extreme characteristic quintile (recently 9–100 stocks, closer to a concentrated portfolio).
- **Active return.** Favoured portfolio minus the value-weighted return of all big-cap portfolios in the same sort. We reconstructed the universe weights from French's firm counts × average caps. Same-month weights match the CRSP market with 0.5–0.7%/yr TE, versus 0.7–1.0% for lagged weights.
- **Capture.** Mean long-only active return ÷ mean of the published all-cap long-short factor.

**1963-07 → 2026-07 (gross):**
| Large-cap long-only tilt | Stocks in favoured pf (latest / median since 2010) | Active return vs big-cap universe | TE | IR | t | Beta | CAPM alpha (t) | % cal. yrs > 0 | % roll-60m > 0 | Max relative DD | Capture vs all-cap L/S factor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Value (high B/M) [2x3] | 110 / 143 | +2.40% | 8.9% | 0.27 | 2.15 | 1.00 | +2.41% (2.14) | 55% | 68% | -50.6% | 67% |
| Profitability (high OP) [2x3] | 292 / 315 | +1.07% | 3.2% | 0.34 | 2.68 | 0.98 | +1.18% (2.96) | 65% | 78% | -14.0% | 35% |
| Conservative investment (low asset growth) [2x3] | 179 / 196 | +1.64% | 5.5% | 0.30 | 2.39 | 0.94 | +2.10% (3.07) | 60% | 70% | -23.8% | 55% |
| Momentum (high 12-2 return) [2x3] | 318 / 318 | +2.54% | 6.7% | 0.38 | 3.02 | 1.02 | +2.42% (2.85) | 63% | 77% | -23.3% | 35% |
| Value (top B/M quintile) [5x5] | 9 / 28 | +2.66% | 12.6% | 0.21 | 1.68 | 1.03 | +2.42% (1.51) | 56% | 63% | -61.0% | 74% |
| Profitability (top OP quintile) [5x5] | 101 / 94 | +0.94% | 4.2% | 0.23 | 1.79 | 0.98 | +1.08% (2.04) | 58% | 65% | -18.9% | 31% |
| Conservative investment (bottom INV quintile) [5x5] | 30 / 39 | +2.17% | 7.9% | 0.27 | 2.17 | 0.95 | +2.52% (2.51) | 61% | 72% | -32.9% | 73% |
| Momentum (top 12-2 quintile) [5x5] | 80 / 74 | +3.27% | 9.0% | 0.36 | 2.87 | 1.06 | +2.88% (2.52) | 58% | 79% | -25.8% | 45% |
| Low accruals (bottom AC quintile) [5x5] | 50 / 48 | +1.93% | 6.7% | 0.29 | 2.28 | 1.10 | +1.24% (1.48) | 65% | 73% | -27.6% | n/a |
| Net repurchasers (negative net issuance) [5x5] | 198 / 201 | +1.53% | 4.4% | 0.35 | 2.75 | 0.93 | +1.97% (3.61) | 58% | 74% | -14.8% | n/a |
| Low variance (bottom 60d VAR quintile) [5x5] | 52 / 58 | -1.04% | 8.5% | -0.12 | -0.97 | 0.66 | +1.26% (1.44) | 47% | 45% | -62.9% | n/a |
| Low beta (bottom 60m beta quintile) [5x5] | 83 / 93 | -0.64% | 8.2% | -0.08 | -0.62 | 0.70 | +1.44% (1.65) | 47% | 44% | -67.9% | n/a |
| EW mix: value+profitability+investment+momentum (2x3) | mix | +1.91% | 3.1% | 0.62 | 4.92 | 0.98 | +2.03% (5.20) | 74% | 84% | -10.9% | 45% |
| EW mix: value+profitability+investment+momentum (5x5) | mix | +2.26% | 4.3% | 0.52 | 4.13 | 1.00 | +2.24% (4.06) | 69% | 88% | -12.9% | 54% |

**Since 2010-01 (mixes and key tilts):**
| Large-cap long-only tilt | Stocks in favoured pf (latest / median since 2010) | Active return vs big-cap universe | TE | IR | t | Beta | CAPM alpha (t) | % cal. yrs > 0 | % roll-60m > 0 | Max relative DD | Capture vs all-cap L/S factor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Value (high B/M) [2x3] | 110 / 143 | +0.56% | 10.5% | 0.05 | 0.22 | 1.12 | -0.98% (-0.37) | 38% | 28% | -42.7% | n/m (short window) |
| Profitability (high OP) [2x3] | 292 / 315 | +0.96% | 3.0% | 0.32 | 1.32 | 0.97 | +1.37% (1.85) | 69% | 88% | -7.2% | n/m (short window) |
| Conservative investment (low asset growth) [2x3] | 179 / 196 | +0.53% | 5.9% | 0.09 | 0.36 | 0.91 | +1.69% (1.15) | 44% | 55% | -21.6% | n/m (short window) |
| Momentum (high 12-2 return) [2x3] | 318 / 318 | +0.13% | 6.0% | 0.02 | 0.09 | 1.02 | -0.11% (-0.07) | 50% | 31% | -17.7% | n/m (short window) |
| Low accruals (bottom AC quintile) [5x5] | 50 / 48 | +2.36% | 5.9% | 0.40 | 1.64 | 1.01 | +2.20% (1.47) | 56% | 69% | -15.9% | n/a |
| Low variance (bottom 60d VAR quintile) [5x5] | 52 / 58 | -3.15% | 9.8% | -0.32 | -1.31 | 0.60 | +2.13% (1.06) | 25% | 29% | -53.2% | n/a |
| EW mix: value+profitability+investment+momentum (2x3) | mix | +0.54% | 3.0% | 0.18 | 0.73 | 1.00 | +0.49% (0.64) | 44% | 54% | -8.7% | n/m (short window) |
| EW mix: value+profitability+investment+momentum (5x5) | mix | +1.07% | 4.5% | 0.24 | 0.98 | 1.06 | +0.31% (0.27) | 56% | 59% | -10.9% | n/m (short window) |

**Since 2015-01 (mixes and key tilts):**
| Large-cap long-only tilt | Stocks in favoured pf (latest / median since 2010) | Active return vs big-cap universe | TE | IR | t | Beta | CAPM alpha (t) | % cal. yrs > 0 | % roll-60m > 0 | Max relative DD | Capture vs all-cap L/S factor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Value (high B/M) [2x3] | 110 / 143 | +1.26% | 11.9% | 0.11 | 0.36 | 1.10 | +0.06% (0.02) | 36% | 28% | -38.9% | n/m (short window) |
| Profitability (high OP) [2x3] | 292 / 315 | +1.45% | 3.2% | 0.46 | 1.55 | 0.98 | +1.74% (1.83) | 82% | 100% | -6.2% | n/m (short window) |
| Conservative investment (low asset growth) [2x3] | 179 / 196 | +0.41% | 6.8% | 0.06 | 0.21 | 0.89 | +1.76% (0.89) | 36% | 54% | -21.6% | n/m (short window) |
| Momentum (high 12-2 return) [2x3] | 318 / 318 | -0.25% | 6.3% | -0.04 | -0.13 | 0.99 | -0.15% (-0.08) | 55% | 12% | -17.6% | n/m (short window) |
| Low accruals (bottom AC quintile) [5x5] | 50 / 48 | +3.13% | 6.3% | 0.50 | 1.70 | 1.02 | +2.83% (1.49) | 55% | 74% | -15.9% | n/a |
| Low variance (bottom 60d VAR quintile) [5x5] | 52 / 58 | -4.45% | 10.4% | -0.43 | -1.45 | 0.61 | +0.45% (0.17) | 27% | 31% | -52.5% | n/a |
| EW mix: value+profitability+investment+momentum (2x3) | mix | +0.72% | 3.4% | 0.21 | 0.72 | 0.99 | +0.86% (0.83) | 36% | 59% | -8.7% | n/m (short window) |
| EW mix: value+profitability+investment+momentum (5x5) | mix | +1.17% | 4.9% | 0.24 | 0.81 | 1.03 | +0.78% (0.53) | 45% | 61% | -10.9% | n/m (short window) |

**Interpretation:**
- **Capture.** Large-cap long-only captured about **45% (broad 2x3) to 54% (concentrated 5x5)** of the all-cap long-short combo premium over 1963–2026, with TE only 3–4%.
- **The published source agrees.** Israel & Moskowitz (2013) find that the long side supplies ~60% of value's and ~half of momentum's profits, and that the value premium shrinks with firm size while momentum shows no reliable size relation. In our data, profitability's capture is lowest because much of RMW comes from shorting small weak firms.
- **Since 2010 the mixes earned only +0.5% to +1.2%/yr gross.**
- **The mixes above are "mixes" of separately sorted portfolios.** An integrated composite should do somewhat better (Fitzgibbons et al. 2017).

### 2.7 Realized, net-of-fee evidence: live large-cap factor ETFs vs SPY (our computation from Yahoo adjusted closes)
| Fund | Period (month-ends) | Fund ann. | SPY ann. | Active (geometric) | TE | IR | % calendar yrs beating SPY | % rolling 36m beating | Max relative DD |
|---|---|---|---|---|---|---|---|---|---|
| QUAL – iShares MSCI USA Quality Factor | 2013-08..2026-08 | 13.7% | 14.2% | -0.50% | 2.9% | -0.14 | 33% (n=12) | 35% | -12.6% |
| MTUM – iShares MSCI USA Momentum Factor | 2013-05..2026-08 | 15.4% | 14.4% | +1.01% | 8.8% | 0.14 | 58% (n=12) | 58% | -28.7% |
| VLUE – iShares MSCI USA Value Factor | 2013-05..2026-08 | 13.7% | 14.4% | -0.72% | 8.7% | -0.01 | 33% (n=12) | 6% | -40.6% |
| USMV – iShares MSCI USA Min Vol Factor | 2011-11..2026-08 | 11.7% | 15.0% | -3.28% | 7.1% | -0.46 | 29% (n=14) | 23% | -45.4% |
| LRGF – iShares U.S. Equity Factor (multifactor) | 2015-05..2026-08 | 12.5% | 14.1% | -1.54% | 3.0% | -0.45 | 30% (n=10) | 33% | -20.9% |
| GSLC – Goldman Sachs ActiveBeta U.S. Large Cap (multifactor) | 2015-10..2026-08 | 14.4% | 15.4% | -1.00% | 1.4% | -0.65 | 30% (n=10) | 16% | -10.1% |
| MIX(QUAL,MTUM,VLUE) – EW monthly-rebalanced mix of quality, momentum, value ETFs | 2013-08..2026-08 | 14.2% | 14.2% | +0.06% | 4.2% | 0.04 | 33% (n=12) | 39% | -19.0% |
| RSP – Invesco S&P 500 Equal Weight (real EW benchmark, reference) | 2015-10..2026-08 | 12.4% | 15.4% | -3.01% | 5.8% | -0.43 | 30% (n=10) | 14% | -28.4% |

This is genuinely out-of-sample, investable and post-publication evidence. Over roughly 11–15 years the products delivered between **-3.3% and +1.0%/yr** versus SPY, and beat it in only 29–58% of calendar years. The period (2013–2026) was dominated by mega-cap growth leadership, which hurt value, low-volatility and equal-weight approaches. RSP (equal-weight S&P 500) lagged SPY by 3.0%/yr. It is one regime, not the long-run expectation, but it is exactly the kind of decade that makes "90% confident" claims about beating the index untenable.

### 2.8 US total market: probability of positive outcomes by horizon (1926-07 → 2026-07; French Mkt, FRED CPI-U)
| Horizon | # overlapping windows | P(nominal > 0) | P(beat T-bills) | P(real > 0) | Worst cumulative nominal | Worst cumulative real | Median annualized nominal |
|---|---|---|---|---|---|---|---|
| 1 yr | 1190 | 75.5% | 70.7% | 70.5% | -65.7% | -62.0% | 13.9% |
| 3 yr | 1166 | 84.6% | 79.2% | 78.6% | -81.4% | -76.6% | 11.8% |
| 5 yr | 1142 | 88.5% | 79.8% | 79.7% | -66.0% | -56.8% | 11.6% |
| 10 yr | 1082 | 95.4% | 86.5% | 87.6% | -42.7% | -40.0% | 11.2% |
| 15 yr | 1022 | 99.5% | 96.0% | 97.1% | -6.2% | -24.8% | 10.8% |
| 20 yr | 962 | 100.0% | 100.0% | 100.0% | 43.3% | 4.2% | 10.8% |

These results are consistent with Dimensional's "The Uncommon Average" (S&P 500 1926–2018: 75.2% / 87.7% / 94.7% positive at 1 / 5 / 10 years). Caveats:
- Overlapping windows make the effective sample small: only ~10 independent 10-year periods since 1926.
- The US is the best-case survivor. Across 39 developed markets over 1841–2019, the chance of losing to inflation over 30 years is 12% ([Anarkulova, Cederburg & O'Doherty 2022, JFE 143(1):409–433](https://doi.org/10.1016/j.jfineco.2021.06.040)).

---

## 3. Active-management base rates (SPIVA, S&P Dow Jones Indices)

**Share of active US equity funds that underperformed** (absolute returns, count-based, survivorship-adjusted by S&P DJI):
| Scorecard (data as of) | Category vs benchmark | 1y | 3y | 5y | 10y | 15y | 20y |
|---|---|---|---|---|---|---|---|
| SPIVA U.S. Mid-Year 2026 (2026-06-30) | All Large-Cap Funds vs S&P 500 | 78.7% | 76.6% | 89.3% | 83.3% | 90.5% | 92.6% |
| SPIVA U.S. Mid-Year 2026 (2026-06-30) | All Domestic Funds vs S&P Composite 1500 | 60.8% | 79.3% | 91.4% | 88.2% | 93.2% | 94.9% |
| SPIVA U.S. Year-End 2025 (2025-12-31) | All Large-Cap Funds vs S&P 500 | 78.8% | 66.8% | 89.0% | 85.6% | 89.9% | 92.9% |
| SPIVA U.S. Year-End 2025 (2025-12-31) | All Domestic Funds vs S&P Composite 1500 | 79.8% | 80.4% | 91.5% | 90.4% | 93.2% | 95.0% |
| SPIVA U.S. Year-End 2024 (2024-12-31) | All Large-Cap Funds vs S&P 500 | 65.2% | 85.0% | 76.3% | 84.3% | 89.5% | 92.0% |
| SPIVA U.S. Year-End 2025 | All Large-Cap, risk-adjusted | – | 82.8% | 91.1% | 95.7% | 98.6% | 97.8% |

Sources: [SPIVA U.S. Mid-Year 2026 (pub. 2026-09-17)](https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-mid-year-2026.pdf) ·
[SPIVA U.S. Year-End 2025 (pub. 2026-03-03)](https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2025.pdf) ·
[SPIVA U.S. Year-End 2024 (pub. 2025-03-04)](https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2024.pdf).
R3 checked the MY2026 and YE2025 large-cap rows in the PDF text; the domestic MY2026 and YE2024 rows were checked by an R3 sub-agent.

**Annual pattern:**
- In 2025, **79%** of large-cap funds lagged the S&P 500, the fourth-worst year in the scorecard's 25-year history. In H1 2026 the figure was **67%**.
- Over 2001–2025 the annual rate averaged **65%**. A majority outperformed only in 2005, 2007 and 2009.

**Survivorship:** only 67% of large-cap funds survived 10 years and ~35% survived 20 years (YE2025 Report 2).

**Persistence** (SPIVA U.S. Persistence Scorecard Year-End 2025, pub. 2026-05-07, [PDF](https://www.spglobal.com/spdji/en/documents/spiva/persistence-scorecard-year-end-2025.pdf)):
| Category | Measure | Horizon | Value |
|---|---|---|---|
| Large-cap | top quartile in CY2023 staying top quartile through 2025 (3 consecutive yrs) | 3 consecutive years | 28.90% |
| All Domestic | top quartile in CY2023 staying top quartile through 2025 | 3 consecutive years | 33.01% |
| Large-cap | top half staying top half 3 consecutive yrs (random expectation 25%) | 3 consecutive years | 49.41% |
| Large-cap | top quartile in CY2021 staying top quartile 5 consecutive yrs | 5 consecutive years | 0.00% |
| All Domestic | top quartile in CY2021 staying top quartile 5 consecutive yrs | 5 consecutive years | 0.00% |
| Large-cap | top half staying top half 5 consecutive yrs (random expectation 6.25%) | 5 consecutive years | 4.49% |
| Large-cap | top-quartile over 2015-20 still top quartile over 2020-25 (random 25%) | 5y->next 5y | 13.84% |
| All Domestic | top-quartile over 2015-20 still top quartile over 2020-25 (random 25%) | 5y->next 5y | 11.79% |
| Large-cap | top-half over 2015-20 still top half over 2020-25 (random 50%) | 5y->next 5y | 39.62% |

**Implication.** The base rate for "a skilled-looking active large-cap strategy beats the S&P 500 over 10–20 years" is **~7–17%** after fees (100% minus 83–93%). Past top-quartile status predicts little: top-quartile large-cap funds stayed top quartile over the next five years 13.8% of the time, against 25% expected by chance.

---

## 4. Single-stock outcome base rates

### 4.1 Published evidence
| Source | Metric | Value | Sample | Date | Verification |
|---|---|---|---|---|---|
| [Bessembinder (2018) JFE 129(3):440-457](https://doi.org/10.1016/j.jfineco.2018.06.004) | share of CRSP common stocks with lifetime buy-and-hold return > 1-month T-bills | 42.6% | US CRSP 1926-2016, 25,967 stocks | 2018 | VERIFIED-R3 |
| [Bessembinder (2018)](https://doi.org/10.1016/j.jfineco.2018.06.004) | share of stocks beating the value-weighted market: annual / decade / lifetime | 44.4% / 37.3% / 30.8% | US CRSP 1926-2016 (Table 2A) | 2018 | VERIFIED-R3 |
| [Bessembinder (2018)](https://doi.org/10.1016/j.jfineco.2018.06.004) | share beating 1-month T-bills: annual / decade / lifetime | 51.6% / 49.5% / 42.6% | US CRSP 1926-2016 (Table 2A) | 2018 | VERIFIED-R3 |
| [Bessembinder (2018)](https://doi.org/10.1016/j.jfineco.2018.06.004) | share of monthly stock returns > T-bill | 47.8% | US CRSP 1926-2016 | 2018 | VERIFIED-R3 |
| [Bessembinder (2018)](https://doi.org/10.1016/j.jfineco.2018.06.004) | firms accounting for all net wealth creation | 1,092 firms = 4.31% of 25,332 firms | US 1926-2016 | 2018 | VERIFIED-R3 |
| [Bessembinder (2018)](https://doi.org/10.1016/j.jfineco.2018.06.004) | share with positive lifetime return; median lifetime return | 49.5%; median -2.29% | US CRSP 1926-2016 | 2018 | VERIFIED-R3 (sign inferred: <50% positive) |
| [Bessembinder, Chen, Choi & Wei (2023) FAJ 79(3):33-63](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3710251) | share of stocks underperforming 1-month T-bills over life | US 55.2%; non-US 57.4% | 64,000+ global stocks 1990-2020 | 2023 | VERIFIED-SUB |
| [Bessembinder (2026) 'One Hundred Years in the U.S. Stock Markets' (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6438198) | median buy-and-hold return; share reducing wealth | median -6.9%; ~60% reduced wealth | 29,754 US stocks 1926-2025 | 2026-03-18 | VERIFIED-SUB |
| [J.P. Morgan Eye on the Market, 'Agony & Ecstasy' (Cembalest, 2021)](https://assets.jpmprivatebank.com/content/dam/jpm-pb-aem/global/en/documents/eotm/agony-ecstasy-2021.pdf) | catastrophic loss (-70% from peak, not recovered) / negative absolute return / underperformed Russell 3000 / megawinners | 44% / 42% / 66% / 10% | Russell 3000 constituents 1980-2020 | 2021-03-15 | VERIFIED-R3 |
| [J.P. Morgan 'Agony & Ecstasy' (2014, v2.0)](https://www.researchgate.net/publication/303696398) | catastrophic loss / negative absolute / underperformed Russell 3000 (median excess -54%) | 40% / 40% / 64% | ~13,000 Russell 3000 stocks 1980-2014 | 2014 | SECONDARY (mirror; VERIFIED-SUB) |
| [Dimensional, 'Singled Out' (Crill)](https://www.dimensional.com/ie-en/insights/singled-out-historical-performance-of-individual-stocks) | share of US stocks that survived AND beat the market over 5 / 10 / 20 yrs | 34.7% / 28.8% / 21.4% | US stocks, rolling, 1927-2020 | 2022-05-11 | VERIFIED-R3 |
| [Dimensional, 'Singled Out'](https://www.dimensional.com/ie-en/insights/singled-out-historical-performance-of-individual-stocks) | past 20-yr winners vs losers surviving & beating market next 10 yrs | 30.2% vs 30.3% (all stocks 24.3%) | US 1947-2020 | 2022-05-11 | VERIFIED-R3 |
| [S&P DJI SPIVA YE2025, Exhibit 7](https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2025.pdf) | share of S&P 500 stocks beating the index in 2025 (Q1/Q2/Q3/Q4) | 30% (62/29/38/40%) | S&P 500 constituents 2025 | 2026-03-03 | VERIFIED-R3 |
| [S&P DJI Indexology blog 'Skewing Success'](https://www.indexologyblog.com/2025/09/30/skewing-success/) | share of S&P 500 constituents beating the index: 2023 / 2024 | 26% / 28% | S&P 500 | 2025-09-30 | VERIFIED-SUB |
| [S&P DJI 'Shooting the Messenger'](https://www.spglobal.com/spdji/en/documents/research/research-shooting-the-messenger.pdf) | stocks in the S&P 500 at some point 2002-2021 beating the average | 26% (253 of 975); 20-yr median return 88% vs mean 358% | S&P 500 2002-2021 | 2022-11-22 | VERIFIED-SUB |
| ['The Capitalism Distribution' (Blackstar/Longboard, c.2008)](https://web.archive.org/web/20160309100319id_/http://theivyportfolio.com/wp-content/uploads/2008/12/thecapitalismdistribution.pdf) | Russell 3000-eligible stocks: negative lifetime return / underperformed index / lost >=75% | 39% / 64% / 18.5% | 8,054 stocks 1983-2007 | c.2008 | VERIFIED-SUB |
| [Anarkulova, Cederburg & O'Doherty (2022) JFE 143(1):409-433](https://doi.org/10.1016/j.jfineco.2021.06.040) | probability a diversified investor loses to inflation over 30 years | 12% | 39 developed markets 1841-2019 (bootstrap) | 2022 | VERIFIED-R3 (abstract via RePEc) |
| [Dimensional, 'The Uncommon Average'](https://www.dimensional.com/us-en/insights/the-uncommon-average) | S&P 500 positive over rolling 1 / 5 / 10 years | 75.2% / 87.7% / 94.7% | 1926-2018 overlapping | 2019-05-02 | VERIFIED-SUB |
| [MSCI Barra, Gleiser & McKenna 'Converting Scores into Alphas'](https://www.msci.com/documents/10199/1645561/PI_Converting_Scores_Into_Alphas.pdf) | practitioner IC benchmarks | 'good' IC 0.05; 'very good' 0.10 | practitioner note | 2010-05 | VERIFIED-R3 |

### 4.2 Our point-in-time computation: share of S&P 500 members beating the S&P 500 TR (buy-and-hold, by count)

**Method:**
- Membership: agent D2's reconstruction from fja05680 and Wikipedia (`d2_universe_spells.csv`, read-only). D1 owns the authoritative membership.
- Returns: Yahoo adjusted monthly returns (`d2_ret_monthly.parquet`).
- Members whose series ends early are assumed to sit in cash after their last full month.
- Members with no Yahoo data are missing; they are mostly acquired or bankrupt names. We report bounds that assume all missing names lost or all won.

| Year | Members on 1 Jan | Coverage (Yahoo data) | S&P 500 TR | % beating index (covered) | Bounds (missing all lose / all win) |
|---|---|---|---|---|---|
| 2016 | 502 | 75% | 12.0% | 55% | 41%–66% |
| 2017 | 506 | 78% | 21.8% | 45% | 35%–57% |
| 2018 | 505 | 81% | -4.4% | 46% | 37%–56% |
| 2019 | 505 | 83% | 31.5% | 47% | 39%–56% |
| 2020 | 505 | 86% | 18.4% | 34% | 29%–43% |
| 2021 | 505 | 88% | 28.7% | 47% | 42%–53% |
| 2022 | 505 | 90% | -18.1% | 58% | 52%–62% |
| 2023 | 503 | 94% | 26.3% | 28% | 26%–33% |
| 2024 | 503 | 95% | 25.0% | 28% | 26%–31% |
| 2025 | 503 | 97% | 17.9% | 31% | 30%–33% |
| 2026 (Jan–Aug) | 503 | 98% | 13.1% | 43% | 42%–44% |

**Averages across start years:**
- **All complete years 2001–2025:** 1-year beat rate **49.2%** (bounds 34%–63%, mean coverage 71%).
  - Coverage is only ~50% in 2001–2005, so the early years overstate the rate.
- **Years with ≥85% coverage (2020–2025):**
  - 1 year: **37.6%**.
  - 3 years: 35.6%.
  - 5 years: 28.6%.
- **Cross-check against published figures:**
  - S&P DJI: 26% (2023), 28% (2024) and 30% (2025).
  - Ours: 28%, 28% and 31%. This agrees within 1–2 points, which validates the pipeline.
- **Long-run context:** Bessembinder's all-CRSP annual rate is 44.4% (value-weighted market). The cap-weighted index beats the median stock whenever mega-caps lead, which is why recent years sit at 28–34%.

### 4.3 Legacy `close10.pkl` (SURVIVORSHIP-BIASED: 497 stocks that are S&P 500 members in Sept 2026; 2015-09 → 2026-08; benchmark ^SP500TR)
| Horizon | Start months (non-overlapping) | Avg # stocks | % with return > 0 | % beating S&P 500 TR (min–max across starts) | % beating ^GSPC price index (naive – wrong) | Median stock minus index (cumulative) |
|---|---|---|---|---|---|---|
| 1 yr | 120 (10) | 482 | 69.8% | 47.6% (31%–64%) | 50.7% | -2.0% |
| 3 yr | 96 (3) | 478 | 81.5% | 44.5% (27%–59%) | 50.3% | -8.8% |
| 5 yr | 72 (2) | 474 | 88.0% | 42.6% (31%–54%) | 49.7% | -17.5% |
| 10 yr | 12 (1) | 463 | 94.7% | 36.0% (32%–39%) | 45.4% | -88.5% |

Even this upward-biased sample shows that the typical stock lags the index. Only 36% of these *survivors* beat the S&P 500 TR over 10 years, and the median stock trailed the index by 89 percentage points of cumulative return. Using `^GSPC` (price-only) instead of the total-return index would inflate every beat rate by 3–9 points.

**Random equal-weight portfolios from the same universe:**
| Horizon | # stocks | P(portfolio > 0) | P(beats S&P 500 TR) – survivorship-biased | same, crude bias-adjusted | TE of random EW portfolio (median, p10–p90) |
|---|---|---|---|---|---|
| 1 yr | 1 | 69.7% | 47.5% | 37.7% | – |
| 1 yr | 15 | 84.7% | 60.0% | 32.7% | 8.4% (7.3%–9.8%) |
| 1 yr | 20 | 85.0% | 62.6% | 32.4% | 7.7% (6.7%–9.0%) |
| 1 yr | 30 | 85.2% | 65.0% | 30.4% | 7.0% (6.1%–8.0%) |
| 1 yr | 50 | 85.3% | 68.9% | 28.6% | 6.3% (5.6%–7.2%) |
| 3 yr | 1 | 81.2% | 44.6% | 28.2% | – |
| 3 yr | 15 | 99.7% | 64.4% | 20.7% | 8.4% (7.3%–9.8%) |
| 3 yr | 20 | 99.8% | 67.1% | 19.0% | 7.7% (6.7%–9.0%) |
| 3 yr | 30 | 100.0% | 70.5% | 18.0% | 7.0% (6.1%–8.0%) |
| 3 yr | 50 | 100.0% | 76.9% | 15.3% | 6.3% (5.6%–7.2%) |
| 5 yr | 1 | 88.0% | 42.1% | 22.5% | – |
| 5 yr | 15 | 100.0% | 65.9% | 14.9% | 8.4% (7.3%–9.8%) |
| 5 yr | 20 | 100.0% | 69.5% | 12.7% | 7.7% (6.7%–9.0%) |
| 5 yr | 30 | 100.0% | 74.9% | 10.5% | 7.0% (6.1%–8.0%) |
| 5 yr | 50 | 100.0% | 81.6% | 7.5% | 6.3% (5.6%–7.2%) |

**Survivorship bias quantified:** over 2015-10-31..2026-08-31, a monthly-rebalanced equal-weight portfolio of today's members returned **18.1%/yr**. The investable S&P 500 Equal Weight ETF (RSP) returned **12.4%/yr**. The gap, **≈5.7%/yr**, is the bias of back-testing on current constituents; RSP's ~0.20% fee and quarterly rebalancing explain little of it. The biased table says random 20-stock portfolios beat the index 63% of the time over 1 year. After removing the bias, the figure is ≈32%, consistent with RSP lagging SPY in this era.

**Tracking error of a 15–30 stock equal-weight large-cap portfolio:** 7.0%–8.4% (median of 1,000 random draws; TE is little affected by survivorship). A factor-tilted 15–30 stock portfolio should expect **~6–9% TE**.

---

## 5. Synthesis for the v4 model

### 5a. Realistic gross alpha, tracking error and hit rate for a 15–30 stock large-cap long-only Q+V+M+S tilt

| Evidence line | Gross active return/yr | TE | IR | Years with negative active return |
|---|---|---|---|---|
| French big-cap long-only mix, 1963–2026, broad (2x3) | +1.91% | 3.1% | 0.62 | 26% |
| French big-cap long-only mix, 1963–2026, concentrated (5x5) | +2.26% | 4.3% | 0.52 | 31% |
| Same, 2010–2026 (2x3 / 5x5) | +0.54% / +1.07% | 3.0% / 4.5% | 0.18 / 0.24 | 56% / 44% |
| 1963–2026 long-only mix × post-publication retention (~0.45) | ≈ +0.9% to +1.0% | 3–4% | ~0.25 | ~40% |
| Live factor ETFs 2011/13/15–2026 (net; fees 0.08–0.15%) | -3.3% to +1.0% | 1.4–8.8% | −0.65 to 0.14 | 42–71% |
| Random 15–30 stock equal-weight portfolio (idiosyncratic TE only) | – | 7.0%–8.4% | – | – |
| Earnings-surprise drift (large caps, post-2006) | ≈ 0 (Martineau 2022) | – | – | – |

**Recommended prior (pre-registered, not to be tuned on backtests):**
- **Expected gross alpha +1.0%/yr** (80% range 0 to +2%). Net of 10 bps one-way costs at ~100–200% annual turnover, that is ≈ +0.6–0.8%.
- **TE ≈ 7%, IR ≈ 0.15.**
- **What that implies** (1.0% alpha, 7% TE):
  - P(beat S&P 500 in a given year) ≈ **56%**, so the portfolio lags in ≈44% of years.
  - Over 5 years ≈ 63%; over 10 years ≈ 67%.
  - An optimistic case (+2% alpha, 5% TE) gives 66% / 81% / 90%.
- **Tripwire:** any backtest claiming > +3%/yr gross for this design should be treated as evidence of a bug or bias (look-ahead, survivorship, data-snooping), not of skill.

### 5b. What "90% confident" can and cannot legitimately mean

**Calibration table** (normal approximation, iid annual active returns; fat tails make real odds worse):
| Expected alpha | TE | IR | P(beat) 1y | 3y | 5y | 10y | 20y | Years for 90% odds | Years for t = 2 |
|---|---|---|---|---|---|---|---|---|---|
| 0.5% | 3% | 0.17 | 57% | 61% | 65% | 70% | 77% | 59 | 144 |
| 0.5% | 5% | 0.10 | 54% | 57% | 59% | 62% | 67% | 164 | 400 |
| 0.5% | 7% | 0.07 | 53% | 55% | 56% | 59% | 63% | 322 | 784 |
| 0.5% | 9% | 0.06 | 52% | 54% | 55% | 57% | 60% | 532 | 1296 |
| 1.0% | 3% | 0.33 | 63% | 72% | 77% | 85% | 93% | 15 | 36 |
| 1.0% | 5% | 0.20 | 58% | 64% | 67% | 74% | 81% | 41 | 100 |
| 1.0% | 7% | 0.14 | 56% | 60% | 63% | 67% | 74% | 80 | 196 |
| 1.0% | 9% | 0.11 | 54% | 58% | 60% | 64% | 69% | 133 | 324 |
| 2.0% | 3% | 0.67 | 75% | 88% | 93% | 98% | 100% | 4 | 9 |
| 2.0% | 5% | 0.40 | 66% | 76% | 81% | 90% | 96% | 10 | 25 |
| 2.0% | 7% | 0.29 | 61% | 69% | 74% | 82% | 90% | 20 | 49 |
| 2.0% | 9% | 0.22 | 59% | 65% | 69% | 76% | 84% | 33 | 81 |
| 3.0% | 3% | 1.00 | 84% | 96% | 99% | 100% | 100% | 2 | 4 |
| 3.0% | 5% | 0.60 | 73% | 85% | 91% | 97% | 100% | 5 | 11 |
| 3.0% | 7% | 0.43 | 67% | 77% | 83% | 91% | 97% | 9 | 22 |
| 3.0% | 9% | 0.33 | 63% | 72% | 77% | 85% | 93% | 15 | 36 |

**Single-stock hit rates implied by signal quality** (bivariate-normal score/return, correlation = IC):
| Signal IC | Top 5% pick | Top 10% pick | Top 20% pick | (base rate: random stock beats index = 45%) | Top 10% pick if base rate 50% |
|---|---|---|---|---|---|
| 0.00 | 45.0% | 45.0% | 45.0% | | 50.0% |
| 0.03 | 47.5% | 47.1% | 46.7% | | 52.1% |
| 0.05 | 49.1% | 48.5% | 47.8% | | 53.5% |
| 0.08 | 51.6% | 50.6% | 49.5% | | 55.6% |
| 0.10 | 53.2% | 52.0% | 50.6% | | 57.0% |
| 0.15 | 57.4% | 55.5% | 53.4% | | 60.5% |
| 0.20 | 61.5% | 59.1% | 56.2% | | 63.9% |

**Legitimate uses of "90%":**
- **Market exposure over long horizons.** "A diversified US equity portfolio has had a positive nominal return over 10 years about 95% of the time, and over 15 years 99.5%." Add the international caveat: a 12% chance of a real loss over 30 years.
- **Ranges rather than rankings.** "We are ~90% confident next year's return will land within ±12 pp of the S&P 500 if TE ≈ 7%." This is a statement about dispersion. It can be checked, and so it can be calibrated.
- **Process claims.** For example: "90% of positions pass all data-validation gates" or "the portfolio stays within its risk limits."

**Illegitimate uses of "90%":**
- **Any claim that a stock will beat the index over a year.** The base rate depends on the regime: 44% long-run (Bessembinder), but 28–34% in the mega-cap-led years 2020 and 2023–2025. Good signals add only ~2–7 points.
- **That a 15–30 stock tilt will beat the index over 1–5 years.** Realistically the odds are 55–75%.
- **That a strategy's backtest proves it.** A 90% hit rate would need IR ≥ 1.28 over one year, or a net IR ≥ 0.4 sustained for 10 years.
  - The French large-cap long-only mixes reached IR 0.5–0.6 *gross and pre-publication* over 1963–2026.
  - But they managed only 0.18–0.24 since 2010, and live products managed −0.65 to +0.14.
  - So a sustained net IR of 0.4 is not a defensible expectation.

**Recommendation.** Replace per-stock "confidence 0–100" scores with two separate, calibrated quantities:
1. **P(beat S&P 500 TR over 12 months)**, which should sit in the 45–60% band and be validated by out-of-sample calibration (Brier score).
2. **P(drawdown worse than −30% within 12 months)** from the risk engine.

Business-quality "conviction" is a descriptive rating, not a probability.

### 5c. Recommended haircuts for backtested alpha
| Backtest Sharpe (or IR) | Years | t (single test) | Haircut if best of 10 variants | best of 100 | best of 316 |
|---|---|---|---|---|---|
| 0.30 | 10 | 0.95 | 98% | 100% | 100% |
| 0.30 | 20 | 1.34 | 87% | 100% | 100% |
| 0.30 | 60 | 2.32 | 43% | 93% | 100% |
| 0.50 | 10 | 1.58 | 76% | 100% | 100% |
| 0.50 | 20 | 2.24 | 46% | 96% | 100% |
| 0.50 | 60 | 3.87 | 16% | 34% | 45% |
| 0.75 | 10 | 2.37 | 41% | 91% | 100% |
| 0.75 | 20 | 3.35 | 21% | 47% | 64% |
| 0.75 | 60 | 5.81 | 7% | 14% | 18% |
| 1.00 | 10 | 3.16 | 23% | 54% | 73% |
| 1.00 | 20 | 4.47 | 12% | 25% | 32% |
| 1.00 | 60 | 7.75 | 4% | 8% | 10% |

| Source of optimism | Recommended adjustment | Evidence |
|---|---|---|
| Post-publication decay of published anomalies | keep ~40–50% of in-sample alpha (−58% average) | McLean & Pontiff (2016); our French check: value -57%, momentum -53%, investment -108%, profitability -15% |
| In-sample over-fitting / data mining | an additional −26% for published signals; much more for self-mined variants | McLean & Pontiff (2016): out-of-sample, pre-publication decline |
| Multiple testing | require t ≥ 3; the haircut is nonlinear (Sharpe 0.5 over 10 yrs → 76–100%; Sharpe 1.0 over 20 yrs → 12–32%) | Harvey, Liu & Zhu (2016); Harvey & Liu (2015, JPM 42(1):13–28): "50% is too lenient for relatively small Sharpe ratios (< 0.4) and too harsh for large ones (> 1.0)" |
| Long-short all-cap → large-cap long-only | × ~0.35–0.55 | Section 2.6; Israel & Moskowitz (2013) |
| Survivorship (current-constituent universe) | −5 to −6%/yr on equal-weight comparisons (2015–2026) | Section 4.3 (RSP comparison) |
| Price-only benchmark vs dividend-adjusted stocks | −1.5 to −2%/yr (the S&P 500 dividend yield) | Section 4.3 |
| Trading costs | −(annual one-way turnover × 2 × 10 bps) ≈ −0.2 to −0.4%/yr | pre-registration |

**Rule for the lead:** forward alpha = min(0.4 × backtested alpha, literature prior ~+1%/yr) − costs. Report the raw and haircut figures side by side. Never report a backtest-derived probability of outperformance without the haircut and the implied TE.

### 5d. Implications for the pre-registered model (no changes proposed after seeing results)

- **Keep the four families equally weighted.** The evidence does not justify overweighting any family on recent data. Recent winners (momentum, profitability) and losers (value, investment) have swapped leadership over the decades. Diversification across families is the main source of IR: the combo's Sharpe (0.76) is ~1.8× the average single factor's (1963–2026).
- **SUE deserves the weakest prior.** Martineau (2022) finds the drift gone for large caps. Consider flagging S as a tie-breaker in the report narrative, but do not change the frozen weights.
- **Keep low volatility as a constraint only.** It confirms the pre-registration.
- **Expect ~40–45% losing years.** Communicate an IR of ~0.15, a TE of ~7%, and a realistic chance of a 3–5 year stretch of underperformance. The EW factor combo's worst drawdown lasted 12 years (2008–2020).

---

## 6. Validation checks, limitations, files

**Validation checks performed:**
- **Factor data (9/9 pass):**
  - No missing FF5 or UMD months, 1963-07 → 2026-07.
  - HML identical in the FF3 and FF5 files.
  - Mkt-RF differs between files by ≤ 8 bp (mean 0.3 bp).
  - Annual RF matches compounded monthly RF (≤ 3 bp).
  - HML, RMW, CMA and UMD rebuild from their underlying 2x3 portfolio files to within ≤ 1 bp/month (correlation ≥ 0.99999).
  - Data vintage is 202607.
- **Long-only capture (13/13 pass):**
  - The big-cap universe tracks the CRSP market (TE 1.4%).
  - No missing months.
  - Same-month vs lagged weight timing was tested empirically.
- **Stock base rates (4/4 pass):**
  - `close10` confirmed dividend-adjusted: MO and T growth equals Yahoo Adj Close, not Close.
  - `^SP500TR` present for all months.
  - Universe = 497 stocks.
- **Point-in-time cross-check:** our 2023/2024/2025 beat rates (28%/28%/31%) are within 1–2 points of S&P DJI's published 26%/28%/30%.
- **Sources:** SPIVA large-cap rows (YE2025, MY2026), Bessembinder Table 2A, J.P. Morgan 2021, Dimensional, Harvey–Liu 2015 and the MSCI IC benchmark were verified by R3 in the primary documents. Other rows are marked VERIFIED-SUB or SECONDARY in the CSVs.

**Known limitations:**
1. **French factors are not what we will trade.** They are long-short, all-cap and gross, and their construction is not identical to the pre-registered model's variables.
2. **The long-only capture uses mixes, not an integrated composite.**
3. **Short windows.** Post-2010 statistics have t < 1.5 and cannot distinguish decay from bad luck.
4. **The PIT beat-rate is incomplete in early years.** It relies on D2's reconstructed membership and on Yahoo data, which miss most delisted names. Early-year coverage is ~50%, so we report bounds.
5. **`close10` analyses are survivorship-biased** by construction, and labelled as such throughout.
6. **ETF evidence covers one regime** (mega-cap growth leadership 2013–2026).
7. **The normal approximations** in the calibration ignore fat tails and regime shifts.
8. **The literature table's figures** come from abstracts and papers as retrieved; see each row's verification column.

**Files produced (rows):** see the table at the end of `r3_report.md`.
