# -*- coding: utf-8 -*-
# @Time : 2020/4/15 21:47
# @Author : qxm
# @FileName: login_test.py

from selenium import webdriver
from time import sleep
import unittest, time,os,sys #引入unittest包 和time库
from chs.chs3.public import LoginPublic
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

"""
引入unittest框架，实现自动登陆并断言
# 继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
#setUpModule/tearDownModule为整个模块开始与结束执行，setUpClass和tearDownClass为整个类运行一次;
# setUp和tearDown在每个测试方法之前和之后运行;
"""

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        LoginPublic.setUp(self)
        self.base_url = "http://183.62.97.141:9080"

    def test_login(self):
       u"""自动登录"""
       driver = self.driver
       # driver.get(self.base_url + "/") # 基于当前url

       # 调用登录模块
       LoginPublic.login(self)
       # LoginPublic.login("admin","123456") #调用login登录函数并传参
       # LoginPublic.login(users[1] [0],users[0] [1]) #调用login登录函数并传参，[0] [0]txt中的第一行第一个参数
       # LoginPublic.login(users[1] [0],users[1] [1]) #调用login登录函数并传参，[0] [0]csv中的第二行第一个参数
       # LoginPublic.login(users[1] ['username'] ,users[1] ['password'] ) #调用login登录函数并传参，[0] [0]json中的第二行参数

      # 断言 获得登录成功的用户，用户名是否等于admin，不等于将抛出异常
       driver.implicitly_wait(30)
       now_user=driver.find_element_by_class_name("user-info").text
       if now_user == u'当前用户： admin':
           print('登录成功', now_user)
       else:
           raise NameError('user name error!')

       self.assertIn(now_user,'当前用户： admin') #assertIn(a,b)断言，a is b
       print('登录成功', now_user)


       time.sleep(2)

    @classmethod
    def tearDownClass(self):
      # 调用退出模块
      LoginPublic.tearDown(self)




if __name__ == '__main__':
    testunit = unittest.TestSuite() # 定义一个单元测试容器，创建一个测试套件
    testunit.addTest(unittest.makeSuite(Login)) # 将测试用例加入到测试容器中
    # 取当前时间,把当前时间加到报告中,定义报告存放路径，支持相对路径
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))

    # # #直接将结果输出到控制台 (控制台、测试报告txt、测试报告html任意选一项，不能同时输出)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(testunit)

    # #将测试结果输出到测试报告html中  #( wb+ 以二进制读写模式打开)
    with open("G:\\Report\\" + now +'result.html', 'wb+') as fp:
        runner = HTMLTestRunner(stream=fp,title=u'自动登录测试报告',description=u'报告详细描述',verbosity=2)
        runner.run(testunit)
        fp.close()