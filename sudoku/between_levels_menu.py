import pygame
import button
import constants


class BetweenLevelsMenu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Buttons
        self.next_level_button = button.Button(350, 300, 120, 50, constants.PURPLE, "Next")
        self.exit_button = button.Button(350, 400, 120, 50, constants.PURPLE, "Exit")
        self.button_font = pygame.font.Font("freesansbold.ttf", 35)

    # Return 0 to continue playing the game, 1 to exit.
    def run(self):
        background = pygame.image.load('menu_image.jpg')

        # Message.
        message_font = pygame.font.Font("freesansbold.ttf", 25)
        message = message_font.render("Congratulations! You can now access the next level:",
                                      True, constants.BLACK)

        while self.running:
            self.screen.fill(constants.BLACK)
            self.screen.blit(background, (0, 0))
            self.screen.blit(message, (constants.FINISH_LEVEL_MESSAGE_X, constants.FINISH_LEVEL_MESSAGE_Y))

            self.next_level_button.draw(self.screen, self.button_font)
            self.exit_button.draw(self.screen, self.button_font)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 1

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()

                    if self.next_level_button.mouse_is_on_button(mouse_position):
                        self.running = False
                        return 0

                    if self.exit_button.mouse_is_on_button(mouse_position):
                        self.running = False
                        return 1
