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
COIN_WIDTH = 20
COIN_HEIGHT = 20
ghost_img = pygame.image.load(path.join(IMG_DIR, 'ghost.png')).convert_alpha()
ghost_img = pygame.transform.scale(ghost_img, (GHOST_WIDTH, GHOST_HEIGHT))
pacman_img = pygame.image.load(path.join(IMG_DIR, 'pacman.png')).convert_alpha()
pacman_img = pygame.transform.scale(pacman_img, (PACMAN_WIDTH, PACMAN_HEIGHT))
coin_img = pygame.image.load(path.join(IMG_DIR, 'coin.png')).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (COIN_WIDTH, COIN_HEIGHT))

    
class Pacman(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = img
        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        
        self.dx = 1
        self.dy = 0

    def move(self, dx=0, dy=0):
        if self.is_free_space(dx, dy) and self.is_in_bounds((dx, dy)):
            self.dx = dx
            self.dy = dy

            self.x += self.dx
            self.y += self.dy

    def is_free_space(self, dx=0, dy=0):
        for wall in all_walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return False
        
        return True

    def is_in_bounds(self, offset):
        dx, dy = offset

        final_x = self.x + dx
        final_y = self.y + dy

        return final_x > 0 and final_x < WIDTH and final_y > 0 and final_y < HEIGHT

    def update(self):
        self.adjust_image()

        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def adjust_image(self):        
        current_direction = (self.dx, self.dy)

        if (current_direction == (0, -1)):
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif (current_direction == (1, 0)):
            self.image = self.original_image
        elif (current_direction == (0, 1)):
            self.image = pygame.transform.rotate(self.original_image, -90)
        else:
            self.image = pygame.transform.flip(self.original_image, True, False)


class Ghost(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        # self.rect.x = random.randint(0, WIDTH-GHOST_WIDTH)
        # self.rect.y = random.randint(-100, -GHOST_HEIGHT)
        # self.rect.x = 0
        # self.rect.y = 0
        self.dx = -1
        self.dy = 0
        self.x = x
        self.y = y

        self.last_move = pygame.time.get_ticks()
        self.move_ticks = 300

    def move(self):
        if (not self.is_time_to_move()):
            return
        
        self.last_move = pygame.time.get_ticks()
        
        if (self.can_keep_moving()):
            self.x += self.dx
            self.y += self.dy
        else:
            self.move_randomly()
        
    def move_randomly(self):
        possible_moves = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)
        ]

        available_moves = list(filter(self.can_move, possible_moves))
        
        opposite_direction = (self.dx * -1, self.dy * -1)
        if (len(available_moves) > 1 and opposite_direction in available_moves):
            available_moves.remove(opposite_direction)

        if (len(available_moves) > 0):
            dx, dy = random.choice(available_moves)

            self.dx = dx
            self.dy = dy

            self.x = self.x + self.dx
            self.y = self.y + self.dy

    def is_time_to_move(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_move

        return elapsed_ticks >= self.move_ticks

    def update(self):
        self.move()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        
    def can_keep_moving(self):
        chance = random.random()

        return self.can_move((self.dx, self.dy)) and chance > 0.75

    def can_move(self, offset):
        return self.is_free_space(offset) and self.is_in_bounds(offset)
    
    def is_free_space(self, offset):
        dx, dy = offset
        
        for wall in all_walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return False
        
        return True
    
    def is_in_bounds(self, offset):
        dx, dy = offset

        final_x = self.x + dx
        final_y = self.y + dy

        return final_x > 0 and final_x < WIDTH and final_y > 0 and final_y < HEIGHT

class Coin(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE + ((TILESIZE - COIN_WIDTH) // 2)
        self.rect.y = y * TILESIZE + ((TILESIZE - COIN_HEIGHT) // 2) 
    
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
            player = Pacman(pacman_img, col, row)
            all_sprites.add(player)
            all_players.add(player)
        elif tile =='$':
            ghost = Ghost(ghost_img, col, row)
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