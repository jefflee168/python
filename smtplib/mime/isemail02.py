#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 这是一个定制版邮件

import smtplib
from email.mime.text import MIMEText

HOST = "smtp.exmail.qq.com"
SUBJECT = "Python 测试邮件"
TO = "19190888@qq.com"
FROM = "jefflee@test.com"
msg = MIMEText("""
	<table width="600" border="0" cellspacing="0" cellpadding="3">
	<h1>这是一级标题</h1>
	<tr bgcolor="CECFAD"><td><h2>这是二级标题</h2></td></tr>
	<tr bgcolor="#EFEBDE"><td><h3>这是三级标题</h3></td></tr>
	<tr><td><p>这是正文！</p></td></tr>
	</table>
	""","html","utf-8")
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO

try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls()
    server.login(FROM,"abc#123")
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
    print "邮件发送成功！"
except Exception,e:
    print "失败："+str(e)
