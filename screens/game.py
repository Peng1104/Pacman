from doctest import script_from_examples
from multiprocessing.connection import wait
import pygame

# from assets import MOVE_SND, load_assets
from assets import *
from settings import FPS, GAMEOVER, GREY, HEIGHT, QUIT, TILESIZE, WIDTH, WIN, PLAYING, WAITING, COLLIDING
from sprites.coin import Coin
from sprites.ghost import Ghost
from sprites.pacman import Pacman
from sprites.wall import Wall
from screens.baseScreen import BaseScreen
from pygame.sprite import Group 

class GameScreen(BaseScreen):
    
    def __init__(self, window, mapData) -> None:
        super().__init__(window)

        self.score = 0
        self.lives = 3

        self.assets = load_assets()

        self.walls = Group()
        self.coins = Group()
        self.ghosts = Group()
        self.player = None

        self.__loadMap(mapData)
        
    def __loadMap(self, mapData) -> None:
        playerImg = self.assets[PACMAN_IMG]
        ghostImg = self.assets[GHOST_IMG]
        coinImg = self.assets[COIN_IMG]
        
        for x, tiles in enumerate(mapData):
            for y, tile in enumerate(tiles):
                if tile == '#':
                    Wall(y, x, self.walls)
                elif tile == '@':
                    self.player = Pacman(y, x, playerImg, self)
                elif tile =='$':
                    Ghost(y, x, ghostImg, self.ghosts, self)
                    Coin(y, x, coinImg, self.coins)
                elif tile == '.':
                    Coin(y, x, coinImg, self.coins)
        
        if self.player == None:
            raise Exception('Player not found')

    def canMoveTo(self, x, y) -> bool:
        if x <= 0 or y <= 0 or x >= WIDTH or y >= HEIGHT:
            return False
            
        for wall in self.walls:
            if wall.inside(x, y):
                return False
        
        return True
    
    def draw(self) -> None:
        self.window.fill((0, 0, 0))

        self.__drawSprites()
        self.__drawGrid()
        self.__drawScore()
        self.__drawLives()

        pygame.display.update()

    def __drawSprites(self) -> None:
        self.walls.draw(self.window)
        self.coins.draw(self.window)
        self.ghosts.draw(self.window)
        self.player.draw(self.window)
    
    def __drawGrid(self) -> None:
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.window, GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.window, GREY, (0, y), (WIDTH, y))

    def __drawScore(self) -> None:
        text_surface = self.assets['score_font'].render("{:08d}".format(self.score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  (TILESIZE - FONT_SIZE) / 2 )
        self.window.blit(text_surface, text_rect)
    
    def __drawLives (self) -> None:
        text_surface = self.assets['score_font'].render(chr(9829) * self.lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (TILESIZE,  (TILESIZE - FONT_SIZE) / 2)
        self.window.blit(text_surface, text_rect)

    def getNextState(self) -> int:
        self.assets[MUSIC_SND].play()

        for event in pygame.event.get():

            state = WAITING
            if event.type == pygame.QUIT:
                __endGame()
                return QUIT
            
            if state is not COLLIDING and event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    self.player.updateSpeed(dx=-1)
                    state = PLAYING
                
                elif event.key == pygame.K_RIGHT:
                    self.player.updateSpeed(dx=1)
                    state = PLAYING
                
                elif event.key == pygame.K_UP:
                    self.player.updateSpeed(dy=-1)
                    self.state = PLAYING
                
                elif event.key == pygame.K_DOWN:
                    self.player.updateSpeed(dy=1)
                    state = PLAYING
        
        if state is not WAITING:
            self.ghosts.update()
            self.player.update()

        if state == PLAYING:
            ghost_hits = pygame.sprite.spritecollide(self.player, self.ghosts, False)

            if len(ghost_hits) > 0:
                state = COLLIDING
                colliding_tick = pygame.time.get_ticks()
                colliding_duration = 300

            coin_hits = pygame.sprite.spritecollide(self.player, self.coins, True)

            self.score += len(coin_hits) * 100

            if len(self.coins) == 0:
                __endGame()
                return WIN
        
        if state == COLLIDING:
            now = pygame.time.get_ticks()
            
            if now - colliding_tick > colliding_duration:
                self.assets[DEATH_SND].play()
                self.lives -= 1

                if self.lives == 0:
                    angle = 0
                    
                    for i in range(0, 72):
                        angle += 10
                        pacman_rotated, pacman_rotated_rect = self.player.rotate(angle)
                        self.window.blit(pacman_rotated, pacman_rotated_rect)
                        pygame.display.flip()
                    
                    __endGame()
                    return GAMEOVER
                else:
                    self.score -= 1000
                    state = WAITING
                    
                    self.player.reset()

                    for ghost in self.ghosts:
                        ghost.reset()
        
        def __endGame(self) -> None:

            self.walls.empty()
            self.coins.empty()
            self.ghosts.empty()
            self.player = None