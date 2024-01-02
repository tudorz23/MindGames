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
        #message_rect = message.get_rect()
        #message_rect.center(self.x + self.width / 2, self.y + self.height / 2)
        #screen.blit(message, message_rect)
        screen.blit(message, (self.x + self.width / 8, self.y + self.height / 4))

    def mouse_is_on_button(self, mouse_position):
        if (self.x <= mouse_position[0] <= self.x + self.width
                and self.y <= mouse_position[1] <= self.y + self.height):
            return True
        return False
