#!/usr/bin/python3
#Unit Test Object that automatically authenticates to AMP Reborn API for unit testing

from credentials import ENDPOINTS
import requests
import unittest

class AuthenticatedTestCase(unittest.TestCase):
    def setUp(self):
        self.prod = ENDPOINTS["PROD"]
        self.dev = ENDPOINTS["DEV"]
        url = dev["URI"] + "auth"
        auth_payload = {"username":self.dev["USER"], "password":self.dev["KEY"]}
        #auth_payload = {"username":"admin", "passowrd":"password"}
        r = requests.post(url, params=auth_payload)
        if r.status_code != 200:
            raise Exception("Not 200")
        r_json = r.json()
        if r_json["status"] != "ready":
            raise Exception("Auth Failed")
        self.auth_key = r_json["AUTH_KEY"]

if __name__ == '__main__':
    unittest.main()
