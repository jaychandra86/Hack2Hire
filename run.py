from flask import Flask, render_template, request

import getStock

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

      


      stockStr = stk1 + " " + stk2 + " " + stk3 + " " + stk4 + " " + stk5

      stocks = []
      stocks.append(stk1)
      stocks.append(stk2)
      stocks.append(stk3)
      stocks.append(stk4)
      stocks.append(stk5)

      #print(stockStr)
      #print(stocks)

      #this gets the stock data
      stockData = getStock.adj_close_multi(stockStr, startDate, endDate)
      

      res = {}

      for stock in stocks:
         res[stock] = stockData["Adj Close"][stock]

      print(res)


      return render_template("index.html", data = [res, startDate])

if __name__ == '__main__':
   app.run(debug = True, port=3000)