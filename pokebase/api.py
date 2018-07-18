# -*- coding: utf-8 -*-

import requests

from .common import BASE_URL, ENDPOINTS, api_url_build, sprite_url_build
from .cache import save, load, save_sprite, load_sprite, get_sprite_path


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


def get_data(endpoint, resource_id=None, force_lookup=False):

    if not force_lookup:
        try:
            data = load(endpoint, resource_id)
            return data
        except KeyError:
            pass

    data = _call_api(endpoint, resource_id)
    save(data, endpoint, resource_id)

    return data


def _call_sprite_api(sprite_type, sprite_id, **kwargs):

    url = sprite_url_build(sprite_type, sprite_id, **kwargs)

    response = requests.get(url)
    response.raise_for_status()

    return response.content


def get_sprite(sprite_type, sprite_id, **kwargs):

    if not kwargs.get('force_lookup', False):
        try:
            img_data = load_sprite(sprite_type, sprite_id, **kwargs)

            abs_path = get_sprite_path(sprite_type, sprite_id, **kwargs)
            data = {'img_data': img_data, 'path': abs_path}
            return data
        except FileNotFoundError:
            pass

    img_data = _call_sprite_api(sprite_type, sprite_id, **kwargs)
    save_sprite(img_data, sprite_type, sprite_id, **kwargs)

    abs_path = get_sprite_path(sprite_type, sprite_id, **kwargs)

    data = {'img_data': img_data, 'path': abs_path}

    return data
