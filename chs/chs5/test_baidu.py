# -*- coding: utf-8 -*-
# @Time : 2020/4/20 10:16
# @Author : qxm
# @FileName: test_baidu.py


import pytest
from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
1.引入pytest测试框架, pytest更简单灵活的单元测试框架,断言更方便
2.在Terminal命令框 切换到文件目录下，输入pytest运行文件 ；pytest 
  pytest执行文件和函数必须以test开头，不需要指定执行文件也可以自动执行该目录下test开头的.py文件,也可以指定(pytest test_baidu.py);
3.可通知设置run运行文件，file->Setting->Tools->Python Integrated Tools->项目名称->Default test runner->选择py.test
4.setup_module/teardown_module在当前文件中，所以用例前和最后执行一次
  setup_function/teardown_function 在每个用例前后执行一次
  setup和teardown在每个测试函数之前和之后执行一次
"""


def setup_module():
    """" 打开百度"""
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(1)
    assert (driver.title, "selenium" + u"_百度搜索")

# def test_search1(cls):
#     """" 百度搜索关键字selenium"""
#     # cls.driver = webdriver.Chrome()
#     cls.driver.get('https://www.baidu.com/')
#     cls.driver.find_element_by_id("kw").send_keys("selenium")
#     cls.driver.find_element_by_id("su").click()
#     sleep(1)
#     assert(cls.driver.title, "selenium" + u"_百度搜索")

def teardown_module(self):
    self.driver.quit()


#执行test开头的用例
    if __name__ == "__main__":
        pytest.main('-q test_baidu.py')





