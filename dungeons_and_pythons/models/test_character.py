import unittest
from character import Character
from weapon import Weapon
from spell import Spell


class TestCharacterInitialization(unittest.TestCase):

    def test_raises_exception_when_health_is_not_of_int_type(self):
        exc = None

        try:
            character = Character('100', 35)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect value for health!')

    def test_raises_exception_when_mana_is_not_of_int_type(self):
        exc = None

        try:
            character = Character(100, 35.2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect value for mana!')

class TestCharacterMethods(unittest.TestCase):

    def test_checks_if_hero_is_alive_when_he_is_not(self):
        character = Character(0, 10)

        result = character.is_alive()
        expected = False

        self.assertTrue(result == expected, 'Values are equal')

    def test_checks_if_hero_is_alive_when_he_is(self):
        character = Character(10, 10)

        result = character.is_alive()
        expected = True

        self.assertTrue(result == expected, 'Values are equal')

    def test_get_health_method(self):
        character = Character(10, 10)

        result = character.get_health()
        expected = 10

        self.assertTrue(result == expected, 'Values are equal')

    def test_get_mana_method(self):
        character = Character(10, 10)

        result = character.get_mana()
        expected = 10

        self.assertTrue(result == expected, 'Values are equal')

    def test_take_damage_method(self):
        character = Character(10, 10)

        character.take_damage(5)
        result = character.get_health()
        expected = 5

        self.assertTrue(result == expected, 'Values are equal')

    def test_take_healing_method_when_health_is_fully_restored(self):
        character = Character(10, 10)

        character.take_damage(5)
        result_value = character.take_healing(5)
        result_health = character.get_health()
        expected_health = 10
        expected_value = True

        self.assertTrue(result_health == expected_health, 'Healths are equal')
        self.assertTrue(result_value == expected_value, 'Values are equal')

    def test_take_healing_method_when_health_is_not_fully_restored(self):
        character = Character(10, 10)

        character.take_damage(7)
        result_value = character.take_healing(5)
        result_health = character.get_health()
        expected_health = 8
        expected_value = True

        self.assertTrue(result_health == expected_health, 'Healths are equal')
        self.assertTrue(result_value == expected_value, 'Values are equal')

    def test_take_healing_method_when_health_is_zero(self):

        character = Character(0, 10)

        result_value = character.take_healing(5)
        result_health = character.get_health()
        expected_value = False
        expected_health = 0

        self.assertTrue(result_health == expected_health, 'Healths are equal')
        self.assertTrue(result_value == expected_value, 'Values are equal')

    def test_equip_method_raises_exception_when_weapon_is_of_wrong_type(self):
        exc = None
        character = Character(10, 10)

        try:
            character.equip(1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Wrong value - it must be of Weapon type!')

    def test_learn_method_raises_exception_when_spell_is_of_wrong_type(self):
        exc = None
        character = Character(10, 10)

        try:
            character.learn(1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Wrong value - it must be of Spell type!')

    def test_can_cast_fucntion_if_it_is_not_equal(self):
        character = Character(10, 10)
        result = character.can_cast()

        self.assertFalse(result)

    def test_can_cast_fucntion_if_it_is_equal(self):
        character = Character(10, 10)
        character.learn(Spell('BlackMagic', 20, 0, 0))
        result = character.can_cast()

        self.assertTrue(result)

    def test_attack_fucntion_if_it_is_working_for_spell(self):
        character = Character(10, 10)
        character.learn(Spell('BlackMagic', 20, 20, 20))
        result = character.attack('spell')

        self.assertEqual(result, 20)

    def test_attack_fucntion_if_it_is_working_for_weapon(self):
        character = Character(10, 10)
        character.equip(Weapon('Weapon', 20))
        result = character.attack('weapon')

        self.assertEqual(result, 20)

    def test_equip_method_if_it_is_working_for_weapon_with_higher_stats(self):
        character = Character(10, 10)
        character.equip(Weapon('Weapon', 20))
        character.equip(Weapon('Weapon', 50))
        result = character.attack('weapon')

        self.assertEqual(result, 50)

    def test_attack_fucntion_if_it_is_working_without_weapon_and_spell(self):
        character = Character(10, 10)
        character.equip(Weapon('Weapon', 20))
        result = character.attack('')

        self.assertEqual(result, 0)

    def test_take_mana_method_when_mana_is_not_fully_restored(self):
        character = Character(10, 10)
        character.current_mana = 2
        character.take_mana(5)

        self.assertEqual(character.get_mana(), 7)

    def test_take_mana_method_when_mana_is_fully_restored(self):
        character = Character(10, 10)
        character.current_mana = 7
        character.take_mana(5)

        self.assertEqual(character.get_mana(), 10)


if __name__ == '__main__':
    unittest.main()
