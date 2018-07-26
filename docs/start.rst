Getting Started
===============

Installation
------------

.. code-block:: bash
   
   pip install pokebase

Alternatively, the source can be found on GitHub


Importing
---------

For most use cases,
::

   import pokebase

will be sufficient. Or, to save a few characters:
::

   import pokebase as pb

This will include the core wrapper classes, as well as the loaders functions.

.. note:: If you plan to change the cache location, avoid importing the cache constants directly.
   You should only import them with the whole cache module. If you do not do this, calling :meth:`set_cache`
   will not change your local copy of the variable.

   Bad!

   >>> from pokebase.cache import API_CACHE

   Good!

   >>> from pokebase import cache
   >>> cache.API_CACHE
