class Weapon:
    def __init__(self,name,damage):
        self.validate_values(name,damage)

        self.name = name
        self.damage = damage

    def __str__(self):
        return f'The weapon is {self.name} and has {self.damage} damage'

    def __eq__(self,other):
        return self.name == other.name and self.damage == other.damage

    def get_damage(self):
        return self.damage

    @staticmethod
    def validate_values(name,damage):
        if not isinstance(name,str):
            raise ValueError('Weapon name must be string!')
        elif not isinstance(damage,int):
            raise ValueError('Damage must be int!')