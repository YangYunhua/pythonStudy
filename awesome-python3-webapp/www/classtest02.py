#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'

class Programer(object):
    def __new__(cls, *args, **kwargs):
        print("this is __new__ method")
        print(args)
        return super(Programer, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        print("this is __init__ method")
        self.name = name
        self.age = age

if __name__ == '__main__':
    programer = Programer('yangyh',40)
    print(programer.__dict__)