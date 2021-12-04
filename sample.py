# import pandas as pd
# from pandas_datareader.data import DataReader
# ibm = DataReader('AAPL',  'yahoo', '2016-01-01', '2021-01-01')
# print(ibm.groupby(pd.Grouper(freq='M'))['Adj Close'].mean())
# monthly_adj_close = []
# for i in range(len(df)):
#     monthly_adj_close.append(df[i])
# print(*monthly_adj_close, sep = "\n")

import yfinance as yf
def forAllStocks(stcks):
    for stck in stcks:
        print(stck)
        amz_df = yf.download(stck, 
                      start='2015-12-01', 
                      end='2020-12-31', 
                      interval='1mo',
                      progress=False,
        )
# monthly_return=((amz_df['Adj Close'][1]-amz_df['Adj Close'][0])/amz_df['Adj Close'][0])*100
# print(amz_df['Adj Close'])
# print(amz_df['Adj Close'][1])
# print(amz_df['Adj Close'][0])
        time_line = [1,3,6,12,36,60]
        cum_return = []
        l = 0
        for j in time_line:
            cum_return.append(1)
            for i in range(1, j+1):
                v1 = amz_df['Adj Close'][i - 1]
                v2 = amz_df['Adj Close'][i]
                monthly_return=((v2-v1)/v1)*100
                cum_return[l] *= (1+monthly_return)    
            cum_return[l] -= 1
            l += 1

        ann_return = []; j = 0
        for i in cum_return:
            ann_return.append(0)
            p = time_line[j]/12
            ann_return[j] = (i+1)**(float(p))
            print("cum_return   " +str(i))
            print("ann_return   " + str(ann_return[j]))
            j += 1
        print("\n\n\n")

stcks = ['AAPL','AMZN','FB','TSLA','NDX']
forAllStocks(stcks)