import random
from character import Character
from weapon import Weapon
from spell import Spell


class Treasure:

    def __init__(self):
        dict_of_treasures = {
            "weapon": Weapon(name='--Sword--', damage=40),
            "weapon": Weapon(name='--Fighting knives--', damage=20),
            "weapon": Weapon(name='--Daggers--', damage=40),
            "spell": Spell(name='--Freezing spell--', damage=30, mana_cost=50, cast_range=1),
            "spell": Spell(name='--Black spell--', damage=30, mana_cost=50, cast_range=1),
            "spell": Spell(name='--Disappear spell--', damage=30, mana_cost=50, cast_range=1),
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
            print("It is a mana potion!")
            return self.treasure

        elif self.kind_of_treasure == 'health':
            print('It is a health potion!')
            return self.treasure

        elif self.kind_of_treasure == 'weapon':
            print("It is a weapon!")
            return self.treasure

        elif self.kind_of_treasure == 'spell':
            print("It is a spell!")
            return self.treasure

'''
treasure = Treasure()
print(treasure.pick_treasure())
'''