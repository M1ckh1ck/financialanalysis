import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm

def d1(s, k, r, stdev, t):
    return (np.log(s / k) + (r + stdev ** 2 / 2) * t) / (stdev * np.sqrt(t))
 
def d2(s, k, r, stdev, t):
    return (np.log(s / k) + (r - stdev ** 2 / 2) * t) / (stdev * np.sqrt(t))

def BSM(s, k, r, stdev, t):
    return (s * norm.cdf(d1(s, k, r, stdev, t))) - (k * np.exp(-r * t) * norm.cdf(d2(s, k, r, stdev, t)))

pg_data = yf.download("PG", start= "2007-01-01", end= "2017-03-22")
pg_adj_close = pg_data["Adj Close"]
log_returns = np.log(1 +pg_adj_close.pct_change())
stdev = log_returns.std() * (250 ** 5
                             )
s = pg_adj_close.iloc[-1]

r = 0.025
k = 110
t = 1

print(d1(s, k, r, stdev, t))

print(d2(s, k, r, stdev, t))

print(BSM(s, k, r, stdev, t))