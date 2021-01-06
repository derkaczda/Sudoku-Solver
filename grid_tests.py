import unittest
import numpy as np
from grid import Grid


class TestGridLoading(unittest.TestCase):
    def test_from_file(self):
        target = np.array([
            [1, 3, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 9, 1, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])

        grid = Grid.from_file("test.board")
        self.assertTrue(np.array_equal(grid.grid, target))


if __name__ == "__main__":
    unittest.main()
