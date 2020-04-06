from treasures import Treasure
from character import Character
from magic_strings import *

def enemy_find_treasure(character):
    print('Enemy has found a treasure!',end = " ")
    new_treasure = Treasure()
    kind = new_treasure.get_kind_of_treasure()
    result = new_treasure.pick_treasure()
    if kind == weapon:
        print(result)
        character.equip(result)
    elif kind == spell:
        print(result)
        character.learn(result)
    else:
        print('Enemy throws away the potion so he can prevent our hero from successfully finishing the dungeon!')

def hero_find_treasure(character):
    new_treasure = Treasure()
    kind = new_treasure.get_kind_of_treasure()
    result = new_treasure.pick_treasure()
    if kind == weapon:
        print(result)
        character.equip(result)
    elif kind == spell:
        print(result)
        character.learn(result)
    elif kind == 'mana potion':
        print('This mana potion restores ' + str(result) + ' mana')
        character.take_mana(result)
    else:
        print('This health potion restores ' + str(result) + ' health')
        character.take_healing(result)

def transpose_matrix(matrix):
    return [list(tup) for tup in zip(*matrix)]