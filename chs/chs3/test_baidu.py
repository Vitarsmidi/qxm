# -*- coding: utf-8 -*-
# @Time : 2020/4/20 10:16
# @Author : qxm
# @FileName: test_baidu.py

from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
登陆baidu.com，并查询两个关键字，两条案例，案例中输入关键字
"""

class TestBaidu(unittest.TestCase):
    """ 百度搜索测试方法"""
    @classmethod
    def setUpClass (self):
        """" 打开百度"""
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        # self.verificationErrors = []
        # self.accept_next_alert = True
        sleep(1)

    def test_search1(self):
        """" 百度搜索关键字selenium"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(1)

    def test_search2(self):
        """" 百度搜索关键字unittest"""
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_id("su").click()
        sleep(1)
        self.assertEqual(self.driver.title, "unittes" + u"_百度搜索")

    def test_search3(self):
        """" 百度搜索关键字unittest"""
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys("testng")
        self.driver.find_element_by_id("su").click()

# 在test_baidu2/test_baidu3中将实现一个用例里查询多个关键字

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


##执行test开头的用例
if __name__ == "__main__":
        unittest.main(verbosity = 2)



#   # #***构建测试集***#
# suit = unittest.TestSuite()
# suit.addTest(unittest.makeSuite(TestBaidu))# 将测试用例加入到测试容器中
# #我定义的路径是：当前路径+存放报告的专有目录Report+文件名(文件名是当前时间+report.html)
# curent_dirc=os.path.dirname(os.path.realpath(__file__))
# report_dirc = "\Report"
# now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
# report_name = curent_dirc+report_dirc+"\\"+now+"report.html"
# fp = open(report_name,"wb+")
# runner = HTMLTestRunner(stream=fp,title=u"测试报告",description=u"用例执行情况",verbosity= 2)
# runner.run(suit)
# fp.close()

#   #构建测试集
# suit = unittest.TestSuite()
# now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
# filename = "G:\\Report\\" + now + 'result.html'
# fp = open(filename, 'wb')
# runner = HTMLTestRunner(stream=fp,title=u"测试报告",description=u"用例执行情况")
# runner.run(suit)
# fp.close()


# if __name__ == '__main__':
#     testunit = unittest.TestSuite() # 定义一个单元测试容器
#     testunit.addTest(unittest.makeSuite(TestBaidu))  # 将测试用例加入到测试容器中
#     # 我定义的路径是：当前路径+存放报告的专有目录Report+文件名(文件名是当前时间+report.html)
#     curent_dirc=os.path.dirname(os.path.realpath(__file__))
#     report_dirc = "\Report"
#     now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
#     report_name = curent_dirc+report_dirc+"\\"+now+"report.html"
#     fp = open(report_name,"wb")
#     runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况")
#     runner.run(testunit) #自动进行测试
#     fp.close() #关闭打开的文件






