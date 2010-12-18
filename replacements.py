#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

lj_username = '[a-zA-Z0-9_]+'
url_regexp = r'(\s|^)(https?:\/\/)([^\s\"\<\>]+)(\s|$)'

pre_markdown = [
    (u'(\s+?|^)"([^"а-ягўєїА-ЯҐЎЄЇ]+?)"(\s+?|$|\.|\,|\!|\?)', r'\1“\2”\3'), # non-cyr test, dbl quotes
    (u'(\s+?|^)"([^"]+?)"(\s+?|$|\.|\,|\!|\?)', u'\\1«\\2»\\3'), # cyrillic text, lapky
    (u"\((tm|тм|TM|ТМ)\)", "™"),  # ™
    (u"\([cсCС]\)", "©"), # ©
    (u"\([rRрР]\)", "®"), # ®
    ('(\s+|^)-(\s+)',  r"\1—\2"), # m-dash
    ('(\s+)(\d+)-(\d+)(\s+)', r"\1\2–\3\4"),	# n-dash
    ('\.\.\.', "…"), # …
    ('(\s+|^)1/2(\s+|$)', r"\1½\2"), # ½
    ('(\s+|^)1/4(\s+|$)', r"\1¼\2"), # ¼
    (u'([а-яА-я])\*([а-яА-я])', r"\1’\2"), # ukrainian apostrope
    (url_regexp, r'\1<a href="\2\3">\3</a>\4'), # clickable urls
]

post_markdown = [
    ('LJ:('+lj_username+')', r'<lj user="\1"/>'), # LJ:username to <lj user="">
    ('([^\!]|^)-{2}([^-]+?)-{2}', r'\1<s>\2</s>'), # --text--  to <s>text</s>
    # nice citations on (( ))
    (r"\(\(([\s\S]+?)\)\)", r'<div style="border-left: 5px solid silver; padding:5px; margin: 10px; background: #eeeeee;">\1</div>'),
]

pre_markdown = [(re.compile(search), repl) for (search, repl) in pre_markdown]
post_markdown = [(re.compile(search), repl) for (search, repl) in post_markdown]
