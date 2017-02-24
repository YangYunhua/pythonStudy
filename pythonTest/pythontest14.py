#!/usr/bin/python3
class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print_student(self):
        print('%s : %s' % (self.__name, self.__age))

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if 0 <= age <=100:
            self.__age = age
        else:
            raise ValueError('bad age')
    def set_name(self, name):
        self.__name = name
student = Student('test1',19)
student.print_student()
print(student.get_name())

class Anilmals(object):
    def run(self):
        print('Animal is running……')
class Cat(Anilmals):
    def run(self):
        print('cat is running……')
class Dog(Anilmals):
    pass
dog = Dog()
dog.run()
cat = Cat()
cat.run()

#判断一个变量是否是某个类型，用isinstance()
print(isinstance(cat,list))

#判断对象类型，使用type()函数
print(type(123))

#判断class的继承关系，isinstance()

