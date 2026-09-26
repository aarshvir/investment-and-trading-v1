"""b1_panel.py - point-in-time stock-month panel for the B1 backtest engine.

Steps (all point-in-time):
 1. month-end calendar (last NYSE trading day; 2026-09 = 2026-09-25 live date)
 2. PIT membership (D1 d1_membership_monthly.parquet if present, else TEMPORARY fallback = D2's fja05680 spells)
 3. entity (CIK) -> Yahoo series mapping; reused tickers now owned by a different CIK are rejected
 4. prices: month-end adjusted closes, next-month TR, 12-1 momentum, 1y daily vol, forward 12/36m TR,
    forward 12m daily max drawdown, split-factor-corrected market cap
 5. fundamentals from d3_pit_monthly_lag1 (facts filed strictly before t) joined on (month_end, CIK)
 6. pre-registered metrics -> sector-neutral percentile ranks -> family scores -> composite
Output: v4/data/b1_panel.parquet (+meta), v4/outputs/b1_coverage_monthly.csv
"""
from __future__ import annotations

import json
import os
import re
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b1_common import (CACHE, DATA, FAMILIES, WINSOR_Q, FAMILY_METRICS, FAMILY_MIN_SHARE, COMPOSITE_MIN_FAMILIES,  # noqa: E402
                       LIVE_DATE, METRICS, MIN_SECTOR_N, OUT, month_end_days, write_meta, utcnow)
from d1_sic_sector_rules import sic_to_sector  # noqa: E402  (D1's documented SIC->sector rules, read-only)

PANEL_START = pd.Timestamp("2008-12-31")   # signals from here (calibration/backtest use >= 2009-12-31)
STALE_DAYS = 400                           # fundamentals older than this (month_end - last_period_end) -> missing
LOG = []


def log(msg):
    print(msg, flush=True)
    LOG.append(msg)


def norm_t(t) -> str:
    return str(t).strip().upper().replace(".", "-")


# ------------------------------------------------------------------------------------------------ membership
def _hist_ticker(hist, mkey):
    """ticker valid in month mkey ('YYYY-MM') from D1 ticker_history 'AA:2007-03..2016-10;ARNC:2016-11..2020-03'"""
    if not isinstance(hist, str):
        return None
    for part in hist.split(";"):
        try:
            tk, rng = part.rsplit(":", 1)
            a_, z_ = rng.split("..")
        except ValueError:
            continue
        if a_ <= mkey <= z_:
            return tk
    return None


def membership_d1(ME: pd.DatetimeIndex):
    """D1 entity-level PIT membership (bool matrix month x entity_id; secondary share-class lines dropped)"""
    p = DATA / "d1_membership_monthly.parquet"
    if not p.exists() or os.environ.get("B1_FORCE_FALLBACK") == "1":
        return None
    m = pd.read_parquet(p)
    m.index = pd.DatetimeIndex(m.index)
    cols = [c for c in m.columns if "." not in c]
    m = m.loc[m.index >= ME[0] - pd.Timedelta(days=40), cols]
    st = m.stack()
    st = st[st.astype(bool)]
    long = st.reset_index()
    long.columns = ["d1_me", "entity_id", "flag"]
    mk = pd.Series(ME, index=ME.to_period("M"))
    long["month_end"] = pd.DatetimeIndex(long.d1_me).to_period("M").map(mk)
    long = long.dropna(subset=["month_end"]).drop(columns=["d1_me", "flag"])
    iv = pd.read_csv(DATA / "d1_membership_intervals.csv", parse_dates=["start_date", "end_date"])
    iv = iv.sort_values("start_date")

    def last_nn(x):
        x = x.dropna()
        return x.iloc[-1] if len(x) else np.nan
    agg = iv.groupby("entity_id").agg(cik=("cik", last_nn), ycur=("ticker_current_yahoo", last_nn), name=("name", last_nn),
                                      hist=("ticker_history", lambda x: ";".join(x.dropna().astype(str))),
                                      tat=("ticker_at_time", last_nn), removal_reason=("removal_reason", last_nn),
                                      cik_confidence=("cik_confidence", last_nn)).reset_index()
    long = long.merge(agg, on="entity_id", how="left")
    cm = pd.read_csv(DATA / "d1_cik_map.csv", parse_dates=["cik_valid_from", "cik_valid_to"])
    multi = cm[cm.entity_id.duplicated(keep=False)]
    for e, g in multi.groupby("entity_id"):
        sel = (long.entity_id == e).to_numpy()
        for r in g.itertuples(index=False):
            w = sel & (long.month_end >= r.cik_valid_from).to_numpy()
            if pd.notna(r.cik_valid_to):
                w &= (long.month_end < r.cik_valid_to).to_numpy()
            long.loc[w, "cik"] = r.cik
    mkeys = pd.DatetimeIndex(long.month_end).strftime("%Y-%m")
    long["ticker"] = [norm_t(_hist_ticker(h, k) or t) for h, k, t in zip(long["hist"], mkeys, long["tat"])]
    long["ycur"] = [norm_t(y) if isinstance(y, str) else pd.NA for y in long.ycur]
    long["cik"] = pd.to_numeric(long.cik, errors="coerce").astype("Int64")
    out = long[["month_end", "entity_id", "cik", "ticker", "ycur", "name", "removal_reason", "cik_confidence"]].copy()
    out["mem_src"] = "D1_membership_monthly"
    return out


