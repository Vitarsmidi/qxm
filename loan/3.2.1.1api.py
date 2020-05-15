# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time #引入time库

from selenium.webdriver.common.by import By  #可使用find_element()通过By元素定位

driver = webdriver.Chrome()
driver.get('http://183.62.97.141:9080/')
driver.maximize_window() #将浏览器最大化显示
driver.find_element_by_id("loginId").clear()
driver.find_element_by_id("loginId").send_keys("admin") #id定位
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456") #name定位
time.sleep( 6 )

#获得前面 title，打印
title = driver.title
print (title)

#拿当前 title 与预期 title 做比较
if title == u"车贷系统":
    print ("title ok!")
else:
    print ("title false!")

#获得当前 URL，打印
now_url = driver.current_url
print (now_url)

#拿当前 URL 与预期 URL 做比较
if now_url == "http://172.17.255.229/":
    print('url ok!')
else:
    print("url false!")

#获得登录成功的用户，打印
now_user=driver.find_element_by_class_name("user-info").text
print('登录成功', now_user)

#driver.find_element_by_tag_name("input").click()  #tag name定位
#driver.find_element_by_class_name("btn-primary").click()  #class= width-35 btn btn-sm btn-primary

#driver.find_element_by_link_text("客户登记").click() #link text,文字链接定位
driver.find_element_by_partial_link_text("登记").click() #partial link text,部分文字链接定位

#添加固定休眠时间
time.sleep( 1 )


driver.switch_to_frame("conframe")  #表单切换
# driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@src='/user/register/list']"))  # 这里是表单切换
driver.find_element_by_id("searchUserName").send_keys("石采南") #id定位

#添加智能等待
driver.implicitly_wait(30)  #隱形等待，30秒內找到元素就執行，否則報錯
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div/div[4]/button[2]").click() #搜索 xpath绝对路径/

#WebDriverWait()等待方法使用
element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//*[@id='addBtn']"))
element.send_keys("selenium")

driver.find_element_by_xpath("//*[@id='addBtn']").click() #新增 //,通过自身的 id 属性定位
# driver.find_elements_by_css_selector('input[type=button]').click() #新增
# driver.find_element_by_xpath("//td[12]/div/button/i").click() #评估
# driver.find_element_by_xpath("//i[contains(text(),'评估')]").click() #评估
# driver.find_element_by_class_name('bigger-120').click() #评估


driver.implicitly_wait(30)

driver.find_element_by_xpath("//*[@name='userName']").send_keys("粵光燈") #客户姓名  相对路径//,通过自身的 name 属性定位
driver.find_element_by_xpath("//*[@id='mobile' or @name='mobile'] ").send_keys("15800158001") #mobile  布尔逻辑运算
driver.find_element_by_css_selector("#applyAmount").send_keys("1000") # 申请金额 css selector id定位id用#代替
#driver.find_element_by_css_selector("[name=idCard]").send_keys("421381195501073029") # 身份证 name需要加上中括号
driver.find_element_by_css_selector("input[placeholder='证件号码']").send_keys("421381195510222663") # 标签名+元素属性
driver.find_element_by_css_selector(".submitOrder").click()  #提单 css selector class定位
#driver.find_element_by_xpath("//*[@class='submitOrder']").click() #提单 通过自身的 class 属性定位

#driver.quit()


# webdriver 提供了一系列的元素定位方法，常用的有以下几种：
#
#  id
#  name
#  class name
#  tag name
#  link text
#  partial link text
#  xpath
#  css selector
#
# 分别对应python webdriver 中的方法为：
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()

# driver.find_element_by_xpath("//from[@id='from']/span/input")
# driver.find_element_by_xpath("//input[@id='from' and @class='s_ip_wr']/span/input")
# driver.find_element_by_xpath("//a[test(),'新闻']")
#
# driver.find_element(By.ID,"loginId")
# driver.find_element(By.NAME,"loginId")
# driver.find_element(By.CLASS_NAME,"S_P")
# driver.find_element(By.XPATH,"//*[@id='loginId'")
# driver.find_elements_by_css_selector("from#form > span > input[type=button]")
# driver.find_elements_by_css_selector("[class*=s_ipt]") #class包含有s_ipt
# driver.find_elements_by_css_selector("[class^=bg]") #class属性以bg开头
# driver.find_elements_by_css_selector("[class$=bg]") #class属性以bg结尾

##定位一组元素  一个列表，如下列列表
# driver.find_elements(By.ID,"loginId")
# driver.find_elements(By.NAME,"loginId")
# driver.find_elements(By.CLASS_NAME,"S_P")
# driver.find_elements(By.XPATH,"//*[@id='loginId'")