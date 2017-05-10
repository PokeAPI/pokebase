#!/usr/bin/python
# -*- coding: utf-8 -*-

from .api import NamedAPIResource


def berry(id_or_name):
    return NamedAPIResource('berry', id_or_name)


def berry_firmness(id_or_name):
    return NamedAPIResource('berry-firmness', id_or_name)


def berry_flavor(id_or_name):
    return NamedAPIResource('berry-flavor', id_or_name)


def contest_type(id_or_name):
    return NamedAPIResource('contest-type', id_or_name)


def contest_effect(id_):
    return NamedAPIResource('contest-effect', id_)


def super_contest_effect(id_):
    return NamedAPIResource('super-contest-effect', id_)


def encounter_method(id_or_name):
    return NamedAPIResource('encounter-method', id_or_name)


def encounter_condition(id_or_name):
    return NamedAPIResource('encounter-condition', id_or_name)


def encounter_condition_value(id_or_name):
    return NamedAPIResource('encounter-condition-value', id_or_name)


def evolution_chain(id_):
    return NamedAPIResource('evolution-chain', id_)


def evolution_trigger(id_or_name):
    return NamedAPIResource('evolution-trigger', id_or_name)


def generation(id_or_name):
    return NamedAPIResource('generation', id_or_name)


def pokedex(id_or_name):
    return NamedAPIResource('pokedex', id_or_name)


def version(id_or_name):
    return NamedAPIResource('version', id_or_name)


def version_group(id_or_name):
    return NamedAPIResource('version-group', id_or_name)


def item(id_or_name):
    return NamedAPIResource('item', id_or_name)


def item_attribute(id_or_name):
    return NamedAPIResource('item-attribute', id_or_name)


def item_category(id_or_name):
    return NamedAPIResource('item-category', id_or_name)


def item_fling_effect(id_or_name):
    return NamedAPIResource('item-fling-effect', id_or_name)


def item_pocket(id_or_name):
    return NamedAPIResource('item-pocket', id_or_name)


def machine(id_):
    return NamedAPIResource('machine', id_)


def move(id_or_name):
    return NamedAPIResource('move', id_or_name)


def move_ailment(id_or_name):
    return NamedAPIResource('move-ailment', id_or_name)


def move_battle_style(id_or_name):
    return NamedAPIResource('move-battle-style', id_or_name)


def move_category(id_or_name):
    return NamedAPIResource('move-category', id_or_name)


def move_damage_class(id_or_name):
    return NamedAPIResource('move-damage-class', id_or_name)


def move_learn_method(id_or_name):
    return NamedAPIResource('move-learn-method', id_or_name)


def move_target(id_or_name):
    return NamedAPIResource('move-target', id_or_name)


def location(id_):
    return NamedAPIResource('location', id_)


def location_area(id_):
    return NamedAPIResource('location-area', id_)


def pal_park_area(id_or_name):
    return NamedAPIResource('pal-park-area', id_or_name)


def region(id_or_name):
    return NamedAPIResource('region', id_or_name)


def ability(id_or_name):
    return NamedAPIResource('ability', id_or_name)


def characteristic(id_):
    return NamedAPIResource('characteristic', id_)


def egg_group(id_or_name):
    return NamedAPIResource('egg-group', id_or_name)


def gender(id_or_name):
    return NamedAPIResource('gender', id_or_name)


def growth_rate(id_or_name):
    return NamedAPIResource('growth-rate', id_or_name)


def nature(id_or_name):
    return NamedAPIResource('nature', id_or_name)


def pokeathlon_stat(id_or_name):
    return NamedAPIResource('pokeathlon-stat', id_or_name)


def pokemon(id_or_name):
    return NamedAPIResource('pokemon', id_or_name)


def pokemon_color(id_or_name):
    return NamedAPIResource('pokemon-color', id_or_name)


def pokemon_form(id_or_name):
    return NamedAPIResource('pokemon-form', id_or_name)


def pokemon_habitat(id_or_name):
    return NamedAPIResource('pokemon-habitat', id_or_name)


def pokemon_shape(id_or_name):
    return NamedAPIResource('pokemon-shape', id_or_name)


def pokemon_species(id_or_name):
    return NamedAPIResource('pokemon-species', id_or_name)


def stat(id_or_name):
    return NamedAPIResource('stat', id_or_name)


def type_(id_or_name):
    return NamedAPIResource('type', id_or_name)


def language(id_or_name):
    return NamedAPIResource('language', id_or_name)
