class Character:
    def __init__(self,health,mana):
        self.validate_values(health,mana)
        
        self.__initial_health = health
        self.__initial_mana = mana
        self.__current_health = health
        self.__current_mana = mana
        self.weapon = None
        self.spell = None
        self.coordinate_x = None
        self.coordinate_y = None

    def equip(self,weapon):
        self.weapon = weapon

    def learn(self,spell):
        self.spell = spell

    def is_alive(self):
        if self.__current_health > 0:
            return True
        return False

    def get_health(self):
        return self.__current_health

    def get_mana(self):
        return self.__current_mana

    def can_cast(self):
        pass
    
    def attack():
        pass

    def take_damage(self,damage):
        if self.__current_health - damage <= 0:
            self.__current_health = 0
        else:
            self.__current_health -= damage

    def take_healing(self,healing):
        if self.__current_health == 0:
            print("The hero is dead. You can not heal dead heroes. Sad.")
            return False
        if self.__current_health + healing >= self.__initial_health:
            self.__current_health = self.__initial_health
            return True
        else:
            self.__current_health += healing
            return True

    def take_mana(self,mana_points):
        pass

    @staticmethod
    def validate_values(health,mana):
        if not isinstance(health,int):
            raise ValueError('Incorrect value for health!')
        elif not isinstance(mana,int):
            raise ValueError('Incorrect value for mana!')