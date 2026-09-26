"""d4_validate.py - validation of the D4 live snapshot.

(a) price vs independent closes (Cboe 'close', CNBC 'last' @16:00 ET) - tolerance 0.5%
    (Stooq, the source requested, serves a JS proof-of-work bot challenge -> not used; see d4_fetch_indep_prices.py)
(b) marketCap vs price x sharesOutstanding - tolerance 3%; dual/multi-class flagged
(c) SEC XBRL frames CY2025 (Revenues / RevenueFromContractWithCustomerExcludingAssessedTax / NetIncomeLoss) vs Yahoo
    annual income_stmt FY2025 column for Dec-FYE filers - tolerance 2%
(d) staleness: regularMarketTime (America/New_York date) != 2026-09-25
(e) anomalies (negative forward EPS, P/E>100, missing estimates, extreme dispersion, metadata oddities, ...)
(f) fiscal-year-end check: Yahoo FY0 end month vs SEC submissions 'fiscalYearEnd' (MMDD)
(g) NTM vs Yahoo forwardPE universe table

Outputs: v4/data/d4_validation_prices.csv, d4_validation_mcap.csv, d4_validation_sec.csv, d4_anomalies.csv,
         v4/outputs/d4_ntm_vs_yahoo_table.csv, v4/outputs/d4_validation_summary.json
"""
from __future__ import annotations

import difflib
import gzip
import json
import pickle
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import ASOF, CACHE, DATA, OUT, utc_now_iso, write_meta  # noqa: E402

SNAP = DATA / "d4_live_snapshot.parquet"
FR = CACHE / "sec" / "frames"
SUB = CACHE / "sec" / "submissions"
YC = CACHE / "yahoo"

# companies with more than one common-share class (listed or unlisted) - Yahoo marketCap often spans classes
REC_OFFSET = 0.0
MULTI_CLASS = {"GOOGL", "GOOG", "FOXA", "FOX", "NWSA", "NWS", "BRK-B", "BF-B", "META", "V", "MA", "CMCSA", "LEN",
               "NKE", "UAA", "UA", "HEI", "MKC", "TKO", "EL", "LBRDK", "DELL", "HUBB", "PSKY", "Q", "ZG", "Z"}


def passflag(diff, tol):
    """nullable boolean pass flag: NA where the comparison is not available"""
    diff = pd.to_numeric(diff, errors="coerce")
    return pd.Series([pd.NA if pd.isna(x) else bool(abs(x) <= tol) for x in diff], index=diff.index, dtype="boolean")


def pct(a, b):
    return (a / b - 1) if (pd.notna(a) and pd.notna(b) and b != 0) else np.nan


def load_frame(concept):
    fp = FR / f"{concept}_CY2025.json.gz"
    if not fp.exists():
        return {}
    d = json.load(gzip.open(fp, "rt", encoding="utf-8"))
    return {int(x["cik"]): x for x in d.get("data", [])}


