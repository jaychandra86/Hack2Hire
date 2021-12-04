import yfinance as yf


def getData(stock):
    amz_df = yf.download(stock, 
                          start='2015-11-30', 
                          end='2020-12-31', 
                          interval='1mo',
                          progress=False,
    )


    first_val = amz_df['Adj Close'][0]

    y = []

    for i in range(1, len(amz_df)):

        v1 = amz_df['Adj Close'][i]
        v2 = amz_df['Adj Close'][i - 1]


        if str(v1) != "nan" and str(v2) != "nan":
            monthly_return=((v1-v2)/v2)*100
        
        
            y.append((v1/first_val)*100)


    js = amz_df['Adj Close'].to_string()

    js = js.split("\n")

    x = []

    for i in js:
        if "Date" not in i:
            x.append(i[:10])


    return (x,y)


stocks = ["AMZN", "AAPL", "MSFT", "TSLA", "FB", "NDX"]

X = []
Y = []

for i in stocks:
    x,y = getData(i)
    X.append(x)
    Y.append(y)

import matplotlib.pyplot as plt

#plot this


plt.figure(figsize = (8, 4))

plt.show()
