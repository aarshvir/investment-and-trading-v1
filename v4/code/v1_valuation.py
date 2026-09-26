r"""
V1 -- Valuation analyst. Systematic, scripted, uniform valuation layer.

Methodology (see v4/outputs/v1_report.md for narrative):
  1. Inputs with lineage: D4 live snapshot (price, shares, NTM EPS, consensus, targets),
     D3 PIT monthly (TTM revenue/EBIT/D&A/capex/SBC/FCF, balance sheet), reconciled vs Yahoo TTM.
  2. Multiples in context: monthly trailing P/E and TTM FCF-yield history 2012-2026 built from
     D2 split-adjusted close (NOT dividend-adjusted, so it lines up with as-reported XBRL EPS after
     un-doing subsequent stock splits via D2 splits table) x D3 PIT shares/NI/OCF/capex. Current
     percentile of NTM P/E and FCF yield in that own history, and vs GICS sub-industry peers.
  3. Reverse DCF: operating companies solve for the constant-start, linearly-fading-to-3%,
     10-year FCFF growth that clears today's EV, FCFF = EBIT(1-t)+D&A-capex-dNWC, SBC NOT added
     back. WACC = E/(E+D)*CoE + D/(E+D)*CoD*(1-t); CoE = rf_10y + beta_adj*ERP, beta from 5y weekly
     total-return regression vs SPY, Blume-adjusted. REITs use an FFO proxy (NI+D&A) in place of
     EPS/P-E. Financials (banks/insurers/asset managers) use justified P/B = (ROE-g)/(COE-g), solved
     for the ROE the market price implies.
  4. Scenario values: bear/base/bull = the company's own historical 20th/50th/80th percentile of
     (revenue growth, net margin or ROE, share-count change) and exit multiple (P/E, P/FFO or P/B).
     No fixed +/-% shocks. Cumulative (flat) dividends added; annualised 3y return reported.
  5. Sanity checks: vs Street target range, SBC-adjusted FCF yield, WACC +/-1pt sensitivity of
     implied growth.

Run:  PYTHONPATH='C:\Users\user\eqv4\pylib' python v1_valuation.py
"""
import json
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq

warnings.filterwarnings("ignore")

V4 = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4")
DATA = V4 / "data"
OUT = V4 / "outputs"

ASOF = pd.Timestamp("2026-09-25")
HIST_START = pd.Timestamp("2012-01-01")

RF_3M = 0.0424
RF_10Y = 0.0517
ERP = 0.0414
TERM_G = 0.03
DEFAULT_TAX = 0.24
EXCLUDE = ["WBD", "KVUE", "TECH", "AES", "NSC", "D"]

# Manual net-debt / EV overrides for post-quarter events not yet in the latest 10-Q balance sheet
# (documented in d4_report.md #12). Units: USD. Populated ad hoc as names enter the run.
NET_DEBT_OVERRIDES = {
    "AME": 5.0e9,  # Indicor acquisition closed 2026-08-26, financed with debt
}

TOP60 = [
    "HST", "APA", "DLTR", "TRV", "CF", "ALL", "EXPE", "TGT", "BMY", "NEM",
    "SNDK", "JBHT", "SYF", "AIZ", "MPC", "UPS", "IVZ", "DG", "MU", "ALB",
    "VZ", "DECK", "EIX", "BBY", "TPR", "WDC", "BIIB", "FRT", "VLO", "DAL",
    "GL", "ALGN", "TROW", "EXPD", "FDX", "GD", "EOG", "SWK", "BAC", "PCAR",
    "HIG", "HAS", "CMCSA", "AMP", "ACGL", "UAL", "WSM", "GM", "LMT", "DVA",
    "ADBE", "SPG", "CNC", "CSX", "LVS", "PSA", "PSX", "CINF", "CMI", "COP",
]


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def sanitize_for_json(obj):
    """Recursively convert numpy/pandas scalars to native types and NaN/Inf -> None so the JSON
    output is strict-JSON-compliant (no bare NaN tokens) for downstream parsers."""
    if isinstance(obj, dict):
        return {str(k): sanitize_for_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [sanitize_for_json(v) for v in obj]
    if isinstance(obj, (np.floating, float)):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.bool_, bool)):
        return bool(obj)
    if isinstance(obj, (pd.Timestamp,)):
        return str(obj)
    if obj is None or isinstance(obj, (str, int)):
        return obj
    try:
        if pd.isna(obj):
            return None
    except (TypeError, ValueError):
        pass
    return str(obj)


# --------------------------------------------------------------------------------------
# Load
# --------------------------------------------------------------------------------------
def load_universe():
    prelim = pd.read_csv(OUT / "lead_prelim_rank.csv")
    tickers = list(TOP60)
    source_note = "top 60 of lead_prelim_rank.csv by `prelim` desc, excluding pending-takeover targets"
    b1_path = DATA / "b1_live_scores.csv"
    added_from_b1 = []
    if b1_path.exists():
        b1 = pd.read_csv(b1_path)
        tick_col = "ticker" if "ticker" in b1.columns else ("ticker_yahoo" if "ticker_yahoo" in b1.columns else None)
        comp_col = None
        for c in ["composite", "score", "b1_composite", "Composite"]:
            if c in b1.columns:
                comp_col = c
                break
        if comp_col and tick_col:
            b1c = b1.copy()
            if "exclude_pending_deal" in b1c.columns:
                b1c = b1c[~b1c["exclude_pending_deal"].fillna(False).astype(bool)]
            b1c = b1c[~b1c[tick_col].isin(EXCLUDE)]
            b1_top40 = b1c.sort_values(comp_col, ascending=False).head(70)[tick_col].tolist()  # lead 07:30: widened 40 -> 70 so every held name is valued
            added_from_b1 = [t for t in b1_top40 if t not in tickers]
            tickers += added_from_b1
            source_note += f"; + {len(added_from_b1)} names from b1_live_scores.csv top-40 by `{comp_col}` not already covered"
            log(f"b1_live_scores.csv loaded: top-40 by {comp_col}, {len(added_from_b1)} new names added: {added_from_b1}")
        else:
            log("b1_live_scores.csv found but composite/ticker columns not recognised:", b1.columns.tolist())
    else:
        log("b1_live_scores.csv not yet present -- proceeding with top-60 only (documented as an open item).")
    return tickers, prelim, added_from_b1, source_note


