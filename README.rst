======
README
======

|travis| |pypi|

pokebase is a simple but powerful Python interface to the
`PokéAPI database <https://pokeapi.co/>`_

=========
IMPORTANT
=========
pokebase is under heavy construction right now, in order to clean up the code
and make it easier to maintain. I have also dropped support for Python 2.7, *for
the time being*. Hopefully this can be added in later. I recommend you continue using
version 1.2.0, download via ``pip``. Once I deem these new changes stable, I'll do another
PyPI release (with fancy new ``shelve`` caching!)

Planned To-do's for the current construction:

 * APISubresource access
 * complete rewrite of the docstrings, and hosting on `readthdocs.io <https://readthedocs.org/>`_
 * Python 2.7 support

Installation
============

``pip install pokebase``

It can't get much easier than that.

Usage
=====

>>> import pokebase as pb
>>> chesto = pb.APIResource('berry', 'chesto')
>>> chesto.name
'chesto'
>>> chesto.natural_gift_type.name
'water'
>>> charmander = pb.pokemon('charmander')  # Quick lookup.
>>> charmander.height
6
>>> # Now with sprites! (again!)
>>> s1 = pb.SpriteResource('pokemon', 17)
<pokebase.interface.SpriteResource object at 0x7f2f15660860>
>>> s1.url
'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png'
>>> s2 = pb.SpriteResource('pokemon', 1, other_sprites=True, official_artwork=True)
>>> s2.path
'/home/user/.cache/pokebase/sprite/pokemon/other-sprites/official-artwork/1.png'
>>> s3 = pb.SpriteResource('pokemon', 3, female=True, back=True)
>>> s3.img_data
b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 ... \xca^\x7f\xbbd*\x00\x00\x00\x00IEND\xaeB`\x82'


... And it's just that simple.

Version Support
===============

pokebase currently (officially) supports Python 3.6

Nomenclature
============

 * an ``endpoint`` is the results of an API call like ``http://pokeapi.co/api/v2/berry`` or ``http://pokeapi.co/api/v2/move``
 * a ``resource`` is the actual data, from a call to ``http://pokeapi.co/api/v2/pokemon/1``

Testing
=======

Python unittests are in a separate ``tests`` directory, and can be run via
``python -m tests``.


Notes to the developer using this module
----------------------------------------

The quick data lookup for a Pokémon type, is ``pokebase.type_('type-name')``,
not ``pokebase.type('type-name')``. This is because of a naming conflict with
the built-in ``type`` function, were you to ``from pokebase import *``.

When changing the cache, avoid importing the cache constants directly. You should only
import them with the whole cache module. If you do not do this, calling ``set_cache``
will not change your local copy of the variable.

NOT THIS!

>>> from pokebase.cache import API_CACHE

Do this :)

>>> from pokebase import cache
>>> cache.API_CACHE

.. |travis| image:: https://travis-ci.org/GregHilmes/pokebase.svg?branch=master
   :target: https://travis-ci.org/GregHilmes/pokebase

.. |pypi| image:: https://img.shields.io/badge/pypi-1.2.0-blue.svg
   :target: https://pypi.python.org/pypi/pokebase
