#!/usr/bin/env python
# coding = utf-8
import unittest,time,os
import sys
sys.path.append("\alogin_case,\bdengji_case") ##把 alogin_case目录添加到 path 下，这里用的相对路径
from loan2.alogin_case import Login
from loan2.bdengji_case import DengJi
#这里需要导入测试文件
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner包

#将用例组装数组
alltestnames = [
Login.Login,
DengJi.Dengji
]

#创建测试套件
testunit=unittest.TestSuite()
#循环读取数组中的用例
for test in alltestnames:
  testunit.addTest(unittest.makeSuite(test))


# testunit=unittest.TestSuite()
# #将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(Login.Login))

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