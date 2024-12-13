# Puzzle 6, part 1 from adventofcode 2020.

puzzle_input = open("input.txt", "r").readlines()

temp = []
cleaned_puzzle_input = []
for line in puzzle_input:
    if line == "\n":
        # sum = sum + len(temp)  # group ends, sum stuff up
        cleaned_puzzle_input.append(temp)
        temp = []

    else:
        temp.append(line.replace("\n", ""))  # to avoid counting escape char

cleaned_puzzle_input.append(temp)


del puzzle_input
temp = []


def solution():
    """Sums the unique responses into a total."""
    sum = 0

    for group in cleaned_puzzle_input:
        temp = 0
        for answers in group[0]:  # We only need to loop the first.
            isUnique = True

            for persons in group:
                if answers not in persons:
                    isUnique = False

            if isUnique is True:
                temp += 1

        sum += temp

    print(sum)


solution()
