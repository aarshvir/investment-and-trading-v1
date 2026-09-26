"""
r1_cma_scenarios.py -- agent R1

Writes three small tables (values transcribed by R1 from the cited primary/secondary sources on 2026-09-26):
  v4/data/r1_cma_survey.csv          institutional capital-market assumptions for US large-cap equities (+ cash)
  v4/data/r1_regime_indicators.csv   valuation / rates / concentration indicators as of Sep-2026
  v4/data/r1_scenarios.csv           recommended Bear/Base/Bull scenarios + illustrative model probabilities
Each gets a .meta.json sidecar.

Probability model (illustrative only): annual log returns i.i.d. Normal(m, s^2) with m = ln(1+g), g = scenario
geometric (compound) annual return, s = annualized log-return volatility. P(T-year cumulative return > 0) = Phi(m*sqrt(T)/s).
"""
import json
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd
from scipy.stats import norm

V4 = r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4"
DATA = os.path.join(V4, "data")
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
BREAKEVEN_10Y = 0.0234  # 10y par 5.17% - 10y TIPS real 2.83%, US Treasury, 2026-09-25

# ------------------------------------------------------------------------------------------------
# 1. CMA survey (nominal, USD, annualized geometric unless noted)
# ------------------------------------------------------------------------------------------------
cma = [
    dict(institution="J.P. Morgan Asset Management", edition="2026 Long-Term Capital Market Assumptions (30th ed.)",
         published="2025-10-20", data_as_of="2025-09-30", horizon="10-15y", asset="U.S. Large Cap",
         nominal=0.067, real_published=None, inflation=0.025, vol=0.1647, arith=0.0794, cash=0.031,
         source_type="primary (PDF matrix)", note="2027 edition not found as of 2026-09-26; US large cap building blocks (Exhibit 6, p.13): revenue 6.0%, buybacks 3.0%, dividends 1.7%, margins -0.5%, gross dilution -1.5%, valuation -2.0%",
         url="https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/portfolio-insights/ltcma/noindex/ltcma-full-report.pdf"),
    dict(institution="Vanguard (VCMM)", edition="VCMM 10-year forecasts (Q2-2026 run)",
         published="2026-07-22", data_as_of="2026-06-30", horizon="10y", asset="U.S. large-cap (range 4.1%-6.1%)",
         nominal=0.051, real_published=None, inflation=0.020, vol=0.150, arith=None, cash=0.035,
         source_type="primary (web table/datawrapper data)", note="Vanguard shows a 2-pp range around the 50th percentile; midpoint used. U.S. equities 4.2-6.2%; U.S. value 6.4-8.4%; U.S. growth 3.6-5.6%; cash 3.0-4.0%; inflation 1.5-2.5%. Prior run (2026-03-31) U.S. equities 4.9-6.9%",
         url="https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html"),
    dict(institution="BlackRock Investment Institute", edition="Capital market assumptions, August 2026 ('Starting point' scenario)",
         published="2026-08", data_as_of="2026-06-30", horizon="10y (5y: 9.44%)", asset="US large cap equities (MSCI USA)",
         nominal=0.0897, real_published=None, inflation=None, vol=0.1935, arith=None, cash=0.0366,
         source_type="primary (xlsx download)", note="10y interquartile range 4.14%-14.02%; scenario sheets: 'AI productivity boom' 15.94% (10y), 'Global risk premia rise' 2.02% (10y); cash = 3M T-bill 10y (5y 3.79%)",
         url="https://www.blackrock.com/blk-inst-c-assets/images/tools/blackrock-investment-institute/cma/blackrock-capital-market-assumptions.xlsx"),
    dict(institution="GMO", edition="7-Year Asset Class Forecast 2Q 2026",
         published="2026-07", data_as_of="2026-06-30", horizon="7y", asset="U.S. Large (real)",
         nominal=(1 - 0.081) * (1 + BREAKEVEN_10Y) - 1, real_published=-0.081, inflation=None, vol=None, arith=None, cash=None,
         source_type="primary (PDF chart)", note="REAL forecast -8.1% ('normal' rates, 1.3% equilibrium real cash) / -5.0% ('low' rates); US cash +1.2% real. Nominal here is DERIVED by R1 using 2.34% 10y breakeven",
         url="https://www.gmo.com/globalassets/articles/gmo-7-year-asset-class-forecast/2026/gmo-7-year-asset-class-forecastjun26.pdf"),
    dict(institution="Research Affiliates", edition="Asset Allocation Interactive (as reported by Fortune)",
         published="2026-05-21", data_as_of="2026-04/05 (approx.; AAI monthly)", horizon="10y", asset="U.S. Large Cap",
         nominal=0.032, real_published=0.006, inflation=0.026, vol=None, arith=None, cash=0.035,
         source_type="secondary (Fortune, S. Tully)", note="AAI site requires accepting a disclaimer; not accessed. U.S. Large Cap Growth 1.7%. YE-2025 figure reported elsewhere as 3.1% (unverified)",
         url="https://fortune.com/2026/05/21/bond-yields-today-highest-since-2007-stocks-outlook/"),
    dict(institution="AQR", edition="2026 Capital Market Assumptions for Major Asset Classes",
         published="2026-01-14", data_as_of="2025-12-31", horizon="5-10y", asset="US Large (local real 3.9%)",
         nominal=0.063, real_published=0.039, inflation=0.024, vol=None, arith=None, cash=None,
         source_type="primary (PDF)", note="Real 3.9% (prior yr 4.1%); nominal 6.3% from Exhibit 3C; US real cash 1.3%; 50% confidence band on US equities roughly 0%-7.5% real (chart)",
         url="https://www.aqr.com/-/media/AQR/Documents/Alternative-Thinking/AQR-Alternative-Thinking---2026-Capital-Market-Assumptions.pdf"),
    dict(institution="Goldman Sachs (Portfolio Strategy, P. Oppenheimer et al.)", edition="Building Long-Term Returns: Our 10-Year Forecasts",
         published="2025-11-12", data_as_of="2025-11", horizon="10y", asset="S&P 500 total return",
         nominal=0.065, real_published=None, inflation=None, vol=None, arith=None, cash=None,
         source_type="secondary (report paywalled; TKer 2025-11-13, Seeking Alpha)", note="Components reported: ~6% EPS growth, -1%/yr valuation, 1.4% dividend yield; bear/bull range 3%-10% (Seeking Alpha summary, unverified vs report). Separately, GS US strategist B. Snider cited 7%/yr in a 2026-06-29 Business Insider interview (Yahoo Finance 2026-07-04)",
         url="https://www.tker.co/p/goldman-sachs-10-year-return-forecast-2025"),
    dict(institution="Morgan Stanley Wealth Mgmt (GIC)", edition="Annual Update of GIC Capital Market Assumptions",
         published="2025-03-27", data_as_of="2025-03-13", horizon="7y (strategic)", asset="US Large-Cap Equities",
         nominal=0.063, real_published=None, inflation=None, vol=None, arith=None, cash=0.037,
         source_type="primary (PDF)", note="STALE: no 2026 edition publicly accessible (morganstanley.com/gicreport still resolves to the 2025 PDF). Blocks: shareholder yield 4.1, valuation -1.6, nominal economic path 3.9",
         url="https://www.morganstanley.com/assets/pdfs/2d9493c3-822f-4f18-8c28-ba3ad25e8473.pdf"),
    dict(institution="Charles Schwab", edition="Schwab's 2026 Long-Term Capital Market Expectations",
         published="2026-01-02", data_as_of="2025-10-31", horizon="10y (2026-2035)", asset="U.S. large-cap equities",
         nominal=0.059, real_published=None, inflation=0.024, vol=None, arith=None, cash=0.033,
         source_type="primary (web)", note="Prior year 6.0%; US agg bonds 4.8%",
         url="https://www.schwab.com/learn/story/schwabs-long-term-capital-market-expectations"),
    dict(institution="Northern Trust Asset Management", edition="Capital Market Assumptions 10-Year Outlook: 2026 Edition",
         published="2025-12 (PDF dated 2026-01-09)", data_as_of="2025-09-30", horizon="10y", asset="U.S. equities (MSCI USA)",
         nominal=0.068, real_published=None, inflation=None, vol=None, arith=None, cash=0.033,
         source_type="primary (PDF)", note="2025 edition 7.5%; text: US revenue growth 3.5%/yr, margin expansion ~1.6%/yr, some P/E contraction, dividend yield rising to 2%",
         url="https://ntam.northerntrust.com/content/dam/northerntrust/investment-management/global/en/documents/thought-leadership/2026/cma/2026-capital-market-assumptions-report.pdf"),
    dict(institution="Invesco Solutions", edition="2026 Capital Market Assumptions, USD, Q2 update",
         published="2026-07 (PDF dated 2026-07-23)", data_as_of="2026-03-31", horizon="10y", asset="US large cap (S&P 500)",
         nominal=0.049, real_published=None, inflation=0.0219, vol=0.166, arith=0.062, cash=None,
         source_type="primary (PDF)", note="Blocks: dividend 1.31, buyback 1.81, LT earnings growth 4.04, inflation 2.19, valuation -4.52",
         url="https://www.invesco.com/content/dam/invesco/emea/en/pdf/invesco-capital-market-assumption-usd.pdf"),
    dict(institution="BNY Investments", edition="Capital Market Assumptions 2026 ('Endurance Under Pressure')",
         published="2026-01 (PDF dated 2026-01-23)", data_as_of="2025-12-31", horizon="10y", asset="U.S. Equity (broad)",
         nominal=0.076, real_published=None, inflation=None, vol=0.159, arith=None, cash=None,
         source_type="primary (PDF)", note="2025 edition 7.5%; broad US equity not large-cap specific",
         url="https://www.bny.com/content/dam/imemea/pdfs/endurance-under-pressure-capital-market-assumptions-2026-full.pdf"),
    dict(institution="Horizon Actuarial (survey of 43 advisors)", edition="Survey of Capital Market Assumptions, 2026 Edition",
         published="2026-08 (PDF dated 2026-08-26)", data_as_of="2026 survey", horizon="10y (20y avg 7.02%)", asset="US Equity - Large Cap (average)",
         nominal=0.0639, real_published=None, inflation=0.0244, vol=0.1643, arith=0.0766, cash=0.0346,
         source_type="primary (PDF)", note="10y distribution: min 4.4%, 25th 5.4%, median 6.7%, 75th 7.0%, max 9.1%. Aggregates many firms above -> not independent",
         url="https://www.horizonactuarial.com/_files/ugd/f76a4b_a73ade7e6ba748f192d531c974bbea2a.pdf"),
    dict(institution="Damodaran implied (market-implied, not a CMA)", edition="Implied ERP, start of month",
         published="2026-09-01", data_as_of="2026-09-01", horizon="perpetuity IRR", asset="S&P 500 implied expected return",
         nominal=0.0884, real_published=None, inflation=None, vol=None, arith=None, cash=None,
         source_type="primary (xlsx/web)", note="Implied ERP 4.14% + T-bond 4.75%; uses consensus EPS growth ~14.0% for 5 years -> sensitive to analyst optimism",
         url="https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xlsx"),
]
cdf = pd.DataFrame(cma)
cdf["real_derived"] = np.where(cdf["real_published"].notna(), cdf["real_published"],
                               (1 + cdf["nominal"]) / (1 + cdf["inflation"].fillna(BREAKEVEN_10Y)) - 1)
