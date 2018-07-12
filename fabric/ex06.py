#!/usr/bin/env python
# coding: utf-8

from fabric.api import *
from fabric.contrib.console import confirm

@task
def uninstall_redis():
    local("apt-get install -y redis-server")

@task
def install_redis():
    local("apt-get install -y redis-server")

@task
def deploy():
    uninstall_redis()
    install_redis()
