#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

cache_dir = os.path.expanduser('~/.zapys/entries/')

if not os.path.isdir(cache_dir):
    os.makedirs(cache_dir)

def put(id, text):
    f = open(cache_dir+str(id)+'.text', 'w')
    f.write(text)
    f.close()

def get(id):
    return open(cache_dir+str(id)+'.text').read()

def get_temp():
    return open(cache_dir+'entry.html', 'w')
