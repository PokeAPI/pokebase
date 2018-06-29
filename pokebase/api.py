# -*- coding: utf-8 -*-

import requests

from .common import BASE_URL, ENDPOINTS, api_url_build
from .cache import save, load


def _call_api(endpoint, resource_id=None):
    
    url = api_url_build(endpoint, resource_id)

    # Get a list of resources at the endpoint, if no resource_id is given.
    get_endpoint_list = resource_id is None

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if get_endpoint_list and data['count'] != len(data['results']):
        # We got a section of all results; we want ALL of them.
        items = data['count']
        num_items = {'limit': items}

        response = requests.get(url, params=num_items)
        response.raise_for_status()

        data = response.json()

    return data


def get_data(endpoint, resource_id=None):

    try:
        data = load(endpoint, resource_id)

    except KeyError:

        data = _call_api(endpoint, resource_id)

        save(data, endpoint, resource_id)

    return data
