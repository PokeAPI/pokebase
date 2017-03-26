# README

pokebase.py is a simple but powerful Python interface to the [PokeAPI database](https://pokeapi.co/).

## Usage

```python
>>> import pokebase as pb
>>> chesto = pb.NamedAPIResource('berry', 'chesto')
>>> chesto.name
'chesto'
>>> chesto.natural_gift_type.name
'water'
>>> 
```
... And it's just that simple.
