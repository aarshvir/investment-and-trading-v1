# V3 "HURDLE-15" MODEL: momentum + earnings momentum + value (building-block E[R]) + quality guardrail; risk as constraint, not a return pillar
import pandas as pd, numpy as np, pickle, json, warnings
warnings.filterwarnings('ignore')
df=pd.read_pickle('s1.pkl'); E=pickle.load(open('est_all.pkl','rb')); F=pickle.load(open('fund_all.pkl','rb')); I=json.load(open('info.json'))
C=pd.read_pickle('close10.pkl').ffill()
def v(x):
    try: x=float(x); return x if x==x else np.nan
    except Exception: return np.nan
rows=[]
for _,r in df.iterrows():
    t=r.t; e=E.get(t,{}); i=I.get(t,{}); tr=e.get('trend'); rv=e.get('rev'); ed=e.get('ed'); ud=e.get('ud')
    if tr is not None and ('current' not in tr.columns or '90daysAgo' not in tr.columns): tr=None
    if rv is not None and ('upLast30days' not in rv.columns or 'downLast30days' not in rv.columns): rv=None
    if ed is not None and ('Reported EPS' not in ed.columns or 'Surprise(%)' not in ed.columns): ed=None
    if ud is not None and 'Action' not in getattr(ud,'columns',[]): ud=None
    eps0=v(tr.loc['0y','current']) if tr is not None and '0y' in tr.index else np.nan
    eps1=v(tr.loc['+1y','current']) if tr is not None and '+1y' in tr.index else np.nan
    e90=v(tr.loc['+1y','90daysAgo']) if tr is not None and '+1y' in tr.index else np.nan
    rev90=eps1/e90-1 if e90 and e90>0 and eps1==eps1 else np.nan
    up=v(rv.loc['+1y','upLast30days']) if rv is not None and '+1y' in rv.index else np.nan
    dn=v(rv.loc['+1y','downLast30days']) if rv is not None and '+1y' in rv.index else np.nan
    nan=i.get('numberOfAnalystOpinions') or np.nan
    netrev=(np.nan_to_num(up)-np.nan_to_num(dn))/max(nan,1) if nan==nan else np.nan
    beats=surp=np.nan
    if ed is not None and len(ed):
        x=ed.dropna(subset=['Reported EPS']).head(8)
        if len(x): beats=(x['Surprise(%)']>0).mean(); surp=x['Surprise(%)'].clip(-30,30).mean()
    ups=dns=0
    if ud is not None and len(ud):
        try:
            cut=pd.Timestamp.now(tz=ud.index.tz)-pd.Timedelta(days=90) if ud.index.tz else pd.Timestamp.now()-pd.Timedelta(days=90)
            u=ud[ud.index>=cut]; ups=int((u.Action=='up').sum()); dns=int((u.Action=='down').sum())
        except Exception: pass
    # shareholder yield
    cf=F.get(t,{}).get('cf'); bb=0.0; iss=0.0
    if cf is not None and len(cf.columns):
        c0=cf.columns[0]
        for nm in ['Repurchase Of Capital Stock','Common Stock Payments']:
            if nm in cf.index and v(cf.loc[nm,c0])==v(cf.loc[nm,c0]): bb=-v(cf.loc[nm,c0]); break
        for nm in ['Issuance Of Capital Stock','Common Stock Issuance']:
            if nm in cf.index and v(cf.loc[nm,c0])==v(cf.loc[nm,c0]): iss=v(cf.loc[nm,c0]); break
    mc=(i.get('marketCap') or np.nan)
    dy=i.get('trailingAnnualDividendYield') or 0
    nby=np.clip((bb-iss)/mc,-0.05,0.08) if mc==mc and mc>0 else 0
    g=np.clip(eps1/eps0-1,-0.3,0.6) if (eps0==eps0 and eps0>0 and eps1==eps1) else (r.fwd_epsg if r.fwd_epsg==r.fwd_epsg else np.nan)
    c=C[t].dropna(); p=float(c.iloc[-1])
    mom=float(c.iloc[-22]/c.iloc[-253]-1) if len(c)>260 else np.nan
    rows.append(dict(t=t,eps0=eps0,eps1=eps1,rev90=rev90,netrev=netrev,beats8=beats,surp=surp,ups=ups,dns=dns,dy=dy,nby=nby,g=g,mom121=mom))
