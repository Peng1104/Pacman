import pygame
import time

# from assets import MOVE_SND, load_assets
from assets import *
from settings import FPS, GAMEOVER, GREY, HEIGHT, QUIT, TILESIZE, WIDTH, WIN
from sprites.coin import Coin
from sprites.ghost import Ghost
from sprites.pacman import Pacman
from sprites.wall import Wall

# Função que chama o carregamento dos assets e do mapa
def game_screen(window, map_data): 
    assets = load_assets()
    sprites = build_map(assets, map_data)

    return run(window, sprites, assets)

# Função que cria o mapa
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
        raise 'Mapa falho'

    return sprites

# Função que desenha as linhas do mapa
def draw_grid(window, color):
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(window, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(window, color, (0, y), (WIDTH, y))

# Função que executa o jogo
def run(window, sprites, assets):
    clock = pygame.time.Clock()
    pygame.key.set_repeat(300, 250)

    player = sprites['player']

    score = 0
    lives = 2
    DONE = 0
    PLAYING = 1
    COLLIDING = 2

    state = PLAYING
    assets[MUSIC_SND].play()
    while state != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                return QUIT
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    # assets[MOVE_SND].play()
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
            ghost_hits = pygame.sprite.spritecollide(player, sprites['all_ghosts'], False)

            if len(ghost_hits) > 0:
                state = COLLIDING
                colliding_tick = pygame.time.get_ticks()
                colliding_duration = 300

            coin_hits = pygame.sprite.spritecollide(player, sprites['all_coins'], True)
            for coin in coin_hits:
                score += 100

            if len(sprites['all_coins']) == 0:
                state = DONE

                return WIN

        if state == COLLIDING:
            now = pygame.time.get_ticks()
            if now - colliding_tick > colliding_duration:
                assets[DEATH_SND].play()
                lives -= 1

                if lives == 0:
                    angle = 0
                    
                    for i in range(0, 72):
                        angle += 10
                        pacman_rotated, pacman_rotated_rect = player.rotate(angle)
                        window.blit(pacman_rotated, pacman_rotated_rect)
                        pygame.display.flip()
                        clock.tick(30)

                    state = DONE
                    return GAMEOVER
                else:
                    new_player = Pacman(assets, player.x, player.y, sprites['all_walls'])

                    player.kill()
                    score -= 1000

                    player = new_player
                    sprites['player'] = player
                    sprites['all_sprites'].add(player)
                    sprites['all_players'].add(player)

                    # time.sleep(1.5)
                    # state = DONE
            
                state = PLAYING
        
        window.fill((0, 0, 0))

        sprites['all_coins'].draw(window)
        sprites['all_players'].draw(window)
        sprites['all_ghosts'].draw(window)
        sprites['all_walls'].draw(window)
        
        draw_grid(window, color=GREY)
        
         # Desenhando o score
        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  (TILESIZE - FONT_SIZE) / 2 )
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets['score_font'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (TILESIZE,  (TILESIZE - FONT_SIZE) / 2)
        window.blit(text_surface, text_rect)

        pygame.display.update() 
