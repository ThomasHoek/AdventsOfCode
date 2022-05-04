#  ( -> go up one floor
#  ) -> go down one floor
#  infinite height

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/../input.txt", "r").readline()
up = puzzle_input.count("(")
down = puzzle_input.count(")")
print(up - down)
