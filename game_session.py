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
        icon = pygame.image.load('sudoku.png')
        pygame.display.set_icon(icon)

    # Runs the game.
    def run(self):
        while self.running:
            start_menu = initial_menu.InitialMenu(self.screen)
            if start_menu.run() == 1:
                self.running = False
                return

            main_game = game_runner.GameRunner(self.screen)
            if main_game.run() == 1:
                self.running = False
                return

            end_menu = end_game_menu.EndGameMenu(self.screen)
            if end_menu.run() == 1:
                self.running = False
                return
