#!/usr/bin/python

# -*- coding: UTF-8 -*-

for letter in 'python':
    if letter == 'h':
       # pass
        print( '这是pass块')
    print("当前字母:",letter)

print("Goodbye")


n = 100
sum = 0
count = 1
while count <= 100:
    sum = sum + count
    count += 1
print('1-%d的和为%d' % (n,sum))


fruits = ['apple','mango','banana']
for index in range(len(fruits)):
    print('当前水果：',fruits[index])
print('goodbye')
