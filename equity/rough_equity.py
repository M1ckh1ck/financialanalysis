import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


#Create a function that gets the information from Yahoo
ticker = "PG"
price_data = yf.download(ticker, period= "10y")
price_data.index = price_data.index.date
adj_close = price_data["Adj Close"]

todays_date = (pd.to_datetime("today")).date()
three_years_ago = (pd.to_datetime('today').date() - pd.DateOffset(years=2)).date()

three_year_return = (adj_close.loc[three_years_ago] / adj_close.loc[todays_date]) -1



print(three_year_return)


# # #Calculate simple moving averages
# # moving_10_avg = mcd_data["Adj Close"].tail(10).mean()
# # moving_20_avg = mcd_data["Adj Close"].tail(20).mean()
# # moving_30_avg = mcd_data["Adj Close"].tail(30).mean()

# # print(f"Moving average for 10 days is {moving_10_avg: .4f}, 20 days is {moving_20_avg: .4f}, 30 days is {moving_30_avg: .4f}")

# #Future calcultaion exponential moving average, relative strentgth index, Stochastic Oscillator, Volume


# # portfolio = ["PG", "MSFT", "T", "F", "GE"]
# # data = yf.download(portfolio, start="2010-01-01")
# # adj_close = data["Adj Close"]

# # Save the adjusted close data to a CSV file
# #adj_close.to_csv("python_for_finance/portfolio_data.csv")

# #Creating a simple return column in the array 
# # pg_data = yf.download("PG", start= "2010-01-01")
# # pg_data["simple_return"] = (pg_data["Adj Close"] / pg_data["Adj Close"].shift()) -1

# #Calculating average daily and daiy annulised return
# # pg_avg_daily_r = pg_data["simple_return"].mean()
# # print(pg_avg_daily_r)
# # pg_avg_daily_a = pg_data["simple_return"].mean() * 250
# # print(pg_avg_daily_a)

# #Plotting the daily returns on a graph
# # plt.figure(figsize= (8,5))
# # plt.plot(pg_data["simple_return"], linewidth= 0.6)
# # plt.title("PG Daliy Simple Returns", fontsize=14)
# # plt.xlabel("Date", fontsize=12)
# # plt.ylabel("% Daliy Return", fontsize=12)
# # plt.legend(fontsize=10)
# # plt.show()

# pg_data["log_return"] = np.log(pg_data["Adj Close"] / pg_data["Adj Close"].shift())
# pg_avg_daily_r = pg_data["log_return"].mean()
# print(pg_avg_daily_r)
# pg_avg_daily_a = pg_data["log_return"].mean() * 250
# print(pg_avg_daily_a)

# plt.figure(figsize= (8,5))
# plt.plot(pg_data["log_return"], linewidth= 0.6)
# plt.title("PG Daliy Log Returns", fontsize=14)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("% Daliy Return", fontsize=12)
# plt.legend(fontsize=10)
# plt.show()

# portfolio = ["PG", "MSFT", "T", "F", "GE"]
# portfolio_data = yf.download(portfolio, start="2010-01-01")[["Adj Close"]]

# #Normalise data to make comparable
# # (portfolio_data / portfolio_data.iloc[0] * 100).plot(figsize=(15, 6))
# # plt.show()

# portfolio_returns = (portfolio_data/portfolio_data.shift()) - 1
# annualised_portfolio = portfolio_returns.mean() * 250
# weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
# weighted_portfolio_r = np.dot(annualised_portfolio, weights)
# print(f" The weighted return is {weighted_portfolio_r *100:.2f}%")


# #Monte Carlo simulation for gross profit
# # rev_mean = 170
# # rev_stdev = 20
# # iterations = 1000

# # rev = np.random.normal(rev_mean, rev_stdev, iterations)
# # cogs = rev * np.random.normal(0.6, 0.1)
# # gross_profit = rev - cogs

# # plt.figure(figsize= (15, 6))
# # plt.plot(gross_profit)
# # plt.show()

# # plt.figure(figsize= (15, 6))
# # plt.hist(gross_profit, bins= 20)
# # plt.show()

# #Download price data for PG
# pg_data = yf.download("PG", start= "2007-01-01", end= "2017-01-01")
# pg_adj_close = pg_data["Adj Close"]

# #Two different ways to calculate returns 
# pg_returns = np.log(pg_adj_close / pg_adj_close.shift())
# pg_returns = np.log(1 + pg_adj_close.pct_change())

# #Calculate drift element
# mean_return = pg_returns.mean()
# var_return = pg_returns.var()

# drift = mean_return - (0.5 * var_return)
# drift = np.array(drift)
# stdev_return = pg_returns.std()
# stdev_return = np.array(stdev_return)

# #Creating a matrix for the different possible scenarios 
# t_intervals = 1000
# iterations = 10
# daily_return = np.exp(drift + stdev_return * norm.ppf(np.random.rand(t_intervals, iterations)))

# #Looping through the different pathways 
# s0 = pg_adj_close.iloc[-1]
# price_list = np.zeros_like(daily_return)
# price_list[0] = s0

# for t in range (1, t_intervals):
#     price_list[t] = price_list[t - 1] * daily_return[t]

# #Plotting the 10 different simulations 
# plt.figure(figsize= (10, 6))
# plt.plot(price_list)
# plt.show()



# data = pd.read_excel("python_for_finance/Housing.xlsx")


