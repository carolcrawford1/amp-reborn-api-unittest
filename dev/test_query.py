#!/usr/bin/python3
#Unit test for query action
#Run after manifest update

import requests
import unittest
from authenticatedTestCase import AuthenticatedTestCase

class TestQuery(AuthenticatedTestCase):
    def test_query(self):
        self
        url = self.dev["URI"] + "query"
        payload = {"auth_key":self.auth_key, "id":0}
        r = requests.get(url, params=payload)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "ready")
        self.assertEqual(r.json()["id"]:0)
        self.assertEqual(r.json()["frst_name"]:"John")
        self.assertEqual(r.json()["last_name"]:"Smith")
        self.assertEqual(r.json()["email"]:"jsmith@test.email")
        self.assertEqual(r.json()["phone"]:"+61234567890")
        self.assertEqual(r.json()["username"]:"jsmith")
        self.assertEqual(r.json()["password"]:"qwerty")

    def test_query_invalid_negative(self):
        self
        url = self.dev["URI"] + "query"
        payload = {"auth_key":self.auth_key, "id":-1}
        r = requests.get(url, params=payload)
        self.assertNotEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "fail")

    def test_query_invalid_huge(self):
        self
        url = self.dev["URI"] + "query"
        payload = {"auth_key":self.auth_key, "id":1337}
        r = requests.get(url, params=payload)
        self.assertNotEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "fail")

if __name__ == '__main__':
    unittest.main()
