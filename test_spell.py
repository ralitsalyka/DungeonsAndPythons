import unittest
from spell import Spell

class TestSpell(unittest.TestCase):

	def test_raises_exception_when_spell_name_is_not_string(self):
		exc = None

		try:
			spell = Spell(1,2,3,4)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Name of spell must be string!')

	def test_raises_exception_when_spell_damage_is_not_int(self):
		exc = None

		try:
			spell = Spell('fire',2.4,3,4)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Damage of spell must be int!')

	def test_raises_exception_when_spell_mana_cost_is_not_int(self):
		exc = None

		try:
			spell = Spell('fire',2,3.8,4)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Mana cost of spell must be int!')

	def test_raises_exception_when_spell_cast_range_is_not_string(self):
		exc = None

		try:
			spell = Spell('fir',2,3,4.7)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Cast range of spell must be int!')

	def test_str_dunder(self):
		spell = Spell('Fireball',20,5,3)

		expected = 'The spell is Fireball and has 20 damage, 5 mana cost and 3 cast range'
		result = str(spell)

		self.assertEqual(expected,result)



if __name__ == '__main__':
	unittest.main()