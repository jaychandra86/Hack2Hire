from flask import Flask, render_template, request

import json

import getStk

import cumulative_return

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



      #Problem B: Get the monthly returns
      monthly_returns = {}

      for stock in stocks:
         l = []
         for i in range(1, len(res[stock])):

            prev = res[stock][i-1]
            cur = res[stock][i]

            if str(prev) != "nan" and str(cur) != "nan":
               s = ((cur - prev)/prev)*100
               l.append(s)

         monthly_returns[stock] = l

      #print(f"Monthly Returns: {monthly_returns}")


      #------------------------------------------------------------------------------------#
      #Problem C, get the max monthly returns and invest in that stock
      #Momentum strategy
      capital = 10000

      mr = []

      mr.append(monthly_returns[stk1])
      mr.append(monthly_returns[stk2])
      mr.append(monthly_returns[stk3])
      mr.append(monthly_returns[stk4])
      mr.append(monthly_returns[stk5])

      import numpy as np

      #uncomment these only when new data is needed
      #import rebase
      #import combined

      mon = np.array(mr)

      #print(mon)

      trans = mon
      ans = 0

      for i in trans:
         max_monthly_return = max(i)

         if str(max_monthly_return) != "nan":
            #print(capital)
            capital = capital*(1+max_monthly_return/100)


      #print(f"Momentum strategy Capital after end: {capital-10000}")


      #Vanilla strategy
      cap = [2000, 2000, 2000, 2000, 2000]
      count = 0
      for i in trans:
         count = 0
         try:
            for j in i:
               cap[count] += cap[count]*(1+j/100)
               count+=1

         except:
            break

      fin_cap = sum(cap)


      #print(f"Vanilla strategy Capital after end: {fin_cap}")

      cr = cumulative_return.getAllValues()

      for i in range(len(cr[2])):
         cr[2][i] = round(cr[2][i], 2)

      return render_template("index.html", data = [round(capital,2), round(fin_cap,2), cr])

if __name__ == '__main__':
   app.run(debug = True, port=3000)


