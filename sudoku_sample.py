import constants
import database
import numpy


class SudokuSample:
    def __init__(self, index):
        self.riddle = numpy.zeros((9, 9), int)
        self.solution = numpy.zeros((9, 9), int)
        self.unmodifiable = numpy.zeros((9, 9), bool)
        self.index = index

    def load_sudoku(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                self.riddle[i][j] = database.input0[i][j]
                if self.riddle[i][j] != 0:
                    self.unmodifiable[i][j] = True

    def print_sudoku(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                print(self.riddle[i][j])
            print()

    def is_square_modifiable(self, row, column):
        return not self.unmodifiable[row][column]

    def get_color(self, row, column):
        if self.unmodifiable[row][column]:
            return 0, 0, 0

        if self.check_user_input_validity(row, column):
            return 0, 0, 255

        return 255, 0, 0

    # Checks if the digit introduced by the user collides with an existing
    # digit from the sudoku.
    def check_user_input_validity(self, row, column):
        value = self.riddle[row][column]

        # Check if there are collisions on the row.
        for j in range(0, constants.COLUMNS_CNT):
            if column == j:
                continue
            if value == self.riddle[row][j]:
                return False

        # Check if there are collisions on the column.
        for i in range(0, constants.ROWS_CNT):
            if row == i:
                continue
            if value == self.riddle[i][column]:
                return False

        # Check if there are collisions in the 3x3 square.
        big_square_row = int(row / 3)
        big_square_column = int(column / 3)
        for i in range(0, constants.BIG_SQUARE_DIMENSION):
            curr_square_row = 3 * big_square_row + i
            for j in range(0, constants.BIG_SQUARE_DIMENSION):
                curr_square_column = 3 * big_square_column + j
                if (curr_square_row != row and curr_square_column != column
                        and self.riddle[curr_square_row][curr_square_column] == value):
                    return False

        return True

    def check_winning(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                if self.riddle[i][j] == 0:
                    return False

        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                if not self.check_user_input_validity(i, j):
                    return False
        return True
