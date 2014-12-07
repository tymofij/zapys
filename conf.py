#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ConfigParser, os
from xdg import BaseDirectory

XML_RPC_URLS = {
    'LiveJournal': 'http://www.livejournal.com/interface/xmlrpc',
    'DreamWidth': 'http://www.dreamwidth.org/interface/xmlrpc',
}
config = ConfigParser.ConfigParser({
    'inline_replace': 'on',
    'server': 'LiveJournal',
})
conf_file = os.path.join(BaseDirectory.save_config_path('zapys'), 'config.ini')

if os.path.exists(conf_file):
    config.read(conf_file)
else:
    config.write(open(conf_file, 'w'))

server = config.get('DEFAULT', 'server')
server_url = XML_RPC_URLS[server]
username = config.get(server, 'username')
password = config.get(server, 'password')
