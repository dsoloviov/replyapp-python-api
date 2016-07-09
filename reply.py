#!/usr/bin/env python

from requests import Request
from requests import Session


class Reply(object):

    def __init__(self, apiKey, v='v1', basePath='https://run.replyapp.io/api/'):
        self.basePath = basePath
        self.version = v
        self.headers = {'X-Api-Key': '%s' % apiKey}

        self.method = None
        self.endpoint = None

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
        # print path
        return path

    @property
    def people(self):
        self.endpoint = 'people'
        return self

    @property
    def campaigns(self):
        self.endpoint = 'campaigns'
        return self

    @property
    def list(self):
        self.method = 'GET'
        return self

    @property
    def save(self, data):
        self.method = 'POST'
        if data:
            # TODO: test it
            return self.__makeRequest('%s' % self.__makePath(), data=data)
        return self

    @property
    def delete(self):
        self.method = 'DELETE'
        return self

    def all(self):
        if self.method == 'GET':
            return self.__makeRequest('%s' % (self.__makePath()))
        else:
            pass  # handle delete here

    def email(self, email):
        return self.__makeRequest('%s' % (self.__makePath('?email=%s' % email)))

    def id(self, _id):
        return self.__makeRequest('%s' % (self.__makePath('/%s' % _id)))

    def one(self, email, firstName, lastName=None, company=None, title=None):
        info = {'email': email, 'firstName': firstName}
        # TODO: add ID
        if lastName:
            info['lastName'] = lastName
        if company:
            info['company'] = company
        if title:
            info['title'] = title
        return self.__makeRequest('%s' % self.__makePath(), data=info)


if __name__ == '__main__':
    pass
