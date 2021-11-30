import pygame

from assets import COIN_IMG
from settings import TILESIZE, COIN_WIDTH, COIN_HEIGHT

# Criando a classe das moedas
class Coin(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[COIN_IMG]
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE + ((TILESIZE - COIN_WIDTH) // 2)
        self.rect.y = y * TILESIZE + ((TILESIZE - COIN_HEIGHT) // 2) 