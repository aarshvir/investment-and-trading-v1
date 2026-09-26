# STAGE 1: Screening Committee — 7 specialist agents + red team + refutation rounds. 503 -> 100
import pandas as pd, numpy as np, json, warnings
warnings.filterwarnings('ignore')
U=pd.read_csv('universe.csv'); I=json.load(open('info.json'))
C=pd.read_pickle('close.pkl').ffill(); spx=C['^GSPC'].dropna()
rows=[]
for _,u in U.iterrows():
    s=u.t; i=I.get(s,{}); 
    if s not in C or C[s].dropna().shape[0]<300: continue
    c=C[s].dropna(); r=c.pct_change().dropna(); r1=r.iloc[-252:]
    sma50,sma150,sma200=c.rolling(50).mean(),c.rolling(150).mean(),c.rolling(200).mean()
    hi52,lo52=c.iloc[-252:].max(),c.iloc[-252:].min(); p=float(c.iloc[-1])
    al=pd.concat([r1,spx.pct_change().iloc[-252:]],axis=1).dropna()
    roll=(c/c.shift(252)-1).dropna()
    mc=i.get('marketCap') or np.nan; fcf=i.get('freeCashflow'); ni=i.get('netIncomeToCommon'); rev=i.get('totalRevenue')
    ebitda=i.get('ebitda'); debt=i.get('totalDebt') or 0
    rows.append(dict(t=s,name=u['name'],sector=u.sector,sub=u['sub'],price=p,mcap=mc/1e9 if mc==mc else np.nan,
     fpe=i.get('forwardPE'),tpe=i.get('trailingPE'),evebitda=i.get('enterpriseToEbitda'),pb=i.get('priceToBook'),ps=i.get('priceToSalesTrailing12Months'),
     fcfy=(fcf/mc) if (fcf and mc==mc and mc>0) else np.nan, divy=i.get('dividendYield'),payout=i.get('payoutRatio'),
     roe=i.get('returnOnEquity'),roa=i.get('returnOnAssets'),gm=i.get('grossMargins'),om=i.get('operatingMargins'),pm=i.get('profitMargins'),
     fcfm=(fcf/rev) if (fcf and rev) else np.nan, de=i.get('debtToEquity'), cr=i.get('currentRatio'),
     nd_ebitda=((debt-(i.get('totalCash') or 0))/ebitda) if ebitda and ebitda>0 else np.nan,
     cash_conv=(fcf/ni) if (fcf and ni and ni>0) else np.nan, ocf_conv=((i.get('operatingCashflow') or np.nan)/ni) if (ni and ni>0) else np.nan,
     revg=i.get('revenueGrowth'),epsg=i.get('earningsGrowth'),
     fwd_epsg=(i['forwardEps']/i['trailingEps']-1) if i.get('forwardEps') and i.get('trailingEps') and i['trailingEps']>0 else np.nan,
     rec=i.get('recommendationMean'),nan=i.get('numberOfAnalystOpinions'),tgt=i.get('targetMeanPrice'),tgt_hi=i.get('targetHighPrice'),tgt_lo=i.get('targetLowPrice'),
     short=i.get('shortPercentOfFloat'),insider=i.get('heldPercentInsiders'),inst=i.get('heldPercentInstitutions'),
     vol=float(r1.std()*np.sqrt(252)),dvol=float(r1[r1<0].std()*np.sqrt(252)),
     beta=float(np.cov(al.iloc[:,0],al.iloc[:,1])[0,1]/al.iloc[:,1].var()),
     mdd3y=float((c/c.cummax()-1).min()),worst12m=float(roll.min()),
     ret12=float(p/c.iloc[-252]-1),ret6=float(p/c.iloc[-126]-1),ret3=float(p/c.iloc[-63]-1),ret1m=float(p/c.iloc[-21]-1),
     rs6=float((p/c.iloc[-126])/(spx.iloc[-1]/spx.iloc[-126])-1),
     off_hi=p/hi52-1,above_lo=p/lo52-1,
     tt=int(p>sma50.iloc[-1])+int(sma50.iloc[-1]>sma150.iloc[-1])+int(sma150.iloc[-1]>sma200.iloc[-1])+int(sma200.iloc[-1]>sma200.iloc[-22])+int(p>sma200.iloc[-1])+int(p/hi52-1>-0.25)+int(p/lo52-1>0.30),
     summary=(i.get('longBusinessSummary') or '')[:900], website=i.get('website'),employees=i.get('fullTimeEmployees'),
     tgt_disp=((i.get('targetHighPrice') or np.nan)-(i.get('targetLowPrice') or np.nan))/p))
df=pd.DataFrame(rows); df=df[~df.t.isin(['GOOG','FOX','NWS'])].reset_index(drop=True); df['upside']=df.tgt/df.price-1
# percentile helpers: sector-relative for valuation & quality (Pb/PE norms differ by sector), absolute for risk & momentum
def pr(col,asc=True,by_sector=False,clip=None):
    s=df[col].astype(float)
    if clip: s=s.clip(*clip)
    s=s.fillna(s.median())
    return (s.groupby(df.sector).rank(pct=True,ascending=asc) if by_sector else s.rank(pct=True,ascending=asc))
