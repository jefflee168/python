#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
此脚本主要采用python的MySQLdb类连接mysql，
并在指定数据库内插入数据。
"""

import MySQLdb

hosts = 'localhost'
user = 'root'
passwd = 'redhat'
data = 'test'

# 打开数据库
db = MySQLdb.connect(hosts,user,passwd,data)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 删除存在的表
sql1 = "DROP TABLE IF EXISTS employee"

# 创建并执行sql语句
sql2 = """ CREATE TABLE employee(
	  first_name CHAR(20) NOT NULL,
	  last_name CHAR(20),
	  age int,
	  sex char(1),			
	  income float)"""
try: 
    # 创建数据库test和表
    cursor.execute(sql1)
    cursor.execute(sql2)
    # 提交到数据库执行
    db.commit()
    # 关闭数据库
    db.close()
except Exception as e:
    # 发生错误时回滚
    db.rollback()
    print str(e)
