import pandas as pd
from pandas_datareader.data import DataReader

def getData(stock, startDate, endDate):
	stk = DataReader(stock, "yahoo", startDate, endDate)

	return stk.groupby(pd.Grouper(freq='M'))["Adj Close"].mean()