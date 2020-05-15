#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.maximize_window() #将浏览器最大化显示

#获得当前窗口句柄
nowhandle=driver.current_window_handle
#打开注册新窗口
driver.implicitly_wait(30)
driver.find_element_by_link_text("登录").click() #link text,文字链接定位
driver.implicitly_wait(30)
driver.find_element_by_link_text("立即注册").click() #link text,文字链接定位

#获得当前窗口句柄
nowhandle2=driver.current_window_handle
#获得所有窗口句柄
allhandles=driver.window_handles
#切换到相应的窗口
allhandles=driver.switch_to.window()

#循环判断窗口是否为当前窗口
for handle in allhandles:
   if handle != nowhandle:
     driver.switch_to_window(handle)
     print ('now register window!')

driver.close() #关闭当前窗口

#回到原先的窗口
driver.switch_to_window(nowhandle) #回到nowhandle窗口
driver.implicitly_wait(30)
driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click() #去掉登录弹窗
driver.implicitly_wait(30)
driver.find_element_by_id("kw").send_keys("中国") #输入中国搜索
driver.find_element_by_id("su").click()
time.sleep(3)

#获得所有窗口句柄
allhandles=driver.window_handles

for handle2 in allhandles:
   if handle2 != nowhandle2:
     driver.switch_to_window(handle2)
     print ('now register window!')

driver.switch_to_window(handle2) #回到handle2窗口

# 表单切换
# driver.switch_to.frame(d.find_element_by_xpath('//*[@id="客户配置"]/iframe'))
# driver.switch_to_frame("conframe")  # 表单切换find_element_by_class_name()
# driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
# driver.switch_to_default_content() #回到最外层页面



# driver.quit()
