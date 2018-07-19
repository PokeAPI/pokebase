# -*- coding: utf-8 -*-

from .interface import APIResource, SpriteResource


def berry(id_or_name, **kwargs):
    """Quick berry lookup.

    See https://pokeapi.co/docsv2/#berries for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('berry', id_or_name, **kwargs)

def berry_firmness(id_or_name, **kwargs):
    """Quick berry-firmness lookup.

    See https://pokeapi.co/docsv2/#berry-firmnesses for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('berry-firmness', id_or_name, **kwargs)

def berry_flavor(id_or_name, **kwargs):
    """Quick berry-flavor lookup.

    See https://pokeapi.co/docsv2/#berry-flavors for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('berry-flavor', id_or_name, **kwargs)

def contest_type(id_or_name, **kwargs):
    """Quick contest-type lookup.

    See https://pokeapi.co/docsv2/#contest-types for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('contest-type', id_or_name, **kwargs)

def contest_effect(id_, **kwargs):
    """Quick contest-effect lookup.

    See https://pokeapi.co/docsv2/#contest-effects for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('contest-effect', id_, **kwargs)

def super_contest_effect(id_, **kwargs):
    """Quick super-contest-effect lookup.

    See https://pokeapi.co/docsv2/#super-contest-effects for attributes and
    more detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('super-contest-effect', id_, **kwargs)

def encounter_method(id_or_name, **kwargs):
    """Quick encounter-method lookup.

    See https://pokeapi.co/docsv2/#encounter-methods for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('encounter-method', id_or_name, **kwargs)

def encounter_condition(id_or_name, **kwargs):
    """Quick encounter-condition lookup.

    See https://pokeapi.co/docsv2/#encounter-conditions for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('encounter-condition', id_or_name, **kwargs)

def encounter_condition_value(id_or_name, **kwargs):
    """Quick encounter-condition-value lookup.

    See https://pokeapi.co/docsv2/#encounter-condition-values for attributes
    and more detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('encounter-condition-value', id_or_name, **kwargs)

def evolution_chain(id_, **kwargs):
    """Quick evolution-chain lookup.

    See https://pokeapi.co/docsv2/#evolution-chains for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('evolution-chain', id_, **kwargs)

def evolution_trigger(id_or_name, **kwargs):
    """Quick evolution-trigger lookup.

    See https://pokeapi.co/docsv2/#evolution-triggers for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('evolution-trigger', id_or_name, **kwargs)

def generation(id_or_name, **kwargs):
    """Quick generation lookup.

    See https://pokeapi.co/docsv2/#generations for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('generation', id_or_name, **kwargs)

def pokedex(id_or_name, **kwargs):
    """Quick pokedex lookup.

    See https://pokeapi.co/docsv2/#pokedexes for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokedex', id_or_name, **kwargs)

def version(id_or_name, **kwargs):
    """Quick version lookup.

    See https://pokeapi.co/docsv2/#versions for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('version', id_or_name, **kwargs)

def version_group(id_or_name, **kwargs):
    """Quick version-group lookup.

    See https://pokeapi.co/docsv2/#version-groups for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('version-group', id_or_name, **kwargs)

def item(id_or_name, **kwargs):
    """Quick item lookup.

    See https://pokeapi.co/docsv2/#items for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('item', id_or_name, **kwargs)

def item_attribute(id_or_name, **kwargs):
    """Quick item-attribute lookup.

    See https://pokeapi.co/docsv2/#item-attributes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('item-attribute', id_or_name, **kwargs)

def item_category(id_or_name, **kwargs):
    """Quick item-category lookup.

    See https://pokeapi.co/docsv2/#item-categories for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('item-category', id_or_name, **kwargs)

def item_fling_effect(id_or_name, **kwargs):
    """Quick item-fling-effect lookup.

    See https://pokeapi.co/docsv2/#item-fling-effects for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('item-fling-effect', id_or_name, **kwargs)

def item_pocket(id_or_name, **kwargs):
    """Quick item-pocket lookup.

    See https://pokeapi.co/docsv2/#item-pockets for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('item-pocket', id_or_name, **kwargs)

def machine(id_, **kwargs):
    """Quick machine lookup.

    See https://pokeapi.co/docsv2/#machines for attributes and more detailed
    information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('machine', id_, **kwargs)

def move(id_or_name, **kwargs):
    """Quick move lookup.

    See https://pokeapi.co/docsv2/#moves for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('move', id_or_name, **kwargs)

def move_ailment(id_or_name, **kwargs):
    """Quick move-ailment lookup.

    See https://pokeapi.co/docsv2/#move-ailments for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('move-ailment', id_or_name, **kwargs)

def move_battle_style(id_or_name, **kwargs):
    """Quick move-battle-style lookup.

    See https://pokeapi.co/docsv2/#move-battle-styles for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('move-battle-style', id_or_name, **kwargs)

