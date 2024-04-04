import pygame
from Player import *
from Enemy import *

pygame.init
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
running = True

player = Player()

while player.get_alive():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()