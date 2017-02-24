#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'

class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception("The type of object must be Programer")

    def __add__(self, other):
        if isinstance(other, Programer):
            return self.age + other.age
        else:
            raise Exception("The type of object must be Programer")

if __name__ == '__main__':
    programer1 = Programer("yangyh", 30)
    programer2 = Programer("yangyh", 30)

    print(programer1 == programer2)
    print(programer1 + programer2)
    L = [programer1,programer2]