cdf["real_is_derived"] = cdf["real_published"].isna()
cdf["retrieved"] = "2026-09-26"
cols = ["institution", "edition", "published", "data_as_of", "horizon", "asset", "nominal", "real_published", "real_derived",
        "real_is_derived", "inflation", "vol", "arith", "cash", "source_type", "note", "url", "retrieved"]
cdf = cdf[cols]
cdf.to_csv(os.path.join(DATA, "r1_cma_survey.csv"), index=False)

# summary stats over institutional point estimates (exclude Horizon aggregate and Damodaran market-implied)
core = cdf[~cdf["institution"].str.startswith(("Horizon", "Damodaran"))]
summ = dict(n=len(core), median=float(core["nominal"].median()), mean=float(core["nominal"].mean()),
            p25=float(core["nominal"].quantile(0.25)), p75=float(core["nominal"].quantile(0.75)),
            min=float(core["nominal"].min()), max=float(core["nominal"].max()),
            median_real=float(core["real_derived"].median()))
recent = core[core["data_as_of"].str.startswith("2026")]
summ_recent = dict(n=len(recent), median=float(recent["nominal"].median()), members=list(recent["institution"]))

# ------------------------------------------------------------------------------------------------
# 2. Regime indicators
# ------------------------------------------------------------------------------------------------
FS = "https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_092526.pdf"
UST = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv"
USTB = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_bill_rates&field_tdr_date_value=2026&page&_format=csv"
USTR = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026&page&_format=csv"
SH = "https://shillerdata.com/ (ie_data.xls saved 2026-09-02)"
GTM = "https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/market-insights/guide-to-the-markets/mi-guide-to-the-markets-us.pdf"
DAM = "https://pages.stern.nyu.edu/~adamodar/ (home page) and https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xlsx"
SPY = "https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx"
YF = "Yahoo Finance via yfinance (^GSPC, ^VIX), retrieved 2026-09-26"
ind = [
    ("S&P 500 close", 7743.41, "index", "2026-09-25", YF, "matches lead-provided close"),
    ("S&P 500 all-time closing high", 7798.99, "index", "2026-08-13", YF, "current level -0.7% below ATH"),
    ("S&P 500 price return YTD", 0.1312, "decimal", "2026-09-25", YF, "computed by R1; max intra-year decline YTD -9.1%"),
    ("Forward 12M P/E (FactSet)", 19.2, "x", "2026-09-25 (price 2026-09-24 7,704.13)", FS, "5y avg 19.8, 10y avg 19.0; was 20.4 on 2026-06-30"),
    ("Trailing 12M P/E (FactSet)", 25.8, "x", "2026-09-25", FS, "5y avg 24.4, 10y avg 23.6"),
    ("CY2026 EPS growth, consensus (FactSet)", 0.320, "decimal", "2026-09-25", FS, "CY2026 revenue growth 12.3%; Q3-26 EPS growth est. 29.1%"),
    ("CY2027 EPS growth, consensus (FactSet)", 0.154, "decimal", "2026-09-25", FS, "CY2027 revenue growth 9.2%"),
    ("Bottom-up 12M target price (FactSet)", 9275.04, "index", "2026-09-25", FS, "+20.4% vs 7,704.13"),
    ("Shiller CAPE (Aug-2026 monthly avg)", 41.12, "x", "2026-08", SH, ""),
    ("Shiller CAPE (Sept-1 close)", 40.58, "x", "2026-09-01", SH, ""),
    ("Shiller CAPE estimated at 2026-09-25", 41.17, "x", "2026-09-25", SH, "R1 scaled Sept value by 7743.41/7631.47; 99th pct since 1881; record 44.2 (Dec-1999)"),
    ("Shiller excess CAPE yield", 0.0101, "decimal", "2026-09", SH, "Shiller definition"),
    ("JPM GTM forward P/E vs 30y avg", 20.4, "x", "2026-06-30", GTM, "30y avg 17.2x; CAPE 40.7x vs 28.8x; div yield 1.4% vs 2.0%; EY minus Baa -0.5% vs 0.7%"),
    ("10-year Treasury par yield", 0.0517, "decimal", "2026-09-25", UST, "2y 4.81%, 5y 4.98%, 30y 5.49%"),
    ("3-month Treasury (CMT par yield)", 0.0424, "decimal", "2026-09-25", UST, "1-month 4.04%, 6-month 4.33%, 1-year 4.50%"),
    ("13-week T-bill (coupon equivalent)", 0.0418, "decimal", "2026-09-25", USTB, "bank discount 4.08%; 52-week CE 4.48%"),
    ("10-year TIPS real yield", 0.0283, "decimal", "2026-09-25", USTR, "implied 10y breakeven inflation ~2.34%"),
    ("Damodaran implied ERP (T12m, adjusted payout)", 0.0414, "decimal", "2026-09-01", DAM, "T-bond 4.75%; prior month 4.28%; implied expected return 8.84%"),
    ("Forward earnings yield minus 10y Treasury", 1 / 19.2 - 0.0517, "decimal", "2026-09-25", FS + " ; " + UST, "computed by R1: 5.21% - 5.17%"),
    ("Top-10 companies weight in S&P 500 (SPY)", 0.4037, "decimal", "2026-09-24", SPY, "Alphabet share classes combined; 38.8% by top-10 lines; top-5 30.3%; top-20 50.6%"),
    ("Top-10 weight in S&P 500 (JPM GTM)", 0.379, "decimal", "2026-06-30", GTM, "top-10 share of S&P 500 earnings 33.7%"),
    ("VIX close", 14.87, "index pts", "2026-09-25", YF, "mean since 1990 19.4, median 17.6"),
    ("S&P 500 realized vol, last 1y (daily, annualized)", 0.1299, "decimal", "2026-09-25", YF, "computed by R1"),
]
idf = pd.DataFrame(ind, columns=["indicator", "value", "unit", "as_of", "source", "note"])
idf["retrieved"] = "2026-09-26"
idf.to_csv(os.path.join(DATA, "r1_regime_indicators.csv"), index=False)

