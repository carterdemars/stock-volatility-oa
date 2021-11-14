import pandas as pd

def percentGain(prices, period):

    pIndex = -1
    lastPrice = prices[pIndex]

    if (period >= 10):
        return (lastPrice/prices[0]*100.0)
    else:
        return (lastPrice/prices[-period*252]*100.0)

def nLargestIndices(values,n):
    temp = pd.Series(values)
    i = temp.nlargest(n)
    return i.index.values.tolist()

def nSmallestIndices(values,n):
    temp = pd.Series(values)
    i = temp.nsmallest(n)
    return i.index.values.tolist()