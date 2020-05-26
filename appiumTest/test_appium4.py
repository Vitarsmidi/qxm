# -*- coding: utf-8 -*-
# @Time : 2020/5/22 19:22
# @Author : qxm
# @FileName: test_appium2.py

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import unittest, time, os

"""
移动Web应用百度
"""

caps = {}
caps['deviceName'] = 'Android Emulator'
caps['automationName'] = 'appium'
caps['platformName'] = 'Android'
caps['platformVersion'] = '8.1.0'
caps['browserName'] = 'Chrome'
caps['appWaitDuration'] = 20000


driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
# driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub',caps)
sleep(3)
driver.implicitly_wait(15)

driver.get("https://m.baidu.com")
driver.implicitly_wait(15)
driver.find_element_by_id('index-kw').send_keys("Aom")
driver.find_element_by_id('index-bn').click()
sleep(3)

driver.quit()

