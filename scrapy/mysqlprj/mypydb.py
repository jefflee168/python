#!/usr/bin/env python
# coding: utf-8

import pymysql

# 打开数据库连接
conn1 = pymysql.connect("10.0.0.26","root","redhat")

# sql插入语句
sql1 = ("DROP DATABASE IF EXISTS mypydb")
sql2 = ("CREATE DATABASE mypydb")
       
# 使用cursor()方法获取游标
cs1 = conn1.cursor()

try:
    # 执行sql语句
    cs1.execute(sql1)
    cs1.execute(sql2)
    # 提交到数据库执行
    conn1.commit()
except:
    # 如果发生错误则回滚
    conn1.rollback()

# 关闭数据库
conn1.close()

conn2 = pymysql.connect("10.0.0.26","root","redhat","mypydb")
cs2 = conn2.cursor()
sql3 = ("CREATE TABLE mytb(title CHAR(20) NOT NULL,keywd CHAR(30))")
sql4 = ("INSERT INTO mytb(title,keywd) VALUES('first title','firstkeywd')")

try:
    cs2.execute(sql3)
    cs2.execute(sql4)
    conn2.commit()
except:
    conn2.rollback()

conn2.close()
