#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ConfigParser, os
from xdg import BaseDirectory


config = ConfigParser.ConfigParser(dict(username='test', password='test', inline_replace='on' ))
conf_dir = BaseDirectory.save_config_path('zapys')

userconf = os.path.join(conf_dir, 'config.ini')

if os.path.exists(userconf):
    config.read(userconf)
else:
    config.write(open(userconf, 'w'))

username = config.get('DEFAULT', 'username')
password = config.get('DEFAULT', 'password')
