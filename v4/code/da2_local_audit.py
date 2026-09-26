"""da2_local_audit.py - local (no-network) checks against D3 files for DA2 audit.
Writes supporting CSVs to v4/audit/da2_supporting/ and prints a JSON summary.
"""
from __future__ import annotations
import sys, json
sys.path.insert(0, r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\code")
import da2_common as c
import numpy as np
import pandas as pd

SUP = c.AUDIT / "da2_supporting"
SUP.mkdir(parents=True, exist_ok=True)
SEED = c.SEED
out = {}

pit = pd.read_parquet(c.DATA / "d3_pit_monthly.parquet")
pit1 = pd.read_parquet(c.DATA / "d3_pit_monthly_lag1.parquet")
eps = pd.read_parquet(c.DATA / "d3_eps_quarterly_pit.parquet")
facts = pd.read_parquet(c.DATA / "d3_xbrl_facts.parquet")
lineage = pd.read_csv(c.DATA / "d3_lineage.csv")
cmeta = pd.read_csv(c.DATA / "d3_company_meta.csv")
cur = pd.read_csv(c.DATA / "d1_current_constituents.csv")
tickmap = pd.read_csv(c.DATA / "d3_ticker_cik_map.csv")

LATEST_ME = pit.month_end.max()
out["latest_month_end"] = str(LATEST_ME.date())
out["pit_rows"] = len(pit)
out["pit_lag1_rows"] = len(pit1)

# ============================================================ SAMPLE
rng = np.random.default_rng(SEED)
purposive = ["JPM", "V", "AAPL", "NVDA", "COST", "AME", "TRV", "ALL", "AIZ", "DLTR", "TGT", "BMY"]
pool = sorted(set(cur["ticker_yahoo"]) - set(purposive))
random20 = sorted(rng.choice(pool, size=20, replace=False).tolist())
sample32 = purposive + random20
samp_df = pd.DataFrame({"ticker": sample32, "group": ["purposive"] * 12 + ["random"] * 20})
samp_df = samp_df.merge(cur[["ticker_yahoo", "cik", "name", "gics_sector"]], left_on="ticker", right_on="ticker_yahoo", how="left")
samp_df.to_csv(SUP / "sample32.csv", index=False)
out["sample32_seed"] = SEED
out["sample32_n"] = len(samp_df)
out["sample32_missing_cik"] = samp_df.cik.isna().sum()

# ============================================================ PIT INTEGRITY (#3)
p = pit.copy()
p["viol"] = p["max_filed_used"] > p["month_end"]
n_total = len(p)
n_viol = int(p["viol"].sum())
out["pit_full_pop_filed_after_monthend"] = {"n": n_total, "violations": n_viol}

samp2000 = p.sample(n=2000, random_state=SEED)
n_viol_2000 = int(samp2000["viol"].sum())
out["pit_2000cell_filed_after_monthend"] = {"n": 2000, "violations": n_viol_2000, "wilson_pass_rate_ci": c.wilson(2000 - n_viol_2000, 2000)}

# also check last_filed_date <= month_end (should hold trivially given max_filed_used def, but confirm)
p["viol_lastfiled"] = p["last_filed_date"] > p["month_end"]
out["pit_last_filed_after_monthend"] = int(p["viol_lastfiled"].sum())

# lag1 file: filed < t strictly (per CONVENTIONS backtest rule) - check max_filed_used < month_end
p1 = pit1.copy()
if "max_filed_used" in p1.columns:
    p1["viol"] = p1["max_filed_used"] >= p1["month_end"]
    out["pit_lag1_filed_not_strictly_before"] = int(p1["viol"].sum())
else:
    out["pit_lag1_filed_not_strictly_before"] = "max_filed_used col absent in lag1 file"

# revision cases: concept values that changed across filings for the same period.
# NOTE: instant (balance-sheet) concepts like Assets have start=NaT -> must group by (cik,end) only,
# not (cik,start,end), or a naive groupby silently drops every row (pandas dropna=True default on NaT keys).
panel_col = {"Assets": "assets", "StockholdersEquity": "equity"}
revision_cases = []
n_revised_total = 0
for con in ["Assets", "StockholdersEquity"]:
    fa = facts[facts.concept == con].copy()
    grp = fa.groupby(["cik", "end"], observed=True)["val"].agg(["nunique", "count"])
    rk = grp[grp["nunique"] > 1].reset_index()
    n_revised_total += len(rk)
    rk = rk.merge(cmeta[["cik", "sec_name", "ticker"]].drop_duplicates("cik"), on="cik", how="left")
    rk = rk.sort_values("count", ascending=False)
    checked = sum(1 for cc in revision_cases if True)
    for _, row in rk.iterrows():
        if len([r for r in revision_cases if r["concept"] == con]) >= 10:
            break
        tick = row.ticker
        if pd.isna(tick):
            continue
        sub = fa[(fa.cik == row.cik) & (fa["end"] == row["end"])].sort_values("filed")
        vals = sub[["val", "filed", "form", "accn"]].drop_duplicates(subset=["val"], keep="first").sort_values("filed")
        if vals["val"].nunique() < 2:
            continue
        orig = vals.iloc[0]
        revisedrow = vals.iloc[-1]
        if orig.val == revisedrow.val:
            continue
        pcol = panel_col[con]
        pc = pit[pit.ticker == tick].sort_values("month_end")
        before = pc[pc.month_end < revisedrow.filed].tail(1)
        after = pc[pc.month_end >= revisedrow.filed].head(1)
        if len(before) == 0 or len(after) == 0:
            continue
        b_val = before[pcol].iloc[0]
        a_val = after[pcol].iloc[0]
        match_before = bool(np.isclose(b_val, orig.val, rtol=1e-6)) if pd.notna(b_val) else False
        match_after = bool(np.isclose(a_val, revisedrow.val, rtol=1e-6)) if pd.notna(a_val) else False
        revision_cases.append(dict(concept=con, ticker=tick, cik=int(row.cik), period_end=str(row["end"].date()),
                                    orig_val=orig.val, orig_filed=str(orig.filed.date()), orig_form=orig.form, orig_accn=orig.accn,
                                    revised_val=revisedrow.val, revised_filed=str(revisedrow.filed.date()), revised_form=revisedrow.form, revised_accn=revisedrow.accn,
                                    panel_month_before=str(before.month_end.iloc[0].date()), panel_val_before=b_val, match_before=match_before,
                                    panel_month_after=str(after.month_end.iloc[0].date()), panel_val_after=a_val, match_after=match_after))
out["n_revised_period_concept_pairs"] = int(n_revised_total)

rev_df = pd.DataFrame(revision_cases)
rev_df.to_csv(SUP / "revision_cases.csv", index=False)
out["revision_cases_found"] = len(rev_df)
out["revision_cases_both_match"] = int((rev_df.match_before & rev_df.match_after).sum()) if len(rev_df) else 0

# ============================================================ COVERAGE & STALENESS (#4)
p["year"] = p.month_end.dt.year
key_cols = ["rev_ttm", "opinc_ttm", "gp_ttm", "ni_ttm", "ocf_ttm", "capex_ttm", "total_debt", "cash_sti", "shares_out", "eps_q0", "sue"]
cov_by_year = p.groupby("year")[key_cols].apply(lambda d: d.notna().mean()).round(4)
cov_by_year["n_rows"] = p.groupby("year").size()
cov_by_year.to_csv(SUP / "coverage_by_year.csv")

latest = p[p.month_end == LATEST_ME].copy()
stal = latest["staleness_days"].describe(percentiles=[.5, .75, .9, .95, .99])
out["staleness_latest_describe"] = {k: (float(v) if pd.notna(v) else None) for k, v in stal.items()}

latest_cur = latest.merge(cur[["ticker_yahoo"]], left_on="ticker", right_on="ticker_yahoo", how="inner")
stale120 = latest_cur[latest_cur.staleness_days > 120].sort_values("staleness_days", ascending=False)
stale120[["ticker", "staleness_days", "last_form", "last_period_end", "last_filed_date"]].to_csv(SUP / "stale_gt120_current.csv", index=False)
out["n_current_constituents_at_latest"] = len(latest_cur)
out["n_current_constituents_stale_gt120d"] = len(stale120)
out["current_constituents_not_in_panel_latest"] = int(len(cur) - latest_cur.ticker.nunique())

# ============================================================ UNITS/SIGNS (#5)
sign_cols = ["capex_ttm", "buyback_ttm", "div_ttm", "issuance_ttm"]
sign_summary = {}
for col in sign_cols:
    s = p[col].dropna()
    sign_summary[col] = {"n": int(len(s)), "pct_negative": float((s < 0).mean()), "pct_positive": float((s > 0).mean()),
                          "pct_zero": float((s == 0).mean()), "min": float(s.min()), "max": float(s.max()), "median": float(s.median())}
out["sign_summary"] = sign_summary

eps_latest = eps[eps.month_end == eps.month_end.max()]
out["eps_scale_check"] = {"n": int(eps_latest.eps_diluted_adj.notna().sum()),
                           "p1": float(eps_latest.eps_diluted_adj.quantile(0.01)),
                           "p50": float(eps_latest.eps_diluted_adj.quantile(0.50)),
                           "p99": float(eps_latest.eps_diluted_adj.quantile(0.99)),
                           "max_abs": float(eps_latest.eps_diluted_adj.abs().max())}

shares_latest = latest[["ticker", "shares_out", "shares_wdil"]].dropna()
out["shares_scale_check"] = {"n": len(shares_latest), "min": float(shares_latest.shares_out.min()), "max": float(shares_latest.shares_out.max()),
                              "AAPL": float(shares_latest[shares_latest.ticker == "AAPL"].shares_out.iloc[0]) if (shares_latest.ticker == "AAPL").any() else None}

# ============================================================ Q4 = FY - 9M derivation (revenue/ni/ocf/capex), local recompute from raw facts
def _first_filed(df, keys):
    """Dedup to the ORIGINAL (earliest-filed) report of each period -> value as known right after that filing,
    not a later comparative/restated repetition of the same period in a subsequent filing."""
    return df.sort_values("filed").drop_duplicates(subset=keys, keep="first")


def fy4_check(concept_candidates, label, n_target=400):
    sub = facts[facts.concept.isin(concept_candidates)].copy()
    sub["dur"] = (sub["end"] - sub["start"]).dt.days
    fy = _first_filed(sub[(sub.form == "10-K") & (sub.dur.between(350, 380))], ["cik", "start", "end"])
    ytd9 = _first_filed(sub[(sub.form == "10-Q") & (sub.dur.between(255, 290))], ["cik", "start", "end"])
    merged = fy.merge(ytd9, on=["cik", "start"], suffixes=("_fy", "_9m"))
    merged = merged[merged.end_9m < merged.end_fy]
    merged["q4_derived"] = merged.val_fy - merged.val_9m
    return dict(label=label, n_fy_minus_9m_pairs=int(len(merged)))

out["q4_fy_minus_9m"] = {
    "revenue": fy4_check(["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"], "revenue"),
    "net_income": fy4_check(["NetIncomeLoss"], "net_income"),
    "ocf": fy4_check(["NetCashProvidedByUsedInOperatingActivities"], "ocf"),
    "capex": fy4_check(["PaymentsToAcquirePropertyPlantAndEquipment"], "capex"),
}

# now actually verify d3 TTM used the right derived quarter: pick companies+FYs, recompute TTM ending at FY-end from 4 quarters (Q1,Q2(YTD-Q1),Q3(YTD-Q2... using 6m,9m),Q4(FY-9M)) purely from facts, compare to pit rev_ttm at first month-end after the 10-K filing
def ttm_recompute_check(concept_candidates, ttm_col, n_checks=60):
    sub = facts[facts.concept.isin(concept_candidates)].copy()
    sub["dur"] = (sub["end"] - sub["start"]).dt.days
    # keep only the ORIGINAL (first-filed) report of each (cik,start,end) period: a later filing's comparative
    # column for the same period is not what was "known right after" the original filing (fixes a bug where the
    # first draft of this check sampled multi-year-stale comparatives, e.g. a "FY2014" fact carried in a 2016 10-K).
    fy = _first_filed(sub[(sub.form == "10-K") & (sub.dur.between(350, 380))], ["cik", "start", "end"]).sort_values("filed")
    q3_all = _first_filed(sub[(sub.form == "10-Q") & (sub.dur.between(255, 290))], ["cik", "start", "end"])
    results = []
    idx = fy.sample(n=min(n_checks, len(fy)), random_state=SEED).index
    for i in idx:
        row = fy.loc[i]
        cik, fystart, fyend, filed_fy = row.cik, row.start, row["end"], row.filed
        q3 = q3_all[(q3_all.cik == cik) & (q3_all.start == fystart) & (q3_all.end < fyend)]
        if q3.empty:
            continue
        q3 = q3.sort_values("end").iloc[-1]
        val_9m = q3.val
        val_q4 = row.val - val_9m
        val_fy_ttm = row.val  # TTM at FY end == FY value itself
        tick = cmeta.loc[cmeta.cik == cik, "ticker"]
        tick = tick.iloc[0] if len(tick) else None
        if tick is None:
            continue
        pc = pit[(pit.ticker == tick) & (pit.month_end >= filed_fy)].sort_values("month_end")
        if pc.empty:
            continue
        first_after = pc.iloc[0]
        panel_ttm = first_after[ttm_col]
        if pd.isna(panel_ttm):
            continue
        diff_pct = (panel_ttm - val_fy_ttm) / abs(val_fy_ttm) if val_fy_ttm != 0 else np.nan
        results.append(dict(ticker=tick, cik=cik, fy_end=str(fyend.date()), filed_fy=str(filed_fy.date()),
                             val_fy=row.val, val_9m=val_9m, val_q4_derived=val_q4,
                             panel_month=str(first_after.month_end.date()), panel_ttm=panel_ttm,
                             diff_pct=diff_pct, within_1pct=bool(abs(diff_pct) <= 0.01) if pd.notna(diff_pct) else None))
    return pd.DataFrame(results)

rev_ttm_check = ttm_recompute_check(["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"], "rev_ttm")
ni_ttm_check = ttm_recompute_check(["NetIncomeLoss"], "ni_ttm")
ocf_ttm_check = ttm_recompute_check(["NetCashProvidedByUsedInOperatingActivities"], "ocf_ttm")
capex_ttm_check = ttm_recompute_check(["PaymentsToAcquirePropertyPlantAndEquipment"], "capex_ttm")

for name, df_ in [("revenue", rev_ttm_check), ("net_income", ni_ttm_check), ("ocf", ocf_ttm_check), ("capex", capex_ttm_check)]:
    df_.to_csv(SUP / f"ttm_recompute_{name}.csv", index=False)
    n = len(df_)
    k = int(df_.within_1pct.sum()) if n else 0
    out.setdefault("ttm_recompute_fy_end_pass_rate", {})[name] = {"n": n, "pass_1pct": k, "wilson": c.wilson(k, n) if n else None}

# ============================================================ split-adjustment spot check (AAPL, NVDA)
def split_spot(ticker, split_dates):
    e = eps[(eps.ticker == ticker)].copy()
    e_latest_asof = e[e.month_end == e.month_end.max()]
    raw = facts[(facts.ticker == ticker) & (facts.concept.isin(["EarningsPerShareDiluted"]))].sort_values("end")
    return dict(ticker=ticker, n_eps_rows_latest_snapshot=len(e_latest_asof),
                raw_eps_sample=raw[["end", "val", "filed", "form"]].tail(6).to_dict("records"))

out["split_spotcheck"] = {"AAPL": split_spot("AAPL", ["2020-08-31"]), "NVDA": split_spot("NVDA", ["2021-07-20", "2024-06-10"])}

with open(SUP / "local_audit_summary.json", "w") as f:
    json.dump(out, f, indent=2, default=str)

print(json.dumps(out, indent=2, default=str)[:6000])
print("...TRUNCATED, full at", SUP / "local_audit_summary.json")
