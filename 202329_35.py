#실습1~3
print('실습#1~3')

le = list(range(1,31))
print('1:',le)
le[0] = 1000
print('2: ',le)
le[-1] = 3000
print('3:',le)

#실습4~6
print('실습#4~6')

for i in range(31, 41):
    le.append(i)
print('4:',le)
for i in range(len(le)):
    if le[i] >= 100:
        le.remove(le[i])
        le.insert(i,i+1)
print('5:',le)
print('6:',le[:5])

#실습7~10
print('실습7~10')

print('7:',le[5:11])

del(le[9])
le.insert(9,[0, 0, 0])
print('8:',le)

for i in range(len(le)):
    if type(le[i]) is not int:
        le[i] = (i+1)
print('9:',le)

ls = le.copy()
ls.sort(reverse=True)
print('10',ls)

#실습11~13
print('#실습11~13')

for i in range(len(le)):
    if le[i]%2==0:
        le[i]=(le[i]*10)
print('11:',le)

le = [list(range(10)) for _ in range(1,4)]
print('12',le)

ls = le[0]
print('13',ls)

hap = 0
for i in ls:
    hap += i
ls.append(hap)
print('14:',ls)

hap = 0
while len(ls) > 1:
    hap += ls.pop()
print('15: 총합('+str(hap)+'), 남은 리스트:(',ls,')',sep='')

#실습16
print("#실습16")

import random

# grd = [random.randint(0,100) for i in range(100)]
grd = []
for i in range(100):
    grd.append(random.randint(0,100))
num = 0
for i in grd:
    if num < i:
        num = i
Ma = num

num = 100
for i in grd:
    if num > i:
        num = i
Mi = num

hap = 0
for i in grd:
    hap += i
print('최고: ', Ma,'점, 최하: ',Mi,'점, 평군: ',('%.2f' %(hap/100)))