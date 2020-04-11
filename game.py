from hero import Hero
from dungeon import Dungeon
from magic_strings import *
from colors import fg


def direction_checker():
    print(f"{fg.green} Choose direction for your hero: {fg.end_color}")
    print(f"{fg.yellow} '->'' - 'r', '<-' - 'l', '↓' - 'd' , '↑' - 'u'\n {fg.end_color}")
    direction = input()
    if directions.get(direction) in directions:
        return directions.get(direction)
    else:
        while direction not in directions:
            direction = input(f"{fg.green} Incorrect direction, choose again: {fg.end_color}")
        return directions.get(direction)


def attack_checker(dungeon, choice):
    if choice not in attack_dict:
        print('Invalid choice!')
    else:
        return dungeon.hero_attack(attack_dict.get(choice))


def choice_checker(dungeon, choice):
    if choice == 'a':
        print(f"{fg.yellow}Choose the thing you want to attack with:\n {fg.end_color}")
        print(f"{fg.yellow}'s' - spell\n'w' - weapon {fg.end_color}")
        choice = input()
        attack_checker(dungeon, choice)
    elif choice == 's':
        print(dungeon.hero.known_as())
        print(str(dungeon.hero))


def start_game():
    result = False
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

    while result is not True:
        print(fg.bold, fg.yellow, "Current map: ", fg.end_color)
        map.print_map()
        print(f"{fg.yellow}Choose one of the following: {fg.end_color}")
        print(f"{fg.yellow}Move your hero: 'm'\n {fg.end_color}")
        print(f"{fg.yellow}Stats of your hero: 's'\n {fg.end_color}")
        print(f"{fg.yellow}Attack with your hero: 'a'\n {fg.end_color}")
        choice = input()
        if choice == 'm':
            t = direction_checker()
            result = map.move_hero(str(t))
        elif choice == 's' or choice == 'a':
            result = choice_checker(map, choice)
        else:
            print('Invalid choice!')

def main():
    start_game()

if __name__=='__main__':
    main()
