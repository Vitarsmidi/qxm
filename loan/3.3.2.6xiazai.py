#!/usr/bin/env python
# coding = utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time ,os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

##上传
# input 标签上传
dir_work = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取文件路径
# dir_work = os.path.abspath('./files/')  # 获取文件路径
# os.path.abspath(__file__)当前模块的绝对路径，os.path.dirname可以获取到除文件名以外的路径
driver.find_element(driver, (By.XPATH, '//*[@id="picker1"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
driver.find_element_by_xpath('//*[@id="picker1"]/div[2]/input').send_keys(dir_work + r"\houtai\atest.pdf")

## AutoIt插件上传
'''
AutoIt 目前最新是 v3 版本，它是一个使用类似 BASIC 脚本语言的免费软件，它被设计用来进行 Windows GUI(图形用户界面)的自动化测试。它利用模拟键盘按键，鼠标移动和窗口/控件的组合来实现自动化任务。 
AutoIt Windows Info： 用于识别 Windows 控件信息。
Compile Script to.exe： 用于将 AutoIt 生成 exe 执行文件。
Run Script： 用于执行 AutoIt 脚本。
SciTE Script Editor： 用于编写 AutoIt 脚本。 

AutoIt录制步骤参考https://blog.csdn.net/yuanmei1986/article/details/51140192

ControlFocus("打开","","Edit1")
;识别windows窗口
WinWait("[CLASS:#32770]","",5)
;窗口等待十秒
ControlSetText("打开", "", "Edit1", "E:\tupian\1.jpg")
;想输入框中输入需要上传的地址
 Sleep(1000)
ControlClick("打开", "","Button1");
;点击[打开】按钮
Sleep(2000)

'''

# releaseFile = r"E:\\tupian\\upfile.exe"
# os.system(releaseFile)
# time.sleep(2)
# driver.find_element_by_id("xx").click() #点击上传



##下载
#**操作ChromeOptions**#
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\xiazaitp'}
#profile.default_content_settings.popups': 0,表示禁止弹出下载窗口，download.default_directory设置下载路径
# download.default_directory': os.getcwd()表示下载到脚本当前目录
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(executable_path='D:\\Program Files\\chromedriver\\chromedriver.exe', chrome_options=options)


driver.get('http://172.17.255.229/')
driver.maximize_window() #将浏览器最大化显示

driver.find_element_by_id("loginId").clear()
driver.find_element_by_id("loginId").send_keys("qq")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("qxm12345")
time.sleep(5) #输入验证码
#driver.find_element_by_id("subButton").click() #点击登录

#获得登录成功的用户，打印
driver.implicitly_wait(30)
now_user=driver.find_element_by_class_name("user-info").text
print('登录成功', now_user)
time.sleep( 0.5 )

driver.find_element_by_link_text("合同打印").click() #link text,文字链接定位
driver.switch_to_frame("conframe")  #表单切换
time.sleep( 0.5 )
driver.find_element_by_id("userName").clear()
driver.find_element_by_id("userName").send_keys("李采文")
driver.find_element_by_id("searchBtn").click() #搜索查询
print('查询成功......')
time.sleep(0.5)

driver.find_element_by_xpath("//i[contains(text(),'合同打印')]") #合同打印详情
driver.find_element_by_class_name("bigger-120").click() #搜索查询
print('已打开详情......')
time.sleep(0.5)

# 聚焦到某个元素位置
target =driver.find_element_by_xpath("//*[@id='picture-table']/tbody/tr[1]/td[4]/a[2]") #页面位置定位到下载
driver.execute_script("arguments[0].scrollIntoView();", target)
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='picture-table']/tbody/tr[1]/td[4]/a[2]").click() #下载
print('已下载文件到指定路径......')



#driver.quit()

