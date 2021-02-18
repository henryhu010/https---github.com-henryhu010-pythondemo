# -*- coding: utf-8
'''
Author: Henry
Date: 2021-01-24 20:02:57
LastEditTime: 2021-02-11 15:56:09
LastEditors: Please set LastEditors
Description: word game
FilePath: /python/wordgame.py
'''

print('----------- HenryFunc1 ---------')
times = 3
import random
secret = random.randint(1, 10)
temp = input('能猜中哪个数字是我想的么？')
guess = int(temp)
while guess != secret and times > 0:
    if guess == temp:
        print('恭喜你，猜中了！')
    else:
        if guess > secret:
            print('大哥，猜大了！')
        else:
            print('不好意思，猜小了啊！')
        times = times - 1
        if times > 0:
            temp = input('猜错啦，请重新输入吧：')
            guess = int(temp)
        else:        
            print('No chance, Game Over!')


print('----------- HenryFunc2 ---------')
temp = input('请输入一个数字：')
number = int(temp)
i = int(1)
while number:
    print(i)
    i = i + 1
    number = number - 1


print('----------- HenryFunc3 ---------')
