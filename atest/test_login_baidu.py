# -*- coding: utf-8 -*-
# @Time : 2020/5/17 10:47
# @Author : qxm
# @FileName: test_print.py
import pytest
from time import sleep
from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(1)
    assert driver.title, "selenium" + u"_百度搜索"
    driver.quit()

