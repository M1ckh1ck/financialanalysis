import yfinance as yf
import numpy as np
import pandas as pd

#List of different signals which will be completed
#1. Moving averages 2. Relative Strength Index 3. Bollinger Bands 
#4. Stochastic Oscillators 5. Moving Average Convergence Divergence
#6. Volume 7. Average True Range 8. Fibonacci Retracement 
#9. Ichimoku Clouds 10. On-Balance Volume

ticker = "SPY"

data = yf.download(ticker, period= "5y")
data.index = pd.to_datetime(data.index)

volume = data["Volume"]

adj_close = data["Adj Close"]
simple_daily_r = ((adj_close / adj_close.shift()) - 1).dropna()
log_daily_r = np.log(adj_close / adj_close.shift()).dropna()
avg_daily_r = log_daily_r.mean()
annualised_return = avg_daily_r * 252


print()
