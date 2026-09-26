"""Independent replication of supplied risk models; source bundle is read-only.
Run from workspace root. Pickle global/opcode inspection saved before this script.
Outputs are conditional diagnostics, not forecasts or recommended allocations.
"""
import json, pathlib, pickle
import numpy as np
import pandas as pd


SRC=pathlib.Path('source_bundle/equity_project'); OUT=pathlib.Path('review/data')
# Restricted class resolution adds a second guard after offline opcode inspection.
ALLOWED={('pandas','DataFrame'),('pandas','StringDtype'),('pandas','Index'),('pandas','RangeIndex'),('pandas','DatetimeIndex'),
 ('pandas.core.internals.managers','BlockManager'),('pandas._libs.internals','_unpickle_block'),
 ('pandas._libs.arrays','__pyx_unpickle_NDArrayBacked'),('pandas.arrays','StringArray'),('pandas.arrays','DatetimeArray'),
 ('numpy._core.multiarray','_reconstruct'),('numpy._core.numeric','_frombuffer'),('numpy','ndarray'),('numpy','dtype'),
 ('builtins','slice'),('pandas.core.indexes.base','_new_Index'),('pandas.core.indexes.datetimes','_new_DatetimeIndex')}
class CheckedUnpickler(pickle.Unpickler):
 def find_class(self,module,name):
  if (module,name) not in ALLOWED: raise ValueError(f'Unexpected global: {module}.{name}')
  return super().find_class(module,name)
def read(name):
 with (SRC/name).open('rb') as f: return CheckedUnpickler(f).load()
X=read('conv.pkl').set_index('t'); C0=read('close10.pkl'); C=C0.ffill(); K=read('K.pkl')
P=json.loads((SRC/'conv_port.json').read_text()); P2=json.loads((SRC/'port2.json').read_text())
pick=[]; sub=set()
for t,r in X[(X.stab>=.5)&(X.E_cons>=.08)].sort_values('cscore',ascending=False).iterrows():
 if r['sub'] not in sub: pick.append(t); sub.add(r['sub'])
w=X.loc[pick,'cscore']*(.5+X.loc[pick,'stab']); w=w/w.sum()
for _ in range(50):
 w=w.clip(.04,.10); w=w/w.sum()
 for s in sorted(set(X.loc[pick,'sector'])):
  m=X.loc[pick,'sector']==s; total=w[m].sum()
  if total>.25: w[m]*=.25/total
 w=w/w.sum()
monthly=C[pick].resample('ME').last().pct_change(fill_method=None).iloc[-121:]
M=monthly.fillna(0); pm=(M@w).values
sm=C['^GSPC'].resample('ME').last().pct_change(fill_method=None).iloc[-121:].fillna(0).values
E=float(w@X.loc[pick,'E_cons'])
def boot(m,E,months=60,n=20000,blk=3,seed=5):
 rng=np.random.default_rng(seed); shifted=m-m.mean()+(1+E)**(1/12)-1
 starts=rng.integers(0,len(m),size=(n,int(np.ceil(months/blk))))
 idx=((starts[:,:,None]+np.arange(blk))%len(m)).reshape(n,-1)[:,:months]
 return np.prod(1+shifted[idx],axis=1)-1
def stats(a):
 return dict(p_positive=float((a>0).mean()),p_double=float((a>=1).mean()),p5=float(np.quantile(a,.05)),median=float(np.median(a)),p95=float(np.quantile(a,.95)),mean=float(a.mean()))
sectors=w.groupby(X.loc[w.index,'sector']).sum()
A=np.array([(X.loc[pick,'sector']==s).values.astype(float) for s in sectors.index])
max_feasible=sum(min(.25,.10*int(row.sum())) for row in A)
out=dict(source_dates=[str(C.index.min()),str(C.index.max())],monthly_dates=[str(M.index.min()),str(M.index.max())],monthly_n=len(M),
 weights=w.to_dict(),sector_weights=sectors.to_dict(),weight_sum=float(w.sum()),cap_violations=w[w>.1+1e-8].to_dict(),
 E=E,replication_1yr=stats(boot(pm,E,12)),replication_5yr=stats(boot(pm,E,60)),
 max_feasible_invested=max_feasible,
 monthly_missing=monthly.isna().sum().to_dict(),first_observation={t:str(C0[t].first_valid_index()) for t in pick},
 delivered_weight_max_abs_difference=float((w-pd.Series(P['w'])).abs().max()))
