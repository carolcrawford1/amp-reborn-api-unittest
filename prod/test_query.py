#!/usr/bin/python3
#Unit test for query action
#Run after manifest update

import requests
import unittest
from authenticatedTestCase import AuthenticatedTestCase

class TestQuery(AuthenticatedTestCase):
    def test_query(self):
        self
        url = self.prod["URI"] + "query"
        payload = {"auth_key":self.auth_key, "id":3}
        r = requests.get(url, params=payload)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "ready")
        self.assertEqual(r.json()["id"]:3)
        self.assertEqual(r.json()["frst_name"]:"Jane")
        self.assertEqual(r.json()["last_name"]:"Austen")
        self.assertEqual(r.json()["email"]:"j.austen1775@gmail.com")
        self.assertEqual(r.json()["phone"]:"+614928892615")
        self.assertEqual(r.json()["username"]:"jausten")
        self.assertEqual(r.json()["password"]:"jau1218")

    def test_query_invalid_negative(self):
        self
        url = self.prod["URI"] + "query"
        payload = {"auth_key":self.auth_key, "id":-1}
        r = requests.get(url, params=payload)
        self.assertNotEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "fail")

    def test_query_invalid_huge(self):
        self
        url = self.prod["URI"] + "query"
        payload = {"auth_key":self.auth_key, "id":1337}
        r = requests.get(url, params=payload)
        self.assertNotEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "fail")

if __name__ == '__main__':
    unittest.main()
