#!/use/bin/env python
# coding: utf-8

# 此脚本同时操作两台机，两台机执行不同的命令

from fabric.api import *

env.roledefs = {
    'server1': ['192.168.1.76'],
    'server2': ['192.168.1.204'],
}

env.passwords = {
    'jeff@192.168.1.76:22': 'redhat',
    'biliang@192.168.1.204:22': 'pzzh123456',
}

@roles('server1')
def task1():
    run('ip addr show')

@roles('server2')
def task2():
    run('hostname')

def deploy():
    execute(task1)
    execute(task2)
