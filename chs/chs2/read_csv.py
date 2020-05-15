# -*- coding: utf-8 -*-
# @Time : 2020/4/12 16:20
# @Author : qxm
# @FileName: read_csv.py

import csv
import codecs
from itertools import islice

#读取本地csv文件gbk、utf_8_sig 、unicode_escape
data= csv.reader(codecs.open('user_info.csv','r','gbk')) #codecs.open() 解码器，指定编码类型，reader读取

#存放用户数据
users=[]

#循环输出每行信息 islice(A,B,C) A指定迭代对象，B指定位置，C结束位
for line in islice(data, 1,None):
    users.append(line)

#打印
print(users)