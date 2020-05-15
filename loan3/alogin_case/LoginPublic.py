#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import unittest ,time ##使用unittest框架编写测试用例。
from loan3.alogin_case import LoginPage
from loan3.alogin_case import LoginData #导入函数

# 通过两个变量，来接收调用 LoginData函数获得用户名&密码
us, pw = LoginData.data()
print(us, pw)  # 打印两个变量

# 继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class LoginPublic(unittest.TestCase):
    # 启动浏览器、访问地址模块
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.url = "http://172.17.255.229"
        # self.url = "https://car.100lending.com/"
        self.url = "http://183.62.97.141:9080/"
        self.username = us
        self.password = pw
        time.sleep(0.5)

    # 用例执行体
    def test_login(self):
        self.driver.implicitly_wait(30)
        login_page = LoginPage.LoginPage(self.driver, self.url, u"用户登录")  ## 声明LoginPage类对象
        login_page.open()  ## 调用LoginPage中open打开页面组件
        # login_page.switch_frame('x-URS-iframe')  # 切换到登录框Frame
        login_page.input_username(self.username)   # 调用LoginPage中input_username用户名输入组件
        login_page.input_password(self.password)   # 调用密码输入组件
        time.sleep(6)  # 等待时间输入验证码

        # 断言 获得登录成功的用户，用户名是否等于admin，不等于将抛出异常
        self.driver.implicitly_wait(30)
        now_user = self.driver.find_element_by_class_name("user-info").text
        if now_user == u'当前用户： admin':
            print('登录成功', now_user)
        else:
            raise NameError('user name error!')


    def tearDown(self):
        self.driver.quit()



