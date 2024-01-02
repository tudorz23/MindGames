import constants
import input_data
import numpy


class SudokuSample:
    def __init__(self, index):
        self.riddle = numpy.zeros((9, 9), int)
        self.solution = numpy.zeros((9, 9), int)
        self.index = index

    def load_sudoku(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                self.riddle[i][j] = input_data.input0[i][j]

    def print_sudoku(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                print(self.riddle[i][j])
            print()

