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

    grid = Grid(test_grid)

    def test_from_file(self):
        grid = Grid.from_file("test.board")
        target = self.test_grid
        self.assertTrue(np.array_equal(grid.grid, target))

    def test_select_row_one(self):
        row = self.grid.row(0)
        target = [1, 3, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(np.array_equal(row, target))

    def test_select_row_seven(self):
        row = self.grid.row(6)
        target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertTrue(np.array_equal(row, target))

    def test_select_column_one(self):
        column = self.grid.column(0)
        target = [1, 0, 1, 1, 1, 1, 1, 1, 1]
        self.assertTrue(np.array_equal(column, target))

    def test_select_column_four(self):
        column = self.grid.column(3)
        target = [4, 0, 9, 4, 4, 4, 4, 4, 4]
        self.assertTrue(np.array_equal(column, target))

    def test_select_cell_one(self):
        cell = self.grid.cell(0).flatten()
        target = [1, 3, 3, 0, 0, 0, 1, 2, 3]
        self.assertTrue(np.array_equal(cell, target))

    def test_select_cell_five(self):
        cell = self.grid.cell(4).flatten()
        target = [4, 5, 6, 4, 5, 6, 4, 5, 6]
        self.assertTrue(np.array_equal(cell, target))

    def test_is_two_possible_in_row_two(self):
        result = self.grid.is_possible_in_row(1, 2)
        self.assertTrue(result)

    def test_is_two_possible_in_row_three(self):
        result = self.grid.is_possible_in_row(2, 2)
        self.assertFalse(result)

    def test_is_two_possible_in_column_nine(self):
        result = self.grid.is_possible_in_column(8, 2)
        self.assertTrue(result)

    def test_is_nine_possible_in_column_nine(self):
        result = self.grid.is_possible_in_column(8, 9)
        self.assertFalse(result)

    def test_is_nine_possible_in_cell_two(self):
        result = self.grid.is_possible_in_cell(1, 9)
        self.assertFalse(result)

    def test_is_nine_possible_in_cell_one(self):
        result = self.grid.is_possible_in_cell(0, 9)
        self.assertTrue(result)

    def test_is_nine_possible_in_cell_seven(self):
        result = self.grid.is_possible_in_cell(6, 9)
        self.assertFalse(result)

    def test_is_four_possible_at_two_four(self):
        result = self.grid.is_possible(1, 3, 4)
        self.assertFalse(result)

    def test_is_three_possible_at_two_four(self):
        result = self.grid.is_possible(1, 3, 3)
        self.assertTrue(result)

    def test_two_four_is_grid_cell_two(self):
        result = self.grid.coordinate_to_cell(1, 3)
        self.assertEqual(1, result)

    def test_eight_eight_is_grid_cell_nine(self):
        result = self.grid.coordinate_to_cell(8, 8)
        self.assertEqual(8, result)

    def test_five_nine_is_grid_cell_six(self):
        result = self.grid.coordinate_to_cell(4, 8)
        self.assertEqual(5, result)


if __name__ == "__main__":
    unittest.main()
