# Uptrend Analyzer Report

**Generated:** 2026-09-26 00:15:19
**Data Source:** Monty's Uptrend Ratio Dashboard (GitHub CSV)
**API Key Required:** No

---

## Overall Assessment

| Metric | Value |
|--------|-------|
| **Composite Score** | **39.6/100** |
| **Zone** | 🟠 Cautious |
| **Zone Detail** | Cautious-Upper |
| **Zone Proximity** | **Near boundary: -0.4 points from 40 (below)** |
| **Exposure Guidance** | Defensive (30-60%) |
| **Warning Penalty** | -3 (raw: 42.6/100) |
| **Active Warnings** | 1: SECTOR DIVERGENCE WARNING |
| **Strongest Component** | Sector Rotation (73/100) |
| **Weakest Component** | Historical Context (16/100) |
| **Data Quality** | Complete (5/5 components) |
| **Confidence** | High (moderate, Both regime coverage) |

> **Guidance:** Weak breadth environment. Prioritize capital preservation over gains.

---

## Active Warnings

### SECTOR DIVERGENCE WARNING
> Significant divergence detected within sector groups. Some sectors within the same group are moving in opposite directions, suggesting hidden risk beneath the averages.

- Verify individual sector trends before entering positions
- Avoid sectors diverging from their group majority
- Monitor for group convergence or further deterioration

---

## Current Market Snapshot

| Metric | Value |
|--------|-------|
| Uptrend Ratio | 13.7% |
| 10-Day MA | 13.8% |
| Trend | up |
| Slope | +0.0011 |
| Distance from 37% (Overbought) | -23.3pp |
| Distance from 9.7% (Oversold) | +4.0pp |
| Date | 2026-09-24 |

---

## Component Scores

| # | Component | Weight | Score | Contribution | Signal |
|---|-----------|--------|-------|--------------|--------|
| 1 | **Market Breadth (Overall)** | 30% | █░░░ 23 | 6.9 | VERY WEAK: 13.7% uptrend ratio, trend up |
| 2 | **Sector Participation** | 25% | ██░░ 46 | 11.5 | MODERATE: 5/11 sectors uptrending, spread 36.5% |
| 3 | **Sector Rotation** | 15% | ███░ 73 | 10.9 | RISK-ON: Cyclical leads by 9.3pp |
| 4 | **Momentum** | 20% | ██░░ 58 | 11.6 | NEUTRAL MOMENTUM: slope=-0.0007, accelerating |
| 5 | **Historical Context** | 10% | ░░░░ 16 | 1.6 | HISTORICALLY LOW: 13.7% at 16.5th percentile historically |

---

## Component Details

### 1. Market Breadth (Overall)

- **Uptrend Ratio:** 13.7%
- **10-Day MA:** 13.8%
- **Trend:** up
- **Slope:** +0.0011
- **Trend Adjustment:** +5

### 2. Sector Participation

- **Uptrending Sectors:** 5/11
- **Count Score:** 40/100
- **Spread:** 36.5% (score: 56/100)
- **Overbought (>37%):** 0 sectors ()
- **Oversold (<9.7%):** 6 sectors (Consumer Cyclical, Financial, Basic Materials, Consumer Defensive, Real Estate, Utilities)

### 3. Sector Rotation

- **Cyclical Avg:** 15.1%
- **Defensive Avg:** 5.8%
- **Commodity Avg:** 9.2%
- **Cyclical-Defensive Gap:** 9.3pp
- **Divergence Warning:** YES (penalty: -5)
  - **Cyclical Divergence:** std=0.1105, spread=0.3006
    - Outlier: Technology (deviation: +0.2135)
    - Trend dissenter: Financial (down vs majority up)
  - **Defensive Divergence:** std=0.082, spread=0.199
    - Outlier: Healthcare (deviation: +0.1413)
    - Trend dissenter: Healthcare (up vs majority down)

**Cyclical Sectors:**

| Sector | Ratio | Trend | Slope |
|--------|-------|-------|-------|
| Technology | 36.5% | Up | +0.0228 |
| Consumer Cyclical | 6.8% | Up | +0.0029 |
| Communication Services | 13.2% | Up | +0.0009 |
| Financial | 6.4% | Down | -0.0070 |
| Industrials | 12.7% | Up | +0.0040 |


**Defensive Sectors:**

