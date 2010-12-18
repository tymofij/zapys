#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import markdown, re
import replacements

lj_username = '[a-zA-Z0-9_]+'

# custom shortcuts
def post(text):
    res = unicode(text)
    
    for search, repl in replacements.pre_markdown:
        res = re.sub(search, repl, res)

    res = markdown.markdown(res)

    for search, repl in replacements.post_markdown:
        res = re.sub(search, repl, res)

    return res

# <lj user and <lj-cut displaying
def preview(text):
    res = post(text)
    res = re.sub("<[Ll][Jj]\s+[Uu][Ss][Ee][Rr]=['\"]?("+lj_username+")['\"]?.*?>", 
        r'<img src="file://'+prog_dir+r'/userinfo.gif" style="position: relative; top: 3px;" alt="[info]" border="0"><a href="http://www.livejournal.com/users/\1/"><b>\1</b></a>',  res)
    return res

