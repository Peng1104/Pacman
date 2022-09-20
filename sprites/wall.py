from pygame import Surface
from sprites.baseSprite import BaseSprite
from settings import TILESIZE, BLUE, WIDTH, HEIGHT
class Wall(BaseSprite):

	def __init__(self, x, y, group):
		super().__init__(x, y, Surface((TILESIZE, TILESIZE)), group)

		self.image.fill(BLUE)