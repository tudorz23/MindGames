import pygame


class Button:
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.width = width
        self.height = height

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
        message = font.render(self.text, True, (255, 255, 255))
        screen.blit(message, (self.x + self.width / 8, self.y + self.height / 4))
