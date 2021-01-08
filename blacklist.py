import numpy as np


class Blacklist:
    def __init__(self, width):
        self.blacklist = {}
        self.width = width

    def add(self, row, column, value):
        key = self.get_key(row, column)
        if key not in self.blacklist:
            self.blacklist[key] = []
        self.blacklist[key].append(value)
#        self.blacklist[key] = value

    def clear_all(self):
        self.balcklist = {}

    def clear(self, row, column):
        self.blacklist[self.get_key(row, column)] = []

    def get_entry(self, row, column):
        key = self.get_key(row, column)
        if key not in self.blacklist:
            return []
        return self.blacklist[key]

    def reduce(self, row, column, other_list):
        key = self.get_key(row, column)
        if key not in self.blacklist:
            self.blacklist[key] = []
        blacked = self.blacklist[key]
        intersection = np.intersect1d(np.array(blacked), np.array(other_list))
        return [number for number in other_list if number not in intersection]

    def get_key(self, row, column):
        return row*self.width + column
