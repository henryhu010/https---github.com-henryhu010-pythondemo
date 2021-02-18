'''
Author: your name
Date: 2020-11-12 22:14:34
LastEditTime: 2021-01-24 11:46:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/print("Hello world").py
'''
print("Hello world")

print("1024*768=", 1024*768)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \\\'Adam\\\''
print(n,'\n',f,'\n',s1,'\n',s2)

bmi = 80.5/(1.75*1.75)
print(bmi)
if bmi <= 18.5:
    print('体重过轻')
elif  18.5 < bmi <= 25:
    print('体重正常')
elif  25 <bmi <= 28:
    print('体重过重')
else :
    print('肥胖')


L = ['Bart', 'Lisa', 'Adam']
for l in L :
    print('Hello, ' +l +'!')


