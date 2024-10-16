import yfinance as yf
import pandas as pd

#Creating a portfolio with the tickers
portfolio = ["AAPL", "NVDA"]
weight = [0.6, 0.4]


# Download historical data for a stock
adj_close = yf.download(portfolio, start='2024-09-01', end='2024-09-30')["Adj Close"]

daily_returns = adj_close.pct_change()
daily_portoflio_return = (daily_returns * weight)

print(daily_portoflio_return)