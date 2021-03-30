import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from pandas import Series
from matplotlib.patches import Polygon

###1차원 자료 그리기
np.random.seed(1000)
y = np.random.standard_normal(20)
x = range(len(y))  ##길이 맞춰야지
#plt.plot(x,y)
#plt.show()

###plot의 인수로 ndarray 객체를 넘기는 경우 plot함수가 이를 감지하고 자동으로 x값을 맞춰준다.
#plt.plot(y)
#plt.show()

##ndarray객체에 메서드를 호출해 넘겨줘도 된다.
#plt.plot(y.cumsum())
#plt.show()
#### 요런 기본적인 플롯 스타일은 보통 보고서나 출판물에 쓸 수 없다.
### 레이텍 폰트와 호환되는 폰트를 쓸 수 도 있고 그림에 축라벨을 붙이거나 그리드를 추가해야할 수도 있다.

##그리드 추가, 라벨붙이기는 어렵지 않다.
#plt.plot(y.cumsum())
#plt.grid(True) #그리드 추가
#plt.axis('tight') # 축 간격을 더 조밀하게 조정
#plt.show()

#plt.plot(y.cumsum())
#plt.grid(True)
#plt.xlim(-1, 20)
#plt.ylim(np.min(y.cumsum()) - 1,
#         np.max(y.cumsum()) + 1)
#plt.show()

#################### 제목, x값, y값 label,  색깔, 포인트
'''
plt.figure(figsize=(7, 4)) ##폭, 높이
plt.plot(y.cumsum(), 'b', lw=1.5) ## 선 파란색, 굵게
plt.plot(y.cumsum(), 'ro')  ## red , 동그라미
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show()
'''

###################################################################################
####################2차원 plot######################################################
np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0) #가로축 따라 누적합
##그러면 두 덩어리 나오지
## plt.plot이 자동으로 두 개로 분리해줌
'''
plt.figure(figsize=(7, 4))
plt.plot(y , lw=1.5)
plt.plot(y, 'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show()
'''

#### 주석달거나 범례 붙일려면?
'''
plt.figure(figsize=(7, 4)) ##폭, 높이
plt.plot(y[:, 0], lw=1.5, label = '1st')
plt.plot(y[:, 1], lw=1.5, label = '2nd')
plt.plot(y, 'ro')  ## red , 동그라미
plt.grid(True)
plt.legend(loc=0)  ###0으로 놓으면 범례에 가려지는 데이터가 최소가 되도록 위치 자동으로 잡아줌
plt.axis('tight')   #### 위치 숫자로 정할 수 있긴 함
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show()
'''

###크기가 다른 두가지 종류의 데이터를 한 plot에 그릴 때 보조축
'''
y[:,1] = y[:, 0] * 100
plt.figure(figsize=(7, 4)) ##폭, 높이
plt.plot(y[:, 0], lw=1.5, label = '1st')
plt.plot(y[:, 1], lw=1.5, label = '2nd')
plt.plot(y, 'ro')  ## red , 동그라미
plt.grid(True)
plt.legend(loc=0)  ###0으로 놓으면 범례에 가려지는 데이터가 최소가 되도록 위치 자동으로 잡아줌
plt.axis('tight')   #### 위치 숫자로 정할 수 있긴 함
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show()
''' ##이런식으로

## 두개의 축을 사용하는 방법 or 두개의 서브플롯을 사용하는 방법

##### 축 두개 쓰는 법
'''
fig, ax1 = plt.subplots()
plt.plot(y[:,0], 'b', lw=1.5, label = '1st')
plt.plot(y[:,0], 'ro')  ## red , 동그라미
plt.grid(True)
plt.legend(loc=8)###0으로 놓으면 범례에 가려지는 데이터가 최소가 되도록 위치 자동으로 잡아줌
plt.axis('tight')   #### 위치 숫자로 정할 수 있긴 함
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
ax2 = ax1.twinx() ## 서프축
plt.plot(y[:, 1], 'g' ,lw=1.5, label = '2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.ylabel('value 2nd')
plt.show()
'''

#########플랏 두개로 구분
'''
plt.figure(figsize=(7,5))
plt.subplot(211)
plt.plot(y[:,0], 'b', lw=1.5, label = '1st')
plt.plot(y[:,0], 'ro')  ## red , 동그라미
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
plt.title('A Simple Plot')

plt.subplot(212) # 2행 1열 중 2번 째
plt.plot(y[:, 1], 'g' ,lw=1.5, label = '2nd')
plt.plot(y[:, 1], 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.show()
'''

############서브 플랏에 각각 다른 플롯 적용해야할 때
'''
plt.figure(figsize=(9,4))
plt.subplot(121)
plt.plot(y[:,0], 'b', lw=1.5, label = '1st')
plt.plot(y[:,0], 'ro')  ## red , 동그라미
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('1st Data Set')

##바차트로
plt.subplot(122) # 2행 1열 중 2번 째
plt.bar(np.arange(len(y)), y[:,1] ,width=0.5,
        color = 'g', label = '2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.title('2nd Data Set')
plt.show()
'''
################ 기타 플롯 유형
##스캐터 양 축 데이터 주면 댐
'''
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7,5))
plt.plot(y[:, 0], y[:,1], 'ro')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
plt.show()
'''
### scatter 함수를 이용한 산점도
'''
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7,5))
plt.scatter(y[:, 0], y[:,1], marker='o')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
plt.show()
'''

######## scatter는 세 번째 차원을 추가해 색깔로 depth를 보여 줄 수 있다.
'''
y = np.random.standard_normal((1000, 2))
c = np.random.randint(0, 10, len(y)) ###임의의 수 생성
plt.figure(figsize=(7,5))
plt.scatter(y[:, 0], y[:,1], c=c ,marker='o')
plt.colorbar()
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
plt.show()
'''

### 히스토 그램으로 금융자산 수익률 나타낼 경우
'''
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7,5))
plt.hist(y, label=['1st', '2nd'], bins=25)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()
'''
#### 히스토그램 겹치기
'''
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7,5))
plt.hist(y, label=['1st', '2nd'], color=['b', 'g'],
         stacked=True, bins=20) ###겹칠래?
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()
'''

##### 박스플롯
'''
y = np.random.standard_normal((1000, 2))
fig, ax = plt.subplots(figsize=(4,2))
plt.boxplot(y)
plt.setp(ax, xticklabels = ['1st', '2nd'])  ###플롯 객체의 속성을 설정하는 함수
plt.xlabel('data set')
plt.ylabel('value')  
plt.title('Boxplot')
plt.show()


line = plt.plot(y, 'r')
plt.setp(line, linestyle = '--')  ###이렇게 선을 실선으로 바꿀 수 있음
plt.show()
'''

def func(x):
    return 0.5 * np.exp(x) + 1

a, b = 0.5, 1.5 # 적분 구간
x = np.linspace(0, 2)
y = func(x)

fig, ax = plt.subplots(figsize=(7,5))
plt.plot(x, y, 'b', linewidth=2)
plt.ylim(ymin=0)

######### 적분값이 함수 상한과 하한 사이의 면적과
######### 같다는 것을 보인다.
'''
Ix = np.linspace(a, b)
Iy = func(Ix)
verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')
ax.add_patch(poly)

plt.text(0.5 * (a+b), 1, r"$\int_a^b f(x) \mathrm{d}x$",
         horizontalalignment = 'center', fontsize=20)
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
ax.set_xticks((a,b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([func(a), func(b)])
ax.set_yticklabels(('$f(a)$', '$f(b)$'))
plt.grid(True)
plt.show()
'''


