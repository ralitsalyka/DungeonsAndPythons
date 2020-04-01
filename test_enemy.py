import unittest
from enemy import Enemy

class TestCharacterInitialization(unittest.TestCase):

    def test_init_if_it_is_working(self):
        enemy=Enemy()
        self.assertIsInstance(enemy, Enemy)

    def test_is_alive_function_work_for_class_Enemy(self):
        enemy=Enemy()
        self.assertTrue(enemy.is_alive())

    def test_get_health_if_it_is_working_for_default_value(self):
        enemy=Enemy()
        self.assertEqual(enemy.get_health(),100)

    def test_get_mana_if_it_is_working_for_default_value(self):
        enemy=Enemy()
        self.assertEqual(enemy.get_mana(),100)

    def test_get_damage_if_it_is_working_for_default_value(self):
        enemy=Enemy()
        self.assertEqual(enemy.get_damage(),20)



if __name__ == '__main__':
    unittest.main()