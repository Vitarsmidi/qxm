# -*- coding: utf-8 -*-
# @Time : 2020/4/5 13:00
# @Author : qxm
# @FileName: import.py

# #调用time模块
# import time
# print(time.ctime())  #time.ctime()获取当前时间
#
# from time import ctime  #直接引入.ctime()
# print(ctime())
#
# from time import ctime,sleep  #直接引入.ctime()
# sleep(2)
#
# from time import sleep as sys_sleep  #如果引入的函数与自己定义的函数重名，用as 对进入的函数重命名
#
# def sleep(aec):
#     print('this is defined sleep()')

#调用defclass模块的add函数
from chs.chs1.defclass import add
print(add(2,3))


import sys # sys模块包含了与Python解释器和它的环境有关的函数。
#__file__获取文件路径，调用os.path的abspath(__file__)可获取文件绝对路径，dirname()获取上级目录
from os.path import dirname,abspath
property_path =dirname(dirname(abspath(__file__)))
sys.path.append(property_path+"\\chongshi") #将该路径与\\chongshi目录拼接，可得到defclass文件所在路径，添加到path即可

from chs.chs1.defclass import add
c=add(2,3)
print(c)


