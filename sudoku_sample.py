import constants
import input_data
import numpy
import square


class SudokuSample:
    def __init__(self, index):
        self.riddle = numpy.empty((9, 9)).tolist()
        self.solution = numpy.zeros((9, 9), int)
        self.index = index

    def load_sudoku(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                self.riddle[i][j] = square.Square(input_data.input0[i][j])
                if self.riddle[i][j].value != 0:
                    self.riddle[i][j].unmodifable_status = True

    def print_sudoku(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                print(self.riddle[i][j].value)
            print()

    def update_color(self, row, column):
        if not self.check_user_input_validity(row, column):
            self.riddle[row][column].color = (255, 0, 0)
        else:
            self.riddle[row][column].color = (0, 0, 255)


    # Checks if the digit introduced by the user collides with an existing
    # digit from the sudoku.
    def check_user_input_validity(self, row, column):
        value_to_check = self.riddle[row][column].value

        # Check if there are collisions on the row.
        for j in range(0, constants.COLUMNS_CNT):
            if column == j:
                continue
            if value_to_check == self.riddle[row][j].value:
                return False

        # Check if there are collisions on the column.
        for i in range(0, constants.ROWS_CNT):
            if row == i:
                continue
            if value_to_check == self.riddle[i][column].value:
                return False

        # Check if there are collisions in the 3x3 square.
        big_square_row = int(row / 3)
        big_square_column = int(column / 3)
        for i in range(0, constants.BIG_SQUARE_DIMENSION):
            curr_square_row = 3 * big_square_row + i
            for j in range(0, constants.BIG_SQUARE_DIMENSION):
                curr_square_column = 3 * big_square_column + j
                if (curr_square_row != row and curr_square_column != column
                        and self.riddle[curr_square_row][curr_square_column].value == value_to_check):
                    return False

        return True
