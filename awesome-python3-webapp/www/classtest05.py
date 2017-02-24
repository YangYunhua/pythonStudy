#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'
class Programer(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __setattr__(self, name, value):
        self.__dict__[name] = value


    def __getattr__(self, name):
        return super(Programer, self).__getattribute__(name)

if __name__ == '__main__':
    p = Programer("yangyh", 12)
    print(p.name, p.age)