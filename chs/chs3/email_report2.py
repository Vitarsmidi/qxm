# -*- coding: utf-8 -*-
# @Time : 2020/4/29 9:04
# @Author : qxm
# @FileName: email_report.py

import smtplib  ,time  # smtplib模块实现邮件的发送功能
from email.mime.text import MIMEText    # MIME邮件处理
from email.header import Header
from email.mime.multipart import MIMEMultipart  # MIMEMultipart 支持带附件，发送多个收件人

"""
发送带附件的邮件
加密SMTP会话
"""

#定义邮件主题
msg = MIMEMultipart()
subject = 'Test report email for ' + time.strftime("%Y-%m-%d-%H%M%S")
msg['Subject']= Header(subject,'utf-8')

#定义邮件正文,格式，编码
msg.attach(MIMEText('<html><hl>测试报告自动发送，请查收，谢谢！</hl></html>', 'html', 'utf-8')) #html文本

# #选择打开发送的附件1
att = MIMEText(open(r'.\Report\2020-04-19-185613report.html','rb').read(),'base64','utf-8')
att["Content-Type"] = 'application/octet-stream' # 指定附件内容类型为'application/octet-stream' 二进制流
att.add_header('Content-Disposition', 'attachment', filename='2020-04-28-194836report.html')
# Content-Disposition 指定显示的附件文件，指定的附件文件名为"2020-04-28-194836report.html"
msg.attach(att)

# 附件2
att2 = MIMEText(open(r'.\Report\2020-04-19-185613report.html','rb').read(),'base64','utf-8')
att2['Content-Type'] = 'application/octet-stream'
att2.add_header('Content-Disposition', 'attachment', filename='11.html')
msg.attach(att2)


#发送邮件 +加密SMTP会话(通过Gmail提供的安全SMTP)
try:
    smtp_server = 'smtp.qq.com'
    smtp_port = 587
    smtp = smtplib.SMTP(smtp_server,smtp_port)
    smtp.starttls() #调用starttls()方法创建安全连接
    # smtp.set_debuglevel(1) #打印出和SMTP服务器交互的所有信息。
    smtp.login("2114132896@qq.com", "prhfeoopaarnbaie")  # 登录发送方邮箱，第三方登录需要用授权码，在qq邮箱设置-账户中设置
    receiver = ['qiuxinming@cfss.net.cn']  # 收件人邮箱
    smtp.sendmail("2114132896@qq.com", receiver, msg.as_string()) # 指定发送人、收件人、内容
    smtp.quit()
    print('邮件发送成功')

    # smtp = smtplib.SMTP()  # smtplib.SMTP构造函数,连接smtp服务器
    # smtp.connect("smtp.qq.com", 25)  # 连接smtp服务器，connect()指定发送方连接的邮箱服务器地址,不能带http、https
    # smtp.login("2114132896@qq.com", "prhfeoopaarnbaie")  # 登录发送方邮箱，第三方登录需要用授权码，在qq邮箱设置-账户中设置
    # smtp.sendmail("2114132896@qq.com", "qiuxinming@cfss.net.cn", msg.as_string())  # 指定发送人、收件人、正文
    # smtp.quit()
    # print('邮件发送成功')

except smtplib.SMTPException:
    print("发送邮件失败")




# # with open(r'G:\\Report\\2020-04-20-110325result.html','rb') as f:
# with open(r'.\Report\2020-04-28-194836report.html','rb') as f:
#     send_att = f.read()
# att = MIMEText(send_att,'html','utf-8')

# smtp.sendmail("2114132896@qq.com", ["test1@qq.com","test2@qq.com"], msg.as_string())  # 多个接收人