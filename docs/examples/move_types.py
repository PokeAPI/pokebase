import pokebase as pb

TYPE = 'normal'
all_moves = pb.APIResourceList('move')

# Bad method. Don't actually do this.
for move_data in all_moves:
    move = pb.move(move_data['name'])
    if move.type.name == TYPE:
        print(move.name)

# Good method.
normal_moves = pb.type_(TYPE).moves
for move in normal_moves:
    print(move.name)
