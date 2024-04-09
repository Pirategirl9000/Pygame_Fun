import pygame
import numpy as np
from Player import *
from Enemy import *
import Matrixical_Navigation as nav
from Map import *


pygame.init
clock = pygame.time.Clock()
map_renderer = Map(file_name="map.png", binary=True, alpha=False)
map = map_renderer.get_map()
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