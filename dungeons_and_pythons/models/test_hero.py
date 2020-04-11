import unittest
from hero import Hero

class TestHeroInitialization(unittest.TestCase):

	def test_raises_exception_when_hero_name_is_not_string(self):
		exc = None

		try:
			hero = Hero(1,2,3,4,5)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Name of Hero must be string!')

	def test_raises_exception_when_hero_title_is_not_string(self):
		exc = None

		try:
			hero = Hero('Ivan',2,3,4,5)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Title of Hero must be string!')

	def test_raise_exception_when_hero_mana_regeneration_is_not_int(self):
		exc = None

		try:
			hero = Hero('Ivan','Hacker',3,4,5.2)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Mana regeneration of Hero must be int!')

class TestHeroMethods(unittest.TestCase):

	def test_known_as_method(self):
		hero = Hero('Ivan','Hacker',30,40,5)

		expected = 'Ivan the Hacker'
		result = hero.known_as()

		self.assertEqual(expected,result)

if __name__ == '__main__':
	unittest.main()