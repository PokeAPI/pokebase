# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from hypothesis import given
from hypothesis.strategies import dictionaries, text, sampled_from, integers, lists

from pokebase import interface
from pokebase.cache import set_cache
from pokebase.common import ENDPOINTS


class TestFunction__make_obj(unittest.TestCase):

    # _make_obj(obj)

    def setUp(self):
        set_cache('testing')

    @given(obj=dictionaries(text(), text()))
    def testArg_obj_Dictionary(self, obj):
        self.assertIsInstance(interface._make_obj(obj), interface.APIMetadata)

    @given(endpoint=sampled_from(ENDPOINTS),
           resource_id=integers(min_value=1),
           obj=dictionaries(text(), text()))
    @patch('pokebase.interface.get_data')
    def testArg_obj_DictionaryWithUrl(self, mock_get_data, endpoint, resource_id, obj):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, resource_id)}]}

        obj['url'] = 'http://base.url/{}/{}/'.format(endpoint, resource_id)
        self.assertIsInstance(interface._make_obj(obj), interface.APIResource)

    @given(obj=lists(elements=text()))
    def testArg_obj_List(self, obj):
        self.assertEqual(obj, interface._make_obj(obj))

    @given(obj=text())
    def testArg_obj_Str(self, obj):
        self.assertEqual(obj, interface._make_obj(obj))


class TestFunction__convert_id_to_name(unittest.TestCase):
    
    # _convert_id_to_name(endpoint, id_)

    def setUp(self):
        set_cache('testing')

    @given(name=text(),
           endpoint=sampled_from(ENDPOINTS),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testArgs(self, mock_get_data, name, endpoint, id_):
        
        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]}

        self.assertEqual(name, interface._convert_id_to_name(endpoint, id_))

    @given(endpoint=sampled_from(ENDPOINTS),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testEnv_NotNamedResource(self, mock_get_data, endpoint, id_):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_)}]}

        self.assertIsNone(interface._convert_id_to_name(endpoint, id_))

    @given(endpoint=text(),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testArg_endpoint_Text(self, mock_get_data, endpoint, id_):

        mock_get_data.side_effect = ValueError()
        
        with self.assertRaises(ValueError):
            interface._convert_id_to_name(endpoint, id_)


class TestFunction__convert_name_to_id(unittest.TestCase):
    
    # _convert_name_to_id(endpoint, name)
    @given(id_=integers(min_value=1),
           endpoint=sampled_from(ENDPOINTS),
           name=text())
    @patch('pokebase.interface.get_data')
    def testArgs(self, mock_get_data, id_, endpoint, name):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]}

        self.assertEqual(id_, interface._convert_name_to_id(endpoint, name))

    @given(endpoint=text(),
           name=text())
    @patch('pokebase.interface.get_data')
    def testArg_endpoint_Text(self, mock_get_data, endpoint, name):

        mock_get_data.side_effect = ValueError()
        
        with self.assertRaises(ValueError):
            interface._convert_id_to_name(endpoint, name)


class TestFunction_name_id_convert(unittest.TestCase):

    # name_id_convert(endpont, name_or_id)

    @given(name=text(),
           endpoint=sampled_from(ENDPOINTS),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testArgs_WithID(self, mock_get_data, name, endpoint, id_):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]}

        self.assertEqual((name, id_), interface.name_id_convert(endpoint, id_))

    @given(id_=integers(min_value=1),
           endpoint=sampled_from(ENDPOINTS),
           name=text())
    @patch('pokebase.interface.get_data')
    def testArgs_WithName(self, mock_get_data, id_, endpoint, name):
        
        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]}

        self.assertEqual((name, id_), interface.name_id_convert(endpoint, id_))

    @given(endpoint=text(),
           name=text())
    @patch('pokebase.interface.get_data')
    def testArg_endpoint_Text(self, mock_get_data, endpoint, name):

        mock_get_data.side_effect = ValueError()
        
        with self.assertRaises(ValueError):
            interface.name_id_convert(endpoint, name)


