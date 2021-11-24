from os import path

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

BLUE = (0, 0, 150)
GREY = (100, 100, 100)


WIDTH = 1024
HEIGHT = 768
FPS = 60

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = WIDTH / TILESIZE

GHOST_WIDTH = TILESIZE
GHOST_HEIGHT = TILESIZE
PACMAN_WIDTH = TILESIZE
PACMAN_HEIGHT = TILESIZE
COIN_WIDTH = 20
COIN_HEIGHT = 20

INIT = 0
GAME = 1
QUIT = 2
