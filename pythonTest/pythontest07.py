#!/usr/bin/python3
def hello():
    print( "hello world" )


hello( )


def area(width, height):
    return width * height


def print_name(name):
    print( "Wlcome", name )


name = 'yangyh'
print_name( name )

w = 4
h = 5
print( area( w, h ) )


def changename(mylist):
    mylist.append( [1, 2, 3, 4] );
    print( "函数内取值", mylist )
    return


mylist = [10, 20, 30];
changename( mylist );
print( "函数外取值", mylist );


def printme():
    print( 'my name is yangyh' )


printme( )


def printhd(str):
    print( str )
    # return【表达式】结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回none。
    return


printhd( '函数调用' )


# 值传递&引用传递
def changeme(mylista):
    mylista.append( [10, 20, 30] );
    print( "函数内取值", mylista )
    return


mylista = [1, 2, 3, 4];
changename( mylista );
print( "函数外取值", mylista )


def guanjianzi(name, age):
    print( name, age )
    return


guanjianzi( age=19, name='test' )


# 不定长函数
def printinfo(arg1, *vauleput):
    "打印任何传入的参数"
    print( "输出：" )
    print( arg1 )
    for var in vauleput:
        print( var )
    return;


printinfo( 10 );
printinfo( 70, 60 );
