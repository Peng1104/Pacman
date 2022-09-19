from types import DynamicClassAttribute
import pygame

from os import path
from screens.game import game_screen
from screens.init import init_screen
from screens.final import FinalScreen
from screens.win import WinScreen

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
pygame.mixer.music.set_volume(0.4)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-man!')

state = INIT
screen = None
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
        screen = FinalScreen(window)

        while state == GAMEOVER:
            screen.draw()
            state = screen.getNextState()

    elif state == WIN:
        state = WinScreen(window)

pygame.quit()