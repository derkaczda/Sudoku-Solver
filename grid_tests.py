import unittest
import numpy as np
from grid import Grid


class TestGrid(unittest.TestCase):
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

    def test_two_four_is_grid_cell_two(self):
        result = self.grid.coordinate_to_cell(1, 3)
        self.assertEqual(1, result)

    def test_eight_eight_is_grid_cell_nine(self):
        result = self.grid.coordinate_to_cell(8, 8)
        self.assertEqual(8, result)

    def test_five_nine_is_grid_cell_six(self):
        result = self.grid.coordinate_to_cell(4, 8)
        self.assertEqual(5, result)

    test_grid_two = np.array([
        [2, 0, 4, 0, 7, 0, 0, 3, 5],
        [8, 9, 0, 0, 1, 4, 0, 7, 0],
        [0, 5, 7, 8, 0, 0, 0, 0, 4],
        [1, 8, 0, 3, 0, 0, 5, 0, 2],
        [0, 2, 0, 0, 0, 0, 0, 4, 0],
        [4, 0, 5, 0, 0, 9, 0, 8, 7],
        [9, 0, 0, 0, 0, 5, 3, 6, 0],
        [0, 6, 0, 4, 8, 0, 0, 5, 9],
        [5, 7, 0, 0, 9, 0, 4, 0, 1]
    ])

    grid_two = Grid(test_grid_two)

    def test_grid_two_possible_values_for_one_two(self):
        result = self.grid_two.possible_values(0, 1)
        target = np.array([1])
        self.assertTrue(np.array_equal(target, result))

    def test_grid_two_possible_values_for_nine_eight(self):
        result = self.grid_two.possible_values(8, 7)
        target = np.array([2])
        self.assertTrue(np.array_equal(target, result))

    def test_grid_two_possible_values_five_five(self):
        result = self.grid_two.possible_values(4, 4)
        target = np.array([5, 6])
        self.assertTrue(np.array_equal(target, result))

    def test_grid_two_one_one_is_fixed_vale(self):
        result = self.grid_two.is_fixed_value(0, 0)
        self.assertTrue(result)

    def test_grid_two_one_two_is_fixed_value(self):
        result = self.grid_two.is_fixed_value(0, 1)
        self.assertFalse(result)

    def test_grid_two_get_possible_values_one_one(self):
        result = self.grid_two.possible_values(0, 0)
        target = np.array([])
        self.assertTrue(np.array_equal(target, result))

    def test_grid_two_set_value_at_one_two(self):
        self.grid_two.set(0, 1, 1)
        target = np.array([
            [2, 1, 4, 0, 7, 0, 0, 3, 5],
            [8, 9, 0, 0, 1, 4, 0, 7, 0],
            [0, 5, 7, 8, 0, 0, 0, 0, 4],
            [1, 8, 0, 3, 0, 0, 5, 0, 2],
            [0, 2, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 5, 0, 0, 9, 0, 8, 7],
            [9, 0, 0, 0, 0, 5, 3, 6, 0],
            [0, 6, 0, 4, 8, 0, 0, 5, 9],
            [5, 7, 0, 0, 9, 0, 4, 0, 1]
        ])
        self.assertTrue(np.array_equal(target, self.grid_two.grid))


if __name__ == "__main__":
    unittest.main()
