# -*- coding: utf-8 -*-
# @Time : 2020/4/18 18:32
# @Author : qxm
# @FileName: run_test.py

from time import sleep
from selenium import webdriver
import unittest, time, os, sys  # 引入unittest包 和time库
from chs.chs3.test_baidu  import TestBaidu
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包

"""
执行test_baidu.by文件并生成测试报告
"""

if __name__ == '__main__':
    testunit = unittest.TestSuite() # 定义一个单元测试容器
    testunit.addTest(unittest.makeSuite(TestBaidu))  # 将测试用例加入到测试容器中
    # 我定义的路径是：当前路径+存放报告的专有目录Report+文件名(文件名是当前时间+report.html)
    curent_dirc=os.path.dirname(os.path.realpath(__file__))
    report_dirc = "\Report"
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
    report_name = curent_dirc+report_dirc+"\\"+now+"report.html"
    fp = open(report_name,"wb")
    runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况",verbosity= 2)
    runner.run(testunit) #自动进行测试
    fp.close() #关闭打开的文件


# if __name__ == '__main__':
#     # testunit=unittest.defaultTestLoader.discover(chs3,pattern='test *.py')
#     """ defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录chs3匹配查找所有测试用例文件（test *.py），
#     并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。"""
#
#     testunit = unittest.TestSuite() # 定义一个单元测试容器
#     # testunit.addTest(TestBaidu("setUp"))# 将测试用例加入到测试容器中
#     testunit.addTest(unittest.makeSuite(TestBaidu))
#     now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
#     filename = "G:\\Report\\" + now + 'result.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况")
#     runner.run(testunit) #自动进行测试
#     fp.close() #关闭打开的文件


# ## 将结果输出到控制台或txt
# if __name__ == '__main__':
#     testunit = unittest.TestSuite() # 定义一个单元测试容器
#     testunit.addTest(unittest.makeSuite(TestBaidu)) # 将测试用例加入到测试容器中
#     # 取当前时间,把当前时间加到报告中,定义报告存放路径，支持相对路径
#     now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
#     # 1直接将结果输出到控制台 (控制台、测试报告txt、测试报告html任意选一项，不能同时输出)
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(testunit)
#     #2将测试结果输出到测试报告#( a  以追加模式打开)
#     with open( "G:\\Report\\"  + now +'result.txt', 'a') as fp:
#         runner = unittest.TextTestRunner(stream=fp, verbosity=2)
#         runner.run(testunit)
#         fp.close()

