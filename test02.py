import decimal
from decimal import Decimal
import re
from datetime import datetime
from functools import reduce
from random import randint

a = 10
type(a)
print(a.bit_length())
a = 100000
print(a.bit_length())

googol = 10 ** 100

#print(decimal.getcontext())

d = Decimal(1) / Decimal(11)
#print(d)

### 숫자 표현 정밀도 변경
decimal.getcontext().prec = 4 # 디폴트보다 낮은 정밀도
e = Decimal(1) / Decimal(11)
print(e)

decimal.getcontext().prec = 60 # 디폴트보다 높은 정밀도
f = Decimal(1) / Decimal(11)
print(f)
### 이런식으로 정밀도 조절
## 서로 다른 정밀도끼리 연산도 가능
g = d + e + f
print(g)

### 문자열 처리
t = "this is a string object"
print(t.capitalize())  ### 첫 글자만 대문자로

print(t.split())  ##띄어쓰기로 분리

## 특정 단어가 시작되는 위치 표시
print(t.find('string')) #0부터 시작 띄어쓰기 포함
## 찾으려는 단어가 문자열 객체 내에 없다면 -1을 반환한다.

## 글자 치환
print(t.replace(' ', '|'))

print('http://www.python.org'.strip('htp:/'))  ##요롷게 땔 수 있음

## 정규식
####여러 줄에 걸친 문자열 정의
series = """    
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:00:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd';
"""
##앞의 날짜/시간 부분을 구분하여 기술해 보자 , #파싱작업의 성능 향상
dt = re.compile("'[0-9/:\s]+'")  # datetime
result = dt.findall(series)
print(result)
## 첫번째 result 해볼겡
pydt = datetime.strptime(result[0].replace("'",""),
                         '%m/%d/%Y %H:%M:%S')
print(pydt)
print(type(pydt))

##튜플
## t = (1, 2.5, 'data')
t = 1, 2.5, 'data'   ###이렇게해도 튜플로 됨
print(type(t))

print(t.count('data')) ## 이 값이 몇번 있는지 세줌
print(t.index(2.5))  ## 2.5가 몇번째에 있는지 index를 뱉어줌

### list
l = [1, 2.5, 'data']
l.append([4,3])  ##요거 자체를 원소로 추가해
print(l)
l.extend([1.0, 1.5, 2.0]) ## 이 원소들을 하나씩 붙여
print(l)
l.insert(l.index(2.5), 'insert')
print(l)  ## 특정 인덱스 앞에 뒤에걸 삽입
l.remove('data')
print(l)
p = l.pop(3) ##특정 인덱스 위치의 원소를 삭제하고 그 값을 뱉음
print(p)
print(l)
###print(l, p)

for element in l[2:5]:
    print(element ** 2)

r = list(range(0, 8, 1) ) #시작값, 끝값+1 (인덱스?), 스텝
print(r)

for i in range(2,5):
    print(l[i] ** 2)

total = 0
while total < 100:
    total += 1
print(total)

###조건 제시법
m = [ i ** 2 for i in range(5)]
print(m)

### map(함수, 범위(리스트형식 각각의 원소에))
def even(x):
    return x % 2 == 0
print(even(3))
print(list(map(even, range(10))))
print(list(map(lambda x: x ** 2, range(10))))

### filter( def, list)  함수를 적용했을 경우 True가 되는 원소만 뱉어준다.
print(list(filter(even, range(15))))

## reduce는 리스트 객체에서 단 하나의 결과값만을 생성한다.
print(reduce(lambda x, y: x+y, range(10)))

def cumsum(l):
    total = 0
    for elem in l:
        total += elem
    return total
print(cumsum(range(100)))

d = {
    'Name' : 'Angela Merkel',
    'Country' : 'Germany',
    'Profession' : 'Chancelor',
    'Age' : 60
}
print(type(d))
print(d['Name'], d['Age'])
print(d.keys())
print(d.values())
print(d.items())
birthday = True
if birthday is True:
    d['Age'] += 1
print(d['Age'])

for item in d.items():
    print(item)
for value in d.items():
    print(type(value))

#for item in d.iteritems():   ## python 2에서 지원
#    print(item)
#for value in d.iteritems():
#    print(type(value))

### set는 우리가 아는 집합의 개념을 구현할 수 있는데
### 특별이 많이 쓸 경우는 없고

## 리스트 객체에서 중복된 원소를 제거할 때 set을 활용할 수 있겠다

I = [randint(0,10) for i in range(1000)]
##### 0~10사이의 임의의 정수 1000개 생성
print(len(I))
print(I[:20])
s = set(I)
print(s)  ##보다시피 안겹치지

v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = [v, v, v]
print(m)

### from copy import deepcopy를 이용하면 초기 배열을 변경해도 파생배열이