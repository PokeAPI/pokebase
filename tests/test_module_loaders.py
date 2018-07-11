# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from hypothesis import given
from hypothesis.strategies import integers

from pokebase import loaders, APIResource
from pokebase.common import ENDPOINTS


def builder(func, func_name):

    @given(id_=integers(min_value=1))
    @patch('pokebase.interface.get_data')
    def test(self, mock_get_data, id_):
        mock_get_data.side_effect = [{'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(func_name, id_)}]},
                                {'simple_attr': 10, 'list_attr': [{'name': 'mocked name'}], 'complex_attr': {'url': 'mocked.url/api/v2/{}/{}/'.format(func_name, 10)}},
                                {'count': 1, 'results': [{'url': 'mocked.url/api/v2/{}/{}/'.format(func_name, id_)}]}]
        self.assertIsInstance(func(id_), APIResource)

    return test


class TestFunctions_loaders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        for endpoint in ENDPOINTS:
            if endpoint in ['type']:
                # special cases, need trailing underscore
                func_name = ''.join([endpoint.replace('-', '_'), '_'])
            else:
                func_name = endpoint.replace('-', '_')

            func = getattr(loaders, func_name)

            setattr(cls, 'testLoader_{}'.format(func_name), builder(func, endpoint))

TestFunctions_loaders.setUpClass()
