#!/usr/bin/env python
# coding: utf-8

from fabric.api import *

def deploy():
    local('hostname')
