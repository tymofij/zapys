#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ConfigParser
c = ConfigParser.ConfigParser(dict(username='test', password='test', inline_replace='on' ))

import os

conf_dir = os.path.expanduser('~/.zapys/')

if not os.path.isdir(conf_dir):
    os.makedirs(conf_dir)

userconf = conf_dir+'config'

if os.path.exists(userconf):
    c.read(userconf)
else:
    c.write(open(userconf, 'w'))

username = c.get('DEFAULT', 'username')
password = c.get('DEFAULT', 'password')
