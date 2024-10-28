import yfinance as yf

class Equity:
    def __init__(self, ticker):
        self.ticker = ticker
        self.company_name = None
        self.price_per_share = None

    def download_data(self):
        """Download data from Yahoo Finance"""
        stock_data = yf.Ticker(self.ticker)
        info = stock_data.info

        self.company_name = info.get('longName', 'N/A')
        self.price_per_share = info.get('currentPrice', 0)

    def print_data(self):
        """Print the information from Yahoo"""
        print(f"{self.company_name} has a most recent price of {self.price_per_share}")