rows=[]
for mix,name in [(0,'stock'),(.5,'50_50'),(1,'index')]:
 m=pm*(1-mix)+sm*mix
 for er in [0,.02,.04,.06,.08,.10,E*(1-mix)+.10*mix,.12]:
  for blk in [1,3,6,12,24]:
   r=dict(portfolio=name,assumed_annual_return=er,block_months=blk,n=20000,seed=5,**stats(boot(m,er,blk=blk)))
   rows.append(r)
pd.DataFrame(rows).to_csv(OUT/'risk_sensitivity.csv',index=False)
# Missing-history treatments are sensitivities, not substitutes for authentic history.
alts={'original_zero_fill':monthly.fillna(0), 'prelisting_index_proxy':monthly.T.fillna(pd.Series(sm,index=monthly.index)).T,
      'common_history':monthly.dropna()}
out['history_sensitivity']={}
for label,frame in alts.items():
 m=(frame@w).values; s=pd.Series(sm,index=M.index).reindex(frame.index).values
 out['history_sensitivity'][label]={'months':len(m),'start':str(frame.index[0]),'stock_vol':float(np.std(m)*np.sqrt(12)),
  'stock_5yr':stats(boot(m,E)), 'blend_5yr':stats(boot(.5*m+.5*s,.5*E+.05))}
# End-date partial month and month-end drawdown versus daily path.
daily=C[pick].pct_change(fill_method=None).loc[M.index[0]:].fillna(0)@w
def dd(a):
 wealth=np.r_[1,np.cumprod(1+a)]; return float((wealth/np.maximum.accumulate(wealth)-1).min())
out['drawdown']={'monthly':dd(pm),'daily_rebalanced_proxy':dd(daily.values)}
# Exact daily wealth path with reset to supplied weights at each prior month end.
# Pre-listing missing returns retain original zero-return cash treatment.
wealth=1.; path=[1.]; path_dates=[C.index[C.index<M.index[0].replace(day=1)][-1]]; endpoints=[]
for month in M.index:
 prior=C[pick].loc[C.index<month.replace(day=1)].iloc[-1]
 prices=C[pick].loc[(C.index>=month.replace(day=1))&(C.index<=month)]
 relatives=prices.div(prior).fillna(1)
 monthpath=wealth*(relatives@w)
 path.extend(monthpath.tolist()); path_dates.extend(prices.index.tolist()); wealth=float(monthpath.iloc[-1]); endpoints.append(wealth)
path=np.array(path)
out['drawdown']['daily_path_monthly_rebalanced']=float((path/np.maximum.accumulate(path)-1).min())
trough=int(np.argmin(path/np.maximum.accumulate(path)-1)); peak=int(np.argmax(path[:trough+1]))
out['drawdown']['daily_path_peak_date']=str(path_dates[peak]); out['drawdown']['daily_path_trough_date']=str(path_dates[trough])
out['drawdown']['monthly_endpoint_max_abs_error']=float(np.max(np.abs(np.array(endpoints)-np.cumprod(1+pm))))
out['complete_months_only']={'end':str(M.index[-2]),'stock_5yr':stats(boot(pm[:-1],E)),'blend_5yr':stats(boot(.5*(pm[:-1]+sm[:-1]),.5*E+.05))}
# Audit delivered v2 weights against constraints on same covariance model.
el=K[(K.E_sh>=.09)&(K.conf2>=50)&(K.A_Quality>=.35)].index.tolist()
Wk=C[el].resample('W-FRI').last().pct_change(fill_method=None).iloc[-157:]
S=Wk.cov()*52; S=.7*S+.3*np.diag(np.diag(S))
out['v2_constraints']={}
for name,p in P2.items():
 if 'w' not in p: continue
 ww=pd.Series(p['w']); sec=ww.groupby(K.loc[ww.index,'sector']).sum(); su=ww.groupby(K.loc[ww.index,'sub']).sum()
 caps=pd.Series(np.where(K.loc[ww.index,'conf2']>=75,.1,.07),index=ww.index)
 out['v2_constraints'][name]={'weight_sum':float(ww.sum()),'vol':float(np.sqrt(ww@S.loc[ww.index,ww.index]@ww)),
  'vol_cap':p.get('vol_cap'),'stock_cap_violations':ww[ww>caps+1e-4].to_dict(),'sector_weights':sec.to_dict(),
  'subindustry_weights':su.to_dict(),'sector_violations':sec[sec>.3001].to_dict(),'subindustry_violations':su[su>.1201].to_dict()}
(OUT/'risk_audit.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ['weights','first_observation','v2_constraints','v2_minimum_feasible_vol']},indent=2))
print('V2',json.dumps({k:{x:y for x,y in v.items() if x not in ['sector_weights','subindustry_weights']} for k,v in out['v2_constraints'].items()},indent=2))
