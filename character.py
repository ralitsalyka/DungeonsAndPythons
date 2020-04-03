from weapon import Weapon
from spell import Spell

class Character:
    def __init__(self,health,mana):
        self.validate_values(health,mana)
        
        self.initial_health = health
        self.initial_mana = mana
        self.current_health = health
        self.current_mana = mana
        self.attack_points=0
        self.weapon = None
        self.spell = None
        self.coordinate_x = None
        self.coordinate_y = None

    def equip(self,weapon):
        if not isinstance(weapon,Weapon):
            raise ValueError('Wrong value - it must be of Weapon type!')
        elif self.weapon is None:
            self.weapon = weapon
        elif self.weapon == weapon:
            print('You have already equipped this weapon')
            return

    def learn(self,spell):
        if not isinstance(spell,Spell):
            raise ValueError('Wrong value - it must be of Spell type!')
        elif self.spell is None:
            self.spell = spell
        elif self.spell == spell:
            print('You have already learned this spell')
            return

    def is_alive(self):
        if self.current_health > 0:
            return True
        return False

    def get_health(self):
        return self.current_health

    def get_mana(self):
        return self.current_mana

    def can_cast(self):
        if self.spell is not None:
            return self.current_mana>=self.spell.get_mana_cost()
        else:
            return False
    
    def attack(self, by=''):
        if by == 'weapon':
            if self.weapon.get_damage()!=0:
                return self.weapon.get_damage()
            else:
                return self.attack_points
        elif by == 'spell':
            if self.spell.get_damage() !=0:
                self.current_mana -= self.spell.get_mana_cost()
                return self.spell.get_damage()
            else:
                return self.attack_points
        else:
            return self.attack_points

    def take_damage(self,damage):
        if self.current_health - damage <= 0:
            self.current_health = 0
        else:
            self.current_health -= damage

    def take_healing(self,healing):
        if self.current_health == 0:
            print("The hero is dead. You can not heal dead heroes. Sad.")
            return False
        if self.current_health + healing >= self.initial_health:
            self.current_health = self.initial_health
            return True
        else:
            self.current_health += healing
            return True

    def take_mana(self,mana_points):
        if self.current_mana + mana_points > self.initial_mana:
            self.current_mana = self.initial_mana
        else:
            self.current_mana += mana_points

    @staticmethod
    def validate_values(health,mana):
        if not isinstance(health,int):
            raise ValueError('Incorrect value for health!')
        elif not isinstance(mana,int):
            raise ValueError('Incorrect value for mana!')