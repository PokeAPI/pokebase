# -*- coding: utf-8 -*-

import requests

from .common import BASE_URL, RESOURCES
from .cache import save, load


def _download_resource(url):

    response = requests.get(url)
    response.raise_for_status()

    resource = response.json()

    if resource['count'] != len(resource['results']):
        # We got a section of all results; we want ALL of them.
        items = resource['count']
        num_items = {'limit': items}

        response = requests.get(url, params=num_items)
        response.raise_for_status()

        resource = response.json()

    return resource


def _download_data(url):
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return data


def get_resource(resource):

    if resource not in RESOURCES:
        raise ValueError('resource not found ({})'.format(resource))

    url = '/'.join([BASE_URL, resource])

    try:
        # Get data from cache.
        data = load(url)

    except KeyError:
        # Data not found in the cache.
        # Download data from the internet then.
        data = _download_resource(url)

        # save it to the cache for later.
        save(data, url)

    return data


def get_data(resource, id_):

    if not isinstance(id_, int):
        raise ValueError('only lookup by id is supported')

    url = '/'.join([BASE_URL, resource, str(id_)])

    try:
        data = load(url)

    except KeyError:

        data = _download_data(url)

        save(data, url)

    return data