def move_category(id_or_name, **kwargs):
    """Quick move-category lookup.

    See https://pokeapi.co/docsv2/#move-categories for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('move-category', id_or_name, **kwargs)

def move_damage_class(id_or_name, **kwargs):
    """Quick move-damage-class lookup.

    See https://pokeapi.co/docsv2/#move-damage-classes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('move-damage-class', id_or_name, **kwargs)

def move_learn_method(id_or_name, **kwargs):
    """Quick move-learn-method lookup.

    See https://pokeapi.co/docsv2/#move-learn-methods for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('move-learn-method', id_or_name, **kwargs)

def move_target(id_or_name, **kwargs):
    """Quick move-target lookup.

    See https://pokeapi.co/docsv2/#move-targets for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('move-target', id_or_name, **kwargs)

def location(id_, **kwargs):
    """Quick location lookup.

    See https://pokeapi.co/docsv2/#locations for attributes and more detailed
    information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('location', id_, **kwargs)

def location_area(id_, **kwargs):
    """Quick location-area lookup.

    See https://pokeapi.co/docsv2/#location-areas for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('location-area', id_, **kwargs)

def pal_park_area(id_or_name, **kwargs):
    """Quick pal-park-area lookup.

    See https://pokeapi.co/docsv2/#pal-park-areas for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pal-park-area', id_or_name, **kwargs)

def region(id_or_name, **kwargs):
    """Quick region lookup.

    See https://pokeapi.co/docsv2/#regions for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('region', id_or_name, **kwargs)

def ability(id_or_name, **kwargs):
    """Quick ability lookup.

    See https://pokeapi.co/docsv2/#abilities for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('ability', id_or_name, **kwargs)

def characteristic(id_, **kwargs):
    """Quick characteristic lookup.

    See https://pokeapi.co/docsv2/#characteristics for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('characteristic', id_, **kwargs)

def egg_group(id_or_name, **kwargs):
    """Quick egg-group lookup.

    See https://pokeapi.co/docsv2/#egg-groups for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('egg-group', id_or_name, **kwargs)

def gender(id_or_name, **kwargs):
    """Quick gender lookup.

    See https://pokeapi.co/docsv2/#genders for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('gender', id_or_name, **kwargs)

def growth_rate(id_or_name, **kwargs):
    """Quick growth-rate lookup.

    See https://pokeapi.co/docsv2/#growth-rates for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('growth-rate', id_or_name, **kwargs)

def nature(id_or_name, **kwargs):
    """Quick nature lookup.

    See https://pokeapi.co/docsv2/#natures for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('nature', id_or_name, **kwargs)

def pokeathlon_stat(id_or_name, **kwargs):
    """Quick pokeathlon-stat lookup.

    See https://pokeapi.co/docsv2/#pokeathlon-stats for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokeathlon-stat', id_or_name, **kwargs)

def pokemon(id_or_name, **kwargs):
    """Quick pokemon lookup.

    See https://pokeapi.co/docsv2/#pokemon for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokemon', id_or_name, **kwargs)

def pokemon_color(id_or_name, **kwargs):
    """Quick pokemon-color lookup.

    See https://pokeapi.co/docsv2/#pokemon-colors for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokemon-color', id_or_name, **kwargs)

def pokemon_form(id_or_name, **kwargs):
    """Quick pokemon-form lookup.

    See https://pokeapi.co/docsv2/#pokemon-forms for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokemon-form', id_or_name, **kwargs)

def pokemon_habitat(id_or_name, **kwargs):
    """Quick pokemon-habitat lookup.

    See https://pokeapi.co/docsv2/#pokemon-habitats for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokemon-habitat', id_or_name, **kwargs)

def pokemon_shape(id_or_name, **kwargs):
    """Quick pokemon-shape lookup.

    See https://pokeapi.co/docsv2/#pokemon-shapes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokemon-shape', id_or_name, **kwargs)

def pokemon_species(id_or_name, **kwargs):
    """Quick pokemon-species lookup.

    See https://pokeapi.co/docsv2/#pokemon-species for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('pokemon-species', id_or_name, **kwargs)

def stat(id_or_name, **kwargs):
    """Quick stat lookup.

    See https://pokeapi.co/docsv2/#stats for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('stat', id_or_name, **kwargs)

def type_(id_or_name, **kwargs):
    """Quick type lookup.

    See https://pokeapi.co/docsv2/#types for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('type', id_or_name, **kwargs)

def language(id_or_name, **kwargs):
    """Quick language lookup.

    See https://pokeapi.co/docsv2/#languages for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return APIResource('language', id_or_name, **kwargs)

def sprite(sprite_type, sprite_id, **kwargs):

    return SpriteResource(sprite_type, sprite_id, **kwargs)
