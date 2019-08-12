'''
Created on 2019年8月11日

@author: HuangYuliang
'''
from investor import Investor

class marketPlace():
    def __init__(self, totalManey):
        self.totalManey = totalManey
        self.lstThreeBuyPriAndHands = [[0,0],[0,0],[0,0]]
        self.lstThreeSelPriAndHands = [[0,0],[0,0],[0,0]]
        self.continuousBuyTimes = 0
        self.continuousSelTimes = 0
        self.lstProPri = 0
        
    def chooseStock(self, strStockName):
        self.stockName = strStockName
        
    def trading(self, riseThr = 0.05, fallThr = -0.1, buyRate = 0.25, selRate = 0.25):
              
        investor = Investor(self.totalManey)
        investor.jianCang(self.stockName, 0)
        stock = investor.stok1
        self.updateLstBuyPriList(0, stock.curPrice, stock.stockHands)
        self.lstProPri = stock.curPrice
        
        for date in range(1,stock.longOfStockHistData):
            stock = investor.stok1
            stock.updateCurPrice(date)
            rate = (stock.curPrice - self.lstProPri) /stock.curPrice
            
            if rate > riseThr:
                investor.sell(date, int(stock.stockHands * selRate))               
                self.updateLstSelPriList(self.continuousSelTimes, stock.curPrice, int(investor.moneyfromSell//stock.curPrice//100))
                
                self.lstProPri = stock.curPrice
                investor.showIvestorInfor()
                stock.showStockInfor()
                self.showMarkInfor()
                
            if rate < fallThr:
                investor.buy(date, investor.freeMoney * buyRate)
                self.updateLstBuyPriList(self.continuousBuyTimes, stock.curPrice, int(investor.money2Buy//stock.curPrice//100))
                
                self.lstProPri = stock.curPrice
                investor.showIvestorInfor()
                stock.showStockInfor()
                self.showMarkInfor()
                   
    def updateLstBuyPriList(self, lastTimes, pri, num):
               
        self.lstThreeBuyPriAndHands[lastTimes][0] = pri
        self.lstThreeBuyPriAndHands[lastTimes][1] = num 
        if self.continuousBuyTimes < 2:
            self.continuousBuyTimes += 1   
        if self.continuousSelTimes > 0:
            self.continuousSelTimes -= 1
        
        
    def updateLstSelPriList(self, lastTimes, pri, num):
        self.lstThreeSelPriAndHands[lastTimes][0] = pri
        self.lstThreeSelPriAndHands[lastTimes][1] = num
        if self.continuousSelTimes < 2:  
            self.continuousSelTimes += 1 
        if self.continuousBuyTimes > 0: 
            self.continuousBuyTimes -= 1
            
    def showMarkInfor(self):
        print("lstThreeBuyPriAndHands:{}, lstThreeSelPriAndHands:{}".format(
        self.lstThreeBuyPriAndHands, self.lstThreeSelPriAndHands))
        print("continuousBuyTimes:{}, continuousSelTimes:{}".format(
            self.continuousBuyTimes,self.continuousSelTimes))
    
if  __name__ == '__main__':
    
    process = marketPlace(100000)  
    process.chooseStock("002414") 
    process.trading()
    
    


