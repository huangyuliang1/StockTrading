'''
Created on 2019年8月11日

@author: HuangYuliang
'''
# from stock import Stock
from investor import Investor


class BuyOrSell():
    def __init__(self, totalManey):
        self.totalManey = totalManey
        self.lstThreeBuyPri = [[0,0],[0,0],[0,0]]
        self.lstThreeSelPri = [[0,0],[0,0],[0,0]]
        self.continuousBuyTimes = 0
        self.continuousSelTimes = 0
        self.lstProPri = 0
        
    def pro(self, riseThr = 0.01, fallThr = -0.05, buyRate = 0.25, selRate = 0.25):
              
        investor = Investor(self.totalManey)
        investor.jianCang("002414", 0)
        stock = investor.stok1
        self.updateLstBuyPriList(0, stock.curPrice, stock.stockHands)
        self.lstProPri = stock.curPrice
        
        for date in range(1,stock.longOfStockHistData):
            stock = investor.stok1
            stock.updateCurPrice(date)
            rate = (stock.curPrice - self.lstProPri) /stock.curPrice
            
            if rate > riseThr:
                investor.buy(date, investor.freeMoney * buyRate)
                self.updateLstBuyPriList(self.continuousBuyTimes, stock.curPrice, int(investor.money2Buy//stock.curPrice//100))
                
                self.lstProPri = stock.curPrice
                investor.showIvestorInfor()
                stock.showStockInfor()
                
            if rate < fallThr:
                investor.sell(date, int(stock.stockHands * selRate))
                self.updateLstSelPriList(self.continuousSelTimes, stock.curPrice, int(investor.moneyfromSell//stock.curPrice//100))
                
                self.lstProPri = stock.curPrice
                investor.showIvestorInfor()
                stock.showStockInfor()
                   
    def updateLstBuyPriList(self, lastTimes, pri, num):
               
        self.lstThreeBuyPri[lastTimes][0] = pri
        self.lstThreeBuyPri[lastTimes][1] = num 
        if self.continuousBuyTimes < 2:
            self.continuousBuyTimes += 1   
        if self.continuousSelTimes > 0:
            self.continuousSelTimes -= 1
        
    def updateLstSelPriList(self, lastTimes, pri, num):
        self.lstThreeSelPri[lastTimes][0] = pri
        self.lstThreeSelPri[lastTimes][1] = num
        if self.continuousSelTimes < 2:  
            self.continuousSelTimes += 1 
        if self.continuousBuyTimes > 0: 
            self.continuousBuyTimes -= 1
    
if  __name__ == '__main__':
    
    process = BuyOrSell(100000)   
    process.pro()
    
    


