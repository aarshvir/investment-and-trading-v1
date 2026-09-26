# Lead verification of the external reviewer's claim: v3 14-stock portfolio daily drawdown ~36% vs 26.2% reported (month-end).
import pandas as pd, numpy as np, json
LEG=r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\equity_project'
C=pd.read_pickle(LEG+r'\close10.pkl'); w=pd.Series(json.load(open(LEG+r'\conv_port.json'))['w']); w=w/w.sum()
spx=C['^GSPC']; P=C[w.index]
d=P.pct_change()
def path(fill):
    dd=d.copy()
    if fill=='zero': dd=dd.fillna(0)
    elif fill=='bkng_proxy':  # ABNB pre-IPO proxied by BKNG daily returns (travel peer) - labelled synthetic
        dd['ABNB']=dd['ABNB'].fillna(C['BKNG'].pct_change())
        dd=dd.fillna(0)
    # monthly rebalanced daily wealth
    wealth=[1.0]; cur=w.copy(); v=1.0; month=None; out=[]
    for dt,row in dd.iterrows():
        if month!=dt.month: cur=w*v; month=dt.month
        cur=cur*(1+row.values); v=cur.sum(); out.append(v)
    s=pd.Series(out,index=dd.index); return s
for fill in ['zero','bkng_proxy']:
    s=path(fill); mdd=(s/s.cummax()-1); m=s.resample('ME').last(); mmdd=(m/m.cummax()-1).min()
    print(fill,'daily maxDD %.1f%% on %s | month-end maxDD %.1f%% | COVID (2020-02-19..03-23) %.1f%% | 2022 %.1f%%'%(100*mdd.min(),mdd.idxmin().date(),100*mmdd,
      100*(s.loc['2020-03-23']/s.loc[:'2020-02-19'].iloc[-1]-1),100*(s.loc[:'2022-12-31'].iloc[-1]/s.loc[:'2021-12-31'].iloc[-1]-1)))
sp=spx.dropna(); print('S&P price index daily maxDD %.1f%% | COVID %.1f%%'%(100*(sp/sp.cummax()-1).min(),100*(sp.loc['2020-03-23']/sp.loc[:'2020-02-19'].iloc[-1]-1)))
print('ABNB first price date:',C['ABNB'].first_valid_index().date())
