import numpy as np
import pandas as pd
from pandas_datareader import data as web
from urllib.request import urlretrieve
import datetime as dt
import matplotlib.pyplot as plt

DAX =  web.DataReader( name = '^GDAXI', data_source='yahoo',
                       start = '2000-1-1') ## 독일 DAX지수
#print(DAX.tail())

#es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
#vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
#urlretrieve(es_url,'./data/es.txt')
#urlretrieve(vs_url, './data/vs.txt')

lines = open('./data/es.txt', 'r').readlines()
lines = [line.replace(' ','') for line in lines]  ### 빈 칸 지우기

#print(lines[:6])
#for line in lines[3886:3890]:
#    print(line[41:])    ##여기 끝에 세미콜론이 붙네 처리해줄 필요가 있음
new_file = open('./data/es50.txt', 'w')
new_file.writelines('date' + lines[3][:-1]
                    + ';DEL' + lines[3][-1]) ###4번쨰줄을 수정해서 첫째줄에 넣느다
new_file.writelines(lines[5:])  ##그 뒷줄 그대로 이어 붙여
new_file.close()

new_lines = open('./data/es50.txt', 'r').readlines()
#print(new_lines[:5])
es = pd.read_csv('./data/es50.txt', index_col= 0,
                 parse_dates=True, sep = ';', dayfirst=True,)  ##parse_Dates :datetime 형식으로 파싱
np.round(es.tail())                                           ##dayfirst는 datetime에서 일이 월보다 먼저 위치하는지

del es['DEL']
#print(es.columns)
cols = ['SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF', 'SXXA', 'DK5F', 'DKXF']
es = pd.read_csv('./data/es50.txt', index_col= 0, header=None,
                 parse_dates=True, sep = ';', dayfirst=True,
                 skiprows=4, names = cols )
#print(es.tail())

vs = pd.read_csv('./data/vs.txt', index_col=0, header=2,
                 parse_dates=True, sep=',', dayfirst=True)
#print(vs.info())

data = pd.DataFrame({'EUROSTOXX' :
                         es['SX5E'][es.index > dt.datetime(1999,1,1)]}) # dict
data = data.join(pd.DataFrame({'VSTOXX' :
                                   vs['V2TX'][vs.index > dt.datetime(1999,1,1)]}))
data = data[data.index < '2014-09-27']

data = data.fillna(method='ffill')  ##과거 자료만 이용할 땐 forward fill
#print(data.info())
#print(data.tail())

### 시각화로 전반적인 자료의 형태 살피기
#data.plot(subplots = True, grid = True, style = 'b', figsize = (8,6))
#plt.show()

rets = np.log(data / data.shift(1))
#print(rets.tail())
rets.dropna(inplace = True) #drop NA , inplace하면 바로 rets에 지정된다
## 수익률 플랏
#rets.plot(subplots=True, grid=True, style = 'b', figsize=(8,6))
#plt.show()

##유로스톡스50 수익률을 독립변수로 vstoxx수익률을 종속변수로
##회귀
xdat = rets['EUROSTOXX'].values
ydat = rets['VSTOXX'].values
reg = np.polyfit(x=xdat,y=ydat, deg =1)  ###이러면 결과값에 [0]이 기울기 [1] 절편, deg는 차수

#plt.plot(xdat, ydat, 'r.')  ##r은 빨간색
#ax = plt.axis()  ##axis
#x = np.linspace(ax[0], ax[1] + 0.01)
#plt.plot(x, reg[1] + reg[0] * x, 'b', lw =2)
#plt.grid(True)
#plt.axis('tight')
#plt.xlabel('EURO STOXX 50 returns')
#plt.ylabel('VSTOXX returns')
#plt.show()

#print(rets.corr())
##이렇게 단일하게 봤을 떄는 음의 상관관계가 말도 안되게 높은데

## 연단위로 계산해서 플랏을 그려보자
rets['EUROSTOXX'].rolling(252).corr(rets['VSTOXX']).plot(grid = True, style = 'b')
#plt.show()   현재 rolling_corr이 중단돼서 위와 같이 써야함 x.rolling(windows).corr(y)












