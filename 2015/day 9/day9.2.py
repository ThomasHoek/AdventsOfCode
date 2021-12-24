# We are making a genetic algorithm for this
from itertools import permutations

puzzle_input = open("input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]
all_places = set()
city_dict = {}

# Create a stange matrix in the dict.
for line in puzzle_input:
    place1, other = line.split(" to ")
    place2, distance = other.split(" = ")
    all_places.add(place1)
    all_places.add(place2)
    city_dict[(place1, place2)] = int(distance)
    city_dict[(place2, place1)] = int(distance)

max_distance = 0

# every possible combination, brute force
for combination in list(permutations(all_places)):
    local_distance = 0
    for city_index in range(len(combination) - 1):
        local_distance += city_dict[(combination[city_index],
                                     combination[city_index + 1])]
    max_distance = local_distance if local_distance > max_distance else max_distance

print(max_distance)