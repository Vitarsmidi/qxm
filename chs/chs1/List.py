# -*- coding: utf-8 -*-
# @Time : 2020/4/4 22:03
# @Author : qxm
# @FileName: List.py

# lists=[1,2,3,'a',5]
# print(lists)

# #打印列表中第一个元素
# a = [1,3,5,"x",2,7]
# print(a[0])
# #打印列表中第3个元素
# a = [1,3,5,"x",2,7]
# print(a[2])

# #打印列表中最后一个元素
# a = [1,3,5,"x",2,7]
# print(a[-1])

# #修改列表中第四个元素为6
# a[3] = '6'
# print(a)

# #在列表末尾中添加元素
# a.append('8')
# print(a)

# #delete列表第一个元素
# a.pop(0)
# print(a)

# #set 去重排序
# b=[1,3,4,8,2,1,6,3,9,5]
# c=list(set(b))
# print(c)

# #.sort排序不去重
# b=[1,3,4,8,2,1,6,3,9,5]
# b.sort()
# print(b)

# #去重不排序
# b=[1,3,4,8,2,1,6,3,9,5]
# c=list(set(b))
# c.sort(key=b.index)
# print(c)

# #冒泡排序 len() 方法返回对象（字符、列表、元组等）长度或项目个数。
# b=[1,3,4,8,2,1,6,3,9,5]
# for i in range(len(b)):   # 外循环控制遍历的次数
#     for j in range(len(b)-1):  # 内循环控制遍历到哪一位
#         if b[j]>b[j+1]:
#             b[j],b[j+1]=b[j+1],b[j]
#     print(b)


# #元组 () 元组和列表的区别：列表是可变的，即可修改删除增加其中元素，元组不可以改变
# tup1=('a','b',1,2)
# tup2=(1,3,4,2)
# print(tup1[0]) #第1个
# print(tup2[0:2]) #从第1个开始，一共两个
#
# tup3=tup1+tup2
# print(tup3)


#字典{}，每个元素由一个key和一个value组成，key和value用：隔开,key唯一value可以相同，元素间用，隔开
a={"name":"test",'password':123456}
print(a.keys())  #打印字典中所有的key
print(a.values()) #打印字典中所有的value

a['age']=22 #向字典添加key和value
print(a.keys())  #打印字典中所有的key

a.pop('name') #删除值为name的key
print(a.keys())  #打印字典中所有的key

print(a.items()) #打印字典以列表方法返回

#循环打印字典key和value
for k,v in a.items():
    print('a keys is %r' %k)
    print('a values is %r' %v)