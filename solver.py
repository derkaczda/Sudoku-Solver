
class BackwardSolver():
    def __init__(self, board):
        self.board = board
        self.current_row = 0
        self.current_column = 0

    def step(self):
        # got a fixed value and just increment the position and
        # go to the next step
        if self.board.is_fixed_value(self.current_row, self.current_column):
            self.increment_position()
            return

        possible_values = self.board.possible_values(
            self.current_row, self.current_column)
        if possible_values == []:
            # backtrack
            return
        else:
            # take first possible value
            self.board.set(self.current_row,
                           self.current_column, possible_values[0])
            self.increment_position()
            return

    def increment_position(self):
        if self.current_column + 1 >= self.board.width:
            self.current_column = 0
            self.current_row += 1
        else:
            self.current_column += 1
