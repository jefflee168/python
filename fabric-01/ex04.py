#!/usr/bin/env python
# coding: utf-8

from invoke import run

cmd = 'hostname'
result = run(cmd,hide=True,warn=True)
print(result.stdout.splitlines()[-1])
