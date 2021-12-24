# [Done] exited with code=0 in 0.216 seconds
import math
import numpy as np
import copy


input_file = open("input.txt","r").readlines()
input_file = [int(word.rstrip()) for word in input_file]

first = 0
end = 25


while end != len(input_file):
    preamble = input_file[first:end]


    def get_set(preamble_input):
        new_set = set()
        for i in preamble_input:
            for j in preamble_input:
                new_set.add(i+j)
        
        return new_set


    if input_file[end] not in get_set(preamble):
        print(input_file[end])
        break

    first += 1
    end += 1
    


