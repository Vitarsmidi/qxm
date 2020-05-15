#!/usr/bin/env python
# coding = utf-8
import unittest,time
from loan2.alogin_case import start_Login2,start_Login3
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(start_Login2.Login))
testunit.addTest(unittest.makeSuite(start_Login3.Login))

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
    filename = "G:\\xiazaitp\\" + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")
    runner.run(testunit) #自动进行测试
    fp.close() #关闭打开的文件