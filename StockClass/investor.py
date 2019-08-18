'''
Created on 2019年8月11日

@author: HuangYuliang
'''
from stock import Stock

class Investor():
    def __init__(self, money):
        self.totalManey = money
        self.cost = money
        self.profit = 0.0
        self.profitMargin = 0.0
        self.marketMoney = 0
        self.freeMoney = money
        self.money2Buy = 0
        self.moneyfromSell = 0
        
        self.stockList = []
        self.recordBuyInfor = []   #[price, hands, state]
        self.recordSelInfor = []
    
    def chooseStock(self, strStockName):
        self.stockName = strStockName
        self.stok1 = Stock(strStockName)
        self.stockList.append(self.stok1)
        self.stok1.getStockHistData()
             
    def jianCang(self, date, rate = 1.0):
        print("JianCanging...")
        self.stok1.updateCurPrice(date)   
        self.buy(date, self.totalManey * rate)
             
    def buy(self, date, boughtMoney):
        print("buying...")
        self.stok1.updateCurPrice(date)
        self.money2Buy = self.stok1.calcStockNumAfterBuyAndReturnBoughtMoney(boughtMoney)
        
        self.stok1.updateStockInfo()
        self.updateInvestorInfo(1)
  
    def sell(self, date, hands):
        print("selling...")
        self.stok1.updateCurPrice(date)
        
        hands = self.stok1.calcStockNumAfterSellAndReturnSelledHands(hands)
        self.moneyfromSell = hands * 100 * self.stok1.curPrice
        
        self.stok1.updateStockInfo()
        self.updateInvestorInfo(0)
    
    def qingCang(self,date):
        print("qingCang...")
        self.sell(date, self.stok1.stockHands)
    
    def chuquanAndQingCang(self, date):
        print("chuquan...")
        self.qingCang(date-1)   
#         self.buy(date, self.moneyfromSell)
        
    def initStock(self,date):
        self.stok1.stockHistData = []
        self.stok1.curPrice = 0
        self.stok1.marketMoney = 0
        self.stok1.stockNum = 0
        self.stok1.stockHands = 0
        self.stok1.longOfStockHistData = 0
        self.stok1.maxAverMinMonth = [0.0,0.0,0.0]
        self.stok1.maxAverMinWeek = [0.0,0.0,0.0]
   
    def updateInvestorInfo(self, ifBuy):
        if ifBuy:    
            hands = int(self.money2Buy / self.stok1.curPrice // 100)
            recode = OperatRecord(self.stok1.curPrice, hands)
            self.recordBuyInfor.append(recode)
            
            self.freeMoney = self.freeMoney - self.money2Buy
        else:
            hands = int(self.moneyfromSell / self.stok1.curPrice // 100)
            recode = OperatRecord(self.stok1.curPrice, hands)
            self.recordSelInfor.append(recode)
            
            self.freeMoney = self.freeMoney + self.moneyfromSell
           
        self.marketMoney = self.stok1.stockNum * self.stok1.curPrice    
        self.totalManey = self.freeMoney + self.marketMoney
        self.profit = self.totalManey - self.cost
        self.profitMargin = self.profit / self.cost
        
    def updateRecord(self,ifBuy):        
        if ifBuy == 1:
            hands = int(self.money2Buy / self.stok1.curPrice // 100)
            recode = OperatRecord(self.stok1.curPrice, hands)
            self.recordBuyInfor.append(recode)
        else:
            hands = int(self.moneyfromSell / self.stok1.curPrice // 100)
            recode = OperatRecord(self.stok1.curPrice, hands)
            self.recordSelInfor.append(recode)
                             
    def showIvestorInfor(self):
        print("money2Buy:{:.2f}, moneyFromSell:{:.2f}".format(self.money2Buy,self.moneyfromSell))
        print("markeyMoney:{:.2f}, freeMoney:{:.2f}, profit:{:.2f}, profitMargin:{}".format(
                self.marketMoney, self.freeMoney,self.profit, self.profitMargin))
 
 
class OperatRecord():
    def __init__(self, price, hands):
        self.price = price
        self.hands = hands
        self.state = 0
    
    
     
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
    
    investor.qingCang(40)
    investor.showIvestorInfor()
    investor.stockList[0].showStockInfor()
    
    
    
    
    
    