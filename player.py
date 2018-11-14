import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position

