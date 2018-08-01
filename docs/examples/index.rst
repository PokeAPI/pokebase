Examples
========

Here is a selection of possible ways to use ``pokebase`` to help you access 
PokéAPI. Obviously they can't *all* be listed, but if you think of another 
good example you would like to add yourself, submit a pull request with
your new example on GitHub. New examples are always welcome! 

Simple Usage
------------
The best way to get familiar with pokebase/PokéAPI is to open up a session in
the Python interactive interpreter!

>>> import pokebase as pb
>>> bulba = pb.pokemon(1)
>>> for type_slot in bulba.types:
...     print('{}: {}'.format(type_slot.slot, type_slot.type.name.title()))
...
1: Grass
2: Poison
>>> bulba.base_experience
64
>>> pound = pb.move('pound')
>>> pound.accuracy
100
>>> pound.type.name.title()
'Normal'

Check out the PokéAPI docs for even more use-cases, information, and data 
examples.

Getting All Pokémon Names from a Generation
-------------------------------------------

In this example, we want to print out the name of every Pokémon that was
introduced in a given generation of Pokémon games.

.. literalinclude:: poke_names.py
   :linenos:

Finding Moves of a Certain Type
-------------------------------
A quick 'n' dirty method to do this is to get a list of every move, check its 
type, and then print it if the type matches our searched type. And this is 
exactly what I did when writing this example. But there's a better way (we'll
get to that in a second). Here's the bad example:

.. literalinclude:: move_types.py
   :linenos:
   :lines: 1-17

But sometimes the API has done work for you already. Looking in the docs for
types, we see that each type resource has a ``moves`` method. Here's the 
better code.

.. literalinclude:: move_types.py
   :linenos:
   :lines: 1-4,17-

The first example is poor is because it calls the API signicantly more times 
than this second example does (once for *every* move, as opposed to only 
calling the API for each move in the type's list of moves). The second method
guarantees that whenever we call the API for a move, we know it has the type
that we're looking for. The more API calls you have, the slower your script 
runs.

Making a Type Chart
-------------------

For this example, we want to write a function to find the type multiplier
when any one Pokémon type attacks any other. This could be useful if you
wanted to make a move damage calculator or a game to test your knowledge of 
the Pokémon type chart.

.. literalinclude:: type_chart.py
   :linenos:
