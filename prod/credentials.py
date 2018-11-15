#!/usr/bin/python3
#Credentials for AMP Reborn api testing

HOME = "www.amp.com.au"
HTTP_BASIC_AUTH_USERNAME:"canary"
#HTTP_BASIC_AUTH_PASSWORD:""
HTTP_BASIC_AUTH_PASSWORD_B64:"dGhpcyBpcyBub3QgYSByZWFsIHJlcG8="
ENDPOINTS = {
                "PROD" : {
                    "URI":"reborn.amp.com.au:3337/api/v1/",
                    "USER":"canary",
                    "KEY":"dGhhdCdzIHJpZ2h0LCB3ZSdyZSB0ZXN0aW5nIGluIHByb2R1Y3Rpb24h"
                },
                "DEV" : {
                    "URI":"reborn-dev.amp.com.au:3337/api/v1",
                    "USER":"canary",
                    "KEY":"eW91IGp1c3QgZm91bmQgdGhlIG5pbmph"
                }
            }

DATABASES = {
                "PROD" : {
                    "DB_HOST":"reborn0.postgresql.internal.amp.com.au",
                    "PORT":"5432",
                    "USER":"root",
                    "KEY":"m8&cCdL35!*6"
                },
                "DEV" : {
                    "DB_HOST":"reborn1.postgresql.internal.amp.com.au",
                    "PORT":"5432",
                    "USER":"root",
                    "KEY":"root"
                }
            }

