# -*- coding: utf-8 -*-

import os

BASE_URL = 'http://pokeapi.co/api/v2'
SPRITE_URL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites'
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
SPRITE_EXT = 'png'


def validate(endpoint, resource_id=None):

    if endpoint not in ENDPOINTS:
        raise ValueError('Unknown API endpoint \'{}\''.format(endpoint))

    if (resource_id is not None and
            not isinstance(resource_id, int)):

        raise ValueError('Bad id \'{}\''.format(resource_id))

    return None


def api_url_build(endpoint, resource_id=None, subresource=None):

    validate(endpoint, resource_id)

    if resource_id is not None:
        if subresource is not None:
            return '/'.join([BASE_URL, endpoint, str(resource_id), subresource, ''])

        return '/'.join([BASE_URL, endpoint, str(resource_id), ''])

    return '/'.join([BASE_URL, endpoint, ''])


def cache_uri_build(endpoint, resource_id=None, subresource=None):

    validate(endpoint, resource_id)

    if resource_id is not None:
        if subresource is not None:
            return '/'.join([endpoint, str(resource_id), subresource, ''])

        return '/'.join([endpoint, str(resource_id), ''])

    return '/'.join([endpoint, ''])


def sprite_url_build(sprite_type, sprite_id, **kwargs):

    options = parse_sprite_options(sprite_type, **kwargs)

    filename = '.'.join([str(sprite_id), SPRITE_EXT])
    url = '/'.join([SPRITE_URL, sprite_type, *options, filename])

    return url


def sprite_filepath_build(sprite_type, sprite_id, **kwargs):
    """returns the filepath of the sprite *relative to SPRITE_CACHE*"""

    options = parse_sprite_options(sprite_type, **kwargs)

    filename = '.'.join([str(sprite_id), SPRITE_EXT])
    filepath = os.path.join(sprite_type, *options, filename)

    return filepath


def parse_sprite_options(sprite_type, **kwargs):
    options = []

    if sprite_type == 'pokemon':
        if kwargs.get('model', False):
            options.append('model')
        elif kwargs.get('other_sprites', False):
            options.append('other-sprites')
            if kwargs.get('official_artwork', False):
                options.append('official-artwork')
        else:
            if kwargs.get('back', False):
                options.append('back')
            if kwargs.get('shiny', False):
                options.append('shiny')
            if kwargs.get('female', False):
                options.append('female')
    elif sprite_type == 'items':
        if kwargs.get('berries', False):
            options.append('berries')
        elif kwargs.get('dream_world', False):
            options.append('dream-world')
        elif kwargs.get('gen3', False):
            options.append('gen3')
        elif kwargs.get('gen5', False):
            options.append('gen5')
        elif kwargs.get('underground', False):
            options.append('underground')

    return options
