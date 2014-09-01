#!/usr/bin/env python
# -*- coding: UTF8 -*-


import xmlrpclib, time
from hashlib import md5

LJ_TIME_FORMAT = r"%Y-%m-%d %H:%M:%S"

class rpcServer:
    username = ''
    password = ''
    initialized = False

    last_event = {}

    def __init__(self, user, password):
        self.username = user
        self.hpassword = md5(password).hexdigest()

    def connect(self):
        if not self.initialized:
            self.server = xmlrpclib.Server("http://www.livejournal.com/interface/xmlrpc")
            self.initialized = True

    def get_last(self):

        self.connect()
        result = self.server.LJ.XMLRPC.getevents({
            'username': self.username,
            'hpassword': self.hpassword,
            'ver': '1',
            'lineendings': '0x0A',
            "selecttype": "lastn",
            "itemid": -1,
            "howmany": 1
            })

        return result['events'][0]

    def del_event(self, itemid):
        return self.server.LJ.XMLRPC.editevent({
            'username': self.username,
            'hpassword': self.hpassword,
            'ver': '1',
            "itemid": itemid,
            })

    # post is dict {subj, taglist, text}
    def post(self, post, eventtime = None):
        self.connect()
        if eventtime == None:
            moment = time.localtime()
        else:
            moment = time.strptime(eventtime, LJ_TIME_FORMAT)

        return self.server.LJ.XMLRPC.postevent({
            'username': self.username,
            'hpassword': self.hpassword,
            'clientversion': 'Zapys/0.8',
            'ver':'1',
            'event': post['text'],
            'subject': post['subj'],
            'props': {'taglist': post['tags'], 'opt_preformatted': True},
            'year': moment[0],
            'mon': moment[1],
            'day': moment[2],
            'hour' : moment[3],
            'min': moment[4],
            'lineendings':'0x0A'
            })

    # post is dict {subj, tags, text}
    def edit(self, itemid, eventtime, post ):
        moment = time.strptime(eventtime, LJ_TIME_FORMAT)
        return self.server.LJ.XMLRPC.editevent({
            'username': self.username,
            'hpassword': self.hpassword,
            'ver': '1',
            "itemid": itemid,
            'event': post['text'],
            'subject': post['subj'],
            'props': {'taglist': post['tags'], 'opt_preformatted': True},
            'year': moment[0],
            'mon': moment[1],
            'day': moment[2],
            'hour' : moment[3],
            'min': moment[4],
            })

