import os

import pygame

images = {}


def get_hangman_image(state: int):
    image_path = os.path.join(os.path.dirname(__file__), 'images', '.')
    if state not in images:
        images[state] = pygame.image.load(image_path + "\\" + str(state) + ".png")
    return images[state]
