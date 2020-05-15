#!/usr/bin/env python
# coding = utf-8
import unittest,time,os
import sys
sys.path.append("\alogin_case") ##把 alogin_case目录添加到 path 下，这里用的相对路径
# from alogin_case import * # 在__init__中导入了对应测试文件，*表示导入 alogin_case 目录下的所有文件，当然也可再此直接导入
from loan2.alogin_case import Login
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

# listaa='D:\\Program Files\\Python\\Python37\\loan2\\alogin_case'
# def creatsuitel():
#   testunit=unittest.TestSuite()
#
#   #discover 方法定义
#   discover=unittest.defaultTestLoader.discover(listaa,pattern ='start_*.py',top_level_dir=None)
#   #discover 方法筛选出来的用例，循环添加到测试套件中
#   for test_suite in discover:
#     for alogin_case in test_suite:
#      testunit.addTests(alogin_case)
#     print(testunit)
#   return testunit
# alltestnames = creatsuitel()



# #将用例组装数组
# alltestnames = [
# start_Login2.Login,
# start_Login3.Login
# ]
#
# #创建测试套件
# testunit=unittest.TestSuite()
# #循环读取数组中的用例
# for test in alltestnames:
#   testunit.addTest(unittest.makeSuite(test))


testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(Login.Login))

# #执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)

# #定义个报告存放路径，支持相对路径。
# filename = 'D:\\xiazaitp\\result.html'
# fp = open(filename, 'wb')
# runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
# #执行测试用例
# runner.run(testunit)

if __name__ == '__main__':
    # 取前面时间%Y-%m-%M-%H_%M_%S
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
    # 把当前时间加到报告中,定义报告存放路径，支持相对路径
    filename = "D:\\xiazaitp\\" + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")
    # runner.run(alltestnames)#自动进行测试
    runner.run(testunit) #自动进行测试
    fp.close() #关闭打开的文件