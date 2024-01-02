import pygame

import input_data
import sudoku_sample
import constants

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 800))

background = pygame.image.load('grid.jpg')

pygame.display.update()

sudoku = sudoku_sample.SudokuSample(0)
sudoku.load_sudoku()
sudoku.print_sudoku()

digitX = constants.BACKGROUND_START_X + constants.DIGIT_OFFSET
digitY = constants.BACKGROUND_START_Y + constants.DIGIT_OFFSET

font = pygame.font.Font("freesansbold.ttf", 30)


def show_sudoku(sudoku_input):
    global digitX
    global digitY

    digitX = constants.BACKGROUND_START_X + constants.DIGIT_OFFSET
    digitY = constants.BACKGROUND_START_Y + constants.DIGIT_OFFSET

    for i in range(0, constants.ROWS_CNT):
        for j in range(0, constants.COLUMNS_CNT):
            if sudoku_input.riddle[i][j] != 0:
                digit = font.render(str(sudoku_input.riddle[i][j]), True, (0, 0, 0))
                screen.blit(digit, (digitX, digitY))

            digitX = digitX + constants.SQUARE_LEN

        digitX = constants.BACKGROUND_START_X + constants.DIGIT_OFFSET
        digitY += constants.SQUARE_LEN


# Game Loop
running = True
while running:
    screen.blit(background, (constants.BACKGROUND_START_X, constants.BACKGROUND_START_Y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    show_sudoku(sudoku)

    pygame.display.update()
