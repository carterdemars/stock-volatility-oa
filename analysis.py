from functions import nLargestIndices, nSmallestIndices, percentGain
import pandas as pd
import numpy as np
import csv


output_format = "{0:.2f}"

# read in company names and ticker symbols
tickerData = list(csv.reader(open("companies.csv")))
tickers, names = ([] for i in range(2))
for row in tickerData:
    tickers.append(row[0])
    names.append(row[1])

# create dataframes
df_main = pd.read_excel("data.xlsx", index_col=None, na_values=['NA'])
df_volatility = pd.DataFrame(columns=tickers)

# EXERCISE 3A: MAXIMUM PERCENT GAIN

# initialize lists for the 10-year, 5-year and 1-year historical returns, respectively
gain10, gain5, gain1 = ([] for i in range(3))

for i in range(0, 505):

    # convert dataframe to list
    currentStock = df_main[i].tolist()

    try:
        # calculate 1, 5, and 10-year gains for each stock
        gain10.append(percentGain(currentStock, 10))
        gain5.append(percentGain(currentStock, 5))
        gain1.append(percentGain(currentStock, 1))

    except ZeroDivisionError:
        print(tickers[i], " does not have data over this timeframe")


# 10-year timeframe
maxIndices10 = nLargestIndices(gain10, 10)
print("\nThe 10 companies whose price has increased the most in the past decade are: ")
for index in maxIndices10:
    print(str(names[index]) + " increased " + str(output_format.format(gain10[index])) + "%")

# 5-year timeframe
maxIndices5 = nLargestIndices(gain5, 10)
print("\nThe 10 companies whose price has increased the most in the past 5 years are: ")
for index in maxIndices5:
    print(str(names[index]) + " increased " + str(output_format.format(gain5[index])) + "%")

# 1-year timeframe
maxIndices1 = nLargestIndices(gain1, 10)
print("\nThe 10 companies whose price has increased the most in the past 1 year are: ")
for index in maxIndices1:
    print(str(names[index]) + " increased " + str(output_format.format(gain1[index])) + "%")


# SECTION 3B AND 3C: MOST AND LEAST VOLATILE STOCKS

# calculating daily logarithmic return
for i in range(0, 505):
    df_volatility[str(tickers[i])] = (np.log(df_main[i]/df_main[i].shift(-1)))

# calculating std of daily returns, annualized for 252 trading days
volatility = []
for ticker in tickers:
    volatility.append(np.std(df_volatility[ticker]) * 252 ** 0.5)

# 10 most volatile stocks
maxIndices = nLargestIndices(volatility, 10)
print("\nThe 10 companies whose stock price is most volatile are: ")
for index in maxIndices:
    print(str(names[index]) + ":", output_format.format(volatility[index]))

# 10 least volatile stocks
minIndices = nSmallestIndices(volatility, 10)
print("\nThe 10 companies whose stock price is least volatile are: ")
for index in minIndices:
    print(str(names[index]) + ":", output_format.format(volatility[index]))
