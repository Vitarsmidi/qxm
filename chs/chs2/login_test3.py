# -*- coding: utf-8 -*-
# @Time : 2020/4/16 22:44
# @Author : qxm
# @FileName: login_test3.py


from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库
from chs.chs2.module import CheDaiLogin
# from chs.chs2.read_txt import users #引入read_txt users
# from chs.chs2.read_csv import users #引入read_csv users
# from chs.chs2.read_json import users #引入read_json users
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包


"""引入装饰器修饰符"""
"""
使用@staticmethod或@classmethod，可以不需要实例化，直接类名.方法名()来调用。
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
setUpClass/tearDownClass 必须要使用装饰器

unittest.skip(reason)# 直接跳过该案例，reason说明原因
unittest.skipIf(condition,reason) #如果条件为真则跳过，unittest.skipIf(3>2,"跳过")
unittest.skipUnless(condition,reason) #如果条件为真则执行，unittest.skipIf(3>2,"条件为真则执行")
unittest.expectedFailure() #不管执行结果是否失败，都标记为失败

"""

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        CheDaiLogin.setUp(self)  # 调用CheDaiLogin方法中的setUp函数打开测试地址
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        CheDaiLogin.login(self)  # 调用CheDaiLogin方法中的login登录脚本
        # chedailogin.login("admin","123456") #调用login登录函数并传参
        # chedailogin.login(users[1] [0],users[0] [1]) #调用login登录函数并传参，[0] [0]txt中的第一行第一个参数
        # chedailogin.login(users[1] [0],users[1] [1]) #调用login登录函数并传参，[0] [0]csv中的第二行第一个参数
        # chedailogin.login(users[1] ['username'] ,users[1] ['password'] ) #调用login登录函数并传参，[0] [0]json中的第二行参数

    @unittest.skip("直接跳过测试")
    def test_search(self):
        u"""业务查询"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("业务受理").click()  # link text,文字链接定位
        driver.switch_to_frame("conframe")  # 表单切换
        time.sleep(0.5)
        driver.find_element_by_id("searchUserName").send_keys("王五")
        driver.implicitly_wait(30)
        driver.find_element_by_id("searchBtn").click()  # 搜索查询
        print('查询成功......')

    def tearDown(self):
        CheDaiLogin.logout(self)


if __name__ == "__main__":
    unittest.main()
    testunit = unittest.TestSuite()  # 定义一个单元测试容器,创建一个测试套件
    testunit.addTest(unittest.makeSuite(Login))  # 将测试用例加入到测试容器中
    # testunit.addTest(TestBaidu("setUp"))# 将测试用例加入到测试容器中




