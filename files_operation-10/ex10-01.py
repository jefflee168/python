#!/usr/bin/env python
# -*- coding: utf-8 _8-

try:
    f = open('/home/jeff/1.txt')
    print(f.read())
finally:
    f.close()
