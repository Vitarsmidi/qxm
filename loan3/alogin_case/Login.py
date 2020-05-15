#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import unittest, time,os,sys #引入unittest包 和time库
from loan3.alogin_case import LoginPublic #引入登录文件
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

# 继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class Login(unittest.TestCase):
    # 启动浏览器、访问地址模块
    @classmethod
    def setUpClass(self):
      LoginPublic.LoginPublic.setUp(self)

   # 登录用例(test_login中放置的就是我们的测试脚本)
    def test_login(self):
       u"""自动登录"""
       # 调用登录模块
       LoginPublic.LoginPublic.test_login(self)

    @classmethod
    def tearDownClass(self):
      # 调用退出模块
      LoginPublic.LoginPublic.tearDown(self)


if __name__ == '__main__':
    testunit = unittest.TestSuite() # 定义一个单元测试容器
    testunit.addTest(unittest.makeSuite(Login)) # 将测试用例加入到测试容器中
    # 取当前时间,把当前时间加到报告中,定义报告存放路径，支持相对路径
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))

    # #直接将结果输出到控制台 (控制台、测试报告txt、测试报告html任意选一项，不能同时输出)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testunit)




