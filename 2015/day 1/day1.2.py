#  ( -> go up one floor
#  ) -> go down one floor
#  infinite height

puzzle_input = open("input.txt", "r").readline()
pos = 0
for count, next_floor in enumerate(puzzle_input, 1):
    if next_floor == "(":
        pos += 1
    else:
        pos -= 1

    if pos == -1:
        break

print(count)
