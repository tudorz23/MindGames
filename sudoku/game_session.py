import os

import pygame

from sudoku import end_game_menu
from sudoku import game_runner
from sudoku import initial_menu
from sudoku import constants
# from GameLauncher.Launcher import GameLauncher as run_main


class GameSession:
    def __init__(self):
        pygame.init()

        self.running = True

        self.screen = pygame.display.set_mode((constants.TOTAL_WIDTH, constants.TOTAL_HEIGHT))

        # Title and icon
        pygame.display.set_caption("Sudoku")
        icon_path = os.path.join(os.path.dirname(__file__), 'sudoku_icon.png')
        icon = pygame.image.load(icon_path)
        # icon = pygame.image.load('sudoku_icon.png')
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
                # # Close the Pygame display
                # pygame.display.quit()
                # # Initialize Pygame before running Sudoku game
                # pygame.init()
                # run_main()
                # # Clean up Pygame after running Sudoku game
                # pygame.quit()
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
