#!/usr/bin/env python
# coding: utf-8

from fabric import Connection
c = Connection('10.0.0.27')
c.run('hostname')
