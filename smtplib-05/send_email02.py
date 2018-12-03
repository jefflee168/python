#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'yuke.li@zun1.com'
receiver = ['191908133@qq.com']

message = MIMEMultipart()
message['From'] = Header("Python 教程",'utf-8') 
message['To'] = Header("测试",'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')

message.attach(MIMEText('这是Python的邮件测试','plain','utf-8'))

att1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment;filename="test.txt"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receiver,message.as_string())
    print "恭喜你，邮件发送成功！"
except smtplib.SMTPException:
    print "Eorror: 无法发送邮件!"
