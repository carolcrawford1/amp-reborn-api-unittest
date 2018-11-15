#!/usr/bin/python3
#Unit test for status listing action

import requests
import unittest
from authenticatedTestCase import AuthenticatedTestCase

class TestStatus(AuthenticatedTestCase):
    def test_status_basic(self):
        self
        url = self.prod["URI"] + "status"
        payload = {"auth_key":self.auth_key, "id":0}
        r = requests.get(url, params=payload)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "ready")

    def test_status_invalid_negative(self):
        self
        url = self.prod["URI"] + "status"
        payload = {"auth_key":self.auth_key, "id":-1}
        r = requests.get(url, params=payload)
        self.assertNotEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "fail")

    def test_status_invalid_huge(self):
        self
        url = self.prod["URI"] + "status"
        payload = {"auth_key":self.auth_key, "id":1337}
        r = requests.get(url, params=payload)
        self.assertNotEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "fail")

if __name__ == '__main__':
    unittest.main()