def load_data():
    d3 = pd.read_parquet(DATA / "d3_pit_monthly.parquet")
    d3["month_end"] = pd.to_datetime(d3["month_end"]).astype("datetime64[ns]")
    d4 = pd.read_parquet(DATA / "d4_live_snapshot.parquet")
    d1 = pd.read_csv(DATA / "d1_current_constituents.csv")
    splits = pd.read_parquet(DATA / "d2_splits.parquet")
    splits["date"] = pd.to_datetime(splits["date"]).astype("datetime64[ns]")
    close_wide = pd.read_parquet(DATA / "d2_close.parquet")
    if close_wide.index.name == "date":
        close_wide = close_wide.reset_index()
    close_wide["date"] = pd.to_datetime(close_wide["date"]).astype("datetime64[ns]")
    adj_wide = pd.read_parquet(DATA / "d2_adjclose.parquet")
    if adj_wide.index.name == "date":
        adj_wide = adj_wide.reset_index()
    adj_wide["date"] = pd.to_datetime(adj_wide["date"]).astype("datetime64[ns]")
    return d3, d4, d1, splits, close_wide, adj_wide


# --------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------
def split_factor_after(splits, ticker, asof=ASOF):
    """Cumulative forward-split multiple applied strictly after each date, through asof.
    Returns a function t -> factor (product of ratios for splits with date > t)."""
    s = splits[(splits["ticker"] == ticker) & (splits["date"] <= asof)].sort_values("date")
    dates = s["date"].values
    ratios = s["split_ratio"].values

    def factor(t):
        if len(dates) == 0:
            return 1.0
        mask = dates > np.datetime64(t)
        return float(np.prod(ratios[mask])) if mask.any() else 1.0

    return factor


def price_asof_series(wide, ticker):
    s = wide[["date", ticker]].dropna().sort_values("date").rename(columns={ticker: "price"})
    return s


def merge_asof_price(price_s, month_ends):
    idx = pd.DataFrame({"month_end": pd.to_datetime(month_ends)}).sort_values("month_end")
    m = pd.merge_asof(idx, price_s, left_on="month_end", right_on="date", direction="backward")
    return m.set_index("month_end")["price"]


def pct_rank_of_value(series, value):
    s = series.dropna()
    if len(s) < 8 or pd.isna(value):
        return np.nan
    return float((s < value).mean() * 100)


def hist_percentiles(series, qs=(20, 50, 80)):
    s = series.dropna()
    if len(s) < 8:
        return {q: np.nan for q in qs}
    return {q: float(np.nanpercentile(s, q)) for q in qs}


def cagr(series_by_date, years):
    s = series_by_date.dropna()
    if len(s) == 0:
        return np.nan
    end_date = s.index.max()
    start_target = end_date - pd.DateOffset(years=years)
    prior = s[s.index <= start_target]
    if prior.empty or s.loc[end_date] is None:
        return np.nan
    v0 = prior.iloc[-1]
    v1 = s.loc[end_date]
    if v0 is None or v1 is None or v0 <= 0 or v1 <= 0:
        return np.nan
    return (v1 / v0) ** (1 / years) - 1


def compute_beta(adj_wide, ticker, asof=ASOF, years=5):
    cols = [c for c in ["date", ticker, "SPY"] if c in adj_wide.columns]
    if ticker not in adj_wide.columns:
        return np.nan, np.nan
    df = adj_wide[["date", ticker, "SPY"]].dropna()
    start = asof - pd.DateOffset(years=years)
    df = df[(df["date"] > start) & (df["date"] <= asof)].sort_values("date")
    if len(df) < 100:
        return np.nan, np.nan
    wk = df.set_index("date").resample("W-FRI").last().dropna()
    rets = wk.pct_change().dropna()
    if len(rets) < 52:
        return np.nan, np.nan
    x = rets["SPY"].values
    y = rets[ticker].values
    beta_raw = float(np.cov(y, x, ddof=1)[0, 1] / np.var(x, ddof=1))
    beta_adj = (2 / 3) * beta_raw + (1 / 3) * 1.0
    return beta_raw, beta_adj


