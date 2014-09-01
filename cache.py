#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from xdg import BaseDirectory


cache_dir = BaseDirectory.save_cache_path('zapys')

def put(id, text):
    f = open(os.path.join(cache_dir, str(id) + '.text'), 'w')
    f.write(text)
    f.close()

def get(id):
    return open(os.path.join(cache_dir, str(id) + '.text')).read()

def get_temp():
    return open(os.path.join(cache_dir, 'entry.html'), 'w')
