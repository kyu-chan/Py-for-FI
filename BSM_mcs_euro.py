S0 = 100
K = 105
T = 1
r = 0.05
sigma = 0.2
from numpy import *
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import h5py
import datetime as dt
import sys
sys.path.append(r'C:\Users\pc\Desktop\stock\Py_for_Finance\tool')
from tool import BSM
import pprint as pp
import tool as tl

I = 100000
###np를 이용한 벡터화 문법 -> MC
np.random.seed(19650507)
z = np.random.standard_normal(I)
ST = S0 * np.exp( (r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)  ## BSM 모형 만기 주가지수
hT = np.maximum(ST - K, 0)
C0 = np.exp( -r * T ) * np.sum(hT) / I

#print( "Value of the European Call Option %5.3f" % C0)   ## % .3f는 서식

yahoo = web.DataReader('GOOG', data_source = 'yahoo', start = '3/14/2009',
                      end = '12/31/2020')

#print(yahoo.tail())
#print(yahoo.columns)

##변동성을 구해보자
yahoo['Log_Ret'] = np.log(yahoo['Close'] / yahoo['Close'].shift(1))
yahoo['Volatility'] = yahoo['Log_Ret'].rolling(window = 252,      ###center는 중간을 중심으로 계산할지?
                                               center = False).std() * np.sqrt(252)   ##window는 몇개씩 연산할 지
### 그 변동성 시간 곱 알잖아, 1년 영업일 수 252일 로 두고 하는거

yahoo[['Close', 'Volatility']].plot(subplots = True , color = 'blue',
                                    figsize = (8 , 6))  ## 축 서식 어떻게 바꾸냐 -> 꼭 찾아볼것
#plt.show()

## numpy로 속도에 문제가 생길 경우는 잘 없겠지만 속도가 더 필요하면 numexpr도 공부해 볼 것


h5 = pd.HDFStore("./data/vstoxx_data_31032014.h5", 'r')
futures_data = h5['futures_data']   ##선물
options_data = h5['options_data'] ##콜옵션
h5.close()
#print(futures_data)
#print(options_data.head())

##극내가격이나 극외가격을 제외하고 만기별 선물 가격 기준 50%이내 행사가를 가진 옵션만 다루자
options_data['IMP_VOL'] = 0.0 ##  내재 변동성 저장할 새로운 열


bs = BSM.bsm_function()


tol = 0.5  ##머니니스 범위
V0 = 17.6639
r = 0.01



#print(options_data)
#and ((forward * (1 - tol) > options_data.loc[option]['STRIKE']))
for option in options_data.index:
    ## 모든 옵션 시장가에 대해 반복
    forward = futures_data[futures_data['MATURITY'] == \
                           options_data.loc[option]['MATURITY']]['PRICE'].values[0]
    ###옵션과 만기가 일치하는 선물 선택
    if forward * (1 - tol) < options_data.loc[option]['STRIKE'] and options_data.loc[option]['STRIKE'] < forward * (
            1 + tol):
        imp_vol = bs.bsm_call_imp_vol(
            V0,  # VSTOXX지수값
            options_data.loc[option]['STRIKE'],
            options_data.loc[option]['TTM'],
            r,  # 단기이자율
            options_data.loc[option]['PRICE'],
            sigma_est=2.,  ##내재변동성 초기 추정치
            it=100)  ## 이터레이션
        options_data.loc[option, 'IMP_VOL'] = imp_vol


#print(futures_data['MATURITY'])
#print(options_data)
cond = (options_data['IMP_VOL'] > 0)
plot_data = options_data[cond]
#print(plot_data)
###플랏으로 같은 만기를 가지지만 행사가가 다른 내재 변동성 값들을 하나의 선으로 그려보려한다
### 그러려면 우선 중복되지 않고 정렬된 상태의 만기 값 리스트가 필요하다

maturities = sorted(set(options_data['MATURITY']))  ### 옵션데이터의 'MATURITY'컬럼을 set객체로 해서 sorted명령어로 정렬
#pp.pprint(maturities)


plt.figure(figsize= ( 8, 6))
for maturity in maturities:
    cond = (options_data["MATURITY"] == maturity)
    data = plot_data[cond]   ### colum을 이렇게도 부를 수 있구나 !!!

    ## 만기 같은것들끼리 솎아서
    plt.plot(data['STRIKE'], data['IMP_VOL'],
             label=maturity.date(), lw = 1.5)
    plt.plot(data['STRIKE'], data['IMP_VOL'], 'r.')
    plt.grid(True)
    plt.xlabel('strike')
    plt.ylabel('implied volatility of volatility')
    plt.legend()
plt.show()

##group!!
keep = ['PRICE', 'IMP_VOL']
group_data = plot_data.groupby(['MATURITY', 'STRIKE'])[keep]
#print(group_data)
### groupby 연산을 해야 dataframegroupby 객체가 반환된다. 그룹당 하나의 자료밖에
### 없는 지금 같은 상황에서 sum을 하면 그 자료 그대로 객체로 뱉어준다.

group_data = group_data.sum()
print(group_data)
## 보다시피 인덱스가 2개층 -> 만기와, 행사가
## 2개의 칼럼을 가진 객체를 뱉은 것을 확인할 수 있다.