def build_ticker_monthly(d3t, close_s):
    """Per-ticker monthly PIT panel with market cap, P/E, FCF yield, P/B, P/FFO, ROE, margins."""
    d3t = d3t.sort_values("month_end").copy()
    d3t = d3t[d3t["month_end"] >= HIST_START - pd.DateOffset(years=1)]
    px = merge_asof_price(close_s, d3t["month_end"])
    d3t = d3t.set_index("month_end")
    d3t["px"] = px
    sf = split_factor_after(SPLITS_G, d3t["ticker"].iloc[0]) if len(d3t) else (lambda t: 1.0)
    d3t["split_factor_after"] = [sf(t) for t in d3t.index]
    d3t["shares_wdil_eff"] = d3t["shares_wdil"].fillna(d3t["shares_out"])
    d3t["mcap_pit"] = d3t["px"] * d3t["shares_wdil_eff"] * d3t["split_factor_after"]
    d3t["pe_ttm"] = np.where(d3t["ni_ttm"] > 0, d3t["mcap_pit"] / d3t["ni_ttm"], np.nan)
    d3t["fcf_ttm"] = d3t["ocf_ttm"] - d3t["capex_ttm"]
    d3t["fcf_yield_ttm"] = np.where(d3t["mcap_pit"] > 0, d3t["fcf_ttm"] / d3t["mcap_pit"], np.nan)
    d3t["ffo_proxy_ttm"] = d3t["ni_ttm"] + d3t["da_ttm"]
    d3t["pffo_ttm"] = np.where(d3t["ffo_proxy_ttm"] > 0, d3t["mcap_pit"] / d3t["ffo_proxy_ttm"], np.nan)
    d3t["ffo_yield_ttm"] = np.where(d3t["mcap_pit"] > 0, d3t["ffo_proxy_ttm"] / d3t["mcap_pit"], np.nan)
    d3t["ffo_margin_ttm"] = np.where(d3t["rev_ttm"] > 0, d3t["ffo_proxy_ttm"] / d3t["rev_ttm"], np.nan)
    d3t["pb_ttm"] = np.where(d3t["equity"] > 0, d3t["mcap_pit"] / d3t["equity"], np.nan)
    d3t["roe_ttm"] = np.where(d3t["equity"] > 0, d3t["ni_ttm"] / d3t["equity"], np.nan)
    d3t["net_margin_ttm"] = np.where(d3t["rev_ttm"] > 0, d3t["ni_ttm"] / d3t["rev_ttm"], np.nan)
    d3t["ebit_margin_ttm"] = np.where(d3t["rev_ttm"] > 0, d3t["ebit_ttm"] / d3t["rev_ttm"], np.nan)
    d3t["da_ratio_ttm"] = np.where(d3t["rev_ttm"] > 0, d3t["da_ttm"] / d3t["rev_ttm"], np.nan)
    d3t["capex_ratio_ttm"] = np.where(d3t["rev_ttm"] > 0, d3t["capex_ttm"] / d3t["rev_ttm"], np.nan)
    d3t["rev_yoy"] = d3t["rev_ttm"] / d3t["rev_ttm"].shift(12) - 1
    d3t["shares_yoy"] = d3t["shares_out"] / d3t["shares_1y_ago"] - 1
    d3t["nwc"] = (d3t["assets_current"] - d3t["cash_sti"]) - d3t["liab_current"]
    d3t["dnwc_ttm"] = d3t["nwc"] - d3t["nwc"].shift(12)
    return d3t


# --------------------------------------------------------------------------------------
# Reverse DCF (operating companies)
# --------------------------------------------------------------------------------------
def reverse_dcf_growth(ev0, rev0, margin, da_ratio, capex_ratio, nwc_ratio, tax, wacc, term_g=TERM_G, n=10):
    def fcff_path_pv(g_start):
        rev = rev0
        pv = 0.0
        fcff_prev_year_rev = rev0
        for t in range(1, n + 1):
            g_t = g_start - (g_start - term_g) * (t - 1) / (n - 1)
            rev_new = rev * (1 + g_t)
            ebit = rev_new * margin
            da = rev_new * da_ratio
            capex = rev_new * capex_ratio
            dnwc = nwc_ratio * (rev_new - rev)
            fcff = ebit * (1 - tax) + da - capex - dnwc
            pv += fcff / (1 + wacc) ** t
            rev = rev_new
            if t == n:
                tv = fcff * (1 + term_g) / (wacc - term_g)
                pv += tv / (1 + wacc) ** n
        return pv

    def obj(g):
        return fcff_path_pv(g) - ev0

    try:
        lo, hi = -0.30, 0.80
        flo, fhi = obj(lo), obj(hi)
        if np.isnan(flo) or np.isnan(fhi):
            return np.nan
        if flo > 0:
            return -0.30  # even -30% start growth overshoots EV -> deeply "priced for" a floor below -30%
        if fhi < 0:
            return 0.80  # even 80% start growth undershoots EV -> priced for more than 80%
        return float(brentq(obj, lo, hi, xtol=1e-6, maxiter=200))
    except Exception:
        return np.nan


def pb_implied_roe(pb, coe, g=TERM_G):
    if pb is None or np.isnan(pb) or np.isnan(coe) or coe <= g:
        return np.nan
    return g + pb * (coe - g)


# --------------------------------------------------------------------------------------
# Main per-ticker build
# --------------------------------------------------------------------------------------
def classify(ticker, d3t_last, gics_sector):
    """GICS sector is authoritative (banks/insurers/asset managers = Financials). D3's SIC-derived
    is_financial flag is only a fallback when GICS sector is unavailable -- it over-fires on names
    like health insurers (SIC 6324) that GICS correctly places outside Financials (e.g. CNC)."""
    if gics_sector is not None and pd.notna(gics_sector):
        if gics_sector == "Real Estate":
            return "reit"
        if gics_sector == "Financials":
            return "financial"
        return "operating"
    is_fin = bool(d3t_last.get("is_financial", False))
    return "financial" if is_fin else "operating"


def safe_div(a, b):
    try:
        if b in (0, None) or pd.isna(b) or pd.isna(a):
            return np.nan
        return a / b
    except Exception:
        return np.nan


