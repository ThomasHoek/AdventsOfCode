import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# puzzle_input = open(f"{dir_path}/test.txt", "r").readlines()
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip().split(" ") for x in puzzle_input]


def calc_win(x, y):
    # rock
    if x == "A":
        # lose -> scissor
        if y == "X":
            return 3
        # draw -> rock
        elif y == "Y":
            return 1
        # win -> paper
        elif y == "Z":
            return 2

    # paper
    if x == "B":
        # lose -> rock
        if y == "X":
            return 1
        # draw -> paper
        elif y == "Y":
            return 2
        # win -> scissor
        elif y == "Z":
            return 3

    # scissor
    if x == "C":
        # lose -> paper
        if y == "X":
            return 2
        # draw -> scissor
        elif y == "Y":
            return 3
        # win -> rock
        elif y == "Z":
            return 1


point_dict = {
    "X": 0,
    "Y": 3,
    "Z": 6}

total_points = 0
for first, second in puzzle_input:
    total_points += point_dict[second]
    total_points += calc_win(first, second)

print(total_points)
