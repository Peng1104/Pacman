from pygame.sprite import Sprite
from settings import TILESIZE

class BaseSprite(Sprite):
	
	def __init__(self, x, y, image, *groups): # x pos, y pos, Sprite image and groups
		super().__init__(groups) # Add to the given groups
		
		self.x = x
		self.y = y
		self.image = image

		self.rect = image.get_rect()
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE

	def update(self) -> bool:
		return False