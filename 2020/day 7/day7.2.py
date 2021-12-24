# [Done] exited with code=0 in 0.722 seconds
import math
import numpy as np
import copy
from collections import Counter



input_file = open("input.txt","r").readlines()

bag_total = []
bag_list = []
new_bags = ["shiny gold"]

def line_cleanup(line):
    line = line.rstrip()
    line = line.replace("bags","bag")
    line = line.replace(".","").replace(",","")
    line = line.split("contain")[-1]
    line = line.split("bag")[:-1]
    return line

while True:
    previous_bag = copy.deepcopy(bag_list)
    for line in input_file:
        for nbag in new_bags:
            if nbag in line:
                if nbag == ' '.join(line.split(" ")[:2]):
                    new_line = [(bag.strip().split(" ")[0], ' '.join(bag.strip().split(" ")[-2:])) for bag in line_cleanup(line)]
                    for bags in new_line:
                        if bags[0] != "no":

                            bag_list = bag_list + [bags[-1]] * int(bags[0])


    
    if previous_bag == bag_list:
        break
    
    else:
        # https://stackoverflow.com/questions/8106227/difference-between-two-lists-with-duplicates-in-python
        
        c1 = Counter(bag_list)
        c2 = Counter(previous_bag)

        diff = c1-c2
        new_bags = list(diff.elements())

print(len(bag_list))

