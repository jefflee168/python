#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib
import string

# 企业邮件，如果是qq则为smtp.qq.com
HOST = "smtp.exmail.qq.com"

# 邮件标题
SUBJECT = "Python 测试邮件"

# 收件邮箱
TO = "19190888@qq.com"

# 发件邮箱
FROM = "jefflee@test.com"

# 邮件内容
text = "Python smtplib 邮件模块测试！"

# 组装sendmail方法的邮件主体内容，各段以“\r\n”进行分隔
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
        ),"\r\n")

# 创建一个 SMTP() 对象
server=smtplib.SMTP()

# 通过connect方法连接 smtp主机
server.connect(HOST,"25")

# 启动安全传输模式
server.starttls()

# 邮件帐号登录校验
server.login(FROM,"abc#123")

# 邮件发送
server.sendmail(FROM,TO,BODY)

# 断开 smtp 连接
server.quit()
