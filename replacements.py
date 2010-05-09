#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

lj_username = '[a-zA-Z0-9_]+'
url_regexp = r'(\s|^)(https?:\/\/)([^\s\"\<\>]+)(\s|$)'

# replaced on the fly
inline = [
('(\s+|^)"([^"]+?)"(\s+|$|\.|\,)', r"\1«\2»\3"), # russian quotes
#('(\s+|^)"([^"]+?)"(\s+|$|\.|\,)', r"\1“\2”\3"), # english quotes

(u"\((tm|тм|TM|ТМ)\)",	"™"),		# ™
(u"\([cсCС]\)",		"©"),		# ©
(u"\([rRрР]\)",		"®"),		# ®
('(\s+|^)-(\s+)', 		r"\1—\2"),	# m-dash
('(\s+)(\d+)-(\d+)(\s+)', 		r"\1\2–\3\4"),	# n-dash
('\.\.\.',			"…"),		# …
('(\s+|^)1/2(\s+|$)', r"\1½\2"),	# ½
('(\s+|^)1/4(\s+|$)', r"\1¼\2"),	# ¼
(u'([а-яА-я])\*([а-яА-я])', r"\1’\2")	# ukrainian apostrope 
]

publish = [
(url_regexp, r'\1<a href="\2\3">\3</a>\4'), # clickable urls
('LJ:('+lj_username+')', r'<lj user="\1"/>'), # LJ:username to <lj user="">
('([^\!]|^)-{2}([^-]+?)-{2}', r'\1<s>\2</s>') # --text--  to <s>text</s>
]

inline = [(re.compile(search), repl) for (search, repl) in inline]
publish = [(re.compile(search), repl) for (search, repl) in publish]
