import pygame
import random
import sys
import time

pygame.init()

from os import path

from settings import *
WIDTH = 1024
HEIGHT = 768
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-man!')

GHOST_WIDTH = TILESIZE
GHOST_HEIGHT = TILESIZE
PACMAN_WIDTH = TILESIZE
PACMAN_HEIGHT = TILESIZE

ghost_img = pygame.image.load(path.join(IMG_DIR, 'ghost.png')).convert_alpha()
ghost_img = pygame.transform.scale(ghost_img, (GHOST_WIDTH, GHOST_HEIGHT))
pacman_img = pygame.image.load(path.join(IMG_DIR, 'pacman.png')).convert_alpha()
pacman_img = pygame.transform.scale(pacman_img, (PACMAN_WIDTH, PACMAN_HEIGHT))

    
class Pacman(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0 

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def collide_with_walls(self, dx=0, dy=0):
        for wall in all_walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Ghost(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        # self.rect.x = random.randint(0, WIDTH-GHOST_WIDTH)
        # self.rect.y = random.randint(-100, -GHOST_HEIGHT)
        self.rect.x = 0
        self.rect.y = 0
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(2, 9)
        self.x = x
        self.y = y

    def move(self):

        if not self.collide_with_walls():
            self.x += self.dx
            self.y += self.dy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-GHOST_WIDTH)
            self.rect.y = random.randint(-100, -GHOST_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    def collide_with_walls(self):
        for wall in all_walls:
            if wall.x == self.x + self.dx and wall.y == self.y + self.dy:
                return True
        
        return False

class Wall(pygame.sprite.Sprite):
    def __init__(self, all_sprites, all_walls, x, y):
        self.groups = all_sprites, all_walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE      
game = True

game_folder = path.dirname(__file__)
map_data = []
with open(path.join(game_folder, 'map.txt'), 'rt') as f:
    for line in f:
        map_data.append(line)

clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
all_ghosts = pygame.sprite.Group()
all_walls = pygame.sprite.Group()

player = None

for row, tiles in enumerate(map_data):
    for col, tile in enumerate(tiles):
        if tile == '#':
            wall = Wall(all_sprites, all_walls, col, row)
            all_sprites.add(wall)
            all_walls.add(wall)
        if tile == '@':
            player = Pacman(pacman_img, col, row)
            all_sprites.add(player)
        if tile =='$':
            ghost = Ghost(ghost_img, col, row)
            all_sprites.add(ghost)
            all_ghosts.add(ghost)
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

    # for ghost in all_ghosts:
    #     ghost.move()
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, all_ghosts, True)

    if len(hits) > 0:
        game = False

    window.fill((0, 0, 0))

    all_sprites.draw(window)
    
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(window,GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(window,GREY, (0, y), (WIDTH, y))

    pygame.display.update() 

pygame.quit() 