from blacklist import Blacklist
import numpy as np


class BackwardSolver():
    def __init__(self, board):
        self.board = board
        self.current_row = 0
        self.last_correct_row = 0
        self.current_column = 0
        self.last_correct_column = 0
        self.solved = False
        self.stop = False
        self.blacklist = Blacklist(self.board.width)
        self.step_backward = False
        self.row_to_solve = -1
        self.column_to_solve = -1
        self.set_next_possible_position()

    def step(self):
        sampled_value = self.sample_value()
        # best step just use sampled value
        if sampled_value is not None:
            print(
                f"setting {sampled_value} at position {self.current_row}, {self.current_column}")
            self.board.set(self.current_row,
                           self.current_column, sampled_value)
            self.last_correct_row, self.last_correct_column = self.get_position()
            self.set_next_possible_position(backward=False)
            if self.row_to_solve != -1:
                index_to_solve = self.row_to_solve * self.board.width + self.column_to_solve
                current_index = self.current_row * self.board.width + self.current_column
                if current_index > index_to_solve:
                    self.row_to_solve = self.column_to_solve = -1
                    self.blacklist.clear()
        else:
            print(
                f"no possible value at {self.current_row}, {self.current_column}. Going back to {self.last_correct_row}, {self.last_correct_column}")
            if self.row_to_solve == -1:
                self.row_to_solve = self.current_row
                self.column_to_solve = self.current_column
            self.set_to_last_correct_position()
            false_value = self.board.pop(self.current_row, self.current_column)
            self.blacklist.add(
                self.current_row, self.current_column, false_value)
            # any option left after blacklisting?
            possible_values = self.blacklist.reduce(self.current_row, self.current_column,
                                                    self.board.possible_values(
                                                        self.current_row, self.current_column))
            possible_values = self.blacklist.reduce(
                self.current_row, self.current_column, possible_values)
            while (possible_values == []):
                self.set_next_possible_position(backward=True)
                print(
                    f"after blacklist no possible value. go back to {self.current_row}, {self.current_column}")
                false_value = self.board.pop(
                    self.current_row, self.current_column)
                self.blacklist.add(
                    self.current_row, self.current_column, false_value)
                possible_values = self.blacklist.reduce(self.current_row, self.current_column,
                                                        self.board.possible_values(
                                                            self.current_row, self.current_column))
                self.last_correct_row, self.last_correct_column = self.get_position()

    def solve(self):
        while not self.solved and not self.stop:
            self.step()

    def forward(self):
        is_fixed_value = self.board(self.current_row, self.current_column)
        if is_fixed_value:
            print(
                f"fixed value at {self.current_row}, {self.current_column}. skipping.")
            self.increment_position()
            self.check_for_solved()
            return
        sampled_value = self.sample_value()
        if sampled_value is None:
            print(
                f"this is not correct at position {self.current_row}, {self.current_column}")
            self.step_backward = True
            self.set_to_last_correct_position()

    def get_position(self):
        return self.current_row, self.current_column

    def set_to_last_correct_position(self):
        self.current_row = self.last_correct_row
        self.current_column = self.last_correct_column

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

    def sample_value(self):
        possible_values = self.board.possible_values(
            self.current_row, self.current_column)
        reduced_list = self.blacklist.reduce(
            self.current_row, self.current_column, possible_values)
        print(f"possible values {reduced_list}")
        if reduced_list == []:
            return None
        return np.random.choice(reduced_list)

    def reduce(self, possible_values):
        intersection = np.intersect1d(
            np.array(self.blacklist), np.array(possible_values))
        return [number for number in possible_values if number not in intersection]

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
