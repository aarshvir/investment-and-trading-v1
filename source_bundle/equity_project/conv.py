# CONVICTION ENGINE: 10 independent lens-agents vote on all 497; 500-run threshold-perturbation audit; target-independent
import pandas as pd, numpy as np, pickle, json, warnings
warnings.filterwarnings('ignore')
X=pd.read_pickle('v3.pkl'); F=pickle.load(open('fund_all.pkl','rb')); ER=json.load(open('edgar_read.json'))
def row(d,ns):
    if d is None: return None
    for n in ns:
        if n in d.index: return d.loc[n].astype(float)
    return None
B=[]
for t in X.t:
    o=F.get(t,{}); I,BS,CF=o.get('inc'),o.get('bs'),o.get('cf')
    rev=row(I,['Total Revenue','Operating Revenue']); ni=row(I,['Net Income Common Stockholders','Net Income']); opi=row(I,['Operating Income','EBIT'])
    eq=row(BS,['Stockholders Equity','Common Stock Equity']); ocf=row(CF,['Operating Cash Flow']); cx=row(CF,['Capital Expenditure']); sh=row(I,['Diluted Average Shares','Basic Average Shares'])
    def s(x): return x.dropna().sort_index(ascending=False).iloc[:4] if x is not None else pd.Series(dtype=float)
    rv,nn,op,e_,oc,c_,shs=map(s,[rev,ni,opi,eq,ocf,cx,sh])
    roe=(nn/e_.reindex(nn.index)).dropna(); fcf=(oc+c_.reindex(oc.index).fillna(0)).dropna()
    n=len(rv); cagr=(rv.iloc[0]/rv.iloc[n-1])**(1/(n-1))-1 if n>=3 and rv.iloc[n-1]>0 else np.nan
    upyrs=int(sum(rv.iloc[k]>rv.iloc[k+1] for k in range(n-1))) if n>=2 else 0
    om=(op/rv.reindex(op.index)).dropna()
    B.append(dict(t=t,roe_yrs=int((roe>0.12).sum()),roe_n=len(roe),fcf_pos=bool(len(fcf)>=3 and (fcf>0).all()),ni_pos=bool(len(nn)>=3 and (nn>0).all()),cagr4=cagr,upyrs=upyrs,nyrs=n,
       om_stable=bool(len(om)>=3 and om.iloc[0]>=om.mean()-0.03),sh_chg=(shs.iloc[0]/shs.iloc[-1]-1) if len(shs)>=2 else np.nan))
X=X.merge(pd.DataFrame(B),on='t')
fin=X.sector.isin(['Financials','Real Estate'])
secpe=X[X.fpe>0].groupby('sector').fpe.median(); X['pe_rel']=X.fpe/X.sector.map(secpe)
X['v3p']=X.v3.rank(pct=True); X['s1p']=X.s1.rank(pct=True)
badj=np.clip(0.67*X.beta3.fillna(1)+0.33,0.6,1.6); X['E_cons']=0.5*X.E_final+0.5*0.10*badj
def cuts_recent(t):
    e=ER.get(t); return None if not e else sum(1 for x in e['timeline'][-4:] if x['c'])
X['cuts4']=X.t.map(cuts_recent); X.loc[X.t=='MSFT','cuts4']=0  # auditor: regex false positive (compared-to-guidance sentence), not a cut
def lenses(f):  # f: dict of threshold multipliers (1 = base)
    L={}
    L['Quality (Buffett)']=(X.roe_yrs>=np.ceil(3*min(f['q'],1.33)).clip(1,4)) & (X.fcf_pos|fin&X.ni_pos) & (X.A_Quality>=0.5*f['q'])
    L['Durable growth']=(X.cagr4>=0.05*f['g']) & (X.revg.fillna(-1)>=-0.02*f['g']) & (X.upyrs>=X.nyrs-2)
    L['Balance sheet']=np.where(fin,(X.roe>0.10*f['b']),(X.nd_ebitda.fillna(0)<=2.5/f['b'])) & ~X.vetoed
    L['Valuation sanity']=(X.fpe>0) & ((X.pe_rel<=1.35/f['v'])|((X.fpe/(X.g.clip(lower=0.01)*100))<=1.5/f['v'])) & (X.E_bb>=0.06*f['v'])
    L['Earnings momentum']=(X.rev90.fillna(0)>=-0.02*f['e']) & (X.beats8.fillna(0.5)>=0.625*f['e'])
    L['Price health']=(X.tt>=np.round(4*f['m'])) & (X.off_hi>=-0.25/f['m'])
    L['Risk']=(X.vol<=0.45/f['r']) & (X.mdd3y>=-0.45/f['r'])
    L['Validated model (v2)']=X.v3p>=0.60*f['p']
    L['Classic model (v1)']=X.s1p>=0.50*f['p']
    L['Management & red flags']=(X.cuts4.fillna(0)==0) & (X['flags'].map(len)<=1)
    return pd.DataFrame(L)
base=lenses({k:1 for k in 'qgbvemrp'})
X['passes']=base.sum(axis=1); hard=base[['Quality (Buffett)','Balance sheet','Risk']].all(axis=1)
X['conv_base']=(X.passes>=9)&hard
rng=np.random.default_rng(11); hits=np.zeros(len(X))
for _ in range(500):
    f={k:rng.uniform(0.8,1.2) for k in 'qgbvemrp'}; L=lenses(f); ok=(L.sum(axis=1)>=9)&L[['Quality (Buffett)','Balance sheet','Risk']].all(axis=1); hits+=ok.values
X['stab']=hits/500
for c in base.columns: X['L_'+c]=base[c].values
X['cscore']=100*(0.35*X.stab+0.25*X.passes/10+0.20*X.E_cons.rank(pct=True)+0.20*X.A_Quality)
X.to_pickle('conv.pkl')
C=X[X.stab>=0.5].sort_values('cscore',ascending=False)
print('base conviction:',int(X.conv_base.sum()),'| stab>=0.9:',int((X.stab>=0.9).sum()),'| stab>=0.7:',int((X.stab>=0.7).sum()))
print('lens pass rates:',{c:int(base[c].sum()) for c in base.columns})
print(C[['t','sector','sub','cscore','stab','passes','E_cons','fpe','vol','cagr4','roe_yrs','cuts4']].head(40).round(3).to_string())
