# ^: north
# v: south
# <: west
# >: east
# Question: how many atleast 1.

# location tuple: (North/south, east/west)
def new_location(direction: str, current_loc: tuple) -> tuple:
    """Get new location

    Args:
        direction (str): cardinal direction
        current_loc (tuple): current location

    Returns:
        tuple: new location
    """
    def add_tuple(tp1, tp2):
        return tuple(map(sum, zip(tp1, tp2)))

    return {
        '^': add_tuple(current_loc, (1, 0)),
        '>': add_tuple(current_loc, (0, 1)),
        'v': add_tuple(current_loc, (-1, 0)),
        '<': add_tuple(current_loc, (0, -1)),
    }[direction]


unique_coords_s1 = set()
loc1 = (0, 0)
unique_coords_s1.add(loc1)

unique_coords_s2 = set()
loc2 = (0, 0)
unique_coords_s2.add(loc2)

puzzle_input = open("input.txt", "r").readline()
for count, command in enumerate(puzzle_input, 0):

    if count % 2 == 0:
        loc1 = new_location(command, loc1)
        unique_coords_s1.add(loc1)
    else:
        loc2 = new_location(command, loc2)
        unique_coords_s2.add(loc2)

print(len(set.union(unique_coords_s1, unique_coords_s2)))
