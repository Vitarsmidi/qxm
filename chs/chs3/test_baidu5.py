# -*- coding: utf-8 -*-
# @Time : 2020/4/28 21:16
# @Author : qxm
# @FileName: test_baidu.py


from ddt import ddt ,data ,file_data,unpack
from time import sleep
from selenium import webdriver
import unittest, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
登陆baidu.com，通过 DDT数据驱动 实现参数化，在一条用例里查询多个关键字

DDT(Data-Driven Tests 数据驱动，使用不同的测试数据运行一个测试用例，并展示为多个测试用例)
@data（直接输入测试数据）
@file_data（可以从json或者yaml中获取测试数据）
@unpack分解数据，如data([a,d]) 若无unpack，则[a,b]当成一个参数传入用例；若有unpack，那么[a,b]被分解开，按照用例中的两个参数传递
"""

#方法必须以@ddt装饰
@ddt
class TestBaidu(unittest.TestCase):
    """ 百度搜索测试方法"""
    @classmethod
    def setUpClass(self):
        """" 打开百度"""
        self.driver = webdriver.Chrome()
        self.base_url='https://www.baidu.com/'
        self.driver.maximize_window()


   #通过@data以列表/元组/字典形式实现参数化
    @data(('case1','unittest'), ('case2','testng'))
    @unpack
    def test_search(self,case,search_key):
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








