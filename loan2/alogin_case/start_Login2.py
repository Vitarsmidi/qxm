#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import unittest, time #引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

# 类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class Login(unittest.TestCase):
    # 启动浏览器、访问地址模块
    @classmethod
    def setUpClass(self):
        # setUp用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://183.62.97.141:9080/"
        time.sleep(0.5)

    # 登录用例(test_login中放置的就是我们的测试脚本)
    def test_login(self):
        u"""自动登录"""
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("loginId").clear()
        driver.find_element_by_id("loginId").send_keys('admin')
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys('123456')
        time.sleep(6)  # 输入验证码
        # driver.find_element_by_id("subButton").click() #点击登录

        # 断言 获得登录成功的用户，用户名是否等于admin，不等于将抛出异常
        driver.implicitly_wait(30)
        now_user = driver.find_element_by_class_name("user-info").text
        if now_user == u'当前用户： admin':
            print('登录成功', now_user)
        else:
            raise NameError('user name error!')
        time.sleep(0.5)

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

    @classmethod
    def tearDownClass(self):

        time.sleep(1)
        self.driver.quit()



# if __name__ == '__main__':
#     testunit = unittest.TestSuite()
#     testunit.addTest(unittest.makeSuite(Login))
#     fp = open(r'D:\testresult.html', 'wb')
#     runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")
#     runner.run(testunit)
#     fp.close()

 ##unittest.main()函数用来测试类中以test开头的测试用例
if __name__ == '__main__':
        testunit = unittest.TestSuite() # 定义一个单元测试容器
        testunit.addTest(Login("test_login")) # 将测试用例加入到测试容器中
        testunit.addTest(Login("test_search"))
        # 取前面时间%Y-%m-%M-%H_%M_%S
        now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
        # 把当前时间加到报告中,定义报告存放路径，支持相对路径
        filename = "G:\\xiazaitp\\" + now + 'result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")
        runner.run(testunit) #自动进行测试
        fp.close() #关闭打开的文件
        print("232")
