import random
from .character import Character
from .weapon import Weapon
from .spell import Spell
from dungeons_and_pythons.models.magic_strings import *

class Treasure:

    def __init__(self):
        self.kind_of_treasure = random.choice(list(dict_of_treasures.keys()))
        self.treasure = dict_of_treasures.get(self.kind_of_treasure)

    def get_kind_of_treasure(self):
        return self.kind_of_treasure

    def get_treasure(self):
        return self.treasure

    def pick_treasure(self):
        if self.kind_of_treasure == mana_potion:
            print("It is a mana potion!")
            return self.treasure

        elif self.kind_of_treasure == health_potion:
            print('It is a health potion!')
            return self.treasure

        elif self.kind_of_treasure == weapon:
            print("It is a weapon!")
            return self.treasure

        elif self.kind_of_treasure == spell:
            print("It is a spell!")
            return self.treasure