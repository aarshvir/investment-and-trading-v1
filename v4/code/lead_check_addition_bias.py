# Lead's own verification: how much of v3's 10-yr momentum result (bt10.py: 29.1% CAGR) comes from
# look-ahead bias — ranking stocks at dates BEFORE they were added to the S&P 500.
import pandas as pd, numpy as np, requests, io, pickle, warnings
warnings.filterwarnings('ignore')
LEG=r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\equity_project'
C=pd.read_pickle(LEG+r'\close10.pkl').ffill(); spx=C.pop('^GSPC')
html=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',headers={'User-Agent':'Mozilla/5.0 (research)'},timeout=60).text
t=pd.read_html(io.StringIO(html))[0]; t['t']=t['Symbol'].str.replace('.','-',regex=False)
added=pd.to_datetime(t.set_index('t')['Date added'],errors='coerce')
M=C.resample('ME').last(); R=M.pct_change()
mom=M.shift(1)/M.shift(12)-1
def run(restrict):
    rets=[];names=[]
    for i in range(13,len(M)-1):
        d=M.index[i]; s=mom.iloc[i].dropna()
        if restrict: s=s[[x for x in s.index if (x in added.index and pd.notna(added[x]) and added[x]<=d)]]
        pick=s.nlargest(50).index; rets.append(R.iloc[i+1][pick].mean()); names.append(len(s))
    r=pd.Series(rets,index=M.index[14:]); eq=(1+r).cumprod(); yrs=len(r)/12
    return eq.iloc[-1]**(1/yrs)-1, r.std()*np.sqrt(12), (eq/eq.cummax()-1).min(), np.mean(names)
def ew(restrict):
    rets=[]
    for i in range(13,len(M)-1):
        d=M.index[i]; cols=[x for x in M.columns if (not restrict) or (x in added.index and pd.notna(added[x]) and added[x]<=d)]
        rets.append(R.iloc[i+1][cols].mean())
    r=pd.Series(rets); eq=(1+r).cumprod(); return eq.iloc[-1]**(12/len(r))-1
a=run(False); b=run(True)
print('Momentum top50, today\'s constituents (v3 method): CAGR %.1f%% vol %.1f%% maxDD %.1f%% avg universe %d'%(100*a[0],100*a[1],100*a[2],a[3]))
print('Momentum top50, only stocks already in index at t:  CAGR %.1f%% vol %.1f%% maxDD %.1f%% avg universe %d'%(100*b[0],100*b[1],100*b[2],b[3]))
print('EW universe today\'s constituents: %.1f%%   EW only already-added: %.1f%%'%(100*ew(False),100*ew(True)))
late=added[added>'2016-09-30'].sort_values(); print('current members added after Sep-2016:',len(late)); print(late.tail(25).to_string())
