'''
Author: Henry Hu
Date: 2021-04-24 18:13:23
LastEditTime: 2021-04-27 22:40:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/MSBDemo/Demo01.py
'''

print(' Hello World!')

#转译字符
print('Hello\nWorld!')
print('Hello\tWorld!')

#变量练习
name = '佟丽娅'
age = 36
print('我是'+ name + '今年' + str(age))

#布尔运算符 and\ or \  not \ in \ not in
s = 'hello world!'
print('hello' in s) 

#位运算符,将数据转为二进制运算，  & , | , << 左移一位，高位溢出舍弃低位补0 , >> 右移一位，低位溢出舍弃高位补0

r = range(1, 10, 2)
print(list(r))

'''计算1-100之间偶数和'''
a = 1
oddnum = 0
evennum = 0
while a <= 100:
    if a % 2:
        oddnum += a
    else:
        evennum += a
    a+=1
print('1-100之间奇数和为：', oddnum)
print('1-100之间偶数和为：', evennum)

'''输出100到999的水仙花数'''
for item in range(100, 1000):
    a = item % 10
    b = item//10%10
    c = item//100
    if item == a**3 + b**3 +c**3:
        print(item)