# -*- coding: utf-8 -*-
# @Time : 2020/4/18 11:31
# @Author : qxm
# @FileName: login_test4.py


"""
套件，跨.py执行多个case
HTMLTestRunner 生成测试报告

"""

import unittest,time
import unittest, time, os, sys  # 引入unittest包 和time库
from chs.chs2 import login_test2,login_test3
from HTMLTestRunner import HTMLTestRunner

# testunit=unittest.TestSuite() # 定义一个单元测试容器,创建一个测试套件
# testunit.addTest(unittest.makeSuite(login_test2.Login.setUp)) # 将测试用例加入到测试容器中
# testunit.addTest(unittest.makeSuite(login_test2.Login.test_login))
# testunit.addTest(unittest.makeSuite(login_test3.Login.test_search))
# testunit.addTest(unittest.makeSuite(login_test3.Login.tearDown))

# #创建测试运行器，调用TextTestRunner类的run()方法运行测试套件
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(testunit)

if __name__ == '__main__':
    testunit = unittest.TestSuite()  # 定义一个单元测试容器,创建一个测试套件
    testunit.addTest(unittest.makeSuite(login_test2.Login.setUp))  # 将测试用例加入到测试容器中
    testunit.addTest(unittest.makeSuite(login_test2.Login.test_login))
    testunit.addTest(unittest.makeSuite(login_test3.Login.test_search))
    testunit.addTest(unittest.makeSuite(login_test3.Login.tearDown))
    # 我定义的路径是：当前路径+存放报告的专有目录Report+文件名(文件名是当前时间+report.html)
    curent_dirc=os.path.dirname(os.path.realpath(__file__))
    report_dirc = "\Report"
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
    report_name = curent_dirc+report_dirc+"\\"+now+"report.html"
    fp = open(report_name,"wb")
    runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况",verbosity= 2)
    runner.run(testunit) #自动进行测试
    fp.close() #关闭打开的文件