# -*- coding: utf-8 -*-
# @Time : 2020/4/16 22:37
# @Author : qxm
# @FileName: login_test2.py

from time import sleep
from selenium import webdriver
import unittest, time,os,sys #引入unittest包 和time库
from chs.chs2.module import CheDaiLogin
# from chs.chs2.read_txt import users #引入read_txt users
# from chs.chs2.read_csv import users #引入read_csv users
# from chs.chs2.read_json import users #引入read_json users
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

"""引入unittest框架"""
"""
继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
setUpModule/tearDownModule为整个模块开始与结束执行，setUpClass和tearDownClass为整个类开始和结束运行一次;
setUp和tearDown在每个测试方法之前和之后运行;

TestSuite() 套件 通过addTest()添加要执行的case
"""

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        CheDaiLogin.setUp(self)  # 调用CheDaiLogin方法中的setUp函数打开测试地址
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_login(self):
        driver = self.driver
        CheDaiLogin.login(self) # 调用CheDaiLogin方法中的login登录脚本
        # chedailogin.login("admin","123456") #调用login登录函数并传参
        # chedailogin.login(users[1] [0],users[0] [1]) #调用login登录函数并传参，[0] [0]txt中的第一行第一个参数
        # chedailogin.login(users[1] [0],users[1] [1]) #调用login登录函数并传参，[0] [0]csv中的第二行第一个参数
        # chedailogin.login(users[1] ['username'] ,users[1] ['password'] ) #调用login登录函数并传参，[0] [0]json中的第二行参数


    def tearDown(self):
        CheDaiLogin.logout(self)

if __name__ == "__main__":
        unittest.main(verbosity=2)
        testunit = unittest.TestSuite()  # 定义一个单元测试容器,创建一个测试套件
        testunit.addTest(unittest.makeSuite(Login))  # 将测试用例加入到测试容器中

        # #创建测试套件
        # testunit = unittest.TestSuite()  # 定义一个单元测试容器,创建一个测试套件
        # testunit.addTest(Login("setUp")) # 添加要执行的方法（按顺序）
        # testunit.addTest(Login("test_login"))
        # #创建测试运行器，调用TextTestRunner类的run()方法运行测试套件
        # runner = unittest.TextTestRunner(verbosity=2)
        # runner.run(testunit)

        #也可以通过方法名test_a/test_b/test_1/test_2安排执行顺序

