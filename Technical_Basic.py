import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

SPY = web.DataReader('SPY', data_source='yahoo',
                     start = '1/1/2000', end = '4/14/2014')
#print(SPY.head())
#print(SPY.info())


## 종가 플랏
#SPY['Close'].plot(grid = True, figsize = ( 8, 5))
#plt.show()

## 2개월(42거래일) 과 1년(252 거래일) 추세(해당 주기 이동평균)으로 전략 생성
##일단 추세 계산 먼저
SPY['42d'] = np.round(SPY['Close'].rolling(window=42).mean(), 2)
SPY['252d'] = np.round(SPY['Close'].rolling(window=252).mean(), 2)

SPY =SPY[['Close', '42d', '252d']]
#print(SPY.tail())

#SPY.plot(grid=True, figsize=(8,5))
#plt.show()

SPY['42-252'] = SPY['42d'] - SPY['252d']
#print(SPY['42-252'].tail())

## SD : signal threshold
SD = 5
SPY['Regime'] = np.where(SPY['42-252'] > SD, 1, 0)
SPY['Regime'] = np.where(SPY['42-252'] < -SD, -1, SPY['Regime'])
#print(SPY['Regime'].value_counts())

#SPY['Regime'].plot(lw=1.5, grid = True)
#plt.ylim([-1.1, 1.1])
#plt.show()

SPY['Market'] = np.log(SPY['Close'] / SPY['Close'].shift(1))
SPY['Strategy'] = SPY['Regime'].shift(1)*SPY['Market']
SPY[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True,
                                                        figsize=(8, 5))
plt.show()




