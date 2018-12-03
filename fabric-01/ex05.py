#!/usr/bin/env python
# coding: utf-8 

# 此脚本的运行方式为: fab -f ex05.py deploy

from fabric.api import local

def deploy():
    local('hostname')
