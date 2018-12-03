#!/usr/bin/env python
# coding: utf-8

import pymysql

class MysqlprjPipelines(object):
    def __init__(self):
	# 连接对应数据库
        self.conn = pymysql.connect("10.0.0.26","root","redhat","mypydb")
    def process_item(self,item,spider):
	# 将获取的 name 和 key 分别赋值给 title 和 keywd
        name = item["name"][0]
        key = item["keywd"][0]
	# 构造对应的 sql 语句
        sql = "insert into mytb(title,name) VALUES('"+name+"','"+key+"')"
	# 通过query执行sql语句
        self.conn.query(sql)
        return item
    def close_spider(self,spider):
        self.conn.close()
