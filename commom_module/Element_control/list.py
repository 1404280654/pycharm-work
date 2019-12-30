# -*- coding:utf8 -*-

import math
import datetime
import random
import os

list1 = [0, 1, 2, 3, 4]
i = 1
x = 2
y = 3
a = 4
b = 5

list1.append()              # 将x添加到列表末尾

list1.sort()                # 对列表元素排序

list1.reverse()             # 将列表元素逆序

list1.index(x)              # 返回第一次出现元素x的索引值

list1.insert(i, x)          # 在位置i处插入新元素x

list1.count(x)              # 返回元素x在列表中的数量

list1.remove(x)             # 删除列表中第一次出现的元素x

list1.pop(i)                # 取出列表中i位置上的元素，并将其删除


''''--------------------------------------------------------------------------'''
# math库

pi = math.pi               # 圆周率

math.ceil(x)          # 对x向上取整

math.floor(x)         # 对x向下取整

math.pow(x, y)        # x的y次方

math.sqrt(x)          # x的平方根

math.fsum(list1)      # 对集合内的元素求和


'''--------------------------------------------------------------------------'''
# datetime模块
now = datetime.datetime.now()      # 当前时间 2019-03-16 13:57:20.900422
month = now.month                  # 获得当前月3
year = now.year                    # 获得当前年2019


'''--------------------------------------------------------------------------'''
# randomm模块
random()        # 生成一个(0,1.0)之间的随机浮点数
random.uniform(a, b)        # 生成一个a到b之间的随机浮点数
random.randint(a, b)        # 生成一个a到b之间的随机整数
random.choice(list1)       # 从列表中随机返回一个元素
random.shuffle(list1)      # 将列表中元素随机打乱
random.sample(list1, x)    # 从指定列表中随机获取x个元素
os.urandom()         # 从操作系统提供的源生成随机数的类


'''--------------------------------------------------------------------------'''


