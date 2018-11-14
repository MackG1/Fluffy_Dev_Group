import pygame
from attacker import Attacker
from player import Player

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
sprites_list = pygame.sprite.Group()

carryOn = True

cat = Attacker(50, 50)
sprites_list.add(cat)

while carryOn:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            carryOn = False

    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

