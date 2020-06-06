# Dungeons And Pythons

This is a simple, 2D turn-based console game.

# Setup

Download the repository and run the game with ```python3 game.py```.

# Game explanation

When you start the game you will be asked to input the name and title of your hero.

Your Hero starts in a dungeon with 100 health and 100 mana and his goal is to find his way out. The dungeon is a 2D map that looks like this:

```
S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G
```
Where:

- `S` means a starting point for our hero.
- `G` means gateway - the end of the dungeon (and most propably the enter to another)
- `#` is an obstacle
- `.` is a walkable path.
- `T` is a treasure that can be either mana, health, weapon or spell
- `E` is an enemy that our hero can fight

The layout of the map is loaded from a .txt file. In our repository this file is currently called ```level1.txt```

After starting the game before each further move the current display of the map will be shown and a few guidelines for you to input and decide where you want to move. 

If you run into an obstacle the program will notify you.
Whenever you run into an enemy you will be notified and will have the option to choose whether you want to engage into a fight or not. If a fight is started it follows the following algorithm:
- Our hero always attacks first
- We always use the attack that deals more damage
- If our weapon and our spell deals the same amount of damage, use the spell first.
- When you run out of mana, use the weapon (if any)

During the game you will have the chance to discover some treasures. They can be new spells, new weapons, or health and mana potions that replenish your current stats.
