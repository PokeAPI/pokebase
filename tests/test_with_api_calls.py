# -*- coding: utf-8 -*-

from os import environ
import unittest

import pokebase as pb

@unittest.skipIf(environ.get('MOCK_ONLY', False), 'only running mock API calls')
class TestAPICalls(unittest.TestCase):
    
    def testFunction__call_api(self):
        self.assertIsInstance(pb.api._call_api('berry', 1),
                              dict)

    def testFunction_get_data(self):
        self.assertIsInstance(pb.api.get_data('berry', 1, force_lookup=True),
                              dict)

    def testClass_APIResource(self):
        self.assertIsInstance(pb.APIResource('berry', 1, force_lookup=True),
                              pb.APIResource)

    def testClass_APIResourceList(self):
        self.assertIsInstance(pb.APIResourceList('berry', force_lookup=True),
                              pb.APIResourceList)
