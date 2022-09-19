from doctest import script_from_examples
import pygame

# from assets import MOVE_SND, load_assets
from assets import *
from settings import FPS, GAMEOVER, GREY, HEIGHT, QUIT, TILESIZE, WIDTH, WIN
from sprites.coin import Coin, COINS
from sprites.ghost import Ghost, GHOSTS
from sprites.pacman import Pacman
from sprites.wall import Wall, WALLS
from screens.baseScreen import BaseScreen

player = None

# Função que chama o carregamento dos assets e do mapa
def game_screen(window, map_data): 
    assets = load_assets()
    
    global player

    playerImg = assets[PACMAN_IMG]
    ghostImg = assets[GHOST_IMG]
    coinImg = assets[COIN_IMG]

    for x, tiles in enumerate(map_data):
        for y, tile in enumerate(tiles):
            if tile == '#':
                Wall(y, x)
            elif tile == '@':
                player = Pacman(y, x, playerImg)
            elif tile =='$':
                Ghost(y, x, ghostImg)
                Coin(y, x, coinImg)
            elif tile == '.':
                Coin(y, x, coinImg)

    if player == None:
        raise 'Mapa falho'

    return run(window, assets)

# Função que desenha as linhas do mapa
def draw_grid(window, color):
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(window, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(window, color, (0, y), (WIDTH, y))

# Função que executa o jogo
def run(window, assets):
    clock = pygame.time.Clock()
    pygame.key.set_repeat(300, 250)

    score = 0
    lives = 3

    PLAYING = 0
    COLLIDING = 1
    WAITING = 2

    global player

    state = WAITING

    assets[MUSIC_SND].play()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endGame()
                return QUIT
            
            if state is not COLLIDING and event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player.updateSpeed(dx=-1)
                    state = PLAYING
                
                elif event.key == pygame.K_RIGHT:
                    player.updateSpeed(dx=1)
                    state = PLAYING
                
                elif event.key == pygame.K_UP:
                    player.updateSpeed(dy=-1)
                    state = PLAYING
                
                elif event.key == pygame.K_DOWN:
                    player.updateSpeed(dy=1)
                    state = PLAYING
        
        if state is not WAITING:
            GHOSTS.update()
            player.update()

        if state == PLAYING:
            ghost_hits = pygame.sprite.spritecollide(player, GHOSTS, False)

            if len(ghost_hits) > 0:
                state = COLLIDING
                colliding_tick = pygame.time.get_ticks()
                colliding_duration = 300

            coin_hits = pygame.sprite.spritecollide(player, COINS, True)

            score += len(coin_hits) * 100

            if len(COINS) == 0:
                endGame()
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
                    
                    endGame()
                    return GAMEOVER
                else:
                    score -= 1000
                    state = WAITING
                    
                    player.reset()

                    for ghost in GHOSTS:
                        ghost.reset()
                    
        window.fill((0, 0, 0))

        WALLS.draw(window)
        COINS.draw(window)
        GHOSTS.draw(window)
        window.blit(player.image, (player.rect.x, player.rect.y))
        
        draw_grid(window, GREY)
        
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

def endGame() -> None:
    global player

    WALLS.empty()
    COINS.empty()
    GHOSTS.empty()
    player = None

    

#class GameScreen(BaseScreen):
    #__init__
