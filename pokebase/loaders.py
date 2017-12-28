# -*- coding: utf-8 -*-

from .api import NamedAPIResource, SpriteResource


def berry(id_or_name):
    """Quick berry lookup.

    See https://pokeapi.co/docsv2/#berries for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('berry', id_or_name)


def berry_firmness(id_or_name):
    """Quick berry-firmness lookup.

    See https://pokeapi.co/docsv2/#berry-firmnesses for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('berry-firmness', id_or_name)


def berry_flavor(id_or_name):
    """Quick berry-flavor lookup.

    See https://pokeapi.co/docsv2/#berry-flavors for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('berry-flavor', id_or_name)


def contest_type(id_or_name):
    """Quick contest-type lookup.

    See https://pokeapi.co/docsv2/#contest-types for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('contest-type', id_or_name)


def contest_effect(id_):
    """Quick contest-effect lookup.

    See https://pokeapi.co/docsv2/#contest-effects for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('contest-effect', id_)


def super_contest_effect(id_):
    """Quick super-contest-effect lookup.

    See https://pokeapi.co/docsv2/#super-contest-effects for attributes and
    more detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('super-contest-effect', id_)


def encounter_method(id_or_name):
    """Quick encounter-method lookup.

    See https://pokeapi.co/docsv2/#encounter-methods for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('encounter-method', id_or_name)


def encounter_condition(id_or_name):
    """Quick encounter-condition lookup.

    See https://pokeapi.co/docsv2/#encounter-conditions for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('encounter-condition', id_or_name)


def encounter_condition_value(id_or_name):
    """Quick encounter-condition-value lookup.

    See https://pokeapi.co/docsv2/#encounter-condition-values for attributes
    and more detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('encounter-condition-value', id_or_name)


def evolution_chain(id_):
    """Quick evolution-chain lookup.

    See https://pokeapi.co/docsv2/#evolution-chains for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('evolution-chain', id_)


def evolution_trigger(id_or_name):
    """Quick evolution-trigger lookup.

    See https://pokeapi.co/docsv2/#evolution-triggers for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('evolution-trigger', id_or_name)


def generation(id_or_name):
    """Quick generation lookup.

    See https://pokeapi.co/docsv2/#generations for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('generation', id_or_name)


def pokedex(id_or_name):
    """Quick pokedex lookup.

    See https://pokeapi.co/docsv2/#pokedexes for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokedex', id_or_name)


def version(id_or_name):
    """Quick version lookup.

    See https://pokeapi.co/docsv2/#versions for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('version', id_or_name)


def version_group(id_or_name):
    """Quick version-group lookup.

    See https://pokeapi.co/docsv2/#version-groups for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('version-group', id_or_name)


def item(id_or_name):
    """Quick item lookup.

    See https://pokeapi.co/docsv2/#items for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('item', id_or_name)


def item_attribute(id_or_name):
    """Quick item-attribute lookup.

    See https://pokeapi.co/docsv2/#item-attributes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('item-attribute', id_or_name)


def item_category(id_or_name):
    """Quick item-category lookup.

    See https://pokeapi.co/docsv2/#item-categories for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('item-category', id_or_name)


def item_fling_effect(id_or_name):
    """Quick item-fling-effect lookup.

    See https://pokeapi.co/docsv2/#item-fling-effects for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('item-fling-effect', id_or_name)


def item_pocket(id_or_name):
    """Quick item-pocket lookup.

    See https://pokeapi.co/docsv2/#item-pockets for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('item-pocket', id_or_name)


def machine(id_):
    """Quick machine lookup.

    See https://pokeapi.co/docsv2/#machines for attributes and more detailed
    information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('machine', id_)


def move(id_or_name):
    """Quick move lookup.

    See https://pokeapi.co/docsv2/#moves for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('move', id_or_name)


def move_ailment(id_or_name):
    """Quick move-ailment lookup.

    See https://pokeapi.co/docsv2/#move-ailments for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('move-ailment', id_or_name)


def move_battle_style(id_or_name):
    """Quick move-battle-style lookup.

    See https://pokeapi.co/docsv2/#move-battle-styles for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('move-battle-style', id_or_name)


