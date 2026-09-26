"""d3_pit_core.py - point-in-time (as-filed) feature engine for ONE company lineage.

Core rule: the state at date E contains, for every (concept, period) the value from the LATEST filing with filed <= E
(ties on the same day broken by accession number). Features at month-end t are computed from the state at the last
filing date E <= t (main panel) or E < t (lag-1 variant). Nothing filed after t can enter a feature at t.

Periods: duration d = end - start (days). Quarter: 84..98, half: ~180, 9M: ~272, year: 350..380 (52/53-week years ok).
Quarterly values of flow items: direct 3-month facts; otherwise derived from same-start cumulative (YTD) facts,
e.g. Q2 = 6M - 3M, Q4 = FY - 9M (closure applied twice, so Q4 = (FY - 6M) - Q3 also works).
TTM = sum of the latest 4 consecutive fiscal quarters, or the latest annual (FY) value if its period ends at least as
late as the quarterly window.
"""
from __future__ import annotations

import bisect
import math
from collections import defaultdict

import numpy as np
import pandas as pd

from d3_common import PANEL_FORMS

QMIN, QMAX = 84, 98
YMIN, YMAX = 350, 380
PRUNE_DAYS = 1900          # keep ~5 years of periods behind the latest period end in the state
INST_STALE = 190           # instant items may be at most ~2 quarters older than the balance-sheet anchor

SHARE_CONCEPTS = {"WeightedAverageNumberOfDilutedSharesOutstanding", "WeightedAverageNumberOfSharesOutstandingBasic",
                  "CommonStockSharesOutstanding", "EntityCommonStockSharesOutstanding"}
EPS_CONCEPTS = {"EarningsPerShareDiluted", "EarningsPerShareBasic", "EarningsPerShareBasicAndDiluted"}


def unit_of(concept: str) -> str:
    if concept in SHARE_CONCEPTS:
        return "shares"
    if concept in EPS_CONCEPTS:
        return "USD/shares"
    return "USD"


# ---------------------------------------------------------------- fallback / priority rules (documented in report)
REV_PRIORITY = ["RevenuesNetOfInterestExpense", "Revenues", "RegulatedAndUnregulatedOperatingRevenue",
                "RevenueFromContractWithCustomerExcludingAssessedTax",
                "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet",
                # industry-specific totals (pre-ASC 606 taxonomy), lowest priority
                "HealthCareOrganizationRevenue", "OilAndGasRevenue", "RefiningAndMarketingRevenue",
                "FoodAndBeverageRevenue", "RealEstateRevenueNet", "ElectricUtilityRevenue"]
