from equity_class import Equity

portfolio = {}

finished = False 
while not finished:
    ticker = input("""Please enter ticker symbol or "quit" to finish: """).upper()
    if ticker == "QUIT":
        finished = True
    else:
        holding = Equity(ticker)
        symbol = holding.symbol
        portfolio[symbol] = holding

print(portfolio)