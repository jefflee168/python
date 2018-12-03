#!/usr/bin/env python
# coding: utf-8

from frabric import Connection

c = Connection('127.0.0.1')
c.run('hostname')
