import random
from character import Character
from weapon import Weapon
from spell import Spell


class Treasures:

    def __init__(self):
        dict_of_treasures = {
            "weapons": Weapon(name='--Sword--', damage=40),
            "weapons": Weapon(name='--Fighting knives--', damage=20),
            "weapons": Weapon(name='--Daggers--', damage=40),
            "spells": Spell(name='--Freezing spell--', damage=30, mana_cost=50, cast_range=1),
            "spells": Spell(name='--Black spell--', damage=30, mana_cost=50, cast_range=1),
            "spells": Spell(name='--Disappear spell--', damage=30, mana_cost=50, cast_range=1),
            "mana": 10,
            "mana": 15,
            "mana": 20,
            "health": 10,
            "health": 20,
            "health": 25,

        }
        self.kind_of_treasure = random.choice(list(dict_of_treasures.keys()))
        self.treasure = dict_of_treasures.get(self.kind_of_treasure)

    def get_kind_of_treasure(self):
        return self.kind_of_treasure

    def get_treasure(self):
        return self.treasure

    def pick_treasure(self):
        if self.kind_of_treasure == 'mana':
            print("Hero has found a mana!")
            return self.treasure

        elif self.kind_of_treasure == 'health':
            print('Hero has found a health treasure!')
            return self.treasure

        elif self.kind_of_treasure == 'weapons':
            print("Hero has found a weapon!")
            return self.treasure

        elif self.kind_of_treasure == 'spells':
            print("Hero has learned a spell!")
            return self.treasure


treasure = Treasures()
print(treasure.pick_treasure())
