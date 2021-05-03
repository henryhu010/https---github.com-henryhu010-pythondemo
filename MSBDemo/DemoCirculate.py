'''
Author: Henry
Date: 2021-05-06 15:24:11
LastEditTime: 2021-05-09 17:40:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/MSBDemo/DemoMultiplication.py
'''

# Multiplication Table
for i in range(1, 10): #行数
    for j in range(1, i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print() #换行


'''流程控制语句'''
for n in range(1,5):
    for m in range(1,11):
        if m%2 == 0:
            break
            #continue
        print(m,end='\t')
    print()


'''切片函数'''
lst=[10, 20, 30, 40, 50, 60, 70, 80, 90]

print('--------步长为正数---------')
lst2=lst[1:6:1]
print(lst2)
print(lst[1::2])
print(lst[::2])

print('---------步长为负数--------')
print(lst[::-1])
print(lst[8::-2])

#向列表末尾追加一个元素
lst.append(100)
print(lst)
