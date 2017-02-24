#!/usr/bin/python3
s='Hello,yangyh'
str (s)
repr(1/6)
print(repr(1/7))


for x in range(1,11):
    #print(repr(x).rjust(2), repr(x*x).rjust(3))
    print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
    print(repr(x*x*x).rjust(4))


#键盘读取输入
str = input("请输入：")
print("你输入的是：",str)