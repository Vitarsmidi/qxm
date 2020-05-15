# -*- coding: utf-8 -*-
# @Time : 2020/4/9 22:54
# @Author : qxm
# @FileName: huakuai.py

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

# #...滑块...#
# driver =webdriver.Chrome()
# driver.get("https://www.helloweba.com/demo/2017/unlock")
# # driver.maximize_window()
# driver.implicitly_wait(10)
#
# #定位滑块
# slder = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
# action = ActionChains(driver) #ActionChains 提供鼠标操作方法；通过perform()执行。见3.3.2.1shubiao.py
# action.click_and_hold(slder).perform()
# #click_and_hold() 单击鼠标左键 ，按住滑块
# #通过for 循环移动鼠标 ，移动完后抛UnexpectedAlertPresentException异常， break，捕捉后跳出循环。
# for index in range(100):
#     try:
#         action.move_by_offset(2,0).perform()  #ActionChains类action.move_by_offset(x,y)移动鼠标
#     except UnexpectedAlertPresentException:
#         break
#     action.reset_actions() #重置action清除之前的action
#     sleep(0.5)
#
# #打印警告框提示
# success_text =driver.switch_to_alert().text
# print(success_text)
# success_text.acc
# driver.switch_to_alert().accept()


#...选择日期...#

driver=webdriver.Chrome()
driver.get("http://www.jq22.com/yanshi4976")
driver.implicitly_wait(10)

driver.switch_to_frame(driver.find_element_by_id("iframe"))
driver.find_element_by_xpath('//*[@id="appDate"]').click() #点击打开日期控件

# 定位要滑动的年月日
dwwos=driver.find_elements_by_class_name("dwwo")
year=dwwos[0]
month=dwwos[1]
day =dwwos[2]

action=webdriver.TouchActions(driver)
action.scroll_from_element(year,0,2).perform()  #scroll_from_element()滑动元素
action.scroll_from_element(month,0,20).perform()
action.scroll_from_element(day,0,100).perform()