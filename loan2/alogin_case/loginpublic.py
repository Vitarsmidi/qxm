#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import unittest, time
from loan2.alogin_case import LoginData #导入函数

# 通过两个变量，来接收调用函数获得用户名&密码
us, pw = LoginData.data()
print(us, pw)  # 打印两个变量

class LoginPublic(unittest.TestCase):

  # 浏览器访问地址模块
   def setUp(self):
    # setUp用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。
      self.driver = webdriver.Chrome()
      self.driver.implicitly_wait(30)
      self.base_url = "http://183.62.97.141:9080/"
      self.verificationErrors = []  #数组，脚本运行时的错误信息将被记录到这个数组中。
      self.accept_next_alert = True  # 变量，表示是否继续接受下一个警告，初始状态为True
      time.sleep(0.5)

   # login登陆模块
   def loginApi(self):
     driver = self.driver
     driver.implicitly_wait(30)
     driver.find_element_by_id("loginId").clear()
     driver.find_element_by_id("loginId").send_keys( us )
     driver.find_element_by_name("password").clear()
     driver.find_element_by_name("password").send_keys( pw )
     time.sleep(5)  # 输入验证码
     # driver.find_element_by_id("subButton").click() #点击登录

   # quit退出模块
   #tearDown（）方法在每个测试方法执行后调用，这个方法用于测试用例执行后的清理工作。
   def tearDown(self):
     self.driver.quit()
     # self.assertEqual([], self.verificationErrors)
     #通过assertEqual（）比较setUp前面的verificationErrors是否为空，为空则说明用例执行过程中未出现异常，否则抛出AssertionErrory异常。
