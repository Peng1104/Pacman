from os.path import join
from pygame.image import load
from pygame.transform import scale
from pygame.mixer import Sound
from pygame.font import Font
from settings import *

PACMAN_IMG = 'pacman'
COIN_IMG = 'coin'
GHOST_IMG = 'ghost'
PACMAN_LOGO = 'pacmanLogo'

MOVE_SND = 'move'
DEATH_SND = 'death'
MUSIC_SND = 'music'

SCORE_FONT = 'score_font'

def load_assets():

    assets = {}

    assets[PACMAN_IMG] = scale(load(join(IMG_DIR, 'pacman.png')).convert_alpha(), (PACMAN_WIDTH, PACMAN_HEIGHT)) # 32 x 32 pixels
    assets[PACMAN_LOGO] = scale(assets[PACMAN_IMG].copy(), (50, 50))
    assets[COIN_IMG] = scale(load(join(IMG_DIR, 'coin.png')).convert_alpha(), (COIN_WIDTH, COIN_HEIGHT)) # 20 x 20 pixels
    assets[GHOST_IMG] = scale(load(join(IMG_DIR, 'ghost.png')).convert_alpha(), (GHOST_WIDTH, GHOST_HEIGHT)) # 32 x 32 pixels

    # pygame.mixer.music.load(join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    
    assets[MOVE_SND] = Sound(join(SND_DIR, 'move.wav'))
    assets[DEATH_SND] = Sound(join(SND_DIR, 'death.wav'))
    assets[MUSIC_SND] = Sound(join(SND_DIR, 'music.wav'))

    assets[SCORE_FONT] = Font(join(FNT_DIR, 'PressStart2P.ttf'), FONT_SIZE)

    return assets