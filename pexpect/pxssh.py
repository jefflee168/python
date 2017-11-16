#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
本脚主要实现自定义输入主机、用户名和密码后，
只要信息正确就能成功登录远程主机，并在远程
主机上执行下面变量cmd中的命令。

"""

from pexpect import pxssh
import getpass

cmd = "hostname"

try:
    s = pxssh.pxssh()
    hostname = raw_input("Enter your host: ")
    username = raw_input("Enter your user: ")
    passwd = getpass.getpass("Please enter your password: ")
    # 登录远程主机
    s.login(hostname,username,passwd)
    # 远程执行命令
    s.sendline(cmd)
    s.prompt()
    print s.before
    # 注销登录
    s.logout
except pxssh.ExceptionPxssh as e:
    # 登录失败，输入错误信息
    print "Pxssh failed to login."
    print str(e)
