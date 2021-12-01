import pygame

from os import path
from game_screen import game_screen
from init_screen import init_screen
from final_screen import final_screen
from win_screen import win_screen

from settings import *

# Função que identifica qual mapa foi escolhido
def get_level_path(name):
    level_map = {
        'Level 1': 'maps/map.txt',
        'Level 2': 'maps/map2.txt',
        'Level 3': 'maps/map3.txt'
    }

    return level_map[name]

# Carrega o conteúdo do arquivo do mapa
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
selected_level = None
while state != QUIT:
    if state == INIT:
        selected_level = init_screen(window)
        state = PLAYING
    elif state == PLAYING:
        map_path = get_level_path(selected_level)
        map_data = load_map(map_path)
        state = game_screen(window, map_data)
    elif state == GAMEOVER:
        state = final_screen(window)
    elif state == WIN:
        state = win_screen(window)

pygame.quit() 