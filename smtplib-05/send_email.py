#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
本脚主要实现python自动发送邮件到指定邮箱,
其多用于监控系统时发送警告或者通知给系统
管理员，这样系统管理员就能及时地了解系统
的状况。
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"
mail_user = "test@qq.com"
mail_pass = "123456"

# 发送邮件邮箱
sender = 'test@qq.com'
# 此处填写接收邮件的邮箱，可以是QQ邮件或者其它邮件
receiver = ['888888@qq.com']

# 邮件发送内容
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("Python 教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')


# 邮件标题
title = "Python SMTP 邮件发送测试"
message['Subject'] = Header(title,'utf-8')

try:
    server = smtplib.SMTP()
    server.connect(mail_host,25)
    server.login(mail_user,mail_pass)
    server.sendmail(sender,receiver,message.as_string())
    print "恭喜你，邮件发送成功！"
except smtplib.SMTPException as e:
    print "Error: 邮件无法发送..."
    print str(e)