class TestClass_APIResource(unittest.TestCase):
    
    # APIResource(endpoint, name_or_id, lazy_load=True)

    def setUp(self):
        set_cache('testing')

    @given(id_=integers(min_value=1),
           endpoint=sampled_from(ENDPOINTS),
           name=text())
    @patch('pokebase.interface.get_data')
    def testArgs_WithNameWithLazyLoad(self, mock_get_data, id_, endpoint, name):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]}

        self.assertIsInstance(interface.APIResource(endpoint, name), 
                              interface.APIResource)

    @given(name=text(),
           endpoint=sampled_from(ENDPOINTS),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testArgs_WithIDWithLazyLoad(self, mock_get_data, name, endpoint, id_):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]}

        self.assertIsInstance(interface.APIResource(endpoint, id_), 
                              interface.APIResource)

    @given(id_=integers(min_value=1),
           endpoint=sampled_from(ENDPOINTS),
           name=text())
    @patch('pokebase.interface.get_data')
    def testAttrs_WithNameWithoutLazyLoad(self, mock_get_data, id_, endpoint, name):

        mock_get_data.side_effect = [{'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]},
                                     {'simple_attr': 10, 'list_attr': [{'name': 'mocked name'}]}]

        sample = interface.APIResource(endpoint, name, lazy_load=False)

        self.assertEqual(sample.simple_attr, 10)
        self.assertIsInstance(sample.list_attr, list)
        self.assertIsInstance(sample.list_attr[0], interface.APIMetadata)

    @given(name=text(),
           endpoint=sampled_from(ENDPOINTS),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testAttrs_WithIDWithoutLazyLoad(self, mock_get_data, name, endpoint, id_):

        mock_get_data.side_effect = [{'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]},
                                     {'simple_attr': 10, 'list_attr': [{'name': 'mocked name'}], 'complex_attr': {'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, 10)}},
                                     {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name + '2'}]}]

        sample = interface.APIResource(endpoint, id_, lazy_load=False)

        self.assertEqual(sample.simple_attr, 10)
        self.assertIsInstance(sample.list_attr, list)
        self.assertIsInstance(sample.list_attr[0], interface.APIMetadata)
        self.assertIsInstance(sample.complex_attr, interface.APIResource)

    @given(name=text(),
           endpoint=sampled_from(ENDPOINTS),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testAttrs_WithLazyLoad(self, mock_get_data, name, endpoint, id_):
        mock_get_data.side_effect = [{'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_), 'name': name}]},
                                     {'simple_attr': 10, 'list_attr': [{'name': 'mocked name'}]}]

        sample = interface.APIResource(endpoint, id_, lazy_load=True)
        lazy_len = len(dir(sample))
        sample._load()
        loaded_len = len(dir(sample))

        self.assertGreater(loaded_len, lazy_len)

    @given(endpoint=text(),
           id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testArg_endpoint_Text(self, mock_get_data, endpoint, id_):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(endpoint, id_)}]}

        with self.assertRaises(ValueError):
            interface.APIResource(endpoint, id_)

    @given(id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def testHasLocationAreaEncounters(self, mock_get_data, id_):

        mock_get_data.side_effect = [{'count': 1, 'results': [{'url': 'mocked.url/api/v2/pokemon/{}/'.format(id_), 'name': 'mocked name'}]},
                                     {'location_area_encounters': '/api/v2/pokemon/{}/encounters'.format(id_)},
                                     [{'version_details': [], 'location_area': {'url': 'mocked.url/api/v2/location-area/1/', 'name': 'mocked location_area'}}],
                                     {'count': 1, 'results': [{'url': 'mocked.url/api/v2/location-area/1/', 'name': 'mocked name'}]}]
        pkmn = interface.APIResource('pokemon', id_)
        # Should be list or empty list
        self.assertIsInstance(pkmn.location_area_encounters, list)
        # would be str if it was not handled
        self.assertNotIsInstance(pkmn.location_area_encounters, str)


class TestClass_APIResourceList(unittest.TestCase):
    
    @given(endpoint=sampled_from(ENDPOINTS))
    @patch('pokebase.interface.get_data')
    def testArgs(self, mock_get_data, endpoint):

        mock_get_data.return_value = {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/1/'.format(endpoint)}]}

        self.assertIsInstance(interface.APIResourceList(endpoint),
                              interface.APIResourceList)
    
    @given(endpoint=text())
    @patch('pokebase.interface.get_data')
    def testArg_endpoint_Text(self, mock_get_data, endpoint):

        mock_get_data.side_effect = ValueError()

        with self.assertRaises(ValueError):
            interface.APIResourceList(endpoint)


class TestClass_APIMetadata(unittest.TestCase):

    @given(data=dictionaries(text(), text()))
    def testArgs(self, data):
        self.assertIsInstance(interface.APIMetadata(data),
                              interface.APIMetadata)
