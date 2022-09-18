from pygame.sprite import Group
from sprites.baseSprite import BaseSprite
from settings import TILESIZE, COIN_WIDTH, COIN_HEIGHT

COINS = Group() # Grupo contento todas as moedas

# A Classe das moedas
class Coin(BaseSprite):

	def __init__(self, x, y, img):
		super().__init__(x, y, img, COINS)
		self.rect.x = x * TILESIZE + (TILESIZE - COIN_WIDTH) // 2
		self.rect.y = y * TILESIZE + (TILESIZE - COIN_HEIGHT) // 2