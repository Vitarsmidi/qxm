# -*- coding: utf-8 -*-
# @Time : 2020/4/15 21:39
# @Author : qxm
# @FileName: public.py

from selenium import webdriver
import unittest
from time import sleep
from chs.chs2.configure import getConfig

"""
封装一些登陆的常用方法

#setUp用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。"""
""" __init__()初始化方法中接收driver驱动并赋值给self.driver 
"""

class LoginPublic(unittest.TestCase):

    def __init__(self,driver):
        self.driver=driver

    def setUp(self):
        driver=self.driver
        driver.get('http://183.62.97.141:9080')
        driver.maximize_window()
        self.verificationErrors = []  #数组，脚本运行时的错误信息将被记录到这个数组中。
        self.accept_next_alert = True  # 变量，表示是否继续接受下一个警告，初始状态为True

    def login(self):
        # def login(self,user,password):  #将登录名密码参数化，在调用时传参
        """登录"""
        user = getConfig('Chedai', 'user')
        password = getConfig('Chedai', 'password')

        driver=self.driver
        # driver = webdriver.Chrome()
        driver.find_element_by_id('loginId').clear()
        driver.find_element_by_id('loginId').send_keys(user)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(password)
        # driver.find_element_by_id('captchaCode').send_keys("ABCD") #验证码
        # driver.find_element_by_id("subButton").click()
        sleep(6)

    def logout(self):
        """退出"""
        self.driver.quit()
        # self.driver.close()

    # tearDown（）方法在每个测试方法执行后调用，这个方法用于测试用例执行后的清理工作。
    def tearDown(self):
        self.driver.quit()
