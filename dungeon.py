from hero import Hero
from enemy import Enemy
from treasures import Treasure
from weapon import Weapon
from spell import Spell
from utils import *
from fight import Fight
from magic_strings import *

class Dungeon:
    def __init__(self,file_name):
        self.validate_values(file_name)
        
        self.map = []
        self.file_name = file_name
        self.hero = None
        self.treasures = []
        self.spawn_x = 0
        self.spawn_y = 0

        with open(self.file_name) as file:
            for line in file.readlines():
                self.map.append(list(line))
        file.close()

        self.level_enemy = self.calculate_enemy_stats()

    def print_map(self):
        for list_elem in self.map:
            for elem in list_elem:
                print(elem,end="")
        print('\n')

    def spawn(self,hero):
        if not isinstance(hero,Hero):
            raise ValueError('You must spawn a Hero instance!')

        if self.hero is None:
            self.hero = hero

        flag_for_spawn = False

        n = len(self.map)
        m = len(self.map[0])
        for i in range(0,n):
            for j in range(0,m):
                if self.map[i][j] == '.':
                    self.map[i][j] = 'H'
                    self.spawn_y = i
                    self.spawn_x = j
                    flag_for_spawn = True
                    break
                elif flag_for_spawn == False:
                    continue
                else:
                    print('No more free spawning points')
                    return False

                if self.spawn_x < m-1:
                    self.spawn_x += 1 
                else:
                    self.spawn_x = 0
                    self.spawn_y += 1
                    flag_for_spawn = True
                    break
                
            if flag_for_spawn == True:
                self.hero.coordinate_y = i
                self.hero.coordinate_x = j
                return flag_for_spawn
                break

    def count_enemies(self):
        counter = 0
        for list_elem in self.map:
            for elem in list_elem:
                if elem == 'E':
                    counter += 1
        return counter

    def calculate_enemy_stats(self):
        counter = self.count_enemies()
        if counter == 0:
            counter = 1
        enemy_health = 100 // counter
        if enemy_health == 0:
            enemy_health = 10   
        enemy_damage = 30 // counter
        if enemy_damage == 0:
            enemy_damage = 5
        return Enemy(enemy_health,100,enemy_damage)

    def warn_player_when_casting_spell(self):
        print('If you cast your spell in that direction, you will enter a fight with an Enemy! Enemy stats are:')
        print(self.level_enemy)
        print('Do you want to engage in a fight? (y/n)\n') 
        player_input = input()
        while player_input != 'y' and player_input != 'n':
            print('Invalid choice! Choose again! (y/n)\n')
            player_input = input()
        return player_input

    def warn_player_when_walking(self):
        print('You are about to enter a fight with an Enemy! Enemy stats are:')
        print(self.level_enemy)
        print('Do you want to engage in a fight? (y/n)\n') 
        player_input = input()
        while player_input != 'y' and player_input != 'n':
            print('Invalid choice! Choose again! (y/n)\n')
            player_input = input()
        return player_input

    def regenerate_hero_mana(self):
        if self.hero.current_mana < self.hero.initial_mana:
            self.hero.take_mana(self.hero.mana_regeneration_rate)
    
    def move_and_regenerate(self,oldX,oldY,newX,newY):
        self.map[newY][newX] = 'H'
        self.map[oldY][oldX] = '.'
        self.hero.coordinate_x = newX
        self.hero.coordinate_y = newY
        self.regenerate_hero_mana()

    def move_hero(self,direction):
        if not isinstance(direction,str):
            raise ValueError('Wrong input - you must enter string!')
        
        if not direction in available_directions:
            raise ValueError('Incorrect value!')

        if not self.hero.is_alive():
            print('Your hero is dead. He cannot move.')
            return

        self.hero.direction = direction

        oldX = self.hero.coordinate_x
        oldY = self.hero.coordinate_y
        newX = self.hero.coordinate_x
        newY = self.hero.coordinate_y
        if direction == right:
            newX += 1
        elif direction == left:
            newX -= 1
        elif direction == up:
            newY -= 1
        else:
            newY += 1
        
        if newX >= len(self.map[0])-1 or newX < 0 or newY >= len(self.map) or newY < 0:
            print('Hero is on the edge of the map - you cannot go outside it!')
            return False
        elif self.map[newY][newX] == '#':
            print('There is an obstacle - you can not move there!')
            return False
        elif self.map[newY][newX] == 'T':
            print('You have found a treasure!',end=' ')
            hero_find_treasure(self.hero)
            self.move_and_regenerate(oldX,oldY,newX,newY)
            return True
        elif self.map[newY][newX] == '.':
            self.move_and_regenerate(oldX,oldY,newX,newY)
            return True
        elif self.map[newY][newX] == 'E':
            choice = self.warn_player_when_walking()
            if choice == 'n':
                return False
            else:
                fight = Fight(self.hero,self.level_enemy,['E'])
                outcome = fight.fight()
                if outcome == True:
                    self.move_and_regenerate(oldX,oldY,newX,newY)
                    return True
                else:
                    return False
        elif self.map[newY][newX] == 'G':
            print('Congratulations! You have completed the level!')
            return True

    def hero_attack(self,by=''):
        if by == weapon:
            print('Weapons can attack only enemies on your position')
            return False

        if by == spell and self.hero.can_cast():
            if self.hero.spell is None:
                print('You do not have a spell to attack by a spell!')
                return False
            if self.hero.direction == right:
                list_of_values = self.map[self.hero.coordinate_y][self.hero.coordinate_x+1:self.hero.coordinate_x+self.hero.spell.cast_range+1]
            elif self.hero.direction == left:
                if self.hero.coordinate_x-self.hero.spell.cast_range < 0:
                    newX = 0
                else:
                    newX = self.hero.coordinate_x-self.hero.spell.cast_range
                list_of_values = self.map[self.hero.coordinate_y][newX:self.hero.coordinate_x]
            elif self.hero.direction == up:
                new_map = transpose_matrix(self.map)
                if self.hero.coordinate_y-self.hero.spell.cast_range < 0:
                    newX = 0
                else:
                    newX = self.hero.coordinate_y-self.hero.spell.cast_range
                list_of_values = new_map[self.hero.coordinate_x][newX:self.hero.coordinate_y]
            else:
                new_map = transpose_matrix(self.map)
                list_of_values = new_map[self.hero.coordinate_x][self.hero.coordinate_y+1:self.hero.coordinate_y+self.hero.spell.cast_range+1]
            
            if self.hero.direction == up or self.hero.direction == left:
                list_of_values = list_of_values[::-1]
             
            if 'E' in list_of_values:
                index_of_enemy = list_of_values.index('E')
                if list_of_values[index_of_enemy-1] == '#':
                    print('Nothing to cast against your spell in that direction.')
                    return False

                choice = self.warn_player_when_casting_spell()
                if choice == 'n':
                    return False
                else:
                    fight = Fight(self.hero,self.level_enemy,list_of_values)
                    outcome = fight.fight()
                    if outcome == True:
                        return True
                    else:
                        return False
            else:
                print('Nothing in casting range '+str(self.hero.spell.cast_range))
        else:
            print("You don't have enough mana to cast that spell!")

    @staticmethod
    def validate_values(file_name):
        if not isinstance(file_name,str):
            raise ValueError('File name must be string!')

def main():
    pass
'''
    hero = Hero('Ivan','Hacker',30,40,5)
    hero.equip(Weapon(name='--Daggers--', damage=10))
    hero.learn(Spell(name='--Freezing spell--', damage=30, mana_cost=5, cast_range=2))
    dungeon = Dungeon('level3.txt')
    dungeon.print_map()
    dungeon.spawn(hero)
    dungeon.print_map()
    dungeon.move_hero(right)
    dungeon.print_map()
    dungeon.move_hero(down)'''

if __name__ == '__main__':
    main()