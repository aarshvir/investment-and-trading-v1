import pandas as pd, numpy as np, json
X=pd.read_pickle('conv.pkl').set_index('t'); C=pd.read_pickle('close10.pkl').ffill()
cand=X[(X.stab>=0.5)&(X.E_cons>=0.08)].sort_values('cscore',ascending=False)
pick=[];sub=set();sec={}
for t,r in cand.iterrows():
    if r['sub'] in sub: continue
    pick.append(t); sub.add(r['sub']); sec[r.sector]=sec.get(r.sector,0)+1
w=(X.loc[pick,'cscore']*(0.5+X.loc[pick,'stab'])); w=w/w.sum()
for _ in range(50):
    w=w.clip(0.04,0.10); w=w/w.sum()
    for s in set(X.loc[pick,'sector']):
        m=X.loc[pick,'sector']==s; tot=w[m].sum()
        if tot>0.25: w[m]*=0.25/tot
    w=w/w.sum()
M=C[pick].resample('ME').last().pct_change().iloc[-121:].fillna(0); Ms=C['^GSPC'].resample('ME').last().pct_change().iloc[-121:].fillna(0)
E=float((w*X.loc[pick,'E_cons']).sum()); pm=(M@w).values; sm=Ms.values
def boot(m,E,months,n=20000,blk=3,seed=5):
    rng=np.random.default_rng(seed); m=m-m.mean()+(1+E)**(1/12)-1; T=len(m); out=np.empty(n)
    for i in range(n):
        idx=np.concatenate([np.arange(s,s+blk)%T for s in rng.integers(0,T,months//blk)]); out[i]=np.prod(1+m[idx])-1
    return out
b1,b5=boot(pm,E,12),boot(pm,E,60); s1,s5=boot(sm,0.10,12,seed=6),boot(sm,0.10,60,seed=6)
vol=float(pm.std()*np.sqrt(12)); hist=np.cumprod(1+pm)
res=dict(pick=pick,w=w.round(4).to_dict(),E=E,vol=vol,p_pos1=float((b1>0).mean()),p_pos5=float((b5>0).mean()),p_double5=float((b5>=1).mean()),ann5_med=float(np.median(1+b5)**(1/5)-1),
  p5_1=float(np.percentile(b1,5)),p5_5=float(np.percentile(b5,5)),p_loss20_1=float((b1<=-.2).mean()),p15_1=float((b1>=.15).mean()),
  spx=dict(p_pos1=float((s1>0).mean()),p_pos5=float((s5>0).mean()),vol=float(sm.std()*np.sqrt(12))),
  y2022=float(np.prod(1+M.loc['2022'].values@w.values)-1),covid=float(np.prod(1+M.loc['2020-02':'2020-03'].values@w.values)-1),mdd10=float((hist/np.maximum.accumulate(hist)-1).min()),
  sectors=X.loc[pick].groupby('sector').size().to_dict())
json.dump(res,open('conv_port.json','w'),default=float)
print(json.dumps({k:(round(v,3) if isinstance(v,float) else v) for k,v in res.items() if k!='w'},default=float))
print({t:round(w[t],3) for t in w.sort_values(ascending=False).index})
print(X.loc[pick,['sector','stab','passes','cscore','E_cons','fpe','vol']].round(3).to_string())