COGS = ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold"]
FLOW_SPECS = {
    "opinc": ["OperatingIncomeLoss"],
    "ni": ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "DepreciationAmortizationAndAccretionNet"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
    "div": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
    "buyback": ["PaymentsForRepurchaseOfCommonStock", "PaymentsForRepurchaseOfEquity"],
    "issuance": ["ProceedsFromIssuanceOfCommonStock"],
    "interest": ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"],
    "tax": ["IncomeTaxExpenseBenefit"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "rd": ["ResearchAndDevelopmentExpense"],
    "sga": ["SellingGeneralAndAdministrativeExpense"],
    "cogs": COGS,
}
EPS_PRIORITY = ["EarningsPerShareDiluted", "EarningsPerShareBasicAndDiluted", "EarningsPerShareBasic"]
N_EPS = 13   # q0..q12 (SUE needs q0..q12 for 8 prior YoY differences)

# split ratios: p/q with small integers + common large ratios, excluding |r-1| < 0.15
_R = set()
for p in range(1, 11):
    for q in range(1, 11):
        _R.add(p / q)
for k in (12, 15, 20, 25, 30, 40, 50, 100):
    _R.add(float(k)); _R.add(1.0 / k)
SPLIT_RATIOS = np.array(sorted(r for r in _R if abs(r - 1.0) >= 0.15))


def _match_ratio(r: float, tol: float):
    if not np.isfinite(r) or r <= 0:
        return None
    i = np.argmin(np.abs(SPLIT_RATIOS / r - 1.0))
    c = SPLIT_RATIOS[i]
    return float(c) if abs(r / c - 1.0) <= tol else None


def to_days(s: pd.Series) -> np.ndarray:
    return ((s.values.astype("datetime64[D]") - np.datetime64("1970-01-01", "D")).astype("int64"))


def day2ts(d):
    if d is None or (isinstance(d, float) and math.isnan(d)):
        return pd.NaT
    return pd.Timestamp("1970-01-01") + pd.Timedelta(days=int(d))


# ================================================================ records
def prepare_records(fc: pd.DataFrame, forms=PANEL_FORMS):
    """fc: facts of one lineage (columns concept, unit, val, start, end, filed, form, accn). Returns dict concept ->
    list of (filed, accn, start|-1, end, val) sorted by (filed, accn), plus sorted filing events [(filed, accn, form)]."""
    f = fc[fc["form"].astype(str).isin(forms) & fc["val"].notna() & fc["end"].notna() & fc["filed"].notna()].copy()
    f["concept"] = f["concept"].astype(str)
    f["unit"] = f["unit"].astype(str)
    f = f[f["unit"].values == f["concept"].map(unit_of).values]
    f["s"] = np.where(f["start"].notna(), to_days(f["start"].fillna(pd.Timestamp("1970-01-01"))), -1)
    f["e"] = to_days(f["end"])
    f["fd"] = to_days(f["filed"])
    f["accn"] = f["accn"].astype(str)
    f = f.sort_values(["fd", "accn"], kind="mergesort")
    recs = defaultdict(list)
    for c, fd, a, s, e, v in zip(f["concept"].values, f["fd"].values, f["accn"].values, f["s"].values, f["e"].values,
                                 f["val"].values):
        recs[c].append((int(fd), a, int(s), int(e), float(v)))
    filings = f.drop_duplicates(["fd", "accn"])[["fd", "accn", "form"]]
    filings = [(int(a), b, str(c)) for a, b, c in zip(filings["fd"], filings["accn"], filings["form"])]
    return recs, filings


# ================================================================ split detection
def detect_splits(recs):
    """Detect stock splits from restated comparatives: the same period's weighted shares (x r) or EPS (/ r) re-reported
    in a later filing with r ~ simple split ratio. Returns clusters [{'reveal': day, 'accept': day, 'ratio': r, ...}]."""
    dets = []
    for c in ["WeightedAverageNumberOfDilutedSharesOutstanding", "WeightedAverageNumberOfSharesOutstandingBasic",
              "EarningsPerShareDiluted", "EarningsPerShareBasic", "EarningsPerShareBasicAndDiluted"]:
        is_sh = c.startswith("Weighted")
        last = {}
        for fd, a, s, e, v in recs.get(c, []):
            key = (s, e)
            if key in last:
                v0, f0 = last[key]
                if fd > f0:
                    if is_sh and v0 > 1e4 and v > 1e4:
                        m = _match_ratio(v / v0, 0.015)
                        if m:
                            dets.append((fd, f0, m, "shares", key))
                    elif (not is_sh) and abs(v0) >= 0.10 and abs(v) >= 0.02 and (v0 > 0) == (v > 0):
                        m = _match_ratio(v0 / v, 0.03)
                        if m:
                            dets.append((fd, f0, m, "eps", key))
            last[key] = (v, fd)
    dets.sort()
    clusters = []
    for fd, f0, r, kind, key in dets:
        tgt = None
        for cl in clusters:
            if cl["ratio"] == r and f0 < cl["reveal"] <= fd:
                tgt = cl
                break
        if tgt is None:
            tgt = {"ratio": r, "reveal": fd, "n_sh": 0, "eps_keys": set(), "accept": None, "last": fd}
            clusters.append(tgt)
        if kind == "shares":
            tgt["n_sh"] += 1
        else:
            tgt["eps_keys"].add(key)
        tgt["last"] = max(tgt["last"], fd)
        if tgt["accept"] is None and (tgt["n_sh"] >= 1 or len(tgt["eps_keys"]) >= 2):
            tgt["accept"] = fd
    return [dict(ratio=c["ratio"], reveal=c["reveal"], accept=c["accept"], n_sh=c["n_sh"], n_eps=len(c["eps_keys"]))
            for c in clusters if c["accept"] is not None]


class SplitAdj:
    """factor(filed) = product of ratios of splits revealed after `filed` and accepted by the evaluation date."""

    def __init__(self, clusters, E):
        act = sorted((c["reveal"], c["ratio"]) for c in clusters if c["accept"] <= E)
        self.reveals = [a for a, _ in act]
        suf = [1.0] * (len(act) + 1)
        for i in range(len(act) - 1, -1, -1):
            suf[i] = suf[i + 1] * act[i][1]
        self.suf = suf

    def factor(self, filed):
        if not self.reveals:
            return 1.0
        return self.suf[bisect.bisect_right(self.reveals, filed)]


# ================================================================ period arithmetic
def derive_quarters(pool):
    """pool: {(s,e): (v, f)} durations. Returns {e: (s, v, f, derived)} for quarter-length intervals."""
    Q = {}
    for (s, e), (v, f) in pool.items():
        d = e - s
        if QMIN <= d <= QMAX:
            old = Q.get(e)
            if old is None or abs(d - 91) < abs((e - old[0]) - 91):
                Q[e] = (s, v, f, False)
    ivs = dict(pool)
    for _ in range(2):
        by_s = defaultdict(list)
        for (s, e), (v, f) in ivs.items():
            by_s[s].append((e, v, f))
        new = {}
        for s, lst in by_s.items():
            if len(lst) < 2:
                continue
            lst.sort()
            n = len(lst)
            for i in range(n - 1):
                e1, v1, f1 = lst[i]
                for j in range(i + 1, n):
                    e2, v2, f2 = lst[j]
                    key = (e1 + 1, e2)
                    if key in ivs or key in new or (e2 - e1 - 1) < QMIN:
                        continue
                    new[key] = (v2 - v1, max(f1, f2))
        if not new:
            break
        ivs.update(new)
        for (s, e), (v, f) in new.items():
            if QMIN <= e - s <= QMAX and e not in Q:
                Q[e] = (s, v, f, True)
    return Q


def ttm_from(pool, Q=None):
    """Returns (ttm_value, period_end, max_filed, src) or None."""
    if not pool:
        return None
    if Q is None:
        Q = derive_quarters(pool)
    best_ann = None
    for (s, e), (v, f) in pool.items():
        if YMIN <= e - s <= YMAX and (best_ann is None or e > best_ann[1] or (e == best_ann[1] and f > best_ann[2])):
            best_ann = (v, e, f)
    best_q = None
    if len(Q) >= 4:
        ends = sorted(Q)
        latest = ends[-1]
        for idx in range(len(ends) - 1, 2, -1):
            if latest - ends[idx] > 400:
                break
            w = [(ends[k],) + Q[ends[k]] for k in range(idx - 3, idx + 1)]   # (e, s, v, f, der)
            ok = all(1 <= w[k + 1][1] - w[k][0] <= 5 for k in range(3)) and YMIN <= w[3][0] - w[0][1] <= YMAX
            if ok:
                best_q = (sum(x[2] for x in w), w[3][0], max(x[3] for x in w))
                break
    if best_ann is not None and (best_q is None or best_ann[1] >= best_q[1]):
        return best_ann + ("annual",)
    if best_q is not None:
        return best_q + ("4q",)
    return None


# ================================================================ the engine
class CompanyEngine:
    def __init__(self, fc: pd.DataFrame, is_financial_sic: bool = False):
        self.recs, self.filings = prepare_records(fc)
        self.splits = detect_splits(self.recs)
        self.is_fin_sic = is_financial_sic
        self.dur = defaultdict(dict)    # concept -> {(s,e): (v, f)}
        self.inst = defaultdict(dict)   # concept -> {e: (v, f)}
        self.maxend = {}
        by_day = defaultdict(list)
        for c, lst in self.recs.items():
            for fd, a, s, e, v in lst:
                by_day[fd].append((a, c, s, e, v))
        self.by_day = {d: sorted(x, key=lambda z: z[0]) for d, x in by_day.items()}
        self.events = sorted(self.by_day)
        self.form_of_day = {}
        for fd, a, form in self.filings:
            self.form_of_day[fd] = form   # last accession of the day
        self.ever_current_assets = False

    # ---------------- state update
    def apply(self, E):
        for a, c, s, e, v in self.by_day[E]:
            if s >= 0:
                self.dur[c][(s, e)] = (v, E)
            else:
                self.inst[c][e] = (v, E)
            if c == "AssetsCurrent":
                self.ever_current_assets = True
            if c != "EntityCommonStockSharesOutstanding" and e > self.maxend.get(c, -10**9):
                self.maxend[c] = e

    def prune(self):
        gmax = max(self.maxend.values()) if self.maxend else 0
        cut = gmax - PRUNE_DAYS
        for d in (self.dur, self.inst):
            for c, m in d.items():
                if len(m) > 60:
                    for k in [k for k in m if (k[1] if isinstance(k, tuple) else k) < cut]:
                        del m[k]

    # ---------------- helpers
    def merged_dur(self, concepts):
        out = {}
        for c in concepts:
            m = self.dur.get(c)
            if not m:
                continue
            for k, vf in m.items():
                if k not in out:
                    out[k] = vf
        return out

    def rev_pool(self):
        d = self.dur
        keys = set()
        for c in REV_PRIORITY + ["SalesRevenueGoodsNet", "SalesRevenueServicesNet", "InterestIncomeExpenseNet",
                                 "OperatingLeaseLeaseIncome", "OperatingLeasesIncomeStatementLeaseRevenue"]:
            if c in d:
                keys.update(d[c].keys())
        out = {}
        g = lambda c, k: d[c].get(k) if c in d else None
        for k in keys:
            cands = []
            for c in REV_PRIORITY:
                x = g(c, k)
                if x is not None:
                    cands.append(x)
            rnfc = g("RevenueNotFromContractWithCustomer", k)
            if rnfc is not None and g("Revenues", k) is None and g("RevenuesNetOfInterestExpense", k) is None:
                for c in ("RevenueFromContractWithCustomerExcludingAssessedTax",
                          "RevenueFromContractWithCustomerIncludingAssessedTax"):
                    x = g(c, k)
                    if x is not None:
                        cands.insert(0, (x[0] + rnfc[0], max(x[1], rnfc[1])))
                        break
            gs = [g("SalesRevenueGoodsNet", k), g("SalesRevenueServicesNet", k)]
            gs = [x for x in gs if x is not None]
            if gs:
                cands.append((sum(x[0] for x in gs), max(x[1] for x in gs)))
            chosen = cands[0] if cands else None
            # consistency anchor: GrossProfit + cost of revenue, else OperatingIncome + CostsAndExpenses
            if len(cands) > 1:
                gp = g("GrossProfit", k)
                cg = next((g(c, k) for c in COGS if g(c, k) is not None), None)
                anchor = None
                if gp is not None and cg is not None:
                    anchor = gp[0] + cg[0]
                else:
                    oi, ce = g("OperatingIncomeLoss", k), g("CostsAndExpenses", k)
                    if oi is not None and ce is not None:
                        anchor = oi[0] + ce[0]
                if anchor and anchor > 0:
                    best = min(cands, key=lambda x: abs(x[0] / anchor - 1.0))
                    if abs(best[0] / anchor - 1.0) <= 0.015:
                        chosen = best
            # banks: net interest income + noninterest income when no total (or only a small component) is tagged
            nii, nonii = g("InterestIncomeExpenseNet", k), g("NoninterestIncome", k)
            if nii is not None and nonii is not None:
                bank = (nii[0] + nonii[0], max(nii[1], nonii[1]))
                if chosen is None or (bank[0] > 0 and chosen[0] < 0.5 * bank[0]):
                    chosen = bank
            # REITs: lease income when revenue is only a small ASC-606 component
            lease = g("OperatingLeaseLeaseIncome", k) or g("OperatingLeasesIncomeStatementLeaseRevenue", k)
            if lease is not None and lease[0] > 0:
                if chosen is None:
                    chosen = lease
                elif chosen[0] < 0.5 * lease[0] and g("Revenues", k) is None:
                    chosen = (chosen[0] + lease[0], max(chosen[1], lease[1]))
            if chosen is not None:
                out[k] = chosen
        return out

    def gp_pool(self, rev):
        gp = dict(self.dur.get("GrossProfit", {}))
        cogs = self.merged_dur(COGS)
        for k, (cv, cf) in cogs.items():
            if k not in gp and k in rev:
                rv, rf = rev[k]
                gp[k] = (rv - cv, max(rf, cf))
        return gp

    def eps_series(self, adj: SplitAdj):
        pool = {}
        for c in EPS_PRIORITY:
            for k, (v, f) in self.dur.get(c, {}).items():
                if k not in pool:
                    pool[k] = (v / adj.factor(f), f)
        Q = derive_quarters(pool)
        self._epsQ = Q
        if not Q:
            return [], None
        ends = sorted(Q)
        q0 = ends[-1]
        out = []
        for i in range(N_EPS):
            tgt = q0 - i * 91.3125
            j = bisect.bisect_left(ends, tgt)
            best = None
            for jj in (j - 1, j):
                if 0 <= jj < len(ends) and abs(ends[jj] - tgt) <= 20:
                    if best is None or abs(ends[jj] - tgt) < abs(best - tgt):
                        best = ends[jj]
            if best is None:
                out.append((i, None, np.nan, None, None))
            else:
                s, v, f, der = Q[best]
                out.append((i, best, v, f, der))
        return out, q0

    def inst_merged(self, concepts):
        out = {}
        for c in concepts:
            for e, vf in self.inst.get(c, {}).items():
                if e not in out:
                    out[e] = vf
        return out

    @staticmethod
    def at(m, anchor, stale=INST_STALE):
        """latest (v, e, f) in instant map m with anchor-stale <= e <= anchor."""
        best = None
        for e, (v, f) in m.items():
            if anchor - stale <= e <= anchor and (best is None or e > best[1]):
                best = (v, e, f)
        return best

    @staticmethod
    def near(m, target, tol):
        best = None
        for e, (v, f) in m.items():
            if abs(e - target) <= tol and (best is None or abs(e - target) < abs(best[1] - target)):
                best = (v, e, f)
        return best

    # ---------------- features at state E
    def features(self, E):
        F = {}
        used = []   # filed days of all facts used
        adj = SplitAdj(self.splits, E)

        def put_ttm(name, pool):
            r = ttm_from(pool)
            if r is None:
                F[name + "_ttm"] = np.nan
                return None
            v, e, f, src = r
            F[name + "_ttm"] = v
            used.append(f)
            return r

        rev = self.rev_pool()
        r = put_ttm("rev", rev)
        F["rev_ttm_end"] = day2ts(r[1]) if r else pd.NaT
        F["rev_ttm_src"] = r[3] if r else None
        put_ttm("gp", self.gp_pool(rev))
        for name, concepts in FLOW_SPECS.items():
            r = put_ttm(name, self.merged_dur(concepts))
            if name in ("ni", "ocf"):
                F[name + "_ttm_end"] = day2ts(r[1]) if r else pd.NaT
        # EBIT proxy
        if not np.isnan(F["opinc_ttm"]):
            F["ebit_ttm"], F["ebit_src"] = F["opinc_ttm"], "OperatingIncomeLoss"
        elif not np.isnan(F["pretax_ttm"]) and not np.isnan(F["interest_ttm"]):
            F["ebit_ttm"], F["ebit_src"] = F["pretax_ttm"] + F["interest_ttm"], "pretax+interest"
        else:
            F["ebit_ttm"], F["ebit_src"] = np.nan, None

        # ---------- instants
        assets_m = self.inst_merged(["Assets"])
        anchor_src = assets_m or self.inst_merged(["LiabilitiesAndStockholdersEquity", "StockholdersEquity"])
        anchor = max(anchor_src) if anchor_src else None
        F["bs_date"] = day2ts(anchor) if anchor is not None else pd.NaT

        def inst_feat(name, concepts, stale=INST_STALE, one_year=False):
            m = self.inst_merged(concepts)
            x = self.at(m, anchor, stale) if (m and anchor is not None) else None
            F[name] = x[0] if x else np.nan
            if x:
                used.append(x[2])
            if one_year:
                y = self.near(m, (x[1] if x else anchor) - 365, 15) if (m and anchor is not None) else None
                F[name + "_1y_ago"] = y[0] if y else np.nan
                if y:
                    used.append(y[2])
            return x

        inst_feat("assets", ["Assets"], one_year=True)
        inst_feat("equity", ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
                  one_year=True)
        inst_feat("assets_current", ["AssetsCurrent"], stale=0)
        inst_feat("liab_current", ["LiabilitiesCurrent"], stale=0)
        inst_feat("goodwill", ["Goodwill"])
        inst_feat("intangibles", ["IntangibleAssetsNetExcludingGoodwill"])
        # liabilities
        li = inst_feat("liabilities", ["Liabilities"], stale=0)
        F["liabilities_src"] = "Liabilities" if li else None
        if not li and anchor is not None:
            lse = self.at(self.inst.get("LiabilitiesAndStockholdersEquity", {}), anchor, 0)
            eqn = self.at(self.inst.get("StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", {}), anchor, 0)
            eqp = self.at(self.inst.get("StockholdersEquity", {}), anchor, 0)
            mi = self.at(self.inst.get("MinorityInterest", {}), anchor, 0)
            if lse and eqn:
                F["liabilities"], F["liabilities_src"] = lse[0] - eqn[0], "L&SE-EquityInclNCI"
                used += [lse[2], eqn[2]]
            elif lse and eqp:
                F["liabilities"] = lse[0] - eqp[0] - (mi[0] if mi else 0.0)
                F["liabilities_src"] = "L&SE-Equity-NCI"
                used += [lse[2], eqp[2]]
        # cash + short-term investments (same balance-sheet date)
        cash = None
        for c in ("CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
                  "CashAndDueFromBanks"):
            x = self.at(self.inst.get(c, {}), anchor, 0) if anchor is not None else None
            if x:
                cash = x
                break
        if cash:
            sti = None
            for c in ("ShortTermInvestments", "MarketableSecuritiesCurrent", "AvailableForSaleSecuritiesDebtSecuritiesCurrent"):
                x = self.at(self.inst.get(c, {}), anchor, 0)
                if x:
                    sti = x
                    break
            F["cash_sti"] = cash[0] + (sti[0] if sti else 0.0)
            used.append(cash[2])
            if sti:
                used.append(sti[2])
        else:
            F["cash_sti"] = np.nan
        # total debt
        F["total_debt"], F["debt_src"] = np.nan, None
        if anchor is not None:
            g0 = lambda c: self.at(self.inst.get(c, {}), anchor, 0)
            ltd, ltdn, ltdc = g0("LongTermDebt"), g0("LongTermDebtNoncurrent"), g0("LongTermDebtCurrent")
            clo, cloc = g0("LongTermDebtAndCapitalLeaseObligations"), g0("LongTermDebtAndCapitalLeaseObligationsCurrent")
            stb, cp, dc = g0("ShortTermBorrowings"), g0("CommercialPaper"), g0("DebtCurrent")
            st = max([x[0] for x in (stb, cp) if x] or [0.0])
            parts = None
            if ltd:
                parts, src = [ltd], "LongTermDebt"
            elif ltdn:
                parts, src = [ltdn] + ([ltdc] if ltdc else []), "LTDNoncurrent+Current"
            elif clo:
                parts, src = [clo] + ([cloc] if cloc else []), "LTDandCapitalLease(+Current)"
            if parts is not None:
                F["total_debt"] = sum(x[0] for x in parts) + st
                F["debt_src"] = src + ("+ST" if st else "")
                used += [x[2] for x in parts] + [x[2] for x in (stb, cp) if x]
            elif dc:
                F["total_debt"], F["debt_src"] = dc[0], "DebtCurrent"
                used.append(dc[2])
            elif stb or cp:
                F["total_debt"], F["debt_src"] = st, "ShortTermOnly"
                used += [x[2] for x in (stb, cp) if x]

        # ---------- shares (split-adjusted to the latest basis known at E)
        def sh_map(c):
            return {e: (v * adj.factor(f), f) for e, (v, f) in self.inst.get(c, {}).items()}

        wd = {}
        for c in ("WeightedAverageNumberOfDilutedSharesOutstanding", "WeightedAverageNumberOfSharesOutstandingBasic"):
            for k, (v, f) in self.dur.get(c, {}).items():
                if k not in wd:
                    wd[k] = (v * adj.factor(f), f)
        wdil = None
        if wd:
            qk = [k for k in wd if QMIN <= k[1] - k[0] <= QMAX]
            k = max(qk or wd, key=lambda z: (z[1], -(z[1] - z[0])))
            wdil = (wd[k][0], k[1], wd[k][1], k)
        F["shares_wdil"] = wdil[0] if wdil else np.nan
        dei = sh_map("EntityCommonStockSharesOutstanding")
        csso = sh_map("CommonStockSharesOutstanding")
        F["shares_out"], F["shares_src"], F["shares_out_date"], F["shares_1y_ago"] = np.nan, None, pd.NaT, np.nan
        # reference count = NI / diluted EPS of the latest common quarter (robust to share-tag scaling errors in early
        # XBRL); falls back to weighted diluted shares
        self.eps_series(adj)
        epsQ = self._epsQ
        ni_pool = self.merged_dur(FLOW_SPECS["ni"])
        niQ = derive_quarters(ni_pool) if ni_pool else {}
        ref = None
        for e in sorted(set(niQ) & set(epsQ), reverse=True)[:4]:
            ev, nv = epsQ[e][1], niQ[e][1]
            if abs(ev) >= 0.05 and nv != 0 and (nv > 0) == (ev > 0):
                ref = nv / ev
                break
        F["shares_ref_ni_eps"] = ref if ref is not None else np.nan
        if ref is None and wdil is not None and wdil[0] > 0:
            ref = wdil[0]

        def plausible(v):
            return ref is None or ref <= 0 or 0.5 <= v / ref <= 2.0

        chosen = None
        if dei and anchor is not None:
            e = max(dei)
            v, f = dei[e]
            if e >= anchor - 45 and v > 0 and plausible(v):
                chosen = ("dei", v, e, f, dei)
        if chosen is None and csso and anchor is not None:
            x = self.at(csso, anchor, INST_STALE)
            if x and x[0] > 0 and plausible(x[0]):
                chosen = ("CommonStockSharesOutstanding", x[0], x[1], x[2], csso)
        if chosen is None and wdil is not None and plausible(wdil[0]):
            chosen = ("WeightedAverageDiluted", wdil[0], wdil[1], wdil[2], None)
        if chosen is not None:
            src, v, e, f, m = chosen
            F["shares_out"], F["shares_src"], F["shares_out_date"] = v, src, day2ts(e)
            used.append(f)
            if m is not None:
                y = self.near(m, e - 365, 45 if src == "dei" else 15)
            else:
                qk = {k: vf for k, vf in wd.items() if QMIN <= k[1] - k[0] <= QMAX}
                y = None
                for k, (vv, ff) in qk.items():
                    if abs(k[1] - (e - 365)) <= 20 and (y is None or abs(k[1] - (e - 365)) < abs(y[1] - (e - 365))):
                        y = (vv, k[1], ff)
            if y and v > 0 and 0.25 <= y[0] / v <= 4.0:   # outside -> likely a scale error in one of the filings
                F["shares_1y_ago"] = y[0]
                used.append(y[2])

        # ---------- EPS quarterly (split-adjusted) + SUE
        eps, q0 = self.eps_series(adj)
        vals = [x[2] for x in eps] if eps else [np.nan] * N_EPS
        for i in range(N_EPS):
            F[f"eps_q{i}"] = vals[i] if i < len(vals) else np.nan
        F["eps_q0_end"] = day2ts(q0) if q0 is not None else pd.NaT
        F["n_eps_q"] = int(np.sum(~np.isnan(np.array(vals, dtype=float)))) if eps else 0
        used += [x[3] for x in eps if x[3] is not None]
        F["sue"], F["sue_n_diff"] = np.nan, 0
        if eps:
            v = np.array(vals, dtype=float)
            diffs = np.array([v[i] - v[i + 4] for i in range(1, 9)])
            ok = ~np.isnan(diffs)
            F["sue_n_diff"] = int(ok.sum())
            if ok.sum() >= 6 and not np.isnan(v[0]) and not np.isnan(v[4]):
                sd = float(np.std(diffs[ok], ddof=1))
                if sd > 1e-9:
                    F["sue"] = (v[0] - v[4]) / sd
        self._eps_rows = eps

        # ---------- bookkeeping
        F["last_filed_date"] = day2ts(E)
        F["last_form"] = self.form_of_day.get(E)
        core_ends = [self.maxend[c] for c in self.maxend if c not in ("EntityCommonStockSharesOutstanding",)]
        F["last_period_end"] = day2ts(max(core_ends)) if core_ends else pd.NaT
        F["n_concepts_present"] = sum(1 for c, e in self.maxend.items() if e >= E - 400)
        F["no_current_assets"] = bool(np.isnan(F["assets_current"]))
        F["is_financial"] = bool(self.is_fin_sic or (
            not self.ever_current_assets and any(c in self.maxend for c in (
                "InterestIncomeExpenseNet", "PremiumsEarnedNet", "NoninterestIncome", "InterestAndDividendIncomeOperating"))))
        F["n_splits_known"] = sum(1 for c in self.splits if c["accept"] <= E)
        F["max_filed_used"] = day2ts(max(used)) if used else pd.NaT
        return F

    # ---------------- run over all filing events
    def run(self):
        states = []
        eps_states = []
        for i, E in enumerate(self.events):
            self.apply(E)
            if i % 4 == 3:
                self.prune()
            F = self.features(E)
            states.append((E, F))
            eps_states.append((E, self._eps_rows))
        return states, eps_states


# ================================================================ month-end mapping
def to_monthly(states, eps_states, month_ends, cik, ticker, strict=False, max_after_last=365):
    """Map filing-event states to month-ends. strict=False: state at last event <= t; strict=True: last event < t."""
    if not states:
        return pd.DataFrame(), pd.DataFrame()
    ev = [E for E, _ in states]
    last_ev = ev[-1]
    rows, erows = [], []
    for t in month_ends:
        td = int((t - pd.Timestamp("1970-01-01")).days)
        j = (bisect.bisect_left(ev, td) if strict else bisect.bisect_right(ev, td)) - 1
        if j < 0:
            continue
        if td - last_ev > max_after_last:
            break
        E, F = states[j]
        row = {"month_end": t, "cik": cik, "ticker": ticker}
        row.update(F)
        lpe = F.get("last_period_end")
        row["staleness_days"] = (t - lpe).days if pd.notna(lpe) else np.nan
        assert pd.isna(F["max_filed_used"]) or F["max_filed_used"] <= t, "PIT violation"
        if strict:
            assert pd.isna(F["max_filed_used"]) or F["max_filed_used"] < t, "PIT violation (strict)"
        rows.append(row)
        for (i, pe, v, f, der) in (eps_states[j][1] or []):
            if pe is None:
                continue
            erows.append((t, cik, ticker, i, day2ts(pe), v, day2ts(f), bool(der)))
    panel = pd.DataFrame(rows)
    eps = pd.DataFrame(erows, columns=["month_end", "cik", "ticker", "q", "period_end", "eps_diluted_adj", "filed",
                                       "derived"])
    return panel, eps
