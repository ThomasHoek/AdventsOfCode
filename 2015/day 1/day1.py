#  ( -> go up one floor
#  ) -> go down one floor
#  infinite height

puzzle_input = open("input.txt", "r").readline()
up = puzzle_input.count("(")
down = puzzle_input.count(")")
print(up - down)
