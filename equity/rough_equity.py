from equity_class import Equity
import pandas as pd

ticker = input("What is the ticker you would like to look up? ")
equity = Equity(ticker)

equity.download_historical_data()
print(equity.historical_data)

mcd_data = pd.read_csv("finance_projects/financialanalysis/portfolio_analysis/mcd_data.csv")

max_close = mcd_data["Adj Close"].max()

#Calculate simple moving averages
moving_10_avg = mcd_data["Adj Close"].tail(10).mean()
moving_20_avg = mcd_data["Adj Close"].tail(20).mean()
moving_30_avg = mcd_data["Adj Close"].tail(30).mean()

print(f"Moving average for 10 days is {moving_10_avg: .4f}, 20 days is {moving_20_avg: .4f}, 30 days is {moving_30_avg: .4f}")

# #Future calcultaion exponential moving average, relative strentgth index, Stochastic Oscillator, Volume