import constants
import database
import numpy
import random


class SudokuSample:
    def __init__(self):
        self.riddle = numpy.zeros((9, 9), int)
        self.solution = numpy.zeros((9, 9), int)
        self.unmodifiable = numpy.zeros((9, 9), bool)
        self.is_hint = numpy.zeros((9, 9), bool)

    def load_sudoku(self, level_nr):
        level_list = database.input_data[level_nr]
        index = random.randint(0, len(level_list) - 1)

        grid_source = level_list[index]

        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                self.riddle[i][j] = grid_source[i][j]
                if self.riddle[i][j] != 0:
                    self.unmodifiable[i][j] = True

        level_solution_list = database.solution[level_nr]
        solution_source = level_solution_list[index]

        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                self.solution[i][j] = solution_source[i][j]

    def print_sudoku(self):
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                print(self.riddle[i][j])
            print()

    def is_square_modifiable(self, row, column):
        return not self.unmodifiable[row][column]

    def get_color(self, row, column):
        if self.is_hint[row][column]:
            return 0, 200, 125
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

    def generate_hint(self, level):
        if level.hint_cnt == 0:
            return

        list = []
        for i in range(0, constants.ROWS_CNT):
            for j in range(0, constants.COLUMNS_CNT):
                if not self.unmodifiable[i][j] and self.riddle[i][j] == 0:
                    list.append((i, j))
        if len(list) == 0:
            return

        index = random.randint(0, len(list) - 1)
        (x, y) = list[index]
        self.riddle[x][y] = self.solution[x][y]
        self.unmodifiable[x][y] = True
        self.is_hint[x][y] = True

        level.hint_cnt -= 1

    def select_next_free_square(self, selected_row, selected_column, is_selected):
        x = 0
        y = -1
        if is_selected:
            x = selected_row
            y = selected_column

        y += 1
        if y == constants.COLUMNS_CNT:
            y = 0
            x += 1
            if x == constants.ROWS_CNT:
                x = 0

        while True:
            if self.is_square_modifiable(x, y):
                return x, y
            y += 1
            if y == constants.COLUMNS_CNT:
                y = 0
                x += 1
                if x == constants.ROWS_CNT:
                    x = 0
