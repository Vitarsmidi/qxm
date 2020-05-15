# -*- coding: utf-8 -*-
# @Time : 2020/4/5 22:18
# @Author : qxm
# @FileName: ifelse.py

# if /else <>
a = 2
b = 3
if a > b:
    print("a max")
else:
    print("b max")

result = 85
if result >= 90:
    print("优秀")
elif result >= 70:
    print("良好")
elif result >= 60:
    print("及格")
else:
    print("不及格")

# == !=
if 2 + 2 == 4:
    print("true")
else:
    print("false")

# in not in
s = "hello"
ss = "hello world"
if s in ss:
    print("contain")
else:
    print("not contain")

# ture /false
if True:
    print("true")
else:
    print("false")

# for /while
# 循环遍历字符串
for s in "hello":
    print(s)

# 列表循环
a = ["A", "B", "C"]
for b in a:
    print(b)

# 循环遍历5次 range()函数次数循环，默认从0开始
for i in range(5):
    print(i)

# 从1开始遍历
for i in range(1, 5):
    print(i)

# range(x,y,n)从x开始遍历,y结束，步长为n,以下应打印13579
# for i in range(1,10,2):
#     print(i)


"""python_1……99相加和"""
number = 0
for i in range(1, 100):
    number += i
print(number)

"""奇数之和"""
s = 0
for i in range(1, 100, 2):
    s = s + i
print(s)

s = 0
for i in range(1, 100):
    if i % 2 != 0:
        s = s + i
print(s)

"""偶数之和"""
rst = 0
for i in range(1, 100):
    if i % 2 == 0:
        rst += i
        # rst = rst + i
print(+rst)

s = 0
for i in range(2, 100, 2):
    s = s + i
print(s)

"""计算1-99之和: 
1.小于或等于10的(譬如：1+2+...+10)，全部相加； 
2.大于10的，如果十位数是偶数的，则计算他们之间的偶数之和(譬如：20+22+24+...+40+42..+86+88)； 
3.如果十位数是奇数的，则求他们之间的奇数之和(譬如：11+13...+97+99)
"""
# a = 0
# for i in range(1, 100):
#     if i <= 10:  # 小于或等于10
#         a += i
#     elif (i / 10) % 2 == 1:  # 十位数为奇数
#         if i % 2 == 0:  # 且为偶数
#             a += i  # 则求和
#         else:
#             continue
#     elif (i / 10) % 2 == 0:  # 十位数为偶数
#         if i % 2 != 0:  # 且为奇数
#             a += i  # 则求和
#         else:
#             continue
# print(a)

# a1 = 0
# a2 = 0
# a3 = 0
# for i in range(1, 100):
#     if i <= 10:  # 小于或等于10
#         a1 += i
# a2 = 0
# for i in range(1, 100):
#     if (i / 10) % 2 == 1:  # 十位数为奇数
#         if i % 2 == 0:  # 且为偶数
#             a2 += i  # 则求和
#         else:
#             continue
# print(a2)
#
# for i in range(1, 100):
#     if (i / 10) % 2 == 0:  # 十位数为偶数
#         if i % 2 != 0:  # 且为奇数
#             a3 += i  # 则求和
#         else:
#             continue
#
# print(a1+a2+a3)
