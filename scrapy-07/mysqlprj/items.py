#!/usr/bin/env python
# coding: utf-8

import scrapy

class MysqlprjItem(scrapy.Item):
    # 建立 name 存储网络标题
    name = scrapy.Field()
    # 建立 keywd 存储网页关键词
    keywd = scrapy.Field()
