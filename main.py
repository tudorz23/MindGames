import pygame
import sudoku_sample
import constants
import button
import level

pygame.init()

# Title and icon
pygame.display.set_caption("Sudoku")
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

# Create the screen.
screen = pygame.display.set_mode((800, 800))
background = pygame.image.load('grid.jpg')
pygame.display.update()

# Level handler.
level = level.Level()

# Initialize the sudoku grid.
sudoku = sudoku_sample.SudokuSample()
sudoku.load_sudoku(level.value)

# Upper left digit.
digitX = constants.BACKGROUND_START_X + constants.DIGIT_OFFSET
digitY = constants.BACKGROUND_START_Y + constants.DIGIT_OFFSET

# Digit font.
font = pygame.font.Font("freesansbold.ttf", 30)

# Win message.
messageX = constants.WIN_MESSAGE_X
messageY = constants.WIN_MESSAGE_Y
win_message_font = pygame.font.Font("freesansbold.ttf", 20)
win_message = win_message_font.render("Congratulations! You can now access the next level:",
                                      True, constants.WHITE)

# Hint number.
hint_numberX = constants.BACKGROUND_DIMENSION - 100
hint_numberY = constants.HINT_Y
hint_font = pygame.font.Font("freesansbold.ttf", 40)


def display_hint_number(value):
    global screen
    hint_message = hint_font.render("Hints left: " + str(value), True, constants.PURPLE)
    pygame.draw.rect(screen, constants.BLACK, [hint_numberX, hint_numberY, 100, 50])
    screen.blit(hint_message, (hint_numberX, hint_numberY))


# Draw selection borders.
def draw_selection(row, column):
    global screen

    x = constants.BACKGROUND_START_X + column * constants.SQUARE_LEN
    y = constants.BACKGROUND_START_Y + row * constants.SQUARE_LEN
    pygame.draw.line(screen, constants.PURPLE, (x + 1, y + 1),
                     (x + constants.SQUARE_LEN - 2, y + 1), 2)
    pygame.draw.line(screen, constants.PURPLE, (x + 1, y + 1),
                     (x + 1, y + constants.SQUARE_LEN - 2), 2)
    pygame.draw.line(screen, constants.PURPLE, (x + constants.SQUARE_LEN - 2, y + 1),
                     (x + constants.SQUARE_LEN - 2, y + constants.SQUARE_LEN - 2), 2)
    pygame.draw.line(screen, constants.PURPLE, (x + 1, y + constants.SQUARE_LEN - 2),
                     (x + constants.SQUARE_LEN - 2, y + constants.SQUARE_LEN - 2), 2)


def show_sudoku(sudoku_input):
    global digitX
    global digitY
    global sudoku

    digitX = constants.BACKGROUND_START_X + constants.DIGIT_OFFSET
    digitY = constants.BACKGROUND_START_Y + constants.DIGIT_OFFSET

    for i in range(0, constants.ROWS_CNT):
        for j in range(0, constants.COLUMNS_CNT):
            if sudoku_input.riddle[i][j] != 0:
                color = sudoku.get_color(i, j)
                digit = font.render(str(sudoku_input.riddle[i][j]), True, color)
                screen.blit(digit, (digitX, digitY))

            digitX = digitX + constants.SQUARE_LEN

        digitX = constants.BACKGROUND_START_X + constants.DIGIT_OFFSET
        digitY += constants.SQUARE_LEN


# Returns the coordinates of the square clicked by the mouse.
def get_square(mouse_position):
    global sudoku
    if not (constants.BACKGROUND_START_X <= mouse_position[0]
            <= constants.BACKGROUND_START_X + constants.BACKGROUND_DIMENSION):
        return sudoku.select_next_free_square(0, -1, False)
    if not (constants.BACKGROUND_START_Y <= mouse_position[1]
            <= constants.BACKGROUND_START_Y + constants.BACKGROUND_DIMENSION):
        return sudoku.select_next_free_square(0, -1, False)

    x = int((mouse_position[1] - constants.BACKGROUND_START_Y) / constants.SQUARE_LEN)
    y = int((mouse_position[0] - constants.BACKGROUND_START_X) / constants.SQUARE_LEN)

    return x, y


def get_pressed_key(event):
    match event.key:
        case pygame.K_BACKSPACE:
            return 0
        case pygame.K_DELETE:
            return 0
        case pygame.K_1:
            return 1
        case pygame.K_2:
            return 2
        case pygame.K_3:
            return 3
        case pygame.K_4:
            return 4
        case pygame.K_5:
            return 5
        case pygame.K_6:
            return 6
        case pygame.K_7:
            return 7
        case pygame.K_8:
            return 8
        case pygame.K_9:
            return 9

    return -1


# Game Loop
has_won = False
running = True
is_square_selected = False

pressed_key = 0

# Selected square coordinates in sudoku matrix.
selected_row = 0
selected_column = 0

# Button for going to next level.
next_level_button = button.Button(350, 300, 120, 50, constants.PURPLE, "Next")

# Button for exit.
exit_button = button.Button(350, 400, 120, 50, constants.PURPLE, "Exit")
button_font = pygame.font.Font("freesansbold.ttf", 35)

# Hint button.
hint_button = button.Button(constants.BACKGROUND_START_X, constants.HINT_Y,
                            120, 50, constants.PURPLE, "Hint")

while running:
    screen.fill(constants.BLACK)
    while has_won:
        screen.fill(constants.BLACK)
        screen.blit(win_message, (messageX, messageY))
        next_level_button.draw(screen, button_font)
        exit_button.draw(screen, button_font)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()

                if next_level_button.mouse_is_on_button(mouse_position):
                    has_won = False
                    level.change_to_next_level()
                    sudoku = sudoku_sample.SudokuSample()
                    sudoku.load_sudoku(level.value)
                    screen.fill(constants.BLACK)

                if exit_button.mouse_is_on_button(mouse_position):
                    running = False
                    has_won = False

    if not running:
        continue

    screen.blit(background, (constants.BACKGROUND_START_X, constants.BACKGROUND_START_Y))
    show_sudoku(sudoku)
    hint_button.draw(screen, button_font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            if hint_button.mouse_is_on_button(mouse_position):
                sudoku.generate_hint(level)
                has_won = sudoku.check_winning()
            else:
                (selected_row, selected_column) = get_square(mouse_position)
                if 0 <= selected_row < constants.ROWS_CNT and 0 <= selected_column < constants.COLUMNS_CNT:
                    is_square_selected = True

        if (event.type == pygame.KEYDOWN and is_square_selected
                and sudoku.is_square_modifiable(selected_row, selected_column)):
            pressed_key = get_pressed_key(event)
            if 0 <= pressed_key <= 9:
                sudoku.riddle[selected_row][selected_column] = pressed_key

            if sudoku.check_user_input_validity(selected_row, selected_column):
                has_won = sudoku.check_winning()

        # Navigate with TAB.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            (selected_row, selected_column) = sudoku.select_next_free_square(selected_row,
                                                    selected_column, is_square_selected)
            is_square_selected = True

        # Navigate with left and right arrows.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            (selected_row, selected_column) = sudoku.select_next_free_square(selected_row,
                                                    selected_column, is_square_selected)
            is_square_selected = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            (selected_row, selected_column) = sudoku.select_prev_free_square(selected_row,
                                                    selected_column, is_square_selected)
            is_square_selected = True

    if sudoku.is_square_modifiable(selected_row, selected_column) and is_square_selected:
        draw_selection(selected_row, selected_column)
    display_hint_number(level.hint_cnt)
    pygame.display.update()
