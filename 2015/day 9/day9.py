# https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
# https://core.ac.uk/download/pdf/154419746.pdf

puzzle_input = open("input2.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]
print(puzzle_input)
all_places = set()

for line in puzzle_input:
    place1, other = line.split(" to ")
    place2, distance = other.split(" = ")
    all_places.add(place1)
    all_places.add(place2)
    city_dict[(place1, place2)] = distance
    city_dict[(place2, place1)] = distance


distance = float('inf')


def TSP()

city_dict = {}


