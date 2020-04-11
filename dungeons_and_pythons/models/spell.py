class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.validate_values(name, damage, mana_cost, cast_range)

        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return f'The spell is {self.name} and deals {self.damage} damage, has {self.mana_cost} mana cost and {self.cast_range} cast range'

    def __eq__(self, other):
        return self.name == other.name and self.damage == other.damage and self.mana_cost == other.mana_cost and self.cast_range == other.cast_range

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_mana_cost(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range

    @staticmethod
    def validate_values(name, damage, mana_cost, cast_range):
        if not isinstance(name, str):
            raise ValueError('Name of spell must be string!')
        elif not isinstance(damage, int):
            raise ValueError('Damage of spell must be int!')
        elif not isinstance(mana_cost, int):
            raise ValueError('Mana cost of spell must be int!')
        elif not isinstance(cast_range, int):
            raise ValueError('Cast range of spell must be int!')
