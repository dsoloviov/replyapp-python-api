#!/usr/bin/env python

import unittest
import requests
from reply import Reply
from resources import resources
from resources import helpers


class testPeopleEndpoint(unittest.TestCase):

    def setUp(self):
        self.reply = Reply('test-api-key')
        self.request = helpers.RawRequest()
        self.sanitizer = helpers.Sanitizer()
        # Create people
        for each in resources.people:
            res = self.request.createPeople(each)
            self.sanitizer.getId(res)

    def tearDown(self):
        # Delete people
        for _id in self.sanitizer.ids:
            self.request.deletePeople(_id)

    def testListAll(self):
        response = self.reply.people.list.all()

        jsonified = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonified['total'], 3)

    def testListByEmail(self):
        response = self.reply.people.list.email(resources.people[0]['email'])

        jsonified = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonified['firstName'], resources.people[0]['firstName'])
        self.assertEqual(jsonified['email'], resources.people[0]['email'])

    @unittest.skip('Skipping')
    def testNotFoundByEmail(self):
        pass

    def testListById(self):
        response = self.reply.people.list.id(self.sanitizer.ids[0])

        jsonified = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonified['firstName'], resources.people[0]['firstName'])
        self.assertEqual(jsonified['email'], resources.people[0]['email'])

    @unittest.skip('Skipping')
    def testNotFoundById(self):
        pass

    def testCreatePeople(self):
        response = self.reply.people.save.one(resources.people_create)
        self.sanitizer.getId(response)

        jsonified = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(jsonified['firstName'], resources.people_create['firstName'])
        self.assertEqual(jsonified['email'], resources.people_create['email'])

    @unittest.skip('Skipping')
    def testDeletePeopleByEmail(self):
        response = self.reply.people.delete.email(resources.people[0]['email'])
        self.assertEqual(response.status_code, 200)

        allPeople = self.request.listAllPeople()

        jsonified = allPeople.json()
        self.assertEqual(jsonified['total'], 2)

    @unittest.skip('Skipping')
    def testDeletePeopleById(self):
        response = self.reply.people.delete.id()
        self.assertEqual(response.status_code, 200)

        allPeople = self.request.listAllPeople()

        jsonified = allPeople.json()
        self.assertEqual(jsonified['total'], 2)


if __name__ == '__main__':
    unittest.main()
