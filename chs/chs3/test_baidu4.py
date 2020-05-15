# -*- coding: utf-8 -*-
# @Time : 2020/4/28 10:16
# @Author : qxm
# @FileName: test_baidu.py

import csv,codecs
from parameterized import parameterized
from itertools import islice
from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
登陆baidu.com，通过parameterized + csv文件实现参数化，在一条用例里查询多个关键字
parameterized.expand 装饰器
"""

test_data = []  # 创建一个数组 将baidu_data.csv数据存到test_data
with codecs.open('baidu_data.csv', 'r', 'utf_8_sig') as f:  # 打开读取csv件
    data = csv.reader(f)
    for line in islice(data, 1, None):  # islice(文件名, 开始行, 结束行) 循环读取文件中哪些行
        test_data.append(line)


class TestBaidu(unittest.TestCase):
    """ 百度搜索测试方法"""
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.base_url='https://www.baidu.com/'
        self.driver.maximize_window()


   #通过parameterized实现参数化
    @parameterized.expand(test_data) #添加要执行数据，每一条数据当做一条用例执行
    def test_search(self,case,search_key):
        """"百度搜索关键字"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(self.driver.title,search_key + u"_百度搜索")


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


##执行test开头的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)








