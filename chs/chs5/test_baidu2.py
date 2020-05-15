# -*- coding: utf-8 -*-
# @Time : 2020/4/20 10:16
# @Author : qxm
# @FileName: test_baidu.py

from chs.chs5.baidu_page2 import BaiduPage
from ddt import ddt ,data ,file_data,unpack
import pytest
from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
引入pytest测试框架, pytest更简单灵活的单元测试框架，也适用于unittest

"""

@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    @file_data('baidu_data.json')
    def test_search(self,search_key):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)

        page.search_input = search_key
        page.search_button.click()
        sleep(2)
        self.assertEqual(self.driver.title, search_key + u"_百度搜索")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


##执行test开头的用例
if __name__ == "__main__":
    pytest.main('-q test_baidu2.py')


# class TestBaidu(unittest.TestCase):
#     """ 百度搜索测试方法"""
#     @classmethod
#     def setUpClass (self):
#         """" 打开百度"""
#         self.driver = webdriver.Chrome()
#         self.driver.get('https://www.baidu.com/')
#         self.driver.maximize_window()
#         sleep(1)
#
#     def test_search1(self):
#         """" 百度搜索关键字selenium"""
#         self.driver.implicitly_wait(10)
#         self.driver.find_element_by_id("kw").send_keys("selenium")
#         self.driver.find_element_by_id("su").click()
#         sleep(1)
#         self.assertEqual(self.driver.title, "selenium" + u"_百度搜索")
#
#     def test_search2(self):
#         """" 百度搜索关键字unittest"""
#         self.driver.get('https://www.baidu.com/')
#         self.driver.implicitly_wait(10)
#         self.driver.find_element_by_id("kw").send_keys("unittest")
#         self.driver.find_element_by_id("su").click()
#         sleep(1)
#         self.assertEqual(self.driver.title, "unittest" + u"_百度搜索")
#
#
# # 在test_baidu2/test_baidu3中将实现一个用例里查询多个关键字
#
#     @classmethod
#     def tearDownClass(self):
#         self.driver.quit()
#
#
# ##执行test开头的用例
# if __name__ == "__main__":
#     pytest.main('-q test_baidu.py')