# ------------------------------------------------------------------------------------------------
# 3. Scenarios and illustrative probabilities
# ------------------------------------------------------------------------------------------------
SIG = 0.16
CASH = 0.040
scen = [
    ("Bear", 0.020, "Valuation mean reversion: RA 3.2%, Vanguard low end 4.1%, CAPE regressions 2.6-5.0% nominal, BlackRock 'global risk premia rise' 2.0%, GS bear 3%, GMO -6% (7y) as tail"),
    ("Base", 0.060, "Institutional consensus: median of 12 firm point estimates 6.3%; Horizon 2026 survey avg 6.4% (median 6.7%); most recent valuation-aware updates lower (Vanguard ~5.1%, Invesco 4.9%)"),
    ("Bull", 0.090, "Earnings-boom continuation: BlackRock 'starting point' 8.97% (10y) / 9.44% (5y), Damodaran implied 8.84%, Horizon max 9.1%, GS bull 10%"),
    ("Prior v3 assumption (for comparison)", 0.100, "Assumption used in prior research; above every current institutional base case except BlackRock scenario sheets"),
]
out = []
for name, g, basis in scen:
    m = np.log1p(g)
    row = dict(scenario=name, nominal_geo_return=g, real_approx=(1 + g) / (1 + BREAKEVEN_10Y) - 1, vol_log_annual=SIG,
               arithmetic_equiv=g + SIG ** 2 / 2, cash_assumption=CASH, basis=basis)
    for T in [1, 3, 5, 10]:
        row[f"P_gain_{T}y"] = norm.cdf(m * np.sqrt(T) / SIG)
    for T in [5, 10]:
        row[f"P_beat_cash_{T}y"] = norm.cdf((m - np.log1p(CASH)) * np.sqrt(T) / SIG)
    row["P_loss_worse_than_20pct_5y_endpoint"] = norm.cdf((np.log(0.8) - m * 5) / (SIG * np.sqrt(5)))
    row["median_5y_cumulative"] = np.expm1(m * 5)
    out.append(row)
