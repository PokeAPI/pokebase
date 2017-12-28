# -*- coding: utf-8 -*-

"""pokebase/api.py - Main file for program interface with the API.

To access the data in the API, create a new `NamedAPIResource` instance, the
data for that resource can be accessed through that instance's attributes.

>>> import pokebase as pb
>>> squirtle = pb.NamedAPIResource('pokemon', 'squirtle')
>>> squirtle.weight
90
>>>

`pokebase.loaders` contains convenient shortcuts for requesting data without
having to specify the first parameter.

Data about each API resource will come in the form of basic Python types, like
`int` and `str`, as well as of APIMetadata type, which acts as a glorified
dictionary allowing attribute lookup via the dot operator, rather than normal
`dict` lookup with square brackets and a string.

By default, this wrapper will cache all API data in `~/.pokebase`. To change
this behavior, call `set_cache('/abs/or/rel/filepath')` before you make any API
calls.
"""

import json
import os

import requests


BASE_URL = 'http://pokeapi.co/api/v2'
SPRITE_URL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites'
CACHE = None  # To be set after set_cache() definition
SPRITE_CACHE = None  # Ditto
RESOURCES = ['ability', 'berry', 'berry-firmness', 'berry-flavor',
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


def safemakedirs(path, mode=0o777):
    """Create a leaf directory and all intermediate ones in a safe way.

    A wrapper to os.makedirs() that handles existing leaf directories while
    avoiding os.path.exists() race conditions.

    :param path: relative or absolute directory tree to create
    :param mode: directory permissions in octal
    :return: The newly-created path
    """
    try:
        os.makedirs(path, mode)
    except OSError as e:
        if e.errno != 17:  # File exists
            raise

    return path


def get_default_cache():
    """Get the default cache location.

    Adheres to the XDG Base Directory specification, as described in
    https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

    For backward-compatibility purposes, if the old location ~/.pokebase
    exists use it instead of the XDG standard

    :return: the default cache directory absolute path
    """

    old_cache = os.path.join(os.path.expanduser('~'), '.pokebase')

    if os.path.exists(old_cache):
        return old_cache

    xdg_cache_home = os.environ.get('XDG_CACHE_HOME') or \
                     os.path.join(os.path.expanduser('~'), '.cache')

    return os.path.join(xdg_cache_home, 'pokebase')


def set_cache(new_path=None):
    """Simple function to change the cache location.

    `new_path` can be an absolute or relative path. If the directory does not
    exist yet, this function will create it. If None it will set the cache to
    the default cache directory.

    If you are going to change the cache directory, this function should be
    called at the top of your script, before you make any calls to the API.
    This is to avoid duplicate files and excess API calls.

    :param new_path: relative or absolute path to the desired new cache
    directory
    :return: None
    """
    global CACHE, SPRITE_CACHE

    if new_path is None:
        new_path = get_default_cache()

    CACHE = safemakedirs(os.path.abspath(new_path))
    SPRITE_CACHE = safemakedirs(os.path.join(CACHE, 'sprite'))

    return CACHE, SPRITE_CACHE


set_cache()


def lookup_data(sub_dir, name, force_reload=False):
    """Locates and saves a specific reference, and then returns the data.

    If the resource desired is already cached, this function will return the
    cached copy. However, data files can be forced to re-download using the
    force_reload parameter. Reference are saved to the user's home directory
    in a folder `~/.pokebase`.

    :param sub_dir: what type of data is requested. (ex. 'move' or 'type')
    :param name: the name of the resource to lookup (ex. 'pound' or 'fire')
    :param force_reload: force the download, even if it the file exists already
    :return the data requested, as a Python `dict` instance
    """

    cwd = os.getcwd()
    os.chdir(CACHE)

    # Create the data directory if it does not exist.
    if not os.path.exists(sub_dir):
        lookup_resource(sub_dir)

    # Go to that directory.
    os.chdir(sub_dir)

    # Some resources don't have names, so use their ID.
    if isinstance(name, int):
        name = str(name)

    if os.path.exists('.'.join([name, 'json'])) and not force_reload:
        # If the resources wanted already exists, load it from disk.

        with open('.'.join([name, 'json']), 'r') as f:
            data = json.load(f)
    else:
        # If it doesn't exist, go download and save the resources.
        r = requests.get('/'.join([BASE_URL, sub_dir, name]))
        r.raise_for_status()
        data = json.loads(r.text)
        with open('.'.join([name, 'json']), 'w') as f:
            json.dump(data, f, indent=2)

    os.chdir(cwd)  # Return to original working directory.
    return data


def lookup_resource(name, force_reload=False):
    """Returns a resource with all of the data references in the category.

    If the resource desired is already cached, this function will return the
    cached copy. However, data files can be forced to re-download using the
    force_reload parameter. Reference are saved to the user's home directory
    in a folder `~/.pokebase`.

    :param name: which resource to download (ex. 'ability' or 'berry')
    :param force_reload: force the download, even if it the file exists already
    :return Python dict with the data this resource contains
    """

    if name not in RESOURCES:
        raise ValueError('resource not found ({}), check spelling'
                         .format(name))

    cwd = os.getcwd()
    os.chdir(CACHE)

    if os.path.exists(name) and not force_reload:
        os.chdir(name)

        with open('resource.json', 'r') as f:
            resource = json.load(f)

    else:
        os.mkdir(name)
        os.chdir(name)

        url = '/'.join([BASE_URL, name])
        r = requests.get(url)
        r.raise_for_status()
        resource = json.loads(r.text)

        if resource['count'] != len(resource['results']):
            # We got multiple pages of results; we want ALL of them.
            items = resource['count']
            url = '/'.join([BASE_URL, name, '?limit={}'.format(items)])

            r = requests.get(url)
            r.raise_for_status()
            resource = json.loads(r.text)

        with open('resource.json', 'w') as f:
            json.dump(resource, f, indent=2)

    os.chdir(cwd)
    return resource


def lookup_sprite(resource, filename, force_reload=False):
    """Helper function to locate and also download sprites onto the computer.

    Images will be caches in the directory ~/.pokebase/sprite and then named by
    id number.

    :param resource: which type of sprite, currently, 'pokemon' is the only
        valid option.
    :param filename: id + .png extension of the sprite online.
    :param force_reload: whether or not to force-download the image even if it
        has already been downloaded.
    :return: absolute file path to the sprite on the computer.
    """

    cwd = os.getcwd()
    os.chdir(SPRITE_CACHE)

    if not os.path.exists(resource):   # Make the cache if it doesn't exist.
        os.mkdir(resource)
    os.chdir(resource)

    if not os.path.exists(filename) or force_reload:
        # Download the sprite, if needed.
        url = '/'.join([SPRITE_URL, resource, filename])

        r = requests.get(url)
        r.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in r.iter_content(1000000):
                f.write(chunk)

    # Determine the file path.
    file_path = os.path.abspath(filename)

    os.chdir(cwd)  # Working directory not affected.
    return file_path


def make_obj(d):
    """Takes a dictionary and returns a NamedAPIResource or APIMetadata.

    The names and values of the data will match exactly with those found
    in the online docs at https://pokeapi.co/docsv2/ . In some cases, the data
    may be of a standard type, such as an integer or string. For those cases,
    the input value is simply returned, unchanged.

    :param d: the dictionary to be converted
    :return either the same value, if it does not need to be converted, or a
    NamedAPIResource or APIMetadata instance, depending on the data inputted.
    """

    if isinstance(d, dict):
        if 'url' in d.keys():
            url = d['url']
            name = url.split('/')[-2]      # Name of the data.
            location = url.split('/')[-3]  # Where the data is located.
            return NamedAPIResource(location, name, False)
        else:
            return APIMetadata(d)
    else:
        return d


class NamedAPIResource(object):
    """Core API class, used for accessing the bulk of the data.

    The class uses a modified __getattr__ function to serve the appropriate
    data, so lookup data via the `.` operator, and use the `PokeAPI docs
    <https://pokeapi.co/docsv2/>`_ or the builtin `dir` function to see the
    possible lookups.

    This class takes the complexity out of lots of similar classes for each
    different kind of data served by the API, all of which are very similar,
    but not identical
    """

    def __init__(self, resource, name, lookup=True):
        """Returns a new NamedAPIResource object.

        Specify lookup=False to conserve calls to the API and speed up your
        program. This feature is used internally, but you will usually want it
        left True. Leaving it False causes the object to act as a placeholder
        for the data, until the data is called by the user.

        :param str resource: What kind of data you want (ex. 'move' or 'type')
        :param str name: What the resource is called (ex. 'pound' or 'fire')
        :param bool lookup: Whether or not to gather all the data on
        construction
        """

        r = resource.replace(' ', '-').lower()
        n = APIResourceList(r).id_to_name(name)

        self.__data = {'type': r, 'name': n,
                       'url': '/'.join([BASE_URL, r, n])}

        self.resource_type = r

        if lookup:
            self.load()
            self.__is_loaded = True
        else:
            self.__is_loaded = False

    def __getattr__(self, attr):
        """Modified method to auto-load the data when it is needed.

        If the data has not yet been looked up, it is loaded, and then checked
        for the requested attribute. If it is not found, AttributeError is
        raised.
        """

        if not self.__is_loaded:
            self.load()
            self.__is_loaded = True

            return self.__getattribute__(attr)

        else:
            raise AttributeError('{} object has no attribute {}'
                                 .format(type(self), attr))

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return '<{} - {}>'.format(self.resource_type, self.name)

    def load(self):
        """Function to collect reference data and connect it to the instance as
         attributes.

         Internal function, does not usually need to be called by the user, as
         it is called automatically when an attribute is requested.

        :return None
        """

        self.__data.update(lookup_data(self.__data['type'],
                                       self.__data['name']))

        for k, v in self.__data.items():

            if isinstance(v, dict):
                self.__setattr__(k, make_obj(v))

            elif isinstance(v, list):
                self.__setattr__(k, [make_obj(i) for i in v])
            else:
                self.__setattr__(k, v)

        self.__is_loaded = True

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

    def __init__(self, name):
        """Creates a new APIResourceList instance.

        :param name: the name of the resource to get (ex. 'berry' or 'move')
        """

        response = lookup_resource(name)

        self.name = name
        self.__results = [i for i in response['results']]
        self.count = response['count']

    def __len__(self):
        return self.count

    def __iter__(self):
        return iter(self.__results)

    def __str__(self):
        return str(self.__results)

    def id_to_name(self, id_):
        """Attempts to convert a given id_ into its corresponding name.

        If no name exists, the function will return `str(id_)`
        :param id_:
        :return:
        """

        if self.name == 'location-area':
            # location-areas can't be looked up by name.
            return str(id_)

        for res in self.__results:
            if res.get('name', res['url'].split('/')[-2]) == id_:
                # Runs when the end of the url is equal to `id_`.
                return str(id_)

            if res['url'].split('/')[-2] == str(id_):
                # Runs when `id_` is found in a url that has a matching name.
                return res.get('name', res['url'].split('/')[-2])

        else:
            raise ValueError('resource not found ({}), check spelling'
                             .format(id_))

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

    Used for "Common Models" classes and NamedAPIResource helper classes.
    https://pokeapi.co/docsv2/#common-models
    """

    def __init__(self, data):
        self.__data = data

        for k, v in self.__data.items():

            if isinstance(v, dict):
                self.__setattr__(k, make_obj(v))
            else:
                self.__setattr__(k, v)

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return self.__str__()


class SpriteResource(object):
    """Class for downloading sprites to your computer and then locating them.

    The only notable attribute of this class is a str with the absolute path to
    the sprite. This is designed as such so that you can load the image in
    whatever image class your specific application requires. The path can be
    found in the `path` attribute. No surprises.

    """

    def __init__(self, resource, id_, lookup=False):
        """Constructs a SpriteResource object.

        :param resource: which type of sprite, currently, 'pokemon' is the only
            valid option.
        :param id_: id of the pokemon to download.
        :param lookup: whether or not to retrieve the image immediately.
        """

        r = resource.replace(' ', '-').lower()
        filename = '.'.join([str(id_), 'png'])

        self.__data = {'type': r, 'path': filename,
                       'url': '/'.join([SPRITE_URL, r, filename])}

        if lookup:
            self.load()
            self.__is_loaded = True
        else:
            self.__is_loaded = False

    def __getattr__(self, attr):
        """Modified method to auto-load the data when it is needed.

        If the sprite has not yet been downloaded, it is downloaded.
        If the requested attribute is not found, AttributeError is
        raised.
        """

        if not self.__is_loaded:
            self.load()
            self.__is_loaded = True

            return self.__getattribute__(attr)

        else:
            raise AttributeError('{} object has no attribute {}'
                                 .format(type(self), attr))

    def load(self):
        """Downloads the sprite from the internet."""
        path = lookup_sprite(self.__data['type'], self.__data['path'])

        self.__setattr__('path', path)

        return None
