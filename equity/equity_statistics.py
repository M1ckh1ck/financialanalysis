import yfinance as yf

pg_data = yf.download("PG", start= "2010-01-01")

pg_data["simple_return"] = (pg_data["Adj Close"] / pg_data["Adj Close"].shift()) -1

#Calculating average daily and daiy annulised return

avg_daily_return = pg_data["simple_return"].mean()
annualised_daily_return = pg_data["simple_return"].mean() * 250



