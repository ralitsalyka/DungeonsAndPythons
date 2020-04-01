import unittest
from character import Character

class TestCharacterInitialization(unittest.TestCase):

    def test_raises_exception_when_health_is_not_of_float_type(self):
        exc = None

        try:
            character = Character('100',35)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect value for health!')

    def test_raises_exception_when_mana_is_not_of_float_type(self):
        exc = None

        try:
            character = Character(100,35.2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect value for mana!')

class TestCharacterMethods(unittest.TestCase):

    def test_checks_if_hero_is_alive_when_he_is_not(self):
        character = Character(0,10)

        result = character.is_alive()
        expected = False

        self.assertTrue(result == expected, 'Values are equal')

    def test_checks_if_hero_is_alive_when_he_is(self):
        character = Character(10,10)

        result = character.is_alive()
        expected = True

        self.assertTrue(result == expected, 'Values are equal')

    def test_get_health_method(self):
        character = Character(10,10)

        result = character.get_health()
        expected = 10

        self.assertTrue(result == expected, 'Values are equal')

    def test_get_mana_method(self):
        character = Character(10,10)

        result = character.get_mana()
        expected = 10

        self.assertTrue(result == expected, 'Values are equal')

    def test_take_damage_method(self):
        character = Character(10,10)

        character.take_damage(5)
        result = character.get_health()
        expected = 5

        self.assertTrue(result == expected, 'Values are equal')

    def test_take_healing_method_when_health_is_fully_restored(self):
        character = Character(10,10)

        character.take_damage(5)
        result_value = character.take_healing(5)
        result_health = character.get_health()
        expected_health = 10
        expected_value = True

        self.assertTrue(result_health == expected_health, 'Healths are equal')
        self.assertTrue(result_value == expected_value, 'Values are equal')

    def test_take_healing_method_when_health_is_not_fully_restored(self):
        character = Character(10,10)

        character.take_damage(7)
        result_value = character.take_healing(5)
        result_health = character.get_health()
        expected_health = 8
        expected_value = True

        self.assertTrue(result_health == expected_health, 'Healths are equal')
        self.assertTrue(result_value == expected_value, 'Values are equal')

    def test_take_healing_method_when_health_is_zero(self):

        character = Character(0,10)

        result_value = character.take_healing(5)
        result_health = character.get_health()
        expected_value = False
        expected_health = 0

        self.assertTrue(result_health == expected_health, 'Healths are equal')
        self.assertTrue(result_value == expected_value, 'Values are equal')

    

if __name__ == '__main__':
    unittest.main()