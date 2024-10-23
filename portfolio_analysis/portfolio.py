import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

#Starting with one holding, will expand analysis    
portfolio = ["AAPL"]


# Download historical data for a stock
adj_close = yf.download(portfolio, start='2024-09-01', end='2024-09-30')["Adj Close"]

daily_returns = adj_close.pct_change()
print(daily_returns)