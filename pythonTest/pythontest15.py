#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'
"""
a = 5
b = 7
if a > b:
    print(1)
else:
    print(2)

c = "abc"
d = "defg"
if c in d:
    print(3)
else:
    print(4)
n = input("input a name:")
print("my name is %r." %n)


for i in n:

    print(i)

for q in range(9):
    print(q)

for j in range(3,20,6):
    print(j)

dict={'username':'yangyh','password':'111'}
print(dict.keys())
print(dict.values())

for k,y in dict.items():
    print(k)
    print(y)


import time
print(time.ctime())

try:
    open("a", 'r')
except FileNotFoundError as msg:
    print(msg)
"""
from random import randint
number = randint(1,20)
if number % 2 == 0:
    raise NameError("number is even")
else:
    raise NameError("number is odd")

class Car(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def add(self):
        return self.m + self.n
car = Car()
print( car.add(5,7))


