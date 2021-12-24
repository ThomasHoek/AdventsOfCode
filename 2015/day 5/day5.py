
def vowel_check(inp: str) -> bool:
    inp.lower()
    count = 0
    for vowel in "aeiou":
        count += inp.count(vowel)
    return count >= 3


def check_double_letter(inp: str) -> bool:
    for i in range(len(inp) - 1):
        if inp[i] == inp[i+1]:
            return True
    return False


def contains_string(inp: str) -> bool:
    for forbidden_combo in ["ab", "cd", "pq", "xy"]:
        if forbidden_combo in inp:
            return False
    return True


nice = 0
naughty = 0
puzzle_input = open("input.txt", "r").readlines()
for line in puzzle_input:
    if vowel_check(line):
        if check_double_letter(line):
            if contains_string(line):
                nice += 1
            else:
                naughty += 1
        else:
            naughty += 1
    else:
        naughty += 1
print(nice, naughty)
