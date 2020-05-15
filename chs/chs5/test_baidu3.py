# -*- coding: utf-8 -*-
# @Time : 2020/4/20 10:16
# @Author : qxm
# @FileName: test_baidu.py

from ddt import ddt ,data ,file_data,unpack
import pytest
import math
from time import sleep
from selenium import webdriver
# import unittest, time, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
pytest 支持使用测试类，必须以Test开头(大写)

setup_class/teardown_class在测试类开始与结束执行一次
setup_method/teardown_method 在每个测试方法开始与结束执行一次
setup和teardown 在每个测试方法开始与结束执行一次

在执行时生成测试报告
1.pytest test_baidu3.py --junit-xml=./report/log.xml   生成xml文件
2.pytest test_baidu3.py --pastebin=all  生成连接
3.pytest test_baidu3.py --html=./report/report.html  生成html文件

pytest test_dir/test_baidu.py --html=./report/report.html
"""

class TestBaidu:

    @classmethod
    def setup_class(cls):
        # print("setup_class")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com")

    def test1(cls):
        cls.driver.get("https://www.baidu.com")
        cls.driver.implicitly_wait(10)
        cls.driver.find_element_by_id("kw").send_keys("selenium")
        cls.driver.find_element_by_id("su").click()
        sleep(2)
        assert cls.driver.title, "selenium" + u"_百度搜索"


    @classmethod
    def teardown_class(self):
        self.driver.quit()


##执行test开头的用例
if __name__ == "__main__":
    pytest.main('-q test_baidu3.py')










