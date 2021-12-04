"""import yfinance as yf

# def adj_close(stk, start, end):
#     data = yf.download(stk, start = start, end = end)
#     return data['Adj Close']

# stk = 'AMZN'
# start = "2020-12-31"
# end = "2020-12-31"
# ans = adj_close(stk, start, end)
# print(ans[0])

def adj_close_multi(stks, start, end, stk):
    data = yf.download(stks, start = start, end = end, interval="1mo")
    return data['Adj Close'][stk]

stks = 'AMZN AAPL MSFT'
start = "2020-12-31"
end = "2020-12-31"
msft = adj_close_multi(stks, start, end, 'MSFT')
apl = adj_close_multi(stks, start, end, 'AAPL')
amz = adj_close_multi(stks, start, end, 'AMZN')
print("MSFT: ", msft[0])
print("APL: ", apl[0])
print("AMZN: ", amz[0])"""


import yfinance as yf
ticker = yf.Ticker('AMZN')
aapl_df = ticker.history(start='2015-12-01', end='2020-12-31', period="5y",interval='1mo')
aapl_df['Close'].plot(title="AMAZON'S stock price").show()

print(aapl_df)