# AUDIT LOOP 1 (3 auditors in parallel): holdings integrity, survivorship-bias quantification, assumption sensitivity
import pandas as pd, numpy as np, json, pickle, yfinance as yf, re, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
K=pickle.load(open('K.pkl','rb')); P=json.load(open('port2.json')); E=pickle.load(open('edgar.pkl','rb')); w=pd.Series(P['Recommended']['w'])
def holdings():
    out=[]
    for t in w.index:
        r=K.loc[t]; docs=E.get(t) or []
        nm=re.sub(r'[^A-Za-z ]','',r['name']).split()[0].lower()
        ok=sum(1 for d in docs if nm in d['text'][:3000].lower())
        out.append(dict(t=t,w=w[t],vol=r.vol,conf=r.conf2,Ebb=r.E_bb,Efac=r.E_fac,Escen=r.E_scen,spread=r.E_spread,fpe=r.fpe,art=bool(r.g_artifact),docs=len(docs),name_match=ok))
    return pd.DataFrame(out)
def survivorship():
    px=yf.download(['RSP','SPY'],start='2023-09-20',end='2026-09-25',auto_adjust=True,progress=False)['Close']
    bt=json.load(open('backtest.json')); v3=json.load(open('bt_v3.json')); res={}
    for y,(a,b) in {'2023':('2023-09-29','2024-09-27'),'2024':('2024-09-27','2025-09-26'),'2025':('2025-09-26','2026-09-24')}.items():
        r=lambda s:float(px[s].loc[:b].iloc[-1]/px[s].loc[:a].iloc[-1]-1)
        res[y]=dict(RSP=r('RSP'),EW_survivors=bt[y]['ew'],bias=bt[y]['ew']-r('RSP'),v3_top30=v3[y]['top30'],v3_vs_RSP=v3[y]['top30']-r('RSP'),v3_vs_EWsurv=v3[y]['top30']-bt[y]['ew'])
    return res
def sensitivity():
    ws=w; k=K.loc[ws.index]; badj=np.clip(0.67*k.beta3.fillna(1)+0.33,0.6,1.6)
    def Esh(mkt=0.10,hc=0.70,amax=0.028):
        bb=np.clip(k.bb_yield+np.clip(hc*k.g.fillna(0),-0.25,0.30)+k.bb_rerate,-0.3,0.4)
        fac=mkt*badj+np.clip(amax*(k.alpha/0.028),-0.03,0.03)
        ef=pd.concat([bb,fac,k.E_scen],axis=1).mean(axis=1); sp=pd.concat([bb,fac,k.E_scen],axis=1).max(axis=1)-pd.concat([bb,fac,k.E_scen],axis=1).min(axis=1)
        wc=(k.conf2/100)*(1-np.clip(sp/0.4,0,0.5)); return float((ws*(wc*ef+(1-wc)*mkt*badj)).sum())
    base=Esh(); rows={'Base case':base}
    for lab,kw in [('Market prior 8%',dict(mkt=0.08)),('Market prior 12%',dict(mkt=0.12)),('Growth haircut 50%',dict(hc=0.5)),('No growth haircut',dict(hc=1.0)),('Alpha zero',dict(amax=0.0)),('Alpha unshrunk (6.7%)',dict(amax=0.067))]: rows[lab]=Esh(**kw)
    return rows
with ThreadPoolExecutor(3) as ex:
    f1,f2,f3=ex.submit(holdings),ex.submit(survivorship),ex.submit(sensitivity)
    H,S,T=f1.result(),f2.result(),f3.result()
print(H.round(3).to_string()); print(json.dumps({k:{a:round(b,3) for a,b in v.items()} for k,v in S.items()})); print({k:round(v,4) for k,v in T.items()})
json.dump(dict(surv=S,sens=T),open('audit_loop1.json','w'))
