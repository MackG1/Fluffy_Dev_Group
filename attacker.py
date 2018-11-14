class Attacker(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.width = 20
        self.height = 20

        self.speed_x = 2

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
