Examples
========

Here is a selection of possible ways to use ``pokebase`` to help you access 
PokéAPI. Obviously they can't *all* be listed, but if you think of another 
good example you would like to add yourself, submit a pull request with
your new example on GitHub. New examples are always welcome! 

Simple Usage
------------

Getting All Pokémon Names from a Generation
-------------------------------------------

.. literalinclude:: poke_names.py
   :linenos:

Finding Moves of a Certain Type
-------------------------------
A quick 'n' dirty method to do this is to get a list of every move, check its 
type, and then print it if the type matches. And this is exactly what I did 
when writing this example. But there's a better way (we'll get to that in a 
second).

.. literalinclude:: move_types.py
   :linenos:
   :lines: 1-10

But sometimes the API has done work for you already. Looking in the docs for
types, we see that each type resource has a ``moves`` method. Here's the 
better code.

.. literalinclude:: move_types.py
   :linenos:
   :lines: 1-3,12-

The first example is poor is because it calls the API signicantly more times 
(once for *every* move) than this example does (once for the type, and once 
for each move that we want). The more API calls you have, the slower your 
script runs.

Making a Type Chart
-------------------
