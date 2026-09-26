"""Lead: PRELIMINARY live ranking (triage only) so diligence can start before B1 finishes.
Uses the pre-registered Q/V/M families from STATE.md with SEC XBRL facts (TTM = FY + YTD_cur - YTD_prior),
Yahoo market caps (D4) and total-return momentum (D2). S (SUE) is omitted here. The OFFICIAL ranking is B1's
point-in-time live score; this file only decides which dossiers to start first."""
import pandas as pd, numpy as np, pathlib
V4 = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4')
F = pd.read_parquet(V4 / 'data' / 'd3_xbrl_facts.parquet')
S = pd.read_parquet(V4 / 'data' / 'd4_live_snapshot.parquet')
U = pd.read_csv(V4 / 'data' / 'd4_universe.csv')
F['start'] = pd.to_datetime(F['start'], errors='coerce'); F['end'] = pd.to_datetime(F['end'], errors='coerce'); F['filed'] = pd.to_datetime(F['filed'], errors='coerce')
F = F[F.filed <= '2026-09-25']
F['dur'] = (F['end'] - F['start']).dt.days

FLOW = {'rev': ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'RevenueFromContractWithCustomerIncludingAssessedTax', 'SalesRevenueNet', 'RevenuesNetOfInterestExpense'],
        'cogs': ['CostOfRevenue', 'CostOfGoodsAndServicesSold', 'CostOfGoodsSold'], 'gp': ['GrossProfit'], 'opinc': ['OperatingIncomeLoss'],
        'ni': ['NetIncomeLoss', 'NetIncomeLossAvailableToCommonStockholdersBasic', 'ProfitLoss'], 'ocf': ['NetCashProvidedByUsedInOperatingActivities'],
        'capex': ['PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets']}
INST = {'assets': ['Assets'], 'equity': ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
        'debt_lt': ['LongTermDebt', 'LongTermDebtNoncurrent', 'LongTermDebtAndCapitalLeaseObligations'], 'debt_st': ['DebtCurrent', 'LongTermDebtCurrent', 'ShortTermBorrowings', 'CommercialPaper'],
        'cash': ['CashAndCashEquivalentsAtCarryingValue', 'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'], 'sti': ['ShortTermInvestments', 'MarketableSecuritiesCurrent']}


def ttm(g):
    """g: facts of one concept for one company (USD). Returns TTM using latest FY + YTD_cur - YTD_prior."""
    g = g.sort_values('filed').drop_duplicates(['start', 'end'], keep='last')
    fy = g[(g.dur >= 350) & (g.dur <= 380)]
    if fy.empty: return np.nan
    fyr = fy.loc[fy.end.idxmax()]; val = fyr.val
    ytd = g[(g.end > fyr.end) & (g.dur >= 80) & (g.dur < 350) & (g.start > fyr.end - pd.Timedelta(days=15))]
    if not ytd.empty:
        cur = ytd.loc[ytd.end.idxmax()]
        prior = g[(abs((g.end - (cur.end - pd.DateOffset(years=1))).dt.days) <= 10) & (abs(g.dur - cur.dur) <= 10)]
        if not prior.empty: val = val + cur.val - prior.iloc[-1].val
    return val


def latest_inst(g):
    g = g.sort_values(['end', 'filed']); return g.iloc[-1].val if len(g) else np.nan


rows = []
Fu = F[F.unit == 'USD']
for cik, gc in Fu.groupby('cik'):
    r = {'cik': cik}
    for k, cs in FLOW.items():
        v = np.nan
        for c in cs:
            g = gc[gc.concept == c]
            if len(g): v = ttm(g)
            if v == v: break
        r[k] = v
    for k, cs in INST.items():
        v = np.nan
        for c in cs:
            g = gc[gc.concept == c]
            if len(g): v = latest_inst(g)
            if v == v: break
        r[k] = v
    a = gc[gc.concept == 'Assets'].sort_values('end')
    if len(a) >= 2:
        last = a.iloc[-1]; prev = a[abs((a.end - (last.end - pd.DateOffset(years=1))).dt.days) <= 20]
        r['assets_1y'] = prev.iloc[-1].val if len(prev) else np.nan
    rows.append(r)
