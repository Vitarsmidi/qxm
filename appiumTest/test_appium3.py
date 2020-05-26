# -*- coding: utf-8 -*-
# @Time : 2020/5/22 19:22
# @Author : qxm
# @FileName: test_appium2.py

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import unittest, time, os

"""
APP 原生 联系人
"""

caps = {}
caps['deviceName'] = 'Android Emulator'
caps['automationName'] = 'Appium'
caps['platformName'] = 'Android'
caps['platformVersion'] = '8.1.0'
caps['appPackage'] = 'com.android.contacts'
caps['appActivity'] = '.activities.PeopleActivity'
caps['appWaitDuration'] = 20000

caps['noReset'] =True

driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
# driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub',caps)
sleep(3)
driver.implicitly_wait(15)

#单击添加按钮
TouchAction(driver).tap(x=942,y=1635).perform()

#输入联系人信息
driver.find_element_by_android_uiautomator('text("Name")').send_keys("Aom")
driver.find_element_by_android_uiautomator('text("Phone")').send_keys("13700137001")
#保存
driver.find_element_by_id("com.android.contacts：id/menu_save").click()

driver.quit()

