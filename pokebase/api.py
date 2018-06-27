# -*- coding: utf-8 -*-

from .cache import lookup_data, lookup_resource, lookup_sprite


def get_resource(resource):
    return lookup_resource(resource)


def get_data(resource, name_or_id):
    return lookup_data(resource, name_or_id)


def get_sprite(resource, name_or_id):
    return lookup_sprite(resource, name_or_id)