def membership_fallback(ME: pd.DatetimeIndex, tk2cik: dict):
    sp = pd.read_csv(DATA / "d2_universe_spells.csv", parse_dates=["start", "end_excl"])
    parts = []
    for r in sp.itertuples(index=False):
        sel = ME[(ME >= r.start) & ((ME < r.end_excl) if pd.notna(r.end_excl) else np.ones(len(ME), bool))]
        if len(sel):
            parts.append(pd.DataFrame({"month_end": sel, "ticker": norm_t(r.ticker)}))
    m = pd.concat(parts, ignore_index=True)
    m["cik"] = m.ticker.map(tk2cik).astype("Int64")
    m["mem_src"] = "D2_spells_fja05680_TEMPORARY"
    return m


# ------------------------------------------------------------------------------------------------ identity
def load_identity():
    cur = pd.read_csv(DATA / "d1_current_constituents.csv")
    cur["ticker_yahoo"] = cur.ticker_yahoo.map(norm_t)
    u = pd.read_csv(DATA / "d3_universe.csv")
    tm = pd.read_csv(DATA / "d3_ticker_cik_map.csv")
    sec = json.load(open(r"C:\Users\user\eqv4\cache\d1\company_tickers.json"))
    sec_owner = {}
    sec_tickers_of = {}
    for v in sec.values():
        t = norm_t(v["ticker"])
        sec_owner.setdefault(t, int(v["cik_str"]))
        sec_tickers_of.setdefault(int(v["cik_str"]), []).append(t)
    tk2cik = {}
    for r in tm.dropna(subset=["cik"]).itertuples(index=False):
        tk2cik[norm_t(r.ticker)] = int(r.cik)
    for r in u.itertuples(index=False):
        for t in re.split(r"[;|, ]+", str(r.tickers_all)):
            if t and t != "nan":
                tk2cik.setdefault(norm_t(t), int(r.cik))
    for r in cur.itertuples(index=False):
        tk2cik[r.ticker_yahoo] = int(r.cik)
    cov = pd.read_csv(DATA / "d2_coverage.csv")
    cov["ticker"] = cov.ticker.map(norm_t)
    cov = cov.set_index("ticker")
    d1map = DATA / "d1_cik_map.csv"
    return cur, u, tk2cik, sec_owner, sec_tickers_of, cov, (pd.read_csv(d1map) if d1map.exists() else None)


