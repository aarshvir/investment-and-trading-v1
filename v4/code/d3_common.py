"""d3_common.py - shared helpers for agent D3 (SEC XBRL point-in-time fundamentals).

Paths, polite HTTP sessions (SEC <= ~3.3 req/s, Wikipedia/GitHub <= 2 req/s), NYSE month-end calendar,
concept lists, JSON sidecar writer.
"""
from __future__ import annotations

import datetime as dt
import gzip
import json
import os
import threading
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

PROJECT = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments")
V4 = PROJECT / "v4"
CODE = V4 / "code"
DATA = V4 / "data"
OUT = V4 / "outputs"
LEGACY = PROJECT / "equity_project"
CACHE = Path(r"C:\Users\user\eqv4\cache\d3")
CF_DIR = CACHE / "companyfacts"      # raw companyfacts JSON, gzipped
SUB_DIR = CACHE / "submissions"      # raw submissions JSON, gzipped
FACT_SHARDS = CACHE / "facts_shards"  # per-CIK extracted long facts (parquet)
PIT_SHARDS = CACHE / "pit_shards"     # per-CIK PIT monthly features (parquet)
for _p in (CACHE, CF_DIR, SUB_DIR, FACT_SHARDS, PIT_SHARDS, DATA, OUT, CODE):
    _p.mkdir(parents=True, exist_ok=True)

SEC_UA = "PersonalEquityResearch research-admin@personal-research.org"
WEB_UA = "PersonalEquityResearch/1.0 (v4 research program; contact research-admin@personal-research.org) python-requests"

DATA_CUTOFF = pd.Timestamp("2026-09-25")
PANEL_START = pd.Timestamp("2009-06-01")


def utcnow_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------------------------
# Rate-limited HTTP
# --------------------------------------------------------------------------------------------
class RateLimiter:
    def __init__(self, min_interval: float):
        self.min_interval = min_interval
        self._lock = threading.Lock()
        self._last = 0.0

    def wait(self):
        with self._lock:
            now = time.monotonic()
            delta = now - self._last
            if delta < self.min_interval:
                time.sleep(self.min_interval - delta)
            self._last = time.monotonic()


_SEC_LIMITER = RateLimiter(0.30)   # <= 3.33 req/s (convention: max 4/s per agent)
_WEB_LIMITER = RateLimiter(0.60)   # <= ~1.7 req/s


def _session(ua: str) -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": ua, "Accept-Encoding": "gzip, deflate"})
    return s


SEC_SESSION = _session(SEC_UA)
WEB_SESSION = _session(WEB_UA)


def http_get(url: str, sec: bool = True, max_tries: int = 7, timeout: int = 90) -> requests.Response:
    """GET with rate limiting + exponential backoff on 429/5xx/network errors. Returns the final response
    (status 200 or 404); raises RuntimeError after max_tries."""
    limiter = _SEC_LIMITER if sec else _WEB_LIMITER
    sess = SEC_SESSION if sec else WEB_SESSION
    last_err = None
    for attempt in range(max_tries):
        limiter.wait()
        try:
            r = sess.get(url, timeout=timeout)
            if r.status_code in (200, 404):
                return r
            last_err = f"HTTP {r.status_code}"
            if r.status_code == 403:
                # SEC returns 403 when rate-limited / blocked: back off hard
                time.sleep(min(600, 30 * (attempt + 1)))
                continue
        except requests.RequestException as e:  # network error
            last_err = repr(e)
        time.sleep(min(120, 2 ** attempt + np.random.rand()))
    raise RuntimeError(f"GET failed after {max_tries} tries: {url} ({last_err})")


def read_gz_json(path: Path):
    with gzip.open(path, "rb") as f:
        return json.loads(f.read())


def write_gz_bytes(path: Path, content: bytes):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with gzip.open(tmp, "wb", compresslevel=6) as f:
        f.write(content)
    os.replace(tmp, path)


def write_meta(data_path: Path, meta: dict):
    """Write <name>.meta.json sidecar next to a dataset."""
    p = Path(str(data_path).rsplit(".", 1)[0] + ".meta.json")
    meta = dict(meta)
    meta.setdefault("agent", "d3")
    meta.setdefault("written_utc", utcnow_iso())
    with open(p, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, default=str)
    return p


# --------------------------------------------------------------------------------------------
# NYSE calendar (holidays 2008-2026) -> month-end = last trading day of month
# --------------------------------------------------------------------------------------------
def _easter(year: int) -> dt.date:
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return dt.date(year, month, day)


def _nth_weekday(year, month, weekday, n):
    d = dt.date(year, month, 1)
    while d.weekday() != weekday:
        d += dt.timedelta(days=1)
    return d + dt.timedelta(weeks=n - 1)


def _last_weekday(year, month, weekday):
    d = dt.date(year, month + 1, 1) - dt.timedelta(days=1) if month < 12 else dt.date(year, 12, 31)
    while d.weekday() != weekday:
        d -= dt.timedelta(days=1)
    return d


def _observed(d: dt.date) -> dt.date | None:
    if d.weekday() == 5:   # Saturday -> Friday (NYSE does not observe Sat Jan 1 on Dec 31)
        if d.month == 1 and d.day == 1:
            return None
        return d - dt.timedelta(days=1)
    if d.weekday() == 6:
        return d + dt.timedelta(days=1)
    return d


