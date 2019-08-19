'''
Created on 2019年8月11日

@author: HuangYuliang
'''
import tushare as ts
import numpy as np
import matplotlib.pyplot as plt

class Stock():
    def __init__(self, name):    
        self.name = name
        self.date = 0.0
        self.stockHistData = []
        self.curPrice = 0
        self.marketMoney = 0
        self.stockNum = 0
        self.stockHands = 0
        self.longOfStockHistData = 0
        self.maxAverMinMonth = [0.0,0.0,0.0]
        self.maxAverMinWeek = [0.0,0.0,0.0]
        
    def getStockHistData(self):
        df = ts.get_hist_data(self.name)  
        self.stockHistData = list(np.array(df.close))
        self.stockHistData.reverse()
        self.longOfStockHistData = len(self.stockHistData)
        plt.plot(list(range(self.longOfStockHistData)),self.stockHistData)
        
    def calcStockNumAfterBuyAndReturnBoughtMoney(self, money):
        num = int(money // self.curPrice)
        if num < 100:
            print("Money are not enough, Buy none!")
            return 0
        else:
            hands = num // 100
            self.stockNum += hands * 100
            return hands * 100 * self.curPrice
    
    def calcStockNumAfterSellAndReturnSelledHands(self, hands):
        if hands * 100 > self.stockNum:
            print("stockNum are not enougth, Sell none!")
            return 0
        else:
            self.stockNum -= hands * 100
            return hands
        
    def updateCurPrice(self,date):
        self.date = date
        self.curPrice = self.stockHistData[date]
    
    def updateStockInfo(self):
        self.stockHands = self.stockNum // 100
        self.marketMoney = self.stockNum * self.curPrice
    
    def updateStockStatisticsInfo(self, date, week, month):
        if date > week-1:
            self.maxAverMinWeek[0] = max(self.stockHistData[date-week:date:])
            self.maxAverMinWeek[1] = np.average(self.stockHistData[date-week:date:])
            self.maxAverMinWeek[2] = min(self.stockHistData[date-week:date:])
        if date > month-1:
            self.maxAverMinMonth[0] = max(self.stockHistData[date-month:date:])
            self.maxAverMinMonth[1] = np.average(self.stockHistData[date-month:date:])
            self.maxAverMinMonth[2] = min(self.stockHistData[date-month:date:])
        
    def showStockInfor(self):
        print("maxAverMinMonth:{}, maxAverMinWeek:{}".format(self.maxAverMinMonth, self.maxAverMinWeek))
        print("date:{}, curPrice:{:.2f}, stockHands:{}, stockNum:{}, markMoney:{:.2f} ".format(
            self.date, self.curPrice, self.stockHands, self.stockNum, self.marketMoney))
             

       
