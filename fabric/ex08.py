#!/use/bin/env python
# coding: utf-8

# 此脚本同时操作两台机，两台机执行不同的命令

from fabric.api import *

env.roledefs = {
    'node1': ['10.0.0.27'],
    'node2': ['10.0.0.28']
}

env.passwords = {
    'jeff@10.0.0.27:22': 'redhat',
    'jeff@10.0.0.28:22': 'redhat'
}

@roles('node1')
def task1():
    with settings(warn_only=True):
        run('hostname')

@roles('node2')
def task2():
    with settings(warn_only=True):
        run('hostname')

def deploy():
    execute(task1)
    execute(task2)
