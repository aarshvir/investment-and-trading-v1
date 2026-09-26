"""b1x_compare.py - Agent B1X: compare standalone results against B1's outputs (task 4).
Reads ONLY B1's output DATA files (v4/outputs/b1_results.json, v4/data/b1_live_scores.parquet) -- never any
b1_*.py code file. Writes v4/outputs/b1x_vs_b1_comparison.json for use in b1x_report.md.
"""
import json
import sys
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

sys.path.insert(0, r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\code")
import b1x_common as c

b1 = json.load(open(c.OUT / "b1_results.json"))
mine = json.load(open(c.OUT / "b1x_results.json"))

# ---------- IC series correlation ----------
my_ic = pd.read_csv(c.DATA / "b1x_ic_series_full.csv", parse_dates=["month_end"]).set_index("month_end")["ic"]
b1_headline = b1["ic"]["composite_1m"]
my_headline = mine["full_pit_universe"]["ic_headline_2012_01plus"]

cmp = {}
cmp["ic_headline"] = {
    "b1_mean": b1_headline["mean"], "b1x_mean": my_headline["mean_ic"],
    "b1_nw_t": b1_headline["nw_t"], "b1x_t": my_headline["ic_tstat"],
    "b1_n_months": b1_headline["n_months"], "b1x_n_months": my_headline["n_months"],
}

# ---------- CAGR / excess comparisons (net-of-cost, vs SPY, headline 2012-01+) ----------
pp = mine["full_pit_universe"]["portfolio_perf"]
cagr_cmp = {}
for mykey, b1strat in [("top30_net_vs_spy_headline", "primary_top30_ew"),
                       ("top_quintile_net_vs_spy_headline", "primary_topquintile_ew")]:
    b1s = b1["strategies"][b1strat]
    d = pp[mykey]
    cagr_cmp[b1strat] = {
        "b1_net_cagr": b1s["net"]["cagr"], "b1x_net_cagr": d["cagr"],
        "diff_pts": 100 * (d["cagr"] - b1s["net"]["cagr"]),
        "b1_excess_vs_spy": b1s["vs"]["SPY"]["excess_cagr"], "b1x_excess_vs_spy": d["excess_cagr"],
        "excess_diff_pts": 100 * (d["excess_cagr"] - b1s["vs"]["SPY"]["excess_cagr"]),
    }
cmp["cagr_net_vs_spy_headline"] = cagr_cmp

# ---------- live score comparison: rank correlation + top-30 Jaccard + sector agreement ----------
mine_live = pd.read_parquet(c.DATA / "b1x_live_scores.parquet")[["ticker", "sector_grp", "composite"]]
b1_live = pd.read_parquet(c.DATA / "b1_live_scores.parquet")[["ticker_yahoo", "sector_sic_based", "composite",
                                                                "composite_raw", "live_top30"]]
b1_live = b1_live.rename(columns={"ticker_yahoo": "ticker"})
merged = mine_live.merge(b1_live, on="ticker", suffixes=("_b1x", "_b1"), how="inner")
both = merged.dropna(subset=["composite_b1x", "composite_b1"])
rho, pval = spearmanr(both["composite_b1x"], both["composite_b1"])
my_top30 = set(mine_live.sort_values("composite", ascending=False).head(30)["ticker"])
b1_top30 = set(merged.loc[merged["live_top30"] == True, "ticker"])
jaccard = len(my_top30 & b1_top30) / len(my_top30 | b1_top30)
sector_agree = (merged["sector_grp"] == merged["sector_sic_based"]).mean()

cmp["live_scores"] = {
    "n_matched_tickers": int(len(merged)), "n_both_have_composite": int(len(both)),
    "spearman_rank_corr": float(rho), "spearman_p": float(pval),
    "top30_jaccard": float(jaccard), "my_top30_size": len(my_top30), "b1_top30_size": len(b1_top30),
    "top30_overlap_n": len(my_top30 & b1_top30),
    "top30_only_mine": sorted(my_top30 - b1_top30), "top30_only_b1": sorted(b1_top30 - my_top30),
    "sic_sector_agreement_rate": float(sector_agree),
}

c.write_json(c.OUT / "b1x_vs_b1_comparison.json", cmp)
print(json.dumps(cmp, indent=2, default=str))
