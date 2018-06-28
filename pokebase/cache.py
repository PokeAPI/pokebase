# -*- coding: utf-8 -*-

import os
import shelve

import requests

from .common import BASE_URL, SPRITE_URL, RESOURCES

# Cache locations will be set at the end of this file.
CACHE_DIR = None
API_CACHE = None
SPRITE_CACHE = None


def save(data, url):

    with shelve.open(API_CACHE) as cache:
        cache[url] = data


def load(url):

    with shelve.open(API_CACHE) as cache:
        return cache[url]


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
    global CACHE_DIR, API_CACHE, SPRITE_CACHE

    if new_path is None:
        new_path = get_default_cache()

    CACHE_DIR = safe_make_dirs(os.path.abspath(new_path))
    API_CACHE = os.path.join(CACHE_DIR, 'api.cache')
    SPRITE_CACHE = safe_make_dirs(os.path.join(CACHE_DIR, 'sprite'))

    return CACHE_DIR, API_CACHE, SPRITE_CACHE

set_cache()
