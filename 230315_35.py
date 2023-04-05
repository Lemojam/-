print('#실습 1')
num1 = int(input('숫자1 ==> '))
num2 = int(input('숫자2 ==> '))
print(num1,'+',num2,'=',num1 + num2)
print(num1,'-',num2, '=',num1 - num2)
print(num1, '*',num2, '=',num1 * num2)
print(num1,'/',num2, '=',num1 / num2)
print(num1,'%',num2, '=','%.5f'%(num1 % num2))
print(num1,'**',num2,'=',num1 ** num2)

print('#실습 2')
import turtle

turtle.shape('turtle')

for i in range(100):
    turtle.forward(4)
    turtle.right(4)

print('#실습 3')
for i in range(50):
    print('*'*(i+1))

