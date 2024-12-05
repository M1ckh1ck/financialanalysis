import pandas as pd
import yfinance as yf

portfolio = ["PG", "AAPL"]
price_data = yf.download(portfolio, period= "1y")
price_data.index = pd.to_datetime(price_data.index)

adj_close = price_data["Adj Close"]

print(adj_close)
