#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'


class Programer( object ):
    hobby = "play Computer"

    def __init__(self, name, age, weight):
        self.name=name
        self._age=age
        self.__weight=weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_name(self):
        return self.name
    @property
    def get_weight(self):
        return self.__weight

    def sel_age(self):
        print('my age is ',self._age)

if __name__ == '__main__':
    programer = Programer('yangyh',40, 60)
    print( dir( programer ) )
    print(Programer.get_hobby())
    print(programer.get_name)
    print('my weight is',programer.get_weight)
    programer.sel_age()