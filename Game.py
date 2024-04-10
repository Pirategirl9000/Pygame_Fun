import pygame
import numpy as np
from Player import *
from Enemy import *
from Matrixical_Navigation import Np_array_nav as nav
from Map import *


pygame.init
clock = pygame.time.Clock()
map_renderer = Map(file_name="map.png", binary=True, alpha=False, grey_scale=True, binary_light_value=0, binary_dark_value=1)
map = map_renderer.get_map()
screen = pygame.display.set_mode((720, 720))
running = True

player = Player()

while player.get_alive():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()