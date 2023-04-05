#실습 1. 구구단 출력

n = int(input('출력할 단수 입력: '))
for i in range(1,10):
    print(n, '*',i,'=',n*i)

#실습 2. 성적 등급 구분

grd = int(input('점수 입력(0~100): '))
if grd >= 90:
    print('A')
elif grd >= 80:
    print('B')
elif grd >= 70:
    print('C')
elif grd >= 60:
    print('D')
else:
    print('F')

#실습 3.입력된 숫자까지 모두 더하기

n = int(input('숫자 입력: '))
res = 0

for i in range(n+1):
    res += i
print(res)

#실습 4.배수 출력

n = int(input('input number: '))
r = int(input('배수 입력: '))

for i in range(r,n):
    print(i,end=', ')
print(i)

#실습 5.로또 추천 번호 출력

import random as r

for i in range(1,11):
    num1to45 = list(range(1, 46))
    res = []
    for j in range(1,7):
        n = r.choice(num1to45)
        res.append(n)
        num1to45.remove(n)
    print(res)
    