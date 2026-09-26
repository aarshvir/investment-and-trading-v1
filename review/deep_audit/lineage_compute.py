"""Read-only replication of source lineage and missing-data treatment."""
import collections, datetime, hashlib, json, pathlib, pickle, re, sys
import numpy as np
import pandas as pd

ROOT=pathlib.Path(__file__).resolve().parents[2]
P=ROOT/'source_bundle/equity_project'
O=ROOT/'review/deep_audit'
O.mkdir(exist_ok=True)
def load(n): return pickle.load(open(P/n,'rb'))
U=pd.read_csv(P/'universe.csv'); X=load('conv.pkl'); F=load('fund_all.pkl'); E=load('edgar.pkl')
ER=json.loads((P/'edgar_read.json').read_text()); prices=load('close10.pkl'); short=load('close.pkl')
finalists=[r['ticker'] for r in json.loads((ROOT/'review/agents/02_market_data.json').read_text())['rows']]
def norm(x):
    if isinstance(x,(np.integer,)): return int(x)
    if isinstance(x,(np.floating,)): return None if np.isnan(x) else float(x)
    if isinstance(x,(np.bool_,)): return bool(x)
    if isinstance(x,(pd.Timestamp,datetime.datetime)): return x.isoformat()
    return str(x)
docs=[(t,d) for t,dd in E.items() for d in (dd or [])]
docledger=[]
for t,d in docs:
    tx=d['text']; m=re.search(r'/data/(\d+)/(\d+)/(.*)',d['url'])
    docledger.append(dict(ticker=t,filing_date=d['date'],url=d['url'],cik=m.group(1) if m else None,accession_compact=m.group(2) if m else None,document=m.group(3) if m else None,characters=len(tx),text_sha256=hashlib.sha256(tx.encode()).hexdigest(),truncated_at60000=len(tx)==60000,scoring_ignores_after15000=len(tx)>15000,flagging_ignores_after40000=len(tx)>40000,acceptance_timestamp_present='acceptanceDateTime' in d,raw_html_preserved=False))
pd.DataFrame(docledger).to_csv(O/'03_document_ledger.csv',index=False)
coverage=[]
for _,r in X.iterrows():
    t=r.t; dd=E.get(t) or []; cf=F.get(t,{}).get('cf')
    coverage.append(dict(ticker=t,is_finalist=t in finalists,release_count=len(dd),first_cached_release=min((d['date'] for d in dd),default=None),last_cached_release=max((d['date'] for d in dd),default=None),annual_statement_count=len(F.get(t,{}).get('inc',pd.DataFrame()).columns),source_acceptance_timestamp=False,filing_version_vintage=False,missing_release_data=t not in ER,management_lens=bool(r['L_Management & red flags']),cuts4=None if pd.isna(r.cuts4) else float(r.cuts4),stab=float(r.stab)))
pd.DataFrame(coverage).to_csv(O/'03_company_coverage_497.csv',index=False)
pricesummary={}; gaps=[]
for name,c in [('close10',prices),('close3',short)]:
    for t in c:
        s=c[t]; first=s.first_valid_index(); last=s.last_valid_index()
        inner=s.loc[first:last] if first is not None else s
        gaps.append(dict(dataset=name,ticker=t,first=str(first.date()) if first is not None else None,last=str(last.date()) if last is not None else None,leading_missing=int(s.index.get_loc(first)) if first is not None else len(s),internal_missing=int(inner.isna().sum()),trailing_missing=int(len(s)-s.index.get_loc(last)-1) if last is not None else len(s),filled_by_ffill=int((s.isna() & s.ffill().notna()).sum()),observations=int(s.notna().sum())))
    pricesummary[name]=dict(rows=len(c),columns=len(c.columns),first=str(c.index.min().date()),last=str(c.index.max().date()),duplicate_dates=int(c.index.duplicated().sum()),missing_cells=int(c.isna().sum().sum()),ffill_new_cells=int((c.isna() & c.ffill().notna()).sum().sum()),nonpositive_cells=int((c<=0).sum().sum()),columns_with_missing=int(c.isna().any().sum()))
pd.DataFrame(gaps).to_csv(O/'03_price_gaps.csv',index=False)
def row(df,names):
    if df is None:return None
    for n in names:
        if n in df.index:return df.loc[n]
    return None
annual=[]
for year in [2023,2024,2025]:
    cut=pd.Timestamp(f'{year}-09-29')-pd.Timedelta(days=90)
    for t,o in F.items():
        s=row(o.get('inc'),['Total Revenue','Operating Revenue'])
        if s is None: continue
        ss=s.dropna(); available=ss[[d<=cut for d in ss.index]].sort_index(ascending=False)
        annual.append(dict(rebalance_year=year,ticker=t,assumed_period_cutoff=str(cut.date()),selected_fiscal_end=str(available.index[0].date()) if len(available) else None,available_annual_periods=len(available),filing_publication_proven=False,original_vintage_preserved=False))
