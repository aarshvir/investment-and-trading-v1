import yfinance as yf, pandas as pd, json, time, sys, os, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
U=pd.read_csv('universe.csv').t.tolist()
I=json.load(open('info.json')) if os.path.exists('info.json') else {}
todo=[s for s in U if not I.get(s,{}).get('marketCap')][:int(sys.argv[1])]
def f(s):
    for k in range(2):
        try: return s,yf.Ticker(s).info
        except Exception: time.sleep(1)
    return s,{}
with ThreadPoolExecutor(20) as ex:
    for s,v in ex.map(f,todo): I[s]=v
json.dump(I,open('info.json','w'),default=str)
print('have',sum(1 for v in I.values() if v.get('marketCap')),'of',len(U))
