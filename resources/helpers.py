#!/usr/bin/env python

import requests
import resources
from reply import Reply


class Sanitizer(object):

    def __init__(self):
        self.ids = []

    def getId(self, response):
        try:
            jsonified = response.json()
            self.ids.append(jsonified['id'])
        except ValueError:
            pass


class RawRequest(object):

    def __init__(self):
        self.reply = Reply('V6z-Vb-AGcAqfqxZxds3mQ2')
        self.basePath = self.reply.basePath
        self.version = self.reply.version
        self.headers = self.reply.headers

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def listAllPeople(self):
        return self.session.get('%s%s/people' % (self.basePath,
                                                 self.version))

    def createPeople(self, data):
        return self.session.post('%s%s/people' % (self.basePath,
                                                  self.version),
                                 data=data)

    def deletePeople(self, _id):
        return self.session.delete('%s%s/people/%s' % (self.basePath,
                                                       self.version,
                                                       _id))
