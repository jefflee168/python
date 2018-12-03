#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
import pprint
from pymongo import MongoClient

# 连接mongo
client = MongoClient('mongodb://root:redhat@10.0.0.26:27017/admin')

db = client.testdb

# 插入文档
post = {"author": "Jeff",
        "test": "My first blog post!",
        "tags": ["mongodb","python","pymongo"],
        "date": datetime.datetime.now()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

# 获取 post id
print("post id is",post_id)

# 空一行,将前后的显示内容分开
print('\n')

# 获取整个文档
print("获取整个文档...")
pprint.pprint(posts.find_one())
