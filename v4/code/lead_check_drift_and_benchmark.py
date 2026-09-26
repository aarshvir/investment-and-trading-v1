# Lead verification: (1) v3 "90% 5-yr odds" sensitivity to the assumed drift; (2) v3 bt10 benchmark used a PRICE index (^GSPC) vs total-return stocks.
import pandas as pd, numpy as np, json, yfinance as yf
LEG=r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\equity_project'
C=pd.read_pickle(LEG+r'\close10.pkl').ffill(); cp=json.load(open(LEG+r'\conv_port.json')); w=pd.Series(cp['w']); pick=list(w.index)
M=C[pick].resample('ME').last().pct_change().iloc[-121:].fillna(0); Ms=C['^GSPC'].resample('ME').last().pct_change().iloc[-121:].fillna(0)
pm=(M@w).values; sm=Ms.values
def boot(m,E,months,n=20000,blk=3,seed=5):
    rng=np.random.default_rng(seed); m=m-m.mean()+(1+E)**(1/12)-1; T=len(m); out=np.empty(n)
    for i in range(n):
        idx=np.concatenate([np.arange(s,s+blk)%T for s in rng.integers(0,T,months//blk)]); out[i]=np.prod(1+m[idx])-1
    return out
blend=0.5*pm+0.5*sm
print('50/50 blend 5-yr P(profit) by assumed drift (v3 method, same data):')
for E in [0.04,0.06,0.08,0.10,0.1068]:
    b=boot(blend,E,60); print('  drift %.2f%% -> %.1f%%'%(100*E,100*(b>0).mean()))
spy=yf.download('SPY',start='2015-09-01',end='2026-09-26',auto_adjust=True,progress=False)['Close'].squeeze()
g=C['^GSPC'].dropna(); s=spy.reindex(g.index).ffill()
t0,t1=pd.Timestamp('2016-10-31'),pd.Timestamp('2026-08-31')
gi=g.loc[:t0].iloc[-1],g.loc[:t1].iloc[-1]; si=s.loc[:t0].iloc[-1],s.loc[:t1].iloc[-1]; yrs=(t1-t0).days/365.25
print('Nov-2016..Aug-2026: ^GSPC price CAGR %.2f%%  vs SPY total-return CAGR %.2f%%  -> benchmark understated by %.2f pts/yr'%(100*((gi[1]/gi[0])**(1/yrs)-1),100*((si[1]/si[0])**(1/yrs)-1),100*(((si[1]/si[0])**(1/yrs))-((gi[1]/gi[0])**(1/yrs)))))