def build_one(ticker, d3, d4, d1, close_wide, adj_wide, peer_stats):
    out = {"ticker": ticker, "conflicts": [], "flags": []}
    d3t_all = d3[d3["ticker"] == ticker]
    if d3t_all.empty:
        out["error"] = "no D3 data"
        return out
    d4r = d4[d4["ticker"] == ticker]
    if d4r.empty:
        out["error"] = "no D4 data"
        return out
    d4r = d4r.iloc[0]
    d1r = d1[d1["ticker_yahoo"] == ticker]
    gics_sector = d1r["gics_sector"].iloc[0] if not d1r.empty else d4r.get("gics_sector")
    gics_sub = d1r["gics_sub_industry"].iloc[0] if not d1r.empty else d4r.get("gics_sub_industry")

    close_s = price_asof_series(close_wide, ticker)
    panel = build_ticker_monthly(d3t_all, close_s)
    panel_hist = panel[(panel.index >= HIST_START) & (panel.index <= ASOF)]
    last = panel.iloc[-1]
    last_date = panel.index[-1]
    out["as_of"] = {"d3_month_end": str(last_date.date()), "price_date": "2026-09-25"}

    kind = classify(ticker, last, gics_sector)
    out["classification"] = kind
    out["sector"] = gics_sector
    out["sub_industry"] = gics_sub

    # ---- Inputs with lineage ----
    price = float(d4r["price"]) if pd.notna(d4r["price"]) else float(close_s["price"].iloc[-1])
    shares_d4 = d4r.get("impliedSharesOutstanding") or d4r.get("sharesOutstanding")
    shares_d3 = last.get("shares_wdil_eff")
    shares = float(shares_d3) if pd.notna(shares_d3) else float(shares_d4)
    total_debt_d3 = last.get("total_debt")
    cash_d3 = last.get("cash_sti")
    net_debt = None
    src_debt = "D3 latest 10-Q (total_debt - cash_sti)"
    if pd.notna(total_debt_d3) and pd.notna(cash_d3):
        net_debt = float(total_debt_d3 - cash_d3)
    else:
        td4, tc4 = d4r.get("totalDebt"), d4r.get("totalCash")
        if pd.notna(td4) and pd.notna(tc4):
            net_debt = float(td4 - tc4)
            src_debt = "D4/Yahoo (totalDebt - totalCash), D3 balance-sheet fields missing"
    override_note = None
    if ticker in NET_DEBT_OVERRIDES and net_debt is not None:
        net_debt += NET_DEBT_OVERRIDES[ticker]
        override_note = f"+{NET_DEBT_OVERRIDES[ticker]/1e9:.1f}bn manual add for post-quarter M&A financing"
    mcap_now = price * shares
    ev0 = mcap_now + (net_debt if net_debt is not None else 0.0)

    eps_ntm = d4r.get("eps_ntm")
    eps_fy0, eps_fy1 = d4r.get("eps_fy0"), d4r.get("eps_fy1")
    rev_fy0, rev_fy1 = d4r.get("rev_fy0"), d4r.get("rev_fy1")
    rev_ttm_d3, ebit_ttm_d3 = last.get("rev_ttm"), last.get("ebit_ttm")
    da_ttm, capex_ttm, sbc_ttm = last.get("da_ttm"), last.get("capex_ttm"), last.get("sbc_ttm")
    ocf_ttm, ni_ttm = last.get("ocf_ttm"), last.get("ni_ttm")
    fcf_ttm = last.get("fcf_ttm")

    rev_ttm_yahoo = d4r.get("totalRevenue")
    if pd.notna(rev_ttm_yahoo) and pd.notna(rev_ttm_d3) and rev_ttm_d3 != 0:
        diff = abs(rev_ttm_yahoo - rev_ttm_d3) / abs(rev_ttm_d3)
        if diff > 0.05:
            out["conflicts"].append(
                f"D3 TTM revenue {rev_ttm_d3:,.0f} vs Yahoo TTM {rev_ttm_yahoo:,.0f} differ {diff:.1%}"
            )

    # Revenue-base sanity guard: some D3 `rev_ttm` concept picks (e.g. APA) resolve to a partial
    # revenue line, producing an implausible implied EBIT margin. Fall back to Yahoo TTM revenue
    # for the reverse-DCF/scenario revenue base when that happens, and record it as a conflict.
    rev0_dcf = rev_ttm_d3
    rev0_source = "D3 rev_ttm"
    margin_check = safe_div(ebit_ttm_d3, rev_ttm_d3) if pd.notna(rev_ttm_d3) and rev_ttm_d3 > 0 else np.nan
    if pd.isna(rev0_dcf) or (pd.notna(rev0_dcf) and rev0_dcf <= 0) or (pd.notna(margin_check) and (margin_check > 0.65 or margin_check < -1.5)):
        if pd.notna(rev_ttm_yahoo) and rev_ttm_yahoo > 0:
            out["conflicts"].append(
                f"D3 TTM revenue ({rev_ttm_d3}) implies an implausible EBIT margin ({margin_check}); "
                f"reverse-DCF/scenario revenue base switched to Yahoo TTM revenue {rev_ttm_yahoo:,.0f}"
            )
            rev0_dcf = float(rev_ttm_yahoo)
            rev0_source = "Yahoo TTM revenue (D3 revenue concept implausible)"
        else:
            out["flags"].append(f"D3 revenue implausible (EBIT margin {margin_check}) and no Yahoo fallback available")

    # Capex sanity: an exact 0 alongside positive D&A is a missing-tag artefact for asset-heavy
    # operating names, not a genuine zero-capex business. Proxy with D&A (~maintenance capex) and flag.
    capex_ttm_eff = capex_ttm
    if (pd.isna(capex_ttm) or capex_ttm == 0) and pd.notna(da_ttm) and da_ttm > 0:
        capex_ttm_eff = da_ttm
        out["flags"].append("capex_ttm missing/zero in D3; proxied with D&A (~maintenance capex) for reverse DCF")

    out["inputs"] = {
        "price_2026_09_25": price, "price_source": "D4 live_snapshot.price (cross-checked Cboe/CNBC)",
        "diluted_shares": shares, "shares_source": "D3 shares_wdil (fallback D4 implied/sharesOutstanding)",
        "net_debt": net_debt, "net_debt_source": src_debt, "net_debt_override": override_note,
        "market_cap": mcap_now, "ev0": ev0,
        "eps_ntm": eps_ntm, "eps_fy0": eps_fy0, "eps_fy1": eps_fy1,
        "rev_fy0": rev_fy0, "rev_fy1": rev_fy1,
        "ntm_quality": d4r.get("ntm_quality"),
        "ttm_revenue_d3": rev_ttm_d3, "ttm_revenue_yahoo": rev_ttm_yahoo,
        "ttm_ebit_d3": ebit_ttm_d3, "ttm_da_d3": da_ttm, "ttm_capex_d3": capex_ttm,
        "ttm_sbc_d3": sbc_ttm, "ttm_ocf_d3": ocf_ttm, "ttm_ni_d3": ni_ttm, "ttm_fcf_d3": fcf_ttm,
    }

    # ---- Multiples in context ----
    pe_ntm = d4r.get("pe_ntm")
    fcf_yield_now = d4r.get("fcf_yield")
    if pd.isna(fcf_yield_now) and fcf_ttm is not None and mcap_now:
        fcf_yield_now = fcf_ttm / mcap_now
    if kind == "reit":
        own_metric_series = panel_hist["pffo_ttm"]
        own_yield_series = panel_hist["ffo_yield_ttm"]
        ffo_now = last.get("ffo_proxy_ttm")
        p_metric_now = safe_div(mcap_now, ffo_now)
        yield_now = safe_div(ffo_now, mcap_now)
        metric_label = "P/FFO(proxy)"
    elif kind == "financial":
        own_metric_series = panel_hist["pb_ttm"]
        own_yield_series = panel_hist["roe_ttm"]
        p_metric_now = safe_div(mcap_now, last.get("equity"))
        yield_now = safe_div(ni_ttm, last.get("equity"))
        metric_label = "P/B"
    else:
        own_metric_series = panel_hist["pe_ttm"]
        own_yield_series = panel_hist["fcf_yield_ttm"]
        p_metric_now = pe_ntm if pd.notna(pe_ntm) else safe_div(mcap_now, ni_ttm)
        yield_now = fcf_yield_now
        metric_label = "NTM P/E"

    pctl_metric = pct_rank_of_value(own_metric_series, p_metric_now)
    pctl_yield = pct_rank_of_value(own_yield_series, yield_now)
    n_months_hist = int(own_metric_series.dropna().shape[0])

    peer = peer_stats.get(gics_sub, {})
    peer_metric_note = None
    if kind == "financial":
        peer_median_metric = peer.get("median_pb")
    elif kind == "reit":
        peer_median_metric = peer.get("median_pe_ntm")
        peer_metric_note = "peer set has no FFO data available; peer comparison uses NTM P/E as a rough proxy (own-history column is true P/FFO) -- treat with caution"
        out["flags"].append("REIT peer comparison metric is NTM P/E (proxy), not P/FFO -- FFO peer data unavailable")
    else:
        peer_median_metric = peer.get("median_pe_ntm")
    out["multiples"] = {
        "metric_label": metric_label, "value_now": p_metric_now, "own_history_percentile": pctl_metric,
        "own_history_months": n_months_hist,
        "yield_now": yield_now, "yield_own_history_percentile": pctl_yield,
        "peer_gics_sub_industry": gics_sub, "peer_median_metric": peer_median_metric, "peer_metric_note": peer_metric_note,
        "peer_n": peer.get("n"), "peer_tickers_sample": peer.get("sample"),
        "ntm_pe": pe_ntm, "fcf_yield_ttm": fcf_yield_now,
    }
    if n_months_hist < 60:
        out["flags"].append(f"only {n_months_hist} months of own-history for percentile (short/limited history)")

    # ---- Beta / cost of capital ----
    beta_raw, beta_adj = compute_beta(adj_wide, ticker)
    coe = RF_10Y + (beta_adj if pd.notna(beta_adj) else 1.0) * ERP
    tax_ttm, pretax_ttm = last.get("tax_ttm"), last.get("pretax_ttm")
    tax_rate = safe_div(tax_ttm, pretax_ttm)
    if pd.isna(tax_rate) or tax_rate < 0.05 or tax_rate > 0.40:
        tax_rate = DEFAULT_TAX
    interest_ttm = last.get("interest_ttm")
    cod_pretax = safe_div(interest_ttm, total_debt_d3)
    if pd.isna(cod_pretax) or cod_pretax <= 0 or cod_pretax > 0.15 or not net_debt or total_debt_d3 in (None, 0) or pd.isna(total_debt_d3):
        cod_pretax = RF_10Y + 0.015
    D = float(total_debt_d3) if pd.notna(total_debt_d3) else 0.0
    E = mcap_now
    wacc = (E / (E + D)) * coe + (D / (E + D)) * cod_pretax * (1 - tax_rate) if (E + D) > 0 else coe

    out["cost_of_capital"] = {
        "beta_raw_5y_weekly": beta_raw, "beta_blume_adj": beta_adj,
        "rf_10y": RF_10Y, "erp": ERP, "cost_of_equity": coe,
        "cost_of_debt_pretax": cod_pretax, "tax_rate": tax_rate, "wacc": wacc,
    }

    hist_growth_5y = cagr(panel_hist["rev_ttm"], 5)
    hist_growth_10y = cagr(panel_hist["rev_ttm"], 10)
    if pd.notna(rev_fy0) and pd.notna(rev_fy1) and rev_fy0 != 0:
        consensus_growth = (rev_fy1 - rev_fy0) / rev_fy0
    else:
        consensus_growth = d4r.get("rev_fy1_growth")

    if kind == "financial":
        pb_now = safe_div(mcap_now, last.get("equity"))
        roe_hist = hist_percentiles(panel_hist["roe_ttm"])
        roe_actual_ttm = last.get("roe_ttm")
        roe_implied = pb_implied_roe(pb_now, coe, TERM_G)
        roe_sens = {
            "coe_minus1pt": pb_implied_roe(pb_now, coe - 0.01, TERM_G),
            "coe": roe_implied,
            "coe_plus1pt": pb_implied_roe(pb_now, coe + 0.01, TERM_G),
        }
        out["valuation_model"] = {
            "method": "justified P/B = (ROE-g)/(COE-g)", "pb_now": pb_now, "coe": coe, "g_terminal": TERM_G,
            "roe_implied": roe_implied, "roe_actual_ttm": roe_actual_ttm,
            "roe_hist_p20_p50_p80": roe_hist,
            "priced_for_vs_delivered": {"implied": roe_implied, "delivered_ttm": roe_actual_ttm,
                                         "delivered_p50_hist": roe_hist.get(50)},
            "sensitivity_coe_pm1pt": roe_sens,
        }
        implied_g_display = roe_implied
    else:
        # Both "operating" and "reit" use the FCFF reverse DCF here (REITs get FFO-based treatment
        # in the multiples and scenario sections instead); FCFF needs the EBIT margin either way.
        margin_hist_series = panel_hist["ebit_margin_ttm"]
        margin_current = safe_div(ebit_ttm_d3, rev0_dcf)
        margin_hist_median = float(np.nanmedian(margin_hist_series)) if margin_hist_series.notna().sum() >= 6 else np.nan
        MARGIN_FLOOR = 0.005
        if pd.notna(margin_current) and margin_current > MARGIN_FLOOR:
            margin = margin_current
        elif pd.notna(margin_hist_median) and margin_hist_median > MARGIN_FLOOR:
            margin = margin_hist_median
            out["flags"].append(
                f"current TTM EBIT margin ({margin_current}) <= 0; reverse DCF used own full-history "
                f"median margin ({margin_hist_median:.1%}) instead, so implied growth also embeds a margin-recovery assumption"
            )
        else:
            margin = np.nan
        rev0 = rev0_dcf
        da_hist_med = float(np.nanmedian(panel_hist["da_ratio_ttm"])) if panel_hist["da_ratio_ttm"].notna().sum() >= 6 else np.nan
        capex_hist_med = float(np.nanmedian(panel_hist["capex_ratio_ttm"])) if panel_hist["capex_ratio_ttm"].notna().sum() >= 6 else np.nan
        da_ratio = safe_div(da_ttm, rev0)
        if pd.isna(da_ratio) or da_ratio == 0:
            if pd.notna(da_hist_med) and da_hist_med > 0:
                da_ratio = da_hist_med
                out["flags"].append(f"da_ttm missing/zero; used own full-history median D&A/revenue ({da_hist_med:.1%})")
        capex_ratio = safe_div(capex_ttm_eff, rev0)
        if pd.isna(capex_ratio) or capex_ratio == 0:
            if pd.notna(capex_hist_med) and capex_hist_med > 0:
                capex_ratio = capex_hist_med
                out["flags"].append(f"capex_ttm missing/zero; used own full-history median capex/revenue ({capex_hist_med:.1%})")
            elif pd.notna(da_ratio) and da_ratio > 0:
                capex_ratio = da_ratio
        nwc_ratio = safe_div(last.get("nwc"), rev0)
        for nm, v in [("da_ratio", da_ratio), ("capex_ratio", capex_ratio), ("nwc_ratio", nwc_ratio)]:
            if pd.isna(v):
                out["flags"].append(f"{nm} unavailable after all fallbacks, treated as 0 in reverse DCF")
        da_zero_but_capex_material = (pd.isna(da_ratio) or da_ratio == 0) and (pd.notna(capex_ratio) and capex_ratio > 0.02)
        da_ratio = 0.0 if pd.isna(da_ratio) else da_ratio
        capex_ratio = 0.0 if pd.isna(capex_ratio) else capex_ratio
        nwc_ratio = 0.0 if pd.isna(nwc_ratio) else nwc_ratio
        if pd.isna(rev0) or pd.isna(margin) or rev0 <= 0:
            implied_g = np.nan
            sens = {}
            out["flags"].append("reverse DCF not solvable: no usable positive EBIT margin (current or historical)")
        elif da_zero_but_capex_material:
            implied_g = np.nan
            sens = {}
            out["flags"].append(
                "reverse DCF suppressed: D&A is unavailable (own full multi-year history, not just latest quarter) "
                "while capex is material -- FCFF would be structurally understated and implied growth meaningless"
            )
        else:
            implied_g = reverse_dcf_growth(ev0, rev0, margin, da_ratio, capex_ratio, nwc_ratio, tax_rate, wacc)
            sens = {
                "wacc_minus1pt": reverse_dcf_growth(ev0, rev0, margin, da_ratio, capex_ratio, nwc_ratio, tax_rate, wacc - 0.01),
                "wacc": implied_g,
                "wacc_plus1pt": reverse_dcf_growth(ev0, rev0, margin, da_ratio, capex_ratio, nwc_ratio, tax_rate, wacc + 0.01),
            }
        out["valuation_model"] = {
            "method": "reverse DCF (FCFF, SBC not added back, 10y fade to 3% terminal)",
            "ebit_ttm": ebit_ttm_d3, "da_ttm": da_ttm, "capex_ttm": capex_ttm, "sbc_ttm": sbc_ttm,
            "revenue_base": rev0, "revenue_base_source": rev0_source,
            "dnwc_ttm": last.get("dnwc_ttm"), "ebit_margin_used": margin,
            "da_ratio": da_ratio, "capex_ratio": capex_ratio, "nwc_ratio": nwc_ratio,
            "ev0": ev0, "wacc": wacc, "implied_10y_growth": implied_g,
            "consensus_fy1_growth": consensus_growth, "historical_cagr_5y": hist_growth_5y,
            "historical_cagr_10y": hist_growth_10y,
            "priced_for_vs_delivered": {"implied": implied_g,
                                         "delivered_5y": hist_growth_5y, "delivered_10y": hist_growth_10y,
                                         "consensus_fy1": consensus_growth},
            "sensitivity_wacc_pm1pt": sens,
        }
        implied_g_display = implied_g

    # ---- Scenario values ----
    div_ttm = last.get("div_ttm")
    dps0 = safe_div(div_ttm, shares) if pd.notna(div_ttm) else 0.0
    dps0 = 0.0 if pd.isna(dps0) else dps0
    sg_hist = hist_percentiles(panel_hist["shares_yoy"])

    if kind == "financial":
        pb_hist = hist_percentiles(panel_hist["pb_ttm"])
        equity0 = last.get("equity")
        bv0 = safe_div(equity0, shares)
        payout = float(np.clip(safe_div(div_ttm, ni_ttm) if pd.notna(div_ttm) and pd.notna(ni_ttm) else 0.3, 0, 0.9))
        scen_defs = {"bear": (20, 80), "base": (50, 50), "bull": (80, 20)}
        scenarios = {}
        for name, (roe_q, sg_q) in scen_defs.items():
            roe_s = roe_hist.get(roe_q)
            sg_s = sg_hist.get(sg_q, 0.0)
            pb_s = pb_hist.get(roe_q)
            if pd.isna(roe_s) or pd.isna(bv0):
                scenarios[name] = {"error": "insufficient history"}
                continue
            sg_s = 0.0 if pd.isna(sg_s) else sg_s
            bv, sh = equity0, shares
            for _ in range(3):
                bv = bv * (1 + roe_s * (1 - payout))
                sh = sh * (1 + sg_s)
            bvps3 = bv / sh
            exit_mult = pb_s if pd.notna(pb_s) else pb_now
            price3 = bvps3 * exit_mult if pd.notna(exit_mult) else np.nan
            cum_div = dps0 * 3
            total3 = price3 + cum_div if pd.notna(price3) else np.nan
            ann_ret = (total3 / price) ** (1 / 3) - 1 if pd.notna(total3) and price > 0 else np.nan
            scenarios[name] = {"roe_assumed": roe_s, "share_count_cagr": sg_s, "exit_pb": exit_mult,
                                "bvps_yr3": bvps3, "price_yr3": price3, "cum_dividends": cum_div,
                                "value_yr3_total": total3, "annualised_return_3y": ann_ret}
    else:
        # Scenario EPS/FFOPS build always needs the BOTTOM-LINE margin (net income, or FFO for REITs)
        # -- NOT the EBIT margin used upstream for the FCFF reverse DCF -- since it feeds a P/E-style
        # (or P/FFO-style) exit multiple directly onto per-share earnings.
        rg_hist = hist_percentiles(panel_hist["rev_yoy"])
        bottom_line_margin_series = panel_hist["ffo_margin_ttm"] if kind == "reit" else panel_hist["net_margin_ttm"]
        mg_hist = hist_percentiles(bottom_line_margin_series)
        pe_hist = hist_percentiles(own_metric_series)
        scen_defs = {"bear": (20, 20, 80, 20), "base": (50, 50, 50, 50), "bull": (80, 80, 20, 80)}
        scenarios = {}
        ni0 = ni_ttm if kind != "reit" else last.get("ffo_proxy_ttm")
        for name, (g_q, m_q, sg_q, x_q) in scen_defs.items():
            g_s, m_s, x_s = rg_hist.get(g_q), mg_hist.get(m_q), pe_hist.get(x_q)
            sg_s = sg_hist.get(sg_q, 0.0)
            sg_s = 0.0 if pd.isna(sg_s) else sg_s
            if pd.isna(g_s) or pd.isna(m_s) or pd.isna(rev0) or rev0 <= 0:
                scenarios[name] = {"error": "insufficient history"}
                continue
            rev3 = rev0 * (1 + g_s) ** 3
            ni3 = rev3 * m_s
            sh3 = shares * (1 + sg_s) ** 3
            eps3 = safe_div(ni3, sh3)
            exit_mult = x_s
            price3 = eps3 * exit_mult if pd.notna(eps3) and pd.notna(exit_mult) else np.nan
            cum_div = dps0 * 3
            total3 = price3 + cum_div if pd.notna(price3) else np.nan
            ann_ret = (total3 / price) ** (1 / 3) - 1 if pd.notna(total3) and price > 0 and total3 > 0 else np.nan
            scenarios[name] = {"revenue_growth_assumed": g_s, "margin_assumed": m_s, "share_count_cagr": sg_s,
                                "exit_multiple": exit_mult, "eps_or_ffops_yr3": eps3, "price_yr3": price3,
                                "cum_dividends": cum_div, "value_yr3_total": total3,
                                "annualised_return_3y": ann_ret}
    out["scenarios"] = scenarios

    # ---- Sanity checks ----
    t_low, t_mean, t_high = d4r.get("target_low"), d4r.get("target_mean"), d4r.get("target_high")
    base_val = scenarios.get("base", {}).get("value_yr3_total") or scenarios.get("base", {}).get("price_yr3")
    street_flag = None
    if pd.notna(t_high) and pd.notna(base_val):
        if base_val > t_high:
            street_flag = "base 3y value exceeds Street 12m high target"
        elif pd.notna(t_low) and base_val < t_low:
            street_flag = "base 3y value below Street 12m low target"
        else:
            street_flag = "within Street 12m target range"
    sbc_adj_fcf_yield = None
    if fcf_ttm is not None and pd.notna(sbc_ttm) and mcap_now:
        sbc_adj_fcf_yield = (fcf_ttm - sbc_ttm) / mcap_now
    out["sanity"] = {
        "street_target_low": t_low, "street_target_mean": t_mean, "street_target_high": t_high,
        "street_flag": street_flag, "sbc_adjusted_fcf_yield": sbc_adj_fcf_yield,
    }

    # ---- Verdict ----
    def clip(v, lo, hi):
        return max(lo, min(hi, v))

    score = 0.0
    n_comp = 0
    if pd.notna(pctl_metric):
        score += clip(-(pctl_metric - 50) / 50, -1, 1) * 0.30
        n_comp += 0.30
    if kind == "financial":
        if pd.notna(roe_implied) and pd.notna(roe_actual_ttm):
            score += clip((roe_actual_ttm - roe_implied) / 0.06, -1, 1) * 0.35
            n_comp += 0.35
    else:
        achievable = np.nanmax([x for x in [hist_growth_5y, consensus_growth] if x is not None and pd.notna(x)]) if any(
            pd.notna(x) for x in [hist_growth_5y, consensus_growth]) else np.nan
        if pd.notna(implied_g_display) and pd.notna(achievable):
            score += clip((achievable - implied_g_display) / 0.15, -1, 1) * 0.35
            n_comp += 0.35
    base_ret = scenarios.get("base", {}).get("annualised_return_3y")
    if pd.notna(base_ret):
        hurdle = wacc if kind != "financial" else coe
        score += clip((base_ret - hurdle) / 0.10, -1, 1) * 0.35
        n_comp += 0.35
    final_score = score / n_comp if n_comp > 0 else np.nan
    if pd.isna(final_score):
        verdict = "insufficient data"
    elif final_score > 0.30:
        verdict = "attractive"
    elif final_score > -0.10:
        verdict = "fair"
    elif final_score > -0.40:
        verdict = "demanding"
    else:
        verdict = "excessive"
    out["verdict"] = {"label": verdict, "score": final_score,
                       "formula": "0.30*(-(ownPctl-50)/50) + 0.35*(achievable-implied)/15pt_or_(actualROE-impliedROE)/6pt + 0.35*(baseReturn-hurdle)/10pt, clipped [-1,1] each"}
    return out