def move_category(id_or_name):
    """Quick move-category lookup.

    See https://pokeapi.co/docsv2/#move-categories for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('move-category', id_or_name)


def move_damage_class(id_or_name):
    """Quick move-damage-class lookup.

    See https://pokeapi.co/docsv2/#move-damage-classes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('move-damage-class', id_or_name)


def move_learn_method(id_or_name):
    """Quick move-learn-method lookup.

    See https://pokeapi.co/docsv2/#move-learn-methods for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('move-learn-method', id_or_name)


def move_target(id_or_name):
    """Quick move-target lookup.

    See https://pokeapi.co/docsv2/#move-targets for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('move-target', id_or_name)


def location(id_):
    """Quick location lookup.

    See https://pokeapi.co/docsv2/#locations for attributes and more detailed
    information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('location', id_)


def location_area(id_):
    """Quick location-area lookup.

    See https://pokeapi.co/docsv2/#location-areas for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('location-area', id_)


def pal_park_area(id_or_name):
    """Quick pal-park-area lookup.

    See https://pokeapi.co/docsv2/#pal-park-areas for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pal-park-area', id_or_name)


def region(id_or_name):
    """Quick region lookup.

    See https://pokeapi.co/docsv2/#regions for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('region', id_or_name)


def ability(id_or_name):
    """Quick ability lookup.

    See https://pokeapi.co/docsv2/#abilities for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('ability', id_or_name)


def characteristic(id_):
    """Quick characteristic lookup.

    See https://pokeapi.co/docsv2/#characteristics for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('characteristic', id_)


def egg_group(id_or_name):
    """Quick egg-group lookup.

    See https://pokeapi.co/docsv2/#egg-groups for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('egg-group', id_or_name)


def gender(id_or_name):
    """Quick gender lookup.

    See https://pokeapi.co/docsv2/#genders for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('gender', id_or_name)


def growth_rate(id_or_name):
    """Quick growth-rate lookup.

    See https://pokeapi.co/docsv2/#growth-rates for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('growth-rate', id_or_name)


def nature(id_or_name):
    """Quick nature lookup.

    See https://pokeapi.co/docsv2/#natures for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('nature', id_or_name)


def pokeathlon_stat(id_or_name):
    """Quick pokeathlon-stat lookup.

    See https://pokeapi.co/docsv2/#pokeathlon-stats for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokeathlon-stat', id_or_name)


def pokemon(id_or_name):
    """Quick pokemon lookup.

    See https://pokeapi.co/docsv2/#pokemon for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokemon', id_or_name)


def pokemon_color(id_or_name):
    """Quick pokemon-color lookup.

    See https://pokeapi.co/docsv2/#pokemon-colors for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokemon-color', id_or_name)


def pokemon_form(id_or_name):
    """Quick pokemon-form lookup.

    See https://pokeapi.co/docsv2/#pokemon-forms for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokemon-form', id_or_name)


def pokemon_habitat(id_or_name):
    """Quick pokemon-habitat lookup.

    See https://pokeapi.co/docsv2/#pokemon-habitats for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokemon-habitat', id_or_name)


def pokemon_shape(id_or_name):
    """Quick pokemon-shape lookup.

    See https://pokeapi.co/docsv2/#pokemon-shapes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokemon-shape', id_or_name)


def pokemon_species(id_or_name):
    """Quick pokemon-species lookup.

    See https://pokeapi.co/docsv2/#pokemon-species for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('pokemon-species', id_or_name)


def stat(id_or_name):
    """Quick stat lookup.

    See https://pokeapi.co/docsv2/#stats for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('stat', id_or_name)


def type_(id_or_name):
    """Quick type lookup.

    See https://pokeapi.co/docsv2/#types for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('type', id_or_name)


def language(id_or_name):
    """Quick language lookup.

    See https://pokeapi.co/docsv2/#languages for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    """
    return NamedAPIResource('language', id_or_name)


def pokemon_sprite(id_):
    """Quick Pokemon sprite lookup.

    NOTE: This will return an object with the absolute file path to the sprite,
    NOT the sprite. This is designed as such so that you can load the image in
    whatever image class your specific application requires.

    :param id_: id of the sprite to lookup
    :return: SpriteResource object
    """

    return SpriteResource('pokemon', id_)