X=df.merge(pd.DataFrame(rows),on='t')
art=(X.g>0.35)&(X.revg.fillna(0)<0.10)
X['g_artifact']=art; X.loc[art,'g']=np.clip(X.loc[art,'revg'].fillna(0),0,None)+0.10
sec_fpe=X[X.fpe>0].groupby('sector').fpe.median(); sec_g=X.groupby('sector').g.median()
def pr(s,asc=True,bys=False,clip=None):
    s=pd.to_numeric(s,errors='coerce'); s=s.clip(*clip) if clip else s; s=s.fillna(s.median())
    return s.groupby(X.sector).rank(pct=True,ascending=asc) if bys else s.rank(pct=True,ascending=asc)
# Building-block expected return (fundamental method)
HC_G=0.70  # haircut analysts' next-year EPS growth by 30% (assumption: consensus runs optimistic)
Qp=X.A_Quality
fair=X.sector.map(sec_fpe)*(0.8+0.4*Qp)*(1+np.clip(X.g.fillna(0)-X.sector.map(sec_g).fillna(0),-0.2,0.3))
rer=np.clip((fair/X.fpe.where(X.fpe>0))**(1/3)-1,-0.10,0.10).fillna(-0.05)
X['bb_yield']=X.dy.fillna(0)+X.nby.fillna(0); X['bb_growth']=np.clip(HC_G*X.g.fillna(0),-0.25,0.30); X['bb_rerate']=rer
X['E_bb']=np.clip(X.bb_yield+X.bb_growth+X.bb_rerate,-0.3,0.40)
# Pillars
X['P_mom']=(pr(X.mom121,clip=(-1,3))+pr(X.ret6,clip=(-1,3))+X.tt/7)/3
X['P_emom']=(pr(X.rev90,clip=(-.5,1))+pr(X.netrev)+pr(X.beats8)+pr(X.surp)+pr(X.ups-X.dns))/5
X['P_val']=(pr(X.E_bb)+pr(X.fcfy,True,True,(-.2,.2))+pr(X.fpe.where(X.fpe>0),False,True))/3
X['P_q']=X.A_Quality
W=dict(P_mom=.30,P_emom=.20,P_val=.30,P_q=.20)
X['v3']=100*sum(W[k]*X[k] for k in W)
X['gate']=~X.vetoed & (X.vol<=0.60) & (X.fpe>0)
X['gate_why']=np.where(X.vetoed,'Stage-1 veto',np.where(X.vol>0.60,'Volatility >60%',np.where(~(X.fpe>0),'No forward profit','')))
X=X.sort_values('v3',ascending=False).reset_index(drop=True); X['rank_v3']=X.index+1
gp=X.v3.where(X.gate).rank(pct=True)
W3=C.resample('W-FRI').last().pct_change().iloc[-156:]; sw=W3['^GSPC']
b3={t:(np.cov(W3[t].dropna(),sw[W3[t].dropna().index])[0,1]/sw[W3[t].dropna().index].var()) if t in W3 and W3[t].notna().sum()>100 else np.nan for t in X.t}
X['beta3']=X.t.map(b3)
badj=np.clip(0.67*X.beta3.fillna(1)+0.33,0.6,1.6)
X['alpha']=np.clip(0.028*(gp-0.5)/0.44,-0.03,0.03).fillna(-0.02)
X['E_fac']=0.10*badj+X.alpha
S2=pickle.load(open('s2.pkl','rb'))
X['E_scen']=X.t.map(lambda t: 0.6*S2[t]['exp_ret'] if t in S2 else np.nan)
X['E_final']=X[['E_bb','E_fac','E_scen']].mean(axis=1)
X['E_spread']=X[['E_bb','E_fac','E_scen']].max(axis=1)-X[['E_bb','E_fac','E_scen']].min(axis=1)
X.to_pickle('v3.pkl')
g=X[X.gate]
print('gated',len(g)); print(g[['rank_v3','t','sector','v3','P_mom','P_emom','P_val','P_q','E_bb','vol','fpe','g','rev90']].head(40).round(2).to_string())