# ------------------------------------------------------------------------------------------------ main build
def build(mode: str = "pit"):
    """mode='pit' (primary) or 'today' (bias test: today's constituents at every date = the v3 approach)"""
    t0 = pd.Timestamp.now()
    adj = pd.read_parquet(DATA / "d2_adjclose.parquet")
    close = pd.read_parquet(DATA / "d2_close.parquet")
    adj.index = pd.DatetimeIndex(adj.index)
    close.index = pd.DatetimeIndex(close.index)
    days = adj.index
    ME_ALL = month_end_days(days)
    assert ME_ALL[-1] == LIVE_DATE, ME_ALL[-1]
    ME = ME_ALL[ME_ALL >= PANEL_START]
    log(f"calendar: {len(ME)} month-ends {ME[0].date()}..{ME[-1].date()}")

    cur, u3, tk2cik, sec_owner, sec_tickers_of, cov, d1map = load_identity()
    mem = membership_d1(ME) if mode == "pit" else None
    if mode == "today":
        cc = cur[["ticker_yahoo", "cik"]].rename(columns={"ticker_yahoo": "ticker"})
        mem = pd.DataFrame([(t, a, c) for t in ME for a, c in zip(cc.ticker, cc.cik)], columns=["month_end", "ticker", "cik"])
        mem["cik"] = mem.cik.astype("Int64")
        mem["mem_src"] = "TODAY_CONSTITUENTS_2026-09-25_at_all_dates (v3 approach; look-ahead by construction)"
        log("membership: TODAY's constituents at every date (bias test)")
    elif mem is None:
        mem = membership_fallback(ME, tk2cik)
        log("membership: TEMPORARY fallback = d2_universe_spells.csv (fja05680 + Wikipedia); CIK via D3/D1 maps")
    else:
        log("membership: D1 d1_membership_monthly.parquet")
        miss = mem.cik.isna()
        mem.loc[miss, "cik"] = mem.loc[miss, "ticker"].map(tk2cik).astype("Int64")
    mem = mem[mem.month_end.isin(ME)].copy()
    for c_ in ("entity_id", "ycur", "name", "removal_reason"):
        if c_ not in mem:
            mem[c_] = pd.NA

    # ---------------- candidate Yahoo series per (ticker, cik)
    eq_cols = set(cov.index[(cov.asset_class == "equity")]) & set(adj.columns)
    adj_me = adj.loc[ME_ALL]
    close_me = close.loc[ME_ALL]
    avail = adj_me.notna()

    # CIKs that are the same economic entity (holding-company reorganisations / new filer CIKs): D3 lineage pairs and
    # D1 multi-CIK entities. A symbol owned today by a related CIK is NOT ticker reuse (e.g. XOM -> ExxonMobil
    # Holdings Corp CIK 2115436, 2026-08).
    rel = {}

    def _link(a_, b_):
        rel.setdefault(int(a_), set()).add(int(b_))
        rel.setdefault(int(b_), set()).add(int(a_))
    lin = pd.read_csv(DATA / "d3_lineage.csv")
    for r_ in lin.itertuples(index=False):
        _link(r_.successor_cik, r_.predecessor_cik)
    if d1map is not None and "entity_id" in d1map:
        for e_, g_ in d1map.dropna(subset=["cik"]).groupby("entity_id"):
            cs = [int(c_) for c_ in g_.cik.unique()]
            for c1 in cs:
                for c2 in cs:
                    if c1 != c2:
                        _link(c1, c2)

    def related(c):
        seen, stack = {int(c)}, [int(c)]
        while stack:
            x_ = stack.pop()
            for y_ in rel.get(x_, ()):
                if y_ not in seen:
                    seen.add(y_)
                    stack.append(y_)
        return seen
    RELATED = {}

    def ok_series(s, cik):
        if s is None or s not in eq_cols:
            return False
        if bool(cov.at[s, "reuse_suspect"]) if s in cov.index else False:
            return False
        own = sec_owner.get(s)
        if own is not None and pd.notna(cik) and int(own) != int(cik):
            if int(cik) not in RELATED:
                RELATED[int(cik)] = related(int(cik))
            if int(own) not in RELATED[int(cik)]:
                return False      # ticker now belongs to a different company (reuse) -> not this entity's history
        return True

    pairs = mem[["ticker", "cik", "ycur"]].drop_duplicates()
    cand_map = {}
    rej = []
    for r in pairs.itertuples(index=False):
        c = []
        if isinstance(r.ycur, str) and ok_series(r.ycur, r.cik):
            c.append(r.ycur)          # D1: entity's current Yahoo symbol (renames, legal-successor histories)
        if r.ticker in c:
            pass
        elif ok_series(r.ticker, r.cik):
            c.append(r.ticker)
        elif r.ticker in eq_cols:
            rej.append((r.ticker, r.cik, sec_owner.get(r.ticker), bool(cov.at[r.ticker, "reuse_suspect"])))
        succ = cov.at[r.ticker, "rename_successor"] if r.ticker in cov.index else None
        if isinstance(succ, str) and ok_series(norm_t(succ), r.cik):
            c.append(norm_t(succ))
        if pd.notna(r.cik):
            for t in sec_tickers_of.get(int(r.cik), []):
                if ok_series(t, r.cik) and t not in c:
                    c.append(t)
        cand_map[(r.ticker, r.cik if pd.notna(r.cik) else -1, r.ycur if isinstance(r.ycur, str) else "")] = c
    log(f"identity: {len(pairs)} (ticker,cik) pairs; {len(rej)} member tickers rejected as reused/owned by other CIK")

    series = []
    for r in mem.itertuples(index=False):
        cands = cand_map[(r.ticker, r.cik if pd.notna(r.cik) else -1, r.ycur if isinstance(r.ycur, str) else "")]
        pick = None
        for s in cands:
            if avail.at[r.month_end, s]:
                pick = s
                break
        series.append(pick)
    mem["series"] = pd.array(series, dtype="string")
    mem["entity"] = np.where(mem.cik.notna(), "CIK" + mem.cik.astype("string").fillna(""), "TKR_" + mem.ticker)
    if mem.entity_id.notna().all():
        mem["entity"] = mem.entity_id.astype(str)

    # dual-class / duplicate entities: keep one row per (month, entity): prefer D3's primary ticker, then has-price
    d3p = pd.read_parquet(DATA / "d3_pit_monthly_lag1.parquet")
    d3p["cik"] = d3p.cik.astype("Int64")
    prim = d3p.drop_duplicates("cik", keep="last").set_index("cik").ticker.map(norm_t).to_dict()
    mem["_pref"] = [0 if (pd.notna(c) and pd.notna(s) and prim.get(int(c)) == s) else 1
                    for c, s in zip(mem.cik, mem.series)]
    mem["_hasp"] = mem.series.isna().astype(int)
    mem = mem.sort_values(["month_end", "entity", "_hasp", "_pref", "ticker"])
    n_before = len(mem)
    dup_info = mem[mem.duplicated(["month_end", "entity"], keep=False)].groupby("entity").ticker.agg(
        lambda x: ";".join(sorted(set(x))))
    mem = mem.drop_duplicates(["month_end", "entity"], keep="first").drop(columns=["_pref", "_hasp"])
    log(f"dedupe (dual class/shared CIK): {n_before}->{len(mem)} rows; groups: {dup_info.to_dict()}")

    # ---------------- price-derived quantities (month-end grid on ME_ALL, then looked up)
    nxt = adj_me.shift(-1) / adj_me - 1
    nxt.loc[nxt.index >= pd.Timestamp("2026-08-31")] = np.nan       # 2026-09 incomplete
    mom = adj_me.shift(1) / adj_me.shift(12) - 1
    f12 = adj_me.shift(-12) / adj_me - 1
    f36 = adj_me.shift(-36) / adj_me - 1
    f12.loc[f12.index > pd.Timestamp("2025-08-29")] = np.nan  # t+12 must be a complete month-end (<= 2026-08-31)
    f36.loc[f36.index > pd.Timestamp("2023-08-31")] = np.nan
    has_next_price = adj_me.shift(-1).notna()
    lr = np.log(adj / adj.shift(1))
    vol = lr.rolling(252, min_periods=200).std().loc[ME_ALL] * np.sqrt(252)
    # split factor after t: product of split ratios with date > t (per Yahoo series)
    spl = pd.read_parquet(DATA / "d2_splits.parquet")
    spl["ticker"] = spl.ticker.map(norm_t)
    F = pd.DataFrame(1.0, index=ME_ALL, columns=adj_me.columns)
    for r in spl.itertuples(index=False):
        if r.ticker in F.columns and r.split_ratio > 0:
            F.loc[F.index < pd.Timestamp(r.date), r.ticker] *= r.split_ratio
    close_actual = close_me * F

    def look(frame, name):
        idx_t = pd.Index(mem.month_end)
        vals = np.full(len(mem), np.nan)
        ok = mem.series.notna().to_numpy()
        ser = mem.series.to_numpy()
        rows = frame.index.get_indexer(idx_t)
        colpos = frame.columns.get_indexer(pd.Index(ser.astype(object)))
        arr = frame.to_numpy(dtype=float)
        sel = ok & (rows >= 0) & (colpos >= 0)
        vals[sel] = arr[rows[sel], colpos[sel]]
        mem[name] = vals

    look(adj_me, "adj")
    look(close_actual, "px_actual")
    look(F, "split_factor_after")
    look(nxt, "ret_next")
    look(has_next_price.astype(float), "has_next_price")
    look(mom, "mom_12_1")
    look(f12, "fwd12")
    look(f36, "fwd36")
    look(vol, "vol_1y")
    mem["in_universe"] = mem.adj.notna() & (mem.adj > 0)
    mem["delist_next"] = mem.in_universe & (mem.has_next_price == 0) & (mem.month_end < pd.Timestamp("2026-08-31"))
    # benchmark forward returns
    for b in ("SPY", "RSP", "^SP500TR"):
        s12 = f12[b] if b in f12 else None
        mem[f"fwd12_{b}"] = mem.month_end.map(s12) if s12 is not None else np.nan
    mem["fwd36_SPY"] = mem.month_end.map(f36["SPY"])
    mem["fwd12_excess_spy"] = mem.fwd12 - mem["fwd12_SPY"]
    mem["fwd36_excess_spy"] = mem.fwd36 - mem["fwd36_SPY"]

    # forward 12m daily max drawdown per stock-month
    pos = {d: i for i, d in enumerate(days)}
    me_pos = pd.Series([pos[d] for d in ME_ALL], index=ME_ALL)
    me_next12 = me_pos.shift(-12)
    A = adj.to_numpy(dtype=float)
    colidx = {c: i for i, c in enumerate(adj.columns)}
    fdd = np.full(len(mem), np.nan)
    for k, (t, s, iu) in enumerate(zip(mem.month_end, mem.series, mem.in_universe)):
        if not iu or pd.isna(s) or t > pd.Timestamp("2025-08-29"):
            continue
        e = me_next12.get(t)
        if pd.isna(e):
            continue
        w = A[int(me_pos[t]): int(e) + 1, colidx[s]]
        w = w[~np.isnan(w)]
        if len(w) < 20:
            continue
        fdd[k] = float((w / np.maximum.accumulate(w) - 1).min())
    mem["fwd12_maxdd"] = fdd

    # ---------------- fundamentals (D3 lag1: filed strictly before t)
    keep = ["month_end", "cik", "rev_ttm", "gp_ttm", "cogs_ttm", "opinc_ttm", "ni_ttm", "ocf_ttm", "capex_ttm",
            "ebit_ttm", "assets", "assets_1y_ago", "equity", "total_debt", "cash_sti", "shares_out", "shares_wdil", "shares_ref_ni_eps",
            "shares_out_date", "shares_1y_ago", "sue", "is_financial", "max_filed_used", "last_filed_date",
            "last_period_end", "staleness_days", "bs_date", "da_ttm"] + [f"eps_q{i}" for i in range(13)]
    f = d3p[keep].copy()
    f["month_end"] = pd.DatetimeIndex(f.month_end).as_unit("ns")
    mem["month_end"] = pd.DatetimeIndex(mem.month_end).as_unit("ns")
    mem = mem.merge(f, on=["month_end", "cik"], how="left")
    # lineage fallback: no D3 state for (t, entity CIK) -> use a related CIK's state at t (D3 successor rows carry the
    # predecessor's facts; e.g. XOM after the 2026-08 ExxonMobil Holdings reorganisation)
    mem["fund_cik"] = mem.cik
    miss = (mem.max_filed_used.isna() & mem.cik.notna()).to_numpy()
    if miss.any():
        fi = f.set_index(["cik", "month_end"])
        fi = fi[~fi.index.duplicated()]
        have = set(fi.index)
        n_fill = 0
        vcols = [c_ for c_ in fi.columns]
        for i_ in np.where(miss)[0]:
            c0 = int(mem.cik.iat[i_])
            t_ = mem.month_end.iat[i_]
            for c2 in sorted(related(c0) - {c0}):
                if (c2, t_) in have:
                    row = fi.loc[(c2, t_)]
                    for c_ in vcols:
                        mem.at[mem.index[i_], c_] = row[c_]
                    mem.at[mem.index[i_], "fund_cik"] = c2
                    n_fill += 1
                    break
        log(f"fundamentals: {n_fill} entity-months filled from a lineage-related CIK (D3 lineage / D1 multi-CIK)")
    # revenue TTM as known 12 month-ends earlier (PIT at t-12) for legacy growth pillar
    mpos = {d: i for i, d in enumerate(pd.DatetimeIndex(ME_ALL).as_unit("ns"))}
    lag12 = {d: pd.DatetimeIndex(ME_ALL).as_unit("ns")[i - 12] for d, i in mpos.items() if i >= 12}
    rv = f.set_index(["cik", "month_end"]).rev_ttm
    rv = rv[~rv.index.duplicated()]
    keys = pd.MultiIndex.from_arrays([mem.cik, mem.month_end.map(lag12)])
    mem["rev_ttm_lag12"] = rv.reindex(keys).to_numpy()
    meta = pd.read_csv(DATA / "d3_company_meta.csv")
    sic = meta.drop_duplicates("cik").set_index("cik").sic
    mem["sic"] = mem.cik.map(lambda c: sic.get(int(c)) if pd.notna(c) else np.nan)
    mem["sic"] = pd.to_numeric(mem.sic, errors="coerce")
    d1sec = DATA / "d1_sector_map.csv"
    sector_src = "sic_to_sector(D3 SIC) via d1_sic_sector_rules.py"
    if d1sec.exists() and mem.entity_id.notna().all():
        sm = pd.read_csv(d1sec).drop_duplicates("entity_id").set_index("entity_id")
        mem["sector"] = mem.entity_id.map(sm.sic_sector)
        sic_d1 = pd.to_numeric(mem.entity_id.map(sm.sic), errors="coerce")
        mem["sic"] = sic_d1.fillna(mem.sic)
        sector_src = "D1 d1_sector_map.csv sic_sector (by entity_id); SIC from D1 (fallback D3)"
    elif d1sec.exists():
        sm = pd.read_csv(d1sec)
        sc = {c.lower(): c for c in sm.columns}
        if "cik" in sc and any(k in sc for k in ("sector", "sector_sic", "sic_sector")):
            scol = sc.get("sector_sic") or sc.get("sic_sector") or sc.get("sector")
            smap = sm.dropna(subset=[sc["cik"]]).drop_duplicates(sc["cik"]).set_index(sc["cik"])[scol]
            mem["sector"] = mem.cik.map(lambda c: smap.get(int(c)) if pd.notna(c) else None)
            sector_src = f"D1 d1_sector_map.csv column {scol}"
    if "sector" not in mem:
        mem["sector"] = [sic_to_sector(s)[0] if pd.notna(s) else None for s in mem.sic]
    gics = cur.drop_duplicates("cik").set_index("cik").gics_sector
    fill = mem.sector.isna() & mem.cik.notna()
    mem.loc[fill, "sector"] = mem.loc[fill, "cik"].map(lambda c: gics.get(int(c)))
    mem["sector"] = mem.sector.fillna("Unknown")
    log(f"sector source: {sector_src}; GICS fallback rows {int(fill.sum())}")
    mem["sic4"] = mem.sic

    # ---------------- DA2 data-audit fixes (v4/audit/da2_data_audit.md), applied before any metric
    EPSC = [f"eps_q{i}" for i in range(13)]
    brk_c = (mem.cik == 1067983).fillna(False).to_numpy()
    mem.loc[brk_c, EPSC] = mem.loc[brk_c, EPSC] / 1500.0        # (1) BRK Class-A-equivalent EPS -> B-share basis
    E = mem[EPSC].to_numpy(dtype=float, copy=True)
    absE = np.abs(E)
    with np.errstate(all="ignore"):
        med = np.nanmedian(absE, axis=1)
    bad_e = np.isfinite(E) & ((absE > 500) | ((med[:, None] > 0) & (absE > 50 * med[:, None])))
    E[bad_e] = np.nan                                            # (2) filer-side EPS scale errors -> missing
    mem[EPSC] = E
    d_ = np.stack([E[:, i] - E[:, i + 4] for i in range(9)], axis=1)
    prior = d_[:, 1:9]
    n_ok = np.isfinite(prior).sum(axis=1)
    with np.errstate(all="ignore"):
        sd = np.nanstd(prior, axis=1, ddof=1)
        sue_new = d_[:, 0] / sd
    sue_new[(n_ok < 6) | ~np.isfinite(d_[:, 0]) | ~(sd > 0)] = np.nan
    mem["sue_d3"] = mem.sue
    mem["sue"] = sue_new
    apa = ((mem.cik == 1841666) & (mem.month_end >= pd.Timestamp("2021-03-01"))).fillna(False).to_numpy()
    mem.loc[apa, ["rev_ttm", "gp_ttm", "cogs_ttm", "rev_ttm_lag12"]] = np.nan   # (3) APA revenue concept incomplete
    # (4) ERIE Class-B cover count and (5) placeholder share counts are caught by the market-cap sanity rules below
    sh_raw = mem.shares_out.to_numpy(dtype=float)
    trail_raw = mem.shares_out.groupby(mem.entity).transform(lambda x: x.shift(1).rolling(12, min_periods=3).median())
    ph = (mem.shares_out < 0.01 * trail_raw).fillna(False).to_numpy()
    mem.loc[ph, "shares_out"] = np.nan                          # (5) placeholder glitch (<1% of trailing median)
    erie = (mem.cik == 922621).fillna(False).to_numpy() & (sh_raw < 1e6)
    mem.loc[erie, "shares_out"] = np.nan                        # (4) ERIE Class-B count
    DA2_LOG = {"brk_rows_eps_div1500": int(brk_c.sum()), "eps_cells_set_missing": int(bad_e.sum()),
               "eps_rows_affected": int(bad_e.any(axis=1).sum()),
               "eps_cells_by_ticker": pd.Series(bad_e.sum(axis=1), index=mem.series.fillna("?")).groupby(level=0).sum()
               .loc[lambda x: x > 0].sort_values(ascending=False).head(15).to_dict(),
               "sue_changed_rows": int((~np.isclose(mem.sue.fillna(-999), mem.sue_d3.fillna(-999))).sum()),
               "apa_rows_revenue_missing": int(apa.sum()), "shares_placeholder_rows_missing": int(ph.sum()),
               "erie_classB_rows_missing": int(erie.sum())}
    log(f"DA2 fixes: {DA2_LOG}")

    # staleness & PIT assertion
    stale = mem.staleness_days > STALE_DAYS
    fcols = [c for c in keep if c not in ("month_end", "cik", "is_financial", "max_filed_used", "last_filed_date",
                                          "last_period_end", "staleness_days", "bs_date", "shares_out_date")]
    mem.loc[stale, fcols] = np.nan
    log(f"stale fundamentals (> {STALE_DAYS}d since last period end) set missing: {int(stale.sum())} rows")
    bad = mem.max_filed_used.notna() & (pd.DatetimeIndex(mem.max_filed_used) >= pd.DatetimeIndex(mem.month_end))
    assert int(bad.sum()) == 0, f"look-ahead: {int(bad.sum())} rows with filed >= month_end"

    # ---------------- market cap with split-basis check
    mc_a = mem.px_actual * mem.shares_out
    # ambiguous when a split of the chosen series occurred in (shares_out_date, t]
    spl_g = {k: v.sort_values("date") for k, v in spl.groupby("ticker")}
    mult_b = np.ones(len(mem))
    amb = np.zeros(len(mem), bool)
    for k, (s, sd, t) in enumerate(zip(mem.series, mem.shares_out_date, mem.month_end)):
        if pd.isna(s) or pd.isna(sd) or s not in spl_g:
            continue
        g = spl_g[s]
        hit = g[(g.date > pd.Timestamp(sd)) & (g.date <= t)]
        if len(hit):
            amb[k] = True
            mult_b[k] = float(hit.split_ratio.prod())
    mem["_sh_today_a"] = mem.shares_out * mem.split_factor_after
    mem["_sh_today_b"] = mem.shares_out * mult_b * mem.split_factor_after
    ref = mem["_sh_today_a"].where(~amb)
    mem["_ref"] = ref.groupby(mem.entity).transform(lambda x: x.rolling(13, center=True, min_periods=1).median())
    mem["_ref"] = mem.groupby("entity")._ref.transform(lambda x: x.ffill().bfill())
    use_b = amb & ((np.log(mem._sh_today_b / mem._ref)).abs() < (np.log(mem._sh_today_a / mem._ref)).abs())
    mult = np.where(use_b, mult_b, 1.0)
    sh = mem.shares_out * mult
    wd = mem.shares_wdil * mult
    # BRK: XBRL share counts are Class-A equivalents; the Yahoo series is BRK-B (1 A = 1,500 B since 2010-01-21)
    brk = (mem.series == "BRK-B").fillna(False) & (sh < 5e6)
    sh = sh.where(~brk, sh * 1500)
    wd = wd.where(~brk, wd * 1500)
    # cross-check vs weighted diluted shares from the same PIT filing set; implausible cover-page counts
    # (class-level counts, unit errors) are replaced by weighted diluted shares
    ne = mem.shares_ref_ni_eps * mult
    ne = ne.where(~brk, ne * 1500)

    def agree(a, b):
        r_ = a / b
        return r_.notna() & (r_ >= 0.5) & (r_ <= 2.0)
    # majority vote: replace the cover-page count only if it disagrees with BOTH weighted-diluted shares and
    # NI/EPS-implied shares while those two agree with each other (then use weighted diluted shares)
    bad_w = sh.notna() & ~agree(sh, wd) & ~agree(sh, ne) & agree(wd, ne)
    sh = sh.where(~bad_w, wd)
    wd = wd.where(agree(wd, ne) | ne.isna())
    # no weighted-diluted cross-check possible: trailing (PIT) 12m median check on today-basis shares
    sh_today = sh * mem.split_factor_after
    trail = sh_today.groupby(mem.entity).transform(lambda x: x.shift(1).rolling(12, min_periods=3).median())
    rt = sh_today / trail
    bad_t = rt.notna() & ((rt < 0.4) | (rt > 2.5))
    sh = sh.where(~bad_t)
    mc_ = mem.px_actual * sh
    bad_sz = mc_.notna() & ((mc_ < 2.5e8) | (mc_ > 8e12))   # implausible for an S&P 500 member (unit/class errors)
    sh = sh.where(~bad_sz)
    mem["shares_used"] = sh
    mem["mktcap"] = mem.px_actual * sh
    mem["mktcap_split_fix"] = use_b
    mem["mktcap_flag"] = np.select([brk, bad_w, bad_t, bad_sz], ["brk_class_a_to_b", "cover_shares_replaced_by_wdil",
                                                                  "shares_jump_vs_trailing12m_set_missing",
                                                                  "implausible_size_set_missing"], "")
    log(f"market cap: BRK rows {int(brk.sum())}; cover shares replaced by wdil {int(bad_w.sum())}; "
        f"set missing (trailing check) {int(bad_t.sum())}; implausible size {int(bad_sz.sum())}")
    log(f"market cap: {int(amb.sum())} rows with split between share-count date and t; {int(use_b.sum())} rescaled")
    mem = mem.drop(columns=["_sh_today_a", "_sh_today_b", "_ref"])

    # ---------------- metrics
    fin = mem.is_financial.fillna(False).astype(bool) | mem.sic.between(6000, 6411)
    mem["financial"] = fin
    A_ = mem.assets.where(mem.assets > 0)
    gp = mem.gp_ttm.fillna(mem.rev_ttm - mem.cogs_ttm)
    mem["gp_a"] = (gp / A_).where(~fin)
    mem["roe"] = (mem.ni_ttm / mem.equity).where(mem.equity > 0)
    mem["ocf_a"] = mem.ocf_ttm / A_
    mem["accruals"] = ((mem.ni_ttm - mem.ocf_ttm) / A_).where(~fin)
    mem["leverage"] = (mem.total_debt / A_).where(~fin)
    mem["asset_growth"] = mem.assets / mem.assets_1y_ago.where(mem.assets_1y_ago > 0) - 1
    mem["net_issuance"] = mem.shares_out / mem.shares_1y_ago.where(mem.shares_1y_ago > 0) - 1
    mc = mem.mktcap.where(mem.mktcap > 0)
    mem["ep"] = mem.ni_ttm / mc
    mem["fcfp"] = (mem.ocf_ttm - mem.capex_ttm.abs()) / mc
    ev = mc + mem.total_debt - mem.cash_sti
    mem["ebit_ev"] = (mem.ebit_ttm / ev.where(ev > 0)).where(~fin)
    mem["bp"] = mem.equity / mc
    # mom_12_1 and sue already present

    U = mem.in_universe
    for m, fam, hib, _ in METRICS:
        x = mem[m].where(U)
        x = x.replace([np.inf, -np.inf], np.nan)
        if fam in ("Q", "V"):      # winsorise ratio metrics per month (early-XBRL scale errors; D3 report)
            gq = x.groupby(mem.month_end)
            x = x.clip(gq.transform(lambda s_: s_.quantile(WINSOR_Q[0])), gq.transform(lambda s_: s_.quantile(WINSOR_Q[1])))
        if not hib:
            x = -x
        valid = x.notna()
        cnt = valid.groupby([mem.month_end, mem.sector]).transform("sum")
        grp = mem.sector.where(cnt >= MIN_SECTOR_N, "POOL")
        r = x.groupby([mem.month_end, grp]).rank(method="average")
        n = valid.groupby([mem.month_end, grp]).transform("sum")
        mem[f"pct_{m}"] = ((r - 0.5) / n).where(valid)

    def xs_pct(s):
        r = s.groupby(mem.month_end).rank(method="average")
        n = s.notna().groupby(mem.month_end).transform("sum")
        return ((r - 0.5) / n).where(s.notna())

    for fam in FAMILIES:
        cols = [f"pct_{m}" for m in FAMILY_METRICS[fam]]
        need = int(np.ceil(FAMILY_MIN_SHARE * len(cols) - 1e-9))
        cnt = mem[cols].notna().sum(axis=1)
        raw = mem[cols].mean(axis=1).where(cnt >= max(need, 1))
        mem[f"fam_{fam}_raw"] = raw
        mem[f"fam_{fam}"] = xs_pct(raw)
        mem[f"n_{fam}"] = cnt
    fcols_ = [f"fam_{f}" for f in FAMILIES]
    nf = mem[fcols_].notna().sum(axis=1)
    mem["n_families"] = nf
    mem["composite_raw"] = mem[fcols_].mean(axis=1).where(nf >= COMPOSITE_MIN_FAMILIES)
    mem["composite"] = xs_pct(mem.composite_raw)
    mem["decile"] = np.ceil(mem.composite * 10).clip(1, 10)
    mem["quintile"] = np.ceil(mem.composite * 5).clip(1, 5)
    # QVM-only composite (variant) - requires >=2 of 3
    q3 = ["fam_Q", "fam_V", "fam_M"]
    mem["composite_qvm"] = xs_pct(mem[q3].mean(axis=1).where(mem[q3].notna().sum(axis=1) >= 2))
    # vol terciles (cross-sectional, universe)
    vr = mem.vol_1y.where(U).groupby(mem.month_end).rank(pct=True)
    mem["vol_tercile"] = np.ceil(vr * 3).clip(1, 3)

    mem = mem.sort_values(["month_end", "entity"]).reset_index(drop=True)
    sfx = "" if mode == "pit" else "_today"
    out = DATA / f"b1_panel{sfx}.parquet"
    mem.to_parquet(out, index=False)

    # coverage table
    cov_m = mem.groupby("month_end").agg(pit_members=("entity", "size"), with_price=("in_universe", "sum"),
                                         with_cik=("cik", lambda x: x.notna().sum()),
                                         with_composite=("composite", lambda x: x.notna().sum()),
                                         delist_next=("delist_next", "sum"))
    cov_m["pct_with_price"] = cov_m.with_price / cov_m.pit_members
    cov_m["pct_with_composite"] = cov_m.with_composite / cov_m.pit_members
    cov_m.to_csv(OUT / f"b1_coverage_monthly{sfx}.csv")
    write_meta(out, {"rows": int(len(mem)), "columns": list(mem.columns), "built_utc": utcnow(),
                     "membership_source": mem.mem_src.iloc[0], "sector_source": sector_src,
                     "sources": ["v4/data/d2_adjclose.parquet", "v4/data/d2_close.parquet", "v4/data/d2_splits.parquet",
                                 "v4/data/d3_pit_monthly_lag1.parquet", "v4/data/d3_company_meta.csv",
                                 "v4/data/d1_current_constituents.csv", "v4/data/d2_universe_spells.csv or D1 membership"],
                     "pit_rules": ["fundamentals: D3 lag1 (filed < month_end)", "prices <= t", "membership at t only",
                                   "Q/V ratio metrics winsorised 1st/99th pct per month before ranking (stored values raw)",
                                   f"fundamentals with staleness_days > {STALE_DAYS} set missing"],
                     "definitions": {"ret_next": "AdjClose(t+1 month-end)/AdjClose(t)-1 on the entity's Yahoo series",
                                     "mom_12_1": "AdjClose(t-1)/AdjClose(t-12)-1",
                                     "vol_1y": "std of 252 daily log TR returns ending t (min 200) * sqrt(252)",
                                     "mktcap": "Close_t x split factor after t x D3 shares_out (split-basis checked)",
                                     "pct_*": "sector-neutral mid-rank percentile (rank-0.5)/n within SIC-derived sector; sectors with <5 valid names pooled",
                                     "fam_*": "cross-sectional re-rank of mean of available metric pcts (>=50% present)",
                                     "composite": "re-rank of mean of available family pcts (>=3 of 4)"},
                     "da2_fixes": DA2_LOG, "log": LOG})
    log(f"panel written: {len(mem)} rows in {(pd.Timestamp.now() - t0).total_seconds():.0f}s")
    return mem


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "pit")
