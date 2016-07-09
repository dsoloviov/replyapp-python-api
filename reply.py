#!/usr/bin/env python

from requests import Request
from requests import Session


class Reply(object):

    def __init__(self, apiKey, v='v1'):
        self.basePath = 'https://run.replyapp.io/api/'
        self.apiKey = apiKey
        self.version = v
        self.method = 'GET'
        self.endpoint = None
        self.headers = {'X-Api-Key': '%s' % self.apiKey}

    def configure(self, apiKey, v='v1'):
        """
        There is a bug in API: old key can
        be used, new key sometimes fails.
        """
        self.apiKey = apiKey
        self.version = v
        self.cursor = self.__setup()

    def __makeRequest(self, path, data=None):
        s = Session()
        req = Request(self.method,
                      url=path,
                      data=data,
                      headers=self.headers)
        prepped = s.prepare_request(req)
        return s.send(prepped)

    def __makePath(self, query=None):
        path = '%s%s/%s' % (self.basePath, self.version, self.endpoint)
        path += query if query else ''
        print path
        return path

    def people(self):
        self.endpoint = 'people'
        return self

    def campaigns(self):
        self.endpoint = 'campaigns'
        return self

    def list(self, _id=None, email=None, name=None):
        if _id:
            return self.__makeRequest('%s' % (self.__makePath('/%s' % _id)))
        elif email:
            return self.__makeRequest('%s' % (self.__makePath('?email=%s' % email)))
        elif name:
            return self.__makeRequest('%s' % (self.__makePath('?name=%s' % name)))
        return self.__makeRequest('%s' % (self.__makePath()))


if __name__ == '__main__':
    reply = Reply('api-key')
    response = reply.people().list()
    print response.json()
