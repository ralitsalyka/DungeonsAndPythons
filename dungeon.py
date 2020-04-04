from hero import Hero
from enemy import Enemy
available_directions = ['right','up','down','left']

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
                if i == self.spawn_y and j == self.spawn_x:
                    if self.map[i][j] == '.':
                        self.map[i][j] = 'H'
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
                elif i <= self.spawn_y and j <= self.spawn_x:
                    continue
                else:
                    print('No more free spawning points')
                    return False
            if flag_for_spawn == True:
                self.hero.current_y = i
                self.hero.current_x = j
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
        enemy_health = 100 // counter
        enemy_damage = 100 // counter
        print(Enemy(enemy_health,100,enemy_damage))
        return Enemy(enemy_health,100,enemy_damage)


    def warn_player(self):
        print('You are about to enter a fight with an Enemy! Enemy stats are:')
        print(self.level_enemy)
        print('Do you want to engage in a fight? (y/n)\n') 
        player_input = input()
        while player_input != 'y' and player_input != 'n':
            print('Invalid choice! Choose again! (y/n)\n')
            player_input = input()
        return player_input

    def move_hero(self,direction):
        if not isinstance(direction,str):
            raise ValueError('Wrong input - you must enter string!')
        
        if not direction in available_directions:
            raise ValueError('Incorrect value!')

        if not self.hero.is_alive():
            print('Your hero is dead. He cannot move.')
            return

        if direction == 'right':
            newX = self.hero.current_x + 1
            if newX > len(self.map[0]):
                print('Hero is on the edge of the map - you cannot go outside it!')
                return False
            elif self.map[self.hero.current_y][newX] == '#':
                print('There is an obstacle - you can not move there!')
                return False
            elif self.map[self.hero.current_y][newX] == 'T':
                print('You have found a treasure!')
                self.map[self.hero.current_y][newX] = 'H'
                self.map[self.hero.current_y][newX-1] = '.'
                self.hero.current_x += 1
                return True
            elif self.map[self.hero.current_y][newX] == '.':
                self.map[self.hero.current_y][newX] = 'H'
                self.map[self.hero.current_y][newX-1] = '.'
                self.hero.current_x += 1
                return True
            elif self.map[self.hero.current_y][newX] == 'E':
                choice = self.warn_player()
                if choice == 'n':
                    return False

        elif direction == 'left':
            newX = self.hero.current_x - 1
            if newX < 0:
                print('Hero is on the edge of the map - you cannot go outside it!')
                return False
            elif self.map[self.hero.current_y][newX] == '#':
                print('There is an obstacle - you can not move there!')
                return False
            elif self.map[self.hero.current_y][newX] == 'T':
                print('You have found a treasure!')
                self.map[self.hero.current_y][newX] = 'H'
                self.map[self.hero.current_y][newX+1] = '.'
                self.hero.current_x -= 1
                return True
            elif self.map[self.hero.current_y][newX] == '.':
                self.map[self.hero.current_y][newX] = 'H'
                self.map[self.hero.current_y][newX+1] = '.'
                self.hero.current_x -= 1
                return True
            elif self.map[self.hero.current_y][newX] == 'E':
                choice = self.warn_player()
                if choice == 'n':
                    return False

        elif direction == 'up':
            newY = self.hero.current_y - 1
            if newY < 0:
                print('Hero is on the edge of the map - you cannot go outside it!')
                return False
            elif self.map[newY][self.hero.current_x] == '#':
                print('There is an obstacle - you can not move there!')
                return False
            elif self.map[newY][self.hero.current_x] == 'T':
                print('You have found a treasure!')
                self.map[newY][self.hero.current_x] = 'H'
                self.map[newY+1][self.hero.current_x] = '.'
                self.hero.current_y -= 1
                return True
            elif self.map[newY][self.hero.current_x] == '.':
                self.map[newY][self.hero.current_x] = 'H'
                self.map[newY+1][self.hero.current_x] = '.'
                self.hero.current_y -= 1
                return True
            elif self.map[newY][self.hero.current_x] == 'E':
                choice = self.warn_player()
                if choice == 'n':
                    return False

        elif direction == 'down':
            newY = self.hero.current_y + 1
            if newY > len(self.map):
                print('Hero is on the edge of the map - you cannot go outside it!')
                return False
            elif self.map[newY][self.hero.current_x] == '#':
                print('There is an obstacle - you can not move there!')
                return False
            elif self.map[newY][self.hero.current_x] == 'T':
                print('You have found a treasure!')
                self.map[newY][self.hero.current_x] = 'H'
                self.map[newY-1][self.hero.current_x] = '.'
                self.hero.current_y += 1
                return True
            elif self.map[newY][self.hero.current_x] == '.':
                self.map[newY][self.hero.current_x] = 'H'
                self.map[newY-1][self.hero.current_x] = '.'
                self.hero.current_y += 1
                return True
            elif self.map[newY][self.hero.current_x] == 'E':
                choice = self.warn_player()
                if choice == 'n':
                    return False

    @staticmethod
    def validate_values(file_name):
        if not isinstance(file_name,str):
            raise ValueError('File name must be string!')

def main():
    hero = Hero('Ivan','Hacker',30,40,5)
    dungeon = Dungeon('level1.txt')
    dungeon.print_map()
    dungeon.spawn(hero)
    dungeon.print_map()
    dungeon.move_hero('right')
    dungeon.print_map()
    dungeon.move_hero('right')
    dungeon.print_map()
    dungeon.move_hero('down')
    dungeon.print_map()
    dungeon.move_hero('left')
    dungeon.move_hero('down')
    dungeon.move_hero('down')
    dungeon.print_map()
    dungeon.move_hero('right')
    dungeon.move_hero('down')
    
if __name__ == '__main__':
    main()