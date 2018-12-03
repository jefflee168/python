#!/usr/bin/env python
# -*- coding: utf-8 

##############################
# 此脚本实现的功能为：获取页面 
# http://auto.sina.com.cn/ 
# 中的所有超链接
##############################

import re,requests

r = requests.get('http://auto.sina.com.cn/')
links = re.findall('"http?://.*?"', r.content)
print(links)
