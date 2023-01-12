import os
import random
import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r")

boss = {}
# boss["hp"] = int(puzzle_input.readline()[-3:].rstrip())
# boss["dmg"] = int(puzzle_input.readline()[-2:].rstrip())

# hp = 50
# mana = 500

hp = 10
mana = 250
boss["hp"] = 14
boss["dmg"] = 8


def my_turn(mana, hp, boss,
            shield, poison, recharge,
            cast, counter):
    global turns

    counter += 1
    spells = [1,    # magic missile
              2,    # drain
              3,    # Shield
              4,    # Poison
              5]    # Recharge

    def lower_spells(shield, poison, boss, mana, recharge):
        if shield > 1:
            shield -= 1

        if poison > 1:
            poison -= 1
            boss["hp"] -= 3

        if recharge > 1:
            mana += 101
            recharge -= 1
        return shield, poison, boss, mana, recharge

    shield, poison, boss, mana, recharge = lower_spells(
        shield, poison, boss, mana, recharge)

    # choosing action
    if cast == 1:       # magic missile
        mana -= 53
        boss["hp"] -= 4
    elif cast == 2:     # drain
        mana -= 73
        boss["hp"] -= 2
        hp += 2
    elif cast == 3:     # shield
        mana -= 113
        shield = 6
    elif cast == 4:     # Poison
        mana -= 173
        poison = 6
    elif cast == 5:     # recharge
        mana -= 229
        recharge = 5

    if boss["hp"] <= 0:
        return counter

    # boss turn
    counter += 1
    shield, poison, boss, mana, recharge = lower_spells(
        shield, poison, boss, mana, recharge)

    if boss["hp"] <= 0:
        return counter

    if shield:
        hp -= boss["dmg"] - 7
    else:
        hp -= boss["dmg"]

    if hp <= 0:
        return float('inf')

    # choose next move
    if mana < 53:
        spells.remove(1)
    if mana < 73:
        spells.remove(2)
    if shield != 0 or mana < 113:
        spells.remove(3)
    if poison != 0 or mana < 173:
        spells.remove(4)
    if recharge != 0 or mana < 229:
        spells.remove(5)

    if spells == []:
        return min(my_turn(mana, hp, boss,
                           shield, poison, recharge,
                           0, counter), turns)

    for cast in spells:
        return min(my_turn(mana, hp, boss,
                           shield, poison, recharge,
                           cast, counter), turns)


turns = float("inf")
for i in range(7):
    my_turn(copy.deepcopy(mana),
            copy.deepcopy(hp),
            copy.deepcopy(boss), 0, 0, 0, i, 0)

print(turns)
