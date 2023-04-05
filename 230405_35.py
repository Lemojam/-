#실습1~3

print('#1')

items = ['색소폰', '바이올린', '피아노', '트럼펫', '일렉기타', '베이스기타', '통기타', 
'리코더', '우쿨렐레', '플루트']
counts = [80, 74, 92, 52, 21, 94, 48, 64, 20, 89]
dic = {}
i=0
for _ in items:
    dic[_] = counts[i]
    i+=1

print(dic, '\n')

print('#2')

dic['색소폰'] = 1000
print(dic, '\n')

print('#3')

del(dic['트럼펫'])
print(dic, '\n')

#실습4~6

print('#4')

print('총합:',sum(dic.values()), '\n')

print('#5')

min = 99999999
max = 0
for _ in dic.keys():
    if dic[_] < min:
        min = dic[_]
        ist = _
    if dic[_] > max:
        max = dic[_]
        ast = _
print('가장 적은 악기:', ist, min, '\n')

print('#6')

print('가장 많은 악기:', ast, max, '\n')

#실습7~9

print('#7')

import random

for _ in dic.keys():
    dic[_] = [dic[_], random.randint(10000,99999)]
print(dic, '\n')

print('#8')

max = 0

for _ in dic.keys():
    if dic[_][0]*dic[_][1] > max:
        max = dic[_][0]*dic[_][1]
        ast = _
print('개수*가격이 가장 높은 악기명: ',_, '\n')

print('#9')

print('악기면 리스트:',list(dic.keys()))

#9-1
num = []
for _ in dic.keys():
    num.append(dic[_][0])
print('개수 리스트', num)
num = []
for _ in dic.keys():
    num.append(dic[_][1])
print('가격 리스트', num)

#9-2
# num = []
# nem = []
# for _ in dic.keys():
#     num.append(dic[_][0])
#     nem.append(dic[_][1])
# print('개수 리스트', num)
# print('가격 리스트', nem)

#9-3
# i= 0
# num = [[0 for _ in range(len(dic))] for i in range(2)]
# for _ in dic.keys():
#     num[0][i] = dic[_][0]
#     num[1][i] = dic[_][1]
#     i+=1
# print('개수 리스트', num[0])
# print('가격 리스트', num[1])

#추가 문제

print('#추가 문제!')

r = int(input('열 크기 입력: '))
n = int(input('행 크기 입력: '))

for i in range(r):
    pl = i
    for j in range(n):
        pl+=1
        if pl > n:
            pl=1
        print(pl, end=' ')
    print()
