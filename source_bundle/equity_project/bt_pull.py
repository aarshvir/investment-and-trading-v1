import yfinance as yf, pandas as pd, pickle, os, sys, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
U=pd.read_pickle('s1.pkl').t.tolist()
F=pickle.load(open('fund_all.pkl','rb')) if os.path.exists('fund_all.pkl') else {}
todo=[t for t in U if t not in F][:int(sys.argv[1])]
def g(t):
    k=yf.Ticker(t); o={}
    for nm,fn in [('inc',lambda:k.income_stmt),('bs',lambda:k.balance_sheet),('cf',lambda:k.cashflow)]:
        try: o[nm]=fn()
        except Exception: o[nm]=None
    return t,o
with ThreadPoolExecutor(20) as ex:
    for t,o in ex.map(g,todo): F[t]=o
pickle.dump(F,open('fund_all.pkl','wb')); print('have',len(F),'of',len(U))
