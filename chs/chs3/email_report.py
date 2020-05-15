# -*- coding: utf-8 -*-
# @Time : 2020/4/29 9:04
# @Author : qxm
# @FileName: email_report.py

import smtplib ,time   # smtplib模块实现邮件的发送功能
from email.mime.text import MIMEText    # MIME邮件处理
from email.header import Header         # header邮件头信息就是邮件发送的路由信息
from email.mime.multipart import MIMEMultipart  # MIMEMultipart 支持带附件，发送多个收件人
"""
自动发送邮件
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。
port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。
local_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可。

SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]) #指定发送人、收件人、正文
from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息

"""

#定义邮件主题
msg = MIMEMultipart()
subject = 'Test report email for ' + time.strftime("%Y-%m-%d-%H%M%S")
msg['Subject']= Header(subject,'utf-8') #定义主题和主题编码类型

#定义HTML类型的邮件正文,格式，编码
msg.attach(MIMEText('<html><hl>测试报告自动发送，请查收，谢谢！</hl></html>', 'html', 'utf-8')) #html文本
# msg.attach(MIMEText('测试报告自动发送，请查收，谢谢！', 'plain', 'utf-8')) #纯文本


msg.imgs.append(msg.driver.get_screenshot_as_base64())

#发送邮件
try:
    smtp = smtplib.SMTP()  # smtplib.SMTP构造函数,连接smtp服务器
    smtp.connect("smtp.qq.com", 25)  # 连接smtp服务器，connect()指定发送方连接的邮箱服务器地址,不能带http、https
    # 常用邮箱的smtp服务器：新浪：smtp.sina.com,搜狐：smtp.sohu.com；126：smtp.126.com；139：smtp.139.com,163网易：smtp.163.com
    smtp.login("2114132896@qq.com", "prhfeoopaarnbaie")  # 登录发送方邮箱，第三方登录需要用授权码，在qq邮箱设置-账户中设置
    receiver = ['qiuxinming@cfss.net.cn']  # 收件人邮箱
    smtp.sendmail("2114132896@qq.com", receiver, msg.as_string()) # 指定发送人、收件人、正文
    smtp.quit()
    # smtp.add_img()  # 加入截图
    print('邮件发送成功')

except smtplib.SMTPException:
    print("发送邮件失败")


"""
# #定义HTML类型的邮件正文,格式，编码
# msg = MIMEText('<html><hl>你好！</hl></html>','html','utf-8')
#
# #发送邮件主题
# subject = 'python email baidu_test report'
# msg['Subject']= Header(subject,'utf-8') #定义主题和主题编码类型
"""