def price_check(s, summ):
    ip = pd.read_csv(DATA / "d4_indep_prices.csv")
    d = s[["ticker", "price", "regularMarketTime_utc", "regularMarketDate_ny", "y_regularMarketPreviousClose"]].merge(ip, on="ticker", how="left")
    d["cboe_date"] = d["cboe_last_trade_time"].astype(str).str[:10]
    d["cnbc_date"] = d["cnbc_last_time"].astype(str).str[:10]
    d["diff_cboe"] = [pct(a, b) for a, b in zip(d["price"], d["cboe_close"])]
    d["diff_cnbc"] = [pct(a, b) for a, b in zip(d["price"], d["cnbc_last"])]
    d["pass_cboe"] = passflag(d["diff_cboe"], 0.005)
    d["pass_cnbc"] = passflag(d["diff_cnbc"], 0.005)
    d["cboe_vs_cnbc"] = [pct(a, b) for a, b in zip(d["cboe_close"], d["cnbc_last"])]
    d["exact_match_cboe"] = d["diff_cboe"].abs() < 1e-6
    # vendor cross-checks of two fundamentals against CNBC (LSEG-sourced): TTM EPS and shares outstanding
    sx = s.set_index("ticker")
    d["y_trailingEps"] = d["ticker"].map(sx["trailingEps"])
    d["y_sharesOutstanding"] = d["ticker"].map(sx["sharesOutstanding"])
    d["y_impliedShares"] = d["ticker"].map(sx["impliedSharesOutstanding"])

    def parse_sh(x):
        if not isinstance(x, str) or not x:
            return np.nan
        m = re.match(r"^([0-9.,]+)\s*([KMBT]?)$", x.strip())
        if not m:
            return np.nan
        mult = {"": 1, "K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}[m.group(2)]
        return float(m.group(1).replace(",", "")) * mult
    d["cnbc_shares"] = d["cnbc_sharesout"].map(parse_sh)
    d["diff_eps_ttm_cnbc"] = [pct(a, b) for a, b in zip(d["y_trailingEps"], d["cnbc_eps_ttm"])]
    d["diff_shares_cnbc"] = [pct(a, b) for a, b in zip(d["y_sharesOutstanding"], d["cnbc_shares"])]
    d["diff_implshares_cnbc"] = [pct(a, b) for a, b in zip(d["y_impliedShares"], d["cnbc_shares"])]
    d.to_csv(DATA / "d4_validation_prices.csv", index=False)
    summ["vendor_crosscheck_cnbc"] = {
        "trailing_eps_compared": int(d["diff_eps_ttm_cnbc"].notna().sum()),
        "trailing_eps_within_5pct": int((d["diff_eps_ttm_cnbc"].abs() <= 0.05).sum()),
        "trailing_eps_within_1pct": int((d["diff_eps_ttm_cnbc"].abs() <= 0.01).sum()),
        "shares_compared": int(d["diff_shares_cnbc"].notna().sum()),
        "shares_within_3pct": int((d["diff_shares_cnbc"].abs() <= 0.03).sum()),
        "shares_within_3pct_either_yahoo_field": int(((d["diff_shares_cnbc"].abs() <= 0.03) | (d["diff_implshares_cnbc"].abs() <= 0.03)).sum()),
        "worst_eps": d.assign(a=d["diff_eps_ttm_cnbc"].abs()).sort_values("a", ascending=False).head(10)[["ticker", "y_trailingEps", "cnbc_eps_ttm", "diff_eps_ttm_cnbc"]].round(4).to_dict("records"),
        "worst_shares": d.assign(a=d["diff_shares_cnbc"].abs()).sort_values("a", ascending=False).head(10)[["ticker", "y_sharesOutstanding", "y_impliedShares", "cnbc_sharesout", "diff_shares_cnbc"]].round(4).to_dict("records"),
    }
    n_cb = int(d["diff_cboe"].notna().sum())
    n_cn = int(d["diff_cnbc"].notna().sum())
    summ["price"] = {
        "n_universe": int(len(d)),
        "cboe_compared": n_cb, "cboe_pass_0p5pct": int((d["pass_cboe"] == True).sum()),  # noqa: E712
        "cboe_exact_match": int(d["exact_match_cboe"].sum()),
        "cnbc_compared": n_cn, "cnbc_pass_0p5pct": int((d["pass_cnbc"] == True).sum()),  # noqa: E712
        "cnbc_exact_match": int((d["diff_cnbc"].abs() < 1e-6).sum()),
        "either_pass": int(((d["pass_cboe"] == True) | (d["pass_cnbc"] == True)).sum()),  # noqa: E712
        "max_abs_diff_cboe": float(d["diff_cboe"].abs().max()) if n_cb else None,
        "median_abs_diff_cboe": float(d["diff_cboe"].abs().median()) if n_cb else None,
        "cboe_dates": d["cboe_date"].value_counts().to_dict(),
        "cnbc_dates": d["cnbc_date"].value_counts().to_dict(),
        "fail_cboe": d.loc[d["pass_cboe"] == False, ["ticker", "price", "cboe_close", "cnbc_last", "diff_cboe", "diff_cnbc"]].round(5).to_dict("records"),  # noqa: E712
        "fail_cnbc": d.loc[d["pass_cnbc"] == False, ["ticker", "price", "cboe_close", "cnbc_last", "diff_cboe", "diff_cnbc"]].round(5).to_dict("records"),  # noqa: E712
        "missing_cboe": d.loc[d["cboe_close"].isna(), "ticker"].tolist(),
        "missing_cnbc": d.loc[d["cnbc_last"].isna(), "ticker"].tolist(),
    }
    return d


def mcap_check(s, summ):
    d = s[["ticker", "price", "marketCap", "sharesOutstanding", "impliedSharesOutstanding", "cik"]].copy()
    d["mc_calc_so"] = d["price"] * d["sharesOutstanding"]
    d["mc_calc_implied"] = d["price"] * d["impliedSharesOutstanding"]
    d["diff_so"] = [pct(a, b) for a, b in zip(d["marketCap"], d["mc_calc_so"])]
    d["diff_implied"] = [pct(a, b) for a, b in zip(d["marketCap"], d["mc_calc_implied"])]
    d["pass_so_3pct"] = d["diff_so"].abs() <= 0.03
    d["pass_implied_3pct"] = d["diff_implied"].abs() <= 0.03
    d["implied_vs_so"] = [pct(a, b) for a, b in zip(d["impliedSharesOutstanding"], d["sharesOutstanding"])]
    shared_cik = set(d.loc[d["cik"].duplicated(keep=False), "ticker"])
    d["multi_class_flag"] = d["ticker"].isin(MULTI_CLASS | shared_cik) | (d["implied_vs_so"].abs() > 0.03)
    d.to_csv(DATA / "d4_validation_mcap.csv", index=False)
    fails = d[d["pass_so_3pct"] == False]  # noqa: E712
    summ["mcap"] = {
        "compared": int(d["diff_so"].notna().sum()),
        "pass_3pct": int((d["pass_so_3pct"] == True).sum()),  # noqa: E712
        "pass_3pct_using_implied_shares": int((d["pass_implied_3pct"] == True).sum()),  # noqa: E712
        "fails": fails[["ticker", "marketCap", "mc_calc_so", "diff_so", "diff_implied", "multi_class_flag"]].round(4).to_dict("records"),
        "fails_not_multiclass": fails.loc[~fails["multi_class_flag"], "ticker"].tolist(),
    }
    return d


def yahoo_is_row(tk):
    fp = YC / f"{tk}.pkl"
    if not fp.exists():
        return None, None
    rec = pickle.load(open(fp, "rb"))
    ist = rec.get("income_stmt")
    if not isinstance(ist, pd.DataFrame) or ist.empty:
        return None, None
    cols = [c for c in ist.columns if pd.Timestamp("2025-12-15") <= pd.Timestamp(c) <= pd.Timestamp("2026-01-15")]
    if not cols:
        return None, [str(pd.Timestamp(c).date()) for c in ist.columns]
    c = cols[0]
    out = {"yahoo_fy_col": str(pd.Timestamp(c).date())}
    for lab, keys in [("y_total_revenue", ["Total Revenue", "TotalRevenue"]),
                      ("y_operating_revenue", ["Operating Revenue", "OperatingRevenue"]),
                      ("y_net_income", ["Net Income", "NetIncome"]),
                      ("y_ni_common", ["Net Income Common Stockholders", "NetIncomeCommonStockholders"]),
                      ("y_ni_incl_nci", ["Net Income Including Noncontrolling Interests", "NetIncomeIncludingNoncontrollingInterests"]),
                      ("y_ni_cont_ops", ["Net Income Continuous Operations", "NetIncomeContinuousOperations"])]:
        key = next((k for k in keys if k in ist.index), None)
        v = ist.loc[key, c] if key is not None else np.nan
        out[lab] = float(v) if pd.notna(v) else np.nan
    return out, None


def sec_check(s, summ):
    F = {c: load_frame(c) for c in ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "NetIncomeLoss",
                                     "RevenueFromContractWithCustomerIncludingAssessedTax", "RevenuesNetOfInterestExpense",
                                     "ProfitLoss", "NetIncomeLossAvailableToCommonStockholdersBasic"]}
    rows = []
    seen = set()
    for _, r in s.iterrows():
        cik = int(r["cik"]) if pd.notna(r["cik"]) else None
        if cik is None or cik in seen:
            continue
        seen.add(cik)
        y, cols = yahoo_is_row(r["ticker"])
        row = {"ticker": r["ticker"], "cik": cik, "gics_sector": r["gics_sector"], "gics_sub_industry": r["gics_sub_industry"]}
        if y is None:
            row["dec_fye"] = False
            row["note"] = "no Yahoo FY column in Dec-2025/Jan-2026" + (f" (cols {cols[:2]})" if cols else "")
            rows.append(row)
            continue
        row.update(y)
        # SEC concept values, restricted to annual periods ending 2025-12-15..2026-01-15
        for c, fr in F.items():
            x = fr.get(cik)
            ok = x is not None and "2025-12-15" <= x["end"] <= "2026-01-15"
            row[f"sec_{c}"] = float(x["val"]) if ok else np.nan
            if c in ("Revenues", "NetIncomeLoss") and x is not None:
                row[f"sec_{c}_period"] = f"{x['start']}..{x['end']}"
                row[f"sec_{c}_accn"] = x["accn"]
        row["dec_fye"] = True
        if pd.notna(row["sec_Revenues"]):
            row["sec_rev_primary"], row["sec_rev_concept"] = row["sec_Revenues"], "Revenues"
        elif pd.notna(row["sec_RevenueFromContractWithCustomerExcludingAssessedTax"]):
            row["sec_rev_primary"], row["sec_rev_concept"] = row["sec_RevenueFromContractWithCustomerExcludingAssessedTax"], "RevenueFromContractWithCustomerExcludingAssessedTax"
        else:
            row["sec_rev_primary"], row["sec_rev_concept"] = np.nan, None
        row["rev_gap"] = pct(row["y_total_revenue"], row["sec_rev_primary"])
        alts = [row.get(f"sec_{c}") for c in ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                                             "RevenueFromContractWithCustomerIncludingAssessedTax", "RevenuesNetOfInterestExpense"]]
        gaps = [abs(pct(row["y_total_revenue"], a)) for a in alts if pd.notna(a) and a != 0]
        row["rev_gap_best_concept"] = min(gaps) if gaps else np.nan
        row["ni_gap"] = pct(row["y_net_income"], row["sec_NetIncomeLoss"])
        nialts = [row.get("sec_NetIncomeLoss"), row.get("sec_ProfitLoss"), row.get("sec_NetIncomeLossAvailableToCommonStockholdersBasic")]
        ygs = [row["y_net_income"], row["y_ni_common"], row["y_ni_incl_nci"]]
        g2 = [abs(pct(yv, sv)) for yv in ygs for sv in nialts if pd.notna(yv) and pd.notna(sv) and sv != 0]
        row["ni_gap_best_pair"] = min(g2) if g2 else np.nan
        rows.append(row)
    d = pd.DataFrame(rows)
    d["rev_pass_2pct"] = passflag(d["rev_gap"], 0.02)
    d["ni_pass_2pct"] = passflag(d["ni_gap"], 0.02)

    def gap_class(gap, best, yv, sv):
        if pd.isna(gap):
            return None
        if abs(gap) <= 0.02:
            return "pass"
        if pd.notna(yv) and pd.notna(sv) and sv != 0:
            ratio = abs(yv / sv)
            if abs(ratio / 1e3 - 1) < 0.02 or abs(ratio / 1e6 - 1) < 0.02:
                return "sec_xbrl_scale_error"
        if pd.notna(best) and best <= 0.02:
            return "concept_mismatch(other SEC concept/pair within 2%)"
        return "definition_or_unexplained"
    d["rev_gap_class"] = [gap_class(g, b, y, v) for g, b, y, v in zip(d["rev_gap"], d["rev_gap_best_concept"], d["y_total_revenue"], d["sec_rev_primary"])]
    d["ni_gap_class"] = [gap_class(g, b, y, v) for g, b, y, v in zip(d["ni_gap"], d["ni_gap_best_pair"], d["y_net_income"], d["sec_NetIncomeLoss"])]
    d.to_csv(DATA / "d4_validation_sec.csv", index=False)
    dec = d[d["dec_fye"] == True]  # noqa: E712
    rv, ni = dec["rev_gap"].notna(), dec["ni_gap"].notna()
    top_rev = dec[rv].assign(a=dec.loc[rv, "rev_gap"].abs()).sort_values("a", ascending=False).head(15)
    top_ni = dec[ni].assign(a=dec.loc[ni, "ni_gap"].abs()).sort_values("a", ascending=False).head(15)
    summ["sec"] = {
        "companies_unique_cik": int(len(d)), "dec_fye_companies": int(len(dec)),
        "rev_compared": int(rv.sum()), "rev_within_2pct": int((dec["rev_pass_2pct"] == True).sum()),  # noqa: E712
        "rev_within_2pct_best_concept": int((dec["rev_gap_best_concept"] <= 0.02).sum()),
        "ni_compared": int(ni.sum()), "ni_within_2pct": int((dec["ni_pass_2pct"] == True).sum()),  # noqa: E712
        "ni_within_2pct_best_pair": int((dec["ni_gap_best_pair"] <= 0.02).sum()),
        "rev_best_concept_compared": int(dec["rev_gap_best_concept"].notna().sum()),
        "ni_best_pair_compared": int(dec["ni_gap_best_pair"].notna().sum()),
        "rev_gap_class_counts": dec["rev_gap_class"].value_counts().to_dict(),
        "ni_gap_class_counts": dec["ni_gap_class"].value_counts().to_dict(),
        "dec_fye_without_sec_revenue": dec.loc[dec["rev_gap"].isna(), "ticker"].tolist(),
        "dec_fye_without_sec_netincome": dec.loc[dec["ni_gap"].isna(), "ticker"].tolist(),
        "rev_concept_used": dec["sec_rev_concept"].value_counts().to_dict(),
        "rev_fail_by_sector": dec[dec["rev_pass_2pct"] == False]["gics_sector"].value_counts().to_dict(),  # noqa: E712
        "ni_fail_by_sector": dec[dec["ni_pass_2pct"] == False]["gics_sector"].value_counts().to_dict(),  # noqa: E712
        "top_rev_gaps": top_rev[["ticker", "gics_sub_industry", "y_total_revenue", "sec_rev_primary", "sec_rev_concept", "rev_gap", "rev_gap_best_concept", "rev_gap_class"]].round(4).to_dict("records"),
        "top_ni_gaps": top_ni[["ticker", "gics_sub_industry", "y_net_income", "y_ni_common", "sec_NetIncomeLoss", "sec_ProfitLoss", "ni_gap", "ni_gap_best_pair", "ni_gap_class"]].round(4).to_dict("records"),
    }
    return d


