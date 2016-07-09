#!/usr/bin/env python

import unittest
import requests
from reply import Reply
from resources import resources


class testPeopleEndpoint(unittest.TestCase):

    def setUp(self):
        self.reply = Reply('V6z-Vb-AGcAqfqxZxds3mQ2')  # TODO: get from config
        # Create people
        requests.post('%s%s/people' % (self.reply.basePath, self.reply.version),
                      data=resources.people_1, headers=self.reply.headers)
        requests.post('%s%s/people' % (self.reply.basePath, self.reply.version),
                      data=resources.people_2, headers=self.reply.headers)
        requests.post('%s%s/people' % (self.reply.basePath, self.reply.version),
                      data=resources.people_3, headers=self.reply.headers)

    def tearDown(self):
        # Delete people
        requests.delete('%s%s/people?email=%s' % (self.reply.basePath,
                                                  self.reply.version,
                                                  resources.people_1['email']),
                        headers=self.reply.headers)
        requests.delete('%s%s/people?email=%s' % (self.reply.basePath,
                                                  self.reply.version,
                                                  resources.people_2['email']),
                        headers=self.reply.headers)
        requests.delete('%s%s/people?email=%s' % (self.reply.basePath,
                                                  self.reply.version,
                                                  resources.people_3['email']),
                        headers=self.reply.headers)

    def testListAll(self):
        response = self.reply.people.list.all()
        self.assertEqual(response.status_code, 200)

        jsonified = response.json()
        self.assertEqual(jsonified['total'], 3)

    def testListByEmail(self):
        response = self.reply.people.list.email('test1@example.com')
        self.assertEqual(response.status_code, 200)
        jsonified = response.json()
        self.assertEqual(jsonified['firstName'], 'Test1')
        self.assertEqual(jsonified['email'], 'test1@example.com')

    @unittest.skip('Skipping')
    def testListById(self):
        response = self.reply.people.list.id(6488674)
        self.assertEqual(response.status_code, 200)

    @unittest.skip('Skipping')
    def testCreatePeople(self):
        response = self.reply.people.save.one('test@example.com', 'TestName')
        self.assertEqual(response.status_code, 201)

    @unittest.skip('Skipping')
    def testDeletePeople(self):
        response = self.reply.people.delete.email('test@example.com')
        self.assertEqual(response.status_code, 200)
