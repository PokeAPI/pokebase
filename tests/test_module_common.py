# -*- coding: utf-8 -*-

import unittest

from hypothesis import given
from hypothesis.strategies import sampled_from, none, text, integers

from pokebase import common


class TestFunction_validate(unittest.TestCase):
 
    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=none())
    def testParamExpected_endpoint(self, endpoint, resource_id):
        self.assertIsNone(common.validate(endpoint, resource_id))

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1))
    def testParamExpected_resource_id(self, endpoint, resource_id):
        self.assertIsNone(common.validate(endpoint, resource_id))

    @given(endpoint=text(),
           resource_id=none())
    def testParamUnexpected_endpoint(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.validate(endpoint, resource_id)

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=text())
    def testParamUnexpected_resource_id(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.validate(endpoint, resource_id)


class TestFunction_apl_uri_build(unittest.TestCase):

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1))
    def testParamExpected_resource_id(self, endpoint, resource_id):
        self.assertEqual(common.api_url_build(endpoint, resource_id),
                         'http://pokeapi.co/api/v2/{}/{}'
                         .format(endpoint, resource_id))

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=none())
    def testParamNone_resource_id(self, endpoint, resource_id):
        self.assertEqual(common.api_url_build(endpoint, resource_id),
                         'http://pokeapi.co/api/v2/{}'
                         .format(endpoint))

    @given(endpoint=text(),
           resource_id=none())
    def testParamUnexpected_endpoint(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.api_url_build(endpoint, resource_id)


class TestFunction_cache_uri_build(unittest.TestCase):

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1))
    def testParamExpected_resource_id(self, endpoint, resource_id):
        self.assertEqual(common.cache_uri_build(endpoint, resource_id),
                         '{}/{}'.format(endpoint, resource_id))

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=none())
    def testParamNone_resource_id(self, endpoint, resource_id):
        self.assertEqual(common.cache_uri_build(endpoint, resource_id),
                         endpoint)

    @given(endpoint=text(),
           resource_id=none())
    def testParamUnexpected_endpoint(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.cache_uri_build(endpoint, resource_id)


if __name__ == '__main__':
    unittest.main()
