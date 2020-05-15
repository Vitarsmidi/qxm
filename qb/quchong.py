
# #方法一: 使用内置set方法来去重排序
# a = [2,1,3,1,3,5,6,7,8,2,4]
# b = list(set(a))
# print(b)

# #方法一: 使用内置set方法来去重排序
# a = [2,1,3,1,3,5,6,7,8,2,4]
# b = set(a)
# print(b)

# # 方法三: 使用字典中sort()的方法来排序不去重
# a =  [2,1,3,1,3,5,6,7,2,4,8]
# a.sort()
# print(a)

# # 方法二: 去重不排序,先用set()去重，然后sort()排序
# a =  [2,1,3,1,3,5,6,7,2,4,8]
# b = list(set(a))
# b.sort(key=a.index)
# print(b)

# # 合并ab去重排序
# a=[1,5,7,3,9,2]
# b=[2,3,6,4,8,1]
# c=a+b
# d=list(set(c))
# print(d)

# #coding = utf-8
# a = [1,2,3,3,4,2,3,4,5,6,1,7,8]
# news_a = []
# for id in a:
#     if id not in news_a:
#         news_a.append(id)
# print(news_a)


# L = [1,3,3,4,2,1,3,4,5,6,7,8,6,5,4,2]
# def sort_(L):
#     if len(L) <= 1:
#         return L
#     mid = L[0]
#     low = [item for item in L if item < mid]
#     high = [item for item in L if item > mid]
#     return sort_(low) + [mid] + sort_(high)
# print (sort_(L))


# import random
# L = [1,2, 3, 8, 4, 9, 5, 6, 5, 6, 10, 17, 11, 2]
# def sort(L):
#     if len(L) < 2: return L
#     pivot_element = random.choice(L)
#     small = [i for i in L if i < pivot_element]
#     # medium = [i for i in L if i==pivot_element]
#     large = [i for i in L if i > pivot_element]
#     return sort(small) + [pivot_element] + sort(large)
# print(sort(L))

#一行代码输出 1-100 之间的所有偶数。
# print(list(i for i in range(1, 101) if i%2 == 0))
#一行代码输出 1-100 之间的所有奇数。
# print(list(i for i in range(1, 101) if i%2 == 1))

'''
冒泡排序算法的原理如下：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
 len() 方法返回对象（字符、列表、元组等）长度或项目个数。
'''
# # # ##冒泡算法1
# a = [2, 1, 3, 8, 4, 9, 5, 7, 6, 10, 15, 11]
# for i in range(len(a) - 1):  # 外循环控制遍历的次数
#     for j in range(len(a) - 1):  # 内循环控制遍历到哪一位
#         if a[j] > a[j + 1]:  # <则从大到小
#             a[j], a[j + 1] = a[j + 1], a[j]  # 如果后一个数比前一个数大，两个数就交换位置a[j],a[j+1]
#             print(a)

"""当遍历一轮发现没有元素交换时，排序即可结束。"""
# a = [2, 1, 3, 8, 4, 9, 5, 7, 6, 10, 15, 11]
# for i in range(len(a) - 1):  # 外循环控制遍历的次数
#     swap = False  # 每一轮都要重置一次swap的值，所以要写在这边
#     for j in range(len(a) - 1):  # 内循环控制遍历到哪一位
#         if a[j] > a[j + 1]:  # <则从大到小
#             swap = True  # 每次交换就改变swap的值
#             a[j], a[j + 1] = a[j + 1], a[j]  # 如果后一个数比前一个数大，两个数就交换位置a[j],a[j+1]
#             if not swap:  # 当swap为False时，退出循环
#                 break
#             print(a)


"""当列表尾部部分元素提前完成顺序时，不再进行比较。"""
# L = [2, 1, 3, 8, 4, 9, 5, 7, 6, 10, 15, 11]
# maxindex = len(L)  # 索引的初始值应为原先下面len(L)-i的第一个值，即len(L)
# for i in range(len(L) - 1):
#     for j in range(1, maxindex):  # 将之前的len(L)-i替换为上次最后赋值的索引ordindex
#         if L[j - 1] > L[j]:
#             L[j - 1], L[j] = L[j], L[j - 1]
#             maxindex = j  # 记录索引，多次循环过后，ordindex存储的是最后被赋值的索引
#             print(L)


"""鸡尾酒排序，双向比较交换，无交换时排序结束。"""
# L = [2, 1, 3, 8, 4, 9, 5, 7, 6, 10, 15, 11]
# for i in range(len(L) // 2):
#     swap = False
#     for j in range(i + 1, len(L) - i):  # 起始和结尾都在发生变化
#         if L[j - 1] > L[j]:
#             L[j - 1], L[j] = L[j], L[j - 1]
#     for k in range(len(L) - i - 2, i, -1):  # 倒序来进行小值往前走的操作
#         if L[k - 1] > L[k]:
#             L[k - 1], L[k] = L[k], L[k - 1]
#             swap = True  # 只需将交换变量放在最后面的循环即可
#             if not swap:
#                 break
#             print(L)

"""最终优化版本"""
# L = [2, 1, 3, 8, 4, 9, 5, 7, 6]
# minindex = 0
# maxindex = len(L)
# for i in range(len(L) // 2):
#     swap = False
#     for j in range(minindex + 1, maxindex):
#         if L[j - 1] > L[j]:
#             L[j - 1], L[j] = L[j], L[j - 1]
#             maxindex = j
#     for k in range(maxindex - 1, minindex, -1):
#         if L[k - 1] > L[k]:
#             L[k - 1], L[k] = L[k], L[k - 1]
#             minindex = k  # 当前半段提前完成排序时也不用再比较了
#             swap = True
#             if not swap:
#                 break
#             print(L)
