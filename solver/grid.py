import numpy as np
import os
from functools import reduce


class Grid:
    def __init__(self, array):
        self.grid = array
        self._width = len(self.grid[0])
        self.start_grid = self.grid.copy()

    @staticmethod
    def from_file(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            content = content.strip().split('\n')
            grid = []
            for line in content:
                grid.append(np.fromstring(line, dtype=int, sep=','))
            grid = np.array(grid)
        return Grid(grid)

    @property
    def width(self):
        return self._width

    def set(self, row, column, value):
        self.grid[row, column] = value

    def pop(self, row, column):
        result = self.grid[row, column]
        self.grid[row, column] = 0
        return result

    def row(self, id):
        return self.grid[id]

    def column(self, id):
        return self.grid[:, id]

    def cell(self, id):
        cell_size = np.sqrt(self._width)
        row_offset = int(id // cell_size)
        column_offset = int(id % cell_size)
        row = int(cell_size * row_offset)
        row_end = int(row + cell_size)
        column = int(cell_size * column_offset)
        column_end = int(column + cell_size)
        return self.grid[row:row_end, column:column_end]

    def sum_of_values(self):
        # small gauss
        return (self._width ** 2 + self._width) / 2

    def is_fixed_value(self, row, column):
        return self.start_grid[row, column] != 0

    def coordinate_to_cell(self, row, column):
        cell_size = int(np.sqrt(self._width))
        row_offset, column_offset = int(
            row//cell_size), int(column // cell_size)
        return row_offset * cell_size + column_offset


    def possible_values(self, row, column):
        if self.is_fixed_value(row, column):
            return np.array([])
        else:
            row_values = self.row(row)
            column_values = self.column(column)
            cell_values = self.cell(self.coordinate_to_cell(row,column))
            values = reduce(np.union1d, (row_values, column_values, cell_values))
            return np.setdiff1d(np.arange(1, self._width+1), values)

    def show(self):
        print(self.grid)

    def solved(self):
        return 0 not in self.grid.flatten()
