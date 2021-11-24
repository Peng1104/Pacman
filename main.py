import pygame

from os import path
from game_screen import game_screen
from init_screen import init_screen

from settings import *

def load_map(map_path):
    game_folder = path.dirname(__file__)
    
    map_data = []
    with open(path.join(game_folder, map_path), 'rt') as f:
        for line in f:
            map_data.append(line)
    
    return map_data

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-man!')

state = INIT
while state != QUIT:
    if state == INIT:
        # state = init_screen(window)
        state = GAME
    elif state == GAME:
        map_data = load_map('maps/map3.txt')
        state = game_screen(window, map_data)
    else:
        state = QUIT

pygame.quit() 