# --------------------------------------------------------------------------------------
# Peer stats (GICS sub-industry, full 503 universe)
# --------------------------------------------------------------------------------------
def build_peer_stats(d4, d1):
    m = d4.merge(
        d1[["ticker_yahoo", "gics_sub_industry"]].rename(columns={"gics_sub_industry": "gics_sub_industry_d1"}),
        left_on="ticker", right_on="ticker_yahoo", how="left",
    )
    m["gics_sub_industry"] = m["gics_sub_industry_d1"].fillna(m.get("gics_sub_industry")).fillna(m["gics_sector"])
    m["pb_calc"] = m["price"] / m["y_bookValue"].replace(0, np.nan)
    stats = {}
    for sub, g in m.groupby("gics_sub_industry"):
        stats[sub] = {
            "n": int(len(g)),
            "median_pe_ntm": float(g["pe_ntm"].median(skipna=True)) if g["pe_ntm"].notna().any() else np.nan,
            "median_pb": float(g["pb_calc"].median(skipna=True)) if g["pb_calc"].notna().any() else np.nan,
            "sample": g["ticker"].head(5).tolist(),
        }
    return stats


def main():
    tickers, prelim_df, added_from_b1, source_note = load_universe()
    log(f"Universe: {len(tickers)} tickers. {source_note}")
    d3, d4, d1, splits, close_wide, adj_wide = load_data()
    global SPLITS_G
    SPLITS_G = splits

    peer_stats = build_peer_stats(d4, d1)

    results = {}
    for i, t in enumerate(tickers):
        try:
            log(f"[{i+1}/{len(tickers)}] {t}")
            results[t] = build_one(t, d3, d4, d1, close_wide, adj_wide, peer_stats)
        except Exception as e:
            log(f"  ERROR {t}: {e}")
            results[t] = {"ticker": t, "error": str(e)}

    meta = {
        "as_of": "2026-09-25", "generated": pd.Timestamp.utcnow().isoformat(),
        "universe_note": source_note, "n_tickers": len(tickers),
        "added_from_b1_live_scores": added_from_b1,
        "assumptions": {"rf_10y": RF_10Y, "rf_3m": RF_3M, "erp": ERP, "terminal_growth": TERM_G,
                         "beta_window": "5y weekly total return vs SPY, Blume-adjusted (2/3 raw + 1/3*1.0)",
                         "default_tax_rate_fallback": DEFAULT_TAX},
    }
    payload = {"meta": meta, "companies": results}
    payload = sanitize_for_json(payload)
    with open(OUT / "v1_valuation.json", "w") as f:
        json.dump(payload, f, indent=2, allow_nan=False)

    # ---- summary table ----
    rows = []
    for t, r in results.items():
        if "error" in r and "verdict" not in r:
            rows.append({"ticker": t, "error": r.get("error")})
            continue
        mult = r.get("multiples", {})
        vm = r.get("valuation_model", {})
        scen = r.get("scenarios", {})
        rows.append({
            "ticker": t, "sector": r.get("sector"), "sub_industry": r.get("sub_industry"),
            "classification": r.get("classification"),
            "metric_label": mult.get("metric_label"), "metric_value": mult.get("value_now"),
            "own_history_percentile": mult.get("own_history_percentile"),
            "peer_median": mult.get("peer_median_metric"),
            "implied_growth_or_roe": vm.get("implied_10y_growth", vm.get("roe_implied")),
            "delivered_5y_or_actual_roe": vm.get("historical_cagr_5y", vm.get("roe_actual_ttm")),
            "consensus_fy1_growth": vm.get("consensus_fy1_growth"),
            "wacc_or_coe": vm.get("wacc", vm.get("coe")),
            "bear_ann_return_3y": scen.get("bear", {}).get("annualised_return_3y"),
            "base_ann_return_3y": scen.get("base", {}).get("annualised_return_3y"),
            "bull_ann_return_3y": scen.get("bull", {}).get("annualised_return_3y"),
            "street_flag": r.get("sanity", {}).get("street_flag"),
            "sbc_adj_fcf_yield": r.get("sanity", {}).get("sbc_adjusted_fcf_yield"),
            "verdict": r.get("verdict", {}).get("label"),
            "verdict_score": r.get("verdict", {}).get("score"),
        })
    tbl = pd.DataFrame(rows)
    tbl.to_csv(OUT / "v1_valuation_table.csv", index=False)
    log("Wrote v1_valuation.json and v1_valuation_table.csv")
    return tbl, meta


if __name__ == "__main__":
    main()
