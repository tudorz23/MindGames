import constants
import input_data
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
                self.riddle[i][j] = input_data.input0[i][j]
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
        if not self.unmodifiable[row][column]:
            return 0, 0, 255

        return 0, 0, 0
