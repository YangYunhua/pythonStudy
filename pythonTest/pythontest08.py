#!/usr/bin/python3
#可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

#调用sum函数
print ("相加后的值为：", sum(10,20))
print ("相加后的值为：", sum(20,20))


#return

def sumab(arg1, arg2):
    #返回2个参数的和."
    total = arg1 + arg2
    print("函数内：", total)
    return total;

#调用sumab函数
total = sum(10,20);
print("函数外：",total)

#全局变量&局部变量
totalb = 0;
def sumae(arg1, arg2):
    totalb = arg1 + arg2;
    print("函数内局部变量", totalb)
    return totalb;

sumae( 10, 20 );
print("函数外全局变量：",totalb)