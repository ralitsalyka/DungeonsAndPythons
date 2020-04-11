from .character import Character


class Hero(Character):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.validate_values_of_hero(name, title, mana_regeneration_rate)

        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.direction = ''
        super().__init__(health, mana)

    def known_as(self):
        return f'{self.name} the {self.title}'

    def __str__(self):
        return f'Health = {self.current_health}\nMana = {self.current_mana}\nMana regeneration rate = {self.mana_regeneration_rate}\nWeapon: {self.weapon}\nSpell: {self.spell}'

    @staticmethod
    def validate_values_of_hero(name, title, mana_regeneration_rate):
        if not isinstance(name, str):
            raise ValueError('Name of Hero must be string!')
        elif not isinstance(title, str):
            raise ValueError('Title of Hero must be string!')
        elif not isinstance(mana_regeneration_rate, int):
            raise ValueError('Mana regeneration of Hero must be int!')
