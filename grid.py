import numpy as np
import os


class Grid:
    def __init__(self, array):
        self.grid = array
        self._width = len(self.grid[0])

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

    def is_possible_in_row(self, row_id, number):
        return 0 in self.row(row_id) and not(number in self.row(row_id))

    def is_possible_in_column(self, column_id, number):
        return 0 in self.column(column_id) and not(number in self.column(column_id))

    def is_possible_in_cell(self, cell_id, number):
        return 0 in self.cell(cell_id).flatten() and not(number in self.cell(cell_id).flatten())

    def coordinate_to_cell(self, row, column):
        cell_size = int(np.sqrt(self._width))
        row_offset, column_offset = int(
            row//cell_size), int(column % cell_size)
        return row_offset * cell_size + column_offset

    def is_possible(self, row, column, number):
        return self.is_possible_in_row(row, number) and self.is_possible_in_column(column, number) and self.is_possible_in_cell(self.coordinate_to_cell(row, column), number)
