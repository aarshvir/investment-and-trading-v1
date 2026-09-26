# BACKTEST AGENT: point-in-time replay of the screening model, 3 out-of-sample years
import pandas as pd, numpy as np, pickle, json, warnings
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
F=pickle.load(open('fund_all.pkl','rb')); C=pd.read_pickle('close10.pkl').ffill(); U=pd.read_pickle('s1.pkl')[['t','sector']]
sec=dict(zip(U.t,U.sector))
def row(d,names):
    if d is None: return None
    for n in names:
        if n in d.index: return d.loc[n]
    return None
def at(s,cut):  # latest annual value with period end <= cut, and the prior one
    if s is None: return (np.nan,np.nan)
    s=s.dropna(); s=s[[c for c in s.index if c<=cut]].sort_index(ascending=False)
    return (float(s.iloc[0]) if len(s) else np.nan, float(s.iloc[1]) if len(s)>1 else np.nan)
spx=C['^GSPC']
import sys
WTS=eval(sys.argv[1]); res={}; allrows=[]
for yr in [2023,2024,2025]:
    t0=pd.Timestamp(f'{yr}-09-29'); t1=pd.Timestamp(f'{yr+1}-09-24') if yr==2025 else pd.Timestamp(f'{yr+1}-09-27')
    i0=C.index[C.index<=t0][-1]; i1=C.index[C.index<=t1][-1]; cut=t0-pd.Timedelta(days=90)
    rows=[]
    for t,o in F.items():
        if t not in C or C[t].loc[:i0].dropna().shape[0]<300 or np.isnan(C[t].loc[i1]): continue
        I,B,CF=o['inc'],o['bs'],o['cf']
        rev=at(row(I,['Total Revenue','Operating Revenue']),cut); ni=at(row(I,['Net Income Common Stockholders','Net Income']),cut)
        opi=at(row(I,['Operating Income','EBIT']),cut); gp=at(row(I,['Gross Profit']),cut); eb=at(row(I,['EBITDA','Normalized EBITDA']),cut)
        sh=at(row(I,['Diluted Average Shares','Basic Average Shares']),cut); eq=at(row(B,['Stockholders Equity','Common Stock Equity']),cut)
        debt=at(row(B,['Total Debt']),cut); cash=at(row(B,['Cash Cash Equivalents And Short Term Investments','Cash And Cash Equivalents']),cut)
        ocf=at(row(CF,['Operating Cash Flow']),cut); cx=at(row(CF,['Capital Expenditure']),cut)
        eps=at(row(I,['Diluted EPS','Basic EPS']),cut)
        if np.isnan(rev[0]) or np.isnan(sh[0]): continue
        c=C[t].loc[:i0].dropna(); p=float(c.iloc[-1]); mc=p*sh[0]; r=c.pct_change().iloc[-252:]
        sma50,sma150,sma200=c.rolling(50).mean().iloc[-1],c.rolling(150).mean().iloc[-1],c.rolling(200).mean().iloc[-1]
        hi,lo=c.iloc[-252:].max(),c.iloc[-252:].min()
        fcf=ocf[0]+(cx[0] if cx[0]==cx[0] else 0)
        al=pd.concat([r,spx.loc[:i0].pct_change().iloc[-252:]],axis=1).dropna()
        rows.append(dict(t=t,sector=sec.get(t),roe=ni[0]/eq[0] if eq[0] and eq[0]>0 else np.nan,om=opi[0]/rev[0],gm=gp[0]/rev[0] if gp[0]==gp[0] else np.nan,
          fcfm=fcf/rev[0],nde=((debt[0] if debt[0]==debt[0] else 0)-(cash[0] if cash[0]==cash[0] else 0))/eb[0] if eb[0] and eb[0]>0 else np.nan,
          revg=rev[0]/rev[1]-1 if rev[1] and rev[1]>0 else np.nan, epsg=eps[0]/eps[1]-1 if eps[1] and eps[1]>0 else np.nan,
          ey=ni[0]/mc, fcfy=fcf/mc, sy=rev[0]/mc, ret12=p/c.iloc[-252]-1, ret6=p/c.iloc[-126]-1,
          tt=int(p>sma50)+int(sma50>sma150)+int(sma150>sma200)+int(p>sma200)+int(p/hi-1>-.25)+int(p/lo-1>.3),
          vol=r.std()*np.sqrt(252), mdd=(c.iloc[-756:]/c.iloc[-756:].cummax()-1).min(),
          beta=np.cov(al.iloc[:,0],al.iloc[:,1])[0,1]/al.iloc[:,1].var(),
          veto=(ni[0]<=0) or (fcf<0 and sec.get(t) not in('Financials','Real Estate')) or ((c.iloc[-756:]/c.iloc[-756:].cummax()-1).min()<-0.6),
          fwd=float(C[t].loc[i1]/p-1)))
    d=pd.DataFrame(rows)
    def pr(col,asc=True,bys=False,clip=None):
        s=d[col].astype(float); s=s.clip(*clip) if clip else s; s=s.fillna(s.median())
        return s.groupby(d.sector).rank(pct=True,ascending=asc) if bys else s.rank(pct=True,ascending=asc)
    d['Q']=(pr('roe',True,True,(-1,1.5))+pr('om',True,True)+pr('fcfm',True,True,(-1,1))+pr('gm',True,True)+pr('nde',False,False,(-5,10)))/5
    d['G']=(pr('revg',clip=(-.5,1.5))+pr('epsg',clip=(-1,2)))/2
    d['V']=(pr('ey',True,True,(-.5,.5))+pr('fcfy',True,True,(-.3,.3))+pr('sy',True,True))/3
    d['M']=(d.tt/6+pr('ret6')+pr('ret12',clip=(-1,3)))/3
    d['R']=(pr('vol',False)+pr('mdd')+pr('beta',False))/3
    W=WTS
    d['score']=sum(W[k]*d[k] for k in W)
    e=d[~d.veto]
    q=e.score.rank(pct=True)
    top10=e.nlargest(10,'score'); top30=e.nlargest(30,'score'); topq=e[q>=0.8]; botq=e[q<=0.2]
    ic=spearmanr(e.score,e.fwd).correlation
    pic={k:spearmanr(e[k],e.fwd).correlation for k in ['Q','G','V','M','R']}
    res[yr]=dict(n=len(d),n_elig=len(e),spx=float(spx.loc[i1]/spx.loc[i0]-1),ew=float(d.fwd.mean()),elig_ew=float(e.fwd.mean()),
       top10=float(top10.fwd.mean()),top30=float(top30.fwd.mean()),topq=float(topq.fwd.mean()),botq=float(botq.fwd.mean()),vetoed=float(d[d.veto].fwd.mean()),
       ic=float(ic),pillar_ic=pic,top10_names=top10.t.tolist(),hit15_top30=float((top30.fwd>=0.15).mean()),hit15_all=float((e.fwd>=0.15).mean()),
       top30_vol=float(top30.vol.mean()),all_vol=float(e.vol.mean()))
json.dump(res,open(sys.argv[2],'w'),default=float)
for y,v in res.items():
    print(y,'n',v['n'],'SPX %.1f%% EW %.1f%% | top10 %.1f%% top30 %.1f%% topQ %.1f%% botQ %.1f%% vetoed %.1f%% | IC %.3f | hit15 top30 %.0f%% vs all %.0f%%'%(100*v['spx'],100*v['ew'],100*v['top10'],100*v['top30'],100*v['topq'],100*v['botq'],100*v['vetoed'],v['ic'],100*v['hit15_top30'],100*v['hit15_all']))
    print('   pillar IC',{k:round(x,3) for k,x in v['pillar_ic'].items()})
