#!/usr/bin/env python
# coding: utf-8 

class MycwpjtPipeline(object):
    def process_item(self,item,spider):
        print(item["name"])
        print(item["link"])
	print("----------------")
	return item
