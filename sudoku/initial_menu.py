import pygame
import button
import constants


class InitialMenu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        self.play_button = button.Button(80, 300, 120, 50, constants.PURPLE, "Play")
        self.exit_button = button.Button(300, 300, 120, 50, constants.PURPLE, "Exit")
        self.main_menu_button = button.Button(520, 300, 200, 50, constants.PURPLE, "Main Menu")
        self.button_font = pygame.font.Font("freesansbold.ttf", 35)

    # Return 0 to start playing the game, 1 to exit, 2 to return to main menu.
    def run(self):
        background = pygame.image.load('menu_image.jpg')

        welcome_message_font = pygame.font.Font("freesansbold.ttf", 25)
        welcome_message = welcome_message_font.render("Welcome to Sudoku! Click on <Play> to start the game.",
                                                      True, constants.BLACK)

        while self.running:
            self.screen.blit(background, (0, 0))
            self.screen.blit(welcome_message, (constants.WELCOME_MESSAGE_X, constants.WELCOME_MESSAGE_Y))

            self.play_button.draw(self.screen, self.button_font)
            self.exit_button.draw(self.screen, self.button_font)
            self.main_menu_button.draw(self.screen, self.button_font)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 1

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()

                    if self.exit_button.mouse_is_on_button(mouse_position):
                        self.running = False
                        return 1

                    if self.main_menu_button.mouse_is_on_button(mouse_position):
                        self.running = False
                        return 2

                    if self.play_button.mouse_is_on_button(mouse_position):
                        self.running = False
                        return 0
