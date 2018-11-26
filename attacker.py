import pygame


class Attacker(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.width = 20
        self.height = 20

        self.speed = 3

        self.image = pygame.image.load("images/Piggies.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

        # For combat
        self.alive = True
        self.health = 10
        self.strength = 2
        self.last_move_x = 0
        self.last_move_y = 0

    def move(self, player_x, player_y):
        if self.alive:
            delta_x = player_x - self.rect.x

            if delta_x <= 0:
                x_direction = -1
            else:
                x_direction = 1

            delta_y = player_y - self.rect.y

            if delta_y <= 0:
                y_direction = -1
            else:
                y_direction = 1

            if abs(delta_x) > abs(delta_y):
                x_movement = 2
                y_movement = 0
            elif abs(delta_x) < abs(delta_y):
                y_movement = 2
                x_movement = 0
            else:
                y_movement = 1
                x_movement = 1

            self.rect.x += (x_direction * x_movement)
            self.rect.y += (y_direction * y_movement)
            self.last_move_x = x_direction * x_movement
            self.last_move_y = y_direction * y_movement

    def attack(self):
        print("hit")






