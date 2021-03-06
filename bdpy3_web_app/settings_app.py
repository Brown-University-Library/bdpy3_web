# -*- coding: utf-8 -*-

import json, os


WEB_API_AUTHORIZATION_CODE = os.environ['BDPY3WEB__API_AUTHORIZATION_CODE']  # for v1
WEB_API_IDENTITY = os.environ['BDPY3WEB__API_IDENTITY']  # for v1

LEGIT_IPS = json.loads( os.environ['BDPY3WEB__LEGIT_IPS'] )

README_URL = os.environ['BDPY3WEB__README_URL']

BDPY3_API_URL_ROOT = os.environ['BDPY3WEB__BDPY3_API_ROOT_URL']
BDPY3_API_KEY = os.environ['BDPY3WEB__BDPY3_API_KEY']
BDPY3_UNIVERSITY_CODE = os.environ['BDPY3WEB__BDPY3_UNIVERSITY_CODE']
BDPY3_PARTNERSHIP_ID = os.environ['BDPY3WEB__BDPY3_PARTNERSHIP_ID']
BDPY3_PICKUP_LOCATION = os.environ['BDPY3WEB__BDPY3_PICKUP_LOCATION']


## for bdpy3 caller tests

TEST_API_URL_ROOT = os.environ['BDPY3WEB__BDPY3TEST_API_ROOT_URL']
TEST_AUTH_CODE = os.environ['BDPY3WEB__BDPY3TEST_AUTH_CODE']
TEST_IDENTITY = os.environ['BDPY3WEB__BDPY3TEST_IDENTITY']
TEST_ISBN_NOT_FOUND = os.environ['BDPY3WEB__BDPY3TEST_ISBN_NOT_FOUND']
TEST_PATRON_BARCODE = os.environ['BDPY3WEB__BDPY3TEST_PATRON_BARCODE']
