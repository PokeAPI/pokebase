# -*- coding: utf-8 -*-

BASE_URL = 'http://pokeapi.co/api/v2'
ENDPOINTS = ['ability', 'berry', 'berry-firmness', 'berry-flavor',
             'characteristic', 'contest-effect', 'contest-type', 'egg-group',
             'encounter-condition', 'encounter-condition-value',
             'encounter-method', 'evolution-chain', 'evolution-trigger',
             'gender', 'generation', 'growth-rate', 'item', 'item-attribute',
             'item-category', 'item-fling-effect', 'item-pocket', 'language',
             'location', 'location-area', 'machine', 'move', 'move-ailment',
             'move-battle-style', 'move-category', 'move-damage-class',
             'move-learn-method', 'move-target', 'nature', 'pal-park-area',
             'pokeathlon-stat', 'pokedex', 'pokemon', 'pokemon-color',
             'pokemon-form', 'pokemon-habitat', 'pokemon-shape',
             'pokemon-species', 'region', 'stat', 'super-contest-effect',
             'type', 'version', 'version-group']


def validate(endpoint, resource_id=None):

    if endpoint not in ENDPOINTS:
        raise ValueError('Unknown API endpoint \'{}\''.format(endpoint))

    if (resource_id is not None and
            not isinstance(resource_id, int)):

        raise ValueError('Bad id \'{}\''.format(resource_id))

    return None


def api_url_build(endpoint, resource_id=None):

    validate(endpoint, resource_id)

    url = '/'.join([BASE_URL, endpoint])

    if resource_id is not None:
        url = '/'.join([url, str(resource_id)])

    return url


def cache_uri_build(endpoint, resource_id):

    validate(endpoint, resource_id)

    if resource_id is not None:
        return '/'.join([endpoint, str(resource_id)])

    return endpoint
