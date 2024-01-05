import pygame
import button
import constants


class EndGameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        self.play_again_button = button.Button(290, 300, 240, 50, constants.PURPLE, "Play Again")
        self.exit_button = button.Button(350, 400, 120, 50, constants.PURPLE, "Exit")
        self.button_font = pygame.font.Font("freesansbold.ttf", 35)

    # Return 0 to play again, 1 to exit.
    def run(self):
        background = pygame.image.load('menu_image.jpg')

        message_font = pygame.font.Font("freesansbold.ttf", 25)
        message = message_font.render("Thank you for playing! You are a sudoku master!",
                                      True, constants.BLACK)

        while self.running:
            self.screen.blit(background, (0, 0))
            self.screen.blit(message, (constants.ENDGAME_MESSAGE_X, constants.ENDGAME_MESSAGE_Y))

            self.play_again_button.draw(self.screen, self.button_font)
            self.exit_button.draw(self.screen, self.button_font)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 1

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()

                    if self.play_again_button.mouse_is_on_button(mouse_position):
                        self.running = False
                        return 0

                    if self.exit_button.mouse_is_on_button(mouse_position):
                        self.running = False
                        return 1
