import numpy as np 
import pandas as pd
import yfinance as yf

#Create portfolio

portfolio_value = 0
portfolio = {}

ticker = "PG"

information = yf.Ticker(ticker)
symbol = information.info.get("symbol")

pfolio_data = yf.download(ticker, start= "2024-12-09")
pfolio_data.index = pd.to_datetime(pfolio_data.index)
pfolio_adj_close = pfolio_data["Adj Close"]
log_daily_r = np.log(pfolio_adj_close / pfolio_adj_close.shift()).dropna()

date = "2024-12-12"
date = pd.Timestamp(date) - pd.Timedelta(days=1)
price = 5

pfolio_adj_close = pfolio_adj_close[date:]
pfolio_adj_close.loc[date] = price
log_daily_r = np.log(pfolio_adj_close / pfolio_adj_close.shift()).dropna()

print(symbol)