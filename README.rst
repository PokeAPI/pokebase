======
README
======

|travis| |pypi|

pokebase is a simple but powerful Python interface to the
`PokéAPI database <https://pokeapi.co/>`_

Installation
============

``pip install pokebase``

It can't get much easier than that.

Usage
=====

>>> import pokebase as pb
>>> chesto = pb.NamedAPIResource('berry', 'chesto')
>>> chesto.name
'chesto'
>>> chesto.natural_gift_type.name
'water'
>>> charmander = pb.pokemon('charmander')  # Quick lookup.
>>> charmander.height
6

>>> bulba = pb.pokemon_sprite(1)           # And sprites too!
>>> bulba.path
'/home/user/.pokebase/sprite/pokemon/1.png'
>>>


... And it's just that simple.

Version Support
===============

pokebase currently (officially) supports Python 2.7 and 3.6 versions.

Testing
=======

Python unittests are in a separate ``tests`` directory, and can be run via
``python -m tests.test_pokebase``.


Important
---------

The quick data lookup for a Pokémon type, is ``pokebase.type_('type-name')``,
not ``pokebase.type('type-name')``. This is because of a naming conflict with
the built-in ``type`` function.

.. |travis| image:: https://travis-ci.org/GregHilmes/pokebase.svg?branch=master
   :target: https://travis-ci.org/GregHilmes/pokebase

.. |pypi| image:: https://img.shields.io/badge/pypi-1.2.0-blue.svg
   :target: https://pypi.python.org/pypi/pokebase
