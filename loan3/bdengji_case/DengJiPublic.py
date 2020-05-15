#!/usr/bin/env python
# coding = utf-8
import unittest ,time ##使用unittest框架编写测试用例。
from loan3.alogin_case import LoginPublic #引入登录文件
from loan3.bdengji_case import DengJiPage
from loan3.bdengji_case import DengJiData #导入函数

# 通过变量，来接收调用 DengJiData函数
User,UserName,Mobile,ApplyAmount,IdCrd= DengJiData.data()
print(User,UserName,Mobile,ApplyAmount,IdCrd)  # 打印两个变量

# 继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class DengJiPublic(unittest.TestCase):
    # 启动浏览器、访问地址模块
    def setUp(self):
        # 调用登录模块
        LoginPublic.LoginPublic.setUp(self)
        self.searchUserName = User
        self.userName = UserName
        self.mobile = Mobile
        self.applyAmount = ApplyAmount
        self.idCrd = IdCrd

    def test_01_login(self):
        # 调用登录模块
        LoginPublic.LoginPublic.test_login(self)

    # 登记用例执行体
    def test_02_khdj(self):
        login_page = DengJiPage.DengJiPage(self.driver, self.url, u"客户登记")  ## 声明LoginPage类对象
        self.driver.implicitly_wait(30)
        login_page.click_khdj()  #调用点击'客户登记'按钮组件
        time.sleep(1)
        login_page.switch_frame("conframe")  # 切换到登录框Frame
        # login_page.switch_to_frame('conframe')  # 切换到登录框Frame
        # login_page.switch_to_frame(self.driver.find_element_by_xpath("//iframe[@src='/user/register/list']"))
        # login_page.switch_to_frame(self.driver.find_element_by_xpath("//iframe[@src='/user/register/list']"))
        # login_page.switch_to_frame(By.XPATH, "//iframe[@src='/user/register/list']")
        # self.driver.implicitly_wait(30)
        login_page.input_searchUserName(self.searchUserName)   # 调用LoginPage中input_username用户名输入组件
        login_page.click_searchBtn()  #调用点击'查询'按钮组件click_addBtn
        self.driver.implicitly_wait(30)
        login_page.click_addBtn()  #调用点击'新增'按钮组件
        self.driver.implicitly_wait(30)
        login_page.input_userName(self.userName) #输入新增用户名
        login_page.input_mobile(self.mobile)  # mobile
        login_page.input_applyAmount(self.applyAmount)  # 输入借款金额
        login_page.input_idCrd(self.idCrd) #idCrd
        login_page.input_source()  #客户来源
        login_page.input_idCardType()  #证件类型
        login_page.input_purpose()  #借款用途
        login_page.input_submitOrder()  #提交
        time.sleep(0.5)
        self.driver.implicitly_wait(30)
        login_page.input_definite()  #确定提交
        time.sleep(0.5)
        self.driver.implicitly_wait(30)
        login_page.input_definite2()  #确定
        time.sleep(0.5)

    def tearDown(self):
        self.driver.quit()

