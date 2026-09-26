import yfinance as yf, pandas as pd, pickle, os, sys, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
U=pd.read_pickle('s1.pkl').t.tolist(); D=pickle.load(open('deep.pkl','rb'))
E=pickle.load(open('est_all.pkl','rb')) if os.path.exists('est_all.pkl') else {}
for t in U:
    if t in D and t not in E: E[t]=dict(trend=D[t]['trend'],rev=D[t]['rev'],ed=D[t]['ed'],ud=D[t]['ud'])
todo=[t for t in U if t not in E][:int(sys.argv[1])]
def g(t):
    k=yf.Ticker(t); o={}
    for nm,fn in [('trend',lambda:k.eps_trend),('rev',lambda:k.eps_revisions),('ed',lambda:k.get_earnings_dates(limit=12)),('ud',lambda:k.upgrades_downgrades)]:
        try: o[nm]=fn()
        except Exception: o[nm]=None
    return t,o
with ThreadPoolExecutor(16) as ex:
    for t,o in ex.map(g,todo): E[t]=o
pickle.dump(E,open('est_all.pkl','wb')); print('have',len(E))
