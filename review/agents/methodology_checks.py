from pathlib import Path
import pandas as pd, numpy as np, json, pickle
p=Path('source_bundle/equity_project')
x=pd.read_pickle(p/'conv.pkl').set_index('t')
port=json.loads((p/'conv_port.json').read_text())
w=pd.Series(port['w']); k=x.loc[w.index]
s2=pickle.load(open(p/'s2.pkl','rb'))
fields=['E_cons','E_bb','E_fac','E_scen','E_final','nby','dy','g','bb_growth','bb_rerate','fpe','price','cuts4','nd_ebitda']
print('HOLDINGS',k[fields].round(5).to_json(orient='index'))
print('SUMMARY',json.dumps({'n':len(x),'scenario_available':int(x.E_scen.notna().sum()),'holdings_scenario_available':int(k.E_scen.notna().sum()),'weighted_nby':float(w@k.nby),'weighted_E':float(w@k.E_cons),'weights_sum':float(w.sum()),'largest_weight':float(w.max()),'sector_weights':w.groupby(k.sector).sum().to_dict(),'management_no_docs':int(x.cuts4.isna().sum()),'management_lens_pass_no_docs':int(x.loc[x.cuts4.isna(),'L_Management & red flags'].sum()),'missing_debt':int(x.nd_ebitda.isna().sum())}))
print('CAPEX_OVERRIDE',json.dumps({t:{'capex_adj':s2[t]['capex_adj'],'methods':s2[t]['methods']} for t in w.index if t in s2},default=float))
print('LENS_CORR',x[[c for c in x if c.startswith('L_')]].astype(float).corr().round(3).to_json())
# Existing holdings, prior portfolio construction retained; this isolates sensitivity, not a corrected investable model.
C=pd.read_pickle(p/'close10.pkl').ffill()
M=C[w.index].resample('ME').last().pct_change().iloc[-121:]
print('MISSING_MONTHS',M.isna().sum().to_json())
pm=(M.fillna(0)@w).values
sm=C['^GSPC'].resample('ME').last().pct_change().iloc[-121:].fillna(0).values
def boots(m,prior):
    rng=np.random.default_rng(5); n=20000; months=60; blk=3; T=len(m)
    idx=((rng.integers(0,T,(n,months//blk,1))+np.arange(blk))%T).reshape(n,months)
    mm=m-m.mean()+(1+prior)**(1/12)-1
    r=np.prod(1+mm[idx],axis=1)-1
    return {'p_profit5':float((r>0).mean()),'median_cagr5':float(np.median(1+r)**.2-1),'fifth_cagr5':float(np.percentile(1+r,5)**.2-1)}
print('DRIFT_SENSITIVITY',json.dumps({str(prior):{'index':boots(sm,prior),'blend_50':boots(.5*pm+.5*sm,prior+.5*(port['E']-.10))} for prior in [0,.04,.06,.08,.10]}))
print('WINDOW',str(C.index.min()),str(C.index.max()))
