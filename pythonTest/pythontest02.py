#!/usr/bin/python3

list1 = ['test1', 'test2', 'test2']
list2  = ['1', 2, 3, 4]

print("list1[0]",list1[0])
print("list2[1:4]",list2[1:4])

#更新

list1[2] = "test"
print(list1)

del list1[1]
print(list1)

print(list1+list2)
print(list1*4)
print("test" in list1)
print(len(list1))
for x in list1:
    print(x)

print(list1[1:])

c=[list1,list2]
print(c)
list3 = [3, 5, 5, 56, 9]
print(max(list3))
print(min([3,5,6,7,9,789]))
print(list(c))
print(list2.count(2)) #统计某个元素在列表中出现的次数
list1.extend(c)
print(list1)
print(list2.copy())
d = [2,4,1,6,7]
d.sort()
print(d)
d.remove(6)
print(d)
print(d.pop(-3))
print(d)