pos=lambda col: df[col].where(df[col]>0)
df['fpe_p']=pos('fpe'); df['eve_p']=pos('evebitda')
A={}
A['Quality']=(pr('roe',clip=(-1,1.5),by_sector=True)+pr('om',by_sector=True)+pr('fcfm',clip=(-1,1),by_sector=True)+pr('gm',by_sector=True)+pr('cash_conv',clip=(-1,3))+pr('nd_ebitda',False,clip=(-5,10)))/6
A['Growth']=(pr('revg',clip=(-.5,1.5))+pr('epsg',clip=(-1,2))+pr('fwd_epsg',clip=(-.5,1)))/3
A['Valuation']=(pr('fpe_p',False,True)+pr('eve_p',False,True)+pr('fcfy',True,True,(-.2,.2))+pr('upside',clip=(-.5,1)))/4
A['Momentum']=(df.tt/7+pr('rs6')+pr('ret12',clip=(-1,3))+pr('off_hi'))/4
A['Risk']=(pr('vol',False)+pr('dvol',False)+pr('mdd3y')+pr('worst12m')+pr('beta',False))/5
A['Street']=(pr('rec',False)+pr('upside',clip=(-.5,1))+pr('short',False)+pr('nan'))/4
for k,v in A.items(): df['A_'+k]=v
W={'Quality':.22,'Growth':.16,'Valuation':.18,'Momentum':.12,'Risk':.20,'Street':.12}
df['raw']=100*sum(W[k]*df['A_'+k] for k in W)
# Red-team agent: hard vetoes and soft flags
flags={}; veto={}; capex_note=[]
for i_,r in df.iterrows():
    f=[];v=[]
    if r.fpe!=r.fpe or r.fpe<=0: v.append('No forward profit')
    if r.sector not in('Financials','Real Estate') and r.fcfy==r.fcfy and r.fcfy<0: v.append('Burning cash (negative FCF)')
    if r.mdd3y<-0.60: v.append('Fell >60% in 3 yrs')
    if r.sector not in('Financials','Real Estate','Utilities') and r.nd_ebitda==r.nd_ebitda and r.nd_ebitda>4: f.append('High leverage (net debt >4x EBITDA)')
    if r.cash_conv==r.cash_conv and r.cash_conv<0.5 and r.sector not in('Financials','Real Estate'):
        if r.ocf_conv==r.ocf_conv and r.ocf_conv>=0.9: capex_note.append(r.t)
        else: f.append('Weak cash conversion (<50% of profit)')
    if r.payout==r.payout and r.payout>1.0 and r.sector!='Real Estate': f.append('Pays out >100% of earnings')
    if r.short==r.short and r.short>0.08: f.append('High short interest')
    if r.revg==r.revg and r.revg<0: f.append('Shrinking revenue')
    if r.epsg==r.epsg and r.epsg>2 and r.fpe==r.fpe and r.fpe<12: f.append('Possible cyclical peak earnings')
    flags[r.t]=f; veto[r.t]=v
df['flags']=df.t.map(flags); df['veto']=df.t.map(veto)
# Refutation rounds between agents (logged)
debate=[]; adj=np.zeros(len(df))
for i_,r in df.iterrows():
    notes=[]
    if r.A_Valuation>0.75 and r.A_Momentum<0.30:
        if r.A_Quality<0.5: notes.append(('Momentum refutes Valuation','Cheap but falling and mediocre quality: value trap. Penalty -6.',-6))
        else: notes.append(('Quality defends Valuation','Cheap and falling, but high quality: possible genuine dip. Kept, no penalty.',0))
    if r.A_Momentum>0.80 and r.A_Valuation<0.25:
        if r.A_Growth<0.70: notes.append(('Valuation refutes Momentum','Expensive rally not backed by growth: bubble risk. Penalty -6.',-6))
        else: notes.append(('Growth defends Momentum','Expensive but growth is top-30%: premium earned. No penalty.',0))
    if r.A_Growth>0.80 and (r.fcfy==r.fcfy and r.fcfy<0.01) and r.sector not in('Financials','Real Estate'):
        notes.append(('Quality refutes Growth','Fast growth with <1% FCF yield: growth not yet converting to cash. Penalty -3.',-3))
    if r.A_Street>0.80 and r.A_Risk<0.25: notes.append(('Risk refutes Street','Analysts love it but price swings are extreme. Penalty -4.',-4))
    if r.A_Quality>0.80 and r.A_Risk>0.70 and r.A_Valuation>0.45: notes.append(('Buffett lens endorses','Wonderful business, calm stock, fair price. Bonus +4.',4))
    if r.t in capex_note: notes.append(('Capital-allocation agent overrules red team','Low free cash flow is heavy growth capex, not weak earnings: operating cash flow covers >=90% of profit. Cash-conversion flag withdrawn.',0))
    for k in r['flags']: notes.append(('Red team flag',k+'. Penalty -2.',-2))
    adj[i_]=sum(n[2] for n in notes); debate.append(notes)
df['debate']=debate; df['adj']=adj; df['s1']=df.raw+df.adj
df['vetoed']=df.veto.map(len)>0
df=df.sort_values('s1',ascending=False).reset_index(drop=True); df['rank500']=df.index+1
# shortlist 100 with sector cap 22
sl=[];cnt={}
for _,r in df[~df.vetoed].iterrows():
    if cnt.get(r.sector,0)>=22: continue
    sl.append(r.t); cnt[r.sector]=cnt.get(r.sector,0)+1
    if len(sl)==100: break
df['short100']=df.t.isin(sl)
df.to_pickle('s1.pkl')
print('universe',len(df),'vetoed',df.vetoed.sum(),'debates',sum(len(d)>0 for d in df.debate))
print(pd.Series(cnt).sort_values(ascending=False).to_string())
print(df[df.short100][['rank500','t','sector','s1','A_Quality','A_Growth','A_Valuation','A_Momentum','A_Risk']].head(25).round(2).to_string())
