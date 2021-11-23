import pygame

from sprites.pacman import Pacman
from sprites.ghost import Ghost
from sprites.wall import Wall
from sprites.coin import Coin

pygame.init()

from os import path

from settings import *
WIDTH = 1024
HEIGHT = 768
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-man!')

ghost_img = pygame.image.load(path.join(IMG_DIR, 'ghost.png')).convert_alpha()
ghost_img = pygame.transform.scale(ghost_img, (GHOST_WIDTH, GHOST_HEIGHT))
pacman_img = pygame.image.load(path.join(IMG_DIR, 'pacman.png')).convert_alpha()
pacman_img = pygame.transform.scale(pacman_img, (PACMAN_WIDTH, PACMAN_HEIGHT))
coin_img = pygame.image.load(path.join(IMG_DIR, 'coin.png')).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (COIN_WIDTH, COIN_HEIGHT))
    
game = True

game_folder = path.dirname(__file__)
map_data = []
with open(path.join(game_folder, 'map.txt'), 'rt') as f:
    for line in f:
        map_data.append(line)

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group() 
all_players = pygame.sprite.Group()
all_ghosts = pygame.sprite.Group()
all_walls = pygame.sprite.Group()
all_coins = pygame.sprite.Group()

player = None

for row, tiles in enumerate(map_data):
    for col, tile in enumerate(tiles):
        if tile == '#':
            wall = Wall(all_sprites, all_walls, col, row)
            all_sprites.add(wall)
            all_walls.add(wall)
        elif tile == '@':
            player = Pacman(pacman_img, col, row, all_walls)
            all_sprites.add(player)
            all_players.add(player)
        elif tile =='$':
            ghost = Ghost(ghost_img, col, row, all_walls)
            all_sprites.add(ghost)
            all_ghosts.add(ghost)
        elif tile == '.':
            coin = Coin(coin_img, col, row)
            all_sprites.add(coin)
            all_coins.add(coin)

if player == None:
    raise 'Mapa ruim'

pygame.key.set_repeat(300, 250)

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(dx = -1) 
            if event.key == pygame.K_RIGHT:
                player.move(dx = 1)
            if event.key == pygame.K_UP:
                player.move(dy = -1)
            if event.key == pygame.K_DOWN:
                player.move(dy = 1)

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, all_ghosts, True)

    if len(hits) > 0:
        game = False

    hits = pygame.sprite.spritecollide(player, all_coins, True)
    if len(all_coins) == 0:
        game = False
    window.fill((0, 0, 0))

    # all_sprites.draw(window)

    all_coins.draw(window)
    all_players.draw(window)
    all_ghosts.draw(window)
    all_walls.draw(window)
    
    
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(window,GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(window,GREY, (0, y), (WIDTH, y))

    pygame.display.update() 

pygame.quit() 