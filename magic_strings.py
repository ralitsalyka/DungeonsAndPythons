from weapon import Weapon
from spell import Spell

right = 'right'
up = 'up'
down = 'down'
left = 'left'
spell = 'spell'
weapon = 'weapon'
enemy_name = 'Enemy'
health_potion = 'health potion'
mana_potion = 'mana potion'
available_directions = [right,up,down,left]

weapon_one = Weapon('Widowmaker',40)
weapon_two = Weapon('Blade of the Reaper',50)
weapon_three = Weapon('Poisonous daggers',30)
weapon_four = Weapon('Moonlight Idol',25)
weapon_five = Weapon('Netherbane, Might of the Void',55)

spell_one = Spell('Frostbolt',30,30,1)
spell_two = Spell('Fireball',40,40,2)
spell_three = Spell('Arcane Missiles',10,10,1)
spell_four = Spell('Flamestrike',50,50,3)
spell_five = Spell('Deadly shot',35,20,2)

dict_of_treasures = {
            weapon: weapon_one,
            weapon: weapon_two,
            weapon: weapon_three,
            weapon: weapon_four,
            weapon: weapon_five,
            spell: spell_one,
            spell: spell_two,
            spell: spell_three,
            spell: spell_four,
            spell: spell_five,
            mana_potion: 10,
            mana_potion: 15,
            mana_potion: 20,
            health_potion: 10,
            health_potion: 20,
            health_potion: 25,
        }