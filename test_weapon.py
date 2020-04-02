import unittest
from weapon import Weapon

class TestWeapon(unittest.TestCase):

	def test_raises_exception_when_name_of_weapon_is_not_string(self):
		exc = None

		try:
			weapon = Weapon(1,1)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Weapon name must be string!')

	def test_raises_exception_when_damage_of_weapon_is_not_int(self):
		exc = None

		try:
			weapon = Weapon('Kronx',12.3)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Damage must be int!')

	def test_str_method(self):
		weapon = Weapon('Ivan',20)

		result = str(weapon)
		expected = 'The weapon is Ivan and has 20 damage'

		self.assertEqual(result,expected)


if __name__ == '__main__':
	unittest.main()