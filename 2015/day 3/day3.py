# ^: north
# v: south
# <: west
# >: east
# Question: how many atleast 1.
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readline()


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


unique_coords = set()
loc = (0, 0)
unique_coords.add(loc)

for command in puzzle_input:
    loc = new_location(command, loc)
    unique_coords.add(loc)

print(len(unique_coords))
