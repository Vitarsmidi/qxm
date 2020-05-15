# -*- coding: utf-8 -*-
# @Time : 2020/4/8 22:32
# @Author : qxm
# @FileName: cookie.py

import unittest, time #引入unittest包 和time库
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://183.62.97.141:9080/')
driver.maximize_window() #将浏览器最大化显示

cookie=driver.get_cookies() #获得所有cookie信息
print(cookie)
#添加cookie
driver.add_cookie({'name':'chedai','value':'value-aaa'})
#遍历指定的cookie
for cookie in driver.get_cookies():
    print("%s-> %s" %(cookie['name'],cookie['value']))


