#!/usr/bin/python3
a=[-1, 50, 30, 40, 33, 80]
print("list.count(x),返回x在列表中出现的次数",a.count(50),a.count(1),a.count('x'));
print(a)
print("list.insert(i,x)在指定位置i插入一个x元素。")
a.insert(2,-1)
print(a)
print("list.append(x)在列尾添加x，相当于list.insert(len(a),x)")
a.append(30)
print(a)
print("list.index(x),返回列表中第一个元素的位置索引");
print(a.index(-1))
print("list.remove(x),删除列表中第一个x元素，若没有，返回错误")
a.remove(-1)
print(a)
print("list.reverse()，倒排列表中的元素")
a.reverse()
print(a)
print("list.sort()对列表中的元素进行排序")
a.sort()
print(a)
print("******************************************************")
print("将列表当作堆栈使用，后进先出")
#数据结构
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print("pop，出栈")
a = stack.pop()
print(a,stack)
print("将列表当作队列使用,先进先出，popleft,取出第一个元素；")

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
name1 = queue.popleft()



print(name1)
print(queue)
name1 = queue.popleft()
print(name1)

#列表推导式
print("列表推导式")
vec = [2, 4, 6]
value = [3*x for x in vec]
print(value)

value2=[[x,x**2] for x in vec]
print(value2)

print("对序列里每一个元素逐个调用某方法")
freshfruit = ['banana', 'loganberry', 'passion fruit']
value3 = [weapon.strip() for weapon in freshfruit]
print(value3)

print("用if子句作为过滤器")
value4 = [3*x for x in vec if x > 3]
print(value4)

value5 = [4*x for x in vec if x < 2]
print(value5)

print("更多循环使用")
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
value6 = [x*y for x in vec1 for y in vec2]
print(value6)

value7 = [x+y for x in vec1 for y in vec2]
print(value7)

value8 = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(value8)

print("列表推导式可以使用复杂表达式或嵌套函数")
value9 = [str(round(355/113, i)) for i in range(1,6)]
print(value9)

print("嵌套列表,将3×4的矩阵转换为4×3列表")
matrix = [[1,2,3,4],
          [5,6,7,8],
          [3,4,5,6],
          ]
print(matrix)
value10 =  [[row[i] for row in matrix] for i in range(4)]
print(value10)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

