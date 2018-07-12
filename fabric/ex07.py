#!/usr/bin/env python
# coding: utf-8 

from fabric.api import * 

env.hosts = '192.168.1.76'
env.user = 'jeff'
env.password = 'redhat' 

@task
def hostname():
    with settings(warn_only=True):
        run('hostname')

@task
def deploy():
    hostname()
