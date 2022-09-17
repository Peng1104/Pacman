from pygame.time import get_ticks
from sprites.wall import canMoveTo
from sprites.baseSprite import BaseSprite
from settings import TILESIZE

class MoveableSprite(BaseSprite):
	
	def __init__(self, x, y, image, moveDelay=60, *groups):
		super().__init__(x, y, image, groups)
		
		self.moveDelay = moveDelay
		self.lastMovementTime = get_ticks()

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
	
	def updateSpeed(self, dx=0, dy=0) -> None:
		self.dx = dx
		self.dy = dy

	def update(self) -> bool:
		if (get_ticks() - self.lastMovementTime) >= self.moveDelay and canMoveTo(self.x + self.dx, self.y + self.dy):
			self.lastMovementTime = get_ticks()

			self.x += self.dx
			self.y += self.dy

			self.rect.x = self.x * TILESIZE
			self.rect.y = self.y * TILESIZE

			return True
		
		return False