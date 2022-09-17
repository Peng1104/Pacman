import pygame
from settings import TILESIZE
from Wall import canMoveTo

class BaseSprite(pygame.sprite.Sprite):
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

class MoveableSprite(BaseSprite):
	
	def __init__(self, x, y, image, *groups):
		super().__init__(x, y, image, groups)
		
		self.dx = 0
		self.dy = 0
	
	def teleport(self, x, y) -> bool:
		if canMoveTo(x, y):
			self.x = x
			self.y = y

			self.dx = 0
			self.dy = 0

			return self.update()
		
		return False
	
	def updateSpeed(self, dx, dy) -> None:
		self.dx = dx
		self.dy = dy

	def update(self) -> bool:
		if canMoveTo(self.x + self.dx, self.y + self.dy): # Check if can move to the new position
			self.x += self.dx
			self.y += self.dy

			self.rect.x = self.x * TILESIZE
			self.rect.y = self.y * TILESIZE

			return True
		
		return False