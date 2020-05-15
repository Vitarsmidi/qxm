#!/usr/bin/env python
# coding = utf-8

from selenium import webdriver
import time #引入time库
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #ActionChains类提供鼠标操作方法

driver = webdriver.Chrome()
driver.get('http://172.17.255.229/')
driver.maximize_window() #将浏览器最大化显示

#打印当前的title
title=driver.title
print("title:" +title)

#打印当前的URL
now_url=driver.current_url
print("URL:" +now_url)

#.text获取当前页面文本信息
login_user=driver.find_element_by_id("login_user").text
print("登录用户为："+login_user)


size=driver.find_element_by_id("loginId").size
print (size)   #輸入框的寬高度

driver.implicitly_wait(30) #隱形等待，30秒內找到元素就執行，否則報錯

driver.find_element_by_id("loginId").clear()
driver.find_element_by_id("loginId").send_keys("admin") #id定位

driver.find_element_by_id("loginId").send_keys(Keys.CONTROL,'a') #ctrl+A全选
driver.find_element_by_id("loginId").send_keys(Keys.CONTROL,'c') #ctrl+c复制

driver.find_element_by_id("loginId").send_keys(Keys.CONTROL,'x') #ctrl+x剪切
driver.find_element_by_id("loginId").send_keys(Keys.CONTROL,'v') #ctrl+v粘贴


driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456") #name定位

driver.find_element_by_name("password").send_keys(Keys.BACK_SPACE) #删除后面一位
driver.find_element_by_name("password").clear()

driver.find_element_by_name("password").send_keys(Keys.SPACE) #输入空格
driver.find_element_by_name("password").send_keys(u"123") #空格+123

driver.find_element_by_id("subButton").click()  #点击登录
driver.submit() #submit()模拟.click()表单提交登录

#定位到要双击的元素
double =driver.find_element_by_id("yzmImg")
#对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(double).perform() #ActionChains 生成用户的行为；存储在actionchains对象。通过perform()执行。

time.sleep( 1 )

#定位元素的原位置
element = driver.find_element_by_id("yzmImg")
#定位元素要移动到的目标位置
target = driver.find_element_by_id("captchaCode")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()

time.sleep( 1 )

#定位到要右击的元素
right =driver.find_element_by_id("subButton")
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right).perform()
time.sleep(1)
driver.find_element_by_id("subButton").send_keys(Keys.ENTER)

above=driver.find_element_by_id("subButton")
ActionChains(driver).move_to_element(above).perform() #move_to_element()鼠标悬停,perform() 提交ActionChains类行为
ActionChains(driver).context_click(above).perform()  #context_click() #右击
ActionChains(driver).double_click(above).perform()  #double_click() #双击
ActionChains(driver).drag_and_drop(above).perform() #drag_and_drop() #拖动

attribute=driver.find_element_by_id("captchaCode").get_attribute('type')
print (attribute) #返回輸入框的屬性值
attribute=driver.find_element_by_id("captchaCode").get_attribute('class')
print (attribute)
attribute=driver.find_element_by_id("captchaCode").get_attribute('name')
print (attribute)

text=driver.find_element_by_id("subButton").text
print (text)  #返回輸入框的文本信息

result=driver.find_element_by_id("subButton").is_displayed()
print (result) #返回該字段結果是否可見，flase or true

size=driver.find_element_by_id("loginId") #获得输入框尺寸

