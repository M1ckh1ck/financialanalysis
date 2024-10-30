import yfinance as yf

class Equity:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self.company_name = None
        self.price_per_share = None

    def download_information(self):
        """Download information about the company from Yahoo Finance"""
        info = self.ticker.info

        self.company_name = info.get('longName', 'N/A')
        self.price_per_share = info.get('currentPrice', 0)
        print(f"{self.company_name} has a most recent price of {self.price_per_share}")

    def download_historical_data(self, period= None, start= None, end= None, interval="1d"):
        """Download historical entering start and end date, interval set to 1 d as default"""

        interval = input("Enter interval 1mo, 1wk, 1d or 1h: ")
        date_range = input("Enter d for date range or p for period: ")

        if date_range.lower() == "p":
            period = input("Enter the period 1mo, 3mo, 1y, 5y, max: ")
            historical_data = self.ticker.history(period= period, interval= interval)
            print(historical_data)