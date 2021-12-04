from flask import Flask, render_template, request
import json
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import getStk

app = Flask(__name__)

@app.route('/s')
def home():
   return render_template("form.html")

@app.route('/get',methods = ['POST'])
def result():
   if request.method == 'POST':
      result = request.form

      stk1 = result["stock1"]
      stk2 = result["stock2"]
      stk3 = result["stock3"]
      stk4 = result["stock4"]
      stk5 = result["stock5"]

      benchmark = result["benchmark"]

      startDate = result["startdate"]
      endDate = result["enddate"]

      stocks = []
      stocks.append(stk1)
      stocks.append(stk2)
      stocks.append(stk3)
      stocks.append(stk4)
      stocks.append(stk5)
      
      res = {}

      for stock in stocks:
         res[stock] = getStk.getData(stock, startDate, endDate)



      monthly_returns = {}

      for stock in stocks:
         l = []
         for i in range(1, len(res[stock])):
            s = ((res[stock][i] - res[stock][i-1])/res[stock][i-1])*100

            l.append(s)

         monthly_returns[stock] = l
      for stock in stocks:
         ticker = yf.Ticker('stock')
         aapl_df = ticker.history(start='2015-12-01', end='2020-12-31', period="5y",interval='1mo')
         aapl_df['Rebased_to_100'].plot(title="visualisation") #rebased need to be added as column

      x = []
      y = []

      for i in range(len(monthly_returns["TSLA"])):
         x.append(i)

      import matplotlib.pyplot as plt

      plt.plot(x, monthly_returns["TSLA"])

      plt.savefig("./static/monthly_returns.png")


      print(f"Monthly Returns: {monthly_returns}")


      return render_template("index.html", data = [res, startDate])

if __name__ == '__main__':
   app.run(debug = True, port=3000)