sdf = pd.DataFrame(out)
# illustrative 25/50/25 mixture of Bear/Base/Bull
w = {"Bear": 0.25, "Base": 0.50, "Bull": 0.25}
mix = {"scenario": "Mixture 25/50/25 (illustrative weights)", "nominal_geo_return": sum(w[k] * sdf.set_index("scenario").loc[k, "nominal_geo_return"] for k in w),
       "basis": "Probability-weighted blend; weights are R1 judgment, not sourced"}
for c in [c for c in sdf.columns if c.startswith("P_")]:
    mix[c] = sum(w[k] * sdf.set_index("scenario").loc[k, c] for k in w)
sdf = pd.concat([sdf, pd.DataFrame([mix])], ignore_index=True)
req = np.expm1(norm.ppf(0.90) * SIG / np.sqrt(5))  # geometric return needed for 90% P(5y gain)
sdf.to_csv(os.path.join(DATA, "r1_scenarios.csv"), index=False)

# ------------------------------------------------------------------------------------------------
# meta
# ------------------------------------------------------------------------------------------------
json.dump({"name": "r1_cma_survey", "agent": "r1", "retrieved_utc": NOW, "rows": len(cdf), "columns": cols,
           "description": "Institutional long-horizon return assumptions for US large-cap equities (USD, nominal, annualized compound unless noted).",
           "summary_core_12_firms": summ, "summary_2026_dated_estimates": summ_recent,
           "caveats": ["Horizons differ (5-15y); GMO is 7y real; Morgan Stanley is 7y and dated 2025-03; BNY is broad US equity.",
                       "real_derived uses each firm's own inflation assumption where available, else the 2.34% 10y breakeven (2026-09-25).",
                       "Research Affiliates and Goldman figures are from secondary reporting (primary not accessible).",
                       "Horizon survey aggregates many of the listed firms; it is not an independent observation."],
           "sources": list(cdf["url"])}, open(os.path.join(DATA, "r1_cma_survey.meta.json"), "w"), indent=2)
