# -*- coding: utf-8 -*-
# @Time : 2020/4/20 10:16
# @Author : qxm
# @FileName: test_baidu.py


from parameterized import parameterized   
from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
登陆baidu.com，通过parameterized实现参数化，在一条用例里查询多个关键字

parameterized.expand 装饰器 ,每个元组认为是一条测试用例；测试报告中会添加case1/case2标记每一条用例
"""

class TestBaidu(unittest.TestCase):
    """ 百度搜索测试方法"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url='https://www.baidu.com/'
        cls.driver.maximize_window()
        sleep(1)

    def baidu_search(cls, search_keywew):
        """" 读取test_data数据"""
        cls.driver.get(cls.base_url)
        cls.driver.implicitly_wait(10)
        cls.driver.find_element_by_id("kw").send_keys(search_keywew)
        cls.driver.find_element_by_id("su").click()
        sleep(2)

   #通过parameterized实现参数化
    @parameterized.expand([('case1','unittest'), ('case2','testng')]) #添加要执行数据，每一条数据当做一条用例执行
    def test_search(cls,case,search_key):
        """"百度搜索关键字"""
        cls.baidu_search(search_key)
        cls.assertEqual(cls.driver.title,search_key + u"_百度搜索") #assertEqual(arg1, arg2, msg=None)断言，判断两者是否一致

    # @parameterized.expand([('case1', 'unittest'), ('case2', 'testng')])
    # def test_search(self, case, search_key):
    #     self.driver.get(self.base_url)
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_id("kw").send_keys(search_key)
    #     self.driver.find_element_by_id("su").click()
    #     sleep(2)
    #     self.assertEqual(self.driver.title, search_key + u"_百度搜索")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


##执行test开头的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)








