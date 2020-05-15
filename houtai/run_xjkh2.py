# -*- coding: utf-8 -*-
# @Time : 2020/4/18 18:32
# @Author : qxm
# @FileName: run_test.py

import unittest, time, os, sys  # 引入unittest包 和time库
from houtai.xjkh2  import TestKhgl
from HTMLTestRunner import HTMLTestRunner  # 引入 HTMLTestRunner 包
import yagmail

def send_mail(file_new):
    # 连接邮件服务器
    yag = yagmail.SMTP(user="2114132896@qq.com", password="prhfeoopaarnbaie", host='smtp.qq.com')
    # 邮箱主题
    subject = 'python email baidu_test report'
    # 邮箱正文+附件
    contents = ['测试报告如附件，请查阅，谢谢！',file_new]

    try:
        yag.send('qiuxinming@cfss.net.cn', subject=subject, contents=contents)
        yag.close()
        print("邮件发送成功")

    except BaseException:  # BaseException接收所有类型的异常
        print("发送邮件失败")

#查找测试报告目录，找到最新生成的测试报告文件
def new_report(Report):
    lists=os.listdir(Report) # 以列表形式返回Report目录下的所有文件（名）
    lists.sort(key=lambda fn: os.path.getmtime(Report+"\\"+fn)) #按文件时间由前到后排序。
    file_new=os.path.join(Report,lists[-1]) # 获取最新文件的绝对路径，即列表中最后一个文件,文件夹+文件名
    print(file_new)
    return file_new

#执行用例并生成测试报告
if __name__=='__main__':
    testunit = unittest.TestSuite() # 定义一个单元测试容器
    testunit.addTest(unittest.makeSuite(TestKhgl))  # 将测试用例加入到测试容器中
    curent_dirc=os.path.dirname(os.path.realpath(__file__))
    report_dirc = "\Report"
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
    report_name = now + "report.html"
    filename = curent_dirc+report_dirc+"\\"+ report_name
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况")
    runner.run(testunit) #自动进行测试
    fp.close() #关闭打开的文件

    new_report=new_report(curent_dirc+report_dirc) #最新的测试报告
    send_mail(new_report) #发送测试报告




