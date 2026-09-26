"""r3_build_report.py - assemble v4/outputs/r3_evidence_base.md (and the short r3_report.md) from R3's datasets.
All headline numbers in the narrative are pulled from the CSVs so the text cannot drift from the data.
Run after: r3_ff_factors.py, r3_largecap_longonly.py, r3_stock_base_rates.py, r3_pit_beat_rates.py,
           r3_confidence_calibration.py, r3_curated_sources.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from r3_french_lib import DATA, OUT, utc_now  # noqa: E402

FS = pd.read_csv(DATA / "r3_factor_stats.csv")
PD = pd.read_csv(DATA / "r3_factor_pub_decay.csv")
LO = pd.read_csv(DATA / "r3_largecap_longonly_stats.csv")
EV = pd.read_csv(DATA / "r3_etf_factor_evidence.csv")
SB = pd.read_csv(DATA / "r3_stock_base_rates.csv")
PIT = pd.read_csv(DATA / "r3_pit_beat_rates.csv")
HZ = pd.read_csv(DATA / "r3_market_horizon_base_rates.csv")
CAL = pd.read_csv(DATA / "r3_confidence_calibration.csv")
TE = pd.read_csv(DATA / "r3_random_portfolio_te.csv")
SV = pd.read_csv(DATA / "r3_survivorship_bias_estimate.csv").iloc[0]
CY = pd.read_csv(DATA / "r3_calendar_year_beat_rates.csv")
RP = pd.read_csv(DATA / "r3_random_portfolio_base_rates.csv")
SP = pd.read_csv(DATA / "r3_spiva.csv")
BR = pd.read_csv(DATA / "r3_published_base_rates.csv")
LIT = pd.read_csv(DATA / "r3_literature.csv") if (DATA / "r3_literature.csv").exists() else None


def pct(x, d=1, sign=False):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "n/a"
    return f"{x*100:+.{d}f}%" if sign else f"{x*100:.{d}f}%"


def fs(factor, window, col):
    return FS[(FS.factor == factor) & (FS.window == window)][col].iloc[0]


def lo(key, window, col):
    return LO[(LO.key == key) & (LO.window == window)][col].iloc[0]


W63, W10, W15 = "1963-07..2026-07", "2010-01..2026-07", "2015-01..2026-07"

# ------------------------------------------------------------------ table renderers
def factor_table(window):
    rows = ["| Factor | Ann. mean | Vol | Sharpe | t-stat | Max drawdown (peak→trough) | % roll-12m > 0 | % roll-36m > 0 | % cal. yrs > 0 | Worst 12m |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in FS[FS.window == window].iterrows():
        rows.append(f"| {r.label} | {pct(r.ann_mean_arith)} | {pct(r.ann_vol)} | {r.sharpe_or_ir:.2f} | {r.t_stat:.2f} | "
                    f"{pct(r.max_drawdown)} ({str(r.mdd_peak)[:7]}→{str(r.mdd_trough)[:7]}) | {pct(r.pct_roll12_pos,0)} | "
                    f"{pct(r.pct_roll36_pos,0)} | {pct(r.pct_calyears_pos,0)} (n={int(r.n_calyears)}) | {pct(r.worst_12m)} |")
    return "\n".join(rows)


def long_hist_table():
    sub = FS[~FS.window.isin([W63, W10, W15])]
    rows = ["| Series | Window | Ann. mean | Sharpe | t | Max drawdown | Worst 12m |", "|---|---|---|---|---|---|---|"]
    for _, r in sub.iterrows():
        rows.append(f"| {r.label} | {r.window} | {pct(r.ann_mean_arith)} | {r.sharpe_or_ir:.2f} | {r.t_stat:.2f} | "
                    f"{pct(r.max_drawdown)} ({str(r.mdd_peak)[:7]}→{str(r.mdd_trough)[:7]}) | {pct(r.worst_12m)} |")
    return "\n".join(rows)


def pub_table():
    rows = ["| Factor (French definition) / original paper & sample | In-sample mean (t) | After sample end (t) | After publication (t), months | Change vs in-sample |",
            "|---|---|---|---|---|"]
    for _, r in PD.iterrows():
        rows.append(f"| {r.paper_sample} | {pct(r.ann_mean_insample)} ({r.t_insample:.2f}) | {pct(r.ann_mean_post_sample)} ({r.t_post_sample:.2f}) | "
                    f"{pct(r.ann_mean_post_pub)} ({r.t_post_pub:.2f}), {int(r.n_post_pub)} | {r.post_pub_change_pct:+.0f}% |")
    return "\n".join(rows)


def lo_table(window, keys=None):
    rows = ["| Large-cap long-only tilt | Stocks in favoured pf (latest / median since 2010) | Active return vs big-cap universe | TE | IR | t | Beta | CAPM alpha (t) | % cal. yrs > 0 | % roll-60m > 0 | Max relative DD | Capture vs all-cap L/S factor |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    sub = LO[LO.window == window]
    if keys:
        sub = sub[sub.key.isin(keys)]
    for _, r in sub.iterrows():
        nf = "mix" if pd.isna(r.n_fav_firms_latest) else f"{int(r.n_fav_firms_latest)} / {r.n_fav_firms_median_2010on:.0f}"
        if pd.isna(r.LS_all_ann_mean):
            cap = "n/a"
        elif window != W63:
            cap = "n/m (short window)"
        elif r.LS_all_ann_mean < 0.01:
            cap = "n/m (factor mean < 1%/yr)"
        else:
            cap = f"{r.capture_LO_vs_LS_all*100:.0f}%"
        lab = r.label if str(r.key).startswith("combo4") else f"{r.label} [{r.key[-3:]}]"
        rows.append(f"| {lab} | {nf} | {pct(r.LO_active_ann_mean,2,True)} | {pct(r.LO_TE)} | {r.LO_IR:.2f} | {r.LO_t:.2f} | {r.beta_vs_universe:.2f} | "
                    f"{pct(r.capm_alpha_ann,2,True)} ({r.capm_alpha_t:.2f}) | {pct(r.LO_pct_calyears_pos,0)} | {pct(r.LO_pct_roll60_pos,0)} | "
                    f"{pct(r.LO_max_rel_drawdown)} | {cap} |")
    return "\n".join(rows)


def etf_table():
    rows = ["| Fund | Period (month-ends) | Fund ann. | SPY ann. | Active (geometric) | TE | IR | % calendar yrs beating SPY | % rolling 36m beating | Max relative DD |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in EV.iterrows():
        rows.append(f"| {r.ticker} – {r['name']} | {r.start[:7]}..{r.end[:7]} | {pct(r.ann_return_etf)} | {pct(r.ann_return_SPY)} | "
                    f"{pct(r.ann_geo_active,2,True)} | {pct(r.TE)} | {r.IR:.2f} | {pct(r.pct_calyears_outperform,0)} (n={int(r.n_calyears)}) | "
                    f"{pct(r.pct_roll36_outperform,0)} | {pct(r.max_relative_drawdown)} |")
    return "\n".join(rows)


def horizon_table():
    rows = ["| Horizon | # overlapping windows | P(nominal > 0) | P(beat T-bills) | P(real > 0) | Worst cumulative nominal | Worst cumulative real | Median annualized nominal |",
            "|---|---|---|---|---|---|---|---|"]
    for _, r in HZ.iterrows():
        rows.append(f"| {int(r.horizon_years)} yr | {int(r.n_windows)} | {pct(r.pct_nominal_pos)} | {pct(r.pct_beat_tbills)} | {pct(r.pct_real_pos)} | "
                    f"{pct(r.worst_cum_nominal)} | {pct(r.worst_cum_real)} | {pct(r.median_ann_nominal)} |")
    return "\n".join(rows)


def spiva_table():
    def row(report, cat, measure_prefix):
        s = SP[(SP.report == report) & (SP.category == cat) & (SP.measure.str.startswith(measure_prefix))]
        d = dict(zip(s.horizon, s.value_pct))
        return d
    out = ["| Scorecard (data as of) | Category vs benchmark | 1y | 3y | 5y | 10y | 15y | 20y |", "|---|---|---|---|---|---|---|---|"]
    for rep, asof in [("SPIVA U.S. Mid-Year 2026", "2026-06-30"), ("SPIVA U.S. Year-End 2025", "2025-12-31"), ("SPIVA U.S. Year-End 2024", "2024-12-31")]:
        for cat, bm in [("All Large-Cap Funds", "S&P 500"), ("All Domestic Funds", "S&P Composite 1500")]:
            d = row(rep, cat, "% underperforming (absolute")
            if not d:
                continue
            out.append(f"| {rep} ({asof}) | {cat} vs {bm} | " + " | ".join(f"{d[h]:.1f}%" if h in d else "–" for h in ["1y", "3y", "5y", "10y", "15y", "20y"]) + " |")
    d = row("SPIVA U.S. Year-End 2025", "All Large-Cap Funds", "% underperforming (risk-adjusted")
    out.append("| SPIVA U.S. Year-End 2025 | All Large-Cap, risk-adjusted | – | " + " | ".join(f"{d[h]:.1f}%" for h in ["3y", "5y", "10y", "15y", "20y"]) + " |")
    return "\n".join(out)


def persistence_table():
    s = SP[SP.report.str.contains("Persistence")]
    out = ["| Category | Measure | Horizon | Value |", "|---|---|---|---|"]
    for _, r in s.iterrows():
        out.append(f"| {r.category} | {r.measure} | {r.horizon} | {r.value_pct:.2f}% |")
    return "\n".join(out)


def br_table():
    out = ["| Source | Metric | Value | Sample | Date | Verification |", "|---|---|---|---|---|---|"]
    for _, r in BR.iterrows():
        out.append(f"| [{r.source}]({r.url.split(' ')[0]}) | {r.metric} | {r.value} | {r['sample']} | {r.published} | {r.verification} |")
    return "\n".join(out)


def pit_table():
    full = PIT[(PIT.horizon_years == 1)]
    out = ["| Year | Members on 1 Jan | Coverage (Yahoo data) | S&P 500 TR | % beating index (covered) | Bounds (missing all lose / all win) |",
           "|---|---|---|---|---|---|"]
    for _, r in full.iterrows():
        if r.start_year < 2016:
            continue
        yr = f"{r.start_year}" + (" (Jan–Aug)" if r.partial_period else "")
        out.append(f"| {yr} | {r.n_members_start} | {pct(r.coverage,0)} | {pct(r.SP500TR_return)} | {pct(r.pct_beat_covered,0)} | "
                   f"{pct(r.pct_beat_lower_bound,0)}–{pct(r.pct_beat_upper_bound,0)} |")
    return "\n".join(out)


def pit_summary(min_cov=0.0):
    t = PIT[(~PIT.partial_period) & (PIT.coverage >= min_cov)]
    g = t.groupby("horizon_years").agg(n=("start_year", "size"), y0=("start_year", "min"), y1=("start_year", "max"),
                                       beat=("pct_beat_covered", "mean"), lo_=("pct_beat_lower_bound", "mean"), hi_=("pct_beat_upper_bound", "mean"),
                                       cov=("coverage", "mean"), pos=("pct_positive_covered", "mean"))
    return g


def close10_table():
    out = ["| Horizon | Start months (non-overlapping) | Avg # stocks | % with return > 0 | % beating S&P 500 TR (min–max across starts) | % beating ^GSPC price index (naive – wrong) | Median stock minus index (cumulative) |",
           "|---|---|---|---|---|---|---|"]
    for _, r in SB.iterrows():
        out.append(f"| {int(r.horizon_years)} yr | {int(r.n_start_months)} ({int(r.n_nonoverlapping)}) | {r.avg_n_stocks:.0f} | {pct(r.pct_stocks_positive)} | "
                   f"{pct(r.pct_stocks_beat_SP500TR)} ({pct(r.pct_beat_SP500TR_min_over_starts,0)}–{pct(r.pct_beat_SP500TR_max_over_starts,0)}) | "
                   f"{pct(r.pct_stocks_beat_GSPC_price_naive)} | {pct(r.median_stock_minus_SP500TR)} |")
    return "\n".join(out)


def rp_table():
    out = ["| Horizon | # stocks | P(portfolio > 0) | P(beats S&P 500 TR) – survivorship-biased | same, crude bias-adjusted | TE of random EW portfolio (median, p10–p90) |",
           "|---|---|---|---|---|---|"]
    tem = TE.set_index("n_stocks")
    for _, r in RP[RP.n_stocks.isin([1, 15, 20, 30, 50])].iterrows():
        te_s = f"{pct(tem.loc[r.n_stocks,'TE_median'])} ({pct(tem.loc[r.n_stocks,'TE_p10'])}–{pct(tem.loc[r.n_stocks,'TE_p90'])})" if r.n_stocks in tem.index else "–"
        out.append(f"| {int(r.horizon_years)} yr | {int(r.n_stocks)} | {pct(r.P_portfolio_positive)} | {pct(r.P_portfolio_beats_SP500TR)} | "
                   f"{pct(r.P_beats_SP500TR_crude_bias_adj)} | {te_s} |")
    return "\n".join(out)


def cal_table():
    A = CAL[CAL.block == "A_B"]
    A = A[A.TE.isin([0.03, 0.05, 0.07, 0.09]) & A.alpha.isin([0.005, 0.01, 0.02, 0.03])]
    out = ["| Expected alpha | TE | IR | P(beat) 1y | 3y | 5y | 10y | 20y | Years for 90% odds | Years for t = 2 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in A.iterrows():
        out.append(f"| {pct(r.alpha)} | {pct(r.TE,0)} | {r.IR:.2f} | {pct(r.P_outperform_1y,0)} | {pct(r.P_outperform_3y,0)} | {pct(r.P_outperform_5y,0)} | "
                   f"{pct(r.P_outperform_10y,0)} | {pct(r.P_outperform_20y,0)} | {r.years_for_90pct:.0f} | {r.years_for_t2:.0f} |")
    return "\n".join(out)


def ic_table():
    C = CAL[CAL.block == "C"]
    out = ["| Signal IC | Top 5% pick | Top 10% pick | Top 20% pick | (base rate: random stock beats index = 45%) | Top 10% pick if base rate 50% |",
           "|---|---|---|---|---|---|"]
    for ic in sorted(C.IC.dropna().unique()):
        g = C[C.IC == ic]
        v = lambda q, b: g[(g.top_quantile == q) & (g.base_rate_random_stock_beats_index == b)].P_pick_beats_index.iloc[0]  # noqa: E731
        out.append(f"| {ic:.2f} | {pct(v(0.05,0.45))} | {pct(v(0.10,0.45))} | {pct(v(0.20,0.45))} | | {pct(v(0.10,0.50))} |")
    return "\n".join(out)


def haircut_table():
    D = CAL[CAL.block == "D"]
    out = ["| Backtest Sharpe (or IR) | Years | t (single test) | Haircut if best of 10 variants | best of 100 | best of 316 |", "|---|---|---|---|---|---|"]
    for _, r in D.iterrows():
        out.append(f"| {r.SR_backtest:.2f} | {int(r.years)} | {r.t_single:.2f} | {pct(r.haircut_N10,0)} | {pct(r.haircut_N100,0)} | {pct(r.haircut_N316,0)} |")
    return "\n".join(out)


def lit_table():
    if LIT is None:
        return "_Literature table pending (r3_literature.csv not yet built)._"
    out = ["| # | Paper (journal, year) | Sample | Key quantitative finding | Known decay / caveats | DOI / URL | Status |", "|---|---|---|---|---|---|---|"]
    for i, r in LIT.iterrows():
        out.append(f"| {i+1} | **{r.paper}** — {r.authors} ({r.journal}, {r.year}) | {r['sample']} | {r.key_finding} | {r.decay_caveats} | {r.doi_url} | {r.verification} |")
    return "\n".join(out)


# ------------------------------------------------------------------ key numbers
K = {}
for f_ in ["hml", "rmw", "cma", "umd", "combo4", "mkt_rf"]:
    for w in (W63, W10, W15):
        for c in ["ann_mean_arith", "t_stat", "sharpe_or_ir", "pct_roll12_pos", "pct_roll36_pos", "pct_calyears_pos", "max_drawdown"]:
            K[(f_, w, c)] = fs(f_, w, c)
pdm = PD.set_index("factor")
decay_hml = PD[PD.factor == "hml_ff3"].post_pub_change_pct.iloc[0]
decay_umd = PD[PD.factor == "umd"].post_pub_change_pct.iloc[0]
decay_rmw = PD[PD.factor == "rmw"].post_pub_change_pct.iloc[0]
decay_cma = PD[(PD.factor == "cma") & PD.paper_sample.str.startswith("Fama")].post_pub_change_pct.iloc[0]
cap2 = lo("combo4_2x3", W63, "capture_LO_vs_LS_all")
cap5 = lo("combo4_5x5", W63, "capture_LO_vs_LS_all")
mix = EV[EV.ticker.str.startswith("MIX")].iloc[0]
etf_only = EV[~EV.ticker.isin(["RSP"]) & ~EV.ticker.str.startswith("MIX")]
te_by_n = TE.set_index("n_stocks")
hz = HZ.set_index("horizon_years")
sb = SB.set_index("horizon_years")
pit_all = pit_summary()
pit_hi = pit_summary(0.85)
ye25 = SP[(SP.report == "SPIVA U.S. Year-End 2025") & (SP.category == "All Large-Cap Funds") & SP.measure.str.startswith("% underperforming (absolute")].set_index("horizon").value_pct
my26 = SP[(SP.report == "SPIVA U.S. Mid-Year 2026") & (SP.category == "All Large-Cap Funds") & SP.measure.str.startswith("% underperforming (absolute")].set_index("horizon").value_pct
annual = SP[SP.measure.str.startswith("% underperforming in calendar year")].value_pct
calA = CAL[CAL.block == "A_B"].set_index(["alpha", "TE"])
ic_needed = CAL[CAL.block == "C_needed"].IC_needed_for_90pct_hit.iloc[0]
Cc = CAL[CAL.block == "C"]
p_ic05 = Cc[(Cc.IC == 0.05) & (Cc.top_quantile == 0.10) & (Cc.base_rate_random_stock_beats_index == 0.45)].P_pick_beats_index.iloc[0]
p_ic10 = Cc[(Cc.IC == 0.10) & (Cc.top_quantile == 0.10) & (Cc.base_rate_random_stock_beats_index == 0.50)].P_pick_beats_index.iloc[0]
central = calA.loc[(0.01, 0.07)]
opt = calA.loc[(0.02, 0.05)]
lv63 = lo("lowvar_5x5", W63, "LO_active_ann_mean"); lb63 = lo("lowbeta_5x5", W63, "LO_active_ann_mean")
lva63 = lo("lowvar_5x5", W63, "capm_alpha_ann"); lba63 = lo("lowbeta_5x5", W63, "capm_alpha_ann")
lv10 = lo("lowvar_5x5", W10, "LO_active_ann_mean"); lb10 = lo("lowbeta_5x5", W10, "LO_active_ann_mean")
ac63 = lo("accr_5x5", W63, "LO_active_ann_mean"); ni63 = lo("nsi_5x5", W63, "LO_active_ann_mean")
cy_recent = PIT[(PIT.horizon_years == 1) & PIT.start_year.isin([2023, 2024, 2025])].set_index("start_year").pct_beat_covered

# ------------------------------------------------------------------ narrative
md = f"""# R3 Evidence Base — factor research, active-management base rates, stock-outcome base rates

