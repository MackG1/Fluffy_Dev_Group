import pygame


class Attacker(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.width = 20
        self.height = 20

        self.speed = 3

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def move(self, player_x, player_y):
        try:
            delta_x = player_x - self.rect.x
        except ZeroDivisionError:
            delta_x = 0

        if delta_x < 0:
            x_direction = -1
        else:
            x_direction = 1

        try:
            delta_y = player_y - self.rect.y
        except ZeroDivisionError:
            delta_y = 0

        if delta_y < 0:
            y_direction = -1
        else:
            y_direction = 1

        delta_total = delta_x + delta_y
        try:
            x_movement = int(self.speed * (delta_x/delta_total))
        except ZeroDivisionError:
            x_movement = 0

        try:
            y_movement = int(self.speed * (delta_y/delta_total))
        except ZeroDivisionError:
            y_movement = 0
        self.rect.x += (x_direction * x_movement)
        self.rect.y += (y_direction * y_movement)






