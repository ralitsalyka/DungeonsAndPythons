from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell
from utils import *
from magic_strings import *

class Fight:
    def __init__(self,hero,enemy,list_of_steps):
        self.hero = hero
        self.enemy = enemy
        self.list_of_steps = list_of_steps
        self.number_of_steps = len(list_of_steps)

    def attack_and_defend(self,attacker,defender):
        if isinstance(attacker,Hero):
            attacker_name = attacker.name
        else:
            attacker_name = enemy_name
        if isinstance(defender,Hero):
            defender_name = defender.name
        else:
            defender_name = enemy_name

        if attacker.can_cast():
            attacker.attack(spell)
            defender.take_damage(attacker.spell.damage)
            print(attacker_name + ' casts ' + attacker.spell.name + ' and hits ' + defender_name + ' for ' + str(attacker.spell.damage) +'. ',end="")
            print(defender_name + ' health is ' + str(defender.current_health))
            return True
        elif attacker.weapon is not None:
            if self.number_of_steps > 0:
                if isinstance(attacker,Hero):
                    print(attacker.name+' waits for Enemy to move one step closer to him.')
                    return True
            else:
                attacker.attack(weapon)
                defender.take_damage(attacker.weapon.damage)
                print(attacker_name + ' attacks with ' + attacker.weapon.name + ' and hits ' + defender_name + ' for ' + str(attacker.weapon.damage) +'. ',end="")
                print(defender_name + ' health is ' + str(defender.current_health))
                return True
        return False

    def fight(self):
        while self.hero.is_alive() and self.enemy.is_alive():
            if not self.attack_and_defend(self.hero,self.enemy):
                print('Your hero has no mana for spell and is not equipped with a weapon. He will not survive this fight.')
                break
            if self.enemy.is_alive():
                if not self.enemy.can_cast():
                    if self.number_of_steps > 0:
                        self.number_of_steps -= 1
                        if len(self.list_of_steps) > 1:
                            if self.list_of_steps[-2] == 'T':
                                enemy_find_treasure(self.enemy)
                                self.list_of_steps[-2] = self.list_of_steps[-1]
                                self.list_of_steps = self.list_of_steps[:-1]
                            else:
                                self.list_of_steps = self.list_of_steps[:-1]
                                print('Enemy moves one step closer to Hero.')
                    else:
                        self.hero.take_damage(self.enemy.damage)
                        print('Enemy attack with his own damage! Enemy hits Hero for '+str(self.enemy.damage)+' damage. ',end="")
                        print(self.hero.name + ' health is ' + str(self.hero.current_health))
                elif self.enemy.can_cast():
                    if enemy.spell.cast_range >= self.number_of_steps:
                        self.attack_and_defend(self.enemy,self.hero)
                    else:
                        self.number_of_steps -= 1
                        print('Enemy moves one step closer to Hero.')
                else:
                    if not self.attack_and_defend(self.enemy,self.hero):
                        self.hero.take_damage(self.enemy.damage)
                        print('Enemy attack with his own damage! Enemy hits ' +self.hero.name+ 'for '+str(self.enemy.damage),end="")
                        print(self.hero.name+' health is ' + str(self.hero.current_health))
            else:
                print('Enemy is dead!')
                return True
        print('You have died!')
        return False