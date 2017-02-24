#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'
"""
import urllib.request
#Urllib的GET请求
url='http://www.baidu.com'
response=urllib.request.Request(url=url)
html=urllib.request.urlopen(response)
print(html.getcode())
print(html.headers)

#urllib的post请求
url2='http://www.tuling123.com/openapi/api'
data={"key":"your","info":'你好'}
data=urllib.parse.urlencode(data).encode('utf-8')
re=urllib.request.Request(url2,data)
html=urllib.request.urlopen(re)
print(html.getcode(),html.msg)
print(html.read())

#request库的http请求
import requests
r=requests.get('http://www.baidu.com')
print(r.headers)

#request库的POST请求
import requests
payload={'key1':'value1','key2':'value2'}
r2=requests.post("http://httpbin.org/post",data=payload)
print(r2.text)
"""
#python序列化
import pickle
aa={}
aa["title"]="我是好人"
aa["num"]=2
t=pickle.dumps(aa)
print("1.",t)
f=pickle.loads(t)
print("2.",f)

#json库实现序列化
import json
dict1={'name':'yyh','age':'24','address':'北京'}
print(u'未序列化前的数据类型为：',type(dict1))
print(u'未序列化前的数据',dict1)
####序列化处理dict1
str1=json.dumps(dict1)
print(u'序列化后的数据类型为：',type(str1))
print(u'序列化后的数据为：',str1)

#json库实现反序列化
dict2=json.loads(str1)
print(u'反序列化后的数据类型：',type(str1))
print(u'反序列化后的数据：',dict2)


#结合requests库查看返回的json数据
import json,requests
r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=上海')
print(r.text,u'数据类型：',type(r.text))
dict3=json.loads(r.text)
print(dict3,u'数据类型', type(dict3))
