# -*- coding: utf-8 -*-

from .api import get_data, get_sprite
from .common import BASE_URL, api_url_build, sprite_url_build


def _make_obj(obj):
    """Takes an object and returns a corresponding API class.

    The names and values of the data will match exactly with those found
    in the online docs at https://pokeapi.co/docsv2/ . In some cases, the data
    may be of a standard type, such as an integer or string. For those cases,
    the input value is simply returned, unchanged.

    :param obj: the object to be converted
    :return either the same value, if it does not need to be converted, or a
    APIResource or APIMetadata instance, depending on the data inputted.
    """

    if isinstance(obj, dict):
        if 'url' in obj.keys():
            url = obj['url']
            id_ = int(url.split('/')[-2])      # ID of the data.
            endpoint = url.split('/')[-3]  # Where the data is located.
            return APIResource(endpoint, id_, lazy_load=True)

        return APIMetadata(obj)

    return obj


def name_id_convert(endpoint, name_or_id):

    if isinstance(name_or_id, int):
        id_ = name_or_id
        name = _convert_id_to_name(endpoint, id_)

    elif isinstance(name_or_id, str):
        name = name_or_id
        id_ = _convert_name_to_id(endpoint, name)

    else:
        raise ValueError('the name or id \'{}\' could not be converted'
                         .format(name_or_id))

    return name, id_


def _convert_id_to_name(endpoint, id_):
    resource_data = get_data(endpoint)['results']

    for resource in resource_data:
        if resource['url'].split('/')[-2] == str(id_):

            # Return the matching name, or None if it doesn't exsist.
            return resource.get('name', None)

    return None


def _convert_name_to_id(endpoint, name):

    resource_data = get_data(endpoint)['results']

    for resource in resource_data:
        if resource.get('name') == name:
            return int(resource.get('url').split('/')[-2])

    return None


class APIResource(object):
    """Core API class, used for accessing the bulk of the data.

    The class uses a modified __getattr__ function to serve the appropriate
    data, so lookup data via the `.` operator, and use the `PokeAPI docs
    <https://pokeapi.co/docsv2/>`_ or the builtin `dir` function to see the
    possible lookups.

    This class takes the complexity out of lots of similar classes for each
    different kind of data served by the API, all of which are very similar,
    but not identical.
    """

    def __init__(self, endpoint, name_or_id, lazy_load=False, force_lookup=False):

        name, id_ = name_id_convert(endpoint, name_or_id)
        url = api_url_build(endpoint, id_)

        self.__dict__.update({'name': name,
                              'endpoint': endpoint,
                              'id_': id_,
                              'url': url})

        self.__loaded = False
        self.__force_lookup = force_lookup

        if not lazy_load:
            self._load()
            self.__loaded = True

    def __getattr__(self, attr):
        """Modified method to auto-load the data when it is needed.

        If the data has not yet been looked up, it is loaded, and then checked
        for the requested attribute. If it is not found, AttributeError is
        raised.
        """

        if not self.__loaded:
            self._load()
            self.__loaded = True

            return self.__getattribute__(attr)

        else:
            raise AttributeError('{} object has no attribute {}'
                                 .format(type(self), attr))

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return '<{}-{}>'.format(self.endpoint, self.name)

    def _load(self):
        """Function to collect reference data and connect it to the instance as
         attributes.

         Internal function, does not usually need to be called by the user, as
         it is called automatically when an attribute is requested.

        :return None
        """

        data = get_data(self.endpoint, self.id_, force_lookup=self.__force_lookup)

        # Make our custom objects from the data.
        for key, val in data.items():

            if key == 'location_area_encounters' \
                    and self.endpoint == 'pokemon':

                params = val.split('/')[-3:]
                ep, id_, subr = params
                encounters = get_data(ep, int(id_), subr)
                data[key] = [_make_obj(enc) for enc in encounters]
                continue

            if isinstance(val, dict):
                data[key] = _make_obj(val)

            elif isinstance(val, list):
                data[key] = [_make_obj(i) for i in val]

        self.__dict__.update(data)

        return None


class APIResourceList(object):
    """Class for a data container.

    Used to access data corresponding to a category, rather than an individual
    reference. Ex. APIResourceList('berry') gives information about all
    berries, such as which ID's correspond to which berry names, and
    how many berries there are.

    You can iterate through all the names or all the urls, using the respective
    properties. You can also iterate on the object itself to run through the
    `dict`s with names and urls together, whatever floats your boat.
    """

    def __init__(self, endpoint, force_lookup=False):
        """Creates a new APIResourceList instance.

        :param name: the name of the resource to get (ex. 'berry' or 'move')
        """

        response = get_data(endpoint, force_lookup=force_lookup)

        self.name = endpoint
        self.__results = [i for i in response['results']]
        self.count = response['count']

    def __len__(self):
        return self.count

    def __iter__(self):
        return iter(self.__results)

    def __str__(self):
        return str(self.__results)

    @property
    def names(self):
        """Useful iterator for all the resource's names."""
        for result in self.__results:
            yield result.get('name', result['url'].split('/')[-2])

    @property
    def urls(self):
        """Useful iterator for all of the resource's urls."""
        for result in self.__results:
            yield result['url']


class APIMetadata(object):
    """Helper class for smaller references.

    This class emulates a dictionary, but attribute lookup is via the `.`
    operator, not indexing. (ex. instance.attr, not instance['attr']).

    Used for "Common Models" classes and APIResource helper classes.
    https://pokeapi.co/docsv2/#common-models
    """

    def __init__(self, data):

        for key, val in data.items():

            if isinstance(val, dict):
                data[key] = _make_obj(val)

            if isinstance(val, list):
                data[key] = [_make_obj(i) for i in val]

        self.__dict__.update(data)


class SpriteResource(object):

    def __init__(self, sprite_type, sprite_id, **kwargs):

        url = sprite_url_build(sprite_type, sprite_id, **kwargs)

        self.__dict__.update({'sprite_id': sprite_id,
                              'sprite_type': sprite_type,
                              'url': url})

        self.__loaded = False
        self.__force_lookup = kwargs.get('force_lookup', False)
        self.__orginal_kwargs = kwargs

        if not kwargs.get('lazy_load', False):
            self._load()
            self.__loaded = True

    def _load(self):

        data = get_sprite(self.sprite_type, self.sprite_id, **self.__orginal_kwargs)
        self.__dict__.update(data)

        return None

    def __getattr__(self, attr):
        """Modified method to auto-load the data when it is needed.

        If the data has not yet been looked up, it is loaded, and then checked
        for the requested attribute. If it is not found, AttributeError is
        raised.
        """

        if not self.__loaded:
            self._load()
            self.__loaded = True

            return self.__getattribute__(attr)

        else:
            raise AttributeError('{} object has no attribute {}'
                                 .format(type(self), attr))
