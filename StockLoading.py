
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import function as fc
import tushare as ts

# fm = r"D:\7Workspase\python\StockTrading\002415.csv"
# df = ts.get_hist_data("002415")
df = ts.get_hist_data("002142")
# print(df.head(5))

cs = df.close
cs = np.array(cs)

InitAmount = 100000.0
TotalAssets = InitAmount
MarketValue = InitAmount / 2.0  # 市值
Remaining = InitAmount / 2.0   # 剩余金额

LastTimePrice = cs[0]

#建仓
stockNum, MarketValue = fc.JianCang(cs[0], MarketValue)
Remaining = TotalAssets - MarketValue  
print("The result is:",cs[0], stockNum, MarketValue, Remaining)
#交易
for i in range(len(cs)):
    # Sell 卖
    if (cs[i] - LastTimePrice) / LastTimePrice > 0.05:
        if stockNum > 0:
            totalHand = stockNum // 100
            SellHandNum = totalHand // 4        
            leftHand = totalHand - SellHandNum
            
            MarketValue = leftHand * cs[i] * 100
            stockNum = (leftHand * 100)
            Remaining =  Remaining + SellHandNum * cs[i] * 100
            
            LastTimePrice = cs[i]
            
            print("The result of Scell is:",cs[i], stockNum,SellHandNum, MarketValue, Remaining,MarketValue+Remaining)    
           
    # Buy
    if (cs[i] - LastTimePrice) / LastTimePrice < -0.1:
        if Remaining > 0:
            availhand = int(Remaining / cs[i]) // 100
            doBuyHandNum = availhand // 4
            
            MarketValue = doBuyHandNum * 100 * cs[i] + stockNum * cs[i]
            stockNum += (doBuyHandNum * 100)
            Remaining = Remaining - doBuyHandNum * cs[i] * 100       
            print("The result of Buy is:",cs[i], stockNum,doBuyHandNum, MarketValue, Remaining,MarketValue+Remaining)
            
            LastTimePrice = cs[i]

print(MarketValue, Remaining, TotalAssets)
income = MarketValue + Remaining - TotalAssets    
    
print(income)
print("end")






