import unittest
import numpy as np
from grid import Grid


class TestGridLoading(unittest.TestCase):
    test_grid = np.array([
        [1, 3, 3, 4, 5, 6, 7, 8, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 3, 9, 1, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ])

    def test_from_file(self):
        grid = Grid.from_file("test.board")
        target = self.test_grid
        self.assertTrue(np.array_equal(grid.grid, target))

    def test_select_row_one(self):
        grid = Grid(self.test_grid)
        row = grid.row(0)
        target = [1, 3, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(np.array_equal(row, target))

    def test_select_row_seven(self):
        grid = Grid(self.test_grid)
        row = grid.row(6)
        target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertTrue(np.array_equal(row, target))

    def test_select_column_one(self):
        grid = Grid(self.test_grid)
        column = grid.column(0)
        target = [1, 0, 1, 1, 1, 1, 1, 1, 1]
        self.assertTrue(np.array_equal(column, target))

    def test_select_column_four(self):
        grid = Grid(self.test_grid)
        column = grid.column(3)
        target = [4, 0, 9, 4, 4, 4, 4, 4, 4]
        self.assertTrue(np.array_equal(column, target))

    def test_select_cell_one(self):
        grid = Grid(self.test_grid)
        cell = grid.cell(0).flatten()
        target = [1, 3, 3, 0, 0, 0, 1, 2, 3]
        self.assertTrue(np.array_equal(cell, target))

    def test_select_cell_five(self):
        grid = Grid(self.test_grid)
        cell = grid.cell(4).flatten()
        target = [4, 5, 6, 4, 5, 6, 4, 5, 6]
        self.assertTrue(np.array_equal(cell, target))


if __name__ == "__main__":
    unittest.main()
