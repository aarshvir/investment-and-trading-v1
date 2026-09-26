# AUDIT AGENTS X1 (data), X2 (method & robustness), X3 (output reconciliation)
import pandas as pd, numpy as np, pickle, json
df=pd.read_pickle('s1.pkl'); S=pd.read_pickle('s3_100.pkl'); T=pd.read_pickle('s3_30.pkl'); C=pd.read_pickle('close.pkl')
I=json.load(open('info.json')); OVR=pickle.load(open('overrides.pkl','rb'))
A={}
# X1 data integrity
fields=['fpe','evebitda','roe','om','fcfy','revg','epsg','tgt','beta','vol']
cov={f:float(df[f].notna().mean()) for f in fields}
last=C.index[-1]; stale=[t for t in df.t if C[t].dropna().index[-1]<last-pd.Timedelta(days=5)]
mism=[]
for t in df.t:
    cp=I[t].get('currentPrice') or I[t].get('regularMarketPrice'); p=float(df.loc[df.t==t,'price'].iloc[0])
    if cp and abs(cp/p-1)>0.05: mism.append((t,round(p,2),cp))
outl=df[(df.fpe>150)|(df.revg>2)|(df.epsg>10)][['t','fpe','revg','epsg']].round(2).values.tolist()
A['X1']=dict(universe=int(len(df)),coverage=cov,stale=stale,price_mismatch=mism[:15],n_mismatch=len(mism),outliers=outl[:20],n_outliers=len(outl),asof=str(last.date()),
  deep_complete=int(sum(1 for t in S.t if S.loc[S.t==t,'nq'].iloc[0]>=6)))
# X2 robustness: Monte Carlo on committee weights (+/-50% random perturbation), 500 runs
keys=['C_screen','C_forensic','C_capital','C_earn','C_value','C_buffett']; base=np.array([.25,.10,.10,.15,.25,.15])
elig=S[S.veto3.map(len)==0].reset_index(drop=True); M=elig[keys].values
rng=np.random.default_rng(7); hits=np.zeros(len(elig))
for _ in range(500):
    w=base*rng.uniform(0.5,1.5,6); w/=w.sum(); sc=M@w; top=np.argsort(-sc)[:30]; hits[top]+=1
elig['stab']=hits/500
stab=dict(zip(elig.t,elig.stab.round(2)))
T['stability']=T.t.map(stab)
sec_uni=df.sector.value_counts(normalize=True); sec_30=T.sector.value_counts(normalize=True)
A['X2']=dict(runs=500,stability={t:stab[t] for t in T.t},median_stab=float(T.stability.median()),
  fragile=[t for t in T.t if stab[t]<0.5],sector_tilt={s:(float(sec_30.get(s,0)),float(sec_uni.get(s,0))) for s in sec_uni.index},
  overrides=OVR, vetoes_applied=int((S.veto3.map(len)>0).sum()),
  veto_leak=int(sum(len(v)>0 for v in T.veto3)))
# X3 output reconciliation
chk=[]
for _,r in T.iterrows():
    ok=(r.bull>r.base>r.bear) and 0<=r.conf<=100 and r.up>0 and r.down<0
    if not ok: chk.append(r.t)
A['X3']=dict(scenario_order_fail=chk,n30=int(len(T)),exp_basket=float(T.exp_ret.mean()),top10_exp=float(T.head(10).exp_ret.mean()),
  prior_list={t:(int(S.loc[S.t==t,'rank100'].iloc[0]) if (S.t==t).any() else None, bool((T.t==t).any())) for t in ['NVDA','GOOGL','TSM','LLY','V','BRK-B','AVGO','BLK','ABBV','CVX','META','MSFT','AMZN']},
  prior_rank500={t:int(df.loc[df.t==t,'rank500'].iloc[0]) for t in ['NVDA','GOOGL','LLY','V','BRK-B','AVGO','BLK','ABBV','CVX','META','MSFT','AMZN'] if (df.t==t).any()})
T.to_pickle('s3_30.pkl'); json.dump(A,open('audit.json','w'),default=float)
print(json.dumps({k:{kk:vv for kk,vv in v.items() if kk not in('stability','sector_tilt','coverage')} for k,v in A.items()},default=float,indent=0)[:3500])
print(T[['rank30','t','stability']].to_string())
