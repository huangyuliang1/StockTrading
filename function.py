



def JianCang(stockPrice, money):
    num = int(money / stockPrice)
    hand = num % 100  
    num = num - hand
    markValure = num * stockPrice
    return num, markValure
    
def Scell(stockNum):
    pass