def nyse_holidays(y0=2008, y1=2027) -> set:
    hol = set()
    for y in range(y0, y1 + 1):
        for d in [dt.date(y, 1, 1), dt.date(y, 7, 4), dt.date(y, 12, 25)] + ([dt.date(y, 6, 19)] if y >= 2022 else []):
            o = _observed(d)
            if o:
                hol.add(o)
        hol.add(_nth_weekday(y, 1, 0, 3))    # MLK
        hol.add(_nth_weekday(y, 2, 0, 3))    # Presidents
        hol.add(_easter(y) - dt.timedelta(days=2))  # Good Friday
        hol.add(_last_weekday(y, 5, 0))      # Memorial
        hol.add(_nth_weekday(y, 9, 0, 1))    # Labor
        hol.add(_nth_weekday(y, 11, 3, 4))   # Thanksgiving
    # special closures
    hol |= {dt.date(2012, 10, 29), dt.date(2012, 10, 30), dt.date(2018, 12, 5), dt.date(2025, 1, 9)}
    return hol


def month_ends(start="2009-06", end="2026-09", last_override="2026-09-25") -> list[pd.Timestamp]:
    """Last NYSE trading day of each month from start..end (inclusive). The final month uses the data cutoff."""
    hol = nyse_holidays()
    out = []
    for p in pd.period_range(start, end, freq="M"):
        d = p.end_time.normalize().date()
        while d.weekday() >= 5 or d in hol:
            d -= dt.timedelta(days=1)
        out.append(pd.Timestamp(d))
    if last_override:
        out[-1] = pd.Timestamp(last_override)
    return out


# --------------------------------------------------------------------------------------------
# Concepts
# --------------------------------------------------------------------------------------------
REQUESTED_CONCEPTS = [
    # revenue family
    "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "RevenueFromContractWithCustomerIncludingAssessedTax",
    "SalesRevenueNet", "SalesRevenueGoodsNet", "SalesRevenueServicesNet", "RevenuesNetOfInterestExpense",
    "InterestAndDividendIncomeOperating", "NoninterestIncome", "InterestIncomeExpenseNet", "PremiumsEarnedNet",
    # costs / margins
    "CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold", "GrossProfit", "OperatingIncomeLoss",
    "ResearchAndDevelopmentExpense", "SellingGeneralAndAdministrativeExpense",
    # earnings
    "NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
    "IncomeTaxExpenseBenefit", "InterestExpense", "InterestExpenseNonoperating",
    # per share / shares
    "EarningsPerShareDiluted", "EarningsPerShareBasic", "WeightedAverageNumberOfDilutedSharesOutstanding",
    "WeightedAverageNumberOfSharesOutstandingBasic", "CommonStockSharesOutstanding",
    "dei:EntityCommonStockSharesOutstanding",
    # balance sheet
    "Assets", "AssetsCurrent", "Liabilities", "LiabilitiesCurrent", "StockholdersEquity",
    "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "CashAndCashEquivalentsAtCarryingValue",
    "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents", "ShortTermInvestments", "MarketableSecuritiesCurrent",
    "AvailableForSaleSecuritiesDebtSecuritiesCurrent",
    "LongTermDebt", "LongTermDebtNoncurrent", "LongTermDebtCurrent", "DebtCurrent", "ShortTermBorrowings", "CommercialPaper",
    "LongTermDebtAndCapitalLeaseObligations", "LongTermDebtAndCapitalLeaseObligationsCurrent", "Goodwill",
    "IntangibleAssetsNetExcludingGoodwill",
    # cash flow
    "NetCashProvidedByUsedInOperatingActivities", "PaymentsToAcquirePropertyPlantAndEquipment",
    "PaymentsToAcquireProductiveAssets", "DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
    "DepreciationAmortizationAndAccretionNet", "ShareBasedCompensation", "AllocatedShareBasedCompensationExpense",
    "PaymentsOfDividends", "PaymentsOfDividendsCommonStock", "PaymentsForRepurchaseOfCommonStock",
    "ProceedsFromIssuanceOfCommonStock",
]

# Extra fallback concepts (documented in the report) - used only when the requested ones are missing.
EXTRA_CONCEPTS = [
    "LiabilitiesAndStockholdersEquity",                     # liabilities fallback (L&SE - equity incl. NCI)
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
    "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
    "PaymentsForRepurchaseOfEquity",
    "RegulatedAndUnregulatedOperatingRevenue",              # utilities
    "RevenuesNetOfInterestExpense",                         # (also requested)
    "InterestExpenseDebt",
    "CashAndDueFromBanks",                                  # banks' cash line
    "MinorityInterest",
    "RevenueNotFromContractWithCustomer",                   # added to ASC-606 revenue when 'Revenues' absent
    "OperatingLeaseLeaseIncome",                            # REIT lease revenue
    "OperatingLeasesIncomeStatementLeaseRevenue",           # pre-2019 REIT lease revenue tag
    "CostsAndExpenses",                                     # revenue consistency anchor (opinc + costs = revenue)
    "EarningsPerShareBasicAndDiluted",                      # EPS fallback (loss makers / single-class filers)
    # pre-2018 industry-specific total-revenue tags (used only when no generic total-revenue tag exists)
    "HealthCareOrganizationRevenue", "OilAndGasRevenue", "RefiningAndMarketingRevenue", "FoodAndBeverageRevenue",
    "RealEstateRevenueNet", "ElectricUtilityRevenue",
]

ALL_CONCEPTS = list(dict.fromkeys(REQUESTED_CONCEPTS + EXTRA_CONCEPTS))

# forms whose facts are used in the PIT panel: periodic reports only (10-K/10-Q family incl. amendments & transition
# reports, plus annual 20-F/40-F of US-GAAP foreign filers). 8-K, S-1, proxy and 6-K facts are excluded.
PANEL_FORMS = {"10-K", "10-K/A", "10-Q", "10-Q/A", "10-KT", "10-KT/A", "10-QT", "10-QT/A", "10-K405",
               "20-F", "20-F/A", "40-F", "40-F/A"}


def cik10(cik) -> str:
    return f"{int(cik):010d}"
