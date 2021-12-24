# This is an inspired solution for a language like c++ which does not have a .
# .count() function.

puzzle_input = open("input.txt", "r").readline()
print(len(puzzle_input.replace(")", "")) - len(puzzle_input.replace("(", "")))
