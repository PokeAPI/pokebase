# README

pokebase is a simple but powerful Python interface to the [PokéAPI database](https://pokeapi.co/).

## Usage

```python
>>> import pokebase as pb
>>> chesto = pb.NamedAPIResource('berry', 'chesto')
>>> chesto.name
'chesto'
>>> chesto.natural_gift_type.name
'water'
>>> chesto = pb.berry('chesto')  # direct lookup.
>>> chesto.name
'chesto'
>>>
```

... And it's just that simple.

**Important**
 
The quick data lookup for a Pokémon type, is `pokebase.type_('type-name')`, not `pokebase.type('type-name')`. This is because of a naming conflict with the Python language.
