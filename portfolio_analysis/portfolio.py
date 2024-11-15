import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

portfolio = []

def create_portfolio():
    portfolio = []
    another_ticker = True
    while another_ticker:
        ticker = input("What is the ticker symbol? Type quit to finish: ").lower()
        if ticker == "quit":
            break
        portfolio.append(ticker)
    return portfolio

weights = []
for ticker in range(len(portfolio)):
    weight = float(input("What is the weight of the holding in decimals? "))
    weights.append(weight)

print(weights)

create_portfolio()