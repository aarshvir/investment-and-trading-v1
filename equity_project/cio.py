import pandas as pd, numpy as np, pickle, json
from scipy.stats import norm
T=pd.read_pickle('s3_30.pkl'); C=pd.read_pickle('close.pkl').ffill(); df=pd.read_pickle('s1.pkl')
T['tier']=np.where((T.exp_ret>=0.08)&(T.stability>=0.7)&(T.conf>=50)&(T.rank30<=15),'A: Buy now',
          np.where(T.exp_ret>=0.03,'B: Accumulate on dips','C: Watchlist'))
pick=[];sec={};sub={};grp_c={}
for _,r in T.sort_values('final',ascending=False).iterrows():
    if r.stability<0.7 or r.exp_ret<0.07: continue
    grp='Insurance' if 'Insurance' in r['sub'] else r['sub']
    if sec.get(r.sector,0)>=3 or sub.get(r['sub'],0)>=1 or grp_c.get(grp,0)>=2: continue
    pick.append(r.t); sec[r.sector]=sec.get(r.sector,0)+1; sub[r['sub']]=sub.get(r['sub'],0)+1; grp_c[grp]=grp_c.get(grp,0)+1
    if len(pick)==10: break
P=T.set_index('t').loc[pick]
raw=P.conf/100*P.exp_ret/P.vol; w=(raw/raw.sum()).clip(0.05,0.15); w=w/w.sum()
for _ in range(5): w=(w.clip(0.05,0.15)); w=w/w.sum()
r=C[pick].pct_change().dropna().iloc[-252:]; cov=r.cov()*252; wv=w.values
vol=float(np.sqrt(wv@cov.values@wv)); mu=float((P.exp_ret*w).sum())
r3=C[pick].pct_change().dropna(); path=(1+r3@wv).cumprod(); mdd=float((path/path.cummax()-1).min())
spx=C['^GSPC'].dropna(); sr=spx.pct_change().dropna()
HC=0.6
port=dict(haircut=HC,exp_cal=mu*HC,p20_cal=float(1-norm.cdf((np.log(1.2)-(mu*HC-vol**2/2))/vol)),pm20_cal=float(norm.cdf((np.log(0.8)-(mu*HC-vol**2/2))/vol)),pick=pick,w=w.round(4).to_dict(),exp=mu,vol=vol,mdd3y=mdd,
  p20=float(1-norm.cdf((np.log(1.2)-(mu-vol**2/2))/vol)),pm20=float(norm.cdf((np.log(0.8)-(mu-vol**2/2))/vol)),
  bull=float((P.up*w).sum()),bear=float((P.down*w).sum()),fpe=float(1/(w/P.fpe).sum()),conf=float((P.conf*w).sum()),
  spx=dict(vol=float(sr.iloc[-252:].std()*np.sqrt(252)),mdd3y=float((spx/spx.cummax()-1).min()),ret1y=float(spx.iloc[-1]/spx.iloc[-252]-1)),
  ret1y_hind=float((1+r@wv).prod()-1), sectors=sec)
T.to_pickle('s3_30.pkl'); json.dump(port,open('port.json','w'),default=float)
print(json.dumps(port,indent=0,default=float)); print(T[['rank30','t','tier','stability','conf','exp_ret']].head(16).to_string())
