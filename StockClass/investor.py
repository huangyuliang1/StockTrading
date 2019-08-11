'''
Created on 2019年8月11日

@author: HuangYuliang
'''
from stock import Stock
import tushare as ts
import numpy as np

class Investor():
    def __init__(self, money):
        self.totalManey = money
        self.cost = money
        self.profit = 0
        self.marketMoney = 0
        self.freeMoney = money
        self.money2Buy = 0
        self.moneyfromSell = 0
        
        self.stockList = []
          
    def jianCang(self,strStockName, date):
        print("JianCanging...")
        self.stok1 = Stock(strStockName)
        self.stockList.append(self.stok1)
     
        self.stok1.stockHistData = self.getStockHistData(strStockName)
        self.stok1.updateCurPrice(date)
        
        self.buy(date, self.totalManey / 2.0)
             
    def buy(self, date, boughtMoney):
        print("buying...")
        self.stok1.updateCurPrice(date)
        self.money2Buy = self.stok1.calcStockNumAfterBuyAndReturnBoughtMoney(boughtMoney)
        
        self.stok1.updateStockInfo()
        self.updateInvestorInfo(1)
  
    def sell(self, date, hands):
        print("sell...")
        self.stok1.updateCurPrice(date)
        
        hands = self.stok1.calcStockNumAfterSellAndReturnSelledHands(hands)
        self.moneyfromSell = hands * 100 * self.stok1.curPrice
        
        self.stok1.updateStockInfo()
        self.updateInvestorInfo(0)
    
    def updateInvestorInfo(self, ifBuy=1):
        if ifBuy:
            self.freeMoney = self.freeMoney - self.money2Buy
        else:
            self.freeMoney = self.freeMoney + self.moneyfromSell
        
        self.marketMoney = self.stok1.stockNum * self.stok1.curPrice    
        self.totalManey = self.freeMoney + self.marketMoney
        self.profit = self.totalManey - self.cost
        
    def getStockHistData(self, strStockName):
        df = ts.get_hist_data(strStockName)  
        stockHistData = list(np.array(df.close))
        stockHistData.reverse()
        return stockHistData
               
    def showIvestorInfor(self):
        print("markeyMoney:{:.2f}, freeMoney:{:.2f}, profit:{:.2f}".format(
                self.marketMoney, self.freeMoney,self.profit))
    
if  __name__ == '__main__':
    
    investor = Investor(100000)
    investor.jianCang("002415", 0)
    investor.showIvestorInfor()
    investor.stok1.showStockInfor()

    investor.buy(20, investor.freeMoney / 3.0)
    investor.showIvestorInfor()
    investor.stockList[0].showStockInfor()

    investor.sell(30, 10)
    investor.showIvestorInfor()
    investor.stockList[0].showStockInfor()
    
    
    