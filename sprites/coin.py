import pygame

from settings import TILESIZE, COIN_WIDTH, COIN_HEIGHT

class Coin(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE + ((TILESIZE - COIN_WIDTH) // 2)
        self.rect.y = y * TILESIZE + ((TILESIZE - COIN_HEIGHT) // 2) 