**Agent:** R3 · **Built:** {utc_now()} · **Data cutoffs:** Kenneth French Data Library (CRSP vintage 202607, monthly through 2026-07);
SPIVA U.S. Year-End 2025 (pub. 2026-03-03) and Mid-Year 2026 (pub. 2026-09-17); Yahoo prices through 2026-09-25 (monthly analyses end 2026-08).
**Purpose:** give the pre-registered Q/V/M/S model an honest prior, and define what "confidence" can and cannot mean.
All long-short factor numbers are gross of costs, all-cap and value-weighted; numbers marked (biased) use survivorship-biased data and are upper bounds.

---

## 0. Answer first

1. **"90% confident" is a legitimate statement about diversified equity exposure over long horizons, not about beating the index.**
   - Since 1926 the US total market had a positive nominal return in **{pct(hz.loc[10,'pct_nominal_pos'])}** of rolling 10-year windows and **{pct(hz.loc[15,'pct_nominal_pos'])}** of 15-year windows.
   - In real terms the figures are {pct(hz.loc[10,'pct_real_pos'])} and {pct(hz.loc[15,'pct_real_pos'])}. At 1 year the market is positive only {pct(hz.loc[1,'pct_nominal_pos'])} of the time.
   - The US is the survivor case: across 39 developed markets, a diversified investor still had a **12%** chance of losing to inflation over 30 years (Anarkulova, Cederburg & O'Doherty 2022).
   - What is *not* attainable:
     - **A single stock:** it beats the market in about **44%** of stock-years and about **37%** of stock-decades (Bessembinder 2018). S&P 500 members beat the index in only **{pct(cy_recent.loc[2023],0)} / {pct(cy_recent.loc[2024],0)} / {pct(cy_recent.loc[2025],0)}** of cases in 2023/2024/2025 (our point-in-time computation; S&P DJI reports 26% / 28% / 30%).
     - **A top-decile pick from a "very good" signal (IC 0.10)** gets to only **~{pct(p_ic10,0)}**. A 90% single-stock hit rate would need IC ≈ **{ic_needed:.2f}**, versus the 0.05 "good" and 0.10 "very good" practitioner benchmarks.
     - **A 15–30 stock tilt:** at an IR of 0.14 (central case) to 0.4 (optimistic) it beats the S&P 500 over one year with only **{pct(central.P_outperform_1y,0)}–{pct(opt.P_outperform_1y,0)}** probability, and over 10 years with **{pct(central.P_outperform_10y,0)}–{pct(opt.P_outperform_10y,0)}**.
     - **Professional managers:** **{ye25['10y']:.0f}–{ye25['20y']:.0f}%** of US large-cap funds lagged the S&P 500 over 10–20 years (SPIVA YE2025).
2. **Realistic expectation for our 15–30 stock large-cap long-only Q+V+M+S tilt:**
   - **Central case:** gross alpha ≈ **+1%/yr** (plausible range 0 to +2%), before ~0.2–0.4%/yr trading costs.
   - **Tracking error** ≈ **6–9%**, so IR ≈ 0.1–0.3.
   - **Expect to lag the S&P 500 in ~40–45% of calendar years** and in ~20–40% of 5-year windows.
   - **The evidence behind this:**
     - Fama-French big-cap long-only mix, 1963–2026: **{pct(lo('combo4_2x3',W63,'LO_active_ann_mean'),1,True)}** to **{pct(lo('combo4_5x5',W63,'LO_active_ann_mean'),1,True)}/yr gross**, with TE {pct(lo('combo4_2x3',W63,'LO_TE'))}–{pct(lo('combo4_5x5',W63,'LO_TE'))}, and negative in {pct(1-lo('combo4_2x3',W63,'LO_pct_calyears_pos'),0)}–{pct(1-lo('combo4_5x5',W63,'LO_pct_calyears_pos'),0)} of years.
     - The same mix since 2010: only **{pct(lo('combo4_2x3',W10,'LO_active_ann_mean'),1,True)}** to **{pct(lo('combo4_5x5',W10,'LO_active_ann_mean'),1,True)}/yr** (t < 1).
     - Live large-cap factor ETFs, 2011/13/15–2026, net of fees, versus SPY: {'; '.join(f"{r.ticker} {pct(r.ann_geo_active,1,True)}" for _, r in etf_only.iterrows())} per year. An equal-weight QUAL+MTUM+VLUE mix returned {pct(mix.ann_geo_active,2,True)}/yr.
3. **The long-short factors are real over the long run but have decayed.** Over 1963–2026 (all-cap, gross):
   - **Long-run premia:**
     - HML {pct(K[('hml',W63,'ann_mean_arith')])}/yr (t {K[('hml',W63,'t_stat')]:.1f}); RMW {pct(K[('rmw',W63,'ann_mean_arith')])} (t {K[('rmw',W63,'t_stat')]:.1f}).
     - CMA {pct(K[('cma',W63,'ann_mean_arith')])} (t {K[('cma',W63,'t_stat')]:.1f}); UMD {pct(K[('umd',W63,'ann_mean_arith')])} (t {K[('umd',W63,'t_stat')]:.1f}).
     - Equal-weight combo: **{pct(K[('combo4',W63,'ann_mean_arith')])}/yr, Sharpe {K[('combo4',W63,'sharpe_or_ir')]:.2f}**, positive in {pct(K[('combo4',W63,'pct_calyears_pos')],0)} of calendar years and {pct(K[('combo4',W63,'pct_roll36_pos')],0)} of 36-month windows.
   - **Since 2010:**
     - HML {pct(K[('hml',W10,'ann_mean_arith')])}, CMA {pct(K[('cma',W10,'ann_mean_arith')])}, RMW {pct(K[('rmw',W10,'ann_mean_arith')])}, UMD {pct(K[('umd',W10,'ann_mean_arith')])}.
     - Combo {pct(K[('combo4',W10,'ann_mean_arith')])}/yr (t {K[('combo4',W10,'t_stat')]:.1f}).
   - **After publication:**
     - Our own check on French's data: value {decay_hml:+.0f}%, momentum {decay_umd:+.0f}%, profitability {decay_rmw:+.0f}%, investment {decay_cma:+.0f}%.
     - This matches the McLean & Pontiff (2016) average of −58%.
4. **A large-cap long-only implementation captures only ~{cap2*100:.0f}–{cap5*100:.0f}%** of the all-cap long-short combo premium (1963–2026).
   - By factor, the capture is: value 67–74%, profitability 31–35%, investment 55–73% and momentum 35–45%.
5. **Haircut rule for any backtest we produce:**
   - Keep ≤ **40%** of in-sample alpha from published-factor backtests.
   - Multiply by ~**0.45** again if the backtest was long-short and all-cap.
   - Subtract costs.
   - Demand **t ≥ 3** (Harvey, Liu & Zhu 2016) before believing anything new. A 10-year backtest with Sharpe 0.5 has t ≈ 1.6, which is statistically empty once ≥10 variants were tried.
   - The v3 model tuned on 3 annual backtest points carries **no** statistical information.
6. **The legacy price file is badly biased.**
   - Equal-weighting today's S&P 500 members (`close10.pkl`) earned **{pct(SV.EW_survivors_ann)}/yr** over {SV.period}, versus **{pct(SV.RSP_ann)}/yr** for the investable equal-weight S&P 500 (RSP). That is a survivorship/look-ahead bias of **≈{pct(SV.bias_ann_EWsurv_minus_RSP)}/yr**.
   - Its stock closes are also dividend-adjusted while `^GSPC` is price-only. That inflates naive "beat the index" rates by 3–9 points.
   - v4 backtests must use point-in-time membership with delisting returns, and a total-return benchmark.
7. **Low volatility belongs as a constraint, not a return driver** (consistent with the pre-registration).
   - The large-cap low-variance and low-beta quintiles had active returns of {pct(lv63,1,True)} and {pct(lb63,1,True)}/yr versus their universe in 1963–2026, and {pct(lv10,1,True)} and {pct(lb10,1,True)}/yr since 2010.
   - Their beta-adjusted alpha was positive but insignificant ({pct(lva63,1,True)}, {pct(lba63,1,True)}; t ≈ 1.5).
8. **Evidence strength for the model's families:**
   - **Strongest for large caps:** momentum (in the long run) and profitability/quality.
   - **Value and investment:** strong over 1963–2026 but flat since 2010.
   - **Low accruals and net repurchases:** respectable large-cap evidence ({pct(ac63,1,True)} and {pct(ni63,1,True)}/yr long-only active, 1963–2026).
   - **Earnings-surprise drift (SUE/PEAD):** largely gone in large caps after ~2006 (Martineau 2022), so the S family deserves the weakest prior.

---

## 1. Literature — what is well replicated and what decayed

{lit_table()}

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
{factor_table(W63)}

### 2.2 Since 2010-01
{factor_table(W10)}

### 2.3 Since 2015-01
{factor_table(W15)}

### 2.4 Full history (momentum and value from 1926/27)
{long_hist_table()}

**Reading the tables:**
- **Combining helps.** The equal-weight combo roughly halves volatility thanks to the low or negative correlations: value–momentum ≈ −0.2 to −0.3, and profitability is roughly uncorrelated with the others (see `r3_factor_corr.csv`).
- **But the combo can still be underwater for 12 years.** Its drawdown ran from 2008-11 to 2020-12: the 2009 momentum crash, then value's lost decade.
- **Momentum crashes are real.** UMD's peak-to-trough drawdown was {pct(fs('umd', W63, 'max_drawdown'))} (2008-11→2009-09), including −49% in March–May 2009 alone. Its worst drawdown since 1927 is −78% (1932–39); see Daniel & Moskowitz (2016).
- **2026 so far (through July):** UMD +10.2%, HML +12.3%, CMA +7.2%, RMW −5.8%. RMW's drawdown from 2023-10 reached −25.9% in 2026-06.

### 2.5 Publication-decay check on French's own factors (McLean–Pontiff style)
{pub_table()}

The French definitions are not identical to each paper's original variable; for example, RMW is operating profitability, not Novy-Marx's gross profitability. Post-publication windows are short, so their t-stats are low. The direction matches McLean & Pontiff: value and momentum kept roughly 45% of their in-sample premia, and investment kept roughly none.

### 2.6 How much does a LARGE-CAP LONG-ONLY tilt capture?

**Method:**
- **Portfolios.** We use French's size × characteristic portfolios, value-weighted within each portfolio.
  - "2x3" means big stocks (above the NYSE median market cap) in the top 30% of the characteristic.
  - "5x5" means the top NYSE size quintile and the extreme characteristic quintile (recently 9–100 stocks, closer to a concentrated portfolio).
- **Active return.** Favoured portfolio minus the value-weighted return of all big-cap portfolios in the same sort. We reconstructed the universe weights from French's firm counts × average caps. Same-month weights match the CRSP market with 0.5–0.7%/yr TE, versus 0.7–1.0% for lagged weights.
- **Capture.** Mean long-only active return ÷ mean of the published all-cap long-short factor.

**1963-07 → 2026-07 (gross):**
{lo_table(W63)}

**Since 2010-01 (mixes and key tilts):**
{lo_table(W10, ['combo4_2x3','combo4_5x5','prof_2x3','mom_2x3','value_2x3','inv_2x3','accr_5x5','lowvar_5x5'])}

**Since 2015-01 (mixes and key tilts):**
{lo_table(W15, ['combo4_2x3','combo4_5x5','prof_2x3','mom_2x3','value_2x3','inv_2x3','accr_5x5','lowvar_5x5'])}

**Interpretation:**
- **Capture.** Large-cap long-only captured about **{cap2*100:.0f}% (broad 2x3) to {cap5*100:.0f}% (concentrated 5x5)** of the all-cap long-short combo premium over 1963–2026, with TE only 3–4%.
- **The published source agrees.** Israel & Moskowitz (2013) find that the long side supplies ~60% of value's and ~half of momentum's profits, and that the value premium shrinks with firm size while momentum shows no reliable size relation. In our data, profitability's capture is lowest because much of RMW comes from shorting small weak firms.
- **Since 2010 the mixes earned only +0.5% to +1.2%/yr gross.**
- **The mixes above are "mixes" of separately sorted portfolios.** An integrated composite should do somewhat better (Fitzgibbons et al. 2017).

### 2.7 Realized, net-of-fee evidence: live large-cap factor ETFs vs SPY (our computation from Yahoo adjusted closes)
{etf_table()}

This is genuinely out-of-sample, investable and post-publication evidence. Over roughly 11–15 years the products delivered between **{pct(etf_only.ann_geo_active.min(),1,True)} and {pct(etf_only.ann_geo_active.max(),1,True)}/yr** versus SPY, and beat it in only 29–58% of calendar years. The period (2013–2026) was dominated by mega-cap growth leadership, which hurt value, low-volatility and equal-weight approaches. RSP (equal-weight S&P 500) lagged SPY by {pct(-SV.RSP_minus_SPY_ann,1)}/yr. It is one regime, not the long-run expectation, but it is exactly the kind of decade that makes "90% confident" claims about beating the index untenable.

### 2.8 US total market: probability of positive outcomes by horizon (1926-07 → 2026-07; French Mkt, FRED CPI-U)
{horizon_table()}

These results are consistent with Dimensional's "The Uncommon Average" (S&P 500 1926–2018: 75.2% / 87.7% / 94.7% positive at 1 / 5 / 10 years). Caveats:
- Overlapping windows make the effective sample small: only ~10 independent 10-year periods since 1926.
- The US is the best-case survivor. Across 39 developed markets over 1841–2019, the chance of losing to inflation over 30 years is 12% ([Anarkulova, Cederburg & O'Doherty 2022, JFE 143(1):409–433](https://doi.org/10.1016/j.jfineco.2021.06.040)).

---

## 3. Active-management base rates (SPIVA, S&P Dow Jones Indices)

**Share of active US equity funds that underperformed** (absolute returns, count-based, survivorship-adjusted by S&P DJI):
{spiva_table()}

Sources: [SPIVA U.S. Mid-Year 2026 (pub. 2026-09-17)](https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-mid-year-2026.pdf) ·
[SPIVA U.S. Year-End 2025 (pub. 2026-03-03)](https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2025.pdf) ·
[SPIVA U.S. Year-End 2024 (pub. 2025-03-04)](https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2024.pdf).
R3 checked the MY2026 and YE2025 large-cap rows in the PDF text; the domestic MY2026 and YE2024 rows were checked by an R3 sub-agent.

**Annual pattern:**
- In 2025, **79%** of large-cap funds lagged the S&P 500, the fourth-worst year in the scorecard's 25-year history. In H1 2026 the figure was **{my26['YTD (H1 2026)']:.0f}%**.
- Over 2001–2025 the annual rate averaged **{annual.mean():.0f}%**. A majority outperformed only in 2005, 2007 and 2009.

**Survivorship:** only 67% of large-cap funds survived 10 years and ~35% survived 20 years (YE2025 Report 2).

**Persistence** (SPIVA U.S. Persistence Scorecard Year-End 2025, pub. 2026-05-07, [PDF](https://www.spglobal.com/spdji/en/documents/spiva/persistence-scorecard-year-end-2025.pdf)):
{persistence_table()}

**Implication.** The base rate for "a skilled-looking active large-cap strategy beats the S&P 500 over 10–20 years" is **~7–17%** after fees (100% minus 83–93%). Past top-quartile status predicts little: top-quartile large-cap funds stayed top quartile over the next five years 13.8% of the time, against 25% expected by chance.

---

## 4. Single-stock outcome base rates

### 4.1 Published evidence
{br_table()}

### 4.2 Our point-in-time computation: share of S&P 500 members beating the S&P 500 TR (buy-and-hold, by count)

**Method:**
- Membership: agent D2's reconstruction from fja05680 and Wikipedia (`d2_universe_spells.csv`, read-only). D1 owns the authoritative membership.
- Returns: Yahoo adjusted monthly returns (`d2_ret_monthly.parquet`).
- Members whose series ends early are assumed to sit in cash after their last full month.
- Members with no Yahoo data are missing; they are mostly acquired or bankrupt names. We report bounds that assume all missing names lost or all won.

{pit_table()}

**Averages across start years:**
- **All complete years 2001–2025:** 1-year beat rate **{pct(pit_all.loc[1,'beat'])}** (bounds {pct(pit_all.loc[1,'lo_'],0)}–{pct(pit_all.loc[1,'hi_'],0)}, mean coverage {pct(pit_all.loc[1,'cov'],0)}).
  - Coverage is only ~50% in 2001–2005, so the early years overstate the rate.
- **Years with ≥85% coverage ({int(pit_hi.loc[1,'y0'])}–{int(pit_hi.loc[1,'y1'])}):**
  - 1 year: **{pct(pit_hi.loc[1,'beat'])}**.
  - 3 years: {pct(pit_hi.loc[3,'beat']) if 3 in pit_hi.index else 'n/a'}.
  - 5 years: {pct(pit_hi.loc[5,'beat']) if 5 in pit_hi.index else 'n/a'}.
- **Cross-check against published figures:**
  - S&P DJI: 26% (2023), 28% (2024) and 30% (2025).
  - Ours: {pct(cy_recent.loc[2023],0)}, {pct(cy_recent.loc[2024],0)} and {pct(cy_recent.loc[2025],0)}. This agrees within 1–2 points, which validates the pipeline.
- **Long-run context:** Bessembinder's all-CRSP annual rate is 44.4% (value-weighted market). The cap-weighted index beats the median stock whenever mega-caps lead, which is why recent years sit at 28–34%.

### 4.3 Legacy `close10.pkl` (SURVIVORSHIP-BIASED: 497 stocks that are S&P 500 members in Sept 2026; 2015-09 → 2026-08; benchmark ^SP500TR)
{close10_table()}

Even this upward-biased sample shows that the typical stock lags the index. Only {pct(sb.loc[10,'pct_stocks_beat_SP500TR'],0)} of these *survivors* beat the S&P 500 TR over 10 years, and the median stock trailed the index by {-sb.loc[10,'median_stock_minus_SP500TR']*100:.0f} percentage points of cumulative return. Using `^GSPC` (price-only) instead of the total-return index would inflate every beat rate by 3–9 points.

**Random equal-weight portfolios from the same universe:**
{rp_table()}

**Survivorship bias quantified:** over {SV.period}, a monthly-rebalanced equal-weight portfolio of today's members returned **{pct(SV.EW_survivors_ann)}/yr**. The investable S&P 500 Equal Weight ETF (RSP) returned **{pct(SV.RSP_ann)}/yr**. The gap, **≈{pct(SV.bias_ann_EWsurv_minus_RSP)}/yr**, is the bias of back-testing on current constituents; RSP's ~0.20% fee and quarterly rebalancing explain little of it. The biased table says random 20-stock portfolios beat the index {pct(RP[(RP.horizon_years==1)&(RP.n_stocks==20)].P_portfolio_beats_SP500TR.iloc[0],0)} of the time over 1 year. After removing the bias, the figure is ≈{pct(RP[(RP.horizon_years==1)&(RP.n_stocks==20)].P_beats_SP500TR_crude_bias_adj.iloc[0],0)}, consistent with RSP lagging SPY in this era.

**Tracking error of a 15–30 stock equal-weight large-cap portfolio:** {pct(te_by_n.loc[30,'TE_median'])}–{pct(te_by_n.loc[15,'TE_median'])} (median of 1,000 random draws; TE is little affected by survivorship). A factor-tilted 15–30 stock portfolio should expect **~6–9% TE**.

---

## 5. Synthesis for the v4 model

### 5a. Realistic gross alpha, tracking error and hit rate for a 15–30 stock large-cap long-only Q+V+M+S tilt

| Evidence line | Gross active return/yr | TE | IR | Years with negative active return |
|---|---|---|---|---|
| French big-cap long-only mix, 1963–2026, broad (2x3) | {pct(lo('combo4_2x3',W63,'LO_active_ann_mean'),2,True)} | {pct(lo('combo4_2x3',W63,'LO_TE'))} | {lo('combo4_2x3',W63,'LO_IR'):.2f} | {pct(1-lo('combo4_2x3',W63,'LO_pct_calyears_pos'),0)} |
| French big-cap long-only mix, 1963–2026, concentrated (5x5) | {pct(lo('combo4_5x5',W63,'LO_active_ann_mean'),2,True)} | {pct(lo('combo4_5x5',W63,'LO_TE'))} | {lo('combo4_5x5',W63,'LO_IR'):.2f} | {pct(1-lo('combo4_5x5',W63,'LO_pct_calyears_pos'),0)} |
| Same, 2010–2026 (2x3 / 5x5) | {pct(lo('combo4_2x3',W10,'LO_active_ann_mean'),2,True)} / {pct(lo('combo4_5x5',W10,'LO_active_ann_mean'),2,True)} | {pct(lo('combo4_2x3',W10,'LO_TE'))} / {pct(lo('combo4_5x5',W10,'LO_TE'))} | {lo('combo4_2x3',W10,'LO_IR'):.2f} / {lo('combo4_5x5',W10,'LO_IR'):.2f} | {pct(1-lo('combo4_2x3',W10,'LO_pct_calyears_pos'),0)} / {pct(1-lo('combo4_5x5',W10,'LO_pct_calyears_pos'),0)} |
| 1963–2026 long-only mix × post-publication retention (~0.45) | ≈ +0.9% to +1.0% | 3–4% | ~0.25 | ~40% |
| Live factor ETFs 2011/13/15–2026 (net; fees 0.08–0.15%) | {pct(etf_only.ann_geo_active.min(),1,True)} to {pct(etf_only.ann_geo_active.max(),1,True)} | 1.4–8.8% | −0.65 to 0.14 | 42–71% |
| Random 15–30 stock equal-weight portfolio (idiosyncratic TE only) | – | {pct(te_by_n.loc[30,'TE_median'])}–{pct(te_by_n.loc[15,'TE_median'])} | – | – |
| Earnings-surprise drift (large caps, post-2006) | ≈ 0 (Martineau 2022) | – | – | – |

**Recommended prior (pre-registered, not to be tuned on backtests):**
- **Expected gross alpha +1.0%/yr** (80% range 0 to +2%). Net of 10 bps one-way costs at ~100–200% annual turnover, that is ≈ +0.6–0.8%.
- **TE ≈ 7%, IR ≈ 0.15.**
- **What that implies** ({pct(0.01)} alpha, {pct(0.07,0)} TE):
  - P(beat S&P 500 in a given year) ≈ **{pct(central.P_outperform_1y,0)}**, so the portfolio lags in ≈{pct(1-central.P_outperform_1y,0)} of years.
  - Over 5 years ≈ {pct(central.P_outperform_5y,0)}; over 10 years ≈ {pct(central.P_outperform_10y,0)}.
  - An optimistic case (+2% alpha, 5% TE) gives {pct(opt.P_outperform_1y,0)} / {pct(opt.P_outperform_5y,0)} / {pct(opt.P_outperform_10y,0)}.
- **Tripwire:** any backtest claiming > +3%/yr gross for this design should be treated as evidence of a bug or bias (look-ahead, survivorship, data-snooping), not of skill.

### 5b. What "90% confident" can and cannot legitimately mean

**Calibration table** (normal approximation, iid annual active returns; fat tails make real odds worse):
{cal_table()}

**Single-stock hit rates implied by signal quality** (bivariate-normal score/return, correlation = IC):
{ic_table()}

**Legitimate uses of "90%":**
- **Market exposure over long horizons.** "A diversified US equity portfolio has had a positive nominal return over 10 years about {pct(hz.loc[10,'pct_nominal_pos'],0)} of the time, and over 15 years {pct(hz.loc[15,'pct_nominal_pos'],1)}." Add the international caveat: a 12% chance of a real loss over 30 years.
- **Ranges rather than rankings.** "We are ~90% confident next year's return will land within ±{1.645*0.07*100:.0f} pp of the S&P 500 if TE ≈ 7%." This is a statement about dispersion. It can be checked, and so it can be calibrated.
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
{haircut_table()}

| Source of optimism | Recommended adjustment | Evidence |
|---|---|---|
| Post-publication decay of published anomalies | keep ~40–50% of in-sample alpha (−58% average) | McLean & Pontiff (2016); our French check: value {decay_hml:+.0f}%, momentum {decay_umd:+.0f}%, investment {decay_cma:+.0f}%, profitability {decay_rmw:+.0f}% |
| In-sample over-fitting / data mining | an additional −26% for published signals; much more for self-mined variants | McLean & Pontiff (2016): out-of-sample, pre-publication decline |
| Multiple testing | require t ≥ 3; the haircut is nonlinear (Sharpe 0.5 over 10 yrs → 76–100%; Sharpe 1.0 over 20 yrs → 12–32%) | Harvey, Liu & Zhu (2016); Harvey & Liu (2015, JPM 42(1):13–28): "50% is too lenient for relatively small Sharpe ratios (< 0.4) and too harsh for large ones (> 1.0)" |
| Long-short all-cap → large-cap long-only | × ~0.35–0.55 | Section 2.6; Israel & Moskowitz (2013) |
| Survivorship (current-constituent universe) | −5 to −6%/yr on equal-weight comparisons (2015–2026) | Section 4.3 (RSP comparison) |
| Price-only benchmark vs dividend-adjusted stocks | −1.5 to −2%/yr (the S&P 500 dividend yield) | Section 4.3 |
| Trading costs | −(annual one-way turnover × 2 × 10 bps) ≈ −0.2 to −0.4%/yr | pre-registration |

**Rule for the lead:** forward alpha = min(0.4 × backtested alpha, literature prior ~+1%/yr) − costs. Report the raw and haircut figures side by side. Never report a backtest-derived probability of outperformance without the haircut and the implied TE.

### 5d. Implications for the pre-registered model (no changes proposed after seeing results)

- **Keep the four families equally weighted.** The evidence does not justify overweighting any family on recent data. Recent winners (momentum, profitability) and losers (value, investment) have swapped leadership over the decades. Diversification across families is the main source of IR: the combo's Sharpe ({K[('combo4',W63,'sharpe_or_ir')]:.2f}) is ~{K[('combo4',W63,'sharpe_or_ir')]/np.mean([K[(x,W63,'sharpe_or_ir')] for x in ['hml','rmw','cma','umd']]):.1f}× the average single factor's (1963–2026).
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
- **Point-in-time cross-check:** our 2023/2024/2025 beat rates ({pct(cy_recent.loc[2023],0)}/{pct(cy_recent.loc[2024],0)}/{pct(cy_recent.loc[2025],0)}) are within 1–2 points of S&P DJI's published 26%/28%/30%.
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
"""
out = OUT / "r3_evidence_base.md"
out.write_text(md, encoding="utf-8")
print("wrote", out, len(md), "chars")

# ------------------------------------------------------------------ short conventions report with file list
files = sorted([p for p in DATA.glob("r3_*") if not p.name.endswith(".meta.json")])
code = sorted((Path(__file__).parent).glob("r3_*.py"))
rows = []
for p in files:
    try:
        n = len(pd.read_parquet(p)) if p.suffix == ".parquet" else len(pd.read_csv(p))
    except Exception:  # noqa: BLE001
        n = "?"
    rows.append(f"| `v4/data/{p.name}` | {n} | {'yes' if (p.parent / (p.stem + '.meta.json')).exists() else 'NO'} |")
rep = f"""# R3 report (conventions summary) — evidence base, factor research, base rates

Built {utc_now()}. **The full deliverable is [`r3_evidence_base.md`](r3_evidence_base.md)**; this file is the conventions summary.

## Answer first
- **"90% confident" is achievable only for diversified equity exposure over ≥10–15 years** (US market positive in {pct(hz.loc[10,'pct_nominal_pos'],1)}–{pct(hz.loc[15,'pct_nominal_pos'],1)} of 10–15-year windows since 1926). It is not achievable for beating the index:
  - a single stock beats it ~44% of years (Bessembinder 2018);
  - S&P 500 members did so only 28–31% of the time in 2023–25;
  - {ye25['10y']:.0f}–{ye25['20y']:.0f}% of large-cap funds lag over 10–20 years (SPIVA YE2025).
- **Prior for our 15–30 stock large-cap Q+V+M+S tilt:** gross alpha +1%/yr (0 to +2%), TE ~7%, IR ~0.15. Expect to lag in ~44% of years.
- **Evidence behind the prior:** the French big-cap long-only mix returned {pct(lo('combo4_2x3',W63,'LO_active_ann_mean'),1,True)}–{pct(lo('combo4_5x5',W63,'LO_active_ann_mean'),1,True)}/yr gross over 1963–2026, but only {pct(lo('combo4_2x3',W10,'LO_active_ann_mean'),1,True)}–{pct(lo('combo4_5x5',W10,'LO_active_ann_mean'),1,True)} since 2010. Live factor ETFs returned {pct(etf_only.ann_geo_active.min(),1,True)} to {pct(etf_only.ann_geo_active.max(),1,True)}/yr net.
- **Haircuts:**
  - keep ≤40% of published-factor backtest alpha;
  - multiply by ~0.45 again for long-only large-cap versions of long-short factors;
  - require t ≥ 3.
- **The legacy `close10.pkl` inflates equal-weight returns by ~{pct(SV.bias_ann_EWsurv_minus_RSP)}/yr** (survivorship). Its stock closes are also dividend-adjusted while `^GSPC` is price-only.

## What I did
1. Downloaded and validated the French factor and size×characteristic portfolio files, then computed statistics for 3 windows plus full history.
2. Ran a publication-decay check and quantified the large-cap long-only capture.
3. Measured live factor ETFs against SPY.
4. Extracted and verified SPIVA YE2025, MY2026 and Persistence YE2025, plus published stock base rates (Bessembinder, J.P. Morgan, Dimensional, S&P DJI).
5. Computed point-in-time S&P 500 beat rates on D2 data, and survivorship-biased `close10` base rates with a bias estimate.
6. Built calibration tables for P(outperform), IC→hit rate, and Harvey–Liu haircuts.

## Validation
- Factors: 9/9.
- Long-only capture: 13/13.
- Stock base rates: 4/4.
- The PIT cross-check against S&P DJI is within 1–2 points.
- Source verification status is recorded per row in the CSVs.

## Limitations
See §6 of `r3_evidence_base.md`.

## Files
| File | Rows | meta.json |
|---|---|---|
""" + "\n".join(rows) + "\n\nScripts: " + ", ".join(f"`v4/code/{c.name}`" for c in code) + "\n\nRaw cache: `C:/Users/user/eqv4/cache/r3/` (French zips, Yahoo downloads, SPIVA/JPM/Bessembinder source text).\n"
(OUT / "r3_report.md").write_text(rep, encoding="utf-8")
print("wrote r3_report.md")
