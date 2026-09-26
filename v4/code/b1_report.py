"""b1_report.py - writes v4/outputs/b1_report.md from b1_results.json and the B1 tables."""
from __future__ import annotations

import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b1_common import DATA, OUT, FIRST_FORMATION  # noqa: E402


def pc(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{100 * x:.{d}f}%"


def f2(x, d=2):
    return "n/a" if x is None else f"{x:.{d}f}"


def missing_names_by_era(P):
    u = pd.read_csv(DATA / "d2_universe.csv")
    u["ticker"] = u.ticker.str.upper().str.replace(".", "-", regex=False)
    nm = u.set_index("ticker")[["current_name", "wiki_names"]]
    miss = P[~P.in_universe & (P.month_end >= "2009-12-31")]
    eras = {"2010-11 (exploratory)": ("2009-12-31", "2011-12-29"), "2012-14": ("2011-12-30", "2014-12-31"),
            "2015-19": ("2015-01-01", "2019-12-31"), "2020-26": ("2020-01-01", "2026-09-30")}
    out = {}
    for e, (a, z) in eras.items():
        m = miss[(miss.month_end >= a) & (miss.month_end <= z)]
        top = m.groupby("ticker").size().sort_values(ascending=False).head(12)
        items = []
        for t, n in top.items():
            name = nm.current_name.get(t) if t in nm.index else None
            if not isinstance(name, str) and t in nm.index and isinstance(nm.wiki_names.get(t), str):
                name = nm.wiki_names.get(t).split("|")[0].strip()
            items.append(f"{t} ({name if isinstance(name, str) else '?'}; {n} mo)")
        out[e] = items
    return out


def phase_b_sections(r, w):
    pb = r["phase_b"]
    V = pb["variants"]
    w("## Phase B — variants, plateaus, legacy replications, bias, robustness\n")
    w("**All variants (net, 2012-01…2026-08 unless noted; none selected on results):**\n")
    w("| Strategy | CAGR | Vol | MaxDD (m) | Excess vs SPY | t | Excess vs PIT EW | t | Turnover 1-way/yr | Avg names |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for x in pb["variants_table"]:
        w(f"| {x['strategy']} | {pc(x['cagr'])} | {pc(x['vol'])} | {pc(x['mdd_m'])} | {pc(x['ex_spy'])} | {f2(x['t_spy'])} | "
          f"{pc(x['ex_ew'])} | {f2(x['t_ew'])} | {f2(x.get('turnover_1w_yr'))} | {f2(x.get('avg_names'), 0)} |")
    w("")
    d5 = pb["dirichlet_500"]
    w(f"**Plateau test — 500 Dirichlet(alpha=5) family weightings, top-30 monthly net:** excess CAGR vs SPY p5/p50/p95 = "
      f"{pc(d5['excess_cagr_vs_spy_q']['0.05'])} / {pc(d5['excess_cagr_vs_spy_q']['0.5'])} / {pc(d5['excess_cagr_vs_spy_q']['0.95'])} "
      f"({pc(d5['share_positive_vs_spy'], 0)} of draws positive); vs PIT EW {pc(d5['excess_cagr_vs_ew_q']['0.05'])} / "
      f"{pc(d5['excess_cagr_vs_ew_q']['0.5'])} / {pc(d5['excess_cagr_vs_ew_q']['0.95'])} ({pc(d5['share_positive_vs_ew'], 0)} positive). "
      f"Portfolio size (20/30/40/50), rebalance frequency (monthly/quarterly/annual) and the buffer rule all sit on the "
      f"same plateau: **a flat-to-negative one**. The only positive point estimate is momentum alone (family M top-30, "
      f"{pc(V['fam_M_top30']['vs_SPY']['excess_cagr'])} vs SPY, t {f2(V['fam_M_top30']['vs_SPY']['nw_t'])}) - not significant, "
      f"and not selectable after the fact.\n")
    mr = pb.get("membership_robustness", {})
    if "table" in mr:
        w("**Membership-source robustness (D1 CIK-level membership = primary; D2 fja05680 spells = sensitivity):**\n")
        w("| Membership | Strategy | CAGR | Excess vs SPY | t | Excess vs PIT EW | IC 1m | IC t | % members priced | % scored |")
        w("|---|---|---|---|---|---|---|---|---|---|")
        for x in mr["table"]:
            w(f"| {x['membership']} | {x['strategy']} | {pc(x['cagr'], 2)} | {pc(x['excess_vs_spy'], 2)} | {f2(x['t_vs_spy'])} | "
              f"{pc(x['excess_vs_pit_ew'], 2)} | {f2(x['ic_1m'], 4)} | {f2(x['ic_1m_t'])} | {pc(x['pct_members_priced'])} | {pc(x['pct_members_scored'])} |")
        w(f"\nLive composite rank Spearman D1 vs D2-spells: **{f2(mr['live_rank_spearman_d1_vs_d2'], 3)}**; live top-30 overlap "
          f"{mr['live_top30_overlap']}/30 (only D1: {', '.join(mr['only_d1']) or '-'}; only D2: {', '.join(mr['only_d2']) or '-'}). "
          f"Material difference (>0.5 pt CAGR or rank rho <0.97): **{'YES' if mr['material_difference'] else 'NO'}**.\n")
    wf = pb["walk_forward"]
    w("**Walk-forward (each calendar year out-of-sample; frozen rules; primary top-30 net):**\n")
    w("| Year | Top-30 | SPY | PIT EW | Excess vs SPY | Excess vs PIT EW |")
    w("|---|---|---|---|---|---|")
    for y in wf["years"]:
        w(f"| {y['year']} | {pc(y['top30'])} | {pc(y['SPY'])} | {pc(y['PIT_EW'])} | {pc(y['ex_spy'])} | {pc(y['ex_ew'])} |")
    w("")
    w(f"2014 onward: positive excess vs SPY in **{pc(wf['share_years_pos_vs_spy_2014on'], 0)}** of years, vs PIT EW in "
      f"{pc(wf['share_years_pos_vs_ew_2014on'], 0)}; worst three years vs SPY: "
      + ", ".join(f"{k} ({pc(v)})" for k, v in wf["worst3_vs_spy"].items()) +
      f". Majority-of-years rule vs SPY: **{'PASS' if wf['majority_years_positive_vs_spy_10bps'] else 'FAIL'}**.\n")
    cs = pb["cost_stress"]
    w("**Punishing the strategy (primary top-30):**\n")
    w("| Stress | CAGR | Excess vs SPY | t | Excess vs PIT EW | t | Share of years beating SPY |")
    w("|---|---|---|---|---|---|---|")
    for k, lab in (("20bps", "costs 20 bps (2x)"), ("25bps", "costs 25 bps"), ("30bps", "costs 30 bps (3x)"),
                   ("lag1_10bps", "1-month implementation lag, 10 bps")):
        x = cs[k]
        sy = x.get("share_years_pos_vs_spy")
        w(f"| {lab} | {pc(x['cagr'])} | {pc(x['vs_SPY']['excess_cagr'])} | {f2(x['vs_SPY']['nw_t'])} | "
          f"{pc(x['vs_PIT_EW']['excess_cagr'])} | {f2(x['vs_PIT_EW']['nw_t'])} | {pc(sy, 0) if sy is not None else '-'} |")
    rb = pb["robustness"]
    w("")
    w("| Robustness | CAGR | Excess vs SPY | t | Excess vs PIT EW | t |")
    w("|---|---|---|---|---|---|")
    for k, lab in (("exclude_2020_21", "exclude 2020-21"), ("drop_top5_contributors", "drop 5 largest contributors"),
                   ("start_2010_exploratory", "start 2010-01 (exploratory)"), ("costs_25bps", "25 bps costs")):
        x = rb[k]
        w(f"| {lab} | {pc(x['cagr'])} | {pc(x['vs_SPY']['excess_cagr'])} | {f2(x['vs_SPY']['nw_t'])} | "
          f"{pc(x['vs_PIT_EW']['excess_cagr'])} | {f2(x['vs_PIT_EW']['nw_t'])} |")
    w(f"\nDropped contributors (sum of w x (r - r_EW)): {rb['drop_top5_contributors'].get('dropped')}.\n")
    lg = pb["legacy"]
    w("**Legacy-model replications on the PIT infrastructure** (backtest3.py pillar formulas; v2 = Q.20 G.10 V.35 M.35; "
      "v1 = Q.25 G.18 V.20 M.14 R.23; v3 conviction proxy = handoff 9.3 loop 3):\n")
    w("| Model | CAGR | Excess vs SPY | t | Excess vs PIT EW | t | Avg names |")
    w("|---|---|---|---|---|---|---|")
    for k in ("v2_top30_monthly", "v2_topQ_monthly", "v2_top30_annual_sep", "v1_top30_monthly", "v1_topQ_monthly",
              "v1_top30_annual_sep", "v3_conviction_monthly", "v3_conviction_annual_sep"):
        x = lg[k]
        w(f"| {k} | {pc(x['cagr'])} | {pc(x['vs_SPY']['excess_cagr'])} | {f2(x['vs_SPY']['nw_t'])} | "
          f"{pc(x['vs_PIT_EW']['excess_cagr'])} | {f2(x['vs_PIT_EW']['nw_t'])} | {f2(x.get('avg_names'), 1)} |")
    w("\nv3 conviction proxy, 12-month buy-and-hold from late September (compare handoff 9.3: Sep-2024 28 picks, "
      "10.3%, 64% up, 39% beat S&P):\n")
    w("| Start | Picks | Avg fwd-12m | % up | % beat SPY | Universe % up | Universe avg |")
    w("|---|---|---|---|---|---|---|")
    for h in lg["v3_conviction_sep_hit_table"]:
        w(f"| {h['start']} | {h['picks']} | {pc(h['avg_fwd12'])} | {pc(h['pct_up'], 0)} | {pc(h['pct_beat_spy'], 0)} | "
          f"{pc(h['universe_pct_up'], 0)} | {pc(h['universe_avg'])} |")
    w("")
    bi = pb["bias"]
    w("**Bias quantification (same code, same dates; 'today' = the 503 current constituents at every date = the v3 approach):**\n")
    w("| Test | Today's constituents | PIT membership | Bias (CAGR pts/yr) |")
    w("|---|---|---|---|")
    w(f"| Primary top-30 (net) | {pc(bi['primary_top30']['today_cagr'])} | {pc(bi['primary_top30']['pit_cagr'])} | "
      f"**{pc(bi['primary_top30']['bias_cagr'])}** |")
    w(f"| Primary top-quintile (net) | {pc(bi['primary_topQ']['today_cagr'])} | {pc(bi['primary_topQ']['pit_cagr'])} | "
      f"{pc(bi['primary_topQ']['bias_cagr'])} |")
    w(f"| EW universe | {pc(bi['ew_universe']['today_cagr'])} | {pc(bi['ew_universe']['pit_cagr'])} | "
      f"{pc(bi['ew_universe']['today_minus_pit'])} (RSP {pc(bi['ew_universe']['rsp_cagr'])}) |")
    for k, v in bi.items():
        if k.startswith("momentum_top50"):
            w(f"| {k.replace('_', ' ')} | {pc(v['today_cagr'])} | {pc(v['pit_cagr'])} | **{pc(v['bias_cagr'])}** |")
    w("")
    w(f"Today's-constituents excess vs SPY for the primary top-30 would have been {pc(bi['primary_top30']['today_excess_vs_spy'])}/yr "
      f"(vs {pc(bi['primary_top30']['pit_excess_vs_spy'])} PIT): the v3-style test manufactures a positive result out of a "
      f"negative one. (Today's top-30 and today's EW universe end with the same terminal wealth to 5 digits - checked: "
      f"different monthly paths, correlation 0.92 - a coincidence.)\n")
    rs = bi["residual_survivorship_pit_ew_vs_rsp"]
    w(f"**Residual survivorship (PIT EW - RSP):** mean {pc(rs['ann_mean_gap'])}/yr (NW t {f2(rs['nw_t'])}), CAGR gap "
      f"{pc(rs['cagr_gap'])}, PIT above RSP in {pc(rs['share_years_pit_above_rsp'], 0)} of years. {rs['interpretation']}\n")
    w("| Year | PIT EW | RSP | Gap | Today EW |")
    w("|---|---|---|---|---|")
    for y in rs["by_year"]:
        w(f"| {y['year']} | {pc(y['PIT_EW'])} | {pc(y['RSP'])} | {pc(y['PIT_minus_RSP'])} | {pc(y.get('TODAY_EW'))} |")
    w("")
    w(f"**Delisting treatment:** {pb['delisting']['note']} (top-30 holding-months without a next price: "
      f"{pb['delisting']['top30_holding_months_without_next_price']}).\n")
    ls = pb.get("lead_sleeve", {})
    if ls:
        w("**Lead's pre-fixed construction rule** (v4/code/lead_portfolio.py; quarter-end; composite rank among names with "
          "1y vol <= 45%; top-N with <=2 per SIC-4 and <=25% of names per sector; inverse-vol weights 3-8% with 25% sector "
          "weight cap via build_weights (caps never broken, residual = T-bill cash); held quarterly; 10 bps). Historical "
          "pending-deal exclusion cannot be applied (no PIT deal data):\n")
        w("| Construction | CAGR | daily MaxDD | Excess vs SPY | t | TE | Excess vs PIT EW | t | P(12m ex>0) | P(36m) | P(60m) | worst 12m rel. |")
        w("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for k, v in ls.items():
            if not (isinstance(v, dict) and "cagr" in v):
                continue
            w(f"| {k} | {pc(v['cagr'])} | {pc(v.get('mdd_daily'))} | {pc(v['vs_SPY']['excess_cagr'])} | {f2(v['vs_SPY']['nw_t'])} | "
              f"{pc(v['vs_SPY']['tracking_error'])} | {pc(v['vs_PIT_EW']['excess_cagr'])} | {f2(v['vs_PIT_EW']['nw_t'])} | "
              f"{pc(v['vs_SPY']['roll12_pos'], 0)} | {pc(v['vs_SPY']['roll36_pos'], 0)} | {pc(v['vs_SPY']['roll60_pos'], 0)} | "
              f"{pc(v.get('worst_12m_relative_vs_spy')) if v.get('worst_12m_relative_vs_spy') is not None else '-'} |")
        fm = ls.get("failed_member_sensitivity", {})
        for lab, v in fm.items():
            w(f"\nFailed-member sensitivity ({lab}): PIT EW CAGR {pc(v['pit_ew_cagr'], 2)} -> {pc(v['pit_ew_cagr_adj'], 2)} "
              f"({pc(v['delta_cagr'], 2)}/yr); top-30 excess vs adjusted PIT EW {pc(v['top30_excess_vs_adj_ew'], 2)}; "
              f"adjusted PIT EW - RSP {pc(v['pit_ew_adj_minus_rsp_cagr'], 2)}.")
        lv = ls.get("live_sleeve_2026-09-25", {})
        if lv:
            w("\nLive sleeve under the same rule (2026-09-25, pending-deal names excluded; a screen, not a forecast): "
              + ", ".join(f"{x['ticker']} {pc(x['weight'])}" for x in lv["names"]) + f"; cash {pc(lv['cash'])}.\n")
    di = pb.get("da2_fix_impact", {})
    if di and "n_live_top70_rank_changes" in di:
        w(f"**DA2 data-audit fixes** (BRK EPS /1500; EPS cells with |EPS|>$500 or >50x the row's median |EPS| set missing "
          f"before SUE is recomputed with D3's formula; APA revenue-based fields missing from 2021-03; ERIE Class-B share "
          f"count and share-count placeholders (<1% of trailing median) set missing): live top-70 rank changes "
          f"{di['n_live_top70_rank_changes']} (max |change| {f2(di['max_abs_rank_change_top70'], 0)}); entered top-70: "
          f"{di.get('entered_top70') or 'none'}; left: {di.get('left_top70') or 'none'}. HIG's live SUE/fam_S is unchanged "
          f"(its bad EPS cells are historical); HAL loses its SUE (bad quarters inside its 13-quarter window). Cell counts "
          f"are in the b1_panel meta (`da2_fixes`).\n")
    lf = pb.get("lineage_fix_impact", {})
    if lf and "what" in lf:
        w(f"**Lineage fix:** {lf['what']} Live top-70 rank changes: {lf['n_live_top70_rank_changes']} (max |change| "
          f"{f2(lf['max_abs_rank_change_top70'], 0)}); XOM live rank now {f2(lf.get('xom_live_rank_post'), 0)}.\n")
    be = pb["backtest_expert"]
    w("**backtest-expert evaluator (primary top-30):** " + be.get("mapping", "") + "\n")
    for mode in ("absolute_spell_return", "excess_vs_spy_spell_return"):
        x = be.get(mode, {})
        out_ = " ".join((x.get("stdout") or "").split())
        w(f"- {mode}: args `{x.get('args', '')[:170]}` -> {out_[:260]}")
    w("\nThe absolute mapping scores well only because long-only equity spells are usually positive (market beta); the "
      "excess mapping - the one that measures the model - flags negative expectancy. **Verdict: not deployable as an "
      "alpha source; at most a risk screen.**\n")


def main():
    r = json.load(open(OUT / "b1_results.json", encoding="utf-8"))
    P = pd.read_parquet(DATA / "b1_panel.parquet", columns=["month_end", "ticker", "in_universe", "entity"])
    S = r["strategies"]
    t30, tq, ew = S["primary_top30_ew"], S["primary_topquintile_ew"], S["pit_ew_universe"]
    L = []
    w = L.append
    phase = r.get("phase", "A")
    w(f"# B1 — Point-in-time factor backtest engine (Phase {phase})\n")
    w(f"_Agent B1 · generated {r['generated_utc']} · returns {r['sample']['first_return_month']} → "
      f"{r['sample']['last_return_month']} ({r['sample']['n_months']} months) · membership source: "
      f"**{r['membership_source']}**_\n")
    if "TEMPORARY" in r["membership_source"] or "D2_spells" in r["membership_source"]:
        w("> **Membership caveat:** D1's point-in-time membership files had not landed when this phase ran, so "
          "membership = D2's fja05680 + Wikipedia spell reconstruction (`d2_universe_spells.csv`), mapped to CIKs "
          "through D3/D1 ticker maps (not date-aware). Results will be re-run on D1's CIK-level membership.\n")
    w("## Answer first\n")
    a = t30["vs"]["SPY"]
    b = t30["vs"]["PIT_EW"]
    c = tq["vs"]["PIT_EW"]
    w(f"**No — on a point-in-time S&P 500 universe the pre-registered composite (Q+V+M+S, equal weights) has not "
      f"added value after costs over 2012-01…2026-08.**\n")
    w(f"- Primary **top-30 EW** (monthly, 10 bps/trade): CAGR **{pc(t30['net']['cagr'])}** vs SPY TR "
      f"{pc(S['bench_SPY']['net']['cagr'])} → excess **{pc(a['excess_cagr'])}/yr**, NW t = **{f2(a['nw_t'])}**, "
      f"95% CI of annualised mean excess [{pc(a['ci95_ann_mean_excess'][0])}, {pc(a['ci95_ann_mean_excess'][1])}]; "
      f"vs the PIT equal-weight universe {pc(b['excess_cagr'])}/yr (t = {f2(b['nw_t'])}).")
    w(f"- Primary **top-quintile EW**: CAGR {pc(tq['net']['cagr'])}; vs PIT EW {pc(c['excess_cagr'])}/yr "
      f"(t = {f2(c['nw_t'])}); vs SPY {pc(tq['vs']['SPY']['excess_cagr'])}/yr (t = {f2(tq['vs']['SPY']['nw_t'])}).")
    ls = S["q5_minus_q1_gross"]
    w(f"- Q5−Q1 (gross): {pc(ls['ann_mean'], 2)}/yr, NW t = {f2(ls['nw']['t'])}. Composite rank IC (1m) mean "
      f"{f2(r['ic']['composite_1m']['mean'], 4)} (NW t {f2(r['ic']['composite_1m']['nw_t'])}); 12m IC "
      f"{f2(r['ic']['composite_12m']['mean'], 4)} (t {f2(r['ic']['composite_12m']['nw_t'])}).")
    d = r["decile_table"]
    w(f"- Decile table is **not monotonic** (Spearman decile vs mean fwd-12m = {f2(d['spearman_decile_vs_fwd12'])}; "
      f"{d['n_increasing_steps_of_9']}/9 increasing steps; D10−D1 = {pc(d['d10_minus_d1_fwd12'])}).")
    w(f"- FF5+UMD alpha of top-30 (net, vs rf): {pc(r['ff5_umd_regression']['primary_top30_ew']['alpha_ann'])}/yr, "
      f"t = {f2(r['ff5_umd_regression']['primary_top30_ew']['alpha_t_nw'])} — the portfolio mostly loads on "
      f"known factors (UMD, RMW, SMB, HML all significant) that did not pay in large caps in this window.")
    w(f"- Risk: top-30 daily max drawdown **{pc(r['primary_top30_daily']['mdd_daily'])}** "
      f"({r['primary_top30_daily']['mdd_date']}) vs SPY {pc(r['spy_daily_mdd_same_window'])} over the same window; "
      f"monthly vol {pc(t30['net']['vol'])} vs SPY {pc(S['bench_SPY']['net']['vol'])}.")
    w(f"- Rolling windows, top-30 vs SPY: positive excess in {pc(a['rolling_12m']['share_positive'], 0)} of 12m, "
      f"{pc(a['rolling_36m']['share_positive'], 0)} of 36m and {pc(a['rolling_60m']['share_positive'], 0)} of 60m "
      f"windows (vs PIT EW: {pc(b['rolling_12m']['share_positive'], 0)} / {pc(b['rolling_36m']['share_positive'], 0)} / "
      f"{pc(b['rolling_60m']['share_positive'], 0)}).")
    w("- **Implication for the program:** the composite score is not evidence of stock-picking edge. It can still be "
      "used as a screen (it modestly sorts downside risk: bottom decile has the worst p10 and drawdown frequency), "
      "but conviction/probability language must come from the calibration tables below (which are nearly flat across "
      "deciles), not from the backtest.\n")

    w("## Headline statistics (net of 10 bps per unit traded; 2012-01…2026-08)\n")
    w("| Strategy | CAGR | Vol | Sharpe | MaxDD (m) | Excess vs SPY | t | Excess vs PIT EW | t | IR vs SPY | Turnover (1-way/yr) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for k, lab in [("primary_top30_ew", "Top-30 EW"), ("primary_topquintile_ew", "Top quintile EW"),
                   ("primary_bottomquintile_ew", "Bottom quintile EW"), ("pit_ew_universe", "PIT EW universe (bench)"),
                   ("pit_ew_scored_universe", "PIT EW scored names")]:
        s = S[k]
        vs = s["vs"]
        pe = vs.get("PIT_EW", {})
        w(f"| {lab} | {pc(s['net']['cagr'])} | {pc(s['net']['vol'])} | {f2(s['net'].get('sharpe'))} | "
          f"{pc(s['net']['mdd_monthly'])} | {pc(vs['SPY']['excess_cagr'])} | {f2(vs['SPY']['nw_t'])} | "
          f"{pc(pe.get('excess_cagr')) if pe else '—'} | {f2(pe.get('nw_t')) if pe else '—'} | "
          f"{f2(vs['SPY']['information_ratio'])} | {f2(s['annual_turnover_oneway'])} |")
    for b_, lab in [("bench_SPY", "SPY TR"), ("bench_RSP", "RSP (EW ETF)"), ("bench_^SP500TR", "^SP500TR")]:
        s = S[b_]["net"]
        w(f"| {lab} | {pc(s['cagr'])} | {pc(s['vol'])} | {f2(s.get('sharpe'))} | {pc(s['mdd_monthly'])} | | | | | | |")
    w("")
    w("Sharpe uses ^IRX (3-month T-bill) as rf. NW t = Newey-West (3 lags) t-stat of mean monthly excess. "
      "Costs: 10 bps × Σ|Δw| (buys + sells) each rebalance; turnover shown one-way.\n")
    w("**Subperiods (top-30 net vs SPY / vs PIT EW):**\n")
    w("| Period | Top-30 CAGR | SPY | Excess | t | PIT EW | Excess | t |")
    w("|---|---|---|---|---|---|---|---|")
    for per, x in t30["subperiods_vs_SPY"].items():
        y = t30["subperiods_vs_PIT_EW"].get(per, {})
        lab = "2012-2014" if per == "2010-2014" else per
        w(f"| {lab} | {pc(x['cagr'])} | {pc(x['bench_cagr'])} | {pc(x['excess_cagr'])} | {f2(x['nw_t'])} | "
          f"{pc(y.get('bench_cagr'))} | {pc(y.get('excess_cagr'))} | {f2(y.get('nw_t'))} |")
    w("")
    w("**Calendar years:**\n")
    w("| Year | Top-30 | Top-Q | PIT EW | SPY | RSP | Top-30 − SPY | Top-30 − PIT EW | PIT EW − RSP |")
    w("|---|---|---|---|---|---|---|---|---|")
    for row in r["calendar_years"]:
        w(f"| {row['year']} | {pc(row['top30_net'])} | {pc(row['topQ_net'])} | {pc(row['PIT_EW'])} | {pc(row['SPY'])} | "
          f"{pc(row['RSP'])} | {pc(row['top30_minus_SPY'])} | {pc(row['top30_minus_PIT_EW'])} | {pc(row['PIT_EW_minus_RSP'])} |")
    w("")
    ex = r.get("exploratory_2010_start", {})
    if ex:
        e30 = ex["primary_top30_ew"]
        w(f"**Exploratory extension (2010-01 start; thin fundamentals in 2010-11 — not headline):** top-30 CAGR "
          f"{pc(e30['net']['cagr'])}, excess vs SPY {pc(e30['vs_SPY']['excess_cagr'])} (t {f2(e30['vs_SPY']['nw_t'])}), "
          f"vs PIT EW {pc(e30['vs_PIT_EW']['excess_cagr'])} (t {f2(e30['vs_PIT_EW']['nw_t'])}).\n")

    w("## Signal diagnostics\n")
    w("| Signal | mean rank IC (1m) | NW t | months |")
    w("|---|---|---|---|")
    for k, v in r["ic"].items():
        w(f"| {k} | {f2(v['mean'], 4)} | {f2(v['nw_t'])} | {v['n_months']} |")
    w("")
    w("**Decile table** (time-series mean of cross-sectional decile means; formation 2011-12…2025-08):\n")
    w("| Decile | mean fwd-12m TR | mean 1m TR ×12 | stock-months |")
    w("|---|---|---|---|")
    for row in d["rows"]:
        w(f"| {int(row['decile'])} | {pc(row['mean_fwd12'])} | {pc(row['mean_ret1m_ann'])} | {row['n_stock_months']} |")
    w("")
    ff = r["ff5_umd_regression"]
    w("**FF5 + UMD regression** (monthly net return − rf; NW 3 lags):\n")
    w("| Portfolio | alpha/yr | t | Mkt | SMB | HML | RMW | CMA | UMD | R² |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for k, v in ff.items():
        if "loadings" not in v:
            continue
        lo = v["loadings"]
        w(f"| {k} | {pc(v['alpha_ann'])} | {f2(v['alpha_t_nw'])} | {f2(lo['mkt_rf'])} | {f2(lo['smb'])} | {f2(lo['hml'])} | "
          f"{f2(lo['rmw'])} | {f2(lo['cma'])} | {f2(lo['umd'])} | {f2(v['r2'])} |")
    w("")

    w("## Calibration (every PIT stock-month with a composite, formation 2011-12…2025-08)\n")
    w("P(·) are empirical frequencies. Overlapping 12-month windows make stock-months dependent: `CI` uses raw n "
      "(too narrow), `CI n_eff` uses n/12 (conservative). fwd-12m excludes names without a price 12 months later.\n")
    w("| Decile | n | P(fwd12>0) | CI n_eff | P(excess vs SPY>0) | CI n_eff | median fwd12 | p10 | p90 | P(maxDD<−20%) |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for row in r["calibration_by_decile"]:
        ci1 = row["p_fwd12_pos_ci_neff"]
        ci2 = row["p_excess_pos_ci_neff"]
        w(f"| {int(row['decile'])} | {row['n']} | {pc(row['p_fwd12_pos'])} | [{pc(ci1[0], 0)}, {pc(ci1[1], 0)}] | "
          f"{pc(row['p_excess_pos'])} | [{pc(ci2[0], 0)}, {pc(ci2[1], 0)}] | {pc(row['median_fwd12'])} | "
          f"{pc(row['p10_fwd12'])} | {pc(row['p90_fwd12'])} | {pc(row['p_maxdd_worse_20'])} |")
    w("")
    w("Decile × vol-tercile table: `v4/outputs/b1_calibration_by_decile_vol.csv` (also in b1_results.json).\n")
    w(f"Portfolio level (top-30, rolling windows vs SPY): P(12m excess>0) = {pc(a['rolling_12m']['share_positive'])}, "
      f"P(36m) = {pc(a['rolling_36m']['share_positive'])}, P(60m) = {pc(a['rolling_60m']['share_positive'])} "
      f"(windows overlap heavily; 117 60-month windows ≈ 3 independent observations).\n")

    w("## Live scores (as of 2026-09-25, same code path)\n")
    lv = r["live"]
    w(f"`v4/data/b1_live_scores.csv/.parquet`: {lv['n_rows']} constituent lines, {lv['n_with_composite']} with a "
      f"composite; coverage flags {lv['coverage_flags']}. Pending-deal targets (WBD, KVUE, TECH, AES, NSC, D) are "
      f"flagged `exclude_pending_deal` and skipped by the live top-30. Given the backtest, the live ranking is a "
      f"**screen, not a forecast**.\n")
    w("Live top-30 (entity level): " + ", ".join(x["ticker_yahoo"] for x in lv["top30"]) + "\n")

    w("## Coverage and survivorship\n")
    cov = r["coverage"]
    w("| Year | PIT members | with Yahoo price (valid identity) | with composite |")
    w("|---|---|---|---|")
    for row in cov["by_year"]:
        w(f"| {row['month_end']} | {row['pit_members']:.0f} | {row['with_price']:.0f} | {row['with_composite']:.0f} |")
    w("")
    w(f"Mean share of PIT members priced: {pc(cov['mean_pct_with_price'])}; with composite: "
      f"{pc(cov['mean_pct_with_composite'])}. Holdings that lost their price mid-month (delisting): "
      f"{cov['delist_next_total']} stock-months in the whole panel (Yahoo purges delisted symbols, so such names are "
      f"mostly absent altogether rather than delisting in-sample; the −30% distress sensitivity therefore has "
      f"almost nothing to act on — the missing names are the survivorship problem).\n")
    w("**Biggest missing PIT members by era** (no valid Yahoo series; months missing):\n")
    for e, items in missing_names_by_era(P).items():
        w(f"- {e}: " + "; ".join(items))
    w("")
    w(f"**Residual survivorship estimate:** PIT EW universe vs RSP (actual EW S&P 500 ETF, after its ~0.20% fee and "
      f"quarterly rebalancing): excess CAGR {pc(ew['vs']['RSP']['excess_cagr'])}/yr (t {f2(ew['vs']['RSP']['nw_t'])}). "
      f"Our priced universe is biased upward by roughly this amount vs the true index. This bias is of the same order "
      f"as the strategy excess estimates, so it cannot turn the negative composite result positive, but it means all "
      f"absolute CAGRs here are optimistic by ~0.5–1%/yr.\n")

    w("## Method (pre-registered, frozen in STATE.md)\n")
    w("- Universe_t = PIT members at month-end t ∩ entities with a valid Yahoo total-return price at t; entity→series "
      "via CIK; member tickers now owned (SEC company_tickers) by a different CIK or flagged `reuse_suspect` by D2 are "
      "rejected; dual-class lines collapse to one entity per CIK.")
    w("- Fundamentals: `d3_pit_monthly_lag1` (facts filed strictly before t). Market cap = Close_t × split factor "
      "after t × PIT shares (split-basis ambiguity between share-count date and t resolved by D2 split table and a "
      "trailing-median check; BRK Class-A-equivalent shares ×1,500 for BRK-B; share counts that jump >2.5× vs trailing "
      "12m median or imply <$250m / >$8tn cap set missing). Live validation vs `equity_project/info.json` (Yahoo "
      f"marketCap): {r['mktcap_validation'].get('n_within_5pct')}/{r['mktcap_validation'].get('n_compared')} within 5% "
      f"(rule ≥90%: {'PASS' if r['mktcap_validation'].get('pass_90pct_rule') else 'FAIL'}); failures: "
      + ", ".join(f"{x['ticker']} ({x['ratio_b1_over_yahoo']})" for x in r['mktcap_validation'].get('failures', [])) + ".")
    w("- Metrics exactly as STATE.md; Q/V ratios winsorised at 1st/99th pct per month (lead instruction after D3); "
      "sector-neutral mid-rank percentiles within D1's SIC→GICS-like sector rules (sectors <5 valid names pooled); "
      "families need ≥50% of metrics; composite needs ≥3 of 4 families; financials (D3 flag or SIC 6000-6411) have "
      "GP/A, accruals, leverage, EBIT/EV missing.")
    w("- Portfolios formed at month-end close t, held to t+1; names without a t+1 price are dropped from that "
      "month's return (primary treatment).")
    w("- No-look-ahead tests (`v4/code/b1_tests.py`): see `v4/outputs/b1_tests_output.txt`.\n")
    w("## Limitations (Phase A)\n")
    if "D1" in r["membership_source"]:
        w("1. Membership = D1's CIK-level PIT file (primary lines; secondary share classes dropped). Entity -> Yahoo series: "
          "D1's current Yahoo symbol first (renames / legal successors), then the ticker at t; any symbol now owned by a "
          "different CIK (SEC company_tickers) or flagged reuse_suspect by D2 is rejected. The earlier D2-spells run is kept "
          "as a sensitivity (`b1_results_d2spells.json`).")
    else:
        w("1. Membership is the temporary D2/fja05680 reconstruction until D1 lands; ticker->CIK mapping is not date-aware "
          "(reused tickers are mostly neutralised because the reusing company's Yahoo history starts after the old spell).")
    w("2. Survivorship: ~15–30% of member-months before 2020 have no price (acquired/failed names); these are excluded, "
      "which biases absolute returns upward (see RSP gap).")
    w("3. Up-C / dual-class / OP-unit structures (BX, ARES, IBKR, TKO, SPG, CPT, UDR, CHTR…) have Class-A-only market "
      "caps, which is internally consistent with Class-A net income but understates EV-based metrics.")
    w("4. 2010-11 has thin XBRL coverage; the headline starts 2012-01 (lead instruction).")
    if "phase_b" not in r:
        w("5. Phase B items (legacy replications, bias quantification, walk-forward, cost stress, plateau/robustness, "
          "backtest-expert verdict) are pending in this version.\n")
    else:
        w("5. Legacy replications use B1's PIT data (XBRL TTM, SIC-based sectors) with backtest3.py's formulas; they "
          "differ from the v3 originals in data vintage (Yahoo latest-restated annuals) by design.\n")
    if "phase_b" in r:
        phase_b_sections(r, w)
    w("## Files\n")
    for f_ in ["data/b1_panel.parquet", "data/b1_strategy_returns_monthly.parquet", "data/b1_calibration_panel.parquet",
               "data/b1_live_scores.parquet", "data/b1_live_scores.csv", "outputs/b1_results.json",
               "outputs/b1_coverage_monthly.csv", "outputs/b1_calibration_by_decile.csv",
               "outputs/b1_calibration_by_decile_vol.csv", "outputs/b1_tests_output.txt"]:
        p = DATA.parent / f_
        n = ""
        if p.suffix == ".parquet" and p.exists():
            n = f"{len(pd.read_parquet(p)):,} rows"
        elif p.suffix == ".csv" and p.exists():
            n = f"{len(pd.read_csv(p)):,} rows"
        w(f"- `v4/{f_}` {n}")
    w("\nCode: `v4/code/b1_common.py`, `b1_panel.py`, `b1_backtest.py`, `b1_tests.py`, `b1_report.py`.")
    (OUT / "b1_report.md").write_text("\n".join(L), encoding="utf-8")
    print("report written", len(L), "lines")


if __name__ == "__main__":
    main()
