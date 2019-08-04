'''
Created on 2019年7月31日

@author: HuangYuliang
'''
import copy
class StockOperating():
    def __init__(self, stockHistData, money, buyRate, sellRate, fallThr, riseThr):
        self.buyRate = buyRate
        self.sellRate = sellRate
        self.fallThr = fallThr # -0.1
        self.riseThr = riseThr # 0.1
        
        self.stockHistData = stockHistData
        self.currentPrice = stockHistData[0]
        
        self.cost = money
        self.totalMoney = self.cost
        self.proNum = 0
        
        self.stockHand = 0
        self.stockNum = 0
        self.marketMoney = 0
        self.remainMoney = 0
        self.lastProPrice = 0
        self.lstByPrce = [0,[0.0,0],[0.0,0],[0.0,0],[0.0,0]] # 0:连续买卖的次数,[价格，数量]
        self.lstSlPrce = [0,[0.0,0],[0.0,0],[0.0,0],[0.0,0]]
        
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
        
    def fuQuanAndJianCang(self):

        self.totalMoney = self.marketMoney + self.remainMoney
        self.jianCang()

     
    def process(self):
        length = len(self.stockHistData)
        self.jianCang()
        
        
        for i in range(1,length):
            self.currentPrice = self.stockHistData[i]  
            
            rt = (self.stockHistData[i]  - self.stockHistData[i-1]) / self.stockHistData[i-1]
            if rt < -0.15:
                self.fuQuanAndJianCang()
                self.proNum += 1
                continue
                
            rate = (self.currentPrice - self.lastProPrice)

            if rate < 0:   # 跌，买
                n = self.lstSlPrce[0]
