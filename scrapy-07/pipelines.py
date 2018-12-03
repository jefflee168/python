#!/usr/bin/env python
#-*- coding: utf-8 -*-

class MysqlpjtPipeline(object):
    def __init__(self):
        # 连接对应的数据库
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="redhat",db="test01")
    def process_item(self,item,spider):
        # 将获取到的name和keywd分别赋给变量name和变量key
        name = item["name"][0]
        key = item["keywd"][0]
        sql = "insert into mytb"
