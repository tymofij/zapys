#!/usr/bin/env python
# -*- coding: UTF8 -*-

# gives something of that kind 
#  (
#  { 9 : {'insert': ']', 'drop_n': 1} }
#  { 4 {'insert': 'BGB', 'drop_n': 2} }
# )
# char_number: { what to insert, how_many_characters_to_drop}
import difflib

def diff(a,b):
	diff = [(x[0:1],x[2:]) for x in difflib.ndiff(a,b)]

	r_diff = {}
	
	n_char = 0
	removed_chars = 0
	for i, (code, char) in enumerate(diff):
		if code != ' ':
			if not r_diff.has_key(n_char):
				r_diff[n_char] = {'insert': '', 'drop_n': 0}
			if code == '+':
				r_diff[n_char]['insert'] += char
			else:
				removed_chars += 1
				r_diff[n_char]['drop_n'] = removed_chars
		else:
			n_char += 1
			n_char += removed_chars
			removed_chars = 0
	return r_diff

if __name__ == "__main__":
	a = u"© sdfs ** df «fsdfs»"
	b = u"© sdfs ===** df fsdfs»"
	
	r_diff = diff(a,b)
	for r in r_diff.items():
		print r
		
	import gtk
	
	buffer = gtk.TextBuffer()
	buffer.set_text(a)
	
	for n_char, repl in r_diff.items():
		start = buffer.get_iter_at_offset(n_char)
		end = start.copy()
		end.forward_chars(repl['drop_n'])
		buffer.delete(start, end)
		buffer.insert(start, repl['insert'])
	
	start, end = buffer.get_bounds()
	print buffer.get_text(start, end)
		
		