X = pd.DataFrame(rows)
X['gp'] = X.gp.fillna(X.rev - X.cogs)
cikcol = 'cik' if 'cik' in U.columns else [c for c in U.columns if 'cik' in c.lower()][0]
tkcol = 'ticker' if 'ticker' in U.columns else U.columns[0]
U['cik_i'] = pd.to_numeric(U[cikcol], errors='coerce')
X['cik_i'] = pd.to_numeric(X.cik, errors='coerce')
secol = [c for c in U.columns if 'sector' in c.lower()][0]
subcol = [c for c in U.columns if 'sub' in c.lower()][0]
M = U[[tkcol, 'cik_i', secol, subcol]].rename(columns={tkcol: 'ticker', secol: 'sector', subcol: 'sub'}).merge(X, on='cik_i', how='left')
S2 = S.set_index('ticker') if 'ticker' in S.columns else S
M['mcap'] = M.ticker.map(S2['marketCap']); M['pe_ntm'] = M.ticker.map(S2['pe_ntm']) if 'pe_ntm' in S2 else np.nan
P = pd.read_parquet(V4 / 'data' / 'd2_adjclose.parquet')
P = P.loc[:'2026-09-25']
me = P.resample('ME').last()
last = P.iloc[-1]; m1 = me.iloc[-2]; m12 = me.iloc[-13]
mom = (m1 / m12 - 1)  # 12-1: price at end of Aug-2026 vs end of Aug-2025
M['mom121'] = M.ticker.map(mom)
dr = P.pct_change().iloc[-252:]; M['vol'] = M.ticker.map(dr.std() * np.sqrt(252))
fin = M.sector.isin(['Financials', 'Real Estate'])
M['gpa'] = np.where(fin, np.nan, M.gp / M.assets); M['roe'] = np.where(M.equity > 0, M.ni / M.equity, np.nan)
M['cfoa'] = M.ocf / M.assets; M['accr'] = np.where(fin, np.nan, (M.ni - M.ocf) / M.assets)
M['debt'] = M.debt_lt.fillna(0) + M.debt_st.fillna(0); M['lev'] = np.where(fin, np.nan, M.debt / M.assets)
M['agr'] = M.assets / M.assets_1y - 1
M['ep'] = M.ni / M.mcap; M['fcfp'] = (M.ocf - M.capex.fillna(0)) / M.mcap
M['ebitev'] = np.where(fin, np.nan, M.opinc / (M.mcap + M.debt - M.cash.fillna(0) - M.sti.fillna(0))); M['bp'] = M.equity / M.mcap


def pr(col, asc=True):
    return M.groupby('sector')[col].rank(pct=True, ascending=asc)


fam = {'Q': [pr('gpa'), pr('roe'), pr('cfoa'), pr('accr', False), pr('lev', False), pr('agr', False)],
       'V': [pr('ep'), pr('fcfp'), pr('ebitev'), pr('bp')], 'M': [pr('mom121')]}
for k, lst in fam.items():
    D = pd.concat(lst, axis=1); ok = D.notna().sum(axis=1) >= max(1, len(lst) // 2)
    M[k] = D.mean(axis=1).where(ok).rank(pct=True)
M['prelim'] = M[['Q', 'V', 'M']].mean(axis=1)
M = M.sort_values('prelim', ascending=False)
M.to_csv(V4 / 'outputs' / 'lead_prelim_rank.csv', index=False)
cols = ['ticker', 'sector', 'sub', 'prelim', 'Q', 'V', 'M', 'mom121', 'vol', 'pe_ntm']
print(M[cols].head(60).round(3).to_string())
print('coverage: prelim non-null', M.prelim.notna().sum(), 'of', len(M))
