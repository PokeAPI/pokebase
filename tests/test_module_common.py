# -*- coding: utf-8 -*-

import unittest

from hypothesis import given
from hypothesis.strategies import sampled_from, none, text, integers

from pokebase import common


class TestFunction_validate(unittest.TestCase):
 
    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=none())
    def testArg_endpoint_Sampled(self, endpoint, resource_id):
        self.assertIsNone(common.validate(endpoint, resource_id))

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1))
    def testArg_resource_id_NonNegInt(self, endpoint, resource_id):
        self.assertIsNone(common.validate(endpoint, resource_id))

    @given(endpoint=text(),
           resource_id=none())
    def testArg_endpoint_Text(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.validate(endpoint, resource_id)

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=text())
    def testArg_resource_id_Text(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.validate(endpoint, resource_id)


class TestFunction_api_uri_build(unittest.TestCase):

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1))
    def testArg_resource_id_NonNegInt(self, endpoint, resource_id):
        self.assertEqual(common.api_url_build(endpoint, resource_id),
                         'http://pokeapi.co/api/v2/{}/{}/'
                         .format(endpoint, resource_id))

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=none())
    def testArg_resource_id_None(self, endpoint, resource_id):
        self.assertEqual(common.api_url_build(endpoint, resource_id),
                         'http://pokeapi.co/api/v2/{}/'
                         .format(endpoint))

    @given(endpoint=text(),
           resource_id=none())
    def testArg_endpoint_Text(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.api_url_build(endpoint, resource_id)

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1),
           subresource=text())
    def testArg_subresource_Text(self, endpoint, resource_id, subresource):
        self.assertEqual(common.api_url_build(endpoint, resource_id, subresource),
                         'http://pokeapi.co/api/v2/{}/{}/{}/'
                         .format(endpoint, resource_id, subresource))


class TestFunction_cache_uri_build(unittest.TestCase):

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1))
    def testArgs(self, endpoint, resource_id):
        self.assertEqual(common.cache_uri_build(endpoint, resource_id),
                         '{}/{}/'.format(endpoint, resource_id))

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=none())
    def testArg_resource_id_None(self, endpoint, resource_id):
        self.assertEqual(common.cache_uri_build(endpoint, resource_id),
                         '/'.join([endpoint, '']))

    @given(endpoint=text(),
           resource_id=none())
    def testArg_endpoint_Text(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            common.cache_uri_build(endpoint, resource_id)

    @given(endpoint=sampled_from(common.ENDPOINTS),
           resource_id=integers(min_value=1),
           subresource=text())
    def testArg_subresource_Text(self, endpoint, resource_id, subresource):
        self.assertEqual(common.cache_uri_build(endpoint, resource_id, subresource),
                         '/'.join([endpoint, str(resource_id), subresource, '']))
