import pygame
import random
import sys

pygame.init()

from os import path

from settings import *
WIDTH = 1024
HEIGHT = 768
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-man!')

GHOST_WIDTH = 50
GHOST_HEIGHT = 38
PACMAN_WIDTH = 50
PACMAN_HEIGHT = 38

background = pygame.image.load(path.join(IMG_DIR, 'background.jpg')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
ghost_img = pygame.image.load(path.join(IMG_DIR, 'ghost.png')).convert_alpha()
ghost_img = pygame.transform.scale(ghost_img, (GHOST_WIDTH, GHOST_HEIGHT))
pacman_img = pygame.image.load(path.join(IMG_DIR, 'pacman.png')).convert_alpha()
pacman_img = pygame.transform.scale(pacman_img, (PACMAN_WIDTH, PACMAN_HEIGHT))

class Pacman(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.x = x
        self.y = y
    
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0 

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ghost(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-GHOST_WIDTH)
        self.rect.y = random.randint(-100, -GHOST_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
    
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-GHOST_WIDTH)
            self.rect.y = random.randint(-100, -GHOST_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

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

clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
all_ghosts = pygame.sprite.Group()
all_walls = pygame.sprite.Group()

player = Pacman(pacman_img, 10, 10)
all_sprites.add(player)

for i in range(4):
    ghost = Ghost(ghost_img)
    all_sprites.add(ghost)
    all_ghosts.add(ghost)

for x in range(10,20):
    Wall(all_sprites, all_walls, x, 5)

# pygame.key.set_repeat(300, 250)

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= 1
            if event.key == pygame.K_RIGHT:
                player.x += 1
            if event.key == pygame.K_UP:
                player.y -= 1
            if event.key == pygame.K_DOWN:
                player.y += 1

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         player.x += 1
        #     if event.key == pygame.K_RIGHT:
        #         player.x  -= 1
        #     if event.key == pygame.K_UP:
        #         player.y  += 1
        #     if event.key == pygame.K_DOWN:
        #         player.y  -= 1

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, all_ghosts, True)

    if len(hits) > 0:
        game = False

    window.fill((0, 0, 0))  
    window.blit(background, (0, 0))

    all_sprites.draw(window)
    
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(window,GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(window,GREY, (0, y), (WIDTH, y))

    pygame.display.update() 

pygame.quit() 