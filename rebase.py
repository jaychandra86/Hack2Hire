import yfinance as yf
amz_df = yf.download('AMZN', 
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

    monthly_return=((v1-v2)/v2)*100
    
    
    y.append((v1/first_val)*100)


js = amz_df['Adj Close'].to_string()

js = js.split("\n")

x = []

for i in js:
    if "Date" not in i:
        x.append(i[:10])


import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8, 4))

plt.plot(x[:60], y[:60])
plt.xticks(np.arange(0, len(x), 9))
plt.title("5 years peformance")
plt.xlabel("Year")
plt.ylabel("Rebased to 100")

plt.savefig("./static/rebase.png")

#plt.show()