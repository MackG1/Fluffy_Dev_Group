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

test_attacker = Attacker(500, 500)
sprites_list.add(test_attacker)

test_player = Player(50, 50)
sprites_list.add(test_player)

while carryOn:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            carryOn = False
    mouse_position = pygame.mouse.get_pos()
    test_player.rect.x = mouse_position[0]
    test_player.rect.y = mouse_position[1]
    test_attacker.move(test_player.rect.x, test_player.rect.y)
    screen.fill((0, 0, 0))
    sprites_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)

