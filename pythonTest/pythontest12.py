#!/usr/bin/python3

fo = open("D:\sql.txt","r+")
print("文件名为",fo.name)
#line = fo.read(10)
print ("读取的字符串", fo.read())
fo.close()



def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
a = my_abs(10)
print("a=",a)

def nop(age):
    if age >18:
        pass

def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>= 0:
        return x
    else:
        return -x

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

m = move(100, 100, 60, math.pi / 6)
print(m)

def power(f, t):
    s = 1
    while t > 0:
        t = t - 1
        s = s * f
    return s
g = int(input("输入f"))
h = int(input("输入h"))
j = power(g,h)
print(j)


def add_end(L = None):
    if L is None:
        L = []
    L.append('end')
    return L
print(add_end())
print(add_end())