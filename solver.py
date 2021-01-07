from blacklist import Blacklist
import numpy as np


class BackwardSolver():
    def __init__(self, board):
        self.board = board
        self.current_row = 0
        self.current_column = 0
        self.solved = False
        self.stop = False
        self.blacklist = Blacklist(self.board.width)

    def step(self):
        is_fixed_value = self.board.is_fixed_value(
            self.current_row, self.current_column)
        # got a fixed value and just increment the position and
        if is_fixed_value:
            print(
                f"fixed value at {self.current_row}, {self.current_column}. skipping.")
            self.increment_position()
            self.check_for_solved()
            return

        sampled_value = self.sample_value()
        if sampled_value is None:
            # backtrack
            print(
                f"this is not correct. at position {self.current_row}, {self.current_column}")
            self.decrement_position()
            fixed = self.board.is_fixed_value(
                self.current_row, self.current_column)
#            self.board.print()
            while fixed:
                self.decrement_position()
                fixed = self.board.is_fixed_value(
                    self.current_row, self.current_column)

            wrong_value = self.board.pop(self.current_row, self.current_column)
            self.blacklist.add(
                self.current_row, self.current_column, wrong_value)
            print(
                f"corrected state removed {wrong_value} at {self.current_row}, {self.current_column}")
#            self.board.print()
#            self.stop = True

        else:
            # take first possible value
            print(
                f"on blacklist {self.blacklist.get_entry(self.current_row, self.current_column)}")
            print(
                f"setting value {sampled_value} at {self.current_row}, {self.current_column}")
            self.board.set(self.current_row,
                           self.current_column, sampled_value)
            self.increment_position()
            self.check_for_solved()

    def solve(self):
        while not self.solved and not self.stop:
            self.step()

    def sample_value(self):
        possible_values = self.board.possible_values(
            self.current_row, self.current_column)
        reduced_list = self.blacklist.reduce(
            self.current_row, self.current_column, possible_values)
        print(f"possible values {reduced_list}")
        if reduced_list == []:
            return None
        return np.random.choice(reduced_list)

    def increment_position(self):
        if self.current_column + 1 >= self.board.width:
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

    def check_for_solved(self):
        if self.current_row == self.board.width-1 and self.current_column == self.board.width-1:
            self.solved = True
