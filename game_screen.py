import pygame

from assets import load_assets
from settings import FPS, GREY, HEIGHT, TILESIZE, WIDTH
from sprites.coin import Coin
from sprites.ghost import Ghost
from sprites.pacman import Pacman
from sprites.wall import Wall

def game_screen(window, map_data): 
    assets = load_assets()
    sprites = build_map(assets, map_data)

    run(window, sprites)

def build_map(assets, map_data):
    sprites = {
        'all_sprites': pygame.sprite.Group(),
        'all_players': pygame.sprite.Group(),
        'all_ghosts': pygame.sprite.Group(),
        'all_walls': pygame.sprite.Group(),
        'all_coins': pygame.sprite.Group(),
    }

    player = None

    for row, tiles in enumerate(map_data):
        for col, tile in enumerate(tiles):
            if tile == '#':
                wall = Wall(sprites['all_sprites'], sprites['all_walls'], col, row)
                sprites['all_sprites'].add(wall)
                sprites['all_walls'].add(wall)
            elif tile == '@':
                player = Pacman(assets, col, row, sprites['all_walls'])
                sprites['player'] = player
                sprites['all_sprites'].add(player)
                sprites['all_players'].add(player)
            elif tile =='$':
                ghost = Ghost(assets, col, row, sprites['all_walls'])
                sprites['all_sprites'].add(ghost)
                sprites['all_ghosts'].add(ghost)
            elif tile == '.':
                coin = Coin(assets, col, row)
                sprites['all_sprites'].add(coin)
                sprites['all_coins'].add(coin)

    if player == None:
        raise 'Mapa ruim'

    return sprites

def draw_grid(window, color):
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(window, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(window, color, (0, y), (WIDTH, y))

def run(window, sprites):
    clock = pygame.time.Clock()
    pygame.key.set_repeat(300, 250)

    player = sprites['player']

    DONE = 0
    PLAYING = 1
    state = PLAYING

    while state != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.move(dx = -1) 
                    if event.key == pygame.K_RIGHT:
                        player.move(dx = 1)
                    if event.key == pygame.K_UP:
                        player.move(dy = -1)
                    if event.key == pygame.K_DOWN:
                        player.move(dy = 1)

        sprites['all_sprites'].update()

        if state == PLAYING:
            ghost_hits = pygame.sprite.spritecollide(player, sprites['all_ghosts'], True)

            if len(ghost_hits) > 0:
                state = DONE

            pygame.sprite.spritecollide(player, sprites['all_coins'], True)
            if len(sprites['all_coins']) == 0:
                state = DONE
        
        window.fill((0, 0, 0))

        sprites['all_coins'].draw(window)
        sprites['all_players'].draw(window)
        sprites['all_ghosts'].draw(window)
        sprites['all_walls'].draw(window)
        
        draw_grid(window, color=GREY)

        pygame.display.update() 
