'''
Created on 2019年8月11日

@author: HuangYuliang
'''
import tushare as ts
import numpy as np

class Stock():
    def __init__(self, name):    
        self.name = name
        self.stockHistData = []
        self.curPrice = 0
        self.marketMoney = 0
        self.stockNum = 0
        self.stockHands = 0
        self.longOfStockHistData = 0
        
    def getStockHistData(self):
        df = ts.get_hist_data(self.name)  
        self.stockHistData = list(np.array(df.close))
        self.stockHistData.reverse()
        
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
        self.curPrice = self.stockHistData[date]
    
    def updateStockInfo(self):
        self.stockHands = self.stockNum // 100
        self.marketMoney = self.stockNum * self.curPrice
        
    def showStockInfor(self):
        print("curPrice:{:.2f}, stockHands:{}, stockNum:{}, markMoney:{:.2f} ".format(
                self.curPrice, self.stockHands, self.stockNum, self.marketMoney))
             

       
    
    
    
    
    