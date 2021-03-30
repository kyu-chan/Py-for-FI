import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import h5py
import datetime as dt
import sys
sys.path.append(r'C:\Users\pc\Desktop\stock\Py_for_Finance\tool')
from tool import MCS_PURE
import pprint as pp


### 오일러 근사와 유러피안 콜 옵션 price를 추정하는 몬테카를로 추정방법 이용(근사)


#ms = MCS_PURE.mcs_est()
#ms.mcs_pure(S0=100.,K=105.,r=0.05,sigma=0.2,M=50,T=1.0,I=250000,seed_num=20000)

K=105.
ms = MCS_PURE.mcs_est()
S = ms.mcs_vector_np(S0=100.,K=105.,r=0.05,sigma=0.2,M=50,T=1.0,I=250000,seed_num=20000)

###np연산이 훨씬 빠르네

plt.plot(S[:,:10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')

##만기 주가가 대략적으로 로그 정규분포임을 확인해보자
plt.hist(S[-1], bins=50)
plt.grid(True)
plt.xlabel('index level')
plt.ylabel('frequency')

## 만기시 옵션 페이오프 값의 분포 , 만기옵션의 내재가치 히스토그램
plt.hist(np.maximum(S[-1]-K, 0), bins=50)
plt.grid(True)
plt.xlabel('option inner value')
plt.ylabel('frequency')
plt.ylim(0, 50000)
plt.show()

###정확한 값음
print(sum(S[-1] < K))