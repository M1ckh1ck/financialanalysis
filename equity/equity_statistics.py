from equity_class import Equity

portfolio = {}
finished = False 

while not finished:
    ticker = input("""Please enter ticker symbol? """).upper().strip()
    shares = int(input("How many shares were purchased? "))
    
    holding = Equity(ticker)
    symbol = holding.symbol
    info = {
            "equity": holding,
            "symbol": symbol,
            "shares": shares,
        }
    portfolio[symbol] = info

    another = input(
            "Would you like to add another stock? (Y/N): "
            ).upper().strip()
    
    if another == "N":
        finished = True

portfolio_value = 0

for stock in portfolio:
    shares = portfolio[stock]["shares"]
    equity = portfolio[stock]["equity"]
    price = equity.adj_close.iloc[-1]
    portfolio_value += (shares * price)

print(portfolio_value)


