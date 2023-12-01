import os
# import random

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r")

boss = {}
boss["hp"] = int(puzzle_input.readline()[-3:].rstrip())
boss["dmg"] = int(puzzle_input.readline()[-2:].rstrip())

hp = 50
mana = 500


class spells:
    def __init__(self, cost, turns, start_damage=0, end_damage=0, heal=0,
                 armour=0, give_mana=0):
        self.cost = cost
        self.turns = turns
        self.start_damage = start_damage
        self.end_damage = end_damage
        self.heal = heal
        self.armour = armour
        self.give_mana = give_mana

    def lower_turn(self):
        if self.turns:
            self.turns -= 1
            return self.start_damage
        return 0

    def get_damage(self):
        if self.turns:
            return self.end_damage
        return 0

    def get_heal(self):
        if self.turns:
            return self.heal
        return 0

    def get_armour(self):
        if self.turns:
            return self.armour
        return 0

    def get_mana(self):
        if self.turns:
            return self.give_mana
        return 0

    def __repr__(self):
        return f"Mana: {self.cost, self.give_mana} | \
                turns {self.turns} | \
                damage {self.start_damage, self.end_damage} | \
                defence {self.heal, self.armour} \n"


spell_lst = [spells(cost=53, turns=1, end_damage=3),            # missile
             spells(cost=73, turns=1, end_damage=2, heal=2),    # drain
             spells(cost=113, turns=6, armour=7),               # shield
             spells(cost=173, turns=6, start_damage=3),         # poison
             spells(cost=229, turns=5, give_mana=101)]          # recharge
