# -*- coding: utf-8 -*-

import importlib
import shelve
import os
import os.path
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
    def testNormalParams(self, data, endpoint, resource_id):
        self.assertIsNone(cache.save(data, endpoint, resource_id))

    @given(data=text(),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testBadParam_data(self, data, endpoint, resource_id):
        with self.assertRaises(ValueError):
            cache.save(data, endpoint, resource_id)

    @given(data=dictionaries(text(), text()),
           endpoint=text(),
           resource_id=integers(min_value=1))
    def testBadParam_endpoint(self, data, endpoint, resource_id):
        assume(data != dict())
        with self.assertRaises(ValueError):
            cache.save(data, endpoint, resource_id)

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=text())
    def testBadParam_resource_id(self, data, endpoint, resource_id):
        assume(data != dict())
        with self.assertRaises(ValueError):
            cache.save(data, endpoint, resource_id)

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testCacheFileNotFound(self, data, endpoint, resource_id):
        assume(data != dict())
        os.remove(cache.API_CACHE)
        self.assertIsNone(cache.save(data, endpoint, resource_id))

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testCacheFileAlreadyOpen(self, data, endpoint, resource_id):
        cache_db = shelve.open(cache.API_CACHE)
        self.assertIsNone(cache.save(data, endpoint, resource_id))
        cache_db.close()

    def testCacheDirDeleted(self):
        pass


class TestFunction_load(unittest.TestCase):
    
    # cache.load(endpoint, resource_id=None)

    def setUp(self):
        cache.set_cache('testing')

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testExpectedParams(self, data, endpoint, resource_id):
        assume(data != dict())
        cache.save(data, endpoint, resource_id)
        self.assertEqual(data, cache.load(endpoint, resource_id))

    @given(endpoint=text(),
           resource_id=integers(min_value=1))
    def testBadParam_endpoint(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            cache.load(endpoint, resource_id)

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=text())
    def testBadParam_resource_id(self, endpoint, resource_id):
        with self.assertRaises(ValueError):
            cache.load(endpoint, resource_id)

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testCacheFileNotFound(self, endpoint, resource_id):
        os.remove(cache.API_CACHE)
        with self.assertRaises(KeyError):
            cache.load(endpoint, resource_id)

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testCacheFileAlreadyOpen(self, endpoint, resource_id):
        cache_db = shelve.open(cache.API_CACHE)
        with self.assertRaises(KeyError):
            cache.load(endpoint, resource_id)
        cache_db.close()

    def testCacheDirDeleted(self):
        pass

    @given(data=dictionaries(text(), text()),
           endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1))
    def testKeyNotInCache(self, data, endpoint, resource_id):

        with shelve.open(cache.API_CACHE) as c:
            key = cache.cache_uri_build(endpoint, resource_id)
            if key in c:
                del c[key]
        
        with self.assertRaises(KeyError):
            cache.load(endpoint, resource_id)


class TestFunction_set_cache(unittest.TestCase):
    
    # cache.set_cache(new_path=None)
    
    default_home = os.path.join(os.path.expanduser('~'), '.cache')

    def testCachePathsSetOnImport(self):
        importlib.reload(cache)
        self.assertEqual(os.path.join(self.default_home, 'pokebase'),
                         cache.get_default_cache())
        self.assertEqual(os.path.join(self.default_home, 'pokebase'),
                         cache.CACHE_DIR)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'api.cache'),
                         cache.API_CACHE)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'sprite'),
                         cache.SPRITE_CACHE)

    def testCacheDefaultPath(self):
        cache_dir, api_cache, sprite_cache = cache.set_cache()
        self.assertEqual(os.path.join(self.default_home, 'pokebase'),
                         cache_dir)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'api.cache'),
                         api_cache)
        self.assertEqual(os.path.join(self.default_home, 'pokebase', 'sprite'),
                         sprite_cache)

    def testCacheDirNotFound(self):
        os.rmdir(cache.SPRITE_CACHE)
        if os.path.exists(cache.API_CACHE): os.remove(cache.API_CACHE)
        os.rmdir(cache.CACHE_DIR)
        self.assertEqual(cache.set_cache(), 
                         (cache.CACHE_DIR, cache.API_CACHE, cache.SPRITE_CACHE))

    @given(new_path=characters(whitelist_categories=['Lu', 'Ll', 'Nd']))
    def testCachePathsChanged(self, new_path):
        cache.set_cache(new_path)
        self.assertEqual(os.path.abspath(new_path),
                         cache.CACHE_DIR)
        self.assertEqual(os.path.join(os.path.abspath(new_path), 'api.cache'),
                         cache.API_CACHE)
        self.assertEqual(os.path.join(os.path.abspath(new_path), 'sprite'),
                         cache.SPRITE_CACHE)
        os.rmdir(cache.SPRITE_CACHE)
        os.rmdir(cache.CACHE_DIR)
