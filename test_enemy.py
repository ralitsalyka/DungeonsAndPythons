import unittest
from enemy import Enemy

class TestCharacterInitialization(unittest.TestCase):

    def test_init_if_it_is_working(self):
        enemy=Enemy(100,100,20)
        self.assertIsInstance(enemy, Enemy)

    def test_is_alive_function_work_for_class_Enemy(self):
        enemy=Enemy(100,100,20)
        self.assertTrue(enemy.is_alive())

    def test_get_health_if_it_is_working_for_default_value(self):
        enemy=Enemy(100,100,20)
        self.assertEqual(enemy.get_health(),100)

    def test_get_mana_if_it_is_working_for_default_value(self):
        enemy=Enemy(100,100,20)
        self.assertEqual(enemy.get_mana(),100)

    def test_get_damage_if_it_is_working_for_default_value(self):
        enemy=Enemy(100,100,20)
        self.assertEqual(enemy.get_damage(),20)

    def test_repr_method(self):
        enemy = Enemy(100,100,20)
        
        expected = 'Enemy: health = 100, mana = 100, damage = 20'
        result = repr(enemy)
        
        self.assertEqual(expected,result)

    def test_str_method(self):
        enemy = Enemy(100,100,20)
        
        expected = 'Health = 100, mana = 100, damage = 20'
        result = str(enemy)
        
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()