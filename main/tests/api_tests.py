from base import AppTestCase
from faker import Faker
from flask.ext.login import login_user

import dateutil.parser
import factory
import flask.ext.login
import json
import main
import re
import string
import unittest

fake = Faker()

class ApiTests(AppTestCase):
    
    def setUp(self):
        super(ApiTests, self).setUp()

    def test_servertime(self):
        #main.main.logger.info("self client is" + str(self.client.get("/api/util/time")))
        servertime = self.client.get("/api/util/servertime")
        self.assertEquals(servertime._status_code, 200)
        #spam = json.loads(servertime.data)
        self.assertTrue(dateutil.parser.parse(json.loads(servertime.data)["now"]))
