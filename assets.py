from os import path
import pygame

from settings import COIN_HEIGHT, COIN_WIDTH, GHOST_HEIGHT, GHOST_WIDTH, IMG_DIR, SND_DIR, FNT_DIR, PACMAN_HEIGHT, PACMAN_WIDTH, FONT_SIZE

GHOST_IMG = 'ghost'
PACMAN_IMG = 'pacman'
COIN_IMG = 'coin'

MOVE_SND = 'move'
DEATH_SND = 'death'
MUSIC_SND = 'music'

SCORE_FONT = 'score_font'

def load_assets():
    assets = {}
    
    assets[GHOST_IMG] = pygame.image.load(path.join(IMG_DIR, 'ghost.png')).convert_alpha()
    assets[GHOST_IMG] = pygame.transform.scale(assets[GHOST_IMG], (GHOST_WIDTH, GHOST_HEIGHT))
    assets[PACMAN_IMG] = pygame.image.load(path.join(IMG_DIR, 'pacman.png')).convert_alpha()
    assets[PACMAN_IMG] = pygame.transform.scale(assets[PACMAN_IMG], (PACMAN_WIDTH, PACMAN_HEIGHT))
    assets[COIN_IMG] = pygame.image.load(path.join(IMG_DIR, 'coin.png')).convert_alpha()
    assets[COIN_IMG] = pygame.transform.scale(assets[COIN_IMG], (COIN_WIDTH, COIN_HEIGHT))

    # pygame.mixer.music.load(path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[MOVE_SND] = pygame.mixer.Sound(path.join(SND_DIR, 'move.wav'))
    assets[DEATH_SND] = pygame.mixer.Sound(path.join(SND_DIR, 'death.wav'))
    assets[MUSIC_SND] = pygame.mixer.Sound(path.join(SND_DIR, 'music.wav'))

    assets[SCORE_FONT] = pygame.font.Font(path.join(FNT_DIR, 'PressStart2P.ttf'), FONT_SIZE)

    return assets
