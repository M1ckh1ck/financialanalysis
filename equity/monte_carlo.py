import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm


#Download price data for PG
pg_data = yf.download("PG", start= "2007-01-01", end= "2017-01-01")
pg_adj_close = pg_data["Adj Close"]

#Two different ways to calculate returns 
pg_returns = np.log(pg_adj_close / pg_adj_close.shift())
pg_returns = np.log(1 + pg_adj_close.pct_change())

#Calculate drift element
mean_return = pg_returns.mean()
var_return = pg_returns.var()

drift = mean_return - (0.5 * var_return)
drift = np.array(drift)
stdev_return = pg_returns.std()
stdev_return = np.array(stdev_return)

#Creating a matrix for the different possible scenarios 
t_intervals = 1000
iterations = 10
daily_return = np.exp(drift + stdev_return * norm.ppf(np.random.rand(t_intervals, iterations)))

#Looping through the different pathways 
s0 = pg_adj_close.iloc[-1]
price_list = np.zeros_like(daily_return)
price_list[0] = s0

for t in range (1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_return[t]

#Plotting the 10 different simulations 
plt.figure(figsize= (10, 6))
plt.plot(price_list)
plt.show()