import numpy as np 
import pandas as pd
import yfinance as yf

#Create portfolio
portfolio = ["PG"]

pfolio_data = yf.download(portfolio, start= "2024-12-09")
pfolio_data.index = pd.to_datetime(pfolio_data.index)
pfolio_adj_close = pfolio_data["Adj Close"]
log_daily_r = np.log(pfolio_adj_close / pfolio_adj_close.shift()).dropna()

print(pfolio_adj_close)
print(log_daily_r)

date = "2024-12-12"
date = pd.Timestamp(date) - pd.Timedelta(days=1)
price = 5
pfolio_adj_close.loc[date] = price
pfolio_adj_close = pfolio_adj_close[date:]
log_daily_r = np.log(pfolio_adj_close / pfolio_adj_close.shift()).dropna()

print(pfolio_adj_close)
print(log_daily_r)