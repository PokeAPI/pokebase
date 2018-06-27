# -*- coding: utf-8 -*-

import os
import json

import requests

from .common import BASE_URL, SPRITE_URL, RESOURCES

CACHE = None  # To be set after set_cache() definition
SPRITE_CACHE = None  # Ditto


def safe_make_dirs(path, mode=0o777):
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
    :return: str, str
    """
    global CACHE, SPRITE_CACHE

    if new_path is None:
        new_path = get_default_cache()

    CACHE = safe_make_dirs(os.path.abspath(new_path))
    SPRITE_CACHE = safe_make_dirs(os.path.join(CACHE, 'sprite'))

    return CACHE, SPRITE_CACHE


set_cache()


def lookup_data(sub_dir, name, force_reload=False):
    """Locates and saves a specific reference, and then returns the data.

    If the resource desired is already cached, this function will return the
    cached copy. However, data files can be forced to re-download using the
    force_reload parameter. Reference are saved to the user's home directory
    in a folder `~/.cache/pokebase`.

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
    in a folder `~/.cache/pokebase`.

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
        safe_make_dirs(name)
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

    Images will be caches in the directory ~/.cahce/pokebase/sprite and then
    named by id number.

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
        safe_make_dirs(resource)
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
