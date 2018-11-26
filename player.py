import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.width = 20
        self.height = 20

        self.image = pygame.image.load("images/Buzz.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

        # Attack variables
        self.health = 30
        self.strength = 2

