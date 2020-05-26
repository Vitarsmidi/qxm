# -*- coding: utf-8 -*-
# @Time : 2020/5/22 19:22
# @Author : qxm
# @FileName: test_appium2.py

from appium import webdriver
from time import sleep
import unittest, time, os

"""
APP Calculator
"""


desired_caps = {
    'deviceName':'OPPO R11',
    'automationName': 'Appium',
    'platformName': 'Android',
    'platformVersion':'8.1.0',
    # 'app': "G:\\calc.apk",
    'appPackage':'com.mt.mtxx.mtxx',
    'appActivity':'com.meitu.mtxx.MainActivity',
    # 'appActivity': 'com.ibox.calculators.SplashActivity',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub',desired_caps)
# sleep(5)
# driver.implicitly_wait(15)
# driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
# driver.find_element_by_id("com.android.calculator2:id/op_add").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
# driver.find_element_by_id("com.android.calculator2:id/eq").click()
# #
# driver.find_element_by_id('com.android.calculator2:id/digit7').click()
# driver.find_element_by_id('com.android.calculator2:id/plus').click()
# driver.find_element_by_id('com.android.calculator2:id/digit3').click()
# driver.find_element_by_id('com.android.calculator2:id/equal').click()

driver.quit()


if __name__ == '__main__':
    unittest.main()