#                 m = self.lstByPrce[0]
                numHand = (self.remainMoney//self.currentPrice) // 100
                if n == 0:
                    if (self.currentPrice - self.lastProPrice) / self.lastProPrice < self.fallThr and numHand >= 0:
                        
                        self.buyPro2(int(numHand * self.buyRate))
                        
                        print("n={}, m={}, buyNUM0={}, stockHand={}".format(self.lstSlPrce[0],self.lstByPrce[0],int(numHand * self.buyRate),self.stockHand))
#                         print(self.lstByPrce)
                        print("buying,- date={}, stockNum={}, stckHand={}, profit={:.1f}, currentPrice={:.2f}.".format(
                                i,self.stockNum,self.stockHand,(self.marketMoney + self.remainMoney - self.cost),self.currentPrice))
                        print()
                        self.proNum += 1
                    
                elif (self.currentPrice - self.lstSlPrce[n][0]) / self.lstSlPrce[n][0] < self.fallThr and numHand >= 1:
                    buyNum  = 0

                    for j in range(1,n+1):
                        buyNum += self.lstSlPrce[j][1]
                    if numHand > buyNum:    
                        self.buyPro2(buyNum)                        
                        print("n={}, m={}, buyNUM1={}, stockHand={}".format(self.lstSlPrce[0],self.lstByPrce[0],buyNum,self.stockHand))                      
                    else:
                        self.buyPro2(int(numHand))                        
                        print("n={}, m={}, buyNUM2={}, stockHand={}".format(self.lstSlPrce[0],self.lstByPrce[0],int(numHand),self.stockHand))  
#                     print(self.lstByPrce)
                                      
                    print("buying,- date={}, stockNum={}, stckHand={}, profit={:.1f}, currentPrice={:.2f}.".format(
                                i,self.stockNum,self.stockHand,(self.marketMoney + self.remainMoney - self.cost),self.currentPrice))
                    print()
                    self.proNum += 1

            else:  # 涨，卖
#                 n = (self.lstSlPrce[0])
                m = self.lstByPrce[0]
                num = self.stockHand
                if m == 0:
                    if (self.currentPrice - self.lastProPrice) / self.lastProPrice > self.riseThr: 
                        
                        self.sellPro2(int(num * self.sellRate))
                        
                        print("n={}, m={}, sellNUM0={}, stockHand={}".format(self.lstSlPrce[0],self.lstByPrce[0],int(num * self.sellRate),self.stockHand))
#                         print(self.lstSlPrce)
                        print("Selling,- date={}, stockNum={}, stckHand={}, profit={:.1f}, currentPrice={:.2f}.".format(
                                i,self.stockNum,self.stockHand,(self.marketMoney + self.remainMoney - self.cost),self.currentPrice))
                        print()
                        self.proNum += 1
                        
                elif num > 0 and  (self.currentPrice - self.lstByPrce[m][0]) / self.lstByPrce[m][0] > 0.05:   
                    
                    
                    sellNum = 0
                    for j in range(1,m+1):
                        sellNum += self.lstByPrce[j][1]
                        
                    if num > sellNum:   
                        self.sellPro2(sellNum)
                        
                        print("n={}, m={}, sellNUM1={}, stockHand={}".format(self.lstSlPrce[0],self.lstByPrce[0],sellNum,self.stockHand))

                    else:                       
                        self.sellPro2(num)
                        
                        print("n={}, m={}, sellNUM2={}, stockHand={}".format(self.lstSlPrce[0],self.lstByPrce[0],num,self.stockHand))
#                     print(self.lstSlPrce) 
                                          
                    print("Selling,- date={}, stockNum={}, stckHand={}, profit={:.1f}, currentPrice={:.2f}.".format(
                                i,self.stockNum,self.stockHand,(self.marketMoney + self.remainMoney - self.cost),self.currentPrice))
                    print()
                    self.proNum += 1
#             self.showProfit()       
    def showProfit(self):
        print("The total profit is:{}.".format(self.marketMoney + 
                                    self.remainMoney - self.cost))
    
    def buyPro2(self,buyHand):

        self.stockHand += buyHand
        self.stockNum = self.stockHand * 100
        
        self.marketMoney = self.stockNum * self.currentPrice
        self.remainMoney -= buyHand * 100 * self.currentPrice
        
        self.lstByPrce[0] += 1
        if self.lstByPrce[0] < 5:
            self.lstByPrce[self.lstByPrce[0]][0] = self.currentPrice
            self.lstByPrce[self.lstByPrce[0]][1] = buyHand
        else:
            self.lstByPrce[0] = 4
            self.lstByPrce[1] = self.lstByPrce[2]
            self.lstByPrce[2] = self.lstByPrce[3]
            self.lstByPrce[3] = self.lstByPrce[4]
            
            self.lstByPrce[4][0] = self.currentPrice
            self.lstByPrce[4][1] = buyHand
            
        if self.lstSlPrce[0] > 0:    
            self.lstSlPrce[0] -= 1
        
        self.lastProPrice = self.currentPrice
        
    def sellPro2(self,SellHand):
        
        self.stockHand -= SellHand
        self.stockNum = self.stockHand * 100
        
        self.marketMoney = self.stockNum * self.currentPrice
        self.remainMoney += SellHand * 100 * self.currentPrice
        
        self.lstSlPrce[0] += 1
        a = self.lstSlPrce[0]
        if self.lstSlPrce[0] < 5:
#             print(self.lstSlPrce[0],self.currentPrice,SellHand)
            self.lstSlPrce[a] = [self.currentPrice,SellHand]

        else:
            self.lstSlPrce[0] = 4
#             print(self.lstSlPrce[1:4])
#             print(self.lstSlPrce[2:5])
            self.lstSlPrce[1:4] = copy.copy(self.lstSlPrce[2:5])
            
            
            self.lstSlPrce[4][0] = self.currentPrice
#             print(self.lstSlPrce[4][0])
            self.lstSlPrce[4][1] = SellHand
                  
        if self.lstByPrce[0] > 0:
            self.lstByPrce[0] -= 1
        
        self.lastProPrice = self.currentPrice
    
    
    
    
    
    
    
    
    
    
        
        
