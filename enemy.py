from character import Character

class Enemy(Character):
    def __init__(self,health=100, mana=100, damage=20):
        self.damage=damage
        super().__init__(health,mana)


    def get_damage(self):
        return self.damage


def main():
    enemy=Enemy()
    print(enemy.get_health())
    print(enemy.get_mana())
    print(enemy.get_damage())

if __name__=='__main__':
    main()