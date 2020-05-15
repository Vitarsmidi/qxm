# -*- coding: utf-8 -*-
# @Time : 2020/4/5 22:17
# @Author : qxm
# @FileName: exception.py

# try:
#     open("abc.txt",'r')  #打开不存在的abc.txt文件
# except FileNotFoundError: #FileNotFoundError接收没有文件的异常
#     print("出现异常了")

# try:
#     print(a)  #打印没有定义的变量a
# except NameError: #NameError接收没有定义的变量的异常
#     print("出现异常了")

# try:
#     open("abc.txt",'r')  #打开不存在的abc.txt文件
# except BaseException: #BaseException接收所有类型的异常
#     print("出现异常了")
#
# try:
#     open("abc.txt",'r')  #打开不存在的abc.txt文件
# except BaseException as msg: #BaseException接收所有类型的异常,定义了msg变量来接收异常信息
#     print(msg)
#
# try:
#     open("abc.txt",'r')  #打开不存在的abc.txt文件
# except Exception as msg: #Exception接收所有类型的异常,但继承自BaseExceptio类
#     print(msg)

# try:
#     open("abc.txt",'r')  #打开不存在的abc.txt文件
# except Exception as msg: #Exception接收所有类型的异常,但继承自BaseExceptio类
#     print(msg)
# else:
#     print('没有异常时执行') #因为上面的代码出现了异常，所以不会执行这行

# try:
#     open("abc.txt",'r')  #打开不存在的abc.txt文件
# except Exception as msg: #Exception接收所有类型的异常,但继承自BaseExceptio类
#     print(msg)
# finally:
#     print('不管上面是否有异常，都执行这行')


#抛出异常
#定义say_hello()函数
def say_hello(name=None):
    if name is None:
        raise Exception('"name" cannot be empty') #raise 抛出异常
    else:
        print("hello,%r" +name)

say_hello()  #调用say_hello()函数