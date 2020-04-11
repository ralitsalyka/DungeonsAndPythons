import unittest
from utils import transpose_matrix
class TestMatrixTransposition(unittest.TestCase):

    def test_matrix_transposition(self):
        matrix = [[1,3,5],[2,4,6]]

        expected = [[1,2],[3,4],[5,6]]
        result = transpose_matrix(matrix)

        self.assertTrue(expected == res)

if __name__ == '__main__':
    unittest.main()