json.dump({"name": "r1_regime_indicators", "agent": "r1", "retrieved_utc": NOW, "rows": len(idf), "columns": list(idf.columns),
           "description": "US equity valuation, rates, concentration and volatility indicators as of Sept 2026, one row per indicator with source.",
           "caveats": ["FactSet forward P/E uses the 2026-09-24 close; Shiller CAPE for 2026-09-25 is an R1 estimate scaled from the Sept-1 value."],
           "sources": sorted(set(idf["source"]))}, open(os.path.join(DATA, "r1_regime_indicators.meta.json"), "w"), indent=2)
json.dump({"name": "r1_scenarios", "agent": "r1", "retrieved_utc": NOW, "rows": len(sdf), "columns": list(sdf.columns),
           "description": "Recommended Bear/Base/Bull nominal return scenarios for US large caps (5-10y), with illustrative lognormal probabilities.",
           "model": "annual log returns iid Normal(ln(1+g), s^2), s=0.16; P(gain over T)=Phi(ln(1+g)*sqrt(T)/s); cash 4.0%",
           "geometric_return_needed_for_90pct_P_gain_5y_at_16pct_vol": float(req),
           "caveats": ["Model ignores fat tails, volatility clustering and valuation mean reversion; probabilities are conditional on the scenario, not forecasts.",
                       "Scenario returns are geometric (compound). For arithmetic-return simulators use arithmetic_equiv = g + s^2/2."]},
          open(os.path.join(DATA, "r1_scenarios.meta.json"), "w"), indent=2)

pd.set_option("display.width", 250)
print(cdf[["institution", "data_as_of", "horizon", "nominal", "real_derived", "vol", "cash"]].round(4).to_string())
print("core summary", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in summ.items()})
print("2026-dated", summ_recent)
print(sdf.drop(columns=["basis"]).round(3).to_string())
print("g needed for 90% P(5y gain) at 16% vol:", round(req, 4))
