#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import unittest, time,os,sys #引入unittest包 和time库
from loan2.alogin_case import loginpublic #引入登录文件
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

# 继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class Login(unittest.TestCase):
    # 启动浏览器、访问地址模块
#setUpModule/tearDownModule为整个模块开始与结束执行，setUpClass和tearDownClass为整个类运行一次;
# setUp和tearDown在每个测试方法之前和之后运行.
    @classmethod
    def setUpClass(self):
      loginpublic.LoginPublic.setUp(self)

   # 登录用例(test_login中放置的就是我们的测试脚本)
    def test_login(self):
       u"""自动登录"""
       driver = self.driver
       driver.get(self.base_url + "/") # 基于当前url
       driver.maximize_window()

       # 调用登录模块
       loginpublic.LoginPublic.loginApi(self)

      # 断言 获得登录成功的用户，用户名是否等于admin，不等于将抛出异常
       driver.implicitly_wait(30)
       now_user=driver.find_element_by_class_name("user-info").text
       if now_user == u'当前用户： admin':
           print('登录成功', now_user)
       else:
           raise NameError('user name error!')
       time.sleep(0.5)
       print('登录成功', now_user)

    @classmethod
    def tearDownClass(self):
      # 调用退出模块
      loginpublic.LoginPublic.tearDown(self)


# if __name__ == '__main__':
#     testunit = unittest.TestSuite()
#     testunit.addTest(unittest.makeSuite(Login))
#     # 取前面时间
#     now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
#     # 把当前时间加到报告中,定义报告存放路径，支持相对路径
#     filename = "D:\\xiazaitp\\" + now + 'result.html'  # 定义报告存放路径，支持相对路径
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp, title="自动登录测试报告", description="报告详细描述")
#     runner.run(testunit)
#     fp.close()


# open有很多打开模式。a表示append附加方式，r表示read读，w表示write，+表示读写模式。，b表示二进制，t表示文本模式，t是默认的模式。
# a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# r+     以读写模式打开
# w+     以读写模式打开 (参见 w )
# a+     以读写模式打开 (参见 a )
# rb     以二进制读模式打开
# wb     以二进制写模式打开 (参见 w )
# ab     以二进制追加模式打开 (参见 a )
# rb+    以二进制读写模式打开 (参见 r+ )
# wb+    以二进制读写模式打开 (参见 w+ )
# ab+    以二进制读写模式打开 (参见 a+ )