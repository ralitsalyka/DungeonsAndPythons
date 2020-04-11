import unittest
from dungeon import Dungeon
from hero import Hero


class TestDungeonInitialization(unittest.TestCase):

    def test_raises_exception_when_file_name_is_not_string(self):
        exc = None

        try:
            dungeon = Dungeon(12)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'File name must be string!')

class TestDungeonSpawningHero(unittest.TestCase):

    def test_raises_exception_when_spawning_wrong_variable(self):
        exc = None
        dungeon = Dungeon('level1.txt')

        try:
            dungeon.spawn(1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'You must spawn a Hero instance!')

    def test_spawns_hero_on_first_available_position(self):

        hero = Hero('Ivan', 'Hacker', 30, 40, 5)
        dungeon = Dungeon('level1.txt')
        expected = True

        result = dungeon.spawn(hero)

        self.assertEqual(expected, result)
        self.assertTrue(dungeon.map[0][0] == 'H')


class TestDungeonMovingHero(unittest.TestCase):

    def test_raises_exception_when_direction_is_not_string(self):
        exc = None
        dungeon = Dungeon('level1.txt')

        try:
            dungeon.move_hero(1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Wrong input - you must enter string!')

    def test_raises_exception_when_direction_is_incorrect(self):
        exc = None
        dungeon = Dungeon('level1.txt')

        try:
            dungeon.move_hero('nagore')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect value!')

    def test_trying_to_move_dead_hero(self):
        hero = Hero('Ivan', 'Hacker', 0, 0, 5)
        dungeon = Dungeon('level1.txt')
        dungeon.spawn(hero)
        expected = None

        result = dungeon.move_hero('up')

        self.assertEqual(expected, result)

    def test_trying_to_move_hero_in_starting_position_up(self):
        hero = Hero('Ivan', 'Hacker', 20, 20, 5)
        dungeon = Dungeon('level1.txt')
        dungeon.spawn(hero)

        expected = False
        result = dungeon.move_hero('up')

        self.assertEqual(expected, result)

    def test_trying_to_move_hero_in_starting_position_left(self):
        hero = Hero('Ivan', 'Hacker', 20, 20, 5)
        dungeon = Dungeon('level1.txt')
        dungeon.spawn(hero)

        expected = False
        result = dungeon.move_hero('left')

        self.assertEqual(expected, result)

    def test_trying_to_move_hero_in_starting_position_down(self):
        hero = Hero('Ivan', 'Hacker', 20, 20, 5)
        dungeon = Dungeon('level1.txt')
        dungeon.spawn(hero)

        expected = False
        result = dungeon.move_hero('down')

        self.assertEqual(expected, result)

    def test_trying_to_move_hero_in_starting_position_right(self):
        hero = Hero('Ivan', 'Hacker', 20, 20, 5)
        dungeon = Dungeon('level1.txt')
        dungeon.spawn(hero)

        expected = True
        result = dungeon.move_hero('right')

        self.assertEqual(expected, result)

    def test_trying_to_move_hero_in_starting_position_two_times_right(self):
        hero = Hero('Ivan', 'Hacker', 20, 20, 5)
        dungeon = Dungeon('level1.txt')
        dungeon.spawn(hero)

        expected = False
        result = dungeon.move_hero('right')
        result = dungeon.move_hero('right')

        self.assertEqual(expected, result)

    def test_trying_to_move_hero_to_a_place_with_treasure(self):
        hero = Hero('Ivan', 'Hacker', 20, 20, 5)
        dungeon = Dungeon('level1.txt')
        dungeon.spawn(hero)

        expected = True
        result = dungeon.move_hero('right')
        result = dungeon.move_hero('down')

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