def fye_check(s, summ):
    """Yahoo fiscal calendar vs SEC: (1) Yahoo FY0-end month vs SEC 'fiscalYearEnd' (MMDD metadata);
    (2) Yahoo lastFiscalYearEnd vs reportDate of the latest annual report (10-K/10-KT/20-F/40-F) in EDGAR."""
    rows = []
    for _, r in s.iterrows():
        cik = int(r["cik"]) if pd.notna(r["cik"]) else None
        fp = SUB / f"CIK{cik:010d}.json.gz" if cik else None
        sec_fye = sec_name = former = last_ar = last_ar_form = None
        if fp and fp.exists():
            j = json.load(gzip.open(fp, "rt", encoding="utf-8"))
            sec_fye = j.get("fiscalYearEnd")
            sec_name = j.get("name")
            former = "; ".join(f"{x.get('name')} (to {str(x.get('to'))[:10]})" for x in (j.get("formerNames") or []))
            rc = j["filings"]["recent"]
            for f_, rd, fd in zip(rc["form"], rc["reportDate"], rc["filingDate"]):
                if f_ in ("10-K", "10-KT", "20-F", "40-F") and rd and fd <= ASOF.isoformat():
                    last_ar, last_ar_form = rd, f_
                    break
        y_end = r["fy0_end"]
        ymm = pd.Timestamp(y_end).month if pd.notna(y_end) else None
        smm = int(sec_fye[:2]) if sec_fye else None
        sdd = int(sec_fye[2:]) if sec_fye else None
        ok = None
        if ymm and smm:
            # 52/53-week filers: SEC 'fiscalYearEnd' can be e.g. 0125 or 1228 while Yahoo normalises to month-end
            diffm = (ymm - smm) % 12
            ok = diffm == 0 or (diffm == 1 and sdd is not None and sdd >= 24) or (diffm == 11 and sdd is not None and sdd <= 7)
        lfy_gap = None
        if last_ar and pd.notna(r["lastFiscalYearEnd"]):
            lfy_gap = abs((pd.Timestamp(r["lastFiscalYearEnd"]) - pd.Timestamp(last_ar)).days)
        note = r.get("fy0_note")
        expl = None
        if ok is False:
            if isinstance(note, str) and note:
                expl = "documented FYE change / spin (SEC 8-K) - Yahoo correct, SEC metadata stale"
            elif last_ar and pd.Timestamp(last_ar).month == ymm:
                expl = "SEC 'fiscalYearEnd' metadata wrong; latest annual report period matches Yahoo"
            else:
                expl = "unexplained"
        rows.append({"ticker": r["ticker"], "yahoo_fy0_end": y_end, "yahoo_lastFiscalYearEnd": r["lastFiscalYearEnd"],
                     "sec_fiscalYearEnd": sec_fye, "sec_last_annual_report_period": last_ar, "sec_last_annual_form": last_ar_form,
                     "lfy_vs_sec_annual_days": lfy_gap, "fye_consistent": ok, "explanation": expl,
                     "sec_name": sec_name, "sec_former_names": former})
    d = pd.DataFrame(rows)
    d.to_csv(DATA / "d4_validation_fye.csv", index=False)
    lg = pd.to_numeric(d["lfy_vs_sec_annual_days"], errors="coerce")
    summ["fye_vs_sec"] = {"compared": int(d["fye_consistent"].notna().sum()),
                          "consistent": int((d["fye_consistent"] == True).sum()),  # noqa: E712
                          "inconsistent": d.loc[d["fye_consistent"] == False, ["ticker", "yahoo_fy0_end", "sec_fiscalYearEnd", "sec_last_annual_report_period", "explanation"]].astype(str).to_dict("records"),  # noqa: E712
                          "lfy_vs_last_annual_report_compared": int(lg.notna().sum()),
                          "lfy_within_7d_of_last_annual_report": int((lg <= 7).sum()),
                          "lfy_mismatch_gt7d": d.loc[lg > 7, ["ticker", "yahoo_lastFiscalYearEnd", "sec_last_annual_report_period", "sec_last_annual_form"]].astype(str).to_dict("records")}
    return d


