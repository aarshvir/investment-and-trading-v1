# CIO v2: candidate ranking + mandate optimizer + fat-tailed probability engine (10-yr block bootstrap)
import pandas as pd, numpy as np, json, pickle
from scipy.optimize import minimize
X=pd.read_pickle('v3.pkl').set_index('t'); ER=json.load(open('edgar_read.json')); C=pd.read_pickle('close10.pkl').ffill()
pool=[t for t in ER if t in X.index and X.loc[t,'gate']]
K=X.loc[pool].copy()
K['gscore']=[ER[t]['gscore'] for t in pool]; K['gcut']=[ER[t]['cuts'] for t in pool]
comp=K[['fpe','roe','revg','rev90','beats8','E_scen','beta3','fcfy']].notna().mean(axis=1)
agree=1-np.clip(K.E_spread/0.35,0,1)
K['conf2']=(100*(0.30*agree+0.15*comp+0.20*K.beats8.fillna(.5)+0.20*np.clip(0.5+K.gscore,0,1)+0.15*K.A_Quality)).round(0)
pr=lambda s: s.rank(pct=True)
K['score2']=100*(0.35*pr(K.E_final)+0.25*pr(K.v3)+0.15*pr(K.conf2)+0.15*pr(K.gscore)+0.10*pr(K.A_Quality))
K=K.sort_values('score2',ascending=False); K['rank52']=range(1,len(K)+1)
badj=np.clip(0.67*K.beta3.fillna(1)+0.33,0.6,1.6)
wc=(K.conf2/100)*(1-np.clip(K.E_spread.fillna(0.2)/0.4,0,0.5))
K['E_prior']=0.10*badj; K['E_sh']=wc*K.E_final+(1-wc)*K.E_prior
el=K[(K.E_sh>=0.09)&(K.conf2>=50)&(K.A_Quality>=0.35)].index.tolist()
M=C[el].resample('ME').last().pct_change().iloc[-121:].dropna(how='all')
Wk=C[el].resample('W-FRI').last().pct_change().iloc[-157:]
S=Wk.cov()*52; S=0.7*S+0.3*np.diag(np.diag(S))   # shrink toward diagonal
mu0=K.loc[el,'E_sh'].values.copy(); mu=mu0.copy(); subs=K.loc[el,'sub'].values; secs=K.loc[el,'sector'].values; caps=np.where(K.loc[el,'conf2']>=75,0.10,0.07)
def solve(vol_cap):
    n=len(el); x0=np.ones(n)/n
    cons=[{'type':'eq','fun':lambda w:w.sum()-1},{'type':'ineq','fun':lambda w:vol_cap**2-w@S.values@w}]
    for s in set(secs): cons.append({'type':'ineq','fun':lambda w,s=s:0.30-w[secs==s].sum()})
    for s in set(subs): cons.append({'type':'ineq','fun':lambda w,s=s:0.12-w[subs==s].sum()})
    r=minimize(lambda w:-(w@mu)+0.5*np.sum(np.maximum(w-0.0,0)**2)*0.02,x0,bounds=[(0,c) for c in caps],constraints=cons,method='SLSQP',options={'maxiter':200,'ftol':1e-7})
    w=pd.Series(r.x,index=el); w=w[w>0.02]; w=w/w.sum(); return w
