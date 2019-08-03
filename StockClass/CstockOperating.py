'''
Created on 2019年7月31日

@author: HuangYuliang
'''
class StockOperating():
    def __init__(self, stockHistData, money, buyRate, sellRate, fallThr, riseThr):
        self.buyRate = buyRate
        self.sellRate = sellRate
        self.fallThr = fallThr # -0.1
        self.riseThr = riseThr # 0.1
        
        self.stockHistData = stockHistData
        self.currentPrice = stockHistData[0]
        self.totalMoney = money
        
        self.stockHand = 0
        self.stockNum = 0
        self.marketMoney = 0
        self.remainMoney = 0
        self.lastProPrice = 0
        
    def jianCang(self):    
        avalStockNum = int(self.totalMoney / self.currentPrice)
        avalStockHand = avalStockNum // 100
        buyOneOfFourHand = avalStockHand // 2
        
        self.stockHand = buyOneOfFourHand
        self.stockNum = self.stockHand * 100
        self.marketMoney = self.stockNum * self.currentPrice
        self.remainMoney = self.totalMoney - self.marketMoney
        self.lastProPrice = self.currentPrice
        print("JianCang,date={},stockNum={},stckHand={},markMoney={:.1f},remainMoney={:.1f},currentPrice={:.2f}.".format(
                                0,self.stockNum,self.stockHand,self.marketMoney,self.remainMoney,self.currentPrice))
        
    def buyPro(self):
        avalStockNum = int(self.remainMoney / self.currentPrice)
#         print("avalStockNum:{}".format(avalStockNum))
        if avalStockNum < 100: #不买
            return
        
        avalStockHand = avalStockNum // 100
#         print("avalStockHand:{}".format(avalStockHand))
        if avalStockHand < 4:  #全买
            self.stockHand += avalStockHand
            self.stockNum += self.stockHand * 100
        else:
            self.stockHand += int(avalStockHand * self.buyRate)
            self.stockNum = self.stockHand * 100
        
        self.marketMoney = self.stockNum * self.currentPrice
        self.remainMoney -= int(avalStockHand * self.buyRate) * 100 * self.currentPrice
        self.lastProPrice = self.currentPrice
    
    def sellPro(self):
        if self.stockHand < 4:  # 不卖
            return 
        avalStockHand = int(self.stockHand * self.sellRate) # 卖的手数
        
        self.stockHand -= avalStockHand
        self.stockNum = self.stockHand * 100
        
        self.marketMoney = self.stockNum * self.currentPrice
        self.remainMoney += avalStockHand * 100 * self.currentPrice
        self.lastProPrice = self.currentPrice
        
    def process(self):
        length = len(self.stockHistData)
        self.jianCang()
        
        for i in range(1,length):
            self.currentPrice = self.stockHistData[i]
            rate = (self.currentPrice - self.lastProPrice) / self.lastProPrice
#             print("{:.3f},{:.1f}".format(rate, self.currentPrice))
            if rate < self.fallThr and (self.remainMoney//self.currentPrice)>100:               
                self.buyPro()
                print("buying,- date={}, stockNum={}, stckHand={}, profit={:.1f}, currentPrice={:.2f}.".format(
                                i,self.stockNum,self.stockHand,(self.marketMoney + self.remainMoney - self.totalMoney),self.currentPrice))
                
            elif rate > self.riseThr and self.stockHand > 0:
                
                self.sellPro()
                print("Selling,- date={}, stockNum={}, stckHand={}, profit={:.1f}, currentPrice={:.2f}.".format(
                                i,self.stockNum,self.stockHand,(self.marketMoney + self.remainMoney - self.totalMoney),self.currentPrice))
#             self.showProfit()       
    def showProfit(self):
        print("The total profit is:{}.".format(self.marketMoney + 
                                    self.remainMoney - self.totalMoney))
    
    
    
    
    
    
    
    
    
    
    
        
        
