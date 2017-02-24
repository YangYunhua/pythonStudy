#!/usr/bin/python3
'''
test多行注释1
test多行注释1
test多行注释1
'''

"""
test 多行注释2
test 多行注释2
test多行注释2
"""
print("test")

#运算符测试
a = 1
b = 2
c = a+b
print('1+2=',c)
print(c * b)

a = 3
b = 4
c = a * b
print(c)

#比较运算符
if(a == b):
    print('true')
else:
    print('false')

#赋值运算
c += a
print("赋值运算c+=a即c=c+a：", c)
c **= a
print("赋值运算c **= a即c的a次幂运算：", c)

#位运算符
a = 60
b = 70
c = a & b
print(c)
c = a | b
print("a|b",c)
c = a ^ b
print("a^b",c)

#成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5];
if(a in list):
    print("list列表中有a变量")
else:
    print("list列表中有a变量")

#身份运算符

#字符串格式化
print("我叫%s" %('yangyh') )
print("%s is a student"%('yangyh'))
