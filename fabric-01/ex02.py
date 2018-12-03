#!/usr/bin/env python
# coding: utf-8

# 此脚本适合fabric 2.0以上的版本使用

from fabric import Connection
c = Connection('10.0.0.27')
c.run('hostname')
