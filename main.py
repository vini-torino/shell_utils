#!/usr/bin/python
# - * - coding: utf-8  - * -

import os 


os.environ['PYSHELL_VERSION'] = '0.1'
os.environ['PYSHELL_HOME'] = os.getcwd()
os.environ['PYSHELL_USER'] = os.getenv('USER')

import pyshell_profile
pyshell_profile.set_profile()

