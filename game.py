from hero import Hero
from dungeon import Dungeon
from enemy import Enemy
from character import Character
from spell import Spell
from weapon import Weapon
from magic_strings import *
from colors import fg

def direction_checker():
    direction = input(f"{fg.green} Choose direction for your hero: {fg.end_color}")
    if directions.get(direction) in directions:
        return directions.get(direction)
    else:
        while direction not in directions:
            direction = input(f"{fg.green} Incorrect direction, choose again: {fg.end_color}")
        return directions.get(direction)


def start_game():
    print(fg.orange, fg.bold, "\n          Welcome to Dungeons and Pythons          ", '\033[0m')
    print(fg.orange, "       If you want to play, create your hero now:                  \n", fg.end_color)
    n = input("Give him/her a name:")
    t = input("And a title:")
    hero = Hero(str(n), str(t), 100, 100, 2)
    print(f"\n ~~~~~~~~~~Your hero is known as {fg.lightred} {fg.bold} {str(hero.known_as())} {fg.end_color} ~~~~~~~~~~~~~~~")
    print(f" ~~~~~~~~~~You have: {fg.blue} {fg.bold} health - {hero.get_health()}, mana - {hero.get_mana()} {fg.end_color} ~~~~~~~~~~~~~~~\n")
    s = spell_four
    hero.learn(s)
    w = weapon_three
    hero.equip(w)
    map = Dungeon("level1.txt")
    map.spawn(hero)
    print(f"{fg.yellow}{fg.bold}This is your map for the game:\n {fg.end_color}")

    map.print_map()
    print(f"\n'H' - your hero")
    print(f"'E' - enemy")
    print(f"'.' - you can move there")
    print(f"'#' - you can't go there \n\n ")
    print(f"{fg.yellow}Now you have to choose where to move your hero:\n '->'' - 'r', '<-' - 'l', '↓' - 'd' , '↑' - 'u'\n {fg.end_color}")
    t = direction_checker()
    result = map.move_hero(str(t))

    while result != False:
        print(fg.bold, fg.yellow, "Your current position on the map: ", fg.end_color)
        map.print_map()
        t = direction_checker()
        result = map.move_hero(str(t))
        if result == 'y':
            map.hero_attack('spell')

def main():
    print(start_game())

if __name__=='__main__':
    main()
