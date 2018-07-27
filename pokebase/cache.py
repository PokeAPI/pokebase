# -*- coding: utf-8 -*-

import os
import shelve

from .common import cache_uri_build, sprite_filepath_build

# Cache locations will be set at the end of this file.
CACHE_DIR = None
API_CACHE = None
SPRITE_CACHE = None


def save(data, endpoint, resource_id=None, subresource=None):
    """Store the given data in the local API cache.

    :arg data:
    :arg endpoint:
    :arg resource_id:
    :arg subresource:
    :returns: None
    """
    if data == dict():    # No point in saving empty data.
        return None

    if not isinstance(data, (dict, list)):
        raise ValueError('Could not save non-dict data')

    uri = cache_uri_build(endpoint, resource_id, subresource)

    try:
        with shelve.open(API_CACHE) as cache:
            cache[uri] = data
    except OSError as error:
        if error.errno == 11:  # Cache open by another person/program
            # print('Cache unavailable, skipping save')
            pass
        else:
            raise error

    return None


def save_sprite(data, sprite_type, sprite_id, **kwargs):
    """Take image data and save it as a .png image in the local cache.

    :arg data:
    :arg sprite_type:
    :arg sprite_id:
    :returns: None
    """
    abs_path = data['path']

    # Make intermediate directories; this line removes the file+extension.
    dirs = abs_path.rpartition(os.path.sep)[0]
    safe_make_dirs(dirs)

    with open(abs_path, 'wb') as img_file:
        img_file.write(data['img_data'])

    return None


def load(endpoint, resource_id=None, subresource=None):
    """Load API data from the local cache.

    :arg endpoint:
    :arg resource_id:
    :arg subresource:
    :rasies KeyError: if the cache file is already opened OR if the 
       data requested is not in the cache
    :returns: the data stored in the cache
    :rtype: dict
    """
    uri = cache_uri_build(endpoint, resource_id, subresource)

    try:
        with shelve.open(API_CACHE) as cache:
            return cache[uri]
    except OSError as error:
        if error.errno == 11:
            # Cache open by another person/program
            # print('Cache unavailable, skipping load')
            raise KeyError('Cache could not be opened.')
        else:
            raise


def load_sprite(sprite_type, sprite_id, **kwargs):
    """Load a sprite and associated data from the local cache.

    :arg sprite_type:
    :arg sprite_id:
    :returns: the raw sprite data and the path to its correspoinding 
       image file on the disk
    :rtype: dict
    """
    abs_path = get_sprite_path(sprite_type, sprite_id, **kwargs)

    with open(abs_path, 'rb') as img_file:
        img_data = img_file.read()

    return dict(img_data=img_data, path=abs_path)


def safe_make_dirs(path, mode=0o777):
    """Create a leaf directory and all intermediate ones in a safe way.

    A wrapper to os.makedirs() that handles existing leaf directories while
    avoiding os.path.exists() race conditions.

    :arg path: relative or absolute directory tree to create
    :arg mode: directory permissions in octal
    :return: The newly-created path
    """
    try:
        os.makedirs(path, mode)
    except OSError as error:
        if error.errno != 17:  # File exists
            raise

    return path


def get_default_cache():
    """Get the default cache location.

    Adheres to the XDG Base Directory specification, as described in
    https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

    :return: the default cache directory absolute path
    :rtype: str
    """
    xdg_cache_home = os.environ.get('XDG_CACHE_HOME') or \
        os.path.join(os.path.expanduser('~'), '.cache')

    return os.path.join(xdg_cache_home, 'pokebase')


def get_sprite_path(sprite_type, sprite_id, **kwargs):
    """Build the absolute filepath to a sprite.

    :arg sprite_type:
    :arg sprite_id:
    :returns: the absolute path to the requested sprite.
    :rtype: str
    """
    rel_filepath = sprite_filepath_build(sprite_type, sprite_id, **kwargs)
    abs_path = os.path.join(SPRITE_CACHE, rel_filepath)

    return abs_path


def set_cache(new_path=None):
    """Change the cache location.

    *new_path* can be an absolute or relative path. If the directory 
    does not exist yet, this function will create it. If None it will 
    set the cache to the default cache directory.

    If you are going to change the cache directory, this function 
    should be called at the top of your script, before you make any 
    calls to the API. This is to avoid duplicate files and excess API
    calls.

    :arg new_path: relative or absolute path to the desired new cache
       directory
    :return: the new absoulte cache paths, for the cache root, the API
       cache, and the sprite cache root
    :rtype: tuple 
    """
    global CACHE_DIR, API_CACHE, SPRITE_CACHE

    if new_path is None:
        new_path = get_default_cache()

    CACHE_DIR = safe_make_dirs(os.path.abspath(new_path))
    API_CACHE = os.path.join(CACHE_DIR, 'api.cache')
    SPRITE_CACHE = safe_make_dirs(os.path.join(CACHE_DIR, 'sprite'))

    return CACHE_DIR, API_CACHE, SPRITE_CACHE


CACHE_DIR, API_CACHE, SPRITE_CACHE = set_cache()
