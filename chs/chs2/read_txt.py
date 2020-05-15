# -*- coding: utf-8 -*-
# @Time : 2020/4/11 22:42
# @Author : qxm
# @FileName: read_txt.py

#读取txt文件
with(open('user_info.txt', 'r')) as user_file:
    data=user_file.readlines()
    #.read()读取整个文件；readline()读取一行，readlines()读取所有行

#格式化处理
users=[]
for line in data: #循环txt中的每一行数据
    user = line[:-1].split(":") #每一行数据结尾有一个换行符\n 所以用:-1对字符串切片，省略最后一个字符\n；split(":")每行数据拆分
    users.append(user)  #append() 将每行数据追加到user数组中

# # 打印 users二位数组
# print(users)
