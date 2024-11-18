import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

portfolio = []
another_ticker = True
while another_ticker:
    ticker = input("What is the ticker symbol? Type quit to finish: ").lower()
    if ticker == "quit":
        break
    portfolio.append(ticker)

weights = []

for ticker in range(len(portfolio)):
    weight = float(input("What is the weight of the holding in decimals? "))
    weights.append(weight)

weight_array = np.array(weights)

portfolio_data = yf.download(portfolio, start= "2010-01-01")

port_daily_return = (portfolio_data["Adj Close"] / portfolio_data["Adj Close"].shift()) - 1
annualised_return = port_daily_return.mean() * 250
weighted_return = np.dot(annualised_return, weight_array)