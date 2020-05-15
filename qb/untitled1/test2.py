# coding = utf-8
import unittest, time #引入unittest包 和time库
from selenium import webdriver
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://car.100lending.com/')
driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")
#driver.find_element_by_id("subButton").click()
time.sleep(3)
# driver.quit()


