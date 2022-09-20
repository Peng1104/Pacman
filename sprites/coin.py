from sprites.baseSprite import BaseSprite
from settings import TILESIZE, COIN_WIDTH, COIN_HEIGHT
class Coin(BaseSprite):

	def __init__(self, x, y, img, *groups):
		super().__init__(x, y, img, groups)
		self.rect.x = x * TILESIZE + (TILESIZE - COIN_WIDTH) // 2
		self.rect.y = y * TILESIZE + (TILESIZE - COIN_HEIGHT) // 2