# y = data["House Price"]
# x = data[["House Size (sq.ft.)", "Number of Rooms", "Year of Construction"]]

# # plt.scatter(x, y)
# # plt.xlim(0, 2500)
# # plt.ylim(0, 1500000)
# # plt.ylabel('House Price')
# # plt.xlabel('House Size (sq.ft)')
# # plt.show()

# x0 = sm.add_constant(x)
# regression = sm.OLS(y, x0).fit()


# print(regression.summary())


# pg_data = yf.download("PG", start= "2007-01-01", end= "2017-03-22")
# pg_adj_close = pg_data["Adj Close"]

# log_returns = np.log(1 +pg_adj_close.pct_change())
# stdev = log_returns.std() * (250 ** 5)
# stdev = np.array(stdev)

# r = 0.025
# t = 1.0
# t_intervals = 250
# delta_t = t / t_intervals

# iterations = 10000

# s = pg_adj_close.iloc[-1]

# Z = np.random.standard_normal((t_intervals + 1, iterations))  
# S = np.zeros_like(Z) 
# S0 = pg_adj_close.iloc[-1]  
# S[0] = S0

# for t in range(1, t_intervals + 1):
#     S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])

# print(S.shape)

# plt.figure(figsize=(10, 6))
# plt.plot(S[:, :10])
# plt.show()

# data = pd.read_csv("python_for_finance/MSFT_AAPL_2000_2017.csv")

# data["Date"] = pd.to_datetime(data["Date"])
# data.set_index("Date", inplace= True)

# daily_returns = np.log(data / data.shift())
# weights = np.array([0.5, 0.5])

# avg_daily_return = daily_returns["MSFT"].mean()
# annualised_return = daily_returns["MSFT"].mean() * 250
# daily_std = daily_returns["MSFT"].std()
# annualised_std = daily_returns["MSFT"].std() * (np.sqrt(250))

# aapl_var = daily_returns["AAPL"].var()
# aapl_var_a = daily_returns["AAPL"].var() * 250
# msft_var = daily_returns["MSFT"].var()
# msft_var_a = daily_returns["MSFT"].var() * 250


# cov_matrix = daily_returns.cov()
# cov_matrix_a = daily_returns.cov() * 250
# corr_matrix = daily_returns.corr()

# portfolio_var = np.dot(weights.T, np.dot(daily_returns.cov() * 250, weights))
# print(portfolio_var)

# #Importing PG and S&P return information and indexing the dates
# data = pd.read_csv("python_for_finance/Markowitz_Data.csv")
# data["Date"] = pd.to_datetime(data["Date"])
# data.set_index("Date", inplace= True)

# # Plotting the normalised daily returns on a graph
# # ((data / data.iloc[0]) * 100).plot(figsize= (8,5))
# # plt.legend(fontsize=10)
# # plt.show()

# #Analysis price data, effeicient frontier
# log_returns = np.log(data / data.shift())

# annual_returns = log_returns.mean() * 250
# covariance = log_returns.cov() * 250
# correlation = log_returns.corr()

# #Calculate random weighting of the assets
# number_assets = len(data.columns)
# weights = np.random.random(number_assets)
# weights /= np.sum(weights)

# #Calculate expected return, variance and volatility 
# expected_return = np.sum(weights * log_returns.mean()) * 250
# expected_var = np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# expected_vol = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))

# #Run 1,000 scenarios with random portfolio weightings
# pfolio_returns = []
# pfolio_vol = []

# for x in range(1000): 
#     number_assets = len(data.columns)
#     weights = np.random.random(number_assets)
#     weights /= np.sum(weights)

#     pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
#     pfolio_vol.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))

# pfolio_returns = np.array(pfolio_returns)
# pfolio_vol = np.array(pfolio_vol)

# portfolios = pd.DataFrame({"Return": pfolio_returns, "Volatility": pfolio_vol})

# print(portfolios.index)

# plt.figure(figsize=(10, 4))
# plt.scatter(portfolios["Volatility"], portfolios["Return"], alpha=0.5, c="blue", s= 2)
# plt.title("Efficient Frontier")
# plt.xlabel("Expected Volatility")
# plt.ylabel("Expected Returns")
# plt.show()

# #Create portfolio
# portfolio = ["PG", "^GSPC"]

# #Download required data for analysis, and create a DataFrame for Adjust Close
# pfolio_data = yf.download(portfolio, start= "2012-1-1", end= "2016-12-31")
# pfolio_adj_close = pfolio_data["Adj Close"]

# #Calculate daily returns and annualised Covariance
# pfolio_returns = np.log( pfolio_adj_close / pfolio_adj_close.shift())
# pfolio_cov = pfolio_returns.cov() * 250
# cov_market = pfolio_cov.iloc[0, 1]

# market_var = pfolio_returns["^GSPC"].var() * 250

# pg_beta = cov_market / market_var

# #Downloading 10 year yield to be used as the risk free rate
# ten_year_info = yf.Ticker("^TNX").info
# ten_year_yield = ten_year_info.get("previousClose", "N/A") /100

# market_return = pfolio_returns["^GSPC"].mean() * 250

# pg_capm = ten_year_yield + pg_beta * (market_return - ten_year_yield)


# #Sharp Ratio
# pg_std = pfolio_returns["PG"].std() * (250 ** 0.5)

# sharp_ratio = (pg_capm - ten_year_yield) / pg_std


# print(sharp_ratio)