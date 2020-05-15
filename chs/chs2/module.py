# -*- coding: utf-8 -*-
# @Time : 2020/4/11 15:28
# @Author : qxm
# @FileName: module.py

from selenium import webdriver
import unittest,time
from chs.chs2.configure import getConfig

# 继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
# class CheDaiLogin(unittest.TestCase): #与login_test中class Login 连用
class CheDaiLogin():
    #__init__()初始化方法中接收driver驱动并赋值给self.driver
    def __init__(self,driver):
        self.driver=driver

    def setUp(self):
      """#setUp用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。"""
      driver=self.driver
      driver.get('http://183.62.97.141:9080')
      # self.base_url='http://183.62.97.141:9080'
      driver.maximize_window()

    def login(self):
    # def login(self,user,password):  #将登录名密码参数化，在调用时传参
      """登录"""
      user = getConfig('Chedai', 'user')
      password = getConfig('Chedai', 'password')

      driver=self.driver
      # driver = webdriver.Chrome()
      # driver.get(self.base_url)
      driver.find_element_by_id('loginId').clear()
      driver.find_element_by_id('loginId').send_keys(user)
      driver.find_element_by_id('password').clear()
      driver.find_element_by_id('password').send_keys(password)
      # driver.find_element_by_id('captchaCode').send_keys("ABCD") #验证码
      # driver.find_element_by_id("subButton").click()
      time.sleep(8)

    def logout(self):
        """退出"""
        self.driver.quit()
        # self.driver.close()

