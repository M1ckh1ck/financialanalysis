import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

portfolio = ["PG", "MSFT", "T", "F", "GE"]
portfolio_data = yf.download(portfolio, start="2010-01-01")[["Adj Close"]]

#Normalise data to make comparable
# (portfolio_data / portfolio_data.iloc[0] * 100).plot(figsize=(15, 6))
# plt.show()

portfolio_returns = (portfolio_data/portfolio_data.shift()) - 1
annualised_portfolio = portfolio_returns.mean() * 250
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
weighted_portfolio_r = np.dot(annualised_portfolio, weights)
print(f" The weighted return is {weighted_portfolio_r *100:.2f}%")

