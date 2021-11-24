from os import path
import pygame

from settings import COIN_HEIGHT, COIN_WIDTH, GHOST_HEIGHT, GHOST_WIDTH, IMG_DIR, PACMAN_HEIGHT, PACMAN_WIDTH

GHOST_IMG = 'ghost'
PACMAN_IMG = 'pacman'
COIN_IMG = 'coin'

def load_assets():
    assets = {}
    
    assets[GHOST_IMG] = pygame.image.load(path.join(IMG_DIR, 'ghost.png')).convert_alpha()
    assets[GHOST_IMG] = pygame.transform.scale(assets[GHOST_IMG], (GHOST_WIDTH, GHOST_HEIGHT))
    assets[PACMAN_IMG] = pygame.image.load(path.join(IMG_DIR, 'pacman.png')).convert_alpha()
    assets[PACMAN_IMG] = pygame.transform.scale(assets[PACMAN_IMG], (PACMAN_WIDTH, PACMAN_HEIGHT))
    assets[COIN_IMG] = pygame.image.load(path.join(IMG_DIR, 'coin.png')).convert_alpha()
    assets[COIN_IMG] = pygame.transform.scale(assets[COIN_IMG], (COIN_WIDTH, COIN_HEIGHT))

    return assets
