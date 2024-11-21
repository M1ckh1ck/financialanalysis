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
price_data.index = pd.to_datetime(price_data.index)
adj_close = price_data["Adj Close"]

def time_horizon_return():
    """Function to calculate the return of the stock over different time horizons"""

    time_horizon = int(input("What is the time horizon you would like the return calculate? "))

    todays_date = (pd.to_datetime("today"))
    if todays_date not in adj_close.index:
        todays_date = adj_close.index[adj_close.index < todays_date].max()

    previous_date = (todays_date - pd.DateOffset(years= time_horizon))
    if previous_date not in adj_close.index:
        previous_date = adj_close.index[adj_close.index < previous_date].max()

    time_horizon_return = (adj_close.loc[todays_date] / adj_close.loc[previous_date]) - 1

    print(f"{ticker} returned {time_horizon_return * 100:.2f}% over {time_horizon} years")


def moving_averages():
    """Calculate the moving averge"""
    number_of_days = int(input("What number of days would you like the running average? "))
    moving_avg = adj_close.tail(number_of_days).mean()
    print(f"{ticker} had a {number_of_days} moving average of {moving_avg} days.")

def average_return():
    """Calculating average daily and daily annulised return"""
    daily_r = np.log(adj_close / adj_close.shift())
    avg_daily_r = daily_r.mean() * 250
    annualised_return = avg_daily_r
    return annualised_return

def download_data(ticker, period= "10y"):
    """Download price data for the given ticker"""
    price_data = yf.download(ticker, period= period)
    price_data.index = pd.to_datetime(price_data.index)
    adj_close = price_data["Adj Close"]
    return adj_close

def calc_beta(ticker, benchmark= "^GSPC"):
    """Calculate the beta of a given stock against it's benchmark"""
    price_data = pd.concat([download_data(ticker, "5y"), download_data(benchmark, "5y")], axis= 1)
    price_data.columns = [ticker, benchmark]

    daily_return = np.log(price_data / price_data.shift())
    daily_return = daily_return.dropna()

    cov = np.cov(daily_return[ticker], daily_return[benchmark])[0][1]
    market_var = np.var(daily_return[benchmark])
    beta = cov / market_var
    return beta

def calc_capm(ticker):
    """Calculate CAPM for a give stock"""
    ten_year_info = yf.Ticker("^TNX").info
    ten_year_yield = ten_year_info.get("previousClose", "N/A") /100
    market_data = download_data("^GSPC")
    market_return_d = np.log(market_data / market_data.shift())
    market_return_a = market_return_d.mean() * 250
    capm = ten_year_yield + calc_beta(ticker) * (market_return_a - ten_year_yield)
    return capm

def calc_sharp_ratio(ticker):
    data = download_data(ticker)
    daily_return = np.log(data / data.shift())
    stdev = daily_return.std() * (250 ** 0.5)

    ten_year_info = yf.Ticker("^TNX").info
    ten_year_yield = ten_year_info.get("previousClose", "N/A") /100

    capm = calc_capm(ticker)

    sharp_ratio = (capm - ten_year_yield) / stdev
    return sharp_ratio

# #Future calcultaion exponential moving average, relative strentgth index, Stochastic Oscillator, Volume
