# -*- coding: utf-8 -*-
# @Time : 2020/4/11 16:58
# @Author : qxm
# @FileName: login_test.py

from time import sleep
from selenium import webdriver
from chs.chs2.module import CheDaiLogin
# from chs.chs2.read_txt import users #引入read_txt users
# from chs.chs2.read_csv import users #引入read_csv users
# from chs.chs2.read_json import users #引入read_json users
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包


driver =webdriver.Chrome()
chedailogin=CheDaiLogin(driver)

#调用CheDaiLogin方法中的setUp函数打开测试地址
chedailogin.setUp()
driver.implicitly_wait(10)

#调用login登录
chedailogin.login()
# chedailogin.login("admin","123456") #调用login登录函数并传参
# chedailogin.login(users[1] [0],users[0] [1]) #调用login登录函数并传参，[0] [0]txt中的第一行第一个参数
# chedailogin.login(users[1] [0],users[1] [1]) #调用login登录函数并传参，[0] [0]csv中的第二行第一个参数
# chedailogin.login(users[1] ['username'] ,users[1] ['password'] ) #调用login登录函数并传参，[0] [0]json中的第二行参数
sleep(6)

# 调用退出
# chedailogin.logout()