def name_sim(a, b):
    def norm(x):
        x = str(x or "").lower()
        x = re.sub(r"\(.*?\)", " ", x)
        x = re.sub(r"[^a-z0-9 ]", " ", x)
        x = re.sub(r"\b(inc|corp|corporation|company|co|plc|ltd|limited|the|group|holdings|holding|class [a-c]|n v|nv|sa|ag|lp)\b", " ", x)
        return " ".join(x.split())
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def anomalies(s, fye, summ):
    A = []
    global REC_OFFSET
    REC_OFFSET = float((s["rec_mean"] - s["rec_mean_calc_0m"]).median())
    summ["rec_mean_systematic_offset"] = {"median_info_minus_counts_mean": REC_OFFSET,
                                          "n": int((s["rec_mean"] - s["rec_mean_calc_0m"]).notna().sum())}

    def add(tk, check, detail, severity="info"):
        A.append({"ticker": tk, "check": check, "severity": severity, "detail": detail})
    fyem = fye.set_index("ticker")
    for _, r in s.iterrows():
        tk = r["ticker"]
        # staleness
        if r["regularMarketDate_ny"] != ASOF.isoformat():
            add(tk, "stale_price", f"regularMarketTime NY date={r['regularMarketDate_ny']}", "high")
        # negative EPS
        for c in ["forwardEps", "eps_fy0", "eps_fy1", "eps_ntm"]:
            if pd.notna(r[c]) and r[c] < 0:
                add(tk, "negative_forward_eps", f"{c}={r[c]:.3f}", "medium")
        # P/E > 100
        for c in ["pe_ntm", "trailingPE", "forwardPE"]:
            if pd.notna(r[c]) and r[c] > 100:
                add(tk, "pe_gt_100", f"{c}={r[c]:.1f}", "medium")
        # missing / thin estimates
        if pd.isna(r["eps_fy0"]) or pd.isna(r["eps_fy1"]):
            add(tk, "missing_estimates", f"eps_fy0={r['eps_fy0']}, eps_fy1={r['eps_fy1']}", "high")
        elif pd.notna(r["eps_fy1_n"]) and r["eps_fy1_n"] < 3:
            add(tk, "thin_coverage", f"eps_fy1 numberOfAnalysts={r['eps_fy1_n']:.0f}", "medium")
        if pd.isna(r["rev_fy1"]):
            add(tk, "missing_revenue_estimates", "rev_fy1 missing", "medium")
        # dispersion
        a, lo, hi = r["eps_fy1"], r["eps_fy1_low"], r["eps_fy1_high"]
        if pd.notna(a) and pd.notna(lo) and pd.notna(hi) and a != 0:
            disp = (hi - lo) / abs(a)
            if disp > 1.0:
                add(tk, "eps_fy1_dispersion_extreme", f"(high-low)/|avg|={disp:.2f} (low {lo:.2f}, avg {a:.2f}, high {hi:.2f}, n={r['eps_fy1_n']})", "medium")
            elif disp > 0.5:
                add(tk, "eps_fy1_dispersion_high", f"(high-low)/|avg|={disp:.2f} (low {lo:.2f}, avg {a:.2f}, high {hi:.2f})", "low")
        # FY1 << FY0 (one-offs in FY0?)
        if pd.notna(r["eps_fy0"]) and pd.notna(r["eps_fy1"]) and r["eps_fy0"] > 0 and r["eps_fy1"] < 0.85 * r["eps_fy0"]:
            add(tk, "eps_fy1_below_fy0_15pct", f"fy0={r['eps_fy0']:.2f} fy1={r['eps_fy1']:.2f}", "medium")
        # NTM method divergence
        if pd.notna(r["eps_ntm"]) and pd.notna(r["eps_ntm_qaware"]) and r["eps_ntm"] > 0:
            dv = r["eps_ntm_qaware"] / r["eps_ntm"] - 1
            if abs(dv) > 0.10:
                add(tk, "ntm_method_divergence_gt10pct", f"time-weighted {r['eps_ntm']:.2f} vs quarter-aware {r['eps_ntm_qaware']:.2f} ({dv:+.1%}); YTD reported {r['eps_fy0_ytd_reported']:.2f} over {r['fy0_quarters_reported_eh']}q", "medium")
        # Yahoo forward horizon
        if r["yahoo_fwd_horizon"] != "FY1(+1y)":
            add(tk, "yahoo_forwardEps_not_exact_FY1", f"{r['yahoo_fwd_horizon']}: forwardEps={r['forwardEps']}, fy0={r['eps_fy0']}, fy1={r['eps_fy1']}", "low")
        if pd.notna(r["forwardPE_consistency"]) and r["forwardPE_consistency"] > 0.01:
            add(tk, "forwardPE_not_price_over_forwardEps", f"forwardPE={r['forwardPE']:.2f} vs price/forwardEps={r['forwardPE_recalc']:.2f}", "low")
        # fiscal dates
        if r["fy_check"] != "ok":
            add(tk, "fiscal_date_inconsistency", r["fy_check"], "medium")
        if tk in fyem.index and fyem.loc[tk, "fye_consistent"] is False:
            add(tk, "fye_month_vs_sec_mismatch", f"yahoo fy0_end={fyem.loc[tk, 'yahoo_fy0_end']} sec fiscalYearEnd={fyem.loc[tk, 'sec_fiscalYearEnd']}", "medium")
        # metadata
        if isinstance(r["y_prevName"], str) and r["y_prevName"]:
            # verify Yahoo prevName against SEC EDGAR formerNames (+ current SEC name) for the same CIK
            former = fyem.loc[tk, "sec_former_names"] if tk in fyem.index else None
            sec_now = fyem.loc[tk, "sec_name"] if tk in fyem.index else None
            cands = [x.split(" (to ")[0] for x in str(former or "").split("; ") if x] + [str(sec_now or ""), str(r["y_longName"] or "")]
            best = max((name_sim(r["y_prevName"], c) for c in cands if c), default=0.0)
            best_sec = max((name_sim(r["y_prevName"], c) for c in cands[:-1] if c), default=0.0)
            corp_like = bool(re.search(r"\b(inc|incorporated|corp|corporation|company|co|limited|ltd|plc|llc|group|n\.?v|s\.?a|holdings?|trust|reit)\b\.?", str(r["y_prevName"]), re.I))
            ytoks = set(re.findall(r"[a-z0-9]{3,}", str(r["y_longName"]).lower())) | set(re.findall(r"[a-z0-9]{3,}", str(sec_now or "").lower()))
            shared = bool(set(re.findall(r"[a-z0-9]{3,}", str(r["y_prevName"]).lower())) & (ytoks - {"inc", "corp", "corporation", "company", "the", "group", "holdings", "plc", "ltd", "limited", "llc"}))
            if best_sec >= 0.6:
                verdict = "verified_in_SEC_formerNames"
            elif corp_like or shared or best >= 0.6:
                verdict = "plausible_predecessor_not_in_SEC_formerNames_for_this_CIK"
            else:
                verdict = "IMPLAUSIBLE_not_a_company_name"
            add(tk, "metadata_prevName", f"prevName='{r['y_prevName']}' ({verdict}; best SEC sim={best_sec:.2f}) nameChangeDate={r['y_nameChangeDate']} longName='{r['y_longName']}'; SEC formerNames: {str(former)[:160]}",
                "high" if verdict.startswith("IMPLAUSIBLE") else "info")
        if isinstance(r.get("y_ipoExpectedDate"), str) and r.get("y_ipoExpectedDate"):
            add(tk, "metadata_ipoExpectedDate_present", f"ipoExpectedDate={r['y_ipoExpectedDate']} on a long-listed stock", "info")
        sim2 = name_sim(r["y_longName"], r["name_wiki"])
        wt = set(re.findall(r"[a-z0-9]{2,}", re.sub(r"\(.*?\)", " ", str(r["name_wiki"]).lower())))
        yt = set(re.findall(r"[a-z0-9]{2,}", str(r["y_longName"]).lower()))
        if sim2 < 0.5 and not (wt and wt <= yt):
            add(tk, "name_differs_yahoo_vs_wikipedia", f"yahoo='{r['y_longName']}' wiki='{r['name_wiki']}' sim={sim2:.2f} (short/brand name vs legal name; manual check)", "info")
        if r["y_quoteType"] != "EQUITY":
            add(tk, "quoteType_not_equity", str(r["y_quoteType"]), "high")
        if r["y_currency"] != "USD":
            add(tk, "currency_not_usd", str(r["y_currency"]), "high")
        if isinstance(r["y_financialCurrency"], str) and r["y_financialCurrency"] != "USD":
            add(tk, "financialCurrency_not_usd", str(r["y_financialCurrency"]), "medium")
        if isinstance(r["eps_currency"], str) and r["eps_currency"] != "USD":
            add(tk, "estimate_currency_not_usd", str(r["eps_currency"]), "high")
        # targets & recs
        if pd.notna(r["target_mean"]) and pd.notna(r["price"]):
            ratio = r["target_mean"] / r["price"]
            if ratio > 1.6 or ratio < 0.7:
                add(tk, "target_mean_far_from_price", f"target_mean/price={ratio:.2f}", "low")
        if pd.isna(r["target_mean"]):
            add(tk, "missing_price_target", "", "low")
        if pd.notna(r["rec_mean"]) and pd.notna(r["rec_mean_calc_0m"]) and abs(r["rec_mean"] - r["rec_mean_calc_0m"] - REC_OFFSET) > 0.5:
            add(tk, "rec_mean_inconsistent_beyond_systematic_offset", f"info.recommendationMean={r['rec_mean']:.2f} vs recommendations_summary 0m={r['rec_mean_calc_0m']:.2f} (universe median offset {REC_OFFSET:+.2f})", "low")
        # earnings dates
        if not r["next_earnings_date"]:
            add(tk, "next_earnings_date_missing", "all calendar dates in the past or none", "medium")
        elif pd.notna(r["days_to_next_earnings"]) and r["days_to_next_earnings"] > 110:
            add(tk, "next_earnings_date_far", f"{r['next_earnings_date']} ({r['days_to_next_earnings']:.0f}d)", "low")
        if r["yf_calendar_tz_shift"] is True:
            pass  # summarised separately (systematic yfinance local-timezone artefact)
        if isinstance(r["fetch_errors"], str) and r["fetch_errors"]:
            add(tk, "fetch_errors", r["fetch_errors"], "medium")
        # dividend yield sanity
        if pd.notna(r["trailingAnnualDividendYield"]) and r["trailingAnnualDividendYield"] > 0.15:
            add(tk, "dividend_yield_gt_15pct", f"{r['trailingAnnualDividendYield']:.3f}", "medium")
        if pd.notna(r["enterpriseValue"]) and r["enterpriseValue"] <= 0:
            add(tk, "enterprise_value_nonpositive", f"{r['enterpriseValue']:.3g} (cash-rich financial; EV not meaningful)", "info")
    d = pd.DataFrame(A)
    d.to_csv(DATA / "d4_anomalies.csv", index=False)
    summ["anomalies"] = {"rows": int(len(d)), "by_check": d["check"].value_counts().to_dict(),
                         "tickers_with_any_medium_or_high": int(d.loc[d["severity"].isin(["medium", "high"]), "ticker"].nunique())}
    summ["yf_calendar_local_tz_shift_count"] = int((s["yf_calendar_tz_shift"] == True).sum())  # noqa: E712
    return d


