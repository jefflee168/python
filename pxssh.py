#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pexpect import pxssh
import getpass

cmd = "hostname"

try:
    s = pxssh.pxssh()
    hostname = raw_input("Enter your host: ")
    username = raw_input("Enter your user: ")
    passwd = getpass.getpass("Please enter your password: ")
    s.login(hostname,username,passwd)
    s.sendline(cmd)
    s.prompt()
    print s.before
    s.logout
except pxssh.ExceptionPxssh as e:
    print "Pxssh failed to login."
    print str(e)
