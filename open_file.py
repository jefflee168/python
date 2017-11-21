#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
本脚本主要实现定入内容到根目录下的
test.txt文件里，否则提示找不到文件
"""

import os
import sys

try:
    fh = open("test.txt","w")
    fh.write("This is a test.")
except IOError:
    print "Error: 没有找到test.txt文件."
else:
    print "内容写入成功！"
    fh.close()