pd.DataFrame(annual).to_csv(O/'03_backtest_period_availability.csv',index=False)
corp=[]
for t,day,ratio,url in [('NVDA','2024-06-10',10,'https://investor.nvidia.com/files/doc_downloads/2024/06/nvidia-2024-stock-split_faq_investors.pdf'),('IBKR','2025-06-18',4,'https://www.sec.gov/Archives/edgar/data/1381197/000138119725000103/ibkr-20250630x10q.htm'),('CPAY','2024-03-25',1,'https://investor.corpay.com/news-releases/news-release-details/fleetcor-announces-rebranding-corpay')]:
    s=prices[t].dropna(); a=s.loc[:pd.Timestamp(day)]; curr=a.iloc[-1]; prev=a.iloc[-2]
    corp.append(dict(ticker=t,event_date=day,split_ratio=ratio,cached_previous_adjusted_close=float(prev),cached_event_adjusted_close=float(curr),cached_event_return=float(curr/prev-1),primary_event_source=url,corporate_action_ledger_present=False,status='Price continuity checked; full action reconciliation unverified'))
no_edgar=[r for r in coverage if r['missing_release_data']]
summary=dict(as_of='2026-09-26',source_snapshot='2026-09-24 US close',universe_csv_rows=len(U),scored_companies=len(X),omitted_tickers=sorted(set(U.t)-set(X.t)),finalists=len(finalists),edgar_companies=len([dd for dd in E.values() if dd]),edgar_release_documents=len(docs),edgar_companies_no_documents=len(no_edgar),missing_edgar_management_lens_pass_count=sum(r['management_lens'] for r in no_edgar),cached_document_min_date=min(d['date'] for _,d in docs),cached_document_max_date=max(d['date'] for _,d in docs),documents_truncated60000=sum(r['truncated_at60000'] for r in docledger),documents_scoring_limited15000=sum(r['scoring_ignores_after15000'] for r in docledger),documents_flagging_limited40000=sum(r['flagging_ignores_after40000'] for r in docledger),documents_with_acceptance_timestamp=sum(r['acceptance_timestamp_present'] for r in docledger),full_original_filing_vintage_verified_companies=0,historical_membership_interval_rows=0,delisting_return_records=0,explicit_corporate_action_records=0,price_datasets=pricesummary,corporate_action_examples=corp,finalist_coverage=[r for r in coverage if r['is_finalist']],backtest_period_counts={str(y):dict(companies_with_revenue=sum(r['available_annual_periods']>0 for r in annual if r['rebalance_year']==y),companies_with_two_years=sum(r['available_annual_periods']>=2 for r in annual if r['rebalance_year']==y)) for y in [2023,2024,2025]})
mask=prices.isna() & prices.ffill().notna()
summary['forwardfill_by_date']={str(d.date()):int(n) for d,n in mask.sum(axis=1).items() if n}
bt=load('bt_frames.pkl')
summary['saved_backtest_growth_coverage']={str(y):dict(rows=len(b),valid_revenue_growth=int(b.revg.notna().sum()),valid_eps_growth=int(b.epsg.notna().sum()),distinct_growth_scores=int(b.G.nunique()),distinct_revenue_growth=int(b.revg.nunique())) for y,b in bt.groupby('yr')}
summary['annual_periods_2023_with_two_years']=[r for r in annual if r['rebalance_year']==2023 and r['available_annual_periods']>=2]
gapdate=pd.Timestamp('2026-09-22'); gaprows=[]
for t in X.t:
    a=prices[t]; b=short[t]; af=a.ffill(); ar=af.pct_change(fill_method=None).iloc[-252:]
    # Delete all return intervals touching the outage for sensitivity only; this is not a repair.
    valid=a.notna() & a.shift().notna(); clean=ar[valid.reindex(ar.index,fill_value=False)]
    gaprows.append(dict(ticker=t,is_finalist=t in finalists,close10_sep22=None if pd.isna(a.loc[gapdate]) else float(a.loc[gapdate]),close3_sep22=None if pd.isna(b.loc[gapdate]) else float(b.loc[gapdate]),close10_missing_sep22=bool(pd.isna(a.loc[gapdate])),close3_missing_sep22=bool(pd.isna(b.loc[gapdate])),filled_sep22_return=float(af.pct_change(fill_method=None).loc[gapdate]),filled_sep23_return=float(af.pct_change(fill_method=None).loc[gapdate+pd.Timedelta(days=1)]),vol252_original_ffill=float(ar.std()*np.sqrt(252)),vol252_exclude_gap_intervals_sensitivity=float(clean.std()*np.sqrt(252)),source_date='2026-09-24',repair_status='UNREPAIRED: no independently corroborated Sep22 close'))
pd.DataFrame(gaprows).to_csv(O/'03_sep22_outage_497.csv',index=False)
summary['sep22_outage']=dict(scored_missing_close10=sum(r['close10_missing_sep22'] for r in gaprows),scored_missing_close3=sum(r['close3_missing_sep22'] for r in gaprows),recoverable_from_close3=sum(r['close10_missing_sep22'] and not r['close3_missing_sep22'] for r in gaprows),finalists_missing_close10=sum(r['is_finalist'] and r['close10_missing_sep22'] for r in gaprows),finalists_missing_close3=sum(r['is_finalist'] and r['close3_missing_sep22'] for r in gaprows),finalist_rows=[r for r in gaprows if r['is_finalist']],max_abs_vol_sensitivity=max(abs(r['vol252_original_ffill']-r['vol252_exclude_gap_intervals_sensitivity']) for r in gaprows))
summary['artifact_scope']='This JSON describes preserved original input defects. Later externally corroborated repairs are in the separate linked repair impact; original rows are never overwritten.'
summary['repair_impact_file']='03_finalist_repair_impact.json'
summary['druckenmiller_readiness_file']='reports/03_druckenmiller_readiness.json'
(O/'03_lineage.json').write_text(json.dumps(summary,indent=2,default=norm),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='finalist_coverage'},indent=2,default=norm))
