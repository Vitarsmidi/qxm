# -*- coding: utf-8 -*-
# @Time : 2020/5/3 18:27
# @Author : qxm
# @FileName: baidu_page.py

from chs.chs4.baidu_page2 import BaiduPage
from ddt import ddt ,data ,file_data,unpack
from time import sleep
from selenium import webdriver
import unittest, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
调用baidu_page2进行具体操作

使用BaiduPage类及它所继承父类的一些方法，进行百度搜索关键字
"""

@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)


    @file_data('baidu_data.json')
    def test_search(self,search_key):
        page = BaiduPage(self.driver)
        # page.get("https://www.baidu.com")
        # self.driver.implicitly_wait(10)

        page.search_input = search_key
        page.search_button.click()
        sleep(2)
        self.assertEqual(self.driver.title, search_key + u"_百度搜索")


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


##执行test开头的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)