def boot(w,E,n=20000,blk=3,seed=1):
    rng=np.random.default_rng(seed); m=M[w.index].fillna(0).values@w.values
    m=m-m.mean()+(1+E)**(1/12)-1; T=len(m); out=np.empty(n)
    for i in range(n):
        idx=np.concatenate([np.arange(s,s+blk)%T for s in rng.integers(0,T,12//blk)]); out[i]=np.prod(1+m[idx])-1
    return out
def stats(w):
    E=float((w*K.loc[w.index,'E_sh']).sum()); Eraw=float((w*K.loc[w.index,'E_final']).sum()); v=float(np.sqrt(w.values@S.loc[w.index,w.index].values@w.values))
    b=boot(w,E); hist=(1+(M[w.index].fillna(0)@w)).cumprod()
    y22=float((1+M[w.index].fillna(0).loc['2022']@w).prod()-1); c20=float((1+M[w.index].fillna(0).loc['2020-02':'2020-03']@w).prod()-1)
    return dict(E=E,E_raw=Eraw,vol=v,p15=float((b>=.15).mean()),p20=float((b>=.20).mean()),p25=float((b>=.25).mean()),p50=float((b>=.5).mean()),p0=float((b>=0).mean()),
      pl10=float((b<=-.10).mean()),pl20=float((b<=-.20).mean()),p5=float(np.percentile(b,5)),p50th=float(np.median(b)),p95=float(np.percentile(b,95)),
      y2022=y22,covid=c20,mdd10=float((hist/hist.cummax()-1).min()),n=int(len(w)),beta=float((w*K.loc[w.index,'beta3']).sum()),conf=float((w*K.loc[w.index,'conf2']).sum()),
      w=w.round(4).to_dict())
# Resampled efficiency (Michaud): perturb expected returns by their own method disagreement, re-optimise 150x, average weights
rng=np.random.default_rng(42); sd=np.clip(K.loc[el,'E_spread'].fillna(0.15).values/2,0.02,0.12)
def resampled(vc,runs=40):
    global mu; acc=pd.Series(0.0,index=el); hits=pd.Series(0,index=el)
    for _ in range(runs):
        mu=mu0+rng.normal(0,sd); w=solve(vc); acc[w.index]+=w; hits[w.index]+=1
    mu=mu0.copy(); w=acc/runs; w=w[w>0.015]; return w/w.sum(), (hits/runs)
P={}
for name,vc in [('Guardian',0.14),('Balanced',0.16),('Hurdle',0.18),('Stretch',0.22)]:
    w,h=resampled(vc); P[name]=stats(w); P[name]['vol_cap']=vc; P[name]['hit']=h[h>0].round(2).to_dict()
spx=C['^GSPC'].resample('ME').last().pct_change().iloc[-121:].dropna()
P['S&P 500 (for reference)']=dict(E=0.10,vol=float(spx.std()*np.sqrt(12)))
pickle.dump(K,open('K.pkl','wb')); json.dump(P,open('port2.json','w'),default=float)
for k,v in P.items():
    if 'w' not in v: continue
    print(k,'n',v['n'],'E %.1f%% vol %.1f%% beta %.2f | P15 %.0f%% P20 %.0f%% P25 %.0f%% P50 %.1f%% P>=0 %.0f%% P<=-20 %.1f%% | median %.1f%% 5th %.1f%% 95th %.1f%% | 2022 %.1f%% covid %.1f%% conf %.0f'%(100*v['E'],100*v['vol'],v['beta'],100*v['p15'],100*v['p20'],100*v['p25'],100*v['p50'],100*v['p0'],100*v['pl20'],100*v['p50th'],100*v['p5'],100*v['p95'],100*v['y2022'],100*v['covid'],v['conf']))
    print('   ',{a:round(b,3) for a,b in sorted(v['w'].items(),key=lambda z:-z[1])})
print(K[['rank52','sector','score2','E_final','conf2','gscore','v3','vol']].head(25).round(3).to_string())

# Recommended = resampled Hurdle trimmed to its 20 most robust names (weight x hit-rate), re-normalised
h=pd.Series(P['Hurdle']['hit']); w=pd.Series(P['Hurdle']['w'])
keep=(w*h.reindex(w.index).fillna(0)).nlargest(20).index; wr=w[keep]/w[keep].sum()
P['Recommended']=stats(wr); P['Recommended']['hit']=h.reindex(keep).round(2).to_dict()
json.dump(P,open('port2.json','w'),default=float)
v=P['Recommended']; print('REC n',v['n'],'E %.1f%% (raw %.1f%%) vol %.1f%% beta %.2f | P15 %.0f%% P20 %.0f%% P25 %.0f%% P50 %.1f%% P>=0 %.0f%% P<=-10 %.0f%% P<=-20 %.1f%% | 5th %.1f%% median %.1f%% 95th %.1f%% | 2022 %.1f%% covid %.1f%% mdd10 %.1f%% conf %.0f'%(100*v['E'],100*v['E_raw'],100*v['vol'],v['beta'],100*v['p15'],100*v['p20'],100*v['p25'],100*v['p50'],100*v['p0'],100*v['pl10'],100*v['pl20'],100*v['p5'],100*v['p50th'],100*v['p95'],100*v['y2022'],100*v['covid'],100*v['mdd10'],v['conf']))
print({a:round(b,3) for a,b in sorted(v['w'].items(),key=lambda z:-z[1])})
print(K.loc[list(v['w'].keys()),['sector','sub','E_sh','conf2','gscore','vol']].round(3).to_string())
