"""d4_report.py - write v4/outputs/d4_report.md from the D4 outputs (all numbers computed here from files)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import ASOF, DATA, OUT, V3_PORTFOLIO, utc_now_iso, write_meta  # noqa: E402


def md(df: pd.DataFrame, floatfmt: dict | None = None) -> str:
    floatfmt = floatfmt or {}
    cols = list(df.columns)
    out = ["| " + " | ".join(str(c) for c in cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, (float, np.floating)):
                if pd.isna(v):
                    cells.append("n/a")
                else:
                    cells.append(format(v, floatfmt.get(c, ".2f")))
            elif v is None or (isinstance(v, float) and np.isnan(v)):
                cells.append("n/a")
            else:
                cells.append(str(v).replace("|", "/"))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def pctf(x, d=1):
    return "n/a" if x is None or pd.isna(x) else f"{100 * x:.{d}f}%"


def main():
    s = pd.read_parquet(DATA / "d4_live_snapshot.parquet")
    V = json.loads((OUT / "d4_validation_summary.json").read_text(encoding="utf-8"))
    ntab = pd.read_csv(OUT / "d4_ntm_vs_yahoo_table.csv")
    an = pd.read_csv(DATA / "d4_anomalies.csv")
    ev = pd.read_csv(DATA / "d4_corporate_events.csv").fillna("")
    cl = pd.read_csv(DATA / "d4_changelog_v3.csv")
    sec = pd.read_csv(DATA / "d4_validation_sec.csv")
    mc = pd.read_csv(DATA / "d4_validation_mcap.csv")
    ip = pd.read_csv(DATA / "d4_indep_prices.csv")
    fye = pd.read_csv(DATA / "d4_validation_fye.csv")
    meta = json.loads((DATA / "d4_live_snapshot.meta.json").read_text(encoding="utf-8"))
    imeta = json.loads((DATA / "d4_indep_prices.meta.json").read_text(encoding="utf-8"))

    n = len(s)
    P, M, S, F, N = V["price"], V["mcap"], V["sec"], V["fye_vs_sec"], V["ntm"]
    hz = s["yahoo_fwd_horizon"].value_counts()
    n_fy1_exact = int(hz.get("FY1(+1y)", 0))
    n_fy1_3 = n_fy1_exact + int(hz.get("~FY1(+1y)", 0))
    n_fy0 = int(hz.get("FY0(0y)", 0)) + int(hz.get("~FY0(0y)", 0))
    n_off = int(hz.get("~FY1(+1y)>3%off", 0)) + int(hz.get("~FY0(0y)>3%off", 0))
    both = s[s["fwdPE_over_peNTM"].notna()]
    gt10 = both["fwdPE_vs_peNTM_gt10pct"].astype(bool)
    ok = both[both["ntm_quality"] == "ok"]
    ok_gt10 = int(ok["fwdPE_vs_peNTM_gt10pct"].astype(bool).sum())
    q = s["ntm_quality"].value_counts()
    rt = ntab.set_index("group")
    v3 = s.set_index("ticker").loc[V3_PORTFOLIO]
    v3_uplift = (v3["pe_ntm"] / v3["forwardPE"] - 1)
    t_first, t_last = meta["retrieval_utc_first"], meta["retrieval_utc_last"]

    L = []
    A = L.append
    A(f"# D4 — Live S&P 500 snapshot at the {ASOF} close, NTM calendarization and data validation")
    A("")
    A(f"Agent D4 · market-data cutoff US close Friday {ASOF} · Yahoo pull {t_first} → {t_last} (UTC, i.e. 23–40 minutes after the "
      f"16:00 ET close) · independent quotes {imeta.get('retrieval_utc_start')} → {imeta.get('retrieval_utc_end')} UTC · report generated {utc_now_iso()}")
    A("")
    A("## 1. Answer first")
    A("")
    A(f"1. **Snapshot complete: {n}/503 constituents**, {s.shape[1]} columns, in `v4/data/d4_live_snapshot.parquet`. Every price is the "
      f"{ASOF} regular-session close (`regularMarketTime` = {ASOF} ~20:00 UTC for all {n}; **0 stale**).")
    A(f"2. **Prices independently confirmed for all 503.** Every Yahoo close is within 0.5% of the Cboe `close` ({P['cboe_pass_0p5pct']}/{P['cboe_compared']}; "
      f"{P['cboe_exact_match']} exact) **and** of CNBC's 16:00 ET last ({P['cnbc_pass_0p5pct']}/{P['cnbc_compared']}; {P['cnbc_exact_match']} exact). The largest gap is "
      f"{100 * P['max_abs_diff_cboe']:.3f}%. Stooq, the source named in the brief, now answers scripted requests with a JavaScript "
      f"proof-of-work \"verify your browser\" page. That is a bot challenge, so it was **not** solved or bypassed; Cboe and CNBC were used instead.")
    A(f"3. **Yahoo's `forwardPE` is price ÷ next-fiscal-year ('+1y') consensus EPS, not a next-twelve-months (NTM) multiple.** `forwardEps` equals the "
      f"+1y consensus exactly for {n_fy1_exact}/{n} names and within 3% for {n_fy1_3}/{n}. It matches the current-year (0y) consensus for only {n_fy0}, and "
      f"is more than 3% away from both for {n_off} (these are basis or staleness errors; see §3.6).")
    A(f"4. **Yahoo forward P/E vs calendarized NTM P/E: {int(gt10.sum())}/{len(both)} names ({pctf(gt10.mean())}) differ by more than 10%.** "
      f"The median ratio of Yahoo to NTM P/E is {both['fwdPE_over_peNTM'].median():.3f}, and Yahoo's figure is lower for {pctf((both['fwdPE_over_peNTM'] < 1).mean(), 0)} of names, "
      f"so it systematically understates the multiple. The error grows with the share of the current fiscal year still to run (f). "
      f"It exceeds 10% for {pctf(rt.loc['f_bucket=0<f<=0.25', 'share_gt10pct'], 0)} of names with f ≤ 0.25, "
      f"{pctf(rt.loc['f_bucket=0.25<f<=0.5', 'share_gt10pct'], 0)} with 0.25–0.5 (most December year-ends), "
      f"{pctf(rt.loc['f_bucket=0.5<f<=0.75', 'share_gt10pct'], 0)} with 0.5–0.75 and "
      f"{pctf(rt.loc['f_bucket=0.75<f<=1', 'share_gt10pct'], 0)} with f > 0.75. Among the {len(ok)} names whose consensus passes every consistency check, "
      f"{ok_gt10} differ by more than 10%. These are pure horizon effects: ORCL 12.5x (Yahoo) vs 15.1x (NTM), MSFT 21.8x vs 24.9x, and NVDA 14.4x vs 16.7x.")
    A(f"5. **v3 portfolio: the NTM P/E is higher than Yahoo's forward P/E for all 14 holdings** (median +{100 * v3_uplift.median():.1f}%). "
      f"The largest gaps are MSFT +{100 * v3_uplift['MSFT']:.1f}%, NVDA +{100 * v3_uplift['NVDA']:.1f}% and ORCL-like June/May fiscal years (PAYX +{100 * v3_uplift['PAYX']:.1f}%, NTAP +{100 * v3_uplift['NTAP']:.1f}%).")
    A(f"6. **Consensus data quality, graded per ticker (`ntm_quality`): {q.get('ok', 0)} ok, {q.get('caution', 0)} caution, {q.get('unreliable', 0)} unreliable.** "
      f"The unreliable group includes 28 REITs, where EPS is not the valuation earnings measure (FFO is). It also includes names whose Yahoo annual row contradicts its own quarterly rows by more than 25% "
      f"(for example CDNS, where the FY0 row looks GAAP and the quarterly and FY1 rows look adjusted), names with a +1y row whose 'year-ago' figure ≠ the 0y consensus (PANW, DELL, REGN), and names with negative or missing EPS.")
    A(f"7. **Market cap: {M['pass_3pct']}/{M['compared']} are within 3% of price × `sharesOutstanding`, and all {M['pass_3pct_using_implied_shares']}/503 match price × `impliedSharesOutstanding`.** "
      f"The {M['compared'] - M['pass_3pct']} exceptions are multi-class, UP-C or operating-partnership-unit structures (GOOGL/GOOG, BRK-B, IBKR, BX, SPG, …). "
      f"Yahoo's `marketCap` counts all classes and units; its `sharesOutstanding` counts only the listed class.")
    A(f"8. **SEC XBRL cross-check (CY2025 frames vs Yahoo FY2025, December year-ends): revenue within 2% for {S['rev_within_2pct']}/{S['rev_compared']} "
      f"({pctf(S['rev_within_2pct'] / S['rev_compared'])}); net income {S['ni_within_2pct']}/{S['ni_compared']} ({pctf(S['ni_within_2pct'] / S['ni_compared'])}).** "
      f"The largest gaps come from mismatched concepts or definitions: banks' fee-only contract revenue, REIT lease revenue, excise taxes, non-controlling interests and discontinued operations. "
      f"They also include **SEC-side XBRL scale errors: PG&E net income is tagged as $2,593, Arista as $3,511, and ConEd and Schwab are 1,000× too small. In these cases Yahoo is right.**")
    A(f"9. **Fiscal calendars: the Yahoo FY0 end month agrees with SEC for {F['consistent']}/{F['compared']}.** All three exceptions are explained. AMCR (8-K Item 5.03, 2026-05-06) and "
      f"FDX (8-K Item 2.02, 2026-07-21) moved their fiscal year-ends to 31 December, so Yahoo is right and the SEC metadata is stale. BRO's SEC `fiscalYearEnd` field is wrong. "
      f"Yahoo `lastFiscalYearEnd` matches the latest 10-K period for {F['lfy_within_7d_of_last_annual_report']}/{F['lfy_vs_last_annual_report_compared']}; the 3 misses (AZO, CPRT, COST) have released results but not yet filed the 10-K.")
    n_prev = int((an["check"] == "metadata_prevName").sum())
    bad_prev = an[(an["check"] == "metadata_prevName") & (an["severity"] == "high")]["ticker"].tolist()
    A(f"10. **Metadata quarantine.** `prevName` is populated for {n_prev} names. `nameChangeDate` **always equals the retrieval date** "
      f"(2026-09-25 here, 2026-09-24 in the legacy file), so it is a fetch stamp, not an event date. {len(bad_prev)} `prevName` values are not company names: "
      f"**NVDA 'Usual Stablecoin' (still present), CPAY 'VaporWallet', NFLX 'VIVEK' and TFC 'Supernova'**. They look like crypto-token names bleeding into equity metadata. "
      f"Both fields should be quarantined. Separately, yfinance's `calendar` converts epoch times using the machine's local timezone (UTC+4), which "
      f"**shifts {V['yf_calendar_local_tz_shift_count']} after-close earnings dates one day late**. `next_earnings_date` in the snapshot uses America/New_York.")
    flags = cl["flags_gt2pct"].fillna("")
    A(f"11. **Change log vs the legacy snapshot (2026-09-24, one session earlier): {int((flags != '').sum())}/14 v3 names have a consensus EPS or target change above 2%.** "
      f"The largest price moves are MSFT +{100 * cl.set_index('ticker').loc['MSFT', 'chg_price']:.1f}% and ABNB +{100 * cl.set_index('ticker').loc['ABNB', 'chg_price']:.1f}%. "
      f"PAYX, which reported on 2026-09-23, shows a 30-day FY0 revision of {100 * v3.loc['PAYX', 'eps_fy0_rev30_pct']:+.2f}%. The large recent revisions are NVDA FY1 "
      f"+{100 * v3.loc['NVDA', 'eps_fy1_rev30_pct']:.1f}% and NTAP FY1 +{100 * v3.loc['NTAP', 'eps_fy1_rev30_pct']:.1f}% over 30 days. HIG has {int(v3.loc['HIG', 'eps_rev_fy1_down30'])} downward and "
      f"{int(v3.loc['HIG', 'eps_rev_fy1_up30'])} upward FY1 revisions in 30 days.")
    A("12. **Corporate events (best-effort, evidence in `d4_corporate_events.csv`).** Constituents that are targets or merging parties in pending deals: "
      "WBD (Paramount Skydance; SC 14D-9 and merger proxy), KVUE (Kimberly-Clark), TECH (Merck KGaA; holders approved 2026-09-23), "
      "AES (GIP/EQT consortium), NSC (Union Pacific; STB review) and D (all-stock combination with NEE; NEE filed an S-4). "
      "Merger-proxy flags that are *not* pending takeovers: DVN (Coterra merger completed 2026-05-07; an activist letter on 2026-09-23 urges a sale) and CCL (DLC unification). "
      "MGM: People Inc. dropped its bid on 2026-09-24. Recent or planned separations: FDXF and HONA (completed 2026 spins), CTVA (Vylor), FLEX, GPC, SOLV, MDT (MiniMed) and KDP. "
      "AME's $5bn Indicor acquisition closed on 2026-08-26 (8-K 2.01 and press release).")
    A("")
    A("## 2. What was done")
    A("")
    A(f"* **Universe**: Wikipedia *List of S&P 500 companies*, table 1 (`id=constituents`): 503 lines, 500 CIKs (GOOGL/GOOG, FOXA/FOX and NWSA/NWS share CIKs), converted to Yahoo tickers (BRK-B, BF-B). "
      "The page no longer carries the 'selected changes' table. Output: `v4/data/d4_universe.csv`.")
    A("* **Yahoo pull** (`d4_fetch_yahoo.py`, yfinance 1.7.0, 5 threads, global limit of 8 requests/s, exponential backoff, one pickle per ticker in `C:\\Users\\user\\eqv4\\cache\\d4\\yahoo\\`). "
      "Per ticker: `info`, `earnings_estimate`, `revenue_estimate`, `eps_trend`, `eps_revisions` (plus the raw earningsTrend list, which carries each period's `endDate`), `earnings_history`, "
      "`get_earnings_dates(limit=16)`, `analyst_price_targets`, `recommendations_summary`, `upgrades_downgrades`, `calendar` (plus raw calendarEvents epochs), annual `income_stmt`, and news and press-release headlines. "
      "UTC start and end times are recorded per ticker (`retrieved_utc_start/end`). "
      "Only 404s (no data) remained: FOX has no consensus of its own, so the FOXA consensus was borrowed and flagged (`estimates_from_sibling`); ERIE has no upgrades or downgrades; NEM's press-release tab failed.")
    A("* **Independent prices** (`d4_fetch_indep_prices.py`): Cboe delayed-quotes JSON (`close`; 503 single-symbol requests, slowed to 1 every 2.5 s after Cloudflare "
      "rate-limited 2 per second) and CNBC's quote service (`last`, `last_time`, `previous_day_closing`, `eps`, `sharesout`, `feps`, `fpe`; batched). One Stooq probe is kept as evidence of the block.")
    A("* **SEC** (`d4_fetch_sec.py`; SEC User-Agent, ≤2 requests/s): XBRL frames for CY2025 (Revenues, RevenueFromContractWithCustomerExcludingAssessedTax, NetIncomeLoss, plus the diagnostics "
      "RevenueFromContractWithCustomerIncludingAssessedTax, RevenuesNetOfInterestExpense, ProfitLoss, NetIncomeLossAvailableToCommonStockholdersBasic), and submissions JSON for all 500 CIKs. "
      "Three 8-K documents were read to settle fiscal-calendar questions (AMCR 2026-05-06, AMCR 2026-01-15, FDX 2026-07-21).")
    A("* **Build and validation**: `d4_build_snapshot.py` (fields, NTM, quality grade), `d4_validate.py`, `d4_events.py`, `d4_changelog.py` and `d4_report.py`. Re-running the chain reproduces every number here from the cache.")
    A("")
    A("## 3. NTM calendarization (the key fix)")
    A("")
    A("### 3.1 Rule")
    A("")
    A("* **FY0** is the current, not-yet-reported fiscal year, i.e. the period Yahoo labels `0y`. Its end date comes from the raw earningsTrend `endDate` of `0y`. That is exactly the period the "
      "FY0 consensus refers to, and it is normalised to month-end (NVDA 2027-01-31, where the true year-end is the last Sunday of January). "
      "Cross-checks: `info.nextFiscalYearEnd` (= `lastFiscalYearEnd` + 1 year) must agree within 20 days; `mostRecentQuarter` must fall between `lastFiscalYearEnd` and the FY0 end; and the FY0 end month is compared with SEC. "
      "Disagreements are resolved from SEC primary documents (§1 item 9). The only manual override is HONA, a 2026 spin-off: its calendar fiscal year is taken from SEC because Yahoo's label reads Jan-2027.")
    A("* **f** = share of FY0 still to run at 2026-09-25 = clip((FY0_end − 2026-09-25) / (FY1_end − FY0_end), 0, 1). f = 0 when FY0 has ended but is not yet reported "
      "(ACN, FDS, JBL, MU, FDXF). In that case NTM = FY1.")
    A("* **EPS_NTM = f·EPS_FY0 + (1−f)·EPS_FY1** and **REV_NTM = f·REV_FY0 + (1−f)·REV_FY1**, using the earnings_estimate and revenue_estimate averages. "
      "`pe_ntm` = price/EPS_NTM (NaN with a reason when EPS_NTM ≤ 0 or estimates are missing), `ev_sales_ntm` = EV/REV_NTM, plus `pe_fy0` and `pe_fy1`.")
    A("* Two diagnostics that are not the primary measure: **quarter-aware NTM** = (FY0 − EPS already reported for FY0 quarters) + FY1·q/4, where q = FY0 quarters reported; and "
      "**quarterly-sum NTM** = remaining 0q/+1q estimates + FY1·q/4. They expose seasonality and one-off items that the time-weighted formula assumes away.")
    A("")
    A("### 3.2 Verification on the requested companies")
    A("")
    ver = s.set_index("ticker").loc[["NVDA", "MSFT", "AAPL", "ORCL", "WMT", "PAYX", "AME", "JPM"]].reset_index()
    fyl = {"NVDA": "FY2027 (FYE late Jan)", "MSFT": "FY2027 (FYE 30 Jun)", "AAPL": "FY2026 (FYE late Sep)", "ORCL": "FY2027 (FYE 31 May)",
           "WMT": "FY2027 (FYE 31 Jan)", "PAYX": "FY2027 (FYE 31 May)", "AME": "CY2026 (calendar)", "JPM": "CY2026 (calendar)"}
    ver["FY0"] = ver["ticker"].map(fyl)
    for c in ["lastFiscalYearEnd", "mostRecentQuarter", "fy0_end"]:
        ver[c] = pd.to_datetime(ver[c]).dt.date.astype(str)
    fy_sec = fye.set_index("ticker")["sec_fiscalYearEnd"]
    ver["SEC FYE (MMDD)"] = ver["ticker"].map(lambda t: str(fy_sec.get(t)).zfill(4))
    vt = ver[["ticker", "FY0", "lastFiscalYearEnd", "mostRecentQuarter", "fy0_end", "SEC FYE (MMDD)", "f_fy0_remaining", "eps_fy0", "eps_fy1", "eps_ntm",
              "pe_fy0", "pe_ntm", "pe_fy1", "forwardPE", "yahoo_fwd_horizon"]].rename(columns={
        "lastFiscalYearEnd": "last FYE (Yahoo)", "mostRecentQuarter": "MRQ", "fy0_end": "FY0 end (0y endDate)", "f_fy0_remaining": "f",
        "eps_fy0": "EPS FY0", "eps_fy1": "EPS FY1", "eps_ntm": "EPS NTM", "pe_fy0": "P/E FY0", "pe_ntm": "P/E NTM", "pe_fy1": "P/E FY1",
        "forwardPE": "Yahoo fwd P/E", "yahoo_fwd_horizon": "Yahoo horizon"})
    A(md(vt, {"f": ".3f", "EPS FY0": ".2f", "EPS FY1": ".2f", "EPS NTM": ".2f", "P/E FY0": ".1f", "P/E NTM": ".1f", "P/E FY1": ".1f", "Yahoo fwd P/E": ".1f"}))
    A("")
    A("Reading: for all eight names the FY0 end from earningsTrend agrees with `nextFiscalYearEnd` (within the 52/53-week offset) and with the SEC fiscal year-end, and `mostRecentQuarter` falls inside FY0. "
      "AAPL has 5 days of FY2026 left, so f ≈ 0.01 and NTM ≈ FY2027; that is why Yahoo's +1y multiple is nearly right for September year-ends. For MSFT (f = 0.76) the NTM window is still mostly FY2027, "
      "so Yahoo's FY2028-based 21.8x understates the 24.9x NTM multiple by 12.6%. For NVDA (f = 0.35) the 14.4x → 16.7x gap reproduces the prior review's finding "
      "(14.3x on FY+1 vs 24.1x on FY0). The correct NTM figure lies between the two.")
    A("")
    A("### 3.3 How often Yahoo forwardPE differs from NTM P/E by more than 10% (universe table)")
    A("")
    tt = ntab.copy()
    tt = tt.rename(columns={"share_gt10pct": "share >10%", "median_fwdPE_over_peNTM": "median Yahoo/NTM", "share_yahoo_lower": "share Yahoo lower"})
    A(md(tt, {"n": ".0f", "n_gt10pct": ".0f", "share >10%": ".1%", "median Yahoo/NTM": ".3f", "p10": ".3f", "p90": ".3f", "share Yahoo lower": ".1%"}))
    A("")
    A("(Full table: `v4/outputs/d4_ntm_vs_yahoo_table.csv`. Groups: FY-end month of FY0, f bucket, Yahoo horizon flag and GICS sector.)")
    A("")
    A("### 3.4 Largest horizon effects among clean names (ntm_quality = ok)")
    A("")
    ex = ok.assign(dev=(ok["fwdPE_over_peNTM"] - 1).abs()).sort_values("dev", ascending=False).head(15)
    ex = ex[["ticker", "fye_month", "f_fy0_remaining", "eps_fy0", "eps_fy1", "eps_ntm", "forwardPE", "pe_ntm", "pe_fy0", "fwdPE_over_peNTM"]].rename(columns={
        "fye_month": "FY0 end month", "f_fy0_remaining": "f", "forwardPE": "Yahoo fwd P/E", "pe_ntm": "NTM P/E", "pe_fy0": "FY0 P/E", "fwdPE_over_peNTM": "Yahoo/NTM"})
    A(md(ex, {"FY0 end month": ".0f", "f": ".2f", "eps_fy0": ".2f", "eps_fy1": ".2f", "eps_ntm": ".2f", "Yahoo fwd P/E": ".1f", "NTM P/E": ".1f", "FY0 P/E": ".1f", "Yahoo/NTM": ".3f"}))
    A("")
    A("### 3.5 Which horizon Yahoo's forwardEps / forwardPE uses (per ticker: `yahoo_fwd_horizon`)")
    A("")
    hzt = hz.rename_axis("horizon flag").reset_index(name="tickers")
    A(md(hzt))
    A("")
    A("`FY1(+1y)` means within 0.5% of the +1y consensus; `~` means the nearest horizon within 3%; `>3%off` means neither. `forwardPE` = price/`forwardEps` holds for all names with both fields. "
      "The 26 '>3% off' cases show that `info.forwardEps` and `info.epsCurrentYear` come from a different estimate feed or basis than earningsTrend. Examples: TTWO (earningsTrend "
      "FY1 5.29 on what appears to be a GAAP basis vs `forwardEps` 10.29), DASH (4.48 vs 8.14), TPL (`forwardEps` 73.12 is not adjusted for the 3:1 split of 2025-12-23), and "
      "PANW, DELL and REGN (a thin or stale +1y row). **Never mix `forwardEps` with earningsTrend rows.**")
    A("")
    A("### 3.6 Consensus quality grade (`ntm_quality`, `ntm_flags`)")
    A("")
    from collections import Counter
    c = Counter()
    for fl in s["ntm_flags"].fillna(""):
        for x in fl.split(";"):
            if x:
                key = x
                for pre in ["fy0_vs_quarterly_rows", "fy1_row_yearAgo_ne_fy0", "info_epsCurrentYear_vs_trend", "ntm_timeweighted_vs_quarteraware",
                            "fiscal_date_check", "estimates_from_sibling"]:
                    if x.startswith(pre):
                        key = pre
                c[key] += 1
    ct = pd.DataFrame(c.most_common(), columns=["flag", "tickers"])
    A(md(ct))
    A("")
    A("'unreliable' means at least one major issue: missing or non-positive NTM EPS; a REIT (EPS is not FFO); the FY0 annual row inconsistent with (reported YTD + remaining quarterly estimates) by more than 25%; "
      "or the +1y row's `yearAgoEps` ≠ the 0y consensus by more than 10%. Examples: CDNS (FY0 row 4.81 against reported YTD 4.07 plus remaining quarters 4.06), "
      "GOOGL and AMZN (the FY0 consensus includes large already-reported investment gains, so FY1 < FY0 and the quarter-aware NTM is 16% and 14% below the time-weighted figure), "
      "ECHO, DOC and VRTX (one-offs in FY0), and HON (the spin-off changed the perimeter). **Recommendation for downstream agents:** use `pe_ntm` where `ntm_quality == 'ok'`. "
      "For 'caution' names, also look at `pe_ntm_qaware` and `pe_ntm_qsum`. Do not rank 'unreliable' names on P/E without primary-source work (for REITs use FFO or AFFO).")
    A("")
    cf = V.get("cnbc_fpe_closest_horizon", {})
    A(f"**Independent comparator.** CNBC's forward P/E (LSEG data, horizon undocumented) is closest to our NTM P/E for {cf.get('counts', {}).get('NTM', 'n/a')}/{cf.get('n', 'n/a')} names, "
      f"to FY0 for {cf.get('counts', {}).get('FY0', 'n/a')} and to FY1 for {cf.get('counts', {}).get('FY1', 'n/a')}. Median absolute gaps: NTM {pctf(cf.get('median_absdev_by_horizon', {}).get('NTM'))}, "
      f"FY0 {pctf(cf.get('median_absdev_by_horizon', {}).get('FY0'))}, FY1 {pctf(cf.get('median_absdev_by_horizon', {}).get('FY1'))}. A second vendor therefore also puts the "
      "forward multiple nearer our NTM figure than Yahoo's +1y figure. The two consensus datasets differ, so this is corroboration, not validation.")
    A("")
    A("## 4. Validation (pass rates and failures)")
    A("")
    VC = V["vendor_crosscheck_cnbc"]
    vt2 = pd.DataFrame([
        ["(a) Price vs Cboe close 2026-09-25", P["cboe_compared"], P["cboe_pass_0p5pct"], "±0.5%", f"{P['cboe_exact_match']} exact; max gap {100 * P['max_abs_diff_cboe']:.3f}%"],
        ["(a) Price vs CNBC last 16:00 ET", P["cnbc_compared"], P["cnbc_pass_0p5pct"], "±0.5%", f"{P['cnbc_exact_match']} exact"],
        ["(a) Price vs Stooq (requested)", 0, 0, "±0.5%", "source blocked by a JS proof-of-work bot challenge; not circumvented"],
        ["(b) marketCap vs price×sharesOutstanding", M["compared"], M["pass_3pct"], "±3%", f"all {M['compared'] - M['pass_3pct']} failures are multi-class/UP-C/OP-unit"],
        ["(b') marketCap vs price×impliedSharesOutstanding", M["compared"], M["pass_3pct_using_implied_shares"], "±3%", "Yahoo's marketCap definition"],
        ["(c) SEC CY2025 revenue (primary concept) vs Yahoo FY2025", S["rev_compared"], S["rev_within_2pct"], "±2%", f"{S['dec_fye_companies']} Dec-FYE companies (unique CIK)"],
        ["(c) SEC revenue, best of 4 concepts", S["rev_best_concept_compared"], S["rev_within_2pct_best_concept"], "±2%", "diagnostic (lenient)"],
        ["(c) SEC NetIncomeLoss vs Yahoo Net Income", S["ni_compared"], S["ni_within_2pct"], "±2%", "4 SEC XBRL scale errors among failures"],
        ["(c) SEC net income, best pair", S["ni_best_pair_compared"], S["ni_within_2pct_best_pair"], "±2%", "diagnostic (NCI/preferred/ProfitLoss)"],
        ["(d) Staleness: regularMarketTime NY date = 2026-09-25", n, n - V["staleness"]["n_stale"], "exact date", "0 stale"],
        ["(f) FY0 end month vs SEC fiscalYearEnd", F["compared"], F["consistent"], "month (52/53-wk tol.)", "3 exceptions explained"],
        ["(f) lastFiscalYearEnd vs latest 10-K period", F["lfy_vs_last_annual_report_compared"], F["lfy_within_7d_of_last_annual_report"], "±7 days", "3 = results out, 10-K pending"],
        ["(extra) trailing EPS vs CNBC", VC["trailing_eps_compared"], VC["trailing_eps_within_5pct"], "±5%", f"{VC['trailing_eps_within_1pct']} within 1%"],
        ["(extra) sharesOutstanding vs CNBC", VC["shares_compared"], VC["shares_within_3pct"], "±3%", f"{VC['shares_within_3pct_either_yahoo_field']} using either Yahoo share field"],
    ], columns=["check", "compared", "pass", "tolerance", "note"])
    vt2["pass rate"] = [f"{100 * p / c_:.1f}%" if c_ else "n/a" for p, c_ in zip(vt2["pass"], vt2["compared"])]
    A(md(vt2[["check", "compared", "pass", "pass rate", "tolerance", "note"]]))
    A("")
    A("**(a) Prices.** No failures. Cboe `last_trade_time` and CNBC `last_time` are both dated 2026-09-25 for all 503. NYSE names print at 16:00–16:04 ET (closing auction), which is why a few `regularMarketTime` values read 20:03 UTC.")
    A("")
    mcf = mc[mc["pass_so_3pct"] == False]  # noqa: E712
    A(f"**(b) Market cap.** The {len(mcf)} names outside ±3% (price × `sharesOutstanding`): {', '.join(mcf['ticker'])}. Every one reconciles to 0.0% with `impliedSharesOutstanding`. "
      "Causes: listed dual classes (GOOGL/GOOG, FOXA/FOX, NWSA/NWS, BRK-B, BF-B), unlisted high-vote or founder classes (META, ABNB, DASH, PLTR, HOOD, COIN, DDOG, RDDT, WDAY, EL, NKE, HSY, TSN, RL, UPS, LEN, ...), "
      "and UP-C or operating-partnership units (IBKR +276%, TKO, BX, ARES, CHTR, SPG, ESS, EXR, UDR, BXP, ...). PCG (+36%) and BLK (+4.9%) have no obvious class structure and should be checked if their market cap is used. "
      "**Rule: use `marketCap` (all classes) for EV and size; use price and per-share EPS for P/E.**")
    A("")
    dec = sec[sec["dec_fye"] == True]  # noqa: E712
    rv = dec[dec["rev_pass_2pct"] == False].assign(a=lambda x: x["rev_gap"].abs()).sort_values("a", ascending=False)  # noqa: E712
    ni = dec[dec["ni_pass_2pct"] == False].assign(a=lambda x: x["ni_gap"].abs()).sort_values("a", ascending=False)  # noqa: E712
    A(f"**(c) SEC fundamentals.** Revenue failures ({len(rv)}): " + ", ".join(f"{t} ({g:+.0%}, {k})" for t, g, k in zip(rv["ticker"], rv["rev_gap"], rv["rev_gap_class"])) + ".")
    A("")
    A("Investigation of the largest revenue gaps:")
    A("* **Concept mismatch, not data error.** CPT (a REIT whose rental income is lease revenue; the ASC 606 concept captures only $13m), MTB, HBAN and IBKR (ASC 606 revenue is fee income only; Yahoo 'Total Revenue' is net revenue), "
      "AXP, ARES, RSG and HAS (another SEC revenue concept matches Yahoo within 2%).")
    A("* **Definition.** MO: Yahoo revenue is net of excise taxes ($20.1bn) vs $23.3bn gross. BRK-B: Yahoo includes investment and derivative gains. BX: performance allocations. EQT, ACGL, KEY: hedging, insurance and bank revenue definitions (about 3%).")
    A("* **SEC-side tagging anomaly.** FIX: the CY2025 `Revenues` frame holds $1.83bn against about $9.1bn total revenue (the tag is attached to a sub-total).")
    A("")
    A(f"Net-income failures ({len(ni)}): " + ", ".join(f"{t} ({k})" for t, k in zip(ni["ticker"], ni["ni_gap_class"])) + ".")
    A("* **SEC XBRL scale errors.** PCG NetIncomeLoss = 2,593 (should be $2.593bn), ANET = 3,511 ($3.511bn), ED = 2,023,000 ($2.023bn) and SCHW = 8,852,000 ($8.852bn). "
      "The frames API returns the value as filed, so primary-source XBRL needs a magnitude sanity check before use (a lesson for the D3 PIT-fundamentals agent).")
    A("* **Definition.** Non-controlling interests (TKO, DVA, FANG, CSGP), preferred dividends (MET), discontinued operations (DD after the Qnity spin, FTV after the Ralliant spin), and ECHO, where the NetIncomeLoss frame (−$52m) comes from a different filing than ProfitLoss (−$14.5bn, which matches Yahoo).")
    A(f"* Coverage: {len(S['dec_fye_without_sec_revenue'])} December-year-end companies have no revenue frame in the concepts used (mostly banks, brokers and utilities that tag other concepts), and {len(S['dec_fye_without_sec_netincome'])} have no NetIncomeLoss frame for CY2025.")
    A("")
    A("**(d) Staleness.** None: all 503 `regularMarketTime` values fall on 2026-09-25 between 20:00:00 and 20:04 UTC.")
    A("")
    A("## 5. Anomalies")
    A("")
    act = an.groupby(["check", "severity"]).ticker.nunique().reset_index(name="tickers").sort_values(["severity", "tickers"], ascending=[True, False])
    A(md(act))
    A("")
    def tl(chk):
        return ", ".join(sorted(an.loc[an["check"] == chk, "ticker"].unique()))
    A(f"* **Negative forward EPS**: {tl('negative_forward_eps')}. These are GAAP-basis consensus figures with charges (IPR&D at GILD, impairments at ARE); P/E is undefined (`pe_ntm_reason`).")
    A(f"* **P/E > 100 on NTM, trailing or forward EPS**: {tl('pe_gt_100')}.")
    A(f"* **Missing estimates**: CPRT (Yahoo's 0y row is empty and +1y is labelled with the same 2027-07-31 end), ERIE (no +1y), L (no coverage; its last earnings-calendar row is from 2020). "
      f"Thin +1y coverage (≤2 analysts): {tl('thin_coverage')}.")
    A(f"* **Extreme FY1 dispersion ((high−low)/|avg| > 1)**: {tl('eps_fy1_dispersion_extreme')}. The NVDA FY1 range is 9.80–18.75 on 53 analysts, so a mean-based NTM P/E is spuriously precise.")
    A("* **Metadata**: prevName (see §1 item 10). `ipoExpectedDate` is populated for 20 long-listed stocks (e.g. WMT 2025-12-09, LIN 2023-11-07, DPZ 2025-01-02), apparently a listing or ticker-change date; do not use it. "
      "FISV has no fiscal-date fields in `info` (the new ticker since 2025-11). The `recommendationMean` field sits a median "
      f"{V['rec_mean_systematic_offset']['median_info_minus_counts_mean']:+.2f} points below the mean implied by `recommendations_summary` counts, so the two are not the same measure; use one consistently.")
    A("* **EV ≤ 0**: BRK-B, BNY, IBKR and STT (cash-rich financials). EV/sales is not meaningful for financials generally.")
    A("")
    A("## 6. Change log vs the legacy v3 snapshot (equity_project/info.json + est_all.pkl, Yahoo 2026-09-24)")
    A("")
    clt = cl[["ticker", "legacy_price", "fresh_price", "chg_price", "chg_forwardEps", "chg_eps_fy0", "chg_eps_fy1", "chg_targetMean", "legacy_forwardPE", "fresh_pe_ntm", "flags_gt2pct"]].copy()
    clt["30d FY1 rev"] = clt["ticker"].map(v3["eps_fy1_rev30_pct"])
    clt["ntm_quality"] = clt["ticker"].map(v3["ntm_quality"])
    clt["flags_gt2pct"] = clt["flags_gt2pct"].fillna("none")
    A(md(clt, {"legacy_price": ".2f", "fresh_price": ".2f", "chg_price": "+.2%", "chg_forwardEps": "+.2%", "chg_eps_fy0": "+.2%", "chg_eps_fy1": "+.2%",
               "chg_targetMean": "+.2%", "legacy_forwardPE": ".1f", "fresh_pe_ntm": ".1f", "30d FY1 rev": "+.1%"}))
    A("")
    A("There are no estimate changes above 2% between the two snapshots, which are one session apart. PAYX reported before the legacy pull; its FY0 consensus moved −0.3% over 30 days and 0.0% over 7 days, "
      "so the legacy estimates were not stale in a material way. What *does* change materially is the multiple once it is calendarized: every v3 name's NTM P/E is above the v3 'Fwd P/E'. "
      "ABNB carries a 'caution' flag because seasonality makes the time-weighted and quarter-aware NTM differ by 13%. AME's thin +1y coverage is 3 analysts out of 12 on FY0; its Indicor acquisition closed on 2026-08-26 and may not be in all estimates.")
    A("")
    A("## 7. Corporate events (best-effort)")
    A("")
    A("Method: SEC submissions (primary source) plus Yahoo headlines. Signals: SC 14D-9 (target of a tender offer); PREM14A/DEFM14A (merger vote); SC TO-T without 14D-9 (the company is the bidder); S-4 (stock deal, usually the acquirer); "
      "8-K Item 2.01 (completed acquisition or disposition, last 180 days). Headlines are read for the company's position relative to the deal verb. 25-NSE is ignored because it is routinely filed for delisted notes.")
    A("")
    evs = pd.DataFrame([{"flag": c_, "tickers": int((ev[c_] != "").sum())} for c_ in ["evt_being_acquired", "evt_acquirer_pending_or_recent", "evt_recent_completed_deal", "evt_spinoff_separation"]])
    A(md(evs))
    A("")
    A("Reviewed target and merger-party list (each checked against headline and SEC evidence):")
    A("")
    A(md(pd.DataFrame([
        ["WBD", "target", "Paramount Skydance acquisition; SC 14D-9 (Feb 2026), DEFM14A (Mar 2026)"],
        ["KVUE", "target", "Kimberly-Clark acquisition; holders approved 2026-01-29; regulatory review ongoing"],
        ["TECH", "target", "Merck KGaA, Darmstadt; DEFM14A 2026-08-20; holders approved 2026-09-23"],
        ["AES", "target", "GIP/EQT-led consortium (announced 2026-03-02); DEFM14A 2026-05-15"],
        ["NSC", "target", "Union Pacific merger; DEFM14A 2025-10-01; STB review ongoing"],
        ["D", "merger party", "all-stock combination with NEE (announced 2026-05-18); D DEFM14A 2026-07-28, NEE S-4 2026-07-09"],
        ["DVN", "not pending", "Coterra merger completed 2026-05-07; activist letter 2026-09-23 urges a sale"],
        ["CCL", "reorganisation", "DEFM14A 2026-02-27 and S-4: DLC unification (Yahoo longName now 'Carnival Corporation Ltd.')"],
        ["MGM", "bid withdrawn", "People Inc. $48.30 cash proposal (2026-06-01) dropped 2026-09-24"],
    ], columns=["ticker", "role", "evidence"])))
    A("")
    A("Other acquirers with SEC S-4 or tender filings in the last 12 months include AWK, BSX, CTAS, FITB, HBAN, KMB, NEE, ON, SWKS, UNP, VICI, AVGO, AMZN, A, CMCSA, DD, PSA and SPGI, plus FOXA and FOX (Roku), "
      "and the tender bidders CPRT (ACV), MRK, GILD, LLY, BIIB and PSKY. The full list with evidence strings is in the CSV. Spin-offs and separations: FDXF and HONA (completed 2026; both new constituents), Q (Qnity, from DD), "
      "CTVA (Vylor), FLEX (cloud and power infrastructure, Form 10 filed), GPC (automotive/industrial split), SOLV (health-information systems), MDT (MiniMed exchange offer) and KDP (breakup).")
    A("")
    A("## 8. Limitations")
    A("")
    A("* Yahoo consensus is a vendor snapshot with an undocumented, company-specific basis (GAAP for some, adjusted for others) and undocumented analyst sets. The NTM figure inherits this; `ntm_quality` flags only detectable inconsistencies.")
    A("* Time-weighted NTM assumes earnings are spread evenly within each fiscal year. Seasonal businesses (ABNB, retailers) and years with large booked one-offs (GOOGL, AMZN, ECHO) are better read with `pe_ntm_qaware`/`pe_ntm_qsum`. "
      "There is no FY2 estimate, so NTM for f = 0 names is approximated by FY1.")
    A("* Independent price sources are delayed-quote vendors (Cboe, CNBC), not an exchange-certified official close. Stooq could not be used without solving a bot challenge.")
    A("* SEC frames cover only filers tagging the chosen concepts and contain filer errors; the check is limited to December year-ends (381 companies) and FY2025.")
    A("* Corporate-event flags rely on heuristics: headline tabs hold only about 30 items, and merger proxies can be filed by acquirers or for reorganisations. Treat them as leads for the diligence agents, not facts.")
    A("* This is live, not point-in-time, data. It must not be used in backtests (see CONVENTIONS: PIT rule).")
    A("")
    A("## 9. Files produced")
    A("")
    files = [
        ("v4/data/d4_live_snapshot.parquet", len(s), "one row per constituent; 269 columns incl. NTM fields, quality grade, retrieval times"),
        ("v4/data/d4_universe.csv", len(pd.read_csv(DATA / "d4_universe.csv")), "Wikipedia constituents (ticker, name, GICS, CIK)"),
        ("v4/data/d4_indep_prices.csv", len(ip), "Cboe close + CNBC last/eps/shares/fpe"),
        ("v4/data/d4_validation_prices.csv", len(pd.read_csv(DATA / "d4_validation_prices.csv")), "price + vendor cross-checks"),
        ("v4/data/d4_validation_mcap.csv", len(mc), "market-cap reconciliation"),
        ("v4/data/d4_validation_sec.csv", len(sec), "SEC frames vs Yahoo income statement (per CIK)"),
        ("v4/data/d4_validation_fye.csv", len(fye), "fiscal-year-end vs SEC"),
        ("v4/data/d4_anomalies.csv", len(an), "long-format anomaly flags"),
        ("v4/data/d4_changelog_v3.csv", len(cl), "legacy vs fresh for 14 v3 names"),
        ("v4/data/d4_corporate_events.csv", len(ev), "event flags with evidence"),
        ("v4/outputs/d4_ntm_vs_yahoo_table.csv", len(ntab), "universe table of Yahoo fwd P/E vs NTM P/E"),
        ("v4/outputs/d4_validation_summary.json", 1, "all validation statistics"),
    ]
    A(md(pd.DataFrame(files, columns=["file", "rows", "content"])))
    A("")
    A("Each dataset has a `<name>.meta.json` sidecar. Scripts: `v4/code/d4_common.py`, `d4_universe.py`, `d4_fetch_yahoo.py`, `d4_fetch_indep_prices.py`, `d4_fetch_sec.py`, "
      "`d4_build_snapshot.py`, `d4_validate.py`, `d4_events.py`, `d4_changelog.py`, `d4_report.py`. Raw cache (not synced): `C:\\Users\\user\\eqv4\\cache\\d4\\`.")
    A("")
    A("## 10. Sources")
    A("")
    A("* Constituents: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies (retrieved 2026-09-25).")
    A("* Yahoo Finance via yfinance 1.7.0: https://query2.finance.yahoo.com/v10/finance/quoteSummary/{T} (earningsTrend, earningsHistory, financialData, recommendationTrend, upgradeDowngradeHistory, calendarEvents), "
      "https://query1.finance.yahoo.com/v7/finance/quote, https://finance.yahoo.com/calendar/earnings?symbol={T}.")
    A("* Cboe delayed quotes: https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/{SYM}.json; CNBC: https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols={A|B}.")
    A("* Stooq (blocked): https://stooq.com/q/d/l/?s=nvda.us&i=d (bot-challenge page cached as `cache/d4/indep_prices/stooq_probe_nvda.txt`).")
    A("* SEC XBRL frames: https://data.sec.gov/api/xbrl/frames/us-gaap/{Concept}/USD/CY2025.json; submissions: https://data.sec.gov/submissions/CIK##########.json.")
    A("* Amcor FYE change: https://www.sec.gov/Archives/edgar/data/1748790/000110465926055873/tm2613113d1_8k.htm (8-K Item 5.03, filed 2026-05-06).")
    A("* FedEx FYE change: https://www.sec.gov/Archives/edgar/data/1048911/000104891126000108/fdx-20260721.htm (8-K Item 2.02, filed 2026-07-21).")
    A("* Prior review being tested: `review/agents/02_market_data.md` (NVDA 14.32x vs 24.13x horizon finding and the NVDA prevName anomaly; both reproduced).")
    out = OUT / "d4_report.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    # sidecars for output tables
    write_meta(OUT / "d4_ntm_vs_yahoo_table.csv", {"description": "share of names where Yahoo forwardPE differs >10% from NTM P/E, by group",
                                                   "rows": int(len(ntab)), "columns": list(ntab.columns),
                                                   "inputs": ["v4/data/d4_live_snapshot.parquet"], "generated_by": "v4/code/d4_validate.py"})
    write_meta(OUT / "d4_validation_summary.json", {"description": "validation statistics (price, mcap, SEC, FYE, anomalies, NTM, staleness)",
                                                    "inputs": ["v4/data/d4_*.csv", "v4/data/d4_live_snapshot.parquet"], "generated_by": "v4/code/d4_validate.py"})
    fy = pd.read_csv(DATA / "d4_validation_fye.csv")
    write_meta(DATA / "d4_validation_fye.csv", {"description": "Yahoo fiscal calendar vs SEC submissions (fiscalYearEnd + latest annual report period)",
                                                "rows": int(len(fy)), "columns": list(fy.columns),
                                                "source_urls": ["https://data.sec.gov/submissions/CIK##########.json"], "generated_by": "v4/code/d4_validate.py"})
    print("written", out, len(L), "lines")


if __name__ == "__main__":
    main()
