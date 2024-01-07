import pygame

images = {}


def get_hangman_image(state: int):
    if state not in images:
        images[state] = pygame.image.load("assets/images/" + str(state) + ".png")
    return images[state]