def ntm_table(s, summ):
    d = s.copy()
    d["abs_dev"] = (d["fwdPE_over_peNTM"] - 1).abs()
    d["gt10"] = d["abs_dev"] > 0.10
    d["fye_group"] = np.where(d["fye_month"] == 12, "Dec FYE", "non-Dec FYE")
    d["f_bucket"] = pd.cut(d["f_fy0_remaining"], [-0.001, 0.0001, 0.25, 0.5, 0.75, 1.0],
                           labels=["f=0 (FY0 ended)", "0<f<=0.25", "0.25<f<=0.5", "0.5<f<=0.75", "0.75<f<=1"])
    base = d[d["fwdPE_over_peNTM"].notna()]

    def agg(g):
        return pd.Series({"n": len(g), "n_gt10pct": int(g["gt10"].sum()), "share_gt10pct": g["gt10"].mean(),
                          "median_fwdPE_over_peNTM": g["fwdPE_over_peNTM"].median(),
                          "p10": g["fwdPE_over_peNTM"].quantile(0.1), "p90": g["fwdPE_over_peNTM"].quantile(0.9),
                          "share_yahoo_lower": (g["fwdPE_over_peNTM"] < 1).mean()})
    parts = [agg(base).to_frame().T.assign(group="ALL")]
    for col in ["fye_group", "f_bucket", "yahoo_fwd_horizon", "gics_sector"]:
        t = base.groupby(col, observed=True).apply(agg, include_groups=False).reset_index().rename(columns={col: "group"})
        t["group"] = col + "=" + t["group"].astype(str)
        parts.append(t)
    tab = pd.concat(parts, ignore_index=True)
    cols = ["group", "n", "n_gt10pct", "share_gt10pct", "median_fwdPE_over_peNTM", "p10", "p90", "share_yahoo_lower"]
    tab = tab[cols]
    tab.to_csv(OUT / "d4_ntm_vs_yahoo_table.csv", index=False)
    ex = base.sort_values("abs_dev", ascending=False)[["ticker", "price", "fy0_end", "f_fy0_remaining", "eps_fy0", "eps_fy1", "eps_ntm", "forwardEps", "forwardPE", "pe_fy0", "pe_ntm", "pe_fy1", "fwdPE_over_peNTM", "yahoo_fwd_horizon"]].head(25)
    summ["ntm"] = {"n_with_both": int(len(base)), "n_gt10pct": int(base["gt10"].sum()),
                   "share_gt10pct": float(base["gt10"].mean()),
                   "median_ratio": float(base["fwdPE_over_peNTM"].median()),
                   "horizon_counts": s["yahoo_fwd_horizon"].value_counts().to_dict(),
                   "pe_ntm_missing": s["pe_ntm_reason"].value_counts().to_dict(),
                   "top_deviations": ex.assign(fy0_end=ex["fy0_end"].astype(str)).round(3).to_dict("records"),
                   "qaware_vs_timeweighted_median_absdiff": float((s["eps_ntm_qaware"] / s["eps_ntm"] - 1).abs().median()),
                   "qaware_divergence_gt10pct_n": int(((s["eps_ntm_qaware"] / s["eps_ntm"] - 1).abs() > 0.10).sum())}
    # CNBC forward P/E: which horizon is it closest to?
    ip = pd.read_csv(DATA / "d4_indep_prices.csv")[["ticker", "cnbc_fpe", "cnbc_feps", "cnbc_eps_ttm"]]
    m = s.merge(ip, on="ticker", how="left")
    cand = {"FY0": m["pe_fy0"], "NTM": m["pe_ntm"], "FY1": m["pe_fy1"]}
    ok = m["cnbc_fpe"].notna() & m[["pe_fy0", "pe_ntm", "pe_fy1"]].notna().all(axis=1) & (m["cnbc_fpe"] > 0)
    devs = pd.DataFrame({k: (m.loc[ok, "cnbc_fpe"] / v[ok] - 1).abs() for k, v in cand.items()})
    closest = devs.idxmin(axis=1)
    summ["cnbc_fpe_closest_horizon"] = {"n": int(ok.sum()), "counts": closest.value_counts().to_dict(),
                                        "median_absdev_by_horizon": devs.median().round(4).to_dict(),
                                        "share_within_5pct_of_NTM": float((devs["NTM"] <= 0.05).mean()) if ok.any() else None}
    return tab


