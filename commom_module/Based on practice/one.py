#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

#1.判断3的200次方能否被7整除
def one():
    if math.pow(3, 200)%7==0:
        print("可以被整除")
    else:
        print("不能")


#2.a=1,b=True，判断a是否等于b
def two():
    a=1
    b=True
    if a==b:
        print("等于")
    else:
        print("不等于")


#3.i=1024,将i整除32再赋值给自己
def three():
    i=1024
    i=i/32
    print(i)

#4.给定一个四位的年份year，写出判断是否是闰年的表达式
def four():
    a="请输入一个4位数的年数"
    print(a)
    try:
        a = int(input())
    except BaseException:
        print("输入不合法")
        four()
    else:
        if a<399 or a>10000:
            print("不是4位数")
            print("请重新输入一个4位数的年数")
            four()
        else:
            if a % 4 == 0:
                print("您输入的是闰年")
            else:
                 print("不是闰年")

#5.测试一个字符串中是否包含3.14
def five():
    a=input()
    if 3.14 in a:
        print("存在")
    else:
        print("不存在")

#6.a=2e10,b=2e10，测试a与b是否是同一个对象
def six():
    a=2e10
    b=2e10
    if format(id(a))== format(id(b)):
        print("是同一对象")
    else:
        print("不是")
#7.写出判断a=3.1415926,b=3.1415927是否相等的表达式.....
#8.x=1,y=2,z=3,验证x<=y<=z是否成立.....
print("输入你想运行的题目英文数字【one-six】")
asd=input()
shuzu=['one','two','three','four','five','six']
if asd == shuzu[0]:
    one()
if asd == shuzu[1]:
    two()
if asd == shuzu[2]:
    three()
if asd == shuzu[3]:
    four()
if asd == shuzu[4]:
    five()
if asd == shuzu[5]:
    six()
