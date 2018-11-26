import pygame
from attacker import Attacker
from player import Player

# initialize and setup pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
level = 1
attack_list = []

# Clock used for FPS
clock = pygame.time.Clock()
# list of everything that will be displayed on screen
sprites_list = pygame.sprite.Group()
attackers = pygame.sprite.Group()
players = pygame.sprite.Group()
carryOn = True

# For Debugging
test_attacker = Attacker(500, 500)
sprites_list.add(test_attacker)
attackers.add(test_attacker)
# For Debugging
player = Player(50, 50)
sprites_list.add(player)
players.add(player)

# -------------------------Main Loop------------------------------->
while carryOn:
    # -----------------Pygame events---------------->
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                test_attacker.alive = False

    # ------------------Game Logic ----------------->
    mouse_position = pygame.mouse.get_pos()
    player.rect.x = mouse_position[0]
    player.rect.y = mouse_position[1]
    test_attacker.move(player.rect.x, player.rect.y)
    screen.fill((0, 0, 0))

    for player in players:
        attack_list = pygame.sprite.spritecollide(player, attackers, False)

    for x in attack_list:
        x.attack()

    sprites_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)