def main():
    s = pd.read_parquet(SNAP)
    summ = {"generated_utc": utc_now_iso(), "as_of": ASOF.isoformat(), "n_snapshot": int(len(s))}
    price_check(s, summ)
    mcap_check(s, summ)
    sec_check(s, summ)
    fye = fye_check(s, summ)
    anomalies(s, fye, summ)
    ntm_table(s, summ)
    summ["staleness"] = {"n_stale": int((s["regularMarketDate_ny"] != ASOF.isoformat()).sum()),
                         "stale": s.loc[s["regularMarketDate_ny"] != ASOF.isoformat(), ["ticker", "regularMarketDate_ny"]].to_dict("records"),
                         "regularMarketTime_utc_counts": s["regularMarketTime_utc"].value_counts().head(5).to_dict()}
    (OUT / "d4_validation_summary.json").write_text(json.dumps(summ, indent=1, default=str), encoding="utf-8")
    for fn, desc in [("d4_validation_prices.csv", "price vs Cboe close and CNBC last (tolerance 0.5%)"),
                     ("d4_validation_mcap.csv", "marketCap vs price*sharesOutstanding (tolerance 3%)"),
                     ("d4_validation_sec.csv", "SEC XBRL frames CY2025 vs Yahoo annual income statement (tolerance 2%)"),
                     ("d4_anomalies.csv", "long-format anomaly flags (ticker, check, severity, detail)")]:
        df = pd.read_csv(DATA / fn)
        write_meta(DATA / fn, {"description": desc, "rows": int(len(df)), "columns": list(df.columns),
                               "inputs": ["v4/data/d4_live_snapshot.parquet", "v4/data/d4_indep_prices.csv",
                                          "https://data.sec.gov/api/xbrl/frames/us-gaap/<Concept>/USD/CY2025.json",
                                          "https://data.sec.gov/submissions/CIK##########.json"],
                               "generated_by": "v4/code/d4_validate.py"})
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if not isinstance(vv, list)}) for k, v in summ.items()}, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
