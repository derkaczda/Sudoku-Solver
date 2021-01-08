from blacklist import Blacklist
import numpy as np


class BackwardSolver():
    def __init__(self, board):
        self.board = board
        self.current_row = 0
        self.current_column = 0
        self.solved = False
        self.blacklist = Blacklist(self.board.width)
        self.step_backward = False
        self.max_index = -1
        self.set_next_possible_position()

    def step(self):
        sampled_value = self.sample_value()
        # best step just use sampled value
        if sampled_value is not None:
            self.board.set(self.current_row,
                           self.current_column, sampled_value)
            if self.board.solved():
                self.solved = True
                return
            self.set_next_possible_position(backward=False)
            if self.is_new_max_position():
                self.set_new_max_position()
                self.blacklist.clear_all()
        else:
            self.set_next_possible_position(backward=True)
            wrong_value = self.board.pop(self.current_row, self.current_column)
            self.blacklist.add(
                self.current_row, self.current_column, wrong_value)
            possible_values = self.board.possible_values(
                self.current_row, self.current_column)
            possible_values = self.blacklist.reduce(
                self.current_row, self.current_column, possible_values)
            while possible_values == []:
                self.blacklist.clear(self.current_row, self.current_column)
                self.set_next_possible_position(backward=True)
                wrong_value = self.board.pop(
                    self.current_row, self.current_column)
                self.blacklist.add(
                    self.current_row, self.current_column, wrong_value)
                possible_values = self.board.possible_values(
                    self.current_row, self.current_column)
                possible_values = self.blacklist.reduce(
                    self.current_row, self.current_column, possible_values)

    def solve(self):
        while not self.solved:
            self.step()

    def set_next_possible_position(self, backward=False):
        if backward:
            self.decrement_position()
        else:
            self.increment_position()
        fixed_value = self.board.is_fixed_value(
            self.current_row, self.current_column)
        if fixed_value:
            return self.set_next_possible_position(backward)
        else:
            return

    def is_new_max_position(self):
        index = self.current_row * self.board.width + self.current_column
        return index > self.max_index

    def set_new_max_position(self):
        self.max_index = self.current_row * self.board.width + self.current_column

    def sample_value(self):
        possible_values = self.board.possible_values(
            self.current_row, self.current_column)
        reduced_list = self.blacklist.reduce(
            self.current_row, self.current_column, possible_values)
        if reduced_list == []:
            return None
        return np.random.choice(reduced_list)

    def increment_position(self):
        if self.current_column + 1 >= self.board.width and self.current_row + 1 >= self.board.width:
            self.current_column = self.board.width - 1
            self.current_row = self.board.width - 1
        elif self.current_column + 1 >= self.board.width:
            self.current_column = 0
            self.current_row += 1
        else:
            self.current_column += 1

    def decrement_position(self):
        if self.current_column - 1 < 0:
            self.current_column = self.board.width - 1
            self.current_row -= 1
            if self.current_row < 0:
                self.current_row = 0
        else:
            self.current_column -= 1
            if self.current_column < 0:
                self.current_column = 0
