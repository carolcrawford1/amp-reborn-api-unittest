#!/usr/bin/python3
#Unit test for update action
#Run after manifest update

import requests
import unittest
from authenticatedTestCase import AuthenticatedTestCase

class TestUpdate(AuthenticatedTestCase):
    #POST
    def test_update(self):
        self
        url = self.prod["URI"] + "update"
        payload = {"auth_key":self.auth_key}

        id_no = 3
        new_first_name = "Jane"
        new_last_name = "Citizen"
        new_email = "jcitizen@amp.com.au"
        new_phone = "+610987654321"
        new_username = "jcitizen"
        new_password = "password"

        payload["id"] = id_no
        payload["first_name"] = new_first_name
        payload["last_name"] = new_last_name
        payload["email"] = new_email
        payload["phone"] = new_phone
        payload["username"] = new_username
        payload["password"] = new_password

        #test before change
        self.assertEqual(r.json()["status"], "ready")
        self.assertEqual(r.json()["id"]:id_no)
        self.assertEqual(r.json()["frst_name"]:"Jane")
        self.assertEqual(r.json()["last_name"]:"Austen")
        self.assertEqual(r.json()["email"]:"j.austen1775@gmail.com")
        self.assertEqual(r.json()["phone"]:"+614928892615")
        self.assertEqual(r.json()["username"]:"jausten")
        self.assertEqual(r.json()["password"]:"jau1218")

        #make update
        r = requests.post(url, params=payload)
        self.assertEqual(r.status_code, 200)

        #get new values, check if expected
        url = self.dev["URI"] + "query"
        payload = {"auth_key":self.auth_key, "id":id_no}
        r = requests.get(url, params=payload)
        self.assertEqual(r.status_code, 200)

        self.assertEqual(r.json()["status"], "ready")
        self.assertEqual(r.json()["id"]:id_no)
        self.assertEqual(r.json()["frst_name"]:new_first_name)
        self.assertEqual(r.json()["last_name"]:new_last_name)
        self.assertEqual(r.json()["email"]:new_email)
        self.assertEqual(r.json()["phone"]:new_phone)
        self.assertEqual(r.json()["username"]:new_username)
        self.assertEqual(r.json()["password"]:new_password)

if __name__ == '__main__':
    unittest.main()
