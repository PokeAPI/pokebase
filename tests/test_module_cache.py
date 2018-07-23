# -*- coding: utf-8 -*-

import importlib
import shelve
import os
import unittest

from hypothesis import given
from hypothesis.strategies import sampled_from, integers, dictionaries, text, assume, characters

from pokebase import cache
from pokebase.common import ENDPOINTS


class TestFunction_save(unittest.TestCase):
    
    # cache.save(data, endpoint, resource_id=None)

    def setUp(self):
        cache.set_cache('testing')

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testArgs(self, data, endpoint, resource_id):
        self.assertIsNone(cache.save(data, endpoint, resource_id))

    @given(data=text(),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testArg_data_Text(self, data, endpoint, resource_id):
        with self.assertRaises(ValueError):
            cache.save(data, endpoint, resource_id)

    @given(data=dictionaries(text(), text()),
           endpoint=text(),
           resource_id=integers(min_value=1))
    def testArg_endpoint_Text(self, data, endpoint, resource_id):
        assume(data != dict())
        with self.assertRaises(ValueError):
            cache.save(data, endpoint, resource_id)

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=text())
    def testArg_resource_id_Text(self, data, endpoint, resource_id):
        assume(data != dict())
        with self.assertRaises(ValueError):
            cache.save(data, endpoint, resource_id)

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1),
           subresource=text())
    def testArg_subresource_Text(self, data, endpoint, resource_id, subresource):
        self.assertIsNone(cache.save(data, endpoint, resource_id, subresource))

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testEnv_CacheFileNotFound(self, data, endpoint, resource_id):
        assume(data != dict())
        os.remove(cache.API_CACHE)
        self.assertIsNone(cache.save(data, endpoint, resource_id))

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testEnd_CacheFileAlreadyOpen(self, data, endpoint, resource_id):
        cache_db = shelve.open(cache.API_CACHE)
        self.assertIsNone(cache.save(data, endpoint, resource_id))
        cache_db.close()


class TestFunction_load(unittest.TestCase):
    
    # cache.load(endpoint, resource_id=None)

    def setUp(self):
        cache.set_cache('testing')

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testArgs(self, data, endpoint, resource_id):
        assume(data != dict())
        cache.save(data, endpoint, resource_id)
        self.assertEqual(data, cache.load(endpoint, resource_id))

    @given(endpoint=text(),
           resource_id=integers(min_value=1))
    def testArg_endpoint_Text(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            cache.load(endpoint, resource_id)

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=text())
    def testArg_resource_id_Text(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            cache.load(endpoint, resource_id)

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1),
           subresource=text())
    def testArg_subresource_Text(self, data, endpoint, resource_id, subresource):
        assume(data != dict())
        cache.save(data, endpoint, resource_id, subresource)
        self.assertEqual(data, cache.load(endpoint, resource_id, subresource))

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testEnv_CacheFileNotFound(self, endpoint, resource_id):
        # ensure it exsists before we delete it,
        cache.set_cache('testing')
        os.remove(cache.API_CACHE)
        with self.assertRaises(KeyError):
            cache.load(endpoint, resource_id)

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    @unittest.skip('inconsistency between Travis-CI/local machine')
    def testEnv_CacheFileAlreadyOpen(self, endpoint, resource_id):
        cache_db = shelve.open(cache.API_CACHE)
        with self.assertRaises(KeyError):
            cache.load(endpoint, resource_id)
        cache_db.close()

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testEnv_KeyNotInCache(self, endpoint, resource_id):

        with shelve.open(cache.API_CACHE) as c:
            key = cache.cache_uri_build(endpoint, resource_id)
            if key in c:
                del c[key]

        with self.assertRaises(KeyError):
            cache.load(endpoint, resource_id)


class TestFunction_set_cache(unittest.TestCase):
    
    # cache.set_cache(new_path=None)
    
    default_home = os.path.join(os.path.expanduser('~'), '.cache')

    def testAttr_Caches_Import(self):
        importlib.reload(cache)
        self.assertEqual(os.path.join(self.default_home, 'pokebase'),
                         cache.get_default_cache())
        self.assertEqual(os.path.join(self.default_home, 'pokebase'),
                         cache.CACHE_DIR)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'api.cache'),
                         cache.API_CACHE)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'sprite'),
                         cache.SPRITE_CACHE)

    def testAttr_Caches_Default(self):
        cache_dir, api_cache, sprite_cache = cache.set_cache()
        self.assertEqual(os.path.join(self.default_home, 'pokebase'),
                         cache_dir)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'api.cache'),
                         api_cache)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'sprite'),
                         sprite_cache)

    def testEnv_CacheDirNotFound(self):
        cache.set_cache('testing')
        os.rmdir(cache.SPRITE_CACHE)
        if os.path.exists(cache.API_CACHE): os.remove(cache.API_CACHE)
        os.rmdir(cache.CACHE_DIR)
        self.assertEqual(cache.set_cache(), 
                         (cache.CACHE_DIR, cache.API_CACHE, cache.SPRITE_CACHE))

    @given(new_path=characters(whitelist_categories=['Lu', 'Ll', 'Nd']))
    def testAttr_Caches_PathsChanged(self, new_path):
        cache.set_cache(new_path)
        self.assertEqual(os.path.abspath(new_path),
                         cache.CACHE_DIR)
        self.assertEqual(os.path.join(os.path.abspath(new_path), 'api.cache'),
                         cache.API_CACHE)
        self.assertEqual(os.path.join(os.path.abspath(new_path), 'sprite'),
                         cache.SPRITE_CACHE)
        os.rmdir(cache.SPRITE_CACHE)
        os.rmdir(cache.CACHE_DIR)
