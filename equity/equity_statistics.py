from equity_class import Equity
import pandas as pd

portfolio_value = 0
portfolio = {}
finished = False 

while not finished:
    ticker = input("""Please enter ticker symbol? """).upper().strip()
    #shares = int(input("How many shares were purchased? "))
    date = input("""What date were the shares purchased? (YYYY-MM-DD): """)
    date = pd.Timestamp(date) - pd.Timedelta(days=1)

    holding = Equity(ticker)
    symbol = holding.symbol

    portfolio[symbol] = holding

    another = input(
            "Would you like to add another stock? (Y/N): "
            ).upper().strip()
    
    if another == "N":
        finished = True

portfolio_data = pd.DataFrame()

for stock in portfolio:
    equity = portfolio[stock]
    price_data = equity.adj_close
    price_data = price_data[date:]
    portfolio_data = pd.concat([portfolio_data, price_data], axis=1)


 