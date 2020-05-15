#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import unittest, time,os,sys #引入unittest包 和time库
from loan3.bdengji_case import DengJiPublic
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

# 继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class LoginToDengJi(unittest.TestCase):
    # 启动浏览器、访问地址模块
    @classmethod
    def setUpClass(self):
        DengJiPublic.DengJiPublic.setUp(self)

   # 登录用例(test_login中放置的就是我们的测试脚本)
    def test_01_login(self):
       u"""自动登录"""
       # 调用登录模块
       DengJiPublic.DengJiPublic.test_01_login(self)

    # 登录用例(test_login中放置的就是我们的测试脚本)
    def test_02_khdj(self):
        # 调用'客户登记'模块
        DengJiPublic.DengJiPublic.test_02_khdj(self)

    @classmethod
    def tearDownClass(self):
      # 调用退出模块
      DengJiPublic.DengJiPublic.tearDown(self)


if __name__ == '__main__':
    testunit = unittest.TestSuite() # 定义一个单元测试容器
    testunit.addTest(unittest.makeSuite(LoginToDengJi)) # 将测试用例加入到测试容器中
    # 取当前时间,把当前时间加到报告中,定义报告存放路径，支持相对路径
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))

    # #直接将结果输出到控制台 (控制台、测试报告txt、测试报告html任意选一项，不能同时输出)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testunit)

    # # #将测试结果输出到测试报告html中  #( wb+ 以二进制读写模式打开)
    # with open("D:\\xiazaitp\\" + now +'result.html', 'wb+') as fp:
    #     runner = HTMLTestRunner(stream=fp,title=u'自动登录测试报告',description=u'报告详细描述',verbosity=2)
    #     runner.run(testunit)
    #     fp.close()

    # #将测试结果输出到测试报告#( a  以追加模式打开)
    # with open( "D:\\xiazaitp\\"  + now +'result.txt', 'a') as fp:
    #     runner = unittest.TextTestRunner(stream=fp, verbosity=2)
    #     runner.run(testunit)
    #     fp.close()


