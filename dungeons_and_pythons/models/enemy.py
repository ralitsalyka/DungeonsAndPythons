from .character import Character


class Enemy(Character):
    def __init__(self, health, mana, damage):
        self.damage = damage
        super().__init__(health, mana)

    def get_damage(self):
        return self.damage

    def __repr__(self):
        return f'Enemy: health = {self.current_health}, mana = {self.current_mana}, damage = {self.damage}'

    def __str__(self):
        return f'Health = {self.current_health}, mana = {self.current_mana}, damage = {self.damage}'


def main():
    enemy = Enemy()
    print(enemy.get_health())
    print(enemy.get_mana())
    print(enemy.get_damage())


if __name__ == '__main__':
    main()
