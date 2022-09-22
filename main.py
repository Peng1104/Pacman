import pygame

from os import path
from screens.game import GameScreen
from screens.start import StartScreen, COLOR_INACTIVE, COLOR_LIST_INACTIVE
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

while state != QUIT:
    
    if state == INIT:
        screen = StartScreen(COLOR_INACTIVE, COLOR_LIST_INACTIVE, WIDTH/3.25, HEIGHT/3, 400, 100, window)
    
    elif state == PLAYING:
        screen = GameScreen(window, load_map(get_level_path(screen.level)), screen.level)
    
    elif state == GAMEOVER:
        screen = FinalScreen(window, screen.level)

    elif state == WIN:
        screen = WinScreen(window, screen.level)

    if screen is not None:
        actualState = state

        while actualState == state:
            screen.draw()
            state = screen.getNextState()
        
pygame.quit()