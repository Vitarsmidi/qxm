#!/usr/bin/env python
# coding = utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time #引入time库
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://172.17.255.229/')
driver.maximize_window() #将浏览器最大化显示

#捕捉输入框异常
driver.find_element_by_id("loginId").clear()
driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("12345") #错误密码
time.sleep(5) #输入验证码
driver.find_element_by_id("subButton").click() #点击登录
time.sleep(0.5)

#获取警告框文本信息
#.switch_to_alert()定位错误信息，text返回文字信息，accept()接受警告框，dismiss()解散警告框，send_keys()在警告框输入文本
message=driver.switch_to_alert().text
print(message)
# driver.switch_to_alert().send_keys("hello") #输入值
driver.switch_to_alert().accept()   #接受警告框处理
# driver.switch_to_alert.accept()  # 接受警告框处理

# alert = d.switch_to_alert()
# '''添加等待时间'''
# sleep(1)
# '''获取警告对话框的内容'''
# print(alert.text)  # 打印警告对话框内容
# alert.accept()  # alert对话框属于警告对话框，我们这里只能接受弹窗

# 截图

try:
    picture_url=driver.get_screenshot_as_file('D:\\xiazaitp\\png1.png')
    print("%s：截图成功！！！" % picture_url)
except BaseException as msg:
    print(msg)
    time.sleep(1)

# driver.save_screenshot("./files/login_img.png")

driver.find_element_by_name("password").clear()

#  text：返回警告框文本信息 
#  accept()：接受现有警告框。  
#  dismiss()：解散现有警告框。  
#  send_keys(keysToSend)： 发送文本至警告框。 keysToSend：将文本发送至警告框。  

driver.implicitly_wait(30)
#driver.find_element_by_id("subButton").click() #点击登录

#获得登录成功的用户，打印
now_user=driver.find_element_by_class_name("user-info").text
print('登录成功', now_user)
time.sleep(1)

# 获得 cookie 信息
cookie= driver.get_cookies()
#将获得 cookie 的信息打印
print (cookie)

#向 cookie 的 name 和 value 添加会话信息。
driver.add_cookie({'name':'123', 'value':'456'})
#遍历 cookies 中的 name 和 value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
  print ("%s -> %s" % (cookie['name'], cookie['value']))

# 获得指定 cookie 信息
print(driver.get_cookie("name"))
print(driver.get_cookie("value"))

# 获得 cookie 信息
cookie= driver.get_cookies()
#将获得 cookie 的信息打印
print (cookie)

# 删除一个特定的 cookie
driver.delete_cookie(name="SESSIONID")
# 删除所有 cookie
driver.delete_all_cookies()
time.sleep(1)

# 获得 cookie 信息
cookie= driver.get_cookies()
#将获得 cookie 的信息打印
print (cookie)
print ("此时刷新页面应已退出登录")

Select.select_by_value('XX') #选择下拉框value值
# select_by_value() 通过value定位下拉选项
# select_by_visible_text() 通过text定位下拉选项
# select_by_index() 通过下拉框索引进行选择，第一个为0，第二个为1


#driver.quit()

