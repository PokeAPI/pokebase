import pokebase as pb

# View Pokemon from this generation number.
GENERATION = 2

# Get API data associated with that particular generation.
gen_resource = pb.generation(GENERATION)

# Iterate through the list of Pokemon introduced in that generation.
for pokemon in gen_resource.pokemon_species:
    print(pokemon.name.title())
