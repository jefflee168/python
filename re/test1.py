#!/usr/bin/env python
# -*- coding: utf-8 

import re,requests

r = requests.get('http://auto.sina.com.cn/')
links = re.findall('"http?://.*?"', r.content)
print(links)
