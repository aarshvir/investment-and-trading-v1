"""Current covariance and portfolio sensitivity from archived raw Yahoo responses."""

import json
import pathlib
import zipfile

import numpy as np

OUT = pathlib.Path(__file__).resolve().parent
ROOT = OUT.parents[3]
stresses = json.loads((OUT / "stress_diagnostics.json").read_text(encoding="utf-8"))
swaps = json.loads((OUT / "defensive_swap_diagnostics.json").read_text(encoding="utf-8"))
slate = stresses["proposed_concentration"]["stock_weight_pct"]
prior = stresses["v011_concentration"]["stock_weight_pct"]
equal = {ticker: 100 / len(slate) for ticker in slate}
double_defensive = swaps["variants"]["HIG_AMP_to_PG_PEP"]["weights"]
triple_defensive = swaps["variants"]["HIG_AMP_USB_to_PG_PEP_PEG"]["weights"]


def read_prices(ticker):
    data = json.loads((OUT / "raw_yahoo" / f"{ticker}.json").read_text(encoding="utf-8"))["chart"]["result"][0]
    from datetime import datetime, timezone
    return {datetime.fromtimestamp(ts, timezone.utc).date().isoformat(): value
            for ts, value in zip(data["timestamp"], data["indicators"]["adjclose"][0]["adjclose"])
            if value is not None and value > 0}


prices = {ticker: read_prices(ticker) for ticker in set(slate) | set(prior) | set(triple_defensive) | {"SPY"}}
dates = sorted(set.intersection(*(set(x) for x in prices.values())))
dates = [d for d in dates if "2023-09-25" <= d <= "2026-09-25"]
rets = {}
for ticker, series in prices.items():
    values = np.array([series[d] for d in dates], dtype=float)
    rets[ticker] = values[1:] / values[:-1] - 1
spy = rets["SPY"]
spy_var = spy.var(ddof=1)


def profile(weights):
    tickers = list(weights)
    w = np.array([weights[t] / 100 for t in tickers], dtype=float)
    matrix = np.vstack([rets[t] for t in tickers]).T
    portfolio = matrix @ w
    cov = np.cov(matrix, rowvar=False, ddof=1)
    vol = float(np.std(portfolio, ddof=1) * np.sqrt(252))
    beta = float(np.cov(portfolio, spy, ddof=1)[0, 1] / spy_var)
    tracking = float(np.std(portfolio - spy, ddof=1) * np.sqrt(252))
    risk = (w * (cov @ w)) / (w @ cov @ w)
    total = np.ones_like(cov, dtype=bool)
    np.fill_diagonal(total, False)
    sd = np.sqrt(np.diag(cov))
    corr = cov / np.outer(sd, sd)
    return {"annualized_volatility": vol, "beta_to_spy": beta,
            "annualized_tracking_error": tracking,
            "average_pairwise_correlation": float(corr[total].mean()),
            "largest_risk_contributions": sorted(zip(tickers, risk.tolist()), key=lambda x: -x[1])[:8],
            "effective_risk_bets": float(1 / np.square(risk).sum()),
            "daily_observations": len(portfolio)}


result = {"sample_start": dates[0], "sample_end": dates[-1],
          "same_data_all_comparisons": True,
          "proposed": profile(slate), "equal_weight_same_20": profile(equal),
          "double_defensive": profile(double_defensive),
          "triple_defensive": profile(triple_defensive),
          "v011": profile(prior),
          "warning": "Trailing historical covariance for present survivors, not forecast variance, stress floor or calibrated loss odds. Adjusted closes exclude investor-specific withholding and costs."}
(OUT / "covariance_diagnostics.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
