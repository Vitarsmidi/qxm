#!/usr/bin/env python
# coding = utf-8
import time #引入time库

print('a','b' 'c')
print('a','b','c')
print("a","b","c")
print("a","b","c",sep = '') #sep = '' 字符串之间没有空格
print("a","b","c",sep = '/') #sep = '/' 字符串之间间隔/
print("a","b","c",sep = '隔开') #sep = '/' 字符串之间间隔
print("a","b","c",sep = '\n') #spe里的\n代表换行符。
print("a","b","c",end=''), print("d") #end=''在同一行输出俩个print
print('a,"1",b')


a   =  '"{"name":"test"}"' #代表："{"name":"test"}"的字符串。该字符串包含最外面的两个引号。
print('a:'+a)
print('a:',a)
a1  =  '\"{"name":"test"}\"'
print('a1:',a1)
a2  =  '\"{\"name\":\"test\"}\"'
print('a2:',a2)

b2  =  "\"{\"name\":\"test\"}\"}"
print('b2:',b2)

c1  =  "{\"name\":\"test\"}"  #表示：{"name":"test"}字符串。
print('c1:',c1)
c2  =  "{'name':'test'}"
print('c2:',c2)

d2  =  "'{\"name\":\"test\"}'"  #d2代表：'{"name":"test"}'这个字符串。
print('d2:',d2)
d3  =  "'{'name':'test'}'"  #d3代表：'{'name':'test'}'这个字符串。
print('d3:',d3)

print ("Start : %s" % time.ctime())
print ("End : %s" % time.ctime())
#  %字符：标记转换说明符 %s表示输出类型为字符串，%d表示输出类型为整型数字,%r不管什么都打印出来;