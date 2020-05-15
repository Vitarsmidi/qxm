# -*- coding: utf-8 -*-
# @Time : 2020/4/29 9:04
# @Author : qxm
# @FileName: email_report.py

import yagmail ,time   # yagmail 更简单的发送邮件模块
from email.mime.text import MIMEText    # MIME邮件处理
from email.header import Header
from email.mime.multipart import MIMEMultipart  # MIMEMultipart 支持带附件，发送多个收件人

"""
yagmail模块更简单的发送带附件的邮件
"""
# 连接邮件服务器
yag = yagmail.SMTP(user="2114132896@qq.com",password="prhfeoopaarnbaie",host='smtp.qq.com')

# 邮箱主题
subject = 'Test report email for ' + time.strftime("%Y-%m-%d-%H%M%S")

# 邮箱正文
contents = ['Hello, i am sent by yagmail!', 'Report/2020-04-19-185613report.html'] #主题+附件
# contents = ['Hello, i am sent by yagmail!', yagmail.inline('test.jpg')]# 邮件内容中内嵌图片
# contents = ['Hello, i am sent by yagmail!', 'G:/Report/test.jpg'] #图片已附件形式
# contents = ['Hello, i am sent by yagmail!', '"http://www.runoob.com"这是一个链接'] #主题+链接
# contents = ['Hello, i am sent by yagmail!','<p><a href="http://www.runoob.com">这是一个链接</a></p>'] #主题+链接

# 发送邮件
try:
    receiver = ['qiuxinming@cfss.net.cn']  # 收件人邮箱
    yag.send( receiver, subject=subject, contents=contents)
    yag.close()
    print("邮件发送成功")

except BaseException:  # BaseException接收所有类型的异常
    print("发送邮件失败")


# #定义邮件主题
# msg = MIMEMultipart()
# subject = 'python email baidu_test report'
# msg['Subject']= Header(subject,'utf-8')
#
# #定义邮件正文,格式，编码
# msg.attach(MIMEText('<html><hl>测试报告自动发送，请查收，谢谢！</hl></html>', 'html', 'utf-8')) #纯文本
#
# # #选择打开发送的附件1
# att = MIMEText(open(r'.\Report\2020-04-28-194836report.html','rb').read(),'base64','utf-8')
# att["Content-Type"] = 'application/octet-stream' # 指定附件内容类型为'application/octet-stream' 二进制流
# att.add_header('Content-Disposition', 'attachment', filename='2020-04-28-194836report.html')
# # Content-Disposition 指定显示的附件文件，指定的附件文件名为"2020-04-28-194836report.html"
# msg.attach(att)
#
# # 附件2
# att2 = MIMEText(open(r'.\Report\2020-04-28-184307report.html','rb').read(),'base64','utf-8')
# att2['Content-Type'] = 'application/octet-stream'
# att2.add_header('Content-Disposition', 'attachment', filename='11.html')
# msg.attach(att2)
#
# #发送邮件
# try:
#     smtp = smtplib.SMTP()  # smtplib.SMTP构造函数,连接smtp服务器
#     smtp.connect("smtp.qq.com", 25)  # 连接smtp服务器，connect()指定发送方连接的邮箱服务器地址,不能带http、https
#     smtp.login("2114132896@qq.com", "prhfeoopaarnbaie")  # 登录发送方邮箱，第三方登录需要用授权码，在qq邮箱设置-账户中设置
#     smtp.sendmail("2114132896@qq.com", "qiuxinming@cfss.net.cn", msg.as_string())  # 指定发送人、收件人、正文
#     smtp.quit()
#     print('邮件发送成功')
#
# except smtplib.SMTPException:
#     print("发送邮件失败")




# # with open(r'G:\\Report\\2020-04-20-110325result.html','rb') as f:
# with open(r'.\Report\2020-04-28-194836report.html','rb') as f:
#     send_att = f.read()
# att = MIMEText(send_att,'html','utf-8')