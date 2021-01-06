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
        print(
            f"row {row} row_end { row_end } column {column} column_end { column_end }")
        return self.grid[row:row_end, column:column_end]
