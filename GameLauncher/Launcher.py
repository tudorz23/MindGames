import os
import sys
import pygame
from sudoku.main_sudoku import main as run_sudoku_game
from hangman.__main__ import main as run_hangman_game

class GameLauncher:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Game Launcher")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.background1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'background_image1.png'))
        self.background2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'background_image2.jpeg'))

        self.button1_rect = pygame.Rect(250, 150, 300, 200)
        self.button2_rect = pygame.Rect(250, 450, 300, 200)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            if pygame.display.get_surface():
                self.screen.fill((100, 100, 100))
                self.draw_buttons()

                pygame.display.update()

        pygame.quit()

    def handle_click(self, pos):
        if self.button1_rect.collidepoint(pos):
            self.launch_square1()
        elif self.button2_rect.collidepoint(pos):
            self.launch_square2()

    def launch_square1(self):
        pygame.init()
        run_hangman_game()

    def launch_square2(self):
        pygame.init()
        run_sudoku_game()

    def draw_buttons(self):
        # Draw button 1 rectangle
        pygame.draw.rect(self.screen, (52, 152, 219), self.button1_rect)

        # Background image for button 1
        background1_scaled = pygame.transform.scale(self.background1,
                                                    (self.button1_rect.width, self.button1_rect.height))
        self.screen.blit(background1_scaled, (self.button1_rect.x, self.button1_rect.y))

        # Draw button 2 rectangle
        pygame.draw.rect(self.screen, (46, 204, 113), self.button2_rect)

        # Background image for button 2
        background2_scaled = pygame.transform.scale(self.background2,
                                                    (self.button2_rect.width, self.button2_rect.height))
        self.screen.blit(background2_scaled, (self.button2_rect.x, self.button2_rect.y))


if __name__ == "__main__":
    launcher = GameLauncher()
    launcher.run()
