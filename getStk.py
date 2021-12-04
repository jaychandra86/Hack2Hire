"""import pandas as pd
from pandas_datareader.data import DataReader

def getData(stock, startDate, endDate):
	stk = DataReader(stock, "yahoo", startDate, endDate)

	print(stk["Adj Close"])

	return stk["Adj Close"]
"""

import yfinance as yf


def getData(stock, startDate, endDate):
	stk_df = yf.download(stock, start=startDate, end=endDate, interval='1mo', progress=False)

	#print(stk_df['Adj Close'])

	return stk_df['Adj Close']

 

"""
for i in range(1, len(amz_df)):
    v1 = amz_df['Adj Close'][i]
    v2 = amz_df['Adj Close'][i - 1]
    monthly_return=((v1-v2)/v2)*100
    print(monthly_return)"""