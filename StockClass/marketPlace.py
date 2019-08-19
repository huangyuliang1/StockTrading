'''
Created on 2019年8月11日

@author: HuangYuliang
'''
from investor import Investor

class marketPlace():
    def __init__(self, totalManey):
        self.totalManey = totalManey
        self.lstpri = 0
        
    def createInvestor(self):
        self.investor = Investor(self.totalManey)
    
    def trading(self, strStockName, week=7, month=30, riseThr = 0.1, fallThr = -0.10, buyRate = 1.0):
                  
        self.investor.chooseStock(strStockName)
        stock = self.investor.stok1
        print("longOfStockHistData:{}".format(stock.longOfStockHistData))
        start = 260
        ifChuQuan = 0
        for date in range(start ,stock.longOfStockHistData):
                                  
            stock.updateCurPrice(date)
            r = (stock.curPrice - stock.stockHistData[date-1]) / stock.curPrice 
            
            if r < -0.15: # 当派股时，清仓，且month天后再操作
                if stock.stockHands > 0:
                    self.investor.chuquanAndQingCang(date)
                    stock.showStockInfor()
                    self.investor.showIvestorInfor()
                ifChuQuan = date + month
                continue
            
            if ifChuQuan != 0 and date < ifChuQuan: # 如果除权了，month天后再操作
                continue
            ifChuQuan = 0
             
            stock.updateStockStatisticsInfo(date, week, month)
            
            buyrate = (stock.curPrice - stock.maxAverMinMonth[1]) / stock.curPrice #以一个月的股价均值做为参照
            selrate = (stock.curPrice - stock.maxAverMinMonth[1]) / stock.curPrice 
            
            # 长线
            if buyrate < fallThr and stock.stockHands == 0:
                self.investor.jianCang(date, buyRate)
                stock.showStockInfor()
                self.investor.showIvestorInfor()
                
            if selrate > riseThr and stock.stockHands > 0: 
                self.investor.qingCang(date)    
                stock.showStockInfor()
                self.investor.showIvestorInfor() 
                
            # 短线
            '''
            if rate > riseThr:
                self.investor.sell(date, int(stock.stockHands * selRate))               
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
            '''
            
    def showMarkInfor(self):
        print("lstThreeBuyPriAndHands:{}, lstThreeSelPriAndHands:{}".format(
        self.lstThreeBuyPriAndHands, self.lstThreeSelPriAndHands))
        print("continuousBuyTimes:{}, continuousSelTimes:{}".format(
            self.continuousBuyTimes,self.continuousSelTimes))
        
import matplotlib.pyplot as plt    
if  __name__ == '__main__':
    
    # 002142/宁波银行    002414/海康威视   002230/科大讯飞    600598/北大荒     000651/格力电器
    marketPlace = marketPlace(100000)
    marketPlace.createInvestor()
    
    marketPlace.trading("002230")  
#     print(marketPlace.investor.stok1.stockHistData[:40])
    print("end!")
    plt.show()
    
    


