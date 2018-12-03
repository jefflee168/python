#!/usr/bin/env python
# -*- coding: utf-8 _8-

# 本例使用上下文管理器，使代码更加简洁优美

try:
#    f = open('/home/jeff/1.txt')
#    print(f.read())
    with open('/home/jeff/1.txt') as f:
        print(f.read())
finally:
    f.close()
