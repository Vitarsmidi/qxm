#coding=utf-8
from __future__ import division
from selenium import webdriver
import time,sys

url="http://172.17.255.228"
driver = webdriver.Firefox()
driver.get(url+":8080/user/login")
driver.find_element_by_name("loginId").send_keys("18818529673")
driver.find_element_by_name("password").send_keys("aaa12345")
time.sleep(6)
##等待输入验证码
driver.find_element_by_xpath('//a[@class="btn"]').click()
time.sleep(3)
driver.get(url+":8080/product/detail/70002")

#yuamount = driver.find_element_by_xpath('//div[@class="inf-r"]/span[1]/b[@class="min-sy"]').text
yuamount = float(driver.find_element_by_xpath('//div[@class="inf-r"]/span[1]/b[@class="min-sy"]').text.replace(",",""))
print "可投剩余金额：",yuamount

keamount = float(driver.find_element_by_xpath('//div[@class="inf-r"]/span[2]/b[@class="min-mg"]').text.replace(",",""))
print "用户可用余额：",keamount
driver.find_element_by_name("investAmount").clear()

if keamount>=yuamount:
    driver.find_element_by_name("investAmount").send_keys(int(yuamount/3))
elif keamount<yuamount:
    if keamount>=100:
        minadd = int(driver.find_element_by_xpath('//form[@id="form"]/span/b[2]').text)
        driver.find_element_by_name("investAmount").send_keys(int(minadd*(keamount//minadd)))
        print int(keamount)
    else:
        print "不足起投金额100元，投资终止"
        driver.close()
        sys.exit(0)

driver.find_element_by_xpath('//a[@class="btn clk-lay realName-btn"]').click()
time.sleep(2)
driver.find_element_by_xpath('//span[@class="touzi-checkbox"]').click()
time.sleep(2)
driver.find_element_by_xpath('//a[@class="btn toclick"]').click()