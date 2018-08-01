import pokebase as pb

# Print all moves of the type named here.
TYPE = 'normal'

# Get a list of EVERY move from the API.
all_moves = pb.APIResourceList('move')

# Bad method. Don't actually do this.
for move_data in all_moves:
    # Get API data for this move.
    move = pb.move(move_data['name'])

    # Print its name, if its type matches.
    if move.type.name == TYPE:
        print(move.name)

# Good method.
# Get API data associated with the type we want.
type_moves = pb.type_(TYPE).moves

# Iterate & print.
for move in type_moves:
    print(move.name)