| Sector | Ratio | Trend | Slope |
|--------|-------|-------|-------|
| Utilities | 0.0% | Down | -0.0013 |
| Consumer Defensive | 2.5% | Down | -0.0040 |
| Healthcare | 19.9% | Up | +0.0058 |
| Real Estate | 0.7% | Down | -0.0007 |


**Commodity Sectors:**

| Sector | Ratio | Trend | Slope |
|--------|-------|-------|-------|
| Energy | 12.5% | Down | -0.0375 |
| Basic Materials | 6.0% | Down | -0.0023 |


### 4. Momentum

- **Raw Slope:** +0.0011 
- **Smoothed Slope (EMA(3)):** -0.0007 (score: 53/100)
- **Acceleration (10v10):** 0.003227 (accelerating, score: 75/100)
- **Sector Slope Breadth:** 5/11 positive (score: 45/100)

### 5. Historical Context

- **Current Ratio:** 13.7%
- **Percentile Rank:** 16.5th
- **Historical Range:** 1.1% - 44.3%
- **Historical Median:** 23.5%
- **30-Day Avg:** 19.2%
- **90-Day Avg:** 23.4%
- **Data Points:** 808 (2023-08-11 to 2026-09-24)
- **Confidence:** High (sample: moderate, regime: Both, recency: balanced)

---

## Sector Heatmap

| Rank | Sector | Ratio | Count/Total | 10MA | Trend | Slope | Status |
|------|--------|-------|-------------|------|-------|-------|--------|
| 1 | Technology | 36.5% | 151/414 | 25.6% | Up | +0.0228 | Normal |
| 2 | Healthcare | 19.9% | 83/417 | 20.1% | Up | +0.0058 | Normal |
| 3 | Communication Services | 13.2% | 14/106 | 15.0% | Up | +0.0009 | Normal |
| 4 | Industrials | 12.7% | 49/386 | 10.7% | Up | +0.0040 | Normal |
| 5 | Energy | 12.5% | 20/160 | 27.7% | Down | -0.0375 | Normal |
| 6 | Consumer Cyclical | 6.8% | 19/279 | 6.7% | Up | +0.0029 | Oversold |
| 7 | Financial | 6.4% | 37/577 | 9.9% | Down | -0.0070 | Oversold |
| 8 | Basic Materials | 6.0% | 9/150 | 7.2% | Down | -0.0023 | Oversold |
| 9 | Consumer Defensive | 2.5% | 3/122 | 5.9% | Down | -0.0040 | Oversold |
| 10 | Real Estate | 0.7% | 1/134 | 1.6% | Down | -0.0007 | Oversold |
| 11 | Utilities | 0.0% | 0/76 | 1.2% | Down | -0.0013 | Oversold |

> **Note on Status vs Trend:**
> Status (Overbought/Normal/Oversold) reflects the ratio *level* relative to thresholds.
> Trend (Up/Down) reflects the *direction* of the 10-day MA slope.
> These can diverge:
> - **Overbought + Down** = high level but momentum rolling over (warning)
> - **Oversold + Up** = low level but momentum improving (potential recovery)
> - **Consumer Cyclical**: Oversold (6.8%) / Trend Up

---

## Recommended Actions

**Zone:** Cautious (Cautious-Upper)
**Exposure Guidance:** Defensive (30-60%)

- Significant cash allocation (40-70%)
- Only hold strongest leaders in uptrending sectors
- Tight stops on all positions
- Consider defensive sector allocation
- No new aggressive entries

---

## Methodology

This analysis uses Monty's Uptrend Ratio Dashboard data to assess market breadth health.
The dashboard tracks ~2,800 US stocks across 11 sectors, measuring the percentage in uptrends.

**5-Component Scoring System (0-100, higher = healthier):**

1. **Market Breadth (30%):** Overall uptrend ratio level and trend direction
2. **Sector Participation (25%):** Number of uptrending sectors and spread uniformity
3. **Sector Rotation (15%):** Cyclical vs Defensive vs Commodity balance
4. **Momentum (20%):** Slope direction, acceleration, and sector slope breadth
5. **Historical Context (10%):** Percentile rank in historical distribution

**Key Thresholds (Monty's Dashboard):** Overbought = 37%, Oversold = 9.7%

For detailed methodology, see `references/uptrend_methodology.md`.

---

**Disclaimer:** This analysis is for educational and informational purposes only. Not investment advice. Past patterns may not predict future outcomes. Conduct your own research and consult a financial advisor before making investment decisions.
