# -*- coding: utf-8 -*-
# @Time : 2020/4/20 10:16
# @Author : qxm
# @FileName: test_baidu.py

import csv,codecs
from itertools import islice   # itertools迭代器，用于高效循环的迭代函数集合，islice(文件名, 开始行, 结束行):
from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库


"""
登陆baidu.com，并查询两个关键字，将关键字数据放在csv文件读取

数据驱动，读取csv文件实现参数化
文件读取：
codecs.open(filepath,method,encoding)
filepath--文件路径
method--打开方式，r为读，w为写，rw为读写
encoding--文件的编码，中文文件使用utf-8
"""

class TestBaidu(unittest.TestCase):
    """ 百度搜索测试方法"""
    @classmethod
    def setUpClass(self):
        """" 打开百度"""
        self.driver = webdriver.Chrome()
        self.base_url='https://www.baidu.com/'
        self.driver.maximize_window()
        self.test_data=[] #创建一个数组 将baidu_data.csv数据存到test_data
        with codecs.open('baidu_data.csv','r','utf_8_sig') as f:  #打开读取csv件
            data = csv.reader(f)
            for line in islice(data,1,None):  #islice(文件名, 开始行, 结束行) 循环读取文件中哪些行
                self.test_data.append(line)

        sleep(1)

    def baidu_search(self,search_key):
        """" 读取test_data数据"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)

    def test_search_testng(self):
        """" 百度搜索testng"""
        self.baidu_search(self.test_data[1] [1])  #读取test_data数据第一行第二个字段数据
        sleep(2)

    def test_search_unittest(self):
        """" 百度搜索unittest"""
        self.baidu_search(self.test_data[0] [1])  #读取test_data数据第一行第二个字段数据
        sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


##执行test开头的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)








