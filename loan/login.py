# coding = utf-8
import unittest, time #引入unittest包 和time库
from selenium import webdriver

driver = webdriver.Chrome()
# driver.get('http://172.17.255.229/')
# driver.get('https://car.100lending.com/')
driver.get('http://10.31.1.142:3980/qubei_back_server/back/indexBack')
driver.maximize_window() #将浏览器最大化显示
driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")
#driver.find_element_by_id("subButton").click()
time.sleep(3)

driver.quit()
