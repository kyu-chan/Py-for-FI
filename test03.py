import decimal
from decimal import Decimal
import re
from datetime import datetime
from functools import reduce
from random import randint
import numpy as np

a =np.array([0, 0.5, 1.0, 1.5, 2.0])
print(type(a))
print(a[:2])

print(a.sum())
print(a.std())
##누적합계
print(a.cumsum())

print(a * 2)
print(a ** 2)  ###연산가능!!
print(np.sqrt(a))

b = np.array([a, a * 2])
print(b[0])
print(b[0,2])
print(b.sum())

print(b)
print(b.sum(axis = 0))  ## 세로합
print(b.sum(axis = 1))  ## 가로합

### np.array를 쓸라믄  배열의 모든 원소의 값을 이미 알아야함
### np.ndarray를 쓰면 객체부터 만들고 원소를 지정할 수 있음

c = np.zeros((2,3,4),### 3행 4열 배열 2개
             dtype='i',  ## dtype int32
             order = 'C')  ## 행기반 'D'이면 포트란처럼 열 기반이면?
print(c)
##유사한 방식
d = np.ones_like(c,### 3행 4열 배열 2개
             dtype='f',  ## dtype float
             order = 'C')
print(d)


##구조화 배열
dt = np.dtype([('Name' , 'U10'), ('Age' , 'i4'),
               ('Height', 'f'), ('Children/Pets', 'i4', 2)])
s = np.array([('Smith', 45, 1.83, (0, 1)),
              ('Jones', 53, 1.72, (2, 2))], dtype=dt)
print(s)

print(s['Name'])
print(s['Height'].mean())

print(s[0]['Age'])
print(s[1]['Age'])
### 이처럼 각 열마다 다른 자료형ㅇㄹ 사용할 수 있고 사전객체처럼 쓸 수 있다.

### Numpy 배열은 원소끼리 더할 수 있다.
r = np.random.standard_normal((4,3))
s = np.random.standard_normal((4,3))
print(r)
print(s)
print(r+s)

print(2*r + 3)  ## 3이 브로드캐스팅 됨
s = np.random.standard_normal(3)
print(s)
print(r)
print(r + s) ## 모든 행에 브로드캐스팅 돼서 더해졌군 하지만 열이 안맞으면 길이가 안맞아서 브로드캐스팅 안댐

## 전치 transpose()
print(r.transpose())

### math 의 sin함수는 numpy 배열에 적용 안된다.
# math.sin(r) XXX
#대신 np에서 ufunc을 제공함
print(np.sin(r))
print(np.sin(np.pi))



####굉장히 많은 데이터를 array롤 다룰 경우는 메모리 배치도 잘 해줘야한다
### order를 C로 한 5행 100000000열 array를 생각해보자
### 행단위로 더하는 것이 속도가 더 빠른데 이는 메모리상 붙어있기 떄문
### order를 F로 한 포트란 배치에서는 반대로 세로로 메모리가 붙어있어 세로합이 더 빠르다
### 하지만 포트란 방식의 전반적 연산속도가 C방식보다 느리다. 그러니 웬만하면 C방식을 쓰자


