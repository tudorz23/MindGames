import pygame

import end_game_menu
import game_runner
import initial_menu
import constants


class GameSession:
    def __init__(self):
        pygame.init()

        self.running = True

        self.screen = pygame.display.set_mode((constants.TOTAL_WIDTH, constants.TOTAL_HEIGHT))

        # Title and icon
        pygame.display.set_caption("Sudoku")
        icon = pygame.image.load('sudoku_icon.png')
        pygame.display.set_icon(icon)

    # Runs the game.
    # Return 1 to exit, 0 to return to main menu.
    def run(self):
        while self.running:
            start_menu = initial_menu.InitialMenu(self.screen)
            start_choice = start_menu.run()
            if start_choice == 1:
                self.running = False
                return 1
            elif start_choice == 2:
                self.running = False
                return 0

            main_game = game_runner.GameRunner(self.screen)
            if main_game.run() == 1:
                self.running = False
                return 1

            end_menu = end_game_menu.EndGameMenu(self.screen)
            if end_menu.run() == 1:
                self.running = False
                return 1
