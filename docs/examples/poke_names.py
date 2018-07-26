import pokebase as pb

GENERATION = 2

gen_resource = pb.generation(GENERATION)

for pokemon in gen_resource.pokemon_species:
    print(pokemon.name.title())
