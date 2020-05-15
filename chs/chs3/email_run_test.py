# -*- coding: utf-8 -*-
# @Time : 2020/4/18 18:32
# @Author : qxm
# @FileName: run_test.py

from time import sleep
from selenium import webdriver
import unittest, time, os, sys
from chs.chs3.test_baidu4  import TestBaidu
from HTMLTestRunner import HTMLTestRunner
import smtplib    # smtplib模块实现邮件的发送功能
from email.mime.text import MIMEText    # MIME邮件处理
from email.header import Header         # header邮件头信息就是邮件发送的路由信息
from email.mime.multipart import MIMEMultipart  # MIMEMultipart 支持带附件，发送多个收件人

"""
smtplib模块整合测试报告自动发邮件
"""

def send_mail(file_new):

    # 定义邮件主题
    msg = MIMEMultipart()
    subject = 'Test report email for '+ time.strftime("%Y-%m-%d-%H%M%S")
    msg['Subject'] = Header(subject, 'utf-8')

    # 定义邮件正文,格式，编码
    msg.attach(MIMEText('<html><hl>测试报告如附件，请查收，谢谢！</hl></html>', 'html', 'utf-8'))

    # 添加附件
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8') #Base64是一种任意二进制到文本字符串的编码方法，
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=report_name)
    msg.attach(att)

    # 连接smtp服务器登陆邮箱
    try:
        smtp = smtplib.SMTP()
        smtp.connect("smtp.qq.com")
        smtp.login("2114132896@qq.com", "prhfeoopaarnbaie")
        receiver = ['qiuxinming@cfss.net.cn']  # 收件人邮箱
        smtp.sendmail('2114132896@qq.com', receiver, msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
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
    testunit.addTest(unittest.makeSuite(TestBaidu))  # 将测试用例加入到测试容器中
    curent_dirc=os.path.dirname(os.path.realpath(__file__))
    report_dirc = "\Report"
    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
    report_name = now + "report.html"
    filename = curent_dirc+report_dirc+"\\"+ report_name
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况",verbosity= 2)
    runner.run(testunit) #自动进行测试
    fp.close() #关闭打开的文件

    new_report=new_report(curent_dirc+report_dirc) #最新的测试报告
    send_mail(new_report) #发送测试报告




