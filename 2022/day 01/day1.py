import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# puzzle_input = open(f"{dir_path}/test.txt", "r").readlines()
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [int(x.rstrip()) if x.rstrip().isdigit()
                else x.rstrip() for x in puzzle_input]

highest = 0
elf_carry = 0
for i in puzzle_input:
    if i == "":
        highest = max(highest, elf_carry)
        elf_carry = 0
    else:
        elf_carry += i

# remainder
highest = max(highest, elf_carry)


print(highest)
