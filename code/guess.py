# /usr/bin/env python
#coding:utf-8

'''
一个可以多次猜数字的游戏，该游戏代码源自李航，从‘跟着老齐学Python中摘来’
'''

import random


i = 0
while i < 4:
    print '*'*35
    num = input('请输入0到9任何一个数字： ')
    
    xnum = random.randit(0, 9)

    x = 3 -i
    
    if num == xnum:
        print '运气真好，您猜对了！'
        break
    elif num > xnum:
        print '您猜大了！\n哈哈，正确答案是：%s\n您还有%s次机会！' %(xnum, x)
    elif num < xnum:
        print '您猜小了！\n哈哈，正确答案是：%s\n您还有%s次机会！' %(xnum, x)
    print '*'*35

    i += 1
