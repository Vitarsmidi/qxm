#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import loan3.BasePage

#继承BasePage类
class LoginPage(loan3.BasePage.BasePage):
    ##定位器，登录元素定位
    # URL = 'http://172.17.255.229'
    loginId = (By.ID, 'loginId')
    password = (By.NAME, 'password')
    subButton = (By.XPATH, "//*[@id='subButton']")
    # username_info =(By.NAME,"user-info")   #class ="user-info",这里classname写作name
    # username_info = (By.XPATH, "//*[@id='navbar-container']/div[3]/ul/li[3]/a/span")

    # def __init__(self, driver):
    #     super().__init__(driver=driver, url=self.URL)

    ##页面操作，通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    def open(self):
        # 调用BasePage中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 输入用户名：调用BasePage中的send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.loginId).clear()
        self.find_element(*self.loginId).send_keys(username) #username在LoginCase定义

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.password).clear()
        self.find_element(*self.password).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.subButton).click()
    #
    # # # 登录成功页面中的登录用户名查找
    # # def user_info(self):
    # #     return self.find_element(*self.username_info).text
    #
    # # 登录成功用户名信息
    # def user_info(self):
    #     #return self.find_element(*self.username_info).text
    #     now_user = self.find_element(*self.username_info).text
    #     now_user = now_user.strip('您好：')
    #     return now_user




# by定位
# find_element(By.ID,"kw")
# find_element(By.NAME,"wd")
# find_element(By.CLASS_NAME,"s_ipt")
# find_element(By.TAG_NAME,"input")
# find_element(By.LINK_TEXT,u"新闻")
# find_element(By.PARTIAL_LINK_TEXT,u"新")
# find_element(By.XPATH,"//*[@class='bg s_btn']")
# find_element(By.CSS_SELECTOR,"span.bg s_btn_wr>input#su"
