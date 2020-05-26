# -*- coding: utf-8 -*-
# @Time : 2020/5/22 17:24
# @Author : qxm
# @FileName: test_appium.py

"""
APP Calculator
"""

from appium import webdriver
from time import sleep

desired_caps = {
    'deviceName':'Android Emulator',
    'automationName': 'appium',
    'platformName': 'Android',
    'platformVersion':'10.0',
    'appPackage':'com.android.calculator2',
    'appActivity':'.Calculator',
}

# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub',desired_caps)
sleep(5)
driver.implicitly_wait(15)
# driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
# driver.find_element_by_id("com.android.calculator2:id/op_add").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
# driver.find_element_by_id("com.android.calculator2:id/eq").click()

driver.find_element_by_id('com.android.calculator2:id/digit7').click()
driver.find_element_by_id('com.android.calculator2:id/plus').click()
driver.find_element_by_id('com.android.calculator2:id/digit3').click()
driver.find_element_by_id('com.android.calculator2:id/equal').click()

driver.quit()