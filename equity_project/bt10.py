# 10-YEAR PRICE-FACTOR BACKTEST (monthly rebalance, top 50 equal weight) — tests which style can clear 15%
import pandas as pd, numpy as np, json
C=pd.read_pickle('close10.pkl').ffill(); spx=C.pop('^GSPC')
M=C.resample('ME').last(); Ms=spx.resample('ME').last()
R=M.pct_change(); Rs=Ms.pct_change()
D=C.pct_change()
vol=D.rolling(252).std().resample('ME').last()*np.sqrt(252)
mom12_1=M.shift(1)/M.shift(12)-1; mom6=M/M.shift(6)-1
sma200=C.rolling(200).mean().resample('ME').last(); hi=C.rolling(252).max().resample('ME').last()
trend=((M>sma200).astype(int)+(M/hi>0.75).astype(int))
def pr(x): return x.rank(axis=1,pct=True)
S={'Momentum (12-1)':pr(mom12_1),'Low volatility':pr(-vol),'Momentum + low vol':(pr(mom12_1)+pr(-vol))/2,
   'Momentum + trend, vol-capped':pr(mom12_1).where(vol<0.45)+0.25*trend,'Equal-weight universe':pr(M*0+1)}
out={}
for k,sc in S.items():
    rets=[]
    for i in range(13,len(M)-1):
        s=sc.iloc[i].dropna()
        if k=='Equal-weight universe': pick=s.index
        else: pick=s.nlargest(50).index
        rets.append(R.iloc[i+1][pick].mean())
    r=pd.Series(rets,index=M.index[14:])
    eq=(1+r).cumprod(); r12=(1+r).rolling(12).apply(np.prod,raw=True)-1
    yrs=len(r)/12
    out[k]=dict(cagr=float(eq.iloc[-1]**(1/yrs)-1),vol=float(r.std()*np.sqrt(12)),mdd=float((eq/eq.cummax()-1).min()),
      p15=float((r12.dropna()>=0.15).mean()),p25=float((r12.dropna()>=0.25).mean()),p50=float((r12.dropna()>=0.50).mean()),ploss20=float((r12.dropna()<=-0.20).mean()),
      worst12=float(r12.min()),y2022=float((1+r['2022']).prod()-1),y2020=float((1+r['2020-02':'2020-03']).prod()-1))
rs=Rs.iloc[14:]; eq=(1+rs).cumprod(); r12=(1+rs).rolling(12).apply(np.prod,raw=True)-1; yrs=len(rs)/12
out['S&P 500']=dict(cagr=float(eq.iloc[-1]**(1/yrs)-1),vol=float(rs.std()*np.sqrt(12)),mdd=float((eq/eq.cummax()-1).min()),p15=float((r12.dropna()>=0.15).mean()),p25=float((r12.dropna()>=0.25).mean()),p50=float((r12.dropna()>=0.5).mean()),ploss20=float((r12.dropna()<=-0.2).mean()),worst12=float(r12.min()),y2022=float((1+rs['2022']).prod()-1),y2020=float((1+rs['2020-02':'2020-03']).prod()-1))
json.dump(out,open('bt10.json','w'))
print(pd.DataFrame(out).T.round(3).to_string())
