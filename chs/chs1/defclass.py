# -*- coding: utf-8 -*-
# @Time : 2020/4/5 12:31
# @Author : qxm
# @FileName: defclass.py

#定义add()函数
def add(a,b):
    return a+b
if __name__=='__main__': #当该模块直接运行时，下面的代码将被运行，当该模块被其他调用时，下面的代码不被运行
    c=add(3,5)
    print(c)
#
# def add(a=3,b=5):
#     return a+b
# c1=add()
# print(c1)

# #定义MyClass类
# class MyClass(object):
#     def say_hello(self,name):
#         return "hello," +name
# #调用MyClass类
# mc=MyClass()
# print(mc.say_hello("tom"))
#
# # 创建类时先初始化方法__init__()
# class A:
#     def __init__(self,a,b):
#         self.a=int(a)
#         self.b=int(b)
#
#     def add(self):
#         return self.a+self.b

# #调用类时需要传入初始化参数
# count=A('4',5)
# print(count.add())
#
# #创建B类继承A
# class B(A):
#     def sub(self,a,b):
#         return a-b
# print(B(2,3).add())