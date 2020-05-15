# -*- coding: utf-8 -*-
# @Time : 2020/4/3 16:07
# @Author  : qxm
# @FileName: login.py

import unittest, time #引入unittest包 和time库
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #ActionChains类提供鼠标操作方法

driver = webdriver.Chrome()
# driver.get('http://172.17.255.229/')
# driver.get('https://car.100lending.com/')
# driver.get('http://10.31.1.142:3980/qubei_back_server/back/indexBack')
driver.get('http://183.62.97.141:9080/')
driver.maximize_window() #将浏览器最大化显示
driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id('captchaCode').send_keys("ABCD") #验证码
#driver.find_element_by_id("subButton").click()


time.sleep(3)

# driver.quit()
