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
    def __str__(self):
        return '%s is % years old'% (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()

if __name__ == '__mian__':
    p1 = Programer("yangyh", 20)
    print (p1)
 #   print (dir (p))