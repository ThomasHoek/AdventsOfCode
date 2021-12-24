# [Done] exited with code=0 in 0.052 seconds
import re
input_file = open("input.txt", "r").readlines()

new_input = [[]]
counter = 0
for line in input_file:
    if line == "\n":
        counter += 1
        new_input.append([])
    else:
        new_input[counter].append(line.rstrip())

new_input = [[word.split(" ") for word in lst] for lst in new_input]

total_correct = 0
for passport in new_input:
    correct = 0

    passport_dict = {}
    for line in passport:
        for word in line:
            key, value = word.split(":")
            passport_dict[key] = value

    if "byr" in passport_dict:
        if 1920 <= int(passport_dict["byr"]) and 2002 >= int(passport_dict["byr"]):
            correct += 1

    if "iyr" in passport_dict and correct == 1:
        if 2010 <= int(passport_dict["iyr"]) and 2020 >= int(passport_dict["iyr"]):
            correct += 1

    if "eyr" in passport_dict and correct == 2:
        if 2020 <= int(passport_dict["eyr"]) and 2030 >= int(passport_dict["eyr"]):
            correct += 1

    if "hgt" in passport_dict and correct == 3:
        height = passport_dict["hgt"]
        if "cm" in height:
            value1 = 150
            value2 = 193
            height2 = int(height[:-2])

        elif "in" in height:
            value1 = 59
            value2 = 76
            height2 = int(height[:-2])

        else:
            value1 = 0
            value2 = 0
            height2 = 9999

        if value1 <= height2 and value2 >= height2:
            correct += 1

    if "hcl" in passport_dict and correct == 4:
        value = passport_dict["hcl"]
        if value[0] == "#" and len(value) == 7 and re.match("[a-f0-9#]", value):
            correct += 1

    if "ecl" in passport_dict and correct == 5:
        if passport_dict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            correct += 1

    if "pid" in passport_dict and correct == 6:

        if re.match("[0-9]", passport_dict["pid"]) and len(passport_dict["pid"]) == 9:
            correct += 1

    # correct = correct + 1 if "cid"  in passport_dict else correct

    if correct == 7:
        total_correct += 1

print(total_correct)    
