#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time,datetime
import random
import string

url="http://172.17.255.228"
driver = webdriver.Firefox()
driver.get(url+":7080/login")
driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")
time.sleep(6)
##等待收入验证码
driver.find_element_by_id("subButton").click()
time.sleep(3)

driver.execute_script("addTab(\'/product/sporadic/list\',\'散标列表\')")
time.sleep(2)

driver.switch_to.frame("conframe")
driver.find_element_by_xpath('//button[@data-txnid="70002"]').click()
time.sleep(3)

driver.find_element_by_xpath('//button[@data-bb-handler="confirm"]').click()