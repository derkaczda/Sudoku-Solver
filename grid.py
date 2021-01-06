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
