import pandas as pd
import csv
import yfinance as yf
import numpy as np
from yahoofinancials import YahooFinancials


# import current tickers into list
tickerData = list(csv.reader(open("companies.csv")))

tickers = []
for row in tickerData:
    tickers.append(row[0])


gain = []
data = []
i = 0

for ticker in tickers:

    stockData = yf.Ticker(ticker)
    currentStock = stockData.history(period="10y")

    price = []
    for item in currentStock['Close']:
        price.append(item)

    data.append(price)
    print(i, ticker)
    i += 1

df = pd.DataFrame(data).T
df.to_excel(excel_writer="/Users/carterdemars/Desktop/backup/data.xlsx")