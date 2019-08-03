'''
Created on 2019年8月1日

@author: HuangYuliang
'''
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts
from CstockOperating import *

# df = ts.get_hist_data("002142") #宁波银行
df = ts.get_hist_data("600598") #北大荒
# df = ts.get_hist_data("002415")  #海康威视
# df = ts.get_hist_data("000651")  #格力电器
# print(df.head(5))
cs = df.close
cs = np.array(cs)
cs = list(cs)
cs.reverse()

a = StockOperating( cs, 100000, 0.2, 0.2, -0.02, 0.02)  # stockHistData, money, buyRate, sellRate, fallThr, riseThr
a.process()
a.showProfit()
df.close.plot()
plt.show()
print("end!")