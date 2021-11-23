import pygame

from settings import TILESIZE, BLUE

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