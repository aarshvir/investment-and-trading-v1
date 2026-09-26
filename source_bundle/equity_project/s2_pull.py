import yfinance as yf, pandas as pd, pickle, os, sys, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
df=pd.read_pickle('s1.pkl'); T=df[df.short100].t.tolist()
D=pickle.load(open('deep.pkl','rb')) if os.path.exists('deep.pkl') else {}
todo=[t for t in T if t not in D or not D[t].get('ok')][:int(sys.argv[1])]
def g(fn):
    try:
        x=fn(); return x
    except Exception as e: return None
def pull(t):
    k=yf.Ticker(t); o={}
    o['q_inc']=g(lambda:k.quarterly_income_stmt); o['a_inc']=g(lambda:k.income_stmt)
    o['a_cf']=g(lambda:k.cashflow); o['a_bs']=g(lambda:k.balance_sheet); o['q_cf']=g(lambda:k.quarterly_cashflow)
    o['ed']=g(lambda:k.get_earnings_dates(limit=12)); o['trend']=g(lambda:k.eps_trend); o['rev']=g(lambda:k.eps_revisions)
    o['ee']=g(lambda:k.earnings_estimate); o['re']=g(lambda:k.revenue_estimate); o['ud']=g(lambda:k.upgrades_downgrades)
    o['ins']=g(lambda:k.insider_purchases); o['news']=g(lambda:k.news)
    o['ok']=o['a_inc'] is not None and o['q_inc'] is not None
    return t,o
with ThreadPoolExecutor(12) as ex:
    for t,o in ex.map(pull,todo): D[t]=o
pickle.dump(D,open('deep.pkl','wb'))
print('done',sum(1 for t in T if D.get(t,{}).get('ok')),'of',len(T))
