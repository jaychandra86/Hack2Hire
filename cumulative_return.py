import yfinance as yf

def getData(stock):
	amz_df = yf.download(stock, 
	                      start='2015-11-30', 
	                      end='2020-12-31', 
	                      interval='1mo',
	                      progress=False,
	)

	return amz_df


def get_cumulative(amz_df, months):
	for i in range(len(amz_df)-1, 1, -1):
	    v1 = amz_df['Adj Close'][i]
	    v2 = amz_df['Adj Close'][i - months]

	    cumulative_return=((v1-v2)/v2)*100

	    return round(cumulative_return, 2)



def getAllValues():
	m = [1, 3, 6, 12, 24, 36, 60]

	stocks = ["TSLA", "NDX"]

	tsla = []
	ndx = []

	tsla_df = getData("TSLA")
	ndx_df = getData("NDX")

	for i in m:
		tsla.append(get_cumulative(tsla_df, i))

	for i in m:
		ndx.append(get_cumulative(ndx_df, i))


	print(tsla)
	print(ndx)

	import numpy as np

	return [tsla, ndx, list(np.array(tsla) - np.array(ndx))]