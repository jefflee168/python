#!/usr/bin/env python
# coding: utf-8

import scrapy 

class MycwpjtItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
