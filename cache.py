#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from xdg import BaseDirectory


cache_dir = BaseDirectory.save_cache_path('zapys')

def put(server, id, text):
    if not os.path.exists(os.path.join(cache_dir, server)):
        os.makedirs(os.path.join(cache_dir, server))
    f = open(os.path.join(cache_dir, server, str(id) + '.text'), 'w')
    f.write(text)
    f.close()

def get(server, id):
    return open(os.path.join(cache_dir, server, str(id) + '.text')).read()

def get_temp():
    return open(os.path.join(cache_dir, 'entry.html'), 'w')
