#!/usr/bin/python3

"""
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(30))
#print(fact(999))溢出
####################################################333


std = {'name':'mike','score':98}
def print_std():
    print('%s:%s' % (std['name'], std['score']))

print(print_std())
"""

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

std1 = Student('test1', 78)